# Project Context

## Purpose

A CLI tool to download FOSDEM conference videos. It parses an ICS schedule file
(exported from the FOSDEM companion mobile app) to discover bookmarked talks and
downloads their corresponding video files from `video.fosdem.org`. Supports
concurrent downloads and dry-run mode.

## Tech Stack

- Python 3.12+
- `requests` — HTTP downloads
- `icalendar` — ICS file parsing
- `argparse` — CLI argument handling
- `uv` — dependency and environment management

## Project Conventions

### Code Style

- Formatter: `black` (line-length 90)
- Import sorting: `isort` (profile black, line-length 90)
- Linter: `ruff` (line-length 110, `select = ["ALL"]` with select ignores)
- Type checking: `ty`
- Docstrings on all public functions

### Architecture Patterns

- Single-file CLI application (`fosdem_video.py`)
- `Talk` NamedTuple as the core data model (fields: `url`, `year`, `id`)
- Functional style — standalone functions for parsing, downloading, and directory creation
- `ThreadPoolExecutor` for concurrent downloads
- Logging via stdlib `logging`

### Testing Strategy

- No formal test suite yet; manual verification
- `--dry-run` flag for safe URL listing without downloading

### Git Workflow

- Single `main` branch
- Conventional commits preferred

## Domain Context

- FOSDEM is an annual free software conference held in Brussels
- Videos are hosted at `https://video.fosdem.org/{year}/{room}/{slug}.{ext}`
- Available formats: `.mp4` and `.av1.webm`; subtitles as `.vtt`
- The FOSDEM companion app exports bookmarked talks as ICS files
- The FOSDEM schedule is also available as Pentabarf XML at
  `https://fosdem.org/{year}/schedule/xml`
- Rooms/locations in the ICS LOCATION field need normalisation (strip punctuation,
  lowercase, take first word)

## Important Constraints

- Requires Python >= 3.12
- Videos can be large; downloads use 1 MB chunked streaming
- 404s on video URLs are expected (not all talks have recordings) and must not crash the tool

## External Dependencies

- `video.fosdem.org` — video file hosting (HTTP GET, supports `Content-Length`)
- `fosdem.org/{year}/schedule/xml` — Pentabarf schedule XML for year-based discovery
- FOSDEM companion app ICS export — user-provided input file
