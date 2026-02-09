"""Core data model and shared helpers for FOSDEM video downloader."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from urllib.parse import urlparse

HTTP_OK = 200
HTTP_NOT_FOUND = 404


@dataclass(frozen=True)
class Talk:
    """Represent a FOSDEM talk video with optional metadata."""

    url: str
    year: str
    id: str
    location: str

    # Rich metadata (populated from schedule XML, empty for ICS mode)
    title: str = ""
    track: str = ""
    date: str = ""
    start: str = ""
    duration: str = ""
    room: str = ""
    event_url: str = ""
    language: str = ""
    event_type: str = ""
    abstract: str = ""
    description: str = ""
    feedback_url: str = ""
    persons: list[str] = field(default_factory=list)


def get_path_elements(url: str) -> tuple[str, str]:
    """Extract year and talk ID from the URL path."""
    parsed = urlparse(url)
    path_parts = [p for p in parsed.path.split("/") if p]

    if not path_parts:
        return ("", "")

    return (path_parts[0], path_parts[-1])


def normalise_location(raw: str) -> str:
    """
    Normalise a room/location string for use in URLs and paths.

    Strips punctuation, takes the first word, and lowercases it.
    """
    cleaned = re.sub(r"[^\w\s]", "", raw)
    return cleaned.split()[0].lower() if cleaned.split() else raw.lower()


def sanitise_path_component(name: str) -> str:
    r"""
    Make *name* safe for use as a single directory or file name component.

    Replaces path separators (``/``, ``\\``), null bytes, and other
    characters that are problematic on common filesystems (``:``, ``*``,
    ``?``, ``"``, ``<``, ``>``, ``|``) with ``-``.  Collapses runs of
    replacement hyphens and strips leading/trailing hyphens and whitespace.
    """
    cleaned = re.sub(r'[/\\:\*\?"<>|\x00]+', "-", name)
    cleaned = re.sub(r"-{2,}", "-", cleaned)
    return cleaned.strip("- ")


def slugify(text: str) -> str:
    """
    Convert a free-form string into a URL/filesystem-safe slug.

    Lowercases, replaces non-alphanumeric runs with single hyphens,
    and strips leading/trailing hyphens.
    """
    slug = text.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def display_name(
    talk: Talk,
    episode_number: int,
    season_number: int = 0,
) -> str:
    """
    Build the canonical display name used for folders and files.

    Format: ``FOSDEM <year> S<ss>E<ee> <title>`` which follows the
    Jellyfin ``SxxExx`` naming convention so the filename parser and
    NFO metadata agree on season/episode numbers.

    Falls back to the raw ``talk.id`` when track or title metadata is
    unavailable.
    """
    if not talk.track or not talk.title:
        return talk.id
    return f"FOSDEM {talk.year} S{season_number:02d}E{episode_number:02d} {talk.title}"
