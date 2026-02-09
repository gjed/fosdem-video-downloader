"""Talk discovery from ICS files and FOSDEM Pentabarf schedule XML."""

from __future__ import annotations

import html
import logging
import re
import xml.etree.ElementTree as ET
from typing import TYPE_CHECKING

import requests
from icalendar import Calendar

from fosdem_video.models import (
    HTTP_OK,
    Talk,
    get_path_elements,
    normalise_location,
)

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)


def parse_ics_file(ics_path: Path, fmt: str = "mp4") -> list[Talk]:
    """
    Extract video information from ICS file.

    Args:
        ics_path: Path to the ICS file.
        fmt: Video format extension (e.g. "mp4" or "av1.webm").

    """
    if not ics_path.exists() or ics_path.stat().st_size == 0:
        msg = f"Invalid ICS file: {ics_path} (missing or empty)"
        raise ValueError(msg)

    with ics_path.open("rb") as f:
        content = f.read().strip()
        if not content:
            msg = "ICS content is empty after stripping"
            raise ValueError(msg)
        cal = Calendar.from_ical(content)

    talks = []
    for event in cal.walk("vevent"):
        url = event.get("url")
        location = event.get("location")
        if not url or not location:
            continue

        url = str(url)
        year, talk_id = get_path_elements(url)
        location_normalised = normalise_location(str(location))

        video_url = (
            f"https://video.fosdem.org/{year}/{location_normalised}/{talk_id}.{fmt}"
        )

        talks.append(Talk(video_url, year, talk_id, location_normalised))

    return talks


def _el_text(parent: ET.Element, tag: str) -> str:
    """Extract text content from a child element, returning '' if missing."""
    el = parent.find(tag)
    return el.text.strip() if el is not None and el.text else ""


def _strip_html(text: str) -> str:
    """Remove HTML tags and decode entities from a string."""
    unescaped = html.unescape(text)
    return re.sub(r"<[^>]+>", "", unescaped).strip()


def parse_schedule_xml(
    year: int,
    track: str | None = None,
    talk_id: str | None = None,
    fmt: str = "mp4",
) -> list[Talk]:
    """
    Fetch the FOSDEM Pentabarf schedule XML and build Talk objects.

    Args:
        year: FOSDEM edition year (e.g. 2025).
        track: Optional track name filter (case-insensitive substring match).
        talk_id: Optional talk slug to select a single event.
        fmt: Video format extension (e.g. "mp4" or "av1.webm").

    """
    url = f"https://fosdem.org/{year}/schedule/xml"
    logger.info("Fetching schedule XML from %s", url)
    response = requests.get(url, timeout=30)
    if response.status_code != HTTP_OK:
        msg = f"Failed to fetch schedule XML for {year}: HTTP {response.status_code}"
        raise RuntimeError(msg)

    root = ET.fromstring(response.content)  # noqa: S314

    talks: list[Talk] = []
    for day in root.iter("day"):
        for room_el in day.iter("room"):
            room_name = room_el.attrib.get("name", "")
            room_normalised = normalise_location(room_name)

            for event in room_el.iter("event"):
                slug = _el_text(event, "slug")
                if not slug:
                    continue

                if talk_id and slug != talk_id:
                    continue

                event_track = _el_text(event, "track")
                if track and event_track.lower() != track.lower():
                    continue

                persons_el = event.find("persons")
                persons = (
                    [p.text.strip() for p in persons_el.iter("person") if p.text]
                    if persons_el is not None
                    else []
                )

                video_url = (
                    f"https://video.fosdem.org/{year}/{room_normalised}/{slug}.{fmt}"
                )
                talks.append(
                    Talk(
                        url=video_url,
                        year=str(year),
                        id=slug,
                        location=room_normalised,
                        title=_el_text(event, "title"),
                        track=event_track,
                        date=_el_text(event, "date"),
                        start=_el_text(event, "start"),
                        duration=_el_text(event, "duration"),
                        room=room_name,
                        event_url=_el_text(event, "url"),
                        language=_el_text(event, "language"),
                        event_type=_el_text(event, "type"),
                        abstract=_strip_html(_el_text(event, "abstract")),
                        description=_strip_html(
                            _el_text(event, "description"),
                        ),
                        feedback_url=_el_text(event, "feedback_url"),
                        persons=persons,
                    ),
                )

    return talks
