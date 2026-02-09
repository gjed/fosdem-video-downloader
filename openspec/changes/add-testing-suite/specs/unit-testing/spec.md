# unit-testing Specification

## Purpose

Defines requirements for unit tests that verify the
behaviour of individual public functions in isolation,
using mocks for external dependencies (HTTP, file system).

## ADDED Requirements

### Requirement: Model Helper Unit Tests

The test suite SHALL include unit tests for all public
functions in `models.py`: `get_path_elements`,
`normalise_location`, `sanitise_path_component`,
`slugify`, and `display_name`. Tests SHALL cover
typical inputs, edge cases (empty strings, special
characters, Unicode), and the `Talk` dataclass
construction.

#### Scenario: get_path_elements extracts year and slug

- **WHEN** `get_path_elements` is called with a valid
  FOSDEM video URL
- **THEN** it returns a tuple of `(year, slug)`
  extracted from the URL path

#### Scenario: normalise_location strips punctuation and lowercases

- **WHEN** `normalise_location` is called with a room
  string containing punctuation and mixed case
- **THEN** it returns a lowercase single-word string
  with punctuation removed

#### Scenario: slugify converts text to URL-safe slug

- **WHEN** `slugify` is called with free-form text
  containing spaces and special characters
- **THEN** it returns a lowercase hyphen-separated
  string with only alphanumeric characters

#### Scenario: display_name formats Talk for Jellyfin

- **WHEN** `display_name` is called with a Talk that
  has title and year metadata
- **THEN** it returns a string in
  `FOSDEM <year> S<ss>E<ee> <title>` format

#### Scenario: display_name falls back to talk ID

- **WHEN** `display_name` is called with a Talk that
  has no title metadata
- **THEN** it returns a string using `talk.id` as the
  name component

### Requirement: ICS Parsing Unit Tests

The test suite SHALL include unit tests for
`parse_ics_file` that verify talk extraction from ICS
calendar data. Tests SHALL use fixture ICS content
containing VEVENT entries with FOSDEM video URLs.

#### Scenario: Parse valid ICS with multiple talks

- **WHEN** `parse_ics_file` is called with a valid ICS
  file containing multiple VEVENT entries with video
  URLs
- **THEN** it returns a list of `Talk` objects with
  correct `url`, `year`, `id`, and `location` fields

#### Scenario: Parse ICS with no video URLs

- **WHEN** `parse_ics_file` is called with an ICS file
  containing events that have no video URLs
- **THEN** it returns an empty list

#### Scenario: ICS format selection applies correct extension

- **WHEN** `parse_ics_file` is called with
  `fmt="av1.webm"`
- **THEN** the returned Talk URLs end with `.av1.webm`

### Requirement: Schedule XML Parsing Unit Tests

The test suite SHALL include unit tests for
`parse_schedule_xml` that verify talk extraction from
Pentabarf XML. Tests SHALL mock the HTTP request to
`fosdem.org` and provide fixture XML content.

#### Scenario: Parse schedule XML returns talks with rich metadata

- **WHEN** `parse_schedule_xml` is called with mocked
  XML containing events
- **THEN** it returns Talk objects with all metadata
  fields populated (title, track, date, start,
  duration, room, persons, etc.)

#### Scenario: Filter by track name

- **WHEN** `parse_schedule_xml` is called with a
  `track` parameter
- **THEN** only talks matching that track are returned

#### Scenario: Filter by talk ID

- **WHEN** `parse_schedule_xml` is called with a
  `talk_id` parameter
- **THEN** only the talk with the matching slug is
  returned

### Requirement: Download Function Unit Tests

The test suite SHALL include unit tests for
`download_video`, `download_vtt`, `get_output_path`,
`is_downloaded`, and `create_dirs`. HTTP-dependent
functions SHALL use mocked responses. File-dependent
functions SHALL use `tmp_path`.

#### Scenario: download_video succeeds with 200 response

- **WHEN** `download_video` is called and the server
  returns HTTP 200 with content
- **THEN** the file is written to the output path and
  the function returns `True`

#### Scenario: download_video handles 404 gracefully

- **WHEN** `download_video` is called and the server
  returns HTTP 404
- **THEN** no file is written and the function returns
  `False`

#### Scenario: download_video cleans up partial file on failure

- **WHEN** `download_video` is called and the download
  fails mid-stream
- **THEN** any partial file at the output path is
  removed

#### Scenario: download_vtt handles missing subtitle

- **WHEN** `download_vtt` is called and the VTT URL
  returns HTTP 404
- **THEN** the function returns `False` without
  raising an exception

#### Scenario: get_output_path returns correct flat layout path

- **WHEN** `get_output_path` is called with
  `jellyfin=False`
- **THEN** it returns
  `<output>/<year>/<slug>.<format>`

#### Scenario: get_output_path returns correct Jellyfin layout path

- **WHEN** `get_output_path` is called with
  `jellyfin=True` and an episode index
- **THEN** it returns a path following the Jellyfin TV
  series structure

#### Scenario: is_downloaded detects existing file

- **WHEN** `is_downloaded` is called and the expected
  output file exists on disk
- **THEN** it returns `True`

#### Scenario: create_dirs creates directory tree

- **WHEN** `create_dirs` is called with a list of
  talks
- **THEN** the expected directory structure is created
  under the output path

### Requirement: NFO Generation Unit Tests

The test suite SHALL include unit tests for all NFO
generation and writing functions: `generate_tvshow_nfo`,
`write_tvshow_nfo`, `generate_season_nfo`,
`write_season_nfo`, `generate_episode_nfo`, and
`write_episode_nfo`. Tests SHALL verify XML element
structure, content values, and file writing to
`tmp_path`.

#### Scenario: generate_tvshow_nfo produces correct XML structure

- **WHEN** `generate_tvshow_nfo` is called with a year
- **THEN** the returned XML element has root tag
  `<tvshow>` with correct `title`, `plot`,
  `premiered`, `genre`, and `uniqueid` children

#### Scenario: generate_episode_nfo includes speaker elements

- **WHEN** `generate_episode_nfo` is called with a
  Talk that has multiple persons
- **THEN** the returned XML contains a `<director>`
  element for each speaker

#### Scenario: write_tvshow_nfo writes file to disk

- **WHEN** `write_tvshow_nfo` is called with a
  `tmp_path` directory
- **THEN** a `tvshow.nfo` file is created in that
  directory with valid XML content

### Requirement: Image Resolution Unit Tests

The test suite SHALL include unit tests for
`resolve_assets`, `copy_show_images`, and
`copy_season_images`. Tests SHALL create fixture image
files in `tmp_path` to verify the resolution priority
chain and copy behaviour.

#### Scenario: resolve_assets finds year-specific image first

- **WHEN** both `fosdem-2026-primary.jpg` and
  `fosdem-primary.jpg` exist in the assets directory
- **THEN** `resolve_assets` returns the year-specific
  file

#### Scenario: resolve_assets falls back to default image

- **WHEN** no year-specific image exists but a default
  `fosdem-backdrop.png` does
- **THEN** `resolve_assets` returns the default file

#### Scenario: copy_show_images copies to Jellyfin names

- **WHEN** `copy_show_images` is called with assets
  containing a primary image
- **THEN** the show directory contains `poster.<ext>`
  copied from that asset

### Requirement: CLI Argument Parsing Unit Tests

The test suite SHALL include unit tests for
`parse_arguments` that verify argument parsing,
defaults, mutual exclusivity, and validation rules
without invoking the full `main()` function.

#### Scenario: Default argument values

- **WHEN** `parse_arguments` is called with
  `['--ics', 'file.ics']`
- **THEN** the result has `format='mp4'`,
  `output='fosdem_videos'`, `workers=2`, and
  `dry_run=False`

#### Scenario: Mutual exclusivity of ics and year

- **WHEN** `parse_arguments` is called with both
  `['--ics', 'f.ics', '--year', '2025']`
- **THEN** an error is raised indicating mutual
  exclusivity

#### Scenario: Track requires year

- **WHEN** `parse_arguments` is called with
  `['--ics', 'f.ics', '--track', 'Go']`
- **THEN** an error is raised indicating `--track`
  requires `--year`
