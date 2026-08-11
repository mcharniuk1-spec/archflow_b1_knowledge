#!/usr/bin/env python3
"""Assemble an exact ArchFlow public snapshot from a positive file manifest.

The target must not exist. The script never copies Git metadata, follows a
symlink, deletes a path, or discovers files outside the manifest.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
from pathlib import Path, PurePosixPath
from typing import Any


DEFAULT_MANIFEST = "public-product-manifest.json"


def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_manifest(path: Path) -> list[str]:
    payload = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates)
    if payload.get("schema_version") != "1.0":
        raise ValueError("manifest schema_version must be 1.0")
    files = payload.get("files")
    if not isinstance(files, list) or not files:
        raise ValueError("manifest files must be a non-empty list")
    if files != sorted(files) or len(files) != len(set(files)):
        raise ValueError("manifest files must be sorted and unique")
    for value in files:
        if not isinstance(value, str) or not value:
            raise ValueError("every manifest entry must be a non-empty string")
        relative = PurePosixPath(value)
        if relative.is_absolute() or ".." in relative.parts or "." in relative.parts:
            raise ValueError(f"unsafe manifest path: {value}")
        if relative.parts[0] == ".git" or "\\" in value:
            raise ValueError(f"forbidden manifest path: {value}")
    if DEFAULT_MANIFEST not in files or "scripts/assemble-public-release.py" not in files:
        raise ValueError("manifest must include itself and the assembler")
    return files


def aggregate_hash(root: Path, files: list[str]) -> str:
    digest = hashlib.sha256()
    for relative in files:
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update((root / relative).read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="New directory to create; it must not exist.")
    parser.add_argument("--source", type=Path, default=Path.cwd(), help="Candidate repository root.")
    parser.add_argument("--manifest", default=DEFAULT_MANIFEST, help="Manifest path relative to the source root.")
    args = parser.parse_args()

    source = args.source.resolve()
    target = args.target.resolve()
    if not source.is_dir():
        raise SystemExit("assembly=fail:source_not_directory")
    if target.exists():
        raise SystemExit("assembly=fail:target_must_not_exist")
    if target == source or source in target.parents:
        raise SystemExit("assembly=fail:target_must_be_outside_source")

    manifest_path = source / args.manifest
    try:
        files = load_manifest(manifest_path)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(f"assembly=fail:manifest:{error}") from error

    for relative in files:
        candidate = source / relative
        if candidate.is_symlink() or not candidate.is_file():
            raise SystemExit(f"assembly=fail:not_regular_file:{relative}")

    target.mkdir(parents=True, exist_ok=False)
    for relative in files:
        source_file = source / relative
        target_file = target / relative
        target_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source_file, target_file, follow_symlinks=False)
        target_file.chmod(0o755 if source_file.stat().st_mode & 0o111 else 0o644)
        if hasattr(os, "listxattr") and os.listxattr(target_file, follow_symlinks=False):
            raise SystemExit(f"assembly=fail:unexpected_extended_attribute:{relative}")

    copied = sorted(path.relative_to(target).as_posix() for path in target.rglob("*") if path.is_file())
    if copied != files:
        raise SystemExit("assembly=fail:target_file_set_mismatch")
    source_hash = aggregate_hash(source, files)
    target_hash = aggregate_hash(target, files)
    if source_hash != target_hash:
        raise SystemExit("assembly=fail:byte_mismatch")

    print(json.dumps({
        "assembly": "ok",
        "schema_version": "1.0",
        "files": len(files),
        "aggregate_sha256": source_hash,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
