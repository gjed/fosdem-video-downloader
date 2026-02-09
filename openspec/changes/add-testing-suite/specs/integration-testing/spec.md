# integration-testing Specification

## Purpose

Defines requirements for integration tests that verify
end-to-end CLI workflows, exercising multiple modules
together with mocked external services (HTTP) and real
file system operations (via temp directories).

## ADDED Requirements

### Requirement: ICS-Based Download Workflow Test

The test suite SHALL include an integration test that
exercises the full ICS-to-download pipeline: parsing an
ICS file, resolving talks, creating output directories,
and downloading videos (with mocked HTTP). The test SHALL
verify that the correct files appear in the expected
directory structure.

#### Scenario: End-to-end ICS download produces correct files

- **WHEN** the CLI is invoked with `--ics` pointing to
  a fixture ICS file and HTTP responses are mocked to
  return video content
- **THEN** the output directory contains video files
  at the expected flat-layout paths
  `<output>/<year>/<slug>.mp4`

#### Scenario: ICS download with no-vtt skips subtitles

- **WHEN** the CLI is invoked with `--ics` and
  `--no-vtt` and HTTP responses are mocked
- **THEN** the output directory contains video files
  but no `.vtt` files

### Requirement: Year-Based Download Workflow Test

The test suite SHALL include an integration test that
exercises the year-based pipeline: fetching schedule XML
(mocked), resolving talks, creating directories, and
downloading videos (mocked). The test SHALL verify
correct file placement and that all discovered talks are
processed.

#### Scenario: End-to-end year download produces correct files

- **WHEN** the CLI is invoked with `--year` and HTTP
  responses are mocked for both the schedule XML and
  video downloads
- **THEN** the output directory contains video files
  for all talks in the mocked schedule

#### Scenario: Year download with track filter limits output

- **WHEN** the CLI is invoked with `--year` and
  `--track Containers` and the mocked schedule contains
  multiple tracks
- **THEN** only videos from the Containers track
  appear in the output directory

### Requirement: Jellyfin Layout Workflow Test

The test suite SHALL include an integration test that
exercises the Jellyfin layout mode end-to-end: year-based
discovery (mocked), directory creation with NFO sidecars
and metadata images, and video downloads. The test SHALL
verify the complete TV series directory structure.

#### Scenario: Jellyfin layout creates full directory tree with NFOs

- **WHEN** the CLI is invoked with `--year`,
  `--jellyfin`, and mocked HTTP responses
- **THEN** the output directory contains:
  `Fosdem (<year>)/tvshow.nfo`,
  `Fosdem (<year>)/<track>/season.nfo`, and
  `Fosdem (<year>)/<track>/<slug>/<slug>.nfo`
  alongside the video files

#### Scenario: Jellyfin ICS mode omits NFOs

- **WHEN** the CLI is invoked with `--ics`,
  `--jellyfin`, and mocked HTTP responses
- **THEN** the output directory uses the Jellyfin
  folder structure but contains no `.nfo` files

### Requirement: Dry-Run Workflow Test

The test suite SHALL include an integration test that
exercises `--dry-run` mode to confirm that no files are
downloaded and no directories are created beyond what the
CLI itself needs. The test SHALL verify that talk URLs are
listed to output but no video files exist.

#### Scenario: Dry-run lists URLs without downloading

- **WHEN** the CLI is invoked with `--ics` and
  `--dry-run`
- **THEN** no video files are written to the output
  directory and the expected URLs are logged or printed

### Requirement: NFO Regeneration Workflow Test

The test suite SHALL include an integration test for
`--regenerate-nfo` that verifies NFO files are rewritten
for already-downloaded videos without re-downloading
them.

#### Scenario: Regenerate NFO rewrites sidecar files

- **WHEN** the output directory already contains
  downloaded video files and the CLI is invoked with
  `--regenerate-nfo --jellyfin --year`
- **THEN** NFO files are written or overwritten
  alongside the existing videos, and no new video
  downloads occur

### Requirement: Error Handling Workflow Tests

The test suite SHALL include integration tests that
verify graceful error handling for common failure modes
across the full pipeline.

#### Scenario: 404 on video download does not crash pipeline

- **WHEN** the CLI is invoked and one or more video
  URLs return HTTP 404
- **THEN** the pipeline continues processing remaining
  talks and exits without an unhandled exception

#### Scenario: Missing ICS file produces clear error

- **WHEN** the CLI is invoked with `--ics` pointing to
  a non-existent file
- **THEN** the CLI exits with a non-zero status and an
  error message indicating the file was not found
