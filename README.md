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

- Download from your **bookmarked talks** (ICS export) or an **entire year**
- Filter by **track** or **single talk** slug
- `.mp4` and `.av1.webm` formats, with `.vtt` subtitles
- **Jellyfin layout** -- organizes videos as a TV series with NFO metadata
- Concurrent downloads with polite rate-limiting
- Dry-run mode to preview URLs without downloading

## Installation

Requires Python 3.12+ and [uv](https://github.com/astral-sh/uv).

```bash
git clone https://github.com/gjed/fosdem-video-downloader.git
cd fosdem-video-downloader
uv sync
```

## Quick Start

```bash
# From an ICS bookmarks file
uv run fosdem-video --ics bookmarks.ics

# Entire FOSDEM year
uv run fosdem-video --year 2025

# Filter by track
uv run fosdem-video --year 2025 --track Containers

# Single talk
uv run fosdem-video --year 2025 --talk my_talk_slug

# Jellyfin-compatible layout with NFO metadata
uv run fosdem-video --year 2025 --jellyfin
```

## Jellyfin Integration

Pass `--jellyfin` to organize downloads as a TV series -- each edition is a
show, each track a season, each talk an episode. NFO sidecars are generated at
every level:

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
```

## CLI Reference

### Input mode (one required, mutually exclusive)

| Flag | Description |
| --- | --- |
| `--ics <file>` | Path to a FOSDEM schedule ICS file |
| `--year <YYYY>` | FOSDEM edition year (fetches schedule XML) |

### Filters (require `--year`)

| Flag | Description |
| --- | --- |
| `--track <name>` | Download only talks in this track |
| `--talk <slug>` | Download a single talk by slug |

### Output

| Flag | Description |
| --- | --- |
| `-o, --output <path>` | Root output directory (default: `./fosdem_videos`) |
| `--jellyfin` | Jellyfin TV series layout with NFO metadata |
| `--format {mp4,av1.webm}` | Video format (default: `av1.webm`) |
| `--no-vtt` | Skip `.vtt` subtitle download |

### General

| Flag | Description |
| --- | --- |
| `-w, --workers <n>` | Concurrent downloads (default: `2`) |
| `--delay <seconds>` | Pause between downloads per worker (default: `1.0`) |
| `--dry-run` | Print video URLs without downloading |
| `--log-level` | Logging verbosity (default: `INFO`) |

## Getting Your Bookmarks

1. Install the [FOSDEM Companion](https://github.com/cbeyls/fosdem-companion-android) app.
2. Bookmark the talks you want to watch.
3. Export bookmarks as an ICS file.
4. Pass the file with `--ics bookmarks.ics`.

## Server Politeness

FOSDEM is a free, volunteer-run conference. This tool is designed to be a good
citizen:

- Low default concurrency (2 workers) with a 1 s inter-request delay
- Retry with exponential back-off on transient errors
- Identifiable `User-Agent` header
- Connection reuse via a shared `requests.Session`
- Automatic skip of already-downloaded files

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.

## License

[Apache License 2.0](LICENSE)
