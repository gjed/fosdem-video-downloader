## ADDED Requirements

### Requirement: Rich Talk Metadata from Schedule XML

The `Talk` data model SHALL include optional metadata fields populated from the FOSDEM Pentabarf schedule XML: title, track, date, start time, duration, room (human-readable), event URL, language, event type, abstract (HTML-stripped), description (HTML-stripped), feedback URL, and persons (list of speaker names). These fields SHALL default to empty values when not available (e.g. ICS mode).

#### Scenario: Metadata populated from schedule XML

- **WHEN** a talk is parsed from the Pentabarf schedule XML
- **THEN** all available metadata fields (title, track, date, start, duration, room, event_url, language, event_type, abstract, description, feedback_url, persons) are populated from the corresponding XML elements

#### Scenario: Metadata absent in ICS mode

- **WHEN** a talk is parsed from an ICS file
- **THEN** metadata fields default to empty strings and empty lists, and the system continues to function normally

### Requirement: Jellyfin NFO Sidecar Generation

When `--jellyfin` is enabled and the talk has rich metadata (year mode), the system SHALL generate a Jellyfin-compatible `.nfo` XML sidecar file alongside each downloaded video. The NFO file SHALL be named `<slug>.nfo` and placed in the same per-talk subfolder as the video. The NFO SHALL map FOSDEM metadata to Jellyfin tags as follows:

- `title` — talk title
- `plot` — abstract, followed by description if present, followed by a metadata block containing slug, feedback URL, language, and event type
- `aired` — talk date (ISO format)
- `runtime` — duration in minutes
- `genre` — track name
- `studio` — room name
- `tag` — event type, language, and slug as separate `<tag>` elements
- `director` — each person/speaker as a separate `<director>` element
- `trailer` — event URL

#### Scenario: NFO generated in Jellyfin mode

- **WHEN** `--jellyfin` is enabled and `--year` is used
- **THEN** a `.nfo` file is written alongside each successfully downloaded video

#### Scenario: NFO content includes all mapped metadata

- **WHEN** a talk has title, track, persons, abstract, date, and duration
- **THEN** the NFO file contains the corresponding `<title>`, `<genre>`, `<director>`, `<plot>`, `<aired>`, and `<runtime>` elements

#### Scenario: NFO not generated in ICS mode

- **WHEN** `--ics` is used (no rich metadata available)
- **THEN** no `.nfo` files are generated

#### Scenario: NFO not generated without Jellyfin flag

- **WHEN** `--jellyfin` is not provided
- **THEN** no `.nfo` files are generated regardless of input mode

## MODIFIED Requirements

### Requirement: Jellyfin Output Path Construction

When `--jellyfin` is enabled, the system SHALL write each video (and its optional VTT and NFO) into a per-talk subfolder following the pattern `<output>/Fosdem (<year>)/<track>/<slug>/<slug>.<ext>`. The `<track>` SHALL be the track name from the talk metadata. When track is not available (ICS mode), the system SHALL fall back to the `location` field. Directory creation SHALL happen automatically before downloads begin.

#### Scenario: Jellyfin directory tree uses track

- **WHEN** `--jellyfin` is enabled and talks are discovered via `--year`
- **THEN** each track gets its own subdirectory under `Fosdem (<year>)/`, and each talk gets a subfolder within its track directory

#### Scenario: Jellyfin falls back to location when track is empty

- **WHEN** `--jellyfin` is enabled and talks are discovered via `--ics` (no track metadata)
- **THEN** the system uses the `location` field as the grouping directory

#### Scenario: VTT placed alongside video in Jellyfin layout

- **WHEN** `--jellyfin` is enabled and `--no-vtt` is not set
- **THEN** the `.vtt` file is saved in the same per-talk subfolder as the video file

#### Scenario: NFO placed alongside video in Jellyfin layout

- **WHEN** `--jellyfin` is enabled and `--year` is used
- **THEN** the `.nfo` file is saved in the same per-talk subfolder as the video file
