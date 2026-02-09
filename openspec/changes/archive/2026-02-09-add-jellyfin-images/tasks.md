<!-- markdownlint-disable MD041 -->

## 1. Image resolution module

- [x] 1.1 Create `fosdem_video/images.py` with an `resolve_asset` function
  that searches `assets/` for a given prefix, type, and optional number
  using the year-first, default-fallback resolution order
- [x] 1.2 Create `copy_show_images(assets_dir, show_dir, year)` that resolves
  and copies all image types (primary, logo, backdrop, banner, thumb)
  to the show root using Jellyfin filenames (`poster`, `logo`, `backdrop`,
  `banner`, `thumb`) — including numbered backdrop variants
- [x] 1.3 Create `copy_season_images(assets_dir, season_dir, year, track)`
  that resolves and copies season-level images using the track slug —
  target filenames: `cover`, `logo`, `backdrop`, `banner`, `thumb`
- [x] 1.4 Both functions SHALL log a warning per missing image type and a
  single warning if the `assets/` directory is missing

## 2. Integration into download pipeline

- [x] 2.1 In `create_dirs` (`download.py`), after writing `tvshow.nfo`, call
  `copy_show_images` for each show root directory
- [x] 2.2 In `create_dirs`, after writing `season.nfo`, call
  `copy_season_images` for each track directory
- [x] 2.3 In `regenerate_nfos`, add the same image-copying calls after
  NFO generation at show and season levels

## 3. Validation and cleanup

- [x] 3.1 Rename `assets/fosdem_logo.png` to `assets/fosdem-logo.png` to
  match the naming convention (or document that users should do this)
- [x] 3.2 Manual test: run with `--jellyfin --year 2026` and verify
  images are copied to the correct directories
- [x] 3.3 Manual test: run with `--regenerate-nfo --jellyfin --year 2026`
  and verify images are refreshed
- [x] 3.4 Verify warnings are logged for missing image types
