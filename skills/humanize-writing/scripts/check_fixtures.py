#!/usr/bin/env python3
"""Check protected content and meaning invariants in the local fixtures."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "fixtures"


def read(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def protected_spans(text: str) -> list[str]:
    spans = []
    spans.extend(re.findall(r"https?://[^\s)]+", text))
    spans.extend(re.findall(r"\[\d+\]:\s+\S+", text))
    spans.extend(re.findall(r"```.*?```", text, flags=re.DOTALL))
    spans.extend(re.findall(r"`[^`]+`", text))
    spans.extend(re.findall(r"(?ms)^---\n.*?\n---", text)[:1])
    return spans


def check_pair(stem: str, required: list[str]) -> None:
    source = read(f"{stem}-source.md")
    output = read(f"{stem}-output.md")
    for value in required:
        require(value in output, f"{stem}: required value missing: {value}")
    for span in protected_spans(source):
        require(span in output, f"{stem}: protected span changed or disappeared: {span}")


def main() -> int:
    check_pair("01-factual", ["approved evidence", "review", "https://example.com/docs"])
    check_pair("02-cited-argument", ["does not prove faster delivery"])
    check_pair("03-technical", ["HTTP 429", "retry_after", "response.headers[\"retry_after\"]"])
    check_pair("04-style", ["short", "useful point", "—", "Style sample:"])
    source = read("05-already-human-source.md")
    output = read("05-already-human-output.md")
    require(source == output, "05-already-human: already-natural prose should remain unchanged")
    print("humanize-writing fixtures: PASS (5 cases; protected facts, links, citations, code, frontmatter, and style sample preserved)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, OSError) as exc:
        print(f"humanize-writing fixtures: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
