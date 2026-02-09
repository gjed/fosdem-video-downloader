<!-- markdownlint-disable MD041 -->

## Context

Jellyfin recognises metadata images placed alongside NFO files in the media
folder hierarchy. The Jellyfin docs for TV Shows list these supported image
types per level:

| Filename  | Type     | Series | Season | Episode |
| --------- | -------- | ------ | ------ | ------- |
| poster    | Primary  | yes    | yes    | yes     |
| folder    | Primary  | yes    | yes    | yes     |
| cover     | Primary  | yes    | yes    | yes     |
| backdrop  | Backdrop | yes    | yes    |         |
| fanart    | Backdrop | yes    | yes    |         |
| banner    | Banner   | yes    | yes    |         |
| logo      | Logo     | yes    | yes    |         |
| clearlogo | Logo     | yes    | yes    |         |
| landscape | Thumb    | yes    | yes    |         |
| thumb     | Thumb    | yes    | yes    |         |

Multiple backdrop images are supported by appending a number
(e.g. `backdrop-2.jpg`).

The tool already bundles an `assets/` directory with sample images. Users can
add their own images following the naming convention.

## Goals / Non-Goals

- **Goal**: Copy show-level and season-level images from `assets/` into the
  Jellyfin directory tree during `create_dirs` (and `regenerate_nfos`).
- **Goal**: Year-specific images take priority, with a generic fallback.
- **Goal**: Season images keyed by track slug, with same year/default fallback.
- **Goal**: Log warnings for missing images without failing.
- **Non-Goal**: Episode-level thumbnail images (not requested).
- **Non-Goal**: Downloading images from the internet.
- **Non-Goal**: Image generation or resizing.

## Decisions

### Asset naming convention

Images in `assets/` follow this naming pattern:

**Show-level**: `fosdem[-<year>]-<type>[<-number>].<ext>`

- `fosdem-2026-primary.jpg` — year-specific primary image
- `fosdem-primary.jpg` — default primary image (any year)
- `fosdem-backdrop.png` — default backdrop
- `fosdem-backdrop-2.jpg` — second backdrop image
- `fosdem-2026-banner.png` — year-specific banner

**Season-level**: `fosdem[-<year>]-<track-slug>-<type>[<-number>].<ext>`

- `fosdem-2026-containers-primary.jpg` — year-specific for Containers track
- `fosdem-containers-primary.jpg` — default for Containers track

Where:

- `<year>` is optional (4 digits)
- `<type>` is one of: `primary`, `logo`, `backdrop`, `banner`, `thumb`
- `<track-slug>` is the slugified track name (lowercase, hyphens)
- `<number>` is an optional numeric suffix for multiple images of same type
- `<ext>` is `jpg`, `jpeg`, `png`, or `webp`

### Resolution order

For each image type at each level:

1. Look for year-specific file: `fosdem-<year>-<type>.<ext>` (try all
   supported extensions: jpg, jpeg, png, webp)
1. Look for numbered year-specific variants: `fosdem-<year>-<type>-<n>.<ext>`
1. Fall back to default: `fosdem-<type>.<ext>`
1. Fall back to numbered defaults: `fosdem-<type>-<n>.<ext>`
1. If nothing found, log a warning and skip that type.

For seasons, prepend the track slug between the year (or `fosdem`) prefix and
the type: `fosdem[-<year>]-<track-slug>-<type>.<ext>`.

### Jellyfin target filenames

Images are copied to the target directory using Jellyfin's expected filenames:

| Type     | Show directory   | Season directory |
| -------- | ---------------- | ---------------- |
| Primary  | `poster.{ext}`   | `cover.{ext}`    |
| Logo     | `logo.{ext}`     | `logo.{ext}`     |
| Backdrop | `backdrop.{ext}` | `backdrop.{ext}` |
| Banner   | `banner.{ext}`   | `banner.{ext}`   |
| Thumb    | `thumb.{ext}`    | `thumb.{ext}`    |

Numbered variants use Jellyfin's convention: `backdrop2.{ext}`,
`backdrop3.{ext}`, etc. (the first has no number).

### Integration point

Image copying is triggered inside `create_dirs` and `regenerate_nfos`,
immediately after writing NFO files at each level. This keeps image placement
co-located with the rest of the metadata setup.

### Assets directory location

The `assets/` directory is located relative to the package root (sibling of
`fosdem_video/`). The path is resolved at runtime using
`Path(__file__).resolve().parent.parent / "assets"`.

### Handling the existing `fosdem_logo.png`

The existing `fosdem_logo.png` uses underscores instead of hyphens and does not
match the naming convention. It will be ignored by the resolver. Users can
rename it to `fosdem-logo.png` to have it picked up as the default logo.

## Risks / Trade-offs

- **Risk**: `assets/` directory missing at runtime (e.g. pip install without
  data files).
  **Mitigation**: Log a single warning if `assets/` doesn't exist and skip all
  image operations. No crash.

- **Risk**: Large image files inflating the package.
  **Mitigation**: Images are already in the repo and are opt-in (only copied
  when `--jellyfin` is used).

## Open Questions

None — the design is straightforward file-copy logic with a naming convention.
