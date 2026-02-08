## ADDED Requirements

### Requirement: Schedule XML Talk Discovery

The system SHALL fetch and parse the FOSDEM Pentabarf schedule XML (at `https://fosdem.org/{year}/schedule/xml`) to discover talks. Each talk SHALL be converted into a `Talk` with a video URL constructed from the year, room, and talk slug using the selected format extension.

#### Scenario: Parse schedule XML for a year

- **WHEN** the user specifies `--year 2025`
- **THEN** the system fetches `https://fosdem.org/2025/schedule/xml`, parses all events, and builds video URLs for each talk

#### Scenario: Filter by location from schedule XML

- **WHEN** the user specifies `--year 2025 --location janson`
- **THEN** only events whose room matches `janson` (case-insensitive, stripped of punctuation) are included

#### Scenario: Filter by talk ID from schedule XML

- **WHEN** the user specifies `--year 2025 --talk my_talk_slug`
- **THEN** only the event whose slug matches `my_talk_slug` is included

### Requirement: Format-Aware Video URLs

The system SHALL construct video download URLs using the format specified by the `--format` flag. The URL pattern SHALL be `https://video.fosdem.org/{year}/{location}/{slug}.{format_extension}` where `format_extension` is either `mp4` or `av1.webm`.

#### Scenario: MP4 URL construction

- **WHEN** the format is `mp4`
- **THEN** the video URL ends with `.mp4`

#### Scenario: WebM URL construction

- **WHEN** the format is `av1.webm`
- **THEN** the video URL ends with `.av1.webm`

### Requirement: VTT Subtitle Download

The system SHALL, by default, attempt to download a `.vtt` subtitle file for each talk. The VTT URL SHALL follow the pattern `https://video.fosdem.org/{year}/{location}/{slug}.vtt`. If the VTT file returns a 404, the system SHALL log a warning and continue without failing. When the `--no-vtt` flag is provided, subtitle downloads SHALL be skipped entirely.

#### Scenario: VTT file exists and is downloaded

- **WHEN** a video is downloaded and `--no-vtt` is not set
- **THEN** the system also downloads the corresponding `.vtt` file to the same output directory

#### Scenario: VTT file does not exist on server

- **WHEN** the `.vtt` URL returns a 404
- **THEN** the system logs a warning and does not fail the overall download

#### Scenario: VTT download disabled

- **WHEN** `--no-vtt` is provided
- **THEN** no `.vtt` download is attempted

### Requirement: Format-Aware File Naming

Downloaded video files SHALL use the correct extension matching the selected format. The `is_downloaded` check SHALL also use the correct extension so previously downloaded files in the selected format are properly detected.

#### Scenario: File extension matches format

- **WHEN** the format is `av1.webm`
- **THEN** downloaded files are named `{slug}.av1.webm` and duplicate detection checks for that extension

### Requirement: Talk Location Metadata

The `Talk` data model SHALL include a `location` field containing the room/track name. This field SHALL be populated from the ICS `LOCATION` property or the Pentabarf XML `<room>` element. The location SHALL be used for Jellyfin folder layout and for constructing video URLs.

#### Scenario: Location populated from ICS

- **WHEN** a talk is parsed from an ICS file
- **THEN** the `Talk.location` field contains the normalised room name extracted from the event's LOCATION property

#### Scenario: Location populated from schedule XML

- **WHEN** a talk is parsed from the Pentabarf schedule XML
- **THEN** the `Talk.location` field contains the room name from the `<room>` element

### Requirement: Jellyfin Output Path Construction

When `--jellyfin` is enabled, the system SHALL write each video (and its optional VTT) into a per-talk subfolder following the pattern `<output>/Fosdem (<year>)/<room_name>/<slug>/<slug>.<ext>`. The `<room_name>` SHALL be the human-readable room name from the talk metadata. Directory creation SHALL happen automatically before downloads begin.

#### Scenario: Jellyfin directory tree created

- **WHEN** `--jellyfin` is enabled and talks span multiple rooms
- **THEN** each room gets its own subdirectory under `Fosdem (<year>)/`, and each talk gets a subfolder within its room directory

#### Scenario: VTT placed alongside video in Jellyfin layout

- **WHEN** `--jellyfin` is enabled and `--no-vtt` is not set
- **THEN** the `.vtt` file is saved in the same per-talk subfolder as the video file

### Requirement: Default Flat Output Path

When `--jellyfin` is not provided, the system SHALL use the default flat layout `<output>/<year>/<slug>.<ext>` for both video and VTT files.

#### Scenario: Default flat layout

- **WHEN** `--jellyfin` is not provided
- **THEN** files are saved as `<output>/<year>/<slug>.<ext>` with no room or per-talk subdirectories
