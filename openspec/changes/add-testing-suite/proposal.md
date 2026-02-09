# Change: Add Testing Suite

## Why

The project has zero automated tests despite a growing
codebase with six modules, complex ICS/XML parsing, HTTP
download logic, Jellyfin NFO generation, and image asset
resolution. Any refactoring or feature addition risks
silent regressions. A testing suite covering both unit
tests (isolated function behaviour) and integration tests
(cross-module workflows and CLI end-to-end behaviour) is
needed to enable confident development.

## What Changes

- Add `pytest` and `responses` (HTTP mocking) as test
  dependency group
- Add pytest configuration to `pyproject.toml`
- Create `tests/` directory with unit and integration
  test modules
- **Unit tests** covering all public functions across:
  `models.py`, `discovery.py`, `download.py`, `nfo.py`,
  `images.py`, and `cli.py` (argument parsing)
- **Integration tests** covering end-to-end CLI
  workflows: ICS-based download, year-based download,
  Jellyfin layout generation, dry-run mode, and NFO
  regeneration
- Add test fixtures: sample ICS file, sample Pentabarf
  XML fragment, and mock HTTP responses

## Impact

- Affected specs: `unit-testing` (new), `integration-testing` (new)
- Affected code: `pyproject.toml` (new dependency group,
  pytest config), new `tests/` directory tree
- No changes to existing application code
