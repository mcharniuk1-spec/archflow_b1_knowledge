#!/usr/bin/env python3
"""Validate the exact, portable ArchFlow public-product snapshot."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "public-product-manifest.json"
PUBLICATION = "project/assets/linkedin/knowledge-operator-v3/archflow-knowledge-operator-metrics.png"
BENCHMARK = "project/benchmarks/actionable-agents-v3-results.json"
IGNORED_PARTS = {".git", "__pycache__", ".mypy_cache", ".ruff_cache"}
IGNORED_PREFIXES = ("project/local/",)
FORBIDDEN_PREFIXES = (
    "history/",
    "wiki/",
    "graphify-out/",
    "project/automation/",
    "project/content/",
    "project/issues/",
    "project/knowledge/",
    "project/live/",
    "project/qa/",
    "project/reports/",
    "project/runs/",
)
REQUIRED_ENTRYPOINTS = {
    "index.html",
    "jarvis.html",
    "project/dashboard/index.html",
    "project/dashboard/data.json",
    "project/dashboard/data.js",
    "project/assets/architecture/knowledge-crew-tower.svg",
    "project/assets/architecture/context-input-flow.svg",
    "project/assets/architecture/output-receipt-flow.svg",
    "project/assets/architecture/onboarding-teamwork-flow.svg",
    PUBLICATION,
    BENCHMARK,
}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_LINK = re.compile(r"\b(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
CSS_LINK = re.compile(r"url\(([^)]+)\)", re.IGNORECASE)


def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates)
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path.relative_to(ROOT)}")
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest_files() -> list[str]:
    payload = read_json(MANIFEST_PATH)
    files = payload.get("files")
    if payload.get("schema_version") != "1.0" or not isinstance(files, list):
        raise ValueError("invalid product manifest schema")
    if files != sorted(files) or len(files) != len(set(files)):
        raise ValueError("product manifest files must be sorted and unique")
    for value in files:
        if not isinstance(value, str) or not value:
            raise ValueError("manifest paths must be non-empty strings")
        path = PurePosixPath(value)
        if path.is_absolute() or ".." in path.parts or "." in path.parts or "\\" in value:
            raise ValueError(f"unsafe manifest path: {value}")
        if value.startswith(FORBIDDEN_PREFIXES):
            raise ValueError(f"forbidden product path: {value}")
    return files


def visible_files() -> list[str]:
    result = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT).as_posix()
        if any(part in IGNORED_PARTS for part in path.relative_to(ROOT).parts):
            continue
        if relative.startswith(IGNORED_PREFIXES) or relative.endswith((".pyc", ".DS_Store")):
            continue
        result.append(relative)
    return sorted(result)


def normalize_reference(source: str, raw: str) -> str | None:
    value = raw.strip().strip("<>").split()[0].strip("\"'")
    value = value.split("#", 1)[0].split("?", 1)[0]
    if not value or value.startswith(("#", "/", "data:", "mailto:", "tel:", "javascript:")):
        return None
    if re.match(r"^[a-z][a-z0-9+.-]*://", value, re.IGNORECASE):
        return None
    if any(marker in value for marker in ("<", ">", "${", "{{")):
        return None
    base = PurePosixPath(source).parent
    parts: list[str] = []
    for part in (base / value).parts:
        if part == ".":
            continue
        if part == "..":
            if not parts:
                return f"<escape>/{value}"
            parts.pop()
        else:
            parts.append(part)
    return PurePosixPath(*parts).as_posix()


def link_errors(files: list[str]) -> list[str]:
    file_set = set(files)
    errors: list[str] = []
    for relative in files:
        suffix = Path(relative).suffix.lower()
        if suffix not in {".md", ".html", ".css", ".svg"}:
            continue
        text = (ROOT / relative).read_text(encoding="utf-8")
        references = []
        if suffix == ".md":
            references.extend(match.group(1) for match in MARKDOWN_LINK.finditer(text))
        if suffix in {".html", ".svg"}:
            references.extend(match.group(1) for match in HTML_LINK.finditer(text))
        if suffix == ".css":
            references.extend(match.group(1) for match in CSS_LINK.finditer(text))
        for raw in references:
            target = normalize_reference(relative, raw)
            if target is None:
                continue
            candidates = {target, f"{target.rstrip('/')}/index.html", f"{target.rstrip('/')}/README.md"}
            if not candidates.intersection(file_set):
                errors.append(f"{relative} -> {raw} ({target})")
    return sorted(set(errors))


def png_info(path: Path) -> tuple[int, int, int, list[str]]:
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"not PNG: {path.relative_to(ROOT)}")
    offset = 8
    chunks: list[str] = []
    width = height = color_type = -1
    while offset < len(data):
        length = struct.unpack(">I", data[offset : offset + 4])[0]
        kind = data[offset + 4 : offset + 8].decode("ascii")
        payload = data[offset + 8 : offset + 8 + length]
        chunks.append(kind)
        if kind == "IHDR":
            width, height, _, color_type, _, _, _ = struct.unpack(">IIBBBBB", payload)
        offset += 12 + length
    return width, height, color_type, chunks


def validate_publication() -> None:
    width, height, color_type, chunks = png_info(ROOT / PUBLICATION)
    if (width, height, color_type) != (1080, 1350, 2):
        raise ValueError("publication PNG must be 1080x1350 RGB")
    if set(chunks) - {"IHDR", "IDAT", "IEND"}:
        raise ValueError("publication PNG contains nonessential metadata chunks")
    benchmark_hash = sha256(ROOT / BENCHMARK)
    publication_hash = sha256(ROOT / PUBLICATION)
    notes = (ROOT / "project/assets/linkedin/knowledge-operator-v3/asset-notes.md").read_text(encoding="utf-8")
    if benchmark_hash not in notes or publication_hash not in notes:
        raise ValueError("publication notes do not bind final image and benchmark hashes")


def aggregate_hash(files: list[str]) -> str:
    digest = hashlib.sha256()
    for relative in files:
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update((ROOT / relative).read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exact", action="store_true", help="Require no unlisted visible file outside ignored local state.")
    args = parser.parse_args()
    try:
        files = manifest_files()
        missing = sorted(relative for relative in files if not (ROOT / relative).is_file())
        if missing:
            raise ValueError(f"missing manifest files: {missing}")
        if not REQUIRED_ENTRYPOINTS.issubset(files):
            raise ValueError(f"missing required entrypoints: {sorted(REQUIRED_ENTRYPOINTS - set(files))}")
        corpus = read_json(ROOT / "project/dashboard/corpus-manifest.json").get("files", [])
        if not isinstance(corpus, list) or not set(corpus).issubset(files):
            raise ValueError("dashboard corpus is not contained by the public product manifest")
        errors = link_errors(files)
        if errors:
            raise ValueError("broken local links: " + "; ".join(errors[:20]))
        validate_publication()
        if args.exact:
            actual = visible_files()
            if actual != files:
                missing_from_root = sorted(set(files) - set(actual))
                unexpected = sorted(set(actual) - set(files))
                raise ValueError(f"exact file-set mismatch missing={missing_from_root} unexpected={unexpected}")
    except (OSError, ValueError, json.JSONDecodeError, UnicodeDecodeError) as error:
        print(f"public_release=fail:{error}")
        return 1
    print("public_release=ok")
    print(f"files={len(files)}")
    print(f"corpus_files={len(corpus)}")
    print(f"aggregate_sha256={aggregate_hash(files)}")
    print(f"publication_sha256={sha256(ROOT / PUBLICATION)}")
    print(f"benchmark_sha256={sha256(ROOT / BENCHMARK)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
