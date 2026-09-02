#!/usr/bin/env python3
"""Create a non-destructive dated workspace for one daily Skill cassette issue."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def shanghai_today() -> str:
    return datetime.now(ZoneInfo("Asia/Shanghai")).date().isoformat()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create content/daily and deliveries folders for one dated issue."
    )
    parser.add_argument("slug", help="Lowercase ASCII slug, for example grill-me")
    parser.add_argument(
        "--date",
        default=shanghai_today(),
        help="Issue date in YYYY-MM-DD (default: today in Asia/Shanghai)",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository root (default: current directory)",
    )
    return parser.parse_args()


def validate(args: argparse.Namespace) -> None:
    if not SLUG_RE.fullmatch(args.slug):
        raise ValueError(
            "slug must contain lowercase letters, digits, and single hyphens only"
        )
    if not DATE_RE.fullmatch(args.date):
        raise ValueError("date must use YYYY-MM-DD")
    try:
        datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError("date must be a real calendar date") from exc


def write_seed(path: Path, title: str, guidance: str) -> None:
    path.write_text(f"# {title}\n\n{guidance}\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    try:
        validate(args)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    root = args.root.resolve()
    work = root / "content" / "daily" / args.date / args.slug
    delivery = root / "deliveries" / args.date / args.slug

    conflicts = [path for path in (work, delivery) if path.exists()]
    if conflicts:
        joined = ", ".join(str(path) for path in conflicts)
        print(f"error: refusing to overwrite existing issue: {joined}", file=sys.stderr)
        return 1

    (work / "assets").mkdir(parents=True)
    (work / "png").mkdir()
    delivery.mkdir(parents=True)

    write_seed(
        work / "brief.md",
        "Brief",
        "Topic:\n\nAudience lean:\n\nFun payoff:\n\nVisual adjustment:",
    )
    write_seed(
        work / "sources.md",
        "Sources (internal)",
        "Record canonical URLs, access date, supported claims, install instructions, caveats, and every source-supported field needed by the detailed final release card here.",
    )
    write_seed(
        work / "copy.md",
        "Carousel copy",
        "Draft the final page-by-page Chinese copy here before layout. Every concrete recommendation must end with the detailed cassette release card.",
    )
    write_seed(
        work / "image-prompts.md",
        "Image prompts (internal)",
        "Keep generated artwork free of text, logos, UI, and pseudo-lettering.",
    )

    print(f"work={work}")
    print(f"delivery={delivery}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
