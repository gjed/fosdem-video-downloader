# cli-interface Delta

## ADDED Requirements

### Requirement: ICS File Option

The CLI SHALL accept an `--ics <file>` option that
specifies the path to a FOSDEM schedule ICS file.
When provided, talks SHALL be extracted from the ICS
file exactly as the current positional argument
behaviour works.

#### Scenario: Download from ICS file

- **WHEN** the user runs
  `fosdem_video --ics bookmarks.ics`
- **THEN** the tool parses the ICS file and
  downloads videos for all talks found

#### Scenario: ICS file does not exist

- **WHEN** the user provides `--ics missing.ics`
  and the file does not exist
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

### Requirement: Location Filter

The CLI SHALL accept a `--location <loc>` option
that filters talks by room/location. This option
SHALL only be valid when `--year` is also provided.

#### Scenario: Download videos for a specific location

- **WHEN** the user runs
  `fosdem_video --year 2025 --location janson`
- **THEN** only talks in the matching
  room/location are downloaded

#### Scenario: Location without year

- **WHEN** the user provides `--location` without
  `--year`
- **THEN** the CLI SHALL exit with an error
  indicating `--location` requires `--year`

### Requirement: Talk ID Filter

The CLI SHALL accept a `--talk <id>` option that
selects a single talk by its slug/ID. This option
SHALL only be valid when `--year` is also provided.

#### Scenario: Download a single talk by ID

- **WHEN** the user runs
  `fosdem_video --year 2025 --talk my_talk_slug`
- **THEN** only the video for the specified talk
  is downloaded

#### Scenario: Talk without year

- **WHEN** the user provides `--talk` without
  `--year`
- **THEN** the CLI SHALL exit with an error
  indicating `--talk` requires `--year`

### Requirement: Mutual Exclusivity of ICS and Year

The `--ics` and `--year` options SHALL be mutually
exclusive. The CLI SHALL require exactly one of
the two.

#### Scenario: Both ICS and year provided

- **WHEN** the user runs
  `fosdem_video --ics bookmarks.ics --year 2025`
- **THEN** the CLI SHALL exit with an error
  indicating that `--ics` and `--year` are
  mutually exclusive

#### Scenario: Neither ICS nor year provided

- **WHEN** the user runs `fosdem_video` with no
  input source
- **THEN** the CLI SHALL exit with an error
  indicating that one of `--ics` or `--year`
  is required

### Requirement: Video Format Selection

The CLI SHALL accept a `--format` option that
specifies the video format to download. Valid
values SHALL be `mp4` and `av1.webm`. The default
SHALL be `mp4`.

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
- **THEN** the CLI SHALL exit with an error
  listing the valid format choices

### Requirement: VTT Subtitle Control

The CLI SHALL download `.vtt` subtitle files by
default alongside each video. The CLI SHALL accept
a `--no-vtt` flag that disables subtitle downloads.

#### Scenario: Default subtitle download

- **WHEN** the user downloads a video without
  specifying `--no-vtt`
- **THEN** the corresponding `.vtt` file SHALL
  also be downloaded if available

#### Scenario: Skip subtitle download

- **WHEN** the user provides the `--no-vtt` flag
- **THEN** no `.vtt` subtitle files SHALL be
  downloaded

### Requirement: Output Directory Option

The CLI SHALL accept `-o, --output <path>` to
specify the root directory where downloaded files
are saved. The default SHALL be `./fosdem_videos`.
This replaces the previous `--output-dir` flag.

#### Scenario: Custom output directory

- **WHEN** the user runs
  `fosdem_video --ics bookmarks.ics --output ~/my_videos`
- **THEN** all downloaded files are saved under
  `~/my_videos`

#### Scenario: Default output directory

- **WHEN** the user does not provide `--output`
- **THEN** files are saved under
  `./fosdem_videos`

### Requirement: Jellyfin-Compatible Output Layout

The CLI SHALL accept a `--jellyfin` flag that
organises downloaded files into a folder hierarchy
compatible with Jellyfin media server. When
enabled, the output structure SHALL be
`<output>/Fosdem (<year>)/<room_name>/<video_name>/<video_file>`
where `<video_file>` includes the video and
optional `.vtt` subtitle. When `--jellyfin` is not
provided, the default flat layout
(`<output>/<year>/<slug>.<ext>`) SHALL be used.

#### Scenario: Jellyfin layout for a single video

- **WHEN** the user runs
  `fosdem_video --year 2026 --talk my_talk --jellyfin`
- **THEN** the video is saved to
  `<output>/Fosdem (2026)/<room_name>/my_talk/my_talk.mp4`
  and the VTT (if enabled) to
  `<output>/Fosdem (2026)/<room_name>/my_talk/my_talk.vtt`

#### Scenario: Jellyfin layout with WebM format

- **WHEN** the user runs
  `fosdem_video --year 2026 --jellyfin --format av1.webm`
- **THEN** videos are saved as
  `<output>/Fosdem (2026)/<room_name>/<video_name>/<video_name>.av1.webm`

#### Scenario: Default layout without jellyfin flag

- **WHEN** the user does not provide `--jellyfin`
- **THEN** files are saved in the default flat
  structure `<output>/<year>/<slug>.<ext>`
