"""Unit tests for fosdem_video.nfo."""

from __future__ import annotations

from pathlib import Path

from fosdem_video.nfo import (
    generate_episode_nfo,
    generate_season_nfo,
    generate_tvshow_nfo,
    write_episode_nfo,
    write_season_nfo,
    write_tvshow_nfo,
)
from tests.conftest import make_talk


class TestGenerateTvshowNfo:
    """Tests for generate_tvshow_nfo."""

    def test_xml_structure(self) -> None:
        root = generate_tvshow_nfo("2025")
        assert root.tag == "tvshow"
        assert root.findtext("title") == "FOSDEM 2025"
        assert root.findtext("showtitle") == "FOSDEM 2025"
        assert root.findtext("premiered") == "2025-02-01"
        assert root.findtext("studio") == "FOSDEM"
        assert root.findtext("genre") == "Technology"

        # Check tags
        tags = [el.text for el in root.findall("tag")]
        assert "conference" in tags
        assert "open-source" in tags

        # Check uniqueid
        uid = root.find("uniqueid")
        assert uid is not None
        assert uid.text == "fosdem-2025"
        assert uid.get("type") == "fosdem"
        assert uid.get("default") == "true"

    def test_plot_contains_fosdem_description(self) -> None:
        root = generate_tvshow_nfo("2025")
        plot = root.findtext("plot")
        assert plot is not None
        assert "FOSDEM" in plot
        assert "Brussels" in plot


class TestGenerateSeasonNfo:
    """Tests for generate_season_nfo."""

    def test_xml_structure(self) -> None:
        root = generate_season_nfo("2025", "Containers", 3)
        assert root.tag == "season"
        assert root.findtext("title") == "Containers"
        assert root.findtext("seasonnumber") == "3"
        assert root.findtext("lockdata") == "true"

    def test_plot_includes_track_name(self) -> None:
        root = generate_season_nfo("2025", "Go", 1)
        plot = root.findtext("plot")
        assert plot is not None
        assert "Go" in plot
        assert "2025" in plot


class TestGenerateEpisodeNfo:
    """Tests for generate_episode_nfo."""

    def test_xml_structure(self) -> None:
        talk = make_talk(
            title="Container Runtimes",
            duration="01:30",
            room="Janson (K.1.105)",
            date="2025-02-01",
        )
        root = generate_episode_nfo(talk, season_number=2, episode_number=5)
        assert root.tag == "episodedetails"
        assert root.findtext("title") == "Container Runtimes"
        assert root.findtext("showtitle") == "FOSDEM 2025"
        assert root.findtext("lockdata") == "true"
        assert root.findtext("season") == "Main Track"
        assert root.findtext("seasonnumber") == "2"
        assert root.findtext("episode") == "5"
        assert root.findtext("aired") == "2025-02-01"
        assert root.findtext("runtime") == "90"
        assert root.findtext("studio") == "Janson (K.1.105)"

    def test_speaker_elements(self) -> None:
        talk = make_talk(persons=["Alice", "Bob", "Charlie"])
        root = generate_episode_nfo(talk, season_number=1, episode_number=1)
        directors = [el.text for el in root.findall("director")]
        assert directors == ["Alice", "Bob", "Charlie"]

    def test_no_season_episode_when_zero(self) -> None:
        talk = make_talk()
        root = generate_episode_nfo(talk)
        assert root.find("season") is None
        assert root.find("seasonnumber") is None
        assert root.find("episode") is None

    def test_uniqueid_uses_slug(self) -> None:
        talk = make_talk(talk_id="fosdem-2025-my-talk")
        root = generate_episode_nfo(talk)
        uid = root.find("uniqueid")
        assert uid is not None
        assert uid.text == "fosdem-2025-my-talk"

    def test_trailer_uses_event_url(self) -> None:
        talk = make_talk(event_url="https://fosdem.org/2025/event/my-talk/")
        root = generate_episode_nfo(talk)
        assert root.findtext("trailer") == "https://fosdem.org/2025/event/my-talk/"

    def test_plot_includes_abstract_and_metadata(self) -> None:
        talk = make_talk(
            abstract="Talk abstract.",
            description="Talk description.",
            talk_id="my-slug",
            language="en",
            event_type="devroom",
        )
        root = generate_episode_nfo(talk)
        plot = root.findtext("plot")
        assert plot is not None
        assert "Talk abstract." in plot
        assert "Talk description." in plot
        assert "Slug: my-slug" in plot
        assert "Language: en" in plot


class TestWriteTvshowNfo:
    """Tests for write_tvshow_nfo."""

    def test_writes_file(self, tmp_path: Path) -> None:
        result = write_tvshow_nfo(tmp_path, "2025")
        assert result is True
        nfo_path = tmp_path / "tvshow.nfo"
        assert nfo_path.exists()
        content = nfo_path.read_text()
        assert '<?xml version="1.0"' in content
        assert "<tvshow>" in content


class TestWriteSeasonNfo:
    """Tests for write_season_nfo."""

    def test_writes_file(self, tmp_path: Path) -> None:
        result = write_season_nfo(tmp_path, "2025", "Go", 2)
        assert result is True
        nfo_path = tmp_path / "season.nfo"
        assert nfo_path.exists()
        content = nfo_path.read_text()
        assert "<season>" in content
        assert "Go" in content


class TestWriteEpisodeNfo:
    """Tests for write_episode_nfo."""

    def test_writes_file(self, tmp_path: Path) -> None:
        talk = make_talk()
        video_path = tmp_path / "my-talk.mp4"
        video_path.write_bytes(b"fake")

        result = write_episode_nfo(talk, video_path, season_number=1, episode_number=1)
        assert result is True
        nfo_path = tmp_path / "my-talk.nfo"
        assert nfo_path.exists()
        content = nfo_path.read_text()
        assert "<episodedetails>" in content
