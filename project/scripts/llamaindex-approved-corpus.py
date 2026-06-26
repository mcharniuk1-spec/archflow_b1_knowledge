#!/usr/bin/env python3
"""Build a bounded LlamaIndex document set over approved public files.

The first proof avoids cloud embeddings and raw private input. It loads only
approved public Markdown/YAML files, attaches repo-relative source paths, and
runs a deterministic keyword retrieval smoke test.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from llama_index.core import Document


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
OUTPUT_DIR = PROJECT / "local" / "rag_index"
SUMMARY_FILE = OUTPUT_DIR / "approved-corpus-summary.json"

INCLUDE_DIRS = [PROJECT, ROOT / "history", ROOT / "skills", ROOT / "wiki"]
SUFFIXES = {".md", ".yaml", ".yml"}
EXCLUDE_PARTS = {
    ".git",
    "__pycache__",
    "local",
    "raw",
    "source_exports",
    "private",
    "secrets",
    "tmp",
    "dashboard",
}
BLOCKED_TEXT = [
    re.compile(re.escape("/" + "Users/")),
    re.compile(re.escape("app" + ".notion" + ".com")),
    re.compile(re.escape("get" + "apple")),
    re.compile(
        r"(?m)^[ \t]*(?:LANGSMITH_API_KEY|OPENAI_API_KEY|ANTHROPIC_API_KEY|"
        r"GITHUB_TOKEN|GH_TOKEN|AWS_SECRET_ACCESS_KEY)[ \t]*=[ \t]*['\"]?[^'\"\s#]+"
    ),
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def approved_file(path: Path) -> bool:
    if not path.is_file() or path.suffix not in SUFFIXES:
        return False
    parts = set(path.relative_to(ROOT).parts)
    return not parts.intersection(EXCLUDE_PARTS) and not path.name.startswith(".env")


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in re.findall(r"[A-Za-z][A-Za-z0-9_-]{2,}", text)]


def load_documents() -> list[Document]:
    docs: list[Document] = []
    for base in INCLUDE_DIRS:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if not approved_file(path):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            if any(pattern.search(text) for pattern in BLOCKED_TEXT):
                continue
            docs.append(
                Document(
                    text=text,
                    metadata={
                        "source_path": rel(path),
                        "document_type": path.suffix.lstrip("."),
                        "public_safety_status": "approved_public_file",
                        "updated_at": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(),
                    },
                )
            )
    return docs


def retrieve(docs: list[Document], query: str, limit: int = 5) -> list[dict[str, object]]:
    query_terms = set(tokenize(query))
    scored: list[tuple[int, Document]] = []
    for doc in docs:
        counts = Counter(tokenize(doc.text))
        score = sum(counts[term] for term in query_terms)
        if score:
            scored.append((score, doc))
    scored.sort(key=lambda item: (-item[0], str(item[1].metadata.get("source_path", ""))))
    return [
        {
            "score": score,
            "source_path": doc.metadata["source_path"],
            "document_type": doc.metadata["document_type"],
        }
        for score, doc in scored[:limit]
    ]


def main() -> int:
    docs = load_documents()
    if not docs:
        raise SystemExit("llamaindex_index=fail:no_approved_documents")

    query = "dialogue PRD knowledge base LangGraph review gate"
    results = retrieve(docs, query)
    if not results:
        raise SystemExit("llamaindex_query=fail:no_results")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    SUMMARY_FILE.write_text(
        json.dumps(
            {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "document_count": len(docs),
                "query": query,
                "results": results,
                "boundary": "approved public files only",
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    print("llamaindex_documents=ok")
    print(f"document_count={len(docs)}")
    print("llamaindex_query=ok")
    for item in results:
        print(f"source={item['source_path']} score={item['score']}")
    print("persisted=project/local/rag_index/approved-corpus-summary.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
