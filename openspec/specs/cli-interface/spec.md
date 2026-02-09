# cli-interface Specification

## Purpose

Defines the command-line interface for the FOSDEM video
downloader, including input modes (ICS file or year-based
schedule), filtering options, output format and layout
controls, and argument validation rules.

## Requirements

### Requirement: ICS File Option

The CLI SHALL accept an `--ics <file>` option that
specifies the path to a FOSDEM schedule ICS file.
When provided, talks SHALL be extracted from the ICS
file exactly as the current positional argument
behaviour works.

#### Scenario: Download from ICS file

- **WHEN** the user runs
  `fosdem_video --ics bookmarks.ics`
- **THEN** the tool parses the ICS file and downloads
  videos for all talks found

#### Scenario: ICS file does not exist

- **WHEN** the user provides `--ics missing.ics` and
  the file does not exist
- **THEN** the CLI SHALL exit with an error message
  indicating the file was not found

### Requirement: Year-Based Input Mode

The CLI SHALL accept a `--year <YYYY>` option as an
alternative to `--ics`. When only `--year` is
provided, the tool SHALL fetch the FOSDEM Pentabarf
schedule XML for that year and download videos for
all talks in that edition.

#### Scenario: Download entire year

- **WHEN** the user runs
  `fosdem_video --year 2025`
- **THEN** the tool fetches the schedule from
  `https://fosdem.org/2025/schedule/xml` and
  downloads all available videos

#### Scenario: Schedule XML not available

- **WHEN** the user provides `--year` for a year
  whose schedule XML cannot be fetched
- **THEN** the CLI SHALL exit with an error
  describing the failure

### Requirement: Talk ID Filter

The CLI SHALL accept a `--talk <id>` option that
selects a single talk by its slug/ID. This option
SHALL only be valid when `--year` is also provided.

#### Scenario: Download a single talk by ID

- **WHEN** the user runs
  `fosdem_video --year 2025 --talk my_talk_slug`
- **THEN** only the video for the specified talk is
  downloaded

#### Scenario: Talk without year

- **WHEN** the user provides `--talk` without `--year`
- **THEN** the CLI SHALL exit with an error
  indicating `--talk` requires `--year`

### Requirement: Mutual Exclusivity of ICS and Year

The `--ics` and `--year` options SHALL be mutually
exclusive. The CLI SHALL require exactly one of the
two.

#### Scenario: Both ICS and year provided

- **WHEN** the user runs
  `fosdem_video --ics bookmarks.ics --year 2025`
- **THEN** the CLI SHALL exit with an error
  indicating that `--ics` and `--year` are mutually
  exclusive

#### Scenario: Neither ICS nor year provided

- **WHEN** the user runs `fosdem_video` with no
  input source
- **THEN** the CLI SHALL exit with an error
  indicating that one of `--ics` or `--year` is
  required

### Requirement: Video Format Selection

The CLI SHALL accept a `--format` option that
specifies the video format to download. Valid values
SHALL be `mp4` and `av1.webm`. The default SHALL be
`mp4`.

#### Scenario: Download in default format

- **WHEN** the user runs
  `fosdem_video --ics bookmarks.ics` without
  `--format`
- **THEN** videos are downloaded as `.mp4` files

#### Scenario: Download in WebM format

- **WHEN** the user runs
  `fosdem_video --ics bookmarks.ics --format av1.webm`
- **THEN** videos are downloaded as `.av1.webm`
  files

#### Scenario: Invalid format value

- **WHEN** the user provides `--format mkv`
- **THEN** the CLI SHALL exit with an error listing
  the valid format choices

### Requirement: VTT Subtitle Control

The CLI SHALL download `.vtt` subtitle files by
default alongside each video. The CLI SHALL accept a
`--no-vtt` flag that disables subtitle downloads.

#### Scenario: Default subtitle download

- **WHEN** the user downloads a video without
  specifying `--no-vtt`
- **THEN** the corresponding `.vtt` file SHALL also
  be downloaded if available

#### Scenario: Skip subtitle download

- **WHEN** the user provides the `--no-vtt` flag
- **THEN** no `.vtt` subtitle files SHALL be
  downloaded

### Requirement: Output Directory Option

The CLI SHALL accept `-o, --output <path>` to
specify the root directory where downloaded files are
saved. The default SHALL be `./fosdem_videos`. This
replaces the previous `--output-dir` flag.

#### Scenario: Custom output directory

- **WHEN** the user runs
  `fosdem_video --ics bookmarks.ics --output ~/my_videos`
- **THEN** all downloaded files are saved under
  `~/my_videos`

#### Scenario: Default output directory

- **WHEN** the user does not provide `--output`
- **THEN** files are saved under `./fosdem_videos`

### Requirement: Jellyfin-Compatible Output Layout

The CLI SHALL accept a `--jellyfin` flag that
organises downloaded files into a folder hierarchy
compatible with Jellyfin media server, following the
TV series model. When enabled with `--year`, the
output structure SHALL be
`<output>/Fosdem (<year>)/<track>/<slug>/<slug>.<ext>`
where each FOSDEM edition maps to a TV show, each
track to a season, and each talk to an episode. The
system SHALL generate NFO metadata sidecars at all
three levels: `tvshow.nfo` in the show root,
`season.nfo` in each track directory, and
`<slug>.nfo` alongside each video. When `--jellyfin`
is not provided, the default flat layout
(`<output>/<year>/<slug>.<ext>`) SHALL be used. When
track metadata is not available (ICS mode), the
system SHALL fall back to the `location` field as
the grouping directory and no NFO files SHALL be
generated.

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

### Requirement: Track Filter

The CLI SHALL accept a `--track <name>` option that
filters talks by track name (case-insensitive). This
option SHALL only be valid when `--year` is also
provided. This replaces the previous `--location`
option which filtered by room.

#### Scenario: Download videos for a specific track

- **WHEN** the user runs
  `fosdem-video --year 2025 --track Containers`
- **THEN** only talks in the matching track are
  downloaded

#### Scenario: Track without year

- **WHEN** the user provides `--track` without `--year`
- **THEN** the CLI SHALL exit with an error
  indicating `--track` requires `--year`
