"""CLI argument parsing and main entry point."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path
from sys import stdout

from fosdem_video.discovery import parse_ics_file, parse_schedule_xml
from fosdem_video.download import (
    _build_episode_index,
    create_dirs,
    download_fosdem_videos,
    is_downloaded,
    regenerate_nfos,
)

logger = logging.getLogger(__name__)


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments for the FOSDEM video downloader script."""
    parser = argparse.ArgumentParser(
        description="Download FOSDEM videos from an ICS file or by year",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Input mode: --ics or --year (mutually exclusive, one required)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "--ics",
        type=Path,
        help="Path to the FOSDEM schedule ICS file",
    )
    input_group.add_argument(
        "--year",
        type=int,
        help="FOSDEM edition year (e.g. 2025) to fetch talks from schedule XML",
    )

    # Filters (valid only with --year)
    parser.add_argument(
        "--track",
        type=str,
        help="Filter talks by track name (requires --year)",
    )
    parser.add_argument(
        "--talk",
        type=str,
        help="Download a single talk by slug/ID (requires --year)",
    )

    # Format and subtitle options
    parser.add_argument(
        "--format",
        choices=["mp4", "av1.webm"],
        default="av1.webm",
        help="Video format to download",
    )
    parser.add_argument(
        "--no-vtt",
        action="store_true",
        help="Skip downloading .vtt subtitle files",
    )

    # Output options
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("./fosdem_videos"),
        help="Root directory for downloaded files",
    )
    parser.add_argument(
        "--jellyfin",
        action="store_true",
        help=(
            "Use Jellyfin-compatible folder layout: "
            "Fosdem (<year>)/<track>/<slug>/. "
            "Generates .nfo metadata sidecars when used with --year"
        ),
    )

    # General options
    parser.add_argument(
        "-w",
        "--workers",
        type=int,
        default=3,
        help="Number of concurrent downloads",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print video URLs without downloading",
    )
    parser.add_argument(
        "--regenerate-nfo",
        action="store_true",
        help=(
            "Regenerate all .nfo metadata files for already-downloaded "
            "videos without re-downloading them (requires --jellyfin "
            "and --year)"
        ),
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"],
        help="Set the logging output level",
    )

    args = parser.parse_args()

    # Validate --track and --talk require --year
    if args.track and not args.year:
        parser.error("--track requires --year")
    if args.talk and not args.year:
        parser.error("--talk requires --year")

    # Validate --regenerate-nfo requires --jellyfin and --year
    if args.regenerate_nfo and not args.jellyfin:
        parser.error("--regenerate-nfo requires --jellyfin")
    if args.regenerate_nfo and not args.year:
        parser.error("--regenerate-nfo requires --year")

    # Validate ICS file exists when provided
    if args.ics and not args.ics.exists():
        parser.error(f"ICS file not found: {args.ics}")

    return args


def main() -> None:
    """Run the FOSDEM video downloader script."""
    args = parse_arguments()
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s - %(levelname)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    fmt: str = args.format

    # Discover talks from the selected input mode
    if args.ics:
        logger.info("Parsing ICS file %s", args.ics)
        all_talks = parse_ics_file(args.ics, fmt=fmt)
        talks = all_talks
    else:
        logger.info("Fetching schedule for FOSDEM %s", args.year)
        # Always fetch ALL talks first so that the episode index reflects
        # the full schedule.  Season numbers are derived from the
        # alphabetical position of each track across the entire conference,
        # not just the downloaded subset.
        all_talks = parse_schedule_xml(args.year, fmt=fmt)
        talks = all_talks

        # Apply --track / --talk filters *after* building the full list.
        if args.track:
            talks = [t for t in all_talks if t.track.lower() == args.track.lower()]
        if args.talk:
            talks = [t for t in talks if t.id == args.talk]

    logger.info("Found %s talks", len(talks))

    # Build episode index from the FULL talk list so that season numbers
    # reflect each track's position in the complete schedule — not just
    # the filtered subset.  For ICS mode there is no unfiltered list, so
    # we fall back to whatever was parsed.
    if args.jellyfin:
        episode_index = _build_episode_index(all_talks)
    else:
        episode_index = {}

    # Regenerate NFOs and images for all talks (including already-downloaded)
    if args.regenerate_nfo:
        regenerate_nfos(
            talks,
            args.output,
            fmt=fmt,
            episode_index=episode_index,
        )

    # Filter already-downloaded talks
    talks = [
        talk
        for talk in talks
        if not is_downloaded(
            args.output,
            talk,
            fmt,
            jellyfin=args.jellyfin,
            episode_index=episode_index,
        )
    ]
    logger.info("Found %s videos to download", len(talks))

    if args.dry_run:
        urls = "\n".join([f"  - {talk.url}" for talk in talks])
        stdout.write(f"List of talks videos: \n{urls}\n")
        return

    create_dirs(args.output, talks, jellyfin=args.jellyfin, episode_index=episode_index)
    results = download_fosdem_videos(
        talks,
        output_dir=args.output,
        fmt=fmt,
        num_workers=args.workers,
        no_vtt=args.no_vtt,
        jellyfin=args.jellyfin,
        episode_index=episode_index,
    )
    successful = len([r for r in results if r])
    logger.info("Downloaded %s of %s talks", successful, len(talks))
