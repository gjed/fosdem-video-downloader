# cli-interface Delta

## RENAMED Requirements

- FROM: `### Requirement: Location Filter`
- TO: `### Requirement: Track Filter`

## MODIFIED Requirements

### Requirement: Track Filter

The CLI SHALL accept a `--track <name>` option that
filters talks by track name (case-insensitive).
This option SHALL only be valid when `--year` is
also provided. This replaces the previous
`--location` option which filtered by room.

#### Scenario: Download videos for a specific track

- **WHEN** the user runs
  `fosdem-video --year 2025 --track Containers`
- **THEN** only talks in the matching track are
  downloaded

#### Scenario: Track without year

- **WHEN** the user provides `--track` without
  `--year`
- **THEN** the CLI SHALL exit with an error
  indicating `--track` requires `--year`

### Requirement: Jellyfin-Compatible Output Layout

The CLI SHALL accept a `--jellyfin` flag that
organises downloaded files into a folder hierarchy
compatible with Jellyfin media server, following
the TV series model. When enabled with `--year`,
the output structure SHALL be
`<output>/Fosdem (<year>)/<track>/<slug>/<slug>.<ext>`
where each FOSDEM edition maps to a TV show, each
track to a season, and each talk to an episode.
The system SHALL generate NFO metadata sidecars at
all three levels: `tvshow.nfo` in the show root,
`season.nfo` in each track directory, and
`<slug>.nfo` alongside each video. When
`--jellyfin` is not provided, the default flat
layout (`<output>/<year>/<slug>.<ext>`) SHALL be
used. When track metadata is not available (ICS
mode), the system SHALL fall back to the `location`
field as the grouping directory and no NFO files
SHALL be generated.

#### Scenario: Jellyfin TV series layout for year mode

- **WHEN** the user runs
  `fosdem-video --year 2026 --jellyfin`
- **THEN** the output contains `tvshow.nfo` in
  `Fosdem (2026)/`, `season.nfo` in each track
  directory, and for each talk: the video, optional
  VTT, and `<slug>.nfo` in
  `Fosdem (2026)/<track>/<slug>/`

#### Scenario: Jellyfin layout with WebM format

- **WHEN** the user runs
  `fosdem-video --year 2026 --jellyfin --format av1.webm`
- **THEN** videos are saved as
  `<output>/Fosdem (2026)/<track>/<video_name>/<video_name>.av1.webm`

#### Scenario: Default layout without jellyfin flag

- **WHEN** the user does not provide `--jellyfin`
- **THEN** files are saved in the default flat
  structure `<output>/<year>/<slug>.<ext>` with no
  NFO files

#### Scenario: Jellyfin layout falls back to location for ICS mode

- **WHEN** the user runs
  `fosdem-video --ics bookmarks.ics --jellyfin`
- **THEN** the system uses the `location` field
  instead of track, and no `.nfo` files are
  generated at any level
