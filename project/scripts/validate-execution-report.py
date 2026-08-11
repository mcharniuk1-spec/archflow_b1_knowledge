#!/usr/bin/env python3
"""Validate required fields in public-safe execution reports."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED = [
    "## Run identity",
    "## Actor and skill ledger",
    "## Architecture evidence",
    "## Deliverables and checks",
    "## Interpretation",
    "## Memory and next action",
]
ARCH_COMPONENTS = ("LangGraph", "CrewAI", "LlamaIndex", "Parallel execution", "Maintained knowledge")
STATUSES = {"configured", "planned", "locally_tested", "executed", "reviewed", "promoted", "blocked", "not_recorded"}


def validate(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors = [f"missing section: {section}" for section in REQUIRED if section not in text]
    for component in ARCH_COMPONENTS:
        if component not in text:
            errors.append(f"missing architecture component: {component}")
    status = re.search(r"^Status:\s*`?([a-z_]+)", text, re.MULTILINE)
    if not status or status.group(1) not in STATUSES:
        errors.append("status must use an allowed truth state")
    if "FACT:" not in text or "INTERPRETATION:" not in text or "GAP:" not in text:
        errors.append("interpretation must include FACT, INTERPRETATION, and GAP")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    failed = False
    for path in args.paths:
        errors = validate(path)
        if errors:
            failed = True
            print(f"{path}: FAIL")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"{path}: PASS")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
