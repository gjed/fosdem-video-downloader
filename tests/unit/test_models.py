"""Unit tests for fosdem_video.models."""

from __future__ import annotations

import pytest

from fosdem_video.models import (
    Talk,
    display_name,
    get_path_elements,
    normalise_location,
    sanitise_path_component,
    slugify,
)


class TestGetPathElements:
    """Tests for get_path_elements."""

    def test_valid_fosdem_url(self) -> None:
        url = "https://fosdem.org/2025/schedule/event/fosdem-2025-welcome/"
        year, slug = get_path_elements(url)
        assert year == "2025"
        assert slug == "fosdem-2025-welcome"

    def test_video_url(self) -> None:
        url = "https://video.fosdem.org/2025/janson/fosdem-2025-welcome.mp4"
        year, slug = get_path_elements(url)
        assert year == "2025"
        assert slug == "fosdem-2025-welcome.mp4"

    def test_empty_path(self) -> None:
        url = "https://fosdem.org/"
        year, slug = get_path_elements(url)
        assert year == ""
        assert slug == ""

    def test_single_path_element(self) -> None:
        url = "https://fosdem.org/2025"
        year, slug = get_path_elements(url)
        assert year == "2025"
        assert slug == "2025"

    def test_plain_string_no_scheme(self) -> None:
        """A bare path without scheme still works via urlparse."""
        year, slug = get_path_elements("/2025/janson/my-talk.mp4")
        assert year == "2025"
        assert slug == "my-talk.mp4"


class TestNormaliseLocation:
    """Tests for normalise_location."""

    def test_strips_punctuation_takes_first_word(self) -> None:
        assert normalise_location("Janson (K.1.105)") == "janson"

    def test_mixed_case(self) -> None:
        assert normalise_location("UB2.252A (Lameere)") == "ub2252a"

    def test_multi_word(self) -> None:
        assert normalise_location("Main Hall") == "main"

    def test_simple_room(self) -> None:
        assert normalise_location("janson") == "janson"

    def test_empty_string(self) -> None:
        """Empty input returns empty string lowered."""
        assert normalise_location("") == ""

    def test_only_punctuation(self) -> None:
        """All-punctuation falls back to raw.lower()."""
        assert normalise_location("...") == "..."


class TestSanitisePathComponent:
    """Tests for sanitise_path_component."""

    def test_replaces_special_characters(self) -> None:
        assert sanitise_path_component('file/name:with*bad?"chars') == "file-name-with-bad-chars"

    def test_collapses_multiple_hyphens(self) -> None:
        assert sanitise_path_component("a///b") == "a-b"

    def test_strips_leading_trailing_hyphens(self) -> None:
        assert sanitise_path_component("/hello/") == "hello"

    def test_preserves_safe_characters(self) -> None:
        assert sanitise_path_component("normal text here") == "normal text here"

    def test_null_byte_replaced(self) -> None:
        assert sanitise_path_component("before\x00after") == "before-after"


class TestSlugify:
    """Tests for slugify."""

    def test_spaces_to_hyphens(self) -> None:
        assert slugify("Hello World") == "hello-world"

    def test_special_characters_removed(self) -> None:
        assert slugify("FOSDEM 2025: A Talk!") == "fosdem-2025-a-talk"

    def test_unicode_removed(self) -> None:
        assert slugify("café résumé") == "caf-r-sum"

    def test_empty_string(self) -> None:
        assert slugify("") == ""

    def test_leading_trailing_hyphens_stripped(self) -> None:
        assert slugify("  --hello-- ") == "hello"

    def test_consecutive_special_chars_collapsed(self) -> None:
        assert slugify("a!!!b") == "a-b"


class TestDisplayName:
    """Tests for display_name."""

    def test_with_full_metadata(self) -> None:
        talk = Talk(
            url="https://video.fosdem.org/2025/janson/welcome.mp4",
            year="2025",
            id="welcome",
            location="janson",
            title="Welcome to FOSDEM",
            track="Main Track",
        )
        result = display_name(talk, episode_number=3, season_number=1)
        assert result == "FOSDEM 2025 S01E03 Welcome to FOSDEM"

    def test_fallback_when_missing_title(self) -> None:
        talk = Talk(
            url="https://video.fosdem.org/2025/janson/welcome.mp4",
            year="2025",
            id="welcome",
            location="janson",
            track="Main Track",
        )
        result = display_name(talk, episode_number=1, season_number=1)
        assert result == "welcome"

    def test_fallback_when_missing_track(self) -> None:
        talk = Talk(
            url="https://video.fosdem.org/2025/janson/welcome.mp4",
            year="2025",
            id="welcome",
            location="janson",
            title="Welcome to FOSDEM",
        )
        result = display_name(talk, episode_number=1, season_number=1)
        assert result == "welcome"

    def test_season_episode_zero_padding(self) -> None:
        talk = Talk(
            url="https://video.fosdem.org/2025/janson/welcome.mp4",
            year="2025",
            id="welcome",
            location="janson",
            title="Welcome",
            track="Main",
        )
        result = display_name(talk, episode_number=12, season_number=5)
        assert result == "FOSDEM 2025 S05E12 Welcome"


class TestTalkDataclass:
    """Tests for the Talk dataclass."""

    def test_construction_with_required_fields(self) -> None:
        talk = Talk(url="u", year="2025", id="t", location="r")
        assert talk.url == "u"
        assert talk.title == ""
        assert talk.persons == []

    def test_frozen_immutability(self) -> None:
        talk = Talk(url="u", year="2025", id="t", location="r")
        with pytest.raises(AttributeError):
            talk.url = "new"  # type: ignore[misc]

    def test_equality(self) -> None:
        t1 = Talk(url="u", year="2025", id="t", location="r")
        t2 = Talk(url="u", year="2025", id="t", location="r")
        assert t1 == t2

    def test_rich_metadata_defaults(self) -> None:
        talk = Talk(url="u", year="2025", id="t", location="r")
        assert talk.track == ""
        assert talk.date == ""
        assert talk.start == ""
        assert talk.duration == ""
        assert talk.room == ""
        assert talk.event_url == ""
        assert talk.language == ""
        assert talk.event_type == ""
        assert talk.abstract == ""
        assert talk.description == ""
        assert talk.feedback_url == ""
