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
