## 1. Project Configuration

- [x] 1.1 Add `test` dependency group to `pyproject.toml`
  with `pytest>=8.0.0` and `responses>=0.25.0`
- [x] 1.2 Include `test` group in the `dev` meta-group
- [x] 1.3 Add `[tool.pytest.ini_options]` section with
  `testpaths = ["tests"]` and
  `markers` for `unit` and `integration`
- [x] 1.4 Create `tests/__init__.py`,
  `tests/unit/__init__.py`, and
  `tests/integration/__init__.py`

## 2. Test Fixtures

- [x] 2.1 Create `tests/conftest.py` with shared
  fixtures: sample ICS content, sample Pentabarf XML
  fragment, a `Talk` factory helper, and `tmp_path`-based
  output directory fixture
- [x] 2.2 Add a `sample_ics_content` fixture with 2-3
  VEVENT entries containing FOSDEM video URLs
- [x] 2.3 Add a `sample_schedule_xml` fixture with a
  minimal Pentabarf XML containing 2-3 events across
  2 tracks

## 3. Unit Tests — Models (tests/unit/test_models.py)

- [x] 3.1 Test `get_path_elements` with valid URL, edge
  cases
- [x] 3.2 Test `normalise_location` with punctuation,
  mixed case, multi-word
- [x] 3.3 Test `sanitise_path_component` with special
  characters
- [x] 3.4 Test `slugify` with spaces, unicode, empty
  string
- [x] 3.5 Test `display_name` with full metadata and
  with missing title
- [x] 3.6 Test `Talk` dataclass construction and
  immutability

## 4. Unit Tests — Discovery (tests/unit/test_discovery.py)

- [x] 4.1 Test `parse_ics_file` with valid ICS fixture
- [x] 4.2 Test `parse_ics_file` with ICS containing no
  video URLs
- [x] 4.3 Test `parse_ics_file` with `fmt="av1.webm"`
- [x] 4.4 Test `parse_schedule_xml` with mocked HTTP
  returning fixture XML
- [x] 4.5 Test `parse_schedule_xml` track filter
- [x] 4.6 Test `parse_schedule_xml` talk ID filter

## 5. Unit Tests — Download (tests/unit/test_download.py)

- [x] 5.1 Test `download_video` with mocked 200 response
- [x] 5.2 Test `download_video` with mocked 404 response
- [x] 5.3 Test `download_video` partial file cleanup on
  failure
- [x] 5.4 Test `download_vtt` with 404 response
- [x] 5.5 Test `get_output_path` flat layout
- [x] 5.6 Test `get_output_path` Jellyfin layout
- [x] 5.7 Test `is_downloaded` with existing and missing
  files
- [x] 5.8 Test `create_dirs` creates expected directory
  structure

## 6. Unit Tests — NFO (tests/unit/test_nfo.py)

- [x] 6.1 Test `generate_tvshow_nfo` XML structure
- [x] 6.2 Test `generate_season_nfo` XML structure
- [x] 6.3 Test `generate_episode_nfo` XML structure and
  speaker elements
- [x] 6.4 Test `write_tvshow_nfo` writes file to
  `tmp_path`
- [x] 6.5 Test `write_season_nfo` writes file to
  `tmp_path`
- [x] 6.6 Test `write_episode_nfo` writes file to
  `tmp_path`

## 7. Unit Tests — Images (tests/unit/test_images.py)

- [x] 7.1 Test `resolve_assets` year-specific priority
- [x] 7.2 Test `resolve_assets` default fallback
- [x] 7.3 Test `resolve_assets` with no matching files
- [x] 7.4 Test `copy_show_images` copies to Jellyfin
  target names
- [x] 7.5 Test `copy_season_images` copies to Jellyfin
  target names

## 8. Unit Tests — CLI (tests/unit/test_cli.py)

- [x] 8.1 Test `parse_arguments` default values
- [x] 8.2 Test `parse_arguments` mutual exclusivity of
  `--ics` and `--year`
- [x] 8.3 Test `parse_arguments` `--track` requires
  `--year`
- [x] 8.4 Test `parse_arguments` `--talk` requires
  `--year`
- [x] 8.5 Test `parse_arguments` invalid format value

## 9. Integration Tests (tests/integration/test_workflows.py)

- [x] 9.1 Test ICS-based download end-to-end (mocked
  HTTP, real file system via `tmp_path`)
- [x] 9.2 Test ICS download with `--no-vtt`
- [x] 9.3 Test year-based download end-to-end (mocked
  schedule XML + video HTTP)
- [x] 9.4 Test year download with track filter
- [x] 9.5 Test Jellyfin layout with NFO generation
- [x] 9.6 Test Jellyfin ICS mode omits NFOs
- [x] 9.7 Test dry-run mode produces no files
- [x] 9.8 Test NFO regeneration workflow
- [x] 9.9 Test 404 on video download continues pipeline
- [x] 9.10 Test missing ICS file produces clear error

## 10. Validation

- [x] 10.1 Run `pytest tests/` and confirm all tests pass
- [x] 10.2 Run linters (`ruff`, `black`, `isort`) on
  test files and fix any issues
