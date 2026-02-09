<!-- markdownlint-disable MD041 -->

## ADDED Requirements

### Requirement: Jellyfin Show-Level Metadata Images

The system SHALL copy metadata images from the `assets/` directory into the show
root directory `Fosdem (<year>)/` during directory creation when `--jellyfin` is
enabled and talks have rich metadata (year mode). The system SHALL look for each
image type (primary, logo, backdrop, banner, thumb) using the following
resolution order:

1. Year-specific: `fosdem-<year>-<type>.<ext>` (trying jpg, jpeg, png, webp)
1. Year-specific numbered variants: `fosdem-<year>-<type>-<n>.<ext>`
1. Default: `fosdem-<type>.<ext>`
1. Default numbered variants: `fosdem-<type>-<n>.<ext>`

Images SHALL be copied using Jellyfin's expected filenames: `poster.<ext>` for
primary, `logo.<ext>` for logo, `backdrop.<ext>` for backdrop (with
`backdrop2.<ext>`, `backdrop3.<ext>` for numbered variants), `banner.<ext>` for
banner, and `thumb.<ext>` for thumb. The original file extension SHALL be
preserved.

When no matching asset is found for an image type, the system SHALL log a
warning and continue without failing.

When the `assets/` directory does not exist at runtime, the system SHALL log a
warning and skip all image operations.

#### Scenario: Year-specific show images copied to show root

- **WHEN** `--jellyfin` is enabled with `--year 2026` and `assets/` contains
  `fosdem-2026-primary.jpg` and `fosdem-2026-banner.png`
- **THEN** the show root `Fosdem (2026)/` contains `poster.jpg` and
  `banner.png` copied from those assets

#### Scenario: Default fallback when no year-specific image exists

- **WHEN** `--jellyfin` is enabled with `--year 2025` and `assets/` contains
  `fosdem-backdrop.png` but no `fosdem-2025-backdrop.*`
- **THEN** the show root `Fosdem (2025)/` contains `backdrop.png` copied from
  the default `fosdem-backdrop.png`

#### Scenario: Multiple backdrop images copied with Jellyfin numbering

- **WHEN** `assets/` contains `fosdem-backdrop.png` and `fosdem-backdrop-2.jpg`
- **THEN** the show root contains `backdrop.png` and `backdrop2.jpg`

#### Scenario: Missing image type logs a warning

- **WHEN** `assets/` does not contain any file matching `fosdem[-<year>]-logo.*`
- **THEN** the system logs a warning like "No logo image found for show level"
  and continues normally

#### Scenario: Missing assets directory logs a warning

- **WHEN** the `assets/` directory does not exist at runtime
- **THEN** the system logs a single warning and skips all image operations
  without failing

#### Scenario: No images copied without jellyfin flag

- **WHEN** `--jellyfin` is not provided
- **THEN** no images are copied regardless of what exists in `assets/`

#### Scenario: No images copied in ICS mode

- **WHEN** `--ics` is used (no rich metadata)
- **THEN** no images are copied at any level

### Requirement: Jellyfin Season-Level Metadata Images

The system SHALL copy metadata images from the `assets/` directory into each
track directory `Fosdem (<year>)/<track>/` during directory creation when
`--jellyfin` is enabled and talks have rich metadata (year mode). The system
SHALL look for each image type using the track's slugified name in the following
resolution order:

1. Year-specific: `fosdem-<year>-<track-slug>-<type>.<ext>`
1. Year-specific numbered variants: `fosdem-<year>-<track-slug>-<type>-<n>.<ext>`
1. Default: `fosdem-<track-slug>-<type>.<ext>`
1. Default numbered variants: `fosdem-<track-slug>-<type>-<n>.<ext>`

Where `<track-slug>` is the track name converted to a lowercase, hyphenated
slug (using the same `slugify` function used for display names).

Images SHALL be copied using Jellyfin's expected filenames: `cover.<ext>` for
primary, `logo.<ext>` for logo, `backdrop.<ext>` for backdrop, `banner.<ext>`
for banner, and `thumb.<ext>` for thumb. Numbered backdrop variants SHALL use
`backdrop2.<ext>`, `backdrop3.<ext>`, etc.

When no matching asset is found for a season image type, the system SHALL log a
warning and continue without failing.

#### Scenario: Season images copied to track directory

- **WHEN** `--jellyfin` is enabled with `--year 2026` and `assets/` contains
  `fosdem-2026-containers-primary.jpg`
- **THEN** the track directory `Fosdem (2026)/Containers/` contains
  `cover.jpg` copied from that asset

#### Scenario: Default season image fallback

- **WHEN** `assets/` contains `fosdem-go-logo.png` but no
  `fosdem-2026-go-logo.*`
- **THEN** the Go track directory contains `logo.png` copied from the default

#### Scenario: Missing season image logs a warning

- **WHEN** `assets/` does not contain any file matching the track's slug for a
  given image type
- **THEN** the system logs a warning and continues normally

### Requirement: Image Copying During NFO Regeneration

The system SHALL re-copy metadata images from `assets/` to show and season
directories when `--regenerate-nfo` is used, following the same resolution and
placement logic as during initial directory creation.

#### Scenario: Images refreshed during NFO regeneration

- **WHEN** the user runs with `--regenerate-nfo --jellyfin --year 2026`
- **THEN** show-level and season-level images are re-copied from `assets/`
  alongside the regenerated NFO files
