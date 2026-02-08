"""Jellyfin NFO sidecar file generation for FOSDEM talks."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from xml.etree.ElementTree import Element, SubElement, tostring

if TYPE_CHECKING:
    from pathlib import Path

    from fosdem_video.models import Talk

logger = logging.getLogger(__name__)


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


def _build_plot(talk: Talk) -> str:
    """Build the <plot> text from abstract, description, and remaining metadata."""
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


def _add_tags_and_people(movie: Element, talk: Talk) -> None:
    """Add tag and director elements to the NFO movie element."""
    for tag_value in (talk.event_type, talk.language, talk.id):
        if tag_value:
            SubElement(movie, "tag").text = tag_value

    for person in talk.persons:
        SubElement(movie, "director").text = person


def generate_nfo(talk: Talk) -> str:
    """Generate a Jellyfin-compatible NFO XML string for a FOSDEM talk."""
    movie = Element("movie")

    SubElement(movie, "title").text = talk.title

    plot_text = _build_plot(talk)
    if plot_text:
        SubElement(movie, "plot").text = plot_text

    if talk.date:
        SubElement(movie, "aired").text = talk.date

    if talk.duration:
        minutes = _duration_to_minutes(talk.duration)
        if minutes:
            SubElement(movie, "runtime").text = str(minutes)

    if talk.track:
        SubElement(movie, "genre").text = talk.track

    if talk.room:
        SubElement(movie, "studio").text = talk.room

    _add_tags_and_people(movie, talk)

    if talk.event_url:
        SubElement(movie, "trailer").text = talk.event_url

    return tostring(movie, encoding="unicode", xml_declaration=False)


def write_nfo(talk: Talk, video_path: Path) -> bool:
    """
    Write a Jellyfin NFO sidecar file alongside the video.

    The NFO file is named after the video file with a .nfo extension.
    Returns True on success, False on failure.
    """
    nfo_path = video_path.with_suffix(".nfo")
    try:
        xml_content = generate_nfo(talk)
        nfo_path.write_text(
            f'<?xml version="1.0" encoding="UTF-8"?>\n{xml_content}\n',
            encoding="utf-8",
        )
        logger.debug("Wrote NFO sidecar %s", nfo_path.name)
    except Exception:
        logger.exception("Failed to write NFO for %s", talk.id)
        return False
    return True
