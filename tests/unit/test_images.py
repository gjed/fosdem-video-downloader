"""Unit tests for fosdem_video.images."""

from __future__ import annotations

from pathlib import Path

from fosdem_video.images import copy_season_images, copy_show_images, resolve_assets


def _create_asset(assets_dir: Path, name: str) -> Path:
    """Create a dummy asset file and return its path."""
    path = assets_dir / name
    path.write_bytes(b"fake-image-data")
    return path


class TestResolveAssets:
    """Tests for resolve_assets."""

    def test_year_specific_priority(self, tmp_path: Path) -> None:
        assets = tmp_path / "assets"
        assets.mkdir()
        _create_asset(assets, "fosdem-2026-primary.jpg")
        _create_asset(assets, "fosdem-primary.jpg")

        result = resolve_assets(assets, "2026", "primary")
        assert len(result) == 1
        assert result[0].name == "fosdem-2026-primary.jpg"

    def test_default_fallback(self, tmp_path: Path) -> None:
        assets = tmp_path / "assets"
        assets.mkdir()
        _create_asset(assets, "fosdem-backdrop.png")

        result = resolve_assets(assets, "2026", "backdrop")
        assert len(result) == 1
        assert result[0].name == "fosdem-backdrop.png"

    def test_no_matching_files(self, tmp_path: Path) -> None:
        assets = tmp_path / "assets"
        assets.mkdir()

        result = resolve_assets(assets, "2026", "primary")
        assert result == []

    def test_season_track_fallback(self, tmp_path: Path) -> None:
        assets = tmp_path / "assets"
        assets.mkdir()
        _create_asset(assets, "track-go-poster.jpg")

        result = resolve_assets(assets, "2026", "poster", track_slug="go")
        assert len(result) == 1
        assert result[0].name == "track-go-poster.jpg"

    def test_numbered_variants_ordered(self, tmp_path: Path) -> None:
        assets = tmp_path / "assets"
        assets.mkdir()
        _create_asset(assets, "fosdem-backdrop.jpg")
        _create_asset(assets, "fosdem-backdrop-1.jpg")
        _create_asset(assets, "fosdem-backdrop-2.jpg")

        result = resolve_assets(assets, "2026", "backdrop")
        assert len(result) == 3
        # Un-numbered first, then numbered in order
        assert result[0].name == "fosdem-backdrop.jpg"
        assert result[1].name == "fosdem-backdrop-1.jpg"
        assert result[2].name == "fosdem-backdrop-2.jpg"


class TestCopyShowImages:
    """Tests for copy_show_images."""

    def test_copies_to_jellyfin_names(self, tmp_path: Path) -> None:
        assets = tmp_path / "assets"
        assets.mkdir()
        _create_asset(assets, "fosdem-2025-primary.jpg")

        show_dir = tmp_path / "show"
        show_dir.mkdir()

        copy_show_images(assets, show_dir, "2025")
        assert (show_dir / "poster.jpg").exists()

    def test_skips_when_assets_dir_missing(self, tmp_path: Path) -> None:
        show_dir = tmp_path / "show"
        show_dir.mkdir()
        # Should not raise
        copy_show_images(tmp_path / "nonexistent", show_dir, "2025")


class TestCopySeasonImages:
    """Tests for copy_season_images."""

    def test_copies_to_jellyfin_names(self, tmp_path: Path) -> None:
        assets = tmp_path / "assets"
        assets.mkdir()
        _create_asset(assets, "track-go-poster.jpg")

        season_dir = tmp_path / "season"
        season_dir.mkdir()

        copy_season_images(assets, season_dir, "2025", "Go")
        assert (season_dir / "poster.jpg").exists()

    def test_skips_when_assets_dir_missing(self, tmp_path: Path) -> None:
        season_dir = tmp_path / "season"
        season_dir.mkdir()
        # Should not raise
        copy_season_images(tmp_path / "nonexistent", season_dir, "2025", "Go")
