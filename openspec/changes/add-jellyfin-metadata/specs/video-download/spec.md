## ADDED Requirements

### Requirement: Rich Talk Metadata from Schedule XML

The `Talk` data model SHALL include optional metadata fields populated from the FOSDEM Pentabarf schedule XML: title, track, date, start time, duration, room (human-readable), event URL, language, event type, abstract (HTML-stripped), description (HTML-stripped), feedback URL, and persons (list of speaker names). These fields SHALL default to empty values when not available (e.g. ICS mode).

#### Scenario: Metadata populated from schedule XML

- **WHEN** a talk is parsed from the Pentabarf schedule XML
- **THEN** all available metadata fields (title, track, date, start, duration, room, event_url, language, event_type, abstract, description, feedback_url, persons) are populated from the corresponding XML elements

#### Scenario: Metadata absent in ICS mode

- **WHEN** a talk is parsed from an ICS file
- **THEN** metadata fields default to empty strings and empty lists, and the system continues to function normally

### Requirement: Jellyfin NFO Sidecar Generation (TV Series Model)

When `--jellyfin` is enabled and talks have rich metadata (year mode), the system SHALL generate Jellyfin-compatible `.nfo` XML sidecar files at three levels matching the TV series model:

**Show level** — `tvshow.nfo` (root tag `<tvshow>`) placed in the show root directory `Fosdem (<year>)/`:

- `title` / `showtitle` — `FOSDEM <year>`
- `plot` — a short description of the FOSDEM conference
- `premiered` — `<year>-02-01`
- `studio` — `FOSDEM`
- `genre` — `Technology`
- `tag` — `conference`, `open-source`
- `uniqueid` (type `fosdem`) — `fosdem-<year>`
- `namedseason` — one entry per track, sorted alphabetically

**Season level** — `season.nfo` (root tag `<season>`) placed in each track directory `Fosdem (<year>)/<track>/`:

- `title` — track name
- `seasonnumber` — the track's position in the sorted track list
- `plot` — a brief description identifying the track

**Episode level** — `<slug>.nfo` (root tag `<episodedetails>`) placed alongside each downloaded video:

- `title` — talk title
- `showtitle` — `FOSDEM <year>`
- `plot` — abstract, followed by description if present, followed by a metadata block containing slug, feedback URL, language, and event type
- `aired` — talk date (ISO format)
- `runtime` — duration in minutes
- `studio` — room name
- `uniqueid` (type `fosdem`) — the talk slug
- `trailer` — event URL
- `director` — each person/speaker as a separate `<director>` element

#### Scenario: All three NFO levels generated in Jellyfin year mode

- **WHEN** `--jellyfin` is enabled and `--year` is used
- **THEN** `tvshow.nfo` is written in the show root, `season.nfo` in each track directory, and `<slug>.nfo` alongside each successfully downloaded video

#### Scenario: Episode NFO content includes all mapped metadata

- **WHEN** a talk has title, track, persons, abstract, date, and duration
- **THEN** the episode NFO file contains the corresponding `<title>`, `<showtitle>`, `<director>`, `<plot>`, `<aired>`, and `<runtime>` elements

#### Scenario: TVShow NFO lists all tracks as named seasons

- **WHEN** multiple tracks are present in the download set
- **THEN** the `tvshow.nfo` contains one `<namedseason>` element per track, numbered consecutively

#### Scenario: NFO not generated in ICS mode

- **WHEN** `--ics` is used (no rich metadata available)
- **THEN** no `.nfo` files are generated at any level

#### Scenario: NFO not generated without Jellyfin flag

- **WHEN** `--jellyfin` is not provided
- **THEN** no `.nfo` files are generated regardless of input mode

## MODIFIED Requirements

### Requirement: Jellyfin Output Path Construction

When `--jellyfin` is enabled, the system SHALL write each video (and its optional VTT and NFO) into a per-talk subfolder following the pattern `<output>/Fosdem (<year>)/<track>/<slug>/<slug>.<ext>`. The `<track>` SHALL be the track name from the talk metadata. When track is not available (ICS mode), the system SHALL fall back to the `location` field. Directory creation SHALL happen automatically before downloads begin. When talks carry rich metadata (year mode), the system SHALL also write `tvshow.nfo` in the show root and `season.nfo` in each track directory during directory creation.

#### Scenario: Jellyfin directory tree uses track

- **WHEN** `--jellyfin` is enabled and talks are discovered via `--year`
- **THEN** each track gets its own subdirectory under `Fosdem (<year>)/`, and each talk gets a subfolder within its track directory

#### Scenario: Jellyfin falls back to location when track is empty

- **WHEN** `--jellyfin` is enabled and talks are discovered via `--ics` (no track metadata)
- **THEN** the system uses the `location` field as the grouping directory

#### Scenario: VTT placed alongside video in Jellyfin layout

- **WHEN** `--jellyfin` is enabled and `--no-vtt` is not set
- **THEN** the `.vtt` file is saved in the same per-talk subfolder as the video file

#### Scenario: Show and season NFO written during directory creation

- **WHEN** `--jellyfin` is enabled and `--year` is used
- **THEN** `tvshow.nfo` is written once in `Fosdem (<year>)/` and `season.nfo` once in each track directory, alongside the per-episode `<slug>.nfo` files
