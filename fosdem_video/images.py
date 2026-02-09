"""Jellyfin metadata image resolution and copying from bundled assets."""

from __future__ import annotations

import logging
import shutil
from pathlib import Path

from fosdem_video.models import slugify

logger = logging.getLogger(__name__)

# Supported image extensions in search order.
_EXTENSIONS = ("jpg", "jpeg", "png", "webp")

# Jellyfin image types for the show level: (asset_type, target_name).
_SHOW_IMAGE_TYPES: list[tuple[str, str]] = [
    ("primary", "poster"),
    ("logo", "logo"),
    ("backdrop", "backdrop"),
    ("banner", "banner"),
]

# Jellyfin image types for the season level: (asset_type, target_name).
_SEASON_IMAGE_TYPES: list[tuple[str, str]] = [
    ("primary", "cover"),
    ("logo", "logo"),
    ("backdrop", "backdrop"),
    ("banner", "banner"),
    ("poster", "poster"),
]

# Location of the bundled assets directory (sibling of fosdem_video/).
_ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"


def _find_assets(
    assets_dir: Path,
    prefix: str,
    image_type: str,
) -> list[Path]:
    """
    Find all matching asset files for a given prefix and image type.

    Looks for ``<prefix>-<image_type>.<ext>`` and numbered variants
    ``<prefix>-<image_type>-<n>.<ext>`` across all supported extensions.

    Returns a list of paths sorted so the un-numbered file comes first,
    followed by numbered variants in ascending order.
    """
    matches: list[tuple[int, Path]] = []
    for ext in _EXTENSIONS:
        # Un-numbered variant
        candidate = assets_dir / f"{prefix}-{image_type}.{ext}"
        if candidate.is_file():
            matches.append((0, candidate))
        # Numbered variants: <prefix>-<type>-2.ext, <prefix>-<type>-3.ext, …
        for numbered in assets_dir.glob(f"{prefix}-{image_type}-[0-9]*.{ext}"):
            # Extract the number suffix
            stem = numbered.stem  # e.g. "fosdem-backdrop-2"
            suffix_part = stem.rsplit("-", 1)[-1]
            try:
                num = int(suffix_part)
            except ValueError:
                continue
            matches.append((num, numbered))
    # Deduplicate by path and sort by number
    seen: set[Path] = set()
    unique: list[tuple[int, Path]] = []
    for num, path in matches:
        if path not in seen:
            seen.add(path)
            unique.append((num, path))
    unique.sort(key=lambda t: t[0])
    return [p for _, p in unique]


def resolve_assets(
    assets_dir: Path,
    year: str,
    image_type: str,
    *,
    track_slug: str = "",
) -> list[Path]:
    """
    Resolve asset files for *image_type* using year-first, default-fallback.

    For show-level images (no *track_slug*):
      1. ``fosdem-<year>-<type>.<ext>``  (+ numbered variants)
      2. ``fosdem-<type>.<ext>``         (+ numbered variants)

    For season-level images (with *track_slug*):
      1. ``fosdem-<year>-<track>-<type>.<ext>``  (+ numbered)
      2. ``fosdem-<track>-<type>.<ext>``         (+ numbered)
      3. ``track-<track>-<type>.<ext>``          (+ numbered)

    Returns a (possibly empty) list of paths.
    """
    if track_slug:
        # Year-specific season: fosdem-<year>-<track>-<type>.<ext>
        result = _find_assets(assets_dir, f"fosdem-{year}-{track_slug}", image_type)
        if result:
            return result
        # Default season: fosdem-<track>-<type>.<ext>
        result = _find_assets(assets_dir, f"fosdem-{track_slug}", image_type)
        if result:
            return result
        # Track-prefixed fallback: track-<track>-<type>.<ext>
        return _find_assets(assets_dir, f"track-{track_slug}", image_type)

    # Year-specific show
    result = _find_assets(assets_dir, f"fosdem-{year}", image_type)
    if result:
        return result
    # Default show
    return _find_assets(assets_dir, "fosdem", image_type)


def _copy_image(src: Path, dest: Path) -> bool:
    """
    Copy *src* to *dest*, preserving metadata.

    Creates the parent directory if it does not exist.  Returns ``True``
    on success, ``False`` on failure (logged, never raises).
    """
    try:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        logger.debug("Copied image %s -> %s", src.name, dest)
    except Exception:
        logger.exception("Failed to copy image %s -> %s", src.name, dest)
        return False
    return True


def _jellyfin_target_name(base_name: str, index: int, ext: str) -> str:
    """
    Build the Jellyfin target filename for an image.

    The first image (index 0) uses ``<base_name>.<ext>``.  Subsequent
    images use ``<base_name><n>.<ext>`` where *n* starts at 2
    (e.g. ``backdrop2.jpg``, ``backdrop3.jpg``).
    """
    if index == 0:
        return f"{base_name}.{ext}"
    return f"{base_name}{index + 1}.{ext}"


def copy_show_images(
    assets_dir: Path,
    show_dir: Path,
    year: str,
) -> None:
    """
    Copy show-level metadata images into the Jellyfin show root directory.

    Resolves each image type from *assets_dir* using year-first fallback,
    then copies to *show_dir* with the Jellyfin-expected filename.
    Logs a warning for each image type that has no matching asset.
    """
    if not assets_dir.is_dir():
        logger.warning(
            "Assets directory not found: %s — skipping image operations",
            assets_dir,
        )
        return

    for asset_type, show_target in _SHOW_IMAGE_TYPES:
        found = resolve_assets(assets_dir, year, asset_type)
        if not found:
            logger.warning("No %s image found for show level (year %s)", asset_type, year)
            continue
        for idx, src in enumerate(found):
            ext = src.suffix.lstrip(".")
            target_name = _jellyfin_target_name(show_target, idx, ext)
            _copy_image(src, show_dir / target_name)


def copy_season_images(
    assets_dir: Path,
    season_dir: Path,
    year: str,
    track: str,
) -> None:
    """
    Copy season-level metadata images into a Jellyfin track directory.

    Resolves each image type from *assets_dir* using the slugified track
    name and year-first fallback, then copies to *season_dir* with the
    Jellyfin-expected filename.
    Logs a warning for each image type that has no matching asset.
    """
    if not assets_dir.is_dir():
        logger.warning(
            "Assets directory not found: %s — skipping image operations",
            assets_dir,
        )
        return

    track_slug = slugify(track)
    for asset_type, season_target in _SEASON_IMAGE_TYPES:
        found = resolve_assets(assets_dir, year, asset_type, track_slug=track_slug)
        if not found:
            logger.warning(
                "No %s image found for season '%s' (year %s)",
                asset_type,
                track,
                year,
            )
            continue
        target_base = season_target
        for idx, src in enumerate(found):
            ext = src.suffix.lstrip(".")
            target_name = _jellyfin_target_name(target_base, idx, ext)
            _copy_image(src, season_dir / target_name)


def get_assets_dir() -> Path:
    """Return the path to the bundled assets directory."""
    return _ASSETS_DIR
