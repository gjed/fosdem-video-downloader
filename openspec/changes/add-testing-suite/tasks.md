## 1. Project Configuration

- [ ] 1.1 Add `test` dependency group to `pyproject.toml`
  with `pytest>=8.0.0` and `responses>=0.25.0`
- [ ] 1.2 Include `test` group in the `dev` meta-group
- [ ] 1.3 Add `[tool.pytest.ini_options]` section with
  `testpaths = ["tests"]` and
  `markers` for `unit` and `integration`
- [ ] 1.4 Create `tests/__init__.py`,
  `tests/unit/__init__.py`, and
  `tests/integration/__init__.py`

## 2. Test Fixtures

- [ ] 2.1 Create `tests/conftest.py` with shared
  fixtures: sample ICS content, sample Pentabarf XML
  fragment, a `Talk` factory helper, and `tmp_path`-based
  output directory fixture
- [ ] 2.2 Add a `sample_ics_content` fixture with 2-3
  VEVENT entries containing FOSDEM video URLs
- [ ] 2.3 Add a `sample_schedule_xml` fixture with a
  minimal Pentabarf XML containing 2-3 events across
  2 tracks

## 3. Unit Tests — Models (tests/unit/test_models.py)

- [ ] 3.1 Test `get_path_elements` with valid URL, edge
  cases
- [ ] 3.2 Test `normalise_location` with punctuation,
  mixed case, multi-word
- [ ] 3.3 Test `sanitise_path_component` with special
  characters
- [ ] 3.4 Test `slugify` with spaces, unicode, empty
  string
- [ ] 3.5 Test `display_name` with full metadata and
  with missing title
- [ ] 3.6 Test `Talk` dataclass construction and
  immutability

## 4. Unit Tests — Discovery (tests/unit/test_discovery.py)

- [ ] 4.1 Test `parse_ics_file` with valid ICS fixture
- [ ] 4.2 Test `parse_ics_file` with ICS containing no
  video URLs
- [ ] 4.3 Test `parse_ics_file` with `fmt="av1.webm"`
- [ ] 4.4 Test `parse_schedule_xml` with mocked HTTP
  returning fixture XML
- [ ] 4.5 Test `parse_schedule_xml` track filter
- [ ] 4.6 Test `parse_schedule_xml` talk ID filter

## 5. Unit Tests — Download (tests/unit/test_download.py)

- [ ] 5.1 Test `download_video` with mocked 200 response
- [ ] 5.2 Test `download_video` with mocked 404 response
- [ ] 5.3 Test `download_video` partial file cleanup on
  failure
- [ ] 5.4 Test `download_vtt` with 404 response
- [ ] 5.5 Test `get_output_path` flat layout
- [ ] 5.6 Test `get_output_path` Jellyfin layout
- [ ] 5.7 Test `is_downloaded` with existing and missing
  files
- [ ] 5.8 Test `create_dirs` creates expected directory
  structure

## 6. Unit Tests — NFO (tests/unit/test_nfo.py)

- [ ] 6.1 Test `generate_tvshow_nfo` XML structure
- [ ] 6.2 Test `generate_season_nfo` XML structure
- [ ] 6.3 Test `generate_episode_nfo` XML structure and
  speaker elements
- [ ] 6.4 Test `write_tvshow_nfo` writes file to
  `tmp_path`
- [ ] 6.5 Test `write_season_nfo` writes file to
  `tmp_path`
- [ ] 6.6 Test `write_episode_nfo` writes file to
  `tmp_path`

## 7. Unit Tests — Images (tests/unit/test_images.py)

- [ ] 7.1 Test `resolve_assets` year-specific priority
- [ ] 7.2 Test `resolve_assets` default fallback
- [ ] 7.3 Test `resolve_assets` with no matching files
- [ ] 7.4 Test `copy_show_images` copies to Jellyfin
  target names
- [ ] 7.5 Test `copy_season_images` copies to Jellyfin
  target names

## 8. Unit Tests — CLI (tests/unit/test_cli.py)

- [ ] 8.1 Test `parse_arguments` default values
- [ ] 8.2 Test `parse_arguments` mutual exclusivity of
  `--ics` and `--year`
- [ ] 8.3 Test `parse_arguments` `--track` requires
  `--year`
- [ ] 8.4 Test `parse_arguments` `--talk` requires
  `--year`
- [ ] 8.5 Test `parse_arguments` invalid format value

## 9. Integration Tests (tests/integration/test_workflows.py)

- [ ] 9.1 Test ICS-based download end-to-end (mocked
  HTTP, real file system via `tmp_path`)
- [ ] 9.2 Test ICS download with `--no-vtt`
- [ ] 9.3 Test year-based download end-to-end (mocked
  schedule XML + video HTTP)
- [ ] 9.4 Test year download with track filter
- [ ] 9.5 Test Jellyfin layout with NFO generation
- [ ] 9.6 Test Jellyfin ICS mode omits NFOs
- [ ] 9.7 Test dry-run mode produces no files
- [ ] 9.8 Test NFO regeneration workflow
- [ ] 9.9 Test 404 on video download continues pipeline
- [ ] 9.10 Test missing ICS file produces clear error

## 10. Validation

- [ ] 10.1 Run `pytest tests/` and confirm all tests pass
- [ ] 10.2 Run linters (`ruff`, `black`, `isort`) on
  test files and fix any issues
