# Change: Add Jellyfin metadata images for TV series layout

## Why

When using `--jellyfin`, Jellyfin's TV series layout supports metadata images
(primary/cover, logo, backdrop, banner, thumb) at the show and season levels.
Currently the tool generates NFO sidecars but no artwork. Adding image support
will give Jellyfin users a polished library presentation out of the box, using
FOSDEM branding assets bundled in the `assets/` directory.

## What Changes

- Copy show-level metadata images (primary, logo, backdrop, banner, thumb) from
  `assets/` into the show root directory `Fosdem (<year>)/` during directory
  creation when `--jellyfin` is enabled.
- Copy season-level metadata images from `assets/` into each track directory
  `Fosdem (<year>)/<track>/` during directory creation.
- Image resolution follows a year-specific-first, default-fallback strategy:
  look for `fosdem-<year>-<type>.<ext>` first, then `fosdem-<type>.<ext>`.
  For seasons: `fosdem-<year>-<track>-<type>.<ext>` first, then
  `fosdem-<track>-<type>.<ext>`.
- Log a warning when an image type has no matching asset file (not an error).
- Support numbered backdrop variants (e.g. `fosdem-backdrop-2.jpg`).

## Impact

- Affected specs: `video-download`
- Affected code: `fosdem_video/download.py` (create_dirs, regenerate_nfos),
  new helper module or functions for image resolution and copying
- New runtime dependency: none (uses stdlib `shutil.copy2` / `pathlib`)
- `assets/` directory: already contains sample images; naming convention
  documented for users who want to add their own
