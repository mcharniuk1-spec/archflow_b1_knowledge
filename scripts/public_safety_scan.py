#!/usr/bin/env python3
"""Public repository safety scan.

Scans publishable files only: tracked files plus non-ignored untracked files.
Ignored local env/runtime files are not scanned because they are not push
candidates. The goal is to block accidental publication of secrets, private
links, local paths, and unsafe metadata.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def git_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    return [ROOT / line for line in result.stdout.splitlines() if line.strip()]


def read_text(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        parts: list[str] = []
        if shutil.which("pdfinfo"):
            meta = subprocess.run(
                ["pdfinfo", str(path)],
                text=True,
                capture_output=True,
                cwd=ROOT,
            )
            parts.append(meta.stdout)
            parts.append(meta.stderr)
        if shutil.which("pdftotext"):
            text = subprocess.run(
                ["pdftotext", str(path), "-"],
                text=True,
                capture_output=True,
                cwd=ROOT,
            )
            parts.append(text.stdout)
            parts.append(text.stderr)
        return "\n".join(parts)

    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def build_patterns() -> list[tuple[str, re.Pattern[str]]]:
    home_path = "/" + "Users/"
    local_owner = "get" + "apple"
    private_notion = "app" + ".notion" + ".com"
    notion_scheme_parts = ["user" + "://", "collection" + "://", "view" + "://"]
    personal_name = "M" + "ax"

    cyrillic_terms = [
        "\u041c\u0430\u043a\u0441",
        "\u041c\u0438\u0448\u0430",
        "\u042d\u043f\u0438\u043a",
        "\u0417\u0430\u0434\u0430\u0447",
        "\u0410\u0443\u0442\u0440\u0438\u0447",
        "\u0434\u0432\u0438\u0436\u043e\u043a",
        "\u041a\u043e\u043d\u0442\u0435\u043d\u0442",
        "\u0421\u0430\u0439\u0442",
        "\u0432\u0435\u0440\u0434\u0438\u043a\u0442",
    ]

    raw_patterns = [
        ("local_home_path", re.escape(home_path)),
        ("local_owner_token", re.escape(local_owner)),
        ("private_notion_url", re.escape(private_notion)),
        ("github_token", r"gh[pousr]_[A-Za-z0-9_]{20,}"),
        ("openai_key", r"sk-(?:proj-)?[A-Za-z0-9_-]{20,}"),
        ("langsmith_key", r"ls(?:v2|__)[A-Za-z0-9_.-]{20,}"),
        ("slack_token", r"xox[baprs]-[A-Za-z0-9-]{20,}"),
        ("aws_access_key", r"AKIA[0-9A-Z]{16}"),
        (
            "nonempty_secret_env",
            r"(?m)^[ \t]*(?:LANGSMITH_API_KEY|OPENAI_API_KEY|ANTHROPIC_API_KEY|"
            r"GITHUB_TOKEN|GH_TOKEN|AWS_SECRET_ACCESS_KEY)[ \t]*=[ \t]*['\"]?[^'\"\s#]+",
        ),
        ("personal_name", r"\b" + re.escape(personal_name) + r"\b"),
    ]
    raw_patterns.extend((f"private_scheme_{i}", re.escape(s)) for i, s in enumerate(notion_scheme_parts))
    raw_patterns.extend((f"cyrillic_private_term_{i}", re.escape(s)) for i, s in enumerate(cyrillic_terms))
    return [(name, re.compile(pattern)) for name, pattern in raw_patterns]


def blocked_path(path: Path) -> str | None:
    rel = path.relative_to(ROOT).as_posix()
    base = path.name
    if base == ".DS_Store":
        return "macos_metadata"
    if base == ".env" or base.startswith(".env."):
        return "env_file_must_not_be_tracked"
    if rel.startswith("project/local/"):
        return "local_runtime_file_must_not_be_tracked"
    if "/raw/" in f"/{rel}/" or rel.startswith("raw/"):
        return "raw_source_folder_must_not_be_tracked"
    if "/private/" in f"/{rel}/" or rel.startswith("private/"):
        return "private_folder_must_not_be_tracked"
    if "/secrets/" in f"/{rel}/" or rel.startswith("secrets/"):
        return "secrets_folder_must_not_be_tracked"
    return None


def main() -> int:
    patterns = build_patterns()
    findings: list[str] = []

    for path in git_files():
        if not path.exists() or not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        reason = blocked_path(path)
        if reason:
            findings.append(f"{rel}: blocked_path:{reason}")
            continue
        text = read_text(path)
        for name, pattern in patterns:
            if pattern.search(text):
                findings.append(f"{rel}: pattern:{name}")

    if findings:
        print("Public safety scan failed.", file=sys.stderr)
        for item in findings:
            print(item, file=sys.stderr)
        return 1

    print("Public safety scan passed.")
    return 0


if __name__ == "__main__":
    os.chdir(ROOT)
    raise SystemExit(main())
