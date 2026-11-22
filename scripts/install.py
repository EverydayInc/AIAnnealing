#!/usr/bin/env python3
"""Install the Annealing + Pareto Agent Skill without overwriting existing work."""

from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
from pathlib import Path


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def files_below(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*") if path.is_file())


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Plan or install the annealing-pareto Agent Skill."
    )
    parser.add_argument(
        "--target",
        required=True,
        type=Path,
        help="Skills parent directory; annealing-pareto is created below it",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Perform the copy; without this flag the command is a dry-run",
    )
    args = parser.parse_args()

    package_root = Path(__file__).resolve().parent.parent
    source = package_root / "skill" / "annealing-pareto"
    target_root = args.target.expanduser().resolve()
    destination = target_root / "annealing-pareto"

    if not source.is_dir():
        print(f"ERROR source skill not found: {source}", file=sys.stderr)
        return 2
    if destination.exists():
        print(f"ERROR refusing to overwrite existing destination: {destination}", file=sys.stderr)
        return 3

    source_files = files_below(source)
    print(f"MODE={'apply' if args.apply else 'dry-run'}")
    print(f"SOURCE={source}")
    print(f"DESTINATION={destination}")
    for path in source_files:
        relative = path.relative_to(source)
        print(f"COPY {relative.as_posix()} sha256:{file_hash(path)}")

    if not args.apply:
        print(f"PLAN files={len(source_files)} nothing-written")
        return 0

    target_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    for source_path in source_files:
        relative = source_path.relative_to(source)
        installed_path = destination / relative
        if file_hash(source_path) != file_hash(installed_path):
            print(f"ERROR verification failed: {relative}", file=sys.stderr)
            return 4

    print(f"INSTALLED files={len(source_files)} verified=sha256")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
