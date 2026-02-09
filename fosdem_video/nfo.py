"""
Jellyfin NFO sidecar file generation for FOSDEM talks.

Generates three levels of NFO files matching the Jellyfin TV series model:

- **tvshow.nfo** (``<tvshow>``) — placed in the show root directory
  ``Fosdem (<year>)/``.  Contains the FOSDEM edition title, a short
  description of the conference, the premiere date, studio, genre, and tags.

- **season.nfo** (``<season>``) — placed in each track directory
  ``Fosdem (<year>)/<track>/``.  Carries the track name as the season
  title, season number, and a brief description.

- **<slug>.nfo** (``<episodedetails>``) — placed alongside the video file
  in the per-talk subfolder.  Maps talk metadata to episode-level tags:
  title, showtitle, season, seasonnumber, episode, plot (abstract +
  description + extra metadata block), aired, runtime, studio, director
  (speakers), trailer, and a ``<uniqueid>`` for the slug.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from xml.etree.ElementTree import Element, SubElement, tostring

if TYPE_CHECKING:
    from pathlib import Path

    from fosdem_video.models import Talk

logger = logging.getLogger(__name__)

_FOSDEM_PLOT = (
    "FOSDEM is a free event for software developers to meet, share ideas "
    "and collaborate.  Every year, thousands of developers of free and "
    "open source software from all over the world gather at the event "
    "in Brussels.  https://fosdem.org/"
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _duration_to_minutes(duration: str) -> int:
    """
    Convert a duration string (HH:MM) to total minutes.

    Returns 0 if the format is unrecognised.
    """
    parts = duration.strip().split(":")
    if len(parts) == 2:  # noqa: PLR2004
        try:
            return int(parts[0]) * 60 + int(parts[1])
        except ValueError:
            return 0
    return 0


def _build_episode_plot(talk: Talk) -> str:
    """Build the ``<plot>`` text for an episode NFO."""
    sections: list[str] = []

    if talk.abstract:
        sections.append(talk.abstract)
    if talk.description:
        sections.append(talk.description)

    # Collapse metadata that doesn't map cleanly to NFO tags
    meta_lines: list[str] = []
    if talk.id:
        meta_lines.append(f"Slug: {talk.id}")
    if talk.feedback_url:
        meta_lines.append(f"Feedback: {talk.feedback_url}")
    if talk.language:
        meta_lines.append(f"Language: {talk.language}")
    if talk.event_type:
        meta_lines.append(f"Type: {talk.event_type}")

    if meta_lines:
        sections.append("---\n" + "\n".join(meta_lines))

    return "\n\n".join(sections)


def _write_xml(path: Path, root: Element) -> bool:
    """Serialise *root* to *path* with an XML declaration."""
    try:
        xml_content = tostring(root, encoding="unicode", xml_declaration=False)
        path.write_text(
            f'<?xml version="1.0" encoding="UTF-8"?>\n{xml_content}\n',
            encoding="utf-8",
        )
        logger.debug("Wrote NFO sidecar %s", path.name)
    except Exception:
        logger.exception("Failed to write NFO %s", path)
        return False
    return True


# ---------------------------------------------------------------------------
# TVShow-level NFO  (Fosdem (<year>)/tvshow.nfo)
# ---------------------------------------------------------------------------


def generate_tvshow_nfo(year: str) -> Element:
    """Build a ``<tvshow>`` element for a FOSDEM edition."""
    root = Element("tvshow")

    SubElement(root, "title").text = f"FOSDEM {year}"
    SubElement(root, "showtitle").text = f"FOSDEM {year}"
    SubElement(root, "plot").text = _FOSDEM_PLOT
    SubElement(root, "premiered").text = f"{year}-02-01"
    SubElement(root, "studio").text = "FOSDEM"
    SubElement(root, "genre").text = "Technology"
    SubElement(root, "tag").text = "conference"
    SubElement(root, "tag").text = "open-source"

    uniqueid = SubElement(root, "uniqueid")
    uniqueid.set("type", "fosdem")
    uniqueid.set("default", "true")
    uniqueid.text = f"fosdem-{year}"

    return root


def write_tvshow_nfo(show_dir: Path, year: str) -> bool:
    """Write ``tvshow.nfo`` into the show root directory."""
    root = generate_tvshow_nfo(year)
    return _write_xml(show_dir / "tvshow.nfo", root)


# ---------------------------------------------------------------------------
# Season-level NFO  (Fosdem (<year>)/<track>/season.nfo)
# ---------------------------------------------------------------------------


def generate_season_nfo(
    year: str,
    track: str,
    season_number: int,
) -> Element:
    """Build a ``<season>`` element for a FOSDEM track."""
    root = Element("season")

    SubElement(root, "title").text = track
    SubElement(root, "seasonnumber").text = str(season_number)
    SubElement(root, "lockdata").text = "true"
    SubElement(root, "plot").text = (
        f"FOSDEM {year} — {track} track.  All talks presented in the {track} developer room."
    )

    return root


def write_season_nfo(
    season_dir: Path,
    year: str,
    track: str,
    season_number: int,
) -> bool:
    """Write ``season.nfo`` into a track directory."""
    root = generate_season_nfo(year, track, season_number)
    return _write_xml(season_dir / "season.nfo", root)


# ---------------------------------------------------------------------------
# Episode-level NFO  (<slug>.nfo alongside the video)
# ---------------------------------------------------------------------------


def _add_episode_people(root: Element, talk: Talk) -> None:
    """Add ``<director>`` elements (one per speaker) to an episode."""
    for person in talk.persons:
        SubElement(root, "director").text = person


def generate_episode_nfo(
    talk: Talk,
    *,
    season_number: int = 0,
    episode_number: int = 0,
) -> Element:
    """
    Build an ``<episodedetails>`` element for a single FOSDEM talk.

    Args:
        talk: The Talk to generate metadata for.
        season_number: Alphabetical index of the track (1-based).
        episode_number: Position of this talk within its track (1-based),
            ordered by schedule date and start time.

    """
    root = Element("episodedetails")

    SubElement(root, "title").text = talk.title
    SubElement(root, "showtitle").text = f"FOSDEM {talk.year}"
    SubElement(root, "lockdata").text = "true"

    if season_number:
        SubElement(root, "season").text = str(season_number)
        SubElement(root, "seasonnumber").text = str(season_number)
    if episode_number:
        SubElement(root, "episode").text = str(episode_number)

    plot_text = _build_episode_plot(talk)
    if plot_text:
        SubElement(root, "plot").text = plot_text

    if talk.date:
        SubElement(root, "aired").text = talk.date

    if talk.duration:
        minutes = _duration_to_minutes(talk.duration)
        if minutes:
            SubElement(root, "runtime").text = str(minutes)

    if talk.room:
        SubElement(root, "studio").text = talk.room

    uniqueid = SubElement(root, "uniqueid")
    uniqueid.set("type", "fosdem")
    uniqueid.set("default", "true")
    uniqueid.text = talk.id

    if talk.event_url:
        SubElement(root, "trailer").text = talk.event_url

    _add_episode_people(root, talk)

    return root


def write_episode_nfo(
    talk: Talk,
    video_path: Path,
    *,
    season_number: int = 0,
    episode_number: int = 0,
) -> bool:
    """
    Write an episode NFO sidecar file alongside the video.

    The NFO file is named after the video file with a ``.nfo`` extension.
    Returns True on success, False on failure.
    """
    root = generate_episode_nfo(
        talk,
        season_number=season_number,
        episode_number=episode_number,
    )
    return _write_xml(video_path.with_suffix(".nfo"), root)
