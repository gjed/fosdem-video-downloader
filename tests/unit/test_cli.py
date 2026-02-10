"""Unit tests for fosdem_video.cli argument parsing."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from fosdem_video.cli import parse_arguments


class TestParseArguments:
    """Tests for parse_arguments."""

    def test_default_values_with_ics(self, tmp_path: Path) -> None:
        ics_file = tmp_path / "schedule.ics"
        ics_file.write_text("placeholder")

        with patch("sys.argv", ["prog", "--ics", str(ics_file)]):
            args = parse_arguments()

        assert args.format == "av1.webm"
        assert args.output == Path("./fosdem_videos")
        assert args.workers == 2
        assert args.dry_run is False
        assert args.no_vtt is False
        assert args.jellyfin is False

    def test_mutual_exclusivity_ics_and_year(self) -> None:
        with (
            patch("sys.argv", ["prog", "--ics", "f.ics", "--year", "2025"]),
            pytest.raises(SystemExit),
        ):
            parse_arguments()

    def test_track_requires_year(self, tmp_path: Path) -> None:
        ics_file = tmp_path / "schedule.ics"
        ics_file.write_text("placeholder")

        with (
            patch("sys.argv", ["prog", "--ics", str(ics_file), "--track", "Go"]),
            pytest.raises(SystemExit),
        ):
            parse_arguments()

    def test_talk_requires_year(self, tmp_path: Path) -> None:
        ics_file = tmp_path / "schedule.ics"
        ics_file.write_text("placeholder")

        with (
            patch("sys.argv", ["prog", "--ics", str(ics_file), "--talk", "my-talk"]),
            pytest.raises(SystemExit),
        ):
            parse_arguments()

    def test_invalid_format_value(self) -> None:
        with (
            patch("sys.argv", ["prog", "--year", "2025", "--format", "avi"]),
            pytest.raises(SystemExit),
        ):
            parse_arguments()

    def test_year_mode_accepted(self) -> None:
        with patch("sys.argv", ["prog", "--year", "2025"]):
            args = parse_arguments()
        assert args.year == 2025
        assert args.ics is None

    def test_track_with_year_accepted(self) -> None:
        with patch("sys.argv", ["prog", "--year", "2025", "--track", "Go"]):
            args = parse_arguments()
        assert args.track == "Go"

    def test_regenerate_nfo_requires_jellyfin(self) -> None:
        with (
            patch("sys.argv", ["prog", "--year", "2025", "--regenerate-nfo"]),
            pytest.raises(SystemExit),
        ):
            parse_arguments()

    def test_regenerate_nfo_requires_year(self, tmp_path: Path) -> None:
        ics_file = tmp_path / "schedule.ics"
        ics_file.write_text("placeholder")

        with (
            patch(
                "sys.argv",
                ["prog", "--ics", str(ics_file), "--jellyfin", "--regenerate-nfo"],
            ),
            pytest.raises(SystemExit),
        ):
            parse_arguments()

    def test_ics_file_must_exist(self) -> None:
        with (
            patch("sys.argv", ["prog", "--ics", "/nonexistent/file.ics"]),
            pytest.raises(SystemExit),
        ):
            parse_arguments()

    def test_tracks_requires_year(self, tmp_path: Path) -> None:
        ics_file = tmp_path / "schedule.ics"
        ics_file.write_text("placeholder")

        with (
            patch("sys.argv", ["prog", "--ics", str(ics_file), "--tracks", "1-5"]),
            pytest.raises(SystemExit),
        ):
            parse_arguments()

    def test_track_and_tracks_mutually_exclusive(self) -> None:
        with (
            patch(
                "sys.argv",
                ["prog", "--year", "2025", "--track", "Go", "--tracks", "1-5"],
            ),
            pytest.raises(SystemExit),
        ):
            parse_arguments()
