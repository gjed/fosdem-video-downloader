"""Integration tests for end-to-end CLI workflows."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest
import responses

from fosdem_video.cli import main
from tests.conftest import SAMPLE_ICS_CONTENT, SAMPLE_SCHEDULE_XML

# Common video URLs that appear when parsing the sample ICS/XML fixtures.
_ICS_VIDEO_URLS = [
    "https://video.fosdem.org/2025/janson/fosdem-2025-welcome.mp4",
    "https://video.fosdem.org/2025/ub2252a/fosdem-2025-containers-runtime.mp4",
]
_ICS_VTT_URLS = [
    "https://video.fosdem.org/2025/janson/fosdem-2025-welcome.vtt",
    "https://video.fosdem.org/2025/ub2252a/fosdem-2025-containers-runtime.vtt",
]
_XML_VIDEO_URLS = [
    "https://video.fosdem.org/2025/janson/fosdem-2025-welcome.mp4",
    "https://video.fosdem.org/2025/ub2252a/fosdem-2025-containers-runtime.mp4",
    "https://video.fosdem.org/2025/ub2252a/fosdem-2025-containers-security.mp4",
]
_XML_VTT_URLS = [
    "https://video.fosdem.org/2025/janson/fosdem-2025-welcome.vtt",
    "https://video.fosdem.org/2025/ub2252a/fosdem-2025-containers-runtime.vtt",
    "https://video.fosdem.org/2025/ub2252a/fosdem-2025-containers-security.vtt",
]


def _mock_video_responses(urls: list[str]) -> None:
    """Register mocked 200 responses for a list of video URLs."""
    for url in urls:
        responses.add(responses.GET, url, body=b"fakevideo", status=200)


def _mock_vtt_responses(urls: list[str]) -> None:
    """Register mocked 200 responses for a list of VTT URLs."""
    for url in urls:
        responses.add(responses.GET, url, body=b"WEBVTT\n\nsubtitle", status=200)


class TestIcsDownloadWorkflow:
    """ICS-based download integration tests."""

    @responses.activate
    def test_end_to_end_ics_download(self, tmp_path: Path) -> None:
        ics_file = tmp_path / "schedule.ics"
        ics_file.write_text(SAMPLE_ICS_CONTENT)
        output_dir = tmp_path / "output"

        _mock_video_responses(_ICS_VIDEO_URLS)
        _mock_vtt_responses(_ICS_VTT_URLS)

        with patch(
            "sys.argv",
            [
                "prog",
                "--ics",
                str(ics_file),
                "--format",
                "mp4",
                "-o",
                str(output_dir),
                "--delay",
                "0",
            ],
        ):
            main()

        # Verify flat layout: output/<year>/<slug>.mp4
        assert (output_dir / "2025" / "fosdem-2025-welcome.mp4").exists()
        assert (output_dir / "2025" / "fosdem-2025-containers-runtime.mp4").exists()
        # VTT files should also be present
        assert (output_dir / "2025" / "fosdem-2025-welcome.vtt").exists()

    @responses.activate
    def test_ics_download_with_no_vtt(self, tmp_path: Path) -> None:
        ics_file = tmp_path / "schedule.ics"
        ics_file.write_text(SAMPLE_ICS_CONTENT)
        output_dir = tmp_path / "output"

        _mock_video_responses(_ICS_VIDEO_URLS)

        with patch(
            "sys.argv",
            [
                "prog",
                "--ics",
                str(ics_file),
                "--format",
                "mp4",
                "-o",
                str(output_dir),
                "--no-vtt",
                "--delay",
                "0",
            ],
        ):
            main()

        assert (output_dir / "2025" / "fosdem-2025-welcome.mp4").exists()
        # No VTT files should exist
        vtt_files = list(output_dir.rglob("*.vtt"))
        assert vtt_files == []


class TestYearDownloadWorkflow:
    """Year-based download integration tests."""

    @responses.activate
    def test_end_to_end_year_download(self, tmp_path: Path) -> None:
        output_dir = tmp_path / "output"

        responses.add(
            responses.GET,
            "https://fosdem.org/2025/schedule/xml",
            body=SAMPLE_SCHEDULE_XML,
            status=200,
        )
        _mock_video_responses(_XML_VIDEO_URLS)
        _mock_vtt_responses(_XML_VTT_URLS)

        with patch(
            "sys.argv",
            [
                "prog",
                "--year",
                "2025",
                "--format",
                "mp4",
                "-o",
                str(output_dir),
                "--delay",
                "0",
            ],
        ):
            main()

        assert (output_dir / "2025" / "fosdem-2025-welcome.mp4").exists()
        assert (output_dir / "2025" / "fosdem-2025-containers-runtime.mp4").exists()
        assert (output_dir / "2025" / "fosdem-2025-containers-security.mp4").exists()

    @responses.activate
    def test_year_download_with_track_filter(self, tmp_path: Path) -> None:
        output_dir = tmp_path / "output"

        responses.add(
            responses.GET,
            "https://fosdem.org/2025/schedule/xml",
            body=SAMPLE_SCHEDULE_XML,
            status=200,
        )
        # Only Containers videos should be downloaded
        containers_urls = [
            "https://video.fosdem.org/2025/ub2252a/fosdem-2025-containers-runtime.mp4",
            "https://video.fosdem.org/2025/ub2252a/fosdem-2025-containers-security.mp4",
        ]
        containers_vtts = [
            "https://video.fosdem.org/2025/ub2252a/fosdem-2025-containers-runtime.vtt",
            "https://video.fosdem.org/2025/ub2252a/fosdem-2025-containers-security.vtt",
        ]
        _mock_video_responses(containers_urls)
        _mock_vtt_responses(containers_vtts)

        with patch(
            "sys.argv",
            [
                "prog",
                "--year",
                "2025",
                "--track",
                "Containers",
                "--format",
                "mp4",
                "-o",
                str(output_dir),
                "--delay",
                "0",
            ],
        ):
            main()

        # Only Containers track videos should appear
        assert (output_dir / "2025" / "fosdem-2025-containers-runtime.mp4").exists()
        assert (output_dir / "2025" / "fosdem-2025-containers-security.mp4").exists()
        assert not (output_dir / "2025" / "fosdem-2025-welcome.mp4").exists()


class TestJellyfinWorkflow:
    """Jellyfin layout integration tests."""

    @responses.activate
    def test_jellyfin_layout_creates_nfos(self, tmp_path: Path) -> None:
        output_dir = tmp_path / "output"

        responses.add(
            responses.GET,
            "https://fosdem.org/2025/schedule/xml",
            body=SAMPLE_SCHEDULE_XML,
            status=200,
        )
        _mock_video_responses(_XML_VIDEO_URLS)
        _mock_vtt_responses(_XML_VTT_URLS)

        with patch(
            "sys.argv",
            [
                "prog",
                "--year",
                "2025",
                "--jellyfin",
                "--format",
                "mp4",
                "-o",
                str(output_dir),
                "--delay",
                "0",
            ],
        ):
            main()

        show_dir = output_dir / "Fosdem (2025)"
        assert show_dir.is_dir()
        assert (show_dir / "tvshow.nfo").exists()

        # Check that season NFOs exist for tracks
        nfo_files = list(show_dir.rglob("season.nfo"))
        assert len(nfo_files) >= 1

        # Check that episode NFOs exist
        episode_nfos = list(show_dir.rglob("*.nfo"))
        # Should have at least tvshow.nfo + season NFOs + episode NFOs
        assert len(episode_nfos) >= 4

    @responses.activate
    def test_jellyfin_ics_mode_omits_nfos(self, tmp_path: Path) -> None:
        ics_file = tmp_path / "schedule.ics"
        ics_file.write_text(SAMPLE_ICS_CONTENT)
        output_dir = tmp_path / "output"

        _mock_video_responses(_ICS_VIDEO_URLS)
        _mock_vtt_responses(_ICS_VTT_URLS)

        with patch(
            "sys.argv",
            [
                "prog",
                "--ics",
                str(ics_file),
                "--jellyfin",
                "--format",
                "mp4",
                "-o",
                str(output_dir),
                "--delay",
                "0",
            ],
        ):
            main()

        # ICS mode + jellyfin should produce folder structure but no NFOs
        # (ICS talks have no rich metadata)
        nfo_files = list(output_dir.rglob("*.nfo"))
        assert nfo_files == []


class TestDryRunWorkflow:
    """Dry-run mode integration tests."""

    def test_dry_run_produces_no_files(self, tmp_path: Path) -> None:
        ics_file = tmp_path / "schedule.ics"
        ics_file.write_text(SAMPLE_ICS_CONTENT)
        output_dir = tmp_path / "output"

        with patch(
            "sys.argv",
            [
                "prog",
                "--ics",
                str(ics_file),
                "--format",
                "mp4",
                "-o",
                str(output_dir),
                "--dry-run",
            ],
        ):
            main()

        # No video files should be written
        mp4_files = list(output_dir.rglob("*.mp4")) if output_dir.exists() else []
        assert mp4_files == []


class TestNfoRegenerationWorkflow:
    """NFO regeneration integration tests."""

    @responses.activate
    def test_regenerate_nfo_rewrites_sidecars(self, tmp_path: Path) -> None:
        output_dir = tmp_path / "output"

        # First, do a normal download to get video files in place
        responses.add(
            responses.GET,
            "https://fosdem.org/2025/schedule/xml",
            body=SAMPLE_SCHEDULE_XML,
            status=200,
        )
        _mock_video_responses(_XML_VIDEO_URLS)
        _mock_vtt_responses(_XML_VTT_URLS)

        with patch(
            "sys.argv",
            [
                "prog",
                "--year",
                "2025",
                "--jellyfin",
                "--format",
                "mp4",
                "-o",
                str(output_dir),
                "--delay",
                "0",
            ],
        ):
            main()

        # Delete episode NFOs to prove regeneration recreates them
        for nfo in output_dir.rglob("*.nfo"):
            if nfo.name not in {"tvshow.nfo", "season.nfo"}:
                nfo.unlink()

        # Regenerate NFOs
        responses.add(
            responses.GET,
            "https://fosdem.org/2025/schedule/xml",
            body=SAMPLE_SCHEDULE_XML,
            status=200,
        )
        with patch(
            "sys.argv",
            [
                "prog",
                "--year",
                "2025",
                "--jellyfin",
                "--regenerate-nfo",
                "--format",
                "mp4",
                "-o",
                str(output_dir),
                "--delay",
                "0",
            ],
        ):
            main()

        # Episode NFOs should be back
        episode_nfos = [f for f in output_dir.rglob("*.nfo") if f.name not in {"tvshow.nfo", "season.nfo"}]
        assert len(episode_nfos) >= 1


class TestErrorHandlingWorkflow:
    """Error handling integration tests."""

    @responses.activate
    def test_404_on_video_continues_pipeline(self, tmp_path: Path) -> None:
        ics_file = tmp_path / "schedule.ics"
        ics_file.write_text(SAMPLE_ICS_CONTENT)
        output_dir = tmp_path / "output"

        # First video returns 404, second succeeds
        responses.add(responses.GET, _ICS_VIDEO_URLS[0], body=b"", status=404)
        responses.add(responses.GET, _ICS_VIDEO_URLS[1], body=b"fakevideo", status=200)
        _mock_vtt_responses(_ICS_VTT_URLS[1:])

        with patch(
            "sys.argv",
            [
                "prog",
                "--ics",
                str(ics_file),
                "--format",
                "mp4",
                "-o",
                str(output_dir),
                "--delay",
                "0",
            ],
        ):
            main()

        # First video should not exist, second should
        assert not (output_dir / "2025" / "fosdem-2025-welcome.mp4").exists()
        assert (output_dir / "2025" / "fosdem-2025-containers-runtime.mp4").exists()

    def test_missing_ics_file_exits_with_error(self) -> None:
        with (
            patch(
                "sys.argv",
                ["prog", "--ics", "/nonexistent/schedule.ics"],
            ),
            pytest.raises(SystemExit) as exc_info,
        ):
            main()
        assert exc_info.value.code != 0
