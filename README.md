# FOSDEM Video Downloader

A Python tool to download FOSDEM conference videos. It supports two input
modes: parsing an ICS schedule file (exported from the
[FOSDEM mobile app](https://github.com/cbeyls/fosdem-companion-android)), or
fetching the full FOSDEM schedule for a given year via the Pentabarf schedule
XML.

## Features

- Download videos from your bookmarked talks (ICS file) or an entire FOSDEM
  year
- Filter by track name or a single talk slug when using year mode
- Choose between `.mp4` (default) and `.av1.webm` video formats
- Automatically download `.vtt` subtitles alongside each video (opt-out with
  `--no-vtt`)
- Jellyfin-compatible folder layout for media server integration
- Concurrent downloads to speed up the process
- Dry-run mode to preview URLs without downloading

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency and
environment management.

```bash
git clone https://github.com/butlerx/fosdem-video-downloader.git
cd fosdem-video-downloader

uv sync
```

This will create a virtual environment and install all dependencies.

## Usage

The CLI is exposed as `fosdem-video` via the package entry point.
You can also run it with `python -m fosdem_video`.

### Download from an ICS file

```bash
uv run fosdem-video --ics bookmarks.ics
```

### Download an entire FOSDEM year

```bash
uv run fosdem-video --year 2025
```

### Filter by track

```bash
uv run fosdem-video --year 2025 --track Containers
```

### Download a single talk by slug

```bash
uv run fosdem-video --year 2025 --talk my_talk_slug
```

### Choose video format

```bash
uv run fosdem-video --ics bookmarks.ics --format av1.webm
```

### Use Jellyfin-compatible folder layout

```bash
uv run fosdem-video --year 2025 --jellyfin
```

This produces a directory structure grouped by track (when using `--year`) with
Jellyfin-compatible `.nfo` metadata sidecars:

```text
fosdem_videos/
  Fosdem (2025)/
    Containers/
      my_talk_slug/
        my_talk_slug.mp4
        my_talk_slug.vtt
        my_talk_slug.nfo
    Go/
      another_talk/
        another_talk.mp4
        another_talk.vtt
        another_talk.nfo
```

When used with `--ics` (no track metadata available), the layout falls back to
the room/location name and `.nfo` files are not generated.

### Command Line Arguments

**Input mode (one required, mutually exclusive):**

- `--ics <file>` — Path to a FOSDEM schedule ICS file
- `--year <YYYY>` — FOSDEM edition year (fetches schedule XML)

**Filters (require `--year`):**

- `--track <name>` — Filter by track name
- `--talk <id>` — Download a single talk by slug/ID

**Format and subtitles:**

- `--format {mp4,av1.webm}` — Video format (default: `mp4`)
- `--no-vtt` — Skip downloading `.vtt` subtitle files

**Output:**

- `-o, --output <path>` — Root output directory
  (default: `./fosdem_videos`)
- `--jellyfin` — Jellyfin-compatible folder layout with track-based grouping
  and `.nfo` metadata sidecars (NFO generated with `--year` only)

**General:**

- `-w, --workers <n>` — Concurrent downloads (default: `3`)
- `--dry-run` — Print video URLs without downloading
- `--log-level` — Logging level (default: `INFO`)

## Getting Your Bookmarks

1. Use the FOSDEM mobile app to bookmark talks you're interested in.
1. Export your bookmarks as an ICS file from the app.
1. Use this ICS file as input for the tool.

## Development

Install development dependencies:

```bash
uv sync --group dev
```

Run type checking and linting:

```bash
uv run ty check
uv run ruff check --fix
uv run ruff format
```

## License

Apache License 2.0

## Contributing

Contributions are welcome! Please feel free to submit a pull request.
