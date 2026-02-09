# Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Development Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency and
environment management. Python 3.12+ is required.

```bash
git clone https://github.com/gjed/fosdem-video-downloader.git
cd fosdem-video-downloader

# Install all dependencies including dev tools
uv sync --group dev
```

## Code Quality

The project enforces formatting and linting via
[pre-commit](https://pre-commit.com/) hooks. Install them once and they will
run automatically on every commit:

```bash
uv run pre-commit install
```

You can also run them manually:

```bash
uv run pre-commit run --all-files
```

### Individual tools

| Tool | Purpose | Command |
| --- | --- | --- |
| **ruff** | Linting + auto-fix | `uv run ruff check --fix` |
| **ruff** | Formatting | `uv run ruff format` |
| **black** | Code formatting | `uv run black .` |
| **isort** | Import sorting | `uv run isort .` |
| **ty** | Type checking | `uv run ty check` |
| **markdownlint** | Markdown linting | runs via pre-commit |

## Project Structure

```text
fosdem_video/
  cli.py          # CLI argument parsing and main entry point
  discovery.py    # Talk discovery from ICS / schedule XML
  download.py     # Video and subtitle downloading
  models.py       # Talk dataclass and path helpers
  nfo.py          # NFO sidecar XML generation (Jellyfin)
  images.py       # Jellyfin metadata image resolution
assets/           # Bundled Jellyfin artwork
```

## Pull Request Guidelines

- Keep changes focused -- one feature or fix per PR.
- Make sure `uv run ruff check` and `uv run ty check` pass before submitting.
- Add or update docstrings for any new public functions.
