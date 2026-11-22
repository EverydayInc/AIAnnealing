#!/usr/bin/env python3
"""Validate package structure, byte manifest, schemas, and reference fixtures."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


REQUIRED_PATHS = [
    "README.md",
    "LICENSE",
    "AUTHOR-RIGHTS-AGREEMENT.md",
    "NOTICE.md",
    "QUICKSTART.md",
    "agents/PARETO.md",
    "skill/annealing-pareto/SKILL.md",
    "skill/annealing-pareto/LICENSE",
    "skill/annealing-pareto/references/PROTOCOL.md",
    "skill/annealing-pareto/references/SAFETY-BOUNDARIES.md",
    "skill/annealing-pareto/references/OUTPUT-FORMATS.md",
    "machine/manifest.json",
    "machine/round-report.schema.json",
    "machine/pareto-verdict.schema.json",
    "machine/final-result.schema.json",
    "examples/positive-long-tail/expected/criteria.json",
    "examples/positive-long-tail/expected/reference-result.json",
    "examples/safety-control-stop/expected/criteria.json",
    "examples/safety-control-stop/expected/reference-result.json",
    "provenance/SOURCES.md",
    "provenance/annealing-v01-live.md",
    "provenance/pareto-live.md",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_skill(root: Path, failures: list[str]) -> None:
    skill_path = root / "skill" / "annealing-pareto" / "SKILL.md"
    text = skill_path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        failures.append("SKILL.md: missing YAML frontmatter")
        return
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if line and not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    name = fields.get("name", "")
    description = fields.get("description", "")
    if name != skill_path.parent.name:
        failures.append(f"SKILL.md: name {name!r} does not match directory")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        failures.append("SKILL.md: invalid Agent Skills name")
    if not 1 <= len(description) <= 1024:
        failures.append("SKILL.md: description must be 1-1024 characters")


def validate_manifest(root: Path, failures: list[str]) -> None:
    manifest_path = root / "machine" / "manifest.json"
    manifest = load_json(manifest_path)
    entries = manifest.get("files")
    if not isinstance(entries, list):
        failures.append("manifest: files must be an array")
        return
    listed: set[str] = set()
    for entry in entries:
        relative = entry.get("path", "")
        expected = entry.get("sha256", "")
        if relative in listed:
            failures.append(f"manifest: duplicate path {relative}")
            continue
        listed.add(relative)
        path = root / relative
        if not path.is_file():
            failures.append(f"manifest: missing file {relative}")
        elif sha256(path) != expected:
            failures.append(f"manifest: hash mismatch {relative}")
    actual = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file()
        and not ({".git", "__pycache__"} & set(path.parts))
        and path.suffix not in {".pyc", ".pyo", ".zip"}
        and path.relative_to(root).as_posix() not in {"machine/manifest.json", "CHECKSUMS.sha256"}
    }
    if listed != actual:
        for relative in sorted(actual - listed):
            failures.append(f"manifest: unlisted file {relative}")
        for relative in sorted(listed - actual):
            failures.append(f"manifest: listed non-package file {relative}")


def validate_json_documents(root: Path, failures: list[str]) -> None:
    for path in sorted(root.rglob("*.json")):
        try:
            load_json(path)
        except (OSError, json.JSONDecodeError) as error:
            failures.append(f"invalid JSON {path.relative_to(root)}: {error}")


def validate_fixtures(root: Path, failures: list[str]) -> None:
    evaluator = root / "scripts" / "evaluate_run.py"
    for case_name in ("positive-long-tail", "safety-control-stop"):
        case = root / "examples" / case_name
        result = case / "expected" / "reference-result.json"
        process = subprocess.run(
            [sys.executable, str(evaluator), "--case", str(case), "--result", str(result)],
            capture_output=True,
            text=True,
            check=False,
        )
        if process.returncode:
            failures.append(f"fixture {case_name}: {process.stdout}{process.stderr}".strip())


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Annealing + Pareto package")
    parser.add_argument("root", nargs="?", default=".", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    failures: list[str] = []

    for relative in REQUIRED_PATHS:
        if not (root / relative).is_file():
            failures.append(f"missing required file {relative}")
    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1

    try:
        validate_skill(root, failures)
        validate_json_documents(root, failures)
        validate_manifest(root, failures)
        validate_fixtures(root, failures)
    except (OSError, json.JSONDecodeError, TypeError) as error:
        failures.append(str(error))

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        print(f"RESULT failures={len(failures)}")
        return 1

    print("PASS package=annealing-pareto-v02 fixtures=2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
