#!/usr/bin/env python3
"""Run deterministic retrieval over the exact approved public corpus.

The default path is deliberately standard-library only. It provides the
source-path and chunk contract used by the dashboard and benchmarks without
starting a model, probing a local service, reading provider configuration, or
expanding a directory. An optional deep-import check proves that LlamaIndex is
installed; it does not change the retrieval result or call a provider.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import re
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class LocalDocument:
    """Provider-free document shape used by the deterministic retrieval path."""

    text: str
    metadata: dict[str, Any]


Document = LocalDocument

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
OUTPUT_DIR = PROJECT / "local" / "rag_index"
SUMMARY_FILE = OUTPUT_DIR / "approved-corpus-summary.json"
CORPUS_MANIFEST = PROJECT / "dashboard" / "corpus-manifest.json"

SUFFIXES = {".json", ".md", ".yaml", ".yml"}
BLOCKED_PATH_PARTS = {
    ".git",
    "history",
    "private",
    "reports",
    "runs",
    "secrets",
    "source_exports",
    "tmp",
    "wiki",
}
BLOCKED_TEXT = {
    "local_unix_home": re.compile(r"/(?:Users|home)/[A-Za-z0-9._-]+/"),
    "local_windows_home": re.compile(r"[A-Za-z]:\\\\Users\\\\[^\\\\\s]+\\\\"),
    "local_file_url": re.compile("file:" + r"///(?:Users|home)/", re.IGNORECASE),
    "nonempty_secret_assignment": re.compile(
        r"(?im)^\s*(?:[A-Z0-9_]*(?:API_KEY|TOKEN|SECRET|PASSWORD|COOKIE))\s*=\s*"
        r"(?:['\"])?(?!\s*(?:#|$))[^\s'\"]+"
    ),
}

DEFAULT_QUERY = "knowledge workflow state review gate"
DEFAULT_CHUNK_SIZE = 800
DEFAULT_CHUNK_OVERLAP = 120
DEFAULT_VECTOR_TOP_K = 5
DEFAULT_LEXICAL_TOP_K = 5
DEFAULT_RERANK_TOP_K = 5
DEFAULT_EMBEDDING_MODEL = "disabled"


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def stable_hash(value: str, length: int = 14) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:length]


def load_corpus_manifest_paths() -> list[Path]:
    """Return the exact reviewed corpus; never expand a directory implicitly."""

    try:
        manifest = json.loads(CORPUS_MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"llamaindex_documents=fail:invalid_manifest:{error}") from error
    if manifest.get("schema_version") != "3.0":
        raise SystemExit("llamaindex_documents=fail:manifest_schema")
    entries = manifest.get("files")
    if not isinstance(entries, list) or not entries:
        raise SystemExit("llamaindex_documents=fail:manifest_files")

    paths: list[Path] = []
    seen: set[str] = set()
    for entry in entries:
        if not isinstance(entry, str) or not entry or entry.strip() != entry:
            raise SystemExit("llamaindex_documents=fail:invalid_manifest_path")
        relative = Path(entry)
        normalized = relative.as_posix()
        parts = {part.casefold() for part in relative.parts}
        if (
            relative.is_absolute()
            or ".." in relative.parts
            or "\\" in entry
            or normalized != entry
            or parts.intersection(BLOCKED_PATH_PARTS)
        ):
            raise SystemExit(f"llamaindex_documents=fail:unsafe_manifest_path:{entry}")
        if entry in seen:
            raise SystemExit(f"llamaindex_documents=fail:duplicate_manifest_path:{entry}")
        if relative.suffix.casefold() not in SUFFIXES:
            raise SystemExit(f"llamaindex_documents=fail:unsupported_manifest_path:{entry}")
        path = ROOT / relative
        if not path.is_file() or path.is_symlink():
            raise SystemExit(f"llamaindex_documents=fail:missing_manifest_path:{entry}")
        seen.add(entry)
        paths.append(path)
    return paths


def tokenize(text: str) -> list[str]:
    return [token.casefold() for token in re.findall(r"[A-Za-z][A-Za-z0-9_-]{2,}", text)]


def chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    if chunk_size < 200 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("chunk size must be >= 200 and overlap must be smaller")
    clean = text.strip()
    if not clean:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(clean):
        end = min(len(clean), start + chunk_size)
        if end < len(clean):
            boundary = max(clean.rfind("\n", start, end), clean.rfind(" ", start, end))
            if boundary > start + chunk_size // 2:
                end = boundary
        chunk = clean[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(clean):
            break
        start = max(start + 1, end - overlap)
    return chunks


def authority_metadata() -> dict[str, str | float]:
    """Every entry has already passed the same explicit manifest review gate."""

    return {
        "authority_state": "approved_manifest_current",
        "superseded_by": "",
        "authority_weight": 1.0,
    }


def load_documents(
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
) -> list[Document]:
    docs: list[Document] = []
    for path in load_corpus_manifest_paths():
        text = path.read_text(encoding="utf-8", errors="strict")
        source_path = rel(path)
        for category, pattern in BLOCKED_TEXT.items():
            if pattern.search(text):
                raise SystemExit(f"llamaindex_documents=fail:{category}:{source_path}")
        doc_id = f"doc_{stable_hash(source_path)}"
        for index, chunk in enumerate(chunk_text(text, chunk_size, chunk_overlap)):
            docs.append(
                Document(
                    text=chunk,
                    metadata={
                        "source_path": source_path,
                        "document_type": path.suffix.lstrip(".").casefold(),
                        "public_safety_status": "approved_manifest_file",
                        "updated_at": "not_serialized",
                        "doc_id": doc_id,
                        "chunk_id": f"{doc_id}_chunk_{index:04d}",
                        "chunk_index": index,
                        "chunk_hash": stable_hash(chunk, 20),
                        **authority_metadata(),
                    },
                )
            )
    return docs


def candidate(doc: Document, score: float, score_key: str) -> dict[str, Any]:
    metadata = dict(doc.metadata)
    return {
        "score": float(score),
        score_key: float(score),
        "source_path": metadata["source_path"],
        "document_type": metadata["document_type"],
        "updated_at": metadata["updated_at"],
        "doc_id": metadata["doc_id"],
        "chunk_id": metadata["chunk_id"],
        "chunk_index": metadata["chunk_index"],
        "chunk_hash": metadata["chunk_hash"],
        "authority_state": metadata["authority_state"],
        "superseded_by": metadata["superseded_by"],
        "authority_weight": float(metadata["authority_weight"]),
        "text_excerpt": re.sub(r"\s+", " ", doc.text).strip()[:240],
    }


def lexical_candidates(docs: list[Document], query: str, limit: int) -> list[dict[str, Any]]:
    if limit < 1:
        return []
    query_terms = Counter(tokenize(query))
    if not query_terms:
        return []
    scored: list[tuple[float, Document]] = []
    for doc in docs:
        tokens = tokenize(doc.text)
        if not tokens:
            continue
        counts = Counter(tokens)
        raw = sum(counts[term] * weight for term, weight in query_terms.items())
        if not raw:
            continue
        coverage = sum(1 for term in query_terms if counts[term]) / len(query_terms)
        phrase_boost = 1.25 if query.casefold() in doc.text.casefold() else 1.0
        score = (raw * (1.0 + coverage) * phrase_boost) / math.sqrt(len(tokens))
        scored.append((score, doc))
    scored.sort(
        key=lambda item: (
            -item[0],
            str(item[1].metadata["source_path"]),
            str(item[1].metadata["chunk_id"]),
        )
    )
    return [candidate(doc, score, "lexical_score") for score, doc in scored[:limit]]


def enforce_source_paths(results: list[dict[str, Any]]) -> None:
    allowed = {rel(path) for path in load_corpus_manifest_paths()}
    for item in results:
        source_path = str(item.get("source_path", ""))
        chunk_id = str(item.get("chunk_id", ""))
        if not source_path or not chunk_id:
            raise SystemExit("llamaindex_query=fail:missing_source_path_or_chunk_id")
        if source_path not in allowed:
            raise SystemExit("llamaindex_query=fail:source_outside_manifest")


def retrieve(
    docs: list[Document],
    query: str,
    mode: str = "lexical",
    vector_top_k: int = DEFAULT_VECTOR_TOP_K,
    lexical_top_k: int = DEFAULT_LEXICAL_TOP_K,
    rerank_top_k: int = DEFAULT_RERANK_TOP_K,
    embedding_model: str = DEFAULT_EMBEDDING_MODEL,
) -> dict[str, Any]:
    """Return deterministic lexical results for every provider-disabled mode."""

    del vector_top_k, embedding_model
    if mode not in {"hybrid", "lexical", "smoke"}:
        raise ValueError(f"unsupported retrieval mode: {mode}")
    lexical = lexical_candidates(docs, query, lexical_top_k)
    results = lexical[:rerank_top_k]
    enforce_source_paths(results)
    fallback = mode == "hybrid"
    return {
        "mode_used": "hybrid_provider_disabled_lexical" if fallback else mode,
        "vector_available": False,
        "vector_reason": "provider_execution_disabled" if fallback else "not_requested",
        "lexical_candidates": lexical,
        "semantic_candidates": [],
        "results": results,
    }


def build_summary(args: argparse.Namespace, docs: list[Document], retrieval: dict[str, Any]) -> dict[str, Any]:
    return {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "document_count": len({doc.metadata["doc_id"] for doc in docs}),
        "chunk_count": len(docs),
        "query": args.query,
        "requested_mode": args.mode,
        "mode_used": retrieval["mode_used"],
        "vector_available": False,
        "vector_reason": retrieval["vector_reason"],
        "provider_calls": 0,
        "external_writes": 0,
        "parameters": {
            "chunk_size": args.chunk_size,
            "chunk_overlap": args.chunk_overlap,
            "lexical_top_k": args.lexical_top_k,
            "rerank_top_k": args.rerank_top_k,
            "require_source_paths": True,
            "refuse_on_unlisted_source": True,
        },
        "results": retrieval["results"],
        "boundary": "exact reviewed public corpus manifest only",
        "corpus_manifest": rel(CORPUS_MANIFEST),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", default=DEFAULT_QUERY)
    parser.add_argument("--mode", choices=["hybrid", "lexical", "smoke"], default="lexical")
    parser.add_argument("--vector-top-k", type=int, default=DEFAULT_VECTOR_TOP_K)
    parser.add_argument("--lexical-top-k", type=int, default=DEFAULT_LEXICAL_TOP_K)
    parser.add_argument("--rerank-top-k", type=int, default=DEFAULT_RERANK_TOP_K)
    parser.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE)
    parser.add_argument("--chunk-overlap", type=int, default=DEFAULT_CHUNK_OVERLAP)
    parser.add_argument("--embedding-model", default=DEFAULT_EMBEDDING_MODEL)
    parser.add_argument(
        "--deep-import",
        action="store_true",
        help="Verify the optional LlamaIndex package import without changing retrieval or calling a provider.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.deep_import:
        if importlib.util.find_spec("llama_index.core") is None:
            raise SystemExit("llamaindex_index=fail:distribution_not_discoverable")
        import llama_index.core  # noqa: F401

        print("llamaindex_deep_import=ok")
    else:
        print("llamaindex_deep_import=not_requested")

    docs = load_documents(args.chunk_size, args.chunk_overlap)
    if not docs:
        raise SystemExit("llamaindex_index=fail:no_approved_documents")
    retrieval = retrieve(
        docs,
        args.query,
        args.mode,
        args.vector_top_k,
        args.lexical_top_k,
        args.rerank_top_k,
        args.embedding_model,
    )
    if not retrieval["results"]:
        raise SystemExit("llamaindex_query=fail:no_results")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    SUMMARY_FILE.write_text(
        json.dumps(build_summary(args, docs, retrieval), indent=2, ensure_ascii=True, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("llamaindex_documents=ok")
    print(f"document_count={len({doc.metadata['doc_id'] for doc in docs})}")
    print(f"chunk_count={len(docs)}")
    print("llamaindex_query=ok")
    print(f"mode_used={retrieval['mode_used']}")
    print("vector_available=false")
    print(f"vector_reason={retrieval['vector_reason']}")
    print("provider_calls=0")
    print("external_writes=0")
    for item in retrieval["results"]:
        print(
            "source={source_path} chunk={chunk_id} score={score}".format(
                source_path=item["source_path"],
                chunk_id=item["chunk_id"],
                score=round(float(item.get("score", 0.0)), 6),
            )
        )
    print("persisted=project/local/rag_index/approved-corpus-summary.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
