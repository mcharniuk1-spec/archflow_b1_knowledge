#!/usr/bin/env python3
"""Remove local filesystem provenance from public Graphify artifacts."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUTS = (
    ROOT / "graphify-out" / "graph.json",
    ROOT / "graphify-out" / "manifest.json",
    ROOT / "graphify-out" / "graph.html",
)

LOCAL_PATH = re.compile(r"/" + "Users" + r"/[^\"'<>\s]+")
PRIVATE_PATH = re.compile(r"/" + "private" + r"/(?:tmp|var)/[^\"'<>\s]+")
OWNER_TOKEN = re.compile("get" + "apple", re.IGNORECASE)


def sanitize_text(value: str) -> str:
    value = LOCAL_PATH.sub("[local-path]", value)
    value = PRIVATE_PATH.sub("[private-path]", value)
    return OWNER_TOKEN.sub("[local-owner]", value)


def sanitize_json(value):
    if isinstance(value, dict):
        return {sanitize_text(str(key)): sanitize_json(item) for key, item in value.items()}
    if isinstance(value, list):
        return [sanitize_json(item) for item in value]
    if isinstance(value, str):
        return sanitize_text(value)
    return value


def main() -> None:
    for output in OUTPUTS:
        if not output.exists():
            continue
        if output.suffix == ".json":
            data = json.loads(output.read_text())
            output.write_text(json.dumps(sanitize_json(data), indent=2) + "\n")
        else:
            output.write_text(sanitize_text(output.read_text()))
        print(f"sanitized {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
