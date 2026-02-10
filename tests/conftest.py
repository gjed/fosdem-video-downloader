"""Shared fixtures for FOSDEM video downloader tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from fosdem_video.models import Talk

# ---------------------------------------------------------------------------
# Sample ICS content — 2 events with FOSDEM video URLs, 1 event without
# ---------------------------------------------------------------------------

SAMPLE_ICS_CONTENT = """\
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//FOSDEM//Schedule//EN
BEGIN:VEVENT
DTSTART:20250201T100000Z
DTEND:20250201T104500Z
SUMMARY:Welcome to FOSDEM 2025
LOCATION:Janson (K.1.105)
URL:https://fosdem.org/2025/schedule/event/fosdem-2025-welcome/
END:VEVENT
BEGIN:VEVENT
DTSTART:20250201T110000Z
DTEND:20250201T115000Z
SUMMARY:Container Runtimes in 2025
LOCATION:UB2.252A (Lameere)
URL:https://fosdem.org/2025/schedule/event/fosdem-2025-containers-runtime/
END:VEVENT
BEGIN:VEVENT
DTSTART:20250201T120000Z
DTEND:20250201T125000Z
SUMMARY:A talk with no URL
LOCATION:H.1301 (Cornil)
END:VEVENT
END:VCALENDAR
"""

# ---------------------------------------------------------------------------
# Sample Pentabarf Schedule XML — 2 events across 2 tracks
# ---------------------------------------------------------------------------

SAMPLE_SCHEDULE_XML = """\
<?xml version="1.0" encoding="UTF-8"?>
<schedule>
  <conference>
    <title>FOSDEM 2025</title>
  </conference>
  <day index="1" date="2025-02-01">
    <room name="Janson (K.1.105)">
      <event id="1001">
        <slug>fosdem-2025-welcome</slug>
        <title>Welcome to FOSDEM 2025</title>
        <track>Main Track</track>
        <date>2025-02-01</date>
        <start>10:00</start>
        <duration>00:45</duration>
        <room>Janson (K.1.105)</room>
        <url>https://fosdem.org/2025/schedule/event/fosdem-2025-welcome/</url>
        <language>en</language>
        <type>keynote</type>
        <abstract>&lt;p&gt;Welcome keynote for FOSDEM 2025.&lt;/p&gt;</abstract>
        <description>&lt;p&gt;The opening ceremony of FOSDEM 2025.&lt;/p&gt;</description>
        <feedback_url>https://fosdem.org/2025/feedback/fosdem-2025-welcome/</feedback_url>
        <persons>
          <person id="1">Speaker One</person>
        </persons>
      </event>
    </room>
    <room name="UB2.252A (Lameere)">
      <event id="1002">
        <slug>fosdem-2025-containers-runtime</slug>
        <title>Container Runtimes in 2025</title>
        <track>Containers</track>
        <date>2025-02-01</date>
        <start>11:00</start>
        <duration>00:50</duration>
        <room>UB2.252A (Lameere)</room>
        <url>https://fosdem.org/2025/schedule/event/fosdem-2025-containers-runtime/</url>
        <language>en</language>
        <type>devroom</type>
        <abstract>An overview of container runtimes.</abstract>
        <description>Deep dive into runc, crun, and youki.</description>
        <feedback_url>https://fosdem.org/2025/feedback/fosdem-2025-containers-runtime/</feedback_url>
        <persons>
          <person id="2">Alice Dev</person>
          <person id="3">Bob Ops</person>
        </persons>
      </event>
      <event id="1003">
        <slug>fosdem-2025-containers-security</slug>
        <title>Container Security Essentials</title>
        <track>Containers</track>
        <date>2025-02-01</date>
        <start>12:00</start>
        <duration>00:40</duration>
        <room>UB2.252A (Lameere)</room>
        <url>https://fosdem.org/2025/schedule/event/fosdem-2025-containers-security/</url>
        <language>en</language>
        <type>devroom</type>
        <abstract>Security best practices for containers.</abstract>
        <description>Learn how to harden container deployments.</description>
        <feedback_url>https://fosdem.org/2025/feedback/fosdem-2025-containers-security/</feedback_url>
        <persons>
          <person id="4">Charlie Sec</person>
        </persons>
      </event>
    </room>
  </day>
</schedule>
"""


@pytest.fixture
def sample_ics_content() -> str:
    """Return sample ICS content with 2 events containing FOSDEM video URLs."""
    return SAMPLE_ICS_CONTENT


@pytest.fixture
def sample_schedule_xml() -> str:
    """Return sample Pentabarf XML with 3 events across 2 tracks."""
    return SAMPLE_SCHEDULE_XML


@pytest.fixture
def sample_ics_file(tmp_path: Path, sample_ics_content: str) -> Path:
    """Write sample ICS content to a temporary file and return its path."""
    ics_path = tmp_path / "schedule.ics"
    ics_path.write_text(sample_ics_content)
    return ics_path


@pytest.fixture
def output_dir(tmp_path: Path) -> Path:
    """Provide a temporary output directory for downloads."""
    out = tmp_path / "output"
    out.mkdir()
    return out


def make_talk(
    *,
    url: str = "https://video.fosdem.org/2025/janson/fosdem-2025-welcome.mp4",
    year: str = "2025",
    talk_id: str = "fosdem-2025-welcome",
    location: str = "janson",
    title: str = "Welcome to FOSDEM 2025",
    track: str = "Main Track",
    date: str = "2025-02-01",
    start: str = "10:00",
    duration: str = "00:45",
    room: str = "Janson (K.1.105)",
    event_url: str = "https://fosdem.org/2025/schedule/event/fosdem-2025-welcome/",
    language: str = "en",
    event_type: str = "keynote",
    abstract: str = "Welcome keynote for FOSDEM 2025.",
    description: str = "The opening ceremony of FOSDEM 2025.",
    feedback_url: str = "https://fosdem.org/2025/feedback/fosdem-2025-welcome/",
    persons: list[str] | None = None,
) -> Talk:
    """Create a Talk instance with sensible defaults for testing."""
    return Talk(
        url=url,
        year=year,
        id=talk_id,
        location=location,
        title=title,
        track=track,
        date=date,
        start=start,
        duration=duration,
        room=room,
        event_url=event_url,
        language=language,
        event_type=event_type,
        abstract=abstract,
        description=description,
        feedback_url=feedback_url,
        persons=persons if persons is not None else ["Speaker One"],
    )
