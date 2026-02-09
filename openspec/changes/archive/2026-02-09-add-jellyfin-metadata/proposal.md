# Change: Add Jellyfin NFO metadata and use track-based folder layout

## Why

When using `--jellyfin` mode, the folder hierarchy currently uses the room name
(e.g. `janson`) as the grouping level. Tracks (e.g. "Rust", "Go", "Keynotes")
are a more meaningful grouping for browsing in a media server. Additionally,
Jellyfin supports `.nfo` sidecar files for rich metadata — the schedule XML
contains title, date, speakers, abstract, track, language, and more that should
be surfaced to the media server rather than discarded.

## What Changes

- **BREAKING** Jellyfin folder structure changes from `Fosdem (<year>)/<room>/`
  to `Fosdem (<year>)/<track>/`
- Enrich the `Talk` data model with full metadata from the Pentabarf schedule
  XML: title, track, date, start time, duration, room, event URL, language,
  event type, abstract, description, feedback URL, and persons
- Generate a Jellyfin-compatible `.nfo` sidecar file for each video when
  `--jellyfin` is enabled (year mode only)
- Map FOSDEM metadata to NFO tags: `title`, `plot`, `aired`, `runtime`,
  `genre` (track), `studio` (room), `tag` (type, language, slug), `trailer`
  (event URL), `director` (persons), and remaining fields collapsed into the
  plot description

## Impact

- Affected specs: `video-download`, `cli-interface`
- Affected code: `fosdem_video/models.py`, `fosdem_video/discovery.py`,
  `fosdem_video/download.py`, `fosdem_video/nfo.py` (new),
  `fosdem_video/cli.py`, `README.md`
