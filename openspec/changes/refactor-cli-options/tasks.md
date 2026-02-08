## 1. Refactor CLI Argument Parsing

- [ ] 1.1 Remove positional `ics_file` argument from `parse_arguments()`
- [ ] 1.2 Add `--ics` optional argument (type=Path)
- [ ] 1.3 Add `--year` optional argument (type=int)
- [ ] 1.4 Add `--location` optional argument (type=str)
- [ ] 1.5 Add `--talk` optional argument (type=str)
- [ ] 1.6 Add `--format` argument with choices `mp4`, `av1.webm` and default `mp4`
- [ ] 1.7 Add `--no-vtt` flag (store_true)
- [ ] 1.8 Rename `--output-dir` to `-o, --output` (type=Path, default `./fosdem_videos`)
- [ ] 1.9 Add `--jellyfin` flag (store_true)
- [ ] 1.10 Implement mutual-exclusivity validation: exactly one of `--ics` or `--year` required
- [ ] 1.11 Validate `--location` and `--talk` require `--year`

## 2. Extend Talk Data Model

- [ ] 2.1 Add `location` field to the `Talk` NamedTuple to hold the room/track name
- [ ] 2.2 Populate `location` from the ICS `LOCATION` property in `parse_ics_file()`
- [ ] 2.3 Populate `location` from the `<room>` element in the schedule XML parser

## 3. Add Schedule XML Talk Discovery

- [ ] 3.1 Add `parse_schedule_xml(year, location=None, talk_id=None, fmt="mp4")` function that fetches and parses Pentabarf XML
- [ ] 3.2 Extract room, slug, and year from each `<event>` element to build `Talk` objects
- [ ] 3.3 Apply location filter (case-insensitive, punctuation-stripped) when `--location` is provided
- [ ] 3.4 Apply talk ID filter when `--talk` is provided
- [ ] 3.5 Construct video URLs using the selected format extension

## 4. Update Video URL Construction for Format Support

- [ ] 4.1 Update `parse_ics_file()` to accept a `fmt` parameter and use it for the file extension
- [ ] 4.2 Update `Talk` URL construction to use `{slug}.{fmt}` instead of hardcoded `.mp4`
- [ ] 4.3 Update `is_downloaded()` to use the correct format extension
- [ ] 4.4 Update `download_fosdem_videos()` and `process_video()` to use the correct extension in file paths

## 5. Add VTT Subtitle Download

- [ ] 5.1 Add VTT download logic (or extend existing `download_video`) to fetch `.vtt` files
- [ ] 5.2 In `process_video()`, after downloading a video, also download the corresponding `.vtt` unless `--no-vtt` is set
- [ ] 5.3 Handle 404 for VTT gracefully (log warning, do not fail)

## 6. Implement Output Path Strategy

- [ ] 6.1 Add a path-construction helper that returns the correct file path given the output mode (default flat vs Jellyfin)
- [ ] 6.2 Default flat layout: `<output>/<year>/<slug>.<ext>`
- [ ] 6.3 Jellyfin layout: `<output>/Fosdem (<year>)/<room_name>/<slug>/<slug>.<ext>`
- [ ] 6.4 Update `create_dirs()` to create the correct directory tree for each mode
- [ ] 6.5 Update `is_downloaded()` to check the correct path for each mode
- [ ] 6.6 Update `process_video()` to write files to the correct path for each mode

## 7. Wire Up main() with New Input Modes

- [ ] 7.1 Update `main()` to branch on `--ics` vs `--year` and call the appropriate talk-discovery function
- [ ] 7.2 Pass `--format`, `--no-vtt`, `--output`, and `--jellyfin` through to download logic

## 8. Update README

- [ ] 8.1 Update CLI usage examples in README.md to reflect the new flags
- [ ] 8.2 Document both ICS and year-based input modes
- [ ] 8.3 Document `--format`, `--no-vtt`, `--output`, and `--jellyfin` options
- [ ] 8.4 Add example showing Jellyfin folder structure

## 9. Testing

- [ ] 9.1 Verify `--ics` mode works end-to-end (replaces old positional arg behaviour)
- [ ] 9.2 Verify `--year` mode fetches schedule XML and discovers talks
- [ ] 9.3 Verify `--year --location` filters correctly
- [ ] 9.4 Verify `--year --talk` filters correctly
- [ ] 9.5 Verify `--format av1.webm` changes URL and file extension
- [ ] 9.6 Verify VTT downloads by default and `--no-vtt` skips them
- [ ] 9.7 Verify mutual exclusivity errors for `--ics` + `--year`
- [ ] 9.8 Verify `--location` / `--talk` without `--year` produce errors
- [ ] 9.9 Verify `--output` overrides the default output directory
- [ ] 9.10 Verify `--jellyfin` produces `Fosdem (<year>)/<room>/<slug>/<slug>.<ext>` structure
- [ ] 9.11 Verify `--jellyfin` places VTT alongside video in per-talk subfolder
