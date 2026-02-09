"""Video and subtitle downloading, output path logic, and directory creation."""

from __future__ import annotations

import contextlib
import logging
import re
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

if TYPE_CHECKING:
    from pathlib import Path

from fosdem_video.images import copy_season_images, copy_show_images, get_assets_dir
from fosdem_video.models import (
    HTTP_NOT_FOUND,
    HTTP_OK,
    Talk,
    display_name,
    sanitise_path_component,
)
from fosdem_video.nfo import write_episode_nfo, write_season_nfo, write_tvshow_nfo

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Sensible defaults to avoid overloading FOSDEM's volunteer-run infrastructure
# ---------------------------------------------------------------------------
DEFAULT_WORKERS = 2
DEFAULT_DELAY: float = 1.0  # seconds between each download per worker
USER_AGENT = (
    "fosdem-video-downloader/0.1.0 (+https://github.com/butlerx/fosdem-video-downloader)"
)

# Retry strategy: back off on 429 (rate-limit) and server errors (500-503)
_RETRY_STRATEGY = Retry(
    total=3,
    backoff_factor=2,  # 0s, 2s, 4s
    status_forcelist=[429, 500, 502, 503],
    allowed_methods=["GET"],
    raise_on_status=False,
)


def _build_session() -> requests.Session:
    """Create a :class:`requests.Session` with retry and a polite User-Agent."""
    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT
    adapter = HTTPAdapter(max_retries=_RETRY_STRATEGY)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def download_video(
    url: str,
    output_path: Path,
    session: requests.Session | None = None,
) -> bool:
    """Download a video from a URL to the specified output path."""
    _session = session or _build_session()
    try:
        logger.info("Starting download: %s", output_path.name)
        response = _session.get(url, stream=True, timeout=30)
        if response.status_code == HTTP_NOT_FOUND:
            logger.warning("Video not found (404): %s", url)
            return False
        if response.status_code != HTTP_OK:
            response.raise_for_status()

        total_size = int(response.headers.get("content-length", 0))
        logger.debug("%s is %d MB", output_path.name, total_size)
        block_size = 1024 * 1024  # 1MB chunks

        with output_path.open("wb") as f:
            f.writelines(response.iter_content(block_size))

        logger.info("Downloaded %s", output_path.name)
    except Exception:
        logger.exception("Failed to download %s", url)
        with contextlib.suppress(FileNotFoundError):
            # If something happened mid download we should remove the incomplete file
            output_path.unlink()
        return False

    return True


def download_vtt(
    video_url: str,
    output_path: Path,
    session: requests.Session | None = None,
) -> bool:
    """
    Download a VTT subtitle file corresponding to a video URL.

    Replaces the video extension with .vtt. Logs a warning and returns False
    if the subtitle is not found (404).
    """
    _session = session or _build_session()
    # Strip the format extension and replace with .vtt
    vtt_url = re.sub(r"\.(mp4|av1\.webm)$", ".vtt", video_url)
    vtt_path = output_path.with_suffix(".vtt")
    try:
        logger.debug("Downloading subtitle: %s", vtt_url)
        response = _session.get(vtt_url, stream=True, timeout=30)
        if response.status_code == HTTP_NOT_FOUND:
            logger.warning("Subtitle not found (404): %s", vtt_url)
            return False
        if response.status_code != HTTP_OK:
            response.raise_for_status()
        with vtt_path.open("wb") as f:
            f.writelines(response.iter_content(1024 * 1024))
        logger.debug("Downloaded subtitle %s", vtt_path.name)
    except Exception:
        logger.exception("Failed to download subtitle %s", vtt_url)
        with contextlib.suppress(FileNotFoundError):
            vtt_path.unlink()
        return False
    return True


def get_output_path(
    output_dir: Path,
    talk: Talk,
    fmt: str,
    *,
    jellyfin: bool = False,
    episode_index: dict[str, tuple[int, int]] | None = None,
) -> Path:
    """
    Return the file path for a downloaded video or subtitle.

    Args:
        output_dir: Root output directory.
        talk: The Talk object.
        fmt: Video format extension (e.g. "mp4" or "av1.webm").
        jellyfin: When True, use Jellyfin-compatible folder structure.
        episode_index: Mapping of ``talk.id`` to ``(season_number,
            episode_number)``.  When provided in Jellyfin mode the
            season folder uses ``Season <nn>`` and the episode folder
            and file use ``FOSDEM <year> S<ss>E<ee> <title>``.

    """
    if jellyfin:
        ep_info = (episode_index or {}).get(talk.id)
        if ep_info:
            season_num, ep_num = ep_info
            season_folder = sanitise_path_component(talk.track)
            name = sanitise_path_component(
                display_name(talk, ep_num, season_num),
            )
        else:
            season_folder = sanitise_path_component(
                talk.track if talk.track else talk.location,
            )
            name = talk.id
        return (
            output_dir / f"Fosdem ({talk.year})" / season_folder / name / f"{name}.{fmt}"
        )
    return output_dir / talk.year / f"{talk.id}.{fmt}"


def is_downloaded(
    output_dir: Path,
    talk: Talk,
    fmt: str,
    *,
    jellyfin: bool = False,
    episode_index: dict[str, tuple[int, int]] | None = None,
) -> bool:
    """Check if the video file already exists."""
    file_path = get_output_path(
        output_dir,
        talk,
        fmt,
        jellyfin=jellyfin,
        episode_index=episode_index,
    )
    if file_path.exists():
        logger.debug("skipping %s as the file already exists", talk.id)
        return True
    return False


def create_dirs(
    output_dir: Path,
    talks: list[Talk],
    *,
    jellyfin: bool = False,
    episode_index: dict[str, tuple[int, int]] | None = None,
) -> None:
    """
    Create output directories for each talk.

    When *jellyfin* is True and talks carry rich metadata (year mode), this
    also writes ``tvshow.nfo`` in the show root and ``season.nfo`` in each
    track directory so that Jellyfin recognises the folder hierarchy as a
    TV series.
    """
    has_metadata = jellyfin and any(t.title for t in talks)
    show_dir_written: set[str] = set()
    season_dirs_written: set[str] = set()

    for talk in talks:
        folder = get_output_path(
            output_dir,
            talk,
            "mp4",
            jellyfin=jellyfin,
            episode_index=episode_index,
        ).parent
        folder.mkdir(parents=True, exist_ok=True)

        if not has_metadata:
            continue

        # Write tvshow.nfo once per show root
        show_dir = folder.parent.parent  # …/Fosdem (<year>)/
        show_key = str(show_dir)
        if show_key not in show_dir_written:
            write_tvshow_nfo(show_dir, talk.year)
            assets_dir = get_assets_dir()
            copy_show_images(assets_dir, show_dir, talk.year)
            show_dir_written.add(show_key)

        # Write season.nfo once per track directory — use the season
        # number from the episode_index (derived from the full schedule)
        # so it remains correct even when downloading a subset of tracks.
        season_dir = folder.parent  # …/Fosdem (<year>)/<track>/
        season_key = str(season_dir)
        if season_key not in season_dirs_written and talk.track:
            ep_info = (episode_index or {}).get(talk.id)
            season_num = ep_info[0] if ep_info else 0
            write_season_nfo(season_dir, talk.year, talk.track, season_num)
            assets_dir = get_assets_dir()
            copy_season_images(assets_dir, season_dir, talk.year, talk.track)
            season_dirs_written.add(season_key)


def _build_episode_index(
    talks: list[Talk],
) -> dict[str, tuple[int, int]]:
    """
    Compute ``(season_number, episode_number)`` for each talk.

    Tracks are sorted alphabetically and assigned a 1-based season number.
    Within each track, talks are sorted by ``(date, start)`` and assigned
    a 1-based episode number reflecting their schedule order.

    Returns a dict keyed by ``talk.id``.
    """
    by_track: dict[str, list[Talk]] = defaultdict(list)
    for talk in talks:
        if talk.track:
            by_track[talk.track].append(talk)

    all_tracks = sorted(by_track)
    track_to_season = {t: i for i, t in enumerate(all_tracks, start=1)}

    index: dict[str, tuple[int, int]] = {}
    for track_name, track_talks in by_track.items():
        season_num = track_to_season[track_name]
        ordered = sorted(track_talks, key=lambda t: (t.date, t.start))
        for ep_num, talk in enumerate(ordered, start=1):
            index[talk.id] = (season_num, ep_num)

    return index


def regenerate_nfos(
    talks: list[Talk],
    output_dir: Path,
    fmt: str = "mp4",
    *,
    episode_index: dict[str, tuple[int, int]] | None = None,
) -> int:
    """
    Regenerate all NFO sidecar files for existing videos.

    Writes ``tvshow.nfo``, ``season.nfo`` for every track, and per-episode
    NFOs for each talk whose video file already exists on disk.  Returns the
    number of episode NFOs written.
    """
    if episode_index is None:
        episode_index = _build_episode_index(talks)

    show_dir_written: set[str] = set()
    season_dirs_written: set[str] = set()
    count = 0

    for talk in talks:
        if not talk.title:
            continue

        file_path = get_output_path(
            output_dir,
            talk,
            fmt,
            jellyfin=True,
            episode_index=episode_index,
        )

        # Write tvshow.nfo once per show root
        show_dir = file_path.parent.parent.parent
        show_key = str(show_dir)
        if show_key not in show_dir_written:
            show_dir.mkdir(parents=True, exist_ok=True)
            write_tvshow_nfo(show_dir, talk.year)
            assets_dir = get_assets_dir()
            copy_show_images(assets_dir, show_dir, talk.year)
            show_dir_written.add(show_key)

        # Write season.nfo once per track directory — use the season
        # number from the episode_index (derived from the full schedule).
        season_dir = file_path.parent.parent
        season_key = str(season_dir)
        if season_key not in season_dirs_written and talk.track:
            season_dir.mkdir(parents=True, exist_ok=True)
            ep_info = episode_index.get(talk.id)
            season_num = ep_info[0] if ep_info else 0
            write_season_nfo(season_dir, talk.year, talk.track, season_num)
            assets_dir = get_assets_dir()
            copy_season_images(assets_dir, season_dir, talk.year, talk.track)
            season_dirs_written.add(season_key)

        # Write episode NFO only when the video file exists
        if file_path.exists():
            season_num, ep_num = episode_index.get(talk.id, (0, 0))
            write_episode_nfo(
                talk,
                file_path,
                season_number=season_num,
                episode_number=ep_num,
            )
            count += 1

    logger.info("Regenerated %d episode NFOs", count)
    return count


def download_fosdem_videos(  # noqa: PLR0913
    talks: list[Talk],
    output_dir: Path,
    fmt: str = "mp4",
    num_workers: int = DEFAULT_WORKERS,
    *,
    delay: float = DEFAULT_DELAY,
    no_vtt: bool = False,
    jellyfin: bool = False,
    episode_index: dict[str, tuple[int, int]] | None = None,
) -> list[bool]:
    """
    Download FOSDEM videos (and optionally subtitles) concurrently.

    A *delay* (in seconds) is inserted after each download to avoid
    hammering the FOSDEM video server — which is run by volunteers.
    """
    if episode_index is None:
        episode_index = _build_episode_index(talks) if jellyfin else {}

    session = _build_session()

    def process_video(talk: Talk) -> bool:
        file_path = get_output_path(
            output_dir,
            talk,
            fmt,
            jellyfin=jellyfin,
            episode_index=episode_index,
        )
        success = download_video(talk.url, file_path, session=session)
        if success and not no_vtt:
            download_vtt(talk.url, file_path, session=session)
        if success and jellyfin and talk.title:
            season_num, ep_num = episode_index.get(talk.id, (0, 0))
            write_episode_nfo(
                talk,
                file_path,
                season_number=season_num,
                episode_number=ep_num,
            )
        # Be polite: pause between downloads to avoid overloading the server
        if delay > 0:
            time.sleep(delay)
        return success

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        return list(executor.map(process_video, talks))
