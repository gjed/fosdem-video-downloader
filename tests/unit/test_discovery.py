"""Unit tests for fosdem_video.discovery."""

from __future__ import annotations

from pathlib import Path

import pytest
import responses

from fosdem_video.discovery import parse_ics_file, parse_schedule_xml
from tests.conftest import SAMPLE_SCHEDULE_XML


class TestParseIcsFile:
    """Tests for parse_ics_file."""

    def test_valid_ics_extracts_talks(self, sample_ics_file: Path) -> None:
        talks = parse_ics_file(sample_ics_file)
        # The ICS has 2 events with both URL and LOCATION; 1 event has no URL
        assert len(talks) == 2

    def test_talk_fields_populated(self, sample_ics_file: Path) -> None:
        talks = parse_ics_file(sample_ics_file)
        talk = talks[0]
        assert talk.year == "2025"
        assert talk.id == "fosdem-2025-welcome"
        assert talk.location == "janson"
        assert "video.fosdem.org" in talk.url
        assert talk.url.endswith(".mp4")

    def test_ics_with_no_video_urls(self, tmp_path: Path) -> None:
        ics_content = """\
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Test//Test//EN
BEGIN:VEVENT
DTSTART:20250201T100000Z
DTEND:20250201T104500Z
SUMMARY:No URL event
LOCATION:Room A
END:VEVENT
END:VCALENDAR
"""
        ics_path = tmp_path / "no_urls.ics"
        ics_path.write_text(ics_content)
        talks = parse_ics_file(ics_path)
        assert talks == []

    def test_ics_with_av1_webm_format(self, sample_ics_file: Path) -> None:
        talks = parse_ics_file(sample_ics_file, fmt="av1.webm")
        assert all(t.url.endswith(".av1.webm") for t in talks)

    def test_missing_file_raises_value_error(self, tmp_path: Path) -> None:
        with pytest.raises(ValueError, match="missing or empty"):
            parse_ics_file(tmp_path / "nonexistent.ics")

    def test_empty_file_raises_value_error(self, tmp_path: Path) -> None:
        empty = tmp_path / "empty.ics"
        empty.write_text("")
        with pytest.raises(ValueError, match="missing or empty"):
            parse_ics_file(empty)


class TestParseScheduleXml:
    """Tests for parse_schedule_xml."""

    @responses.activate
    def test_returns_talks_with_rich_metadata(self) -> None:
        responses.add(
            responses.GET,
            "https://fosdem.org/2025/schedule/xml",
            body=SAMPLE_SCHEDULE_XML,
            status=200,
        )
        talks = parse_schedule_xml(2025)
        assert len(talks) == 3

        # Check rich metadata on first talk
        welcome = next(t for t in talks if t.id == "fosdem-2025-welcome")
        assert welcome.title == "Welcome to FOSDEM 2025"
        assert welcome.track == "Main Track"
        assert welcome.date == "2025-02-01"
        assert welcome.start == "10:00"
        assert welcome.duration == "00:45"
        assert welcome.room == "Janson (K.1.105)"
        assert welcome.language == "en"
        assert welcome.event_type == "keynote"
        assert welcome.persons == ["Speaker One"]
        assert welcome.url.endswith(".mp4")

    @responses.activate
    def test_filter_by_track(self) -> None:
        responses.add(
            responses.GET,
            "https://fosdem.org/2025/schedule/xml",
            body=SAMPLE_SCHEDULE_XML,
            status=200,
        )
        talks = parse_schedule_xml(2025, track="Containers")
        assert len(talks) == 2
        assert all(t.track == "Containers" for t in talks)

    @responses.activate
    def test_filter_by_track_case_insensitive(self) -> None:
        responses.add(
            responses.GET,
            "https://fosdem.org/2025/schedule/xml",
            body=SAMPLE_SCHEDULE_XML,
            status=200,
        )
        talks = parse_schedule_xml(2025, track="containers")
        assert len(talks) == 2

    @responses.activate
    def test_filter_by_talk_id(self) -> None:
        responses.add(
            responses.GET,
            "https://fosdem.org/2025/schedule/xml",
            body=SAMPLE_SCHEDULE_XML,
            status=200,
        )
        talks = parse_schedule_xml(2025, talk_id="fosdem-2025-containers-runtime")
        assert len(talks) == 1
        assert talks[0].id == "fosdem-2025-containers-runtime"

    @responses.activate
    def test_html_stripped_from_abstract(self) -> None:
        responses.add(
            responses.GET,
            "https://fosdem.org/2025/schedule/xml",
            body=SAMPLE_SCHEDULE_XML,
            status=200,
        )
        talks = parse_schedule_xml(2025)
        welcome = next(t for t in talks if t.id == "fosdem-2025-welcome")
        assert "<p>" not in welcome.abstract
        assert "Welcome keynote for FOSDEM 2025." in welcome.abstract

    @responses.activate
    def test_non_200_raises_runtime_error(self) -> None:
        responses.add(
            responses.GET,
            "https://fosdem.org/2025/schedule/xml",
            body="Not Found",
            status=404,
        )
        with pytest.raises(RuntimeError, match="HTTP 404"):
            parse_schedule_xml(2025)

    @responses.activate
    def test_av1_webm_format(self) -> None:
        responses.add(
            responses.GET,
            "https://fosdem.org/2025/schedule/xml",
            body=SAMPLE_SCHEDULE_XML,
            status=200,
        )
        talks = parse_schedule_xml(2025, fmt="av1.webm")
        assert all(t.url.endswith(".av1.webm") for t in talks)
