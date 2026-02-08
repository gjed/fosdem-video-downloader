## 1. Enrich Talk Data Model

- [x] 1.1 Add metadata fields to `Talk`: title, track, date, start, duration, room, event_url, language, event_type, abstract, description, feedback_url, persons
- [x] 1.2 Convert `Talk` from `NamedTuple` to `dataclass(frozen=True)` to support default values for optional metadata

## 2. Extract Full Metadata from Schedule XML

- [x] 2.1 Update `parse_schedule_xml()` to extract all child elements of each `<event>` into the enriched `Talk`
- [x] 2.2 Strip HTML tags and decode entities from abstract and description fields
- [x] 2.3 Collect `<person>` names from the `<persons>` element

## 3. Change Jellyfin Path to Use Track

- [x] 3.1 Update `get_output_path()` Jellyfin layout from `<room>` to `<track>` grouping
- [x] 3.2 Fall back to `location` when `track` is empty (ICS mode)

## 4. Add NFO Sidecar Generation

- [x] 4.1 Create `fosdem_video/nfo.py` with `generate_nfo(talk) -> str` function
- [x] 4.2 Map metadata to Jellyfin NFO tags: title, plot, aired, runtime, genre (track), studio (room), tag, director (persons), trailer (event URL)
- [x] 4.3 Collapse remaining metadata (slug, feedback URL, language, type) into the plot description
- [x] 4.4 Add `write_nfo(talk, output_path)` that writes the NFO alongside the video file

## 5. Wire NFO Writing into Download Pipeline

- [x] 5.1 In `process_video()`, after successful download, call `write_nfo()` when `--jellyfin` is enabled
- [x] 5.2 Only write NFO when the talk has metadata (year mode); skip silently for ICS mode

## 6. Rename --location to --track

- [x] 6.1 Rename `--location` CLI arg to `--track` and update validation
- [x] 6.2 Rename `parse_schedule_xml()` parameter from `location` to `track` and filter by track name
- [x] 6.3 Update README references from `--location` to `--track`
- [x] 6.4 Update openspec cli-interface delta spec with RENAMED + MODIFIED for Track Filter

## 7. Update CLI Help and README

- [x] 7.1 Update `--jellyfin` help text to mention track-based layout and NFO generation
- [x] 7.2 Update README Jellyfin example to show track-based folder structure and .nfo files

## 8. Verification

- [x] 8.1 Verify Jellyfin path now uses track name instead of room
- [x] 8.2 Verify NFO files are generated with correct content in Jellyfin mode
- [x] 8.3 Verify ICS mode still works without NFO generation
- [x] 8.4 Verify all linters pass
