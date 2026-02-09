"""Video and subtitle downloading, output path logic, and directory creation."""

from __future__ import annotations

import contextlib
import logging
import re
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from pathlib import Path

from fosdem_video.models import (
    HTTP_NOT_FOUND,
    HTTP_OK,
    Talk,
    display_name,
    sanitise_path_component,
)
from fosdem_video.nfo import write_episode_nfo, write_season_nfo, write_tvshow_nfo

logger = logging.getLogger(__name__)


def download_video(url: str, output_path: Path) -> bool:
    """Download a video from a URL to the specified output path."""
    try:
        logger.info("Starting download: %s", output_path.name)
        response = requests.get(url, stream=True, timeout=10)
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


def download_vtt(video_url: str, output_path: Path) -> bool:
    """
    Download a VTT subtitle file corresponding to a video URL.

    Replaces the video extension with .vtt. Logs a warning and returns False
    if the subtitle is not found (404).
    """
    # Strip the format extension and replace with .vtt
    vtt_url = re.sub(r"\.(mp4|av1\.webm)$", ".vtt", video_url)
    vtt_path = output_path.with_suffix(".vtt")
    try:
        logger.debug("Downloading subtitle: %s", vtt_url)
        response = requests.get(vtt_url, stream=True, timeout=10)
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
            folder and file use the canonical display name
            ``fosdem-<year>-<track>-E<nn>-<title>``.

    """
    if jellyfin:
        group = sanitise_path_component(talk.track if talk.track else talk.location)
        ep_info = (episode_index or {}).get(talk.id)
        if ep_info:
            _season_num, ep_num = ep_info
            name = display_name(talk, ep_num)
        else:
            name = talk.id
        return output_dir / f"Fosdem ({talk.year})" / group / name / f"{name}.{fmt}"
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
    all_tracks = sorted({t.track for t in talks if t.track}) if has_metadata else []
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
            show_dir_written.add(show_key)

        # Write season.nfo once per track directory
        season_dir = folder.parent  # …/Fosdem (<year>)/<track>/
        season_key = str(season_dir)
        if season_key not in season_dirs_written and talk.track:
            season_num = all_tracks.index(talk.track) + 1
            write_season_nfo(season_dir, talk.year, talk.track, season_num)
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

    all_tracks = sorted({t.track for t in talks if t.track})
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
            write_tvshow_nfo(show_dir, talk.year)
            show_dir_written.add(show_key)

        # Write season.nfo once per track directory
        season_dir = file_path.parent.parent
        season_key = str(season_dir)
        if season_key not in season_dirs_written and talk.track:
            season_num = all_tracks.index(talk.track) + 1
            write_season_nfo(season_dir, talk.year, talk.track, season_num)
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
    num_workers: int = 3,
    *,
    no_vtt: bool = False,
    jellyfin: bool = False,
    episode_index: dict[str, tuple[int, int]] | None = None,
) -> list[bool]:
    """Download FOSDEM videos (and optionally subtitles) concurrently."""
    if episode_index is None:
        episode_index = _build_episode_index(talks) if jellyfin else {}

    def process_video(talk: Talk) -> bool:
        file_path = get_output_path(
            output_dir,
            talk,
            fmt,
            jellyfin=jellyfin,
            episode_index=episode_index,
        )
        success = download_video(talk.url, file_path)
        if success and not no_vtt:
            download_vtt(talk.url, file_path)
        if success and jellyfin and talk.title:
            season_num, ep_num = episode_index.get(talk.id, (0, 0))
            write_episode_nfo(
                talk,
                file_path,
                season_number=season_num,
                episode_number=ep_num,
            )
        return success

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        return list(executor.map(process_video, talks))
