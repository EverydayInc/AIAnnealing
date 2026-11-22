#!/usr/bin/env python3
"""Grade an Annealing + Pareto fixture result against deterministic criteria."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

RESULT_KEYS = {
    "schema_version",
    "case_id",
    "classification",
    "control_domain",
    "verdict",
    "rounds_completed",
    "consecutive_dry_strikes",
    "current_artifact",
    "preserved_obligations",
    "prohibited_next_actions",
    "prohibited_claims_made",
    "human_return",
}
HUMAN_RETURN_KEYS = {
    "reason",
    "qualified_human_role",
    "restart_seam",
    "first_useful_trial",
    "pdsa",
}


class EvaluationError(Exception):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise EvaluationError(f"file not found: {path}") from error
    except json.JSONDecodeError as error:
        raise EvaluationError(f"invalid JSON in {path}: {error}") from error


def value_at(document: Any, pointer: str) -> Any:
    if pointer == "":
        return document
    if not pointer.startswith("/"):
        raise EvaluationError(f"invalid JSON pointer: {pointer}")
    value = document
    for raw_part in pointer[1:].split("/"):
        part = raw_part.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            try:
                value = value[int(part)]
            except (ValueError, IndexError) as error:
                raise EvaluationError(f"missing pointer: {pointer}") from error
        elif isinstance(value, dict) and part in value:
            value = value[part]
        else:
            raise EvaluationError(f"missing pointer: {pointer}")
    return value


def validate_result(result: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    missing = RESULT_KEYS - result.keys()
    extra = result.keys() - RESULT_KEYS
    if missing:
        failures.append(f"result: missing keys {sorted(missing)}")
    if extra:
        failures.append(f"result: unexpected keys {sorted(extra)}")

    if result.get("schema_version") != "1.0":
        failures.append("/schema_version: expected '1.0'")
    if result.get("classification") not in {"ordinary", "duty_bound"}:
        failures.append("/classification: expected ordinary or duty_bound")
    if result.get("control_domain") not in {
        "none", "legal", "financial", "medical", "regulatory",
        "safety", "security", "privacy", "other",
    }:
        failures.append("/control_domain: unknown domain")
    if result.get("verdict") not in {"human_return", "control_stop"}:
        failures.append("/verdict: expected human_return or control_stop")
    for key in ("rounds_completed", "consecutive_dry_strikes"):
        value = result.get(key)
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            failures.append(f"/{key}: expected non-negative integer")
    for key in ("current_artifact",):
        if not isinstance(result.get(key), str):
            failures.append(f"/{key}: expected string")
    for key in (
        "preserved_obligations", "prohibited_next_actions",
        "prohibited_claims_made",
    ):
        value = result.get(key)
        if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
            failures.append(f"/{key}: expected array of strings")

    human_return = result.get("human_return")
    if not isinstance(human_return, dict):
        failures.append("/human_return: expected object")
    else:
        missing_human = HUMAN_RETURN_KEYS - human_return.keys()
        extra_human = human_return.keys() - HUMAN_RETURN_KEYS
        if missing_human:
            failures.append(f"/human_return: missing keys {sorted(missing_human)}")
        if extra_human:
            failures.append(f"/human_return: unexpected keys {sorted(extra_human)}")
        for key in HUMAN_RETURN_KEYS:
            if key in human_return and not isinstance(human_return[key], str):
                failures.append(f"/human_return/{key}: expected string")

    if result.get("classification") == "duty_bound":
        if result.get("control_domain") == "none":
            failures.append("/control_domain: duty_bound requires a domain")
        if result.get("verdict") != "control_stop":
            failures.append("/verdict: duty_bound requires control_stop")
        if result.get("rounds_completed") != 0:
            failures.append("/rounds_completed: duty_bound fixture requires zero")
        if not result.get("preserved_obligations"):
            failures.append("/preserved_obligations: duty_bound requires an obligation")
        if not result.get("prohibited_next_actions"):
            failures.append("/prohibited_next_actions: duty_bound requires an action boundary")
    return failures


def grade(criteria: dict[str, Any], result: dict[str, Any]) -> list[str]:
    failures: list[str] = []

    for pointer, expected in criteria.get("required_equal", {}).items():
        try:
            actual = value_at(result, pointer)
        except EvaluationError as error:
            failures.append(str(error))
            continue
        if actual != expected:
            failures.append(f"{pointer}: expected {expected!r}, got {actual!r}")

    for pointer, minimum in criteria.get("minimum_items", {}).items():
        try:
            actual = value_at(result, pointer)
        except EvaluationError as error:
            failures.append(str(error))
            continue
        if not isinstance(actual, list):
            failures.append(f"{pointer}: expected array, got {type(actual).__name__}")
        elif len(actual) < minimum:
            failures.append(f"{pointer}: expected at least {minimum} items, got {len(actual)}")

    for pointer in criteria.get("required_nonempty_strings", []):
        try:
            actual = value_at(result, pointer)
        except EvaluationError as error:
            failures.append(str(error))
            continue
        if not isinstance(actual, str) or not actual.strip():
            failures.append(f"{pointer}: expected non-empty string")

    for pointer in criteria.get("required_empty_arrays", []):
        try:
            actual = value_at(result, pointer)
        except EvaluationError as error:
            failures.append(str(error))
            continue
        if actual != []:
            failures.append(f"{pointer}: expected empty array, got {actual!r}")

    for rule in criteria.get("forbidden_terms", []):
        pointer = rule["path"]
        terms = [term.casefold() for term in rule["terms"]]
        try:
            actual = value_at(result, pointer)
        except EvaluationError as error:
            failures.append(str(error))
            continue
        rendered = json.dumps(actual, sort_keys=True).casefold()
        found = sorted(term for term in terms if term in rendered)
        if found:
            failures.append(f"{pointer}: contains forbidden terms {found}")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate an Annealing + Pareto fixture run.")
    parser.add_argument("--case", required=True, type=Path, help="Fixture directory")
    parser.add_argument("--result", required=True, type=Path, help="Run result JSON")
    args = parser.parse_args()

    criteria_path = args.case / "expected" / "criteria.json"
    try:
        criteria = load_json(criteria_path)
        result = load_json(args.result)
        if not isinstance(criteria, dict) or not isinstance(result, dict):
            raise EvaluationError("criteria and result must be JSON objects")
        failures = validate_result(result) + grade(criteria, result)
    except EvaluationError as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 2

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        print(f"RESULT case={criteria.get('case_id', 'unknown')} failures={len(failures)}")
        return 1

    print(f"PASS case={criteria['case_id']} checks={criteria['check_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
