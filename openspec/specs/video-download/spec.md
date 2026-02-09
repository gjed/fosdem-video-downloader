# video-download Specification

## Purpose

Defines how the tool discovers, downloads, and organises
FOSDEM talk videos, including schedule XML parsing, URL
construction, subtitle handling, file naming, output
directory layouts, and Jellyfin NFO sidecar generation.

## Requirements

### Requirement: Schedule XML Talk Discovery

The system SHALL fetch and parse the FOSDEM Pentabarf
schedule XML (at
`https://fosdem.org/{year}/schedule/xml`) to discover
talks. Each talk SHALL be converted into a `Talk`
with a video URL constructed from the year, room, and
talk slug using the selected format extension.

#### Scenario: Parse schedule XML for a year

- **WHEN** the user specifies `--year 2025`
- **THEN** the system fetches
  `https://fosdem.org/2025/schedule/xml`, parses all
  events, and builds video URLs for each talk

#### Scenario: Filter by location from schedule XML

- **WHEN** the user specifies
  `--year 2025 --location janson`
- **THEN** only events whose room matches `janson`
  (case-insensitive, stripped of punctuation) are
  included

#### Scenario: Filter by talk ID from schedule XML

- **WHEN** the user specifies
  `--year 2025 --talk my_talk_slug`
- **THEN** only the event whose slug matches
  `my_talk_slug` is included

### Requirement: Format-Aware Video URLs

The system SHALL construct video download URLs using
the format specified by the `--format` flag. The URL
pattern SHALL be
`https://video.fosdem.org/{year}/{location}/{slug}.{format_extension}`
where `format_extension` is either `mp4` or
`av1.webm`.

#### Scenario: MP4 URL construction

- **WHEN** the format is `mp4`
- **THEN** the video URL ends with `.mp4`

#### Scenario: WebM URL construction

- **WHEN** the format is `av1.webm`
- **THEN** the video URL ends with `.av1.webm`

### Requirement: VTT Subtitle Download

The system SHALL, by default, attempt to download a
`.vtt` subtitle file for each talk. The VTT URL SHALL
follow the pattern
`https://video.fosdem.org/{year}/{location}/{slug}.vtt`.
If the VTT file returns a 404, the system SHALL log a
warning and continue without failing. When the
`--no-vtt` flag is provided, subtitle downloads SHALL
be skipped entirely.

#### Scenario: VTT file exists and is downloaded

- **WHEN** a video is downloaded and `--no-vtt` is
  not set
- **THEN** the system also downloads the
  corresponding `.vtt` file to the same output
  directory

#### Scenario: VTT file does not exist on server

- **WHEN** the `.vtt` URL returns a 404
- **THEN** the system logs a warning and does not
  fail the overall download

#### Scenario: VTT download disabled

- **WHEN** `--no-vtt` is provided
- **THEN** no `.vtt` download is attempted

### Requirement: Format-Aware File Naming

Downloaded video files SHALL use the correct
extension matching the selected format. The
`is_downloaded` check SHALL also use the correct
extension so previously downloaded files in the
selected format are properly detected.

#### Scenario: File extension matches format

- **WHEN** the format is `av1.webm`
- **THEN** downloaded files are named
  `{slug}.av1.webm` and duplicate detection checks
  for that extension

### Requirement: Talk Location Metadata

The `Talk` data model SHALL include a `location`
field containing the room/track name. This field
SHALL be populated from the ICS `LOCATION` property
or the Pentabarf XML `<room>` element. The location
SHALL be used for Jellyfin folder layout and for
constructing video URLs.

#### Scenario: Location populated from ICS

- **WHEN** a talk is parsed from an ICS file
- **THEN** the `Talk.location` field contains the
  normalised room name extracted from the event's
  LOCATION property

#### Scenario: Location populated from schedule XML

- **WHEN** a talk is parsed from the Pentabarf
  schedule XML
- **THEN** the `Talk.location` field contains the
  room name from the `<room>` element

### Requirement: Jellyfin Output Path Construction

When `--jellyfin` is enabled, the system SHALL write
each video (and its optional VTT and NFO) into a
per-talk subfolder following the pattern
`<output>/Fosdem (<year>)/<track>/<slug>/<slug>.<ext>`.
The `<track>` SHALL be the track name from the talk
metadata. When track is not available (ICS mode), the
system SHALL fall back to the `location` field.
Directory creation SHALL happen automatically before
downloads begin. When talks carry rich metadata (year
mode), the system SHALL also write `tvshow.nfo` in
the show root and `season.nfo` in each track
directory during directory creation.

#### Scenario: Jellyfin directory tree uses track

- **WHEN** `--jellyfin` is enabled and talks are
  discovered via `--year`
- **THEN** each track gets its own subdirectory
  under `Fosdem (<year>)/`, and each talk gets a
  subfolder within its track directory

#### Scenario: Jellyfin falls back to location when track is empty

- **WHEN** `--jellyfin` is enabled and talks are
  discovered via `--ics` (no track metadata)
- **THEN** the system uses the `location` field as
  the grouping directory

#### Scenario: VTT placed alongside video in Jellyfin layout

- **WHEN** `--jellyfin` is enabled and `--no-vtt` is
  not set
- **THEN** the `.vtt` file is saved in the same
  per-talk subfolder as the video file

#### Scenario: Show and season NFO written during directory creation

- **WHEN** `--jellyfin` is enabled and `--year` is
  used
- **THEN** `tvshow.nfo` is written once in
  `Fosdem (<year>)/` and `season.nfo` once in each
  track directory, alongside the per-episode
  `<slug>.nfo` files

### Requirement: Default Flat Output Path

When `--jellyfin` is not provided, the system SHALL
use the default flat layout
`<output>/<year>/<slug>.<ext>` for both video and
VTT files.

#### Scenario: Default flat layout

- **WHEN** `--jellyfin` is not provided
- **THEN** files are saved as
  `<output>/<year>/<slug>.<ext>` with no room or
  per-talk subdirectories

### Requirement: Rich Talk Metadata from Schedule XML

The `Talk` data model SHALL include optional metadata
fields populated from the FOSDEM Pentabarf schedule
XML: title, track, date, start time, duration, room
(human-readable), event URL, language, event type,
abstract (HTML-stripped), description
(HTML-stripped), feedback URL, and persons (list of
speaker names). These fields SHALL default to empty
values when not available (e.g. ICS mode).

#### Scenario: Metadata populated from schedule XML

- **WHEN** a talk is parsed from the Pentabarf
  schedule XML
- **THEN** all available metadata fields (title,
  track, date, start, duration, room, event_url,
  language, event_type, abstract, description,
  feedback_url, persons) are populated from the
  corresponding XML elements

#### Scenario: Metadata absent in ICS mode

- **WHEN** a talk is parsed from an ICS file
- **THEN** metadata fields default to empty strings
  and empty lists, and the system continues to
  function normally

### Requirement: Jellyfin NFO Sidecar Generation (TV Series Model)

When `--jellyfin` is enabled and talks have rich
metadata (year mode), the system SHALL generate
Jellyfin-compatible `.nfo` XML sidecar files at
three levels matching the TV series model:

**Show level** — `tvshow.nfo` (root tag `<tvshow>`)
placed in the show root directory
`Fosdem (<year>)/`:

- `title` / `showtitle` — `FOSDEM <year>`
- `plot` — a short description of the FOSDEM
  conference
- `premiered` — `<year>-02-01`
- `studio` — `FOSDEM`
- `genre` — `Technology`
- `tag` — `conference`, `open-source`
- `uniqueid` (type `fosdem`) — `fosdem-<year>`

**Season level** — `season.nfo` (root tag
`<season>`) placed in each track directory
`Fosdem (<year>)/<track>/`:

- `title` — track name
- `seasonnumber` — the track's position in the
  sorted track list (1-based, alphabetical)
- `plot` — a brief description identifying the
  track

**Episode level** — `<slug>.nfo` (root tag
`<episodedetails>`) placed alongside each downloaded
video:

- `title` — talk title
- `showtitle` — `FOSDEM <year>`
- `season` — track name (string)
- `seasonnumber` — alphabetical index of the track
  (1-based integer)
- `episode` — 1-based position of the talk within
  its track, ordered by schedule date and start time
- `plot` — abstract, followed by description if
  present, followed by a metadata block containing
  slug, feedback URL, language, and event type
- `aired` — talk date (ISO format)
- `runtime` — duration in minutes
- `studio` — room name
- `uniqueid` (type `fosdem`) — the talk slug
- `trailer` — event URL
- `director` — each person/speaker as a separate
  `<director>` element

Episode numbering SHALL be computed by grouping
talks by track, sorting each group by
`(date, start)` from the schedule, and assigning
consecutive 1-based numbers. Season numbering SHALL
be the 1-based alphabetical index of the track name.

#### Scenario: All three NFO levels generated in Jellyfin year mode

- **WHEN** `--jellyfin` is enabled and `--year` is
  used
- **THEN** `tvshow.nfo` is written in the show root,
  `season.nfo` in each track directory, and
  `<slug>.nfo` alongside each successfully downloaded
  video

#### Scenario: Episode NFO content includes all mapped metadata

- **WHEN** a talk has title, track, persons,
  abstract, date, and duration
- **THEN** the episode NFO file contains the
  corresponding `<title>`, `<showtitle>`,
  `<season>`, `<seasonnumber>`, `<episode>`,
  `<director>`, `<plot>`, `<aired>`, `<runtime>`,
  `<studio>`, `<uniqueid>`, and `<trailer>` elements

#### Scenario: Episodes are numbered in schedule order within each track

- **WHEN** a track contains multiple talks scheduled
  across different days and times
- **THEN** episodes are numbered sequentially by
  `(date, start)` so that the first talk of the
  track is episode 1, the second is episode 2, and
  so on

#### Scenario: Seasons are numbered in alphabetical track order

- **WHEN** multiple tracks are present in the
  download set
- **THEN** tracks are sorted alphabetically and
  assigned 1-based season numbers

#### Scenario: NFO not generated in ICS mode

- **WHEN** `--ics` is used (no rich metadata
  available)
- **THEN** no `.nfo` files are generated at any
  level

#### Scenario: NFO not generated without Jellyfin flag

- **WHEN** `--jellyfin` is not provided
- **THEN** no `.nfo` files are generated regardless
  of input mode
