## Context

The project currently has no automated tests. The codebase
is a single Python package (`fosdem_video/`) with six
modules totalling ~800 lines. Functions are mostly pure or
have clear I/O boundaries (HTTP requests, file writes),
making them well-suited for unit testing with mocking. The
project already uses `uv` for dependency management and
has `.pytest_cache` in `.gitignore`, suggesting pytest was
anticipated.

## Goals / Non-Goals

- Goals:
  - Unit test coverage for all public functions in every
    module
  - Integration tests for end-to-end CLI workflows
  - Fast test execution (no real network or large file I/O)
  - Simple test infrastructure that matches existing
    project conventions (minimal, stdlib-adjacent)

- Non-Goals:
  - 100% line/branch coverage enforcement (aspirational,
    not gated)
  - Performance/load testing
  - UI/visual testing
  - CI/CD pipeline setup (separate concern)

## Decisions

- **Test framework: pytest**
  - Why: De facto Python standard, already anticipated
    (`.gitignore` includes `.pytest_cache`), minimal
    boilerplate, excellent fixture system
  - Alternatives: `unittest` (more verbose, no fixtures),
    `nose2` (less maintained)

- **HTTP mocking: `responses` library**
  - Why: Lightweight, decorator-based, purpose-built for
    mocking `requests`. The project uses `requests`
    exclusively for HTTP; `responses` integrates directly
  - Alternatives: `requests-mock` (similar quality,
    slightly less popular), `vcrpy` (cassette-based,
    heavier), `unittest.mock` (manual, error-prone for
    HTTP)

- **File system: `tmp_path` pytest fixture**
  - Why: Built into pytest, provides unique temp
    directories per test, auto-cleaned
  - Alternatives: `tempfile` (manual cleanup), `pyfakefs`
    (heavier, not needed for this scope)

- **Test fixtures: static sample files**
  - Provide a minimal ICS file and Pentabarf XML fragment
    as string constants in `conftest.py` or fixture
    functions. Avoids external file dependencies
  - Small enough to inline; no separate `fixtures/`
    directory needed initially

- **Test directory structure:**

  ```text
  tests/
  ├── conftest.py          # Shared fixtures
  ├── unit/
  │   ├── test_models.py
  │   ├── test_discovery.py
  │   ├── test_download.py
  │   ├── test_nfo.py
  │   ├── test_images.py
  │   └── test_cli.py
  └── integration/
      └── test_workflows.py
  ```

  - Mirrors source module names for discoverability
  - Single integration file sufficient for current scope
  - `conftest.py` at root shares fixtures across both
    unit and integration

- **Dependency group: `test`**
  - Add `pytest` and `responses` under a new `test`
    dependency group in `pyproject.toml`
  - Include the test group in the `dev` meta-group

## Risks / Trade-offs

- **Mock fidelity**: Mocked HTTP responses may diverge
  from real FOSDEM server behaviour over time.
  Mitigation: keep mock responses minimal and derived
  from actual server response structure.

- **Test maintenance**: As features grow, tests need
  updating. Mitigation: test at the public API level, not
  implementation details; use fixtures to reduce
  duplication.

- **No CI enforcement yet**: Tests exist but won't block
  merges without CI. Mitigation: this is out of scope;
  can be added as a follow-up change.

## Open Questions

- None; the scope is well-defined and the tooling choices
  are standard for Python projects of this size.
