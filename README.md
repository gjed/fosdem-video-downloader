# FOSDEM Video Downloader

> **Please be kind to FOSDEM's infrastructure.** FOSDEM is a free, volunteer-run
> conference. The video hosting servers are provided on a best-effort basis.
> This tool ships with conservative defaults (2 concurrent workers, 1 s delay
> between downloads, automatic retry with backoff) so it does not put
> unnecessary load on those servers. Please do **not** crank up the concurrency
> or remove the delay unless you know what you are doing. If you are downloading
> a large number of talks, consider running the tool during off-peak hours.

A Python tool to download FOSDEM conference videos. It supports two input
modes: parsing an ICS schedule file (exported from the
[FOSDEM mobile app](https://github.com/cbeyls/fosdem-companion-android)), or
fetching the full FOSDEM schedule for a given year via the Pentabarf schedule
XML.

## Features

- Download videos from your bookmarked talks (ICS file) or an entire FOSDEM
  year
- Filter by track name or a single talk slug when using year mode
- Choose between `.mp4` and `.av1.webm` (default) video formats
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

This produces a directory structure modelled as a Jellyfin TV series — each
FOSDEM edition is a show, each track is a season, and each talk is an episode.
NFO metadata sidecars are generated at all three levels:

```text
fosdem_videos/
  Fosdem (2025)/
    tvshow.nfo
    Containers/
      season.nfo
      my_talk_slug/
        my_talk_slug.mp4
        my_talk_slug.vtt
        my_talk_slug.nfo
    Go/
      season.nfo
      another_talk/
        another_talk.mp4
        another_talk.vtt
        another_talk.nfo
```

When used with `--ics` (no track metadata available), the layout falls back to
the room/location name and no `.nfo` files are generated.

### Command Line Arguments

**Input mode (one required, mutually exclusive):**

- `--ics <file>` — Path to a FOSDEM schedule ICS file
- `--year <YYYY>` — FOSDEM edition year (fetches schedule XML)

**Filters (require `--year`):**

- `--track <name>` — Filter by track name
- `--talk <id>` — Download a single talk by slug/ID

**Format and subtitles:**

- `--format {mp4,av1.webm}` — Video format (default: `av1.webm`)
- `--no-vtt` — Skip downloading `.vtt` subtitle files

**Output:**

- `-o, --output <path>` — Root output directory
  (default: `./fosdem_videos`)
- `--jellyfin` — Jellyfin TV series layout with track-based seasons and
  `.nfo` metadata at show, season, and episode levels (`--year` only)

**General:**

- `-w, --workers <n>` — Concurrent downloads (default: `2`)
- `--delay <seconds>` — Pause between downloads per worker (default: `1.0`)
- `--dry-run` — Print video URLs without downloading
- `--log-level` — Logging level (default: `INFO`)

## Server Politeness

FOSDEM is a free conference that relies entirely on volunteer effort, including
the infrastructure that hosts the video recordings. This tool is designed to be
a good citizen:

- **Low concurrency** — defaults to 2 parallel downloads.
- **Inter-request delay** — a 1-second pause between each download (per
  worker) to spread the load.
- **Retry with exponential back-off** — transient errors (429, 500, 502, 503)
  are retried up to 3 times with increasing delays instead of hammering the
  server.
- **Identifiable User-Agent** — every request carries a descriptive
  `User-Agent` header so server operators can identify and contact the project
  if needed.
- **Connection reuse** — a single `requests.Session` is shared per download
  batch, reducing TCP/TLS overhead for the server.
- **Skip already downloaded** — talks that already exist on disk are
  automatically skipped.

You can adjust `--workers` and `--delay` if needed, but please be considerate
of the shared infrastructure.

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
