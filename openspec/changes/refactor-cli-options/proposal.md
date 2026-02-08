# Change: Refactor CLI to support multiple input modes, format selection, and VTT control

## Why

The current CLI requires a positional ICS file argument as the only way to select talks.
Users need the flexibility to download videos by year (optionally filtered by location or
talk ID) without an ICS file, choose between video formats, and control whether subtitle
(VTT) files are downloaded alongside videos.

## What Changes

- **BREAKING** `ics_file` positional argument is replaced by `--ics <file>` optional flag
- **BREAKING** `-o, --output-dir` is renamed to `-o, --output`
- Add `--year <YYYY>` flag as an alternative input mode (mutually exclusive with `--ics`)
- Add `--location <loc>` flag to filter by room/location when `--year` is provided
- Add `--talk <id>` flag to download a single talk when `--year` is provided
- Add `--format` flag to choose video format (`.mp4` or `.av1.webm`); defaults to `.mp4`
- Download `.vtt` subtitle files by default alongside each video
- Add `--no-vtt` flag to skip subtitle downloads
- Add `--jellyfin` flag to output files in a Jellyfin-compatible folder structure: `Fosdem (<year>)/<room_name>/<video_name>/{video,vtt}`
- Discover talks via FOSDEM Pentabarf schedule XML when using `--year` mode

## Impact

- Affected specs: `cli-interface`, `video-download`
- Affected code: `fosdem_video.py` (argument parsing, talk discovery, download logic, output path construction)
