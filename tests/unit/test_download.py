"""Unit tests for fosdem_video.download."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import responses

from fosdem_video.download import (
    create_dirs,
    download_video,
    download_vtt,
    get_output_path,
    is_downloaded,
)
from fosdem_video.models import Talk
from tests.conftest import make_talk


class TestDownloadVideo:
    """Tests for download_video."""

    @responses.activate
    def test_successful_download(self, tmp_path: Path) -> None:
        url = "https://video.fosdem.org/2025/janson/talk.mp4"
        responses.add(responses.GET, url, body=b"fakevideo", status=200)

        output = tmp_path / "talk.mp4"
        result = download_video(url, output)

        assert result is True
        assert output.exists()
        assert output.read_bytes() == b"fakevideo"

    @responses.activate
    def test_404_returns_false(self, tmp_path: Path) -> None:
        url = "https://video.fosdem.org/2025/janson/missing.mp4"
        responses.add(responses.GET, url, body=b"", status=404)

        output = tmp_path / "missing.mp4"
        result = download_video(url, output)

        assert result is False
        assert not output.exists()

    @responses.activate
    def test_partial_file_cleaned_up_on_failure(self, tmp_path: Path) -> None:
        url = "https://video.fosdem.org/2025/janson/fail.mp4"
        responses.add(
            responses.GET,
            url,
            body=ConnectionError("mid-stream failure"),
        )

        output = tmp_path / "fail.mp4"
        result = download_video(url, output)

        assert result is False
        assert not output.exists()


class TestDownloadVtt:
    """Tests for download_vtt."""

    @responses.activate
    def test_successful_vtt_download(self, tmp_path: Path) -> None:
        video_url = "https://video.fosdem.org/2025/janson/talk.mp4"
        vtt_url = "https://video.fosdem.org/2025/janson/talk.vtt"
        responses.add(responses.GET, vtt_url, body=b"WEBVTT\n\nsubtitle", status=200)

        output = tmp_path / "talk.mp4"
        result = download_vtt(video_url, output)

        assert result is True
        assert (tmp_path / "talk.vtt").exists()

    @responses.activate
    def test_404_returns_false(self, tmp_path: Path) -> None:
        video_url = "https://video.fosdem.org/2025/janson/talk.mp4"
        vtt_url = "https://video.fosdem.org/2025/janson/talk.vtt"
        responses.add(responses.GET, vtt_url, body=b"", status=404)

        output = tmp_path / "talk.mp4"
        result = download_vtt(video_url, output)

        assert result is False
        assert not (tmp_path / "talk.vtt").exists()

    @responses.activate
    def test_av1_webm_extension_replaced(self, tmp_path: Path) -> None:
        video_url = "https://video.fosdem.org/2025/janson/talk.av1.webm"
        vtt_url = "https://video.fosdem.org/2025/janson/talk.vtt"
        responses.add(responses.GET, vtt_url, body=b"WEBVTT\n", status=200)

        output = tmp_path / "talk.av1.webm"
        result = download_vtt(video_url, output)

        assert result is True


class TestGetOutputPath:
    """Tests for get_output_path."""

    def test_flat_layout(self, tmp_path: Path) -> None:
        talk = Talk(url="u", year="2025", id="my-talk", location="janson")
        path = get_output_path(tmp_path, talk, "mp4")
        assert path == tmp_path / "2025" / "my-talk.mp4"

    def test_jellyfin_layout_with_episode_index(self, tmp_path: Path) -> None:
        talk = make_talk(
            talk_id="fosdem-2025-welcome",
            year="2025",
            title="Welcome to FOSDEM",
            track="Main Track",
        )
        episode_index = {"fosdem-2025-welcome": (1, 3)}
        path = get_output_path(tmp_path, talk, "mp4", jellyfin=True, episode_index=episode_index)
        # Should follow: Fosdem (<year>)/<track>/<display_name>/<display_name>.mp4
        assert "Fosdem (2025)" in str(path)
        assert "Main Track" in str(path)
        assert path.name.endswith(".mp4")

    def test_jellyfin_layout_without_episode_index(self, tmp_path: Path) -> None:
        talk = Talk(
            url="u",
            year="2025",
            id="my-talk",
            location="janson",
            track="Go",
        )
        path = get_output_path(tmp_path, talk, "mp4", jellyfin=True)
        assert "Fosdem (2025)" in str(path)
        assert "Go" in str(path)
        assert path.name == "my-talk.mp4"

    def test_jellyfin_without_track_uses_location(self, tmp_path: Path) -> None:
        talk = Talk(url="u", year="2025", id="my-talk", location="janson")
        path = get_output_path(tmp_path, talk, "mp4", jellyfin=True)
        assert "janson" in str(path)


class TestIsDownloaded:
    """Tests for is_downloaded."""

    def test_returns_true_when_file_exists(self, tmp_path: Path) -> None:
        talk = Talk(url="u", year="2025", id="my-talk", location="janson")
        expected = tmp_path / "2025" / "my-talk.mp4"
        expected.parent.mkdir(parents=True)
        expected.write_bytes(b"content")
        assert is_downloaded(tmp_path, talk, "mp4") is True

    def test_returns_false_when_file_missing(self, tmp_path: Path) -> None:
        talk = Talk(url="u", year="2025", id="my-talk", location="janson")
        assert is_downloaded(tmp_path, talk, "mp4") is False


class TestCreateDirs:
    """Tests for create_dirs."""

    def test_flat_layout_creates_year_directory(self, tmp_path: Path) -> None:
        talk = Talk(url="u", year="2025", id="my-talk", location="janson")
        create_dirs(tmp_path, [talk])
        assert (tmp_path / "2025").is_dir()

    @patch("fosdem_video.download.copy_show_images")
    @patch("fosdem_video.download.copy_season_images")
    def test_jellyfin_layout_creates_hierarchy(
        self, _mock_season: object, _mock_show: object, tmp_path: Path
    ) -> None:
        talk = make_talk(track="Containers", title="My Talk")
        episode_index = {talk.id: (1, 1)}
        create_dirs(tmp_path, [talk], jellyfin=True, episode_index=episode_index)
        show_dir = tmp_path / "Fosdem (2025)"
        assert show_dir.is_dir()
        # tvshow.nfo should be written
        assert (show_dir / "tvshow.nfo").exists()
