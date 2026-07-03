#!/usr/bin/env python3
"""Build a bounded hybrid retrieval proof over approved public files.

The proof keeps the existing public corpus boundary intact. It loads only
approved Markdown/YAML files, attaches stable source and chunk metadata, runs a
deterministic lexical path, and optionally adds local Ollama embeddings when the
configured embedder is already available. If vectors are unavailable, the smoke
path falls back to lexical retrieval and reports the reason.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from llama_index.core import Document


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
OUTPUT_DIR = PROJECT / "local" / "rag_index"
SUMMARY_FILE = OUTPUT_DIR / "approved-corpus-summary.json"
EMBEDDING_CACHE_FILE = OUTPUT_DIR / "approved-corpus-embeddings.json"

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

DEFAULT_QUERY = "dialogue PRD knowledge base LangGraph review gate"
DEFAULT_CHUNK_SIZE = 800
DEFAULT_CHUNK_OVERLAP = 120
DEFAULT_VECTOR_TOP_K = 5
DEFAULT_LEXICAL_TOP_K = 5
DEFAULT_RERANK_TOP_K = 5
DEFAULT_EMBEDDING_MODEL = "nomic-embed-text"
DEFAULT_OLLAMA_BASE_URL = "http://127.0.0.1:11434"
VECTOR_SCAN_LIMIT = int(os.getenv("ARCHFLOW_RAG_VECTOR_SCAN_LIMIT", "220"))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def stable_hash(value: str, length: int = 14) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:length]


def approved_file(path: Path) -> bool:
    if not path.is_file() or path.suffix not in SUFFIXES:
        return False
    parts = set(path.relative_to(ROOT).parts)
    return not parts.intersection(EXCLUDE_PARTS) and not path.name.startswith(".env")


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in re.findall(r"[A-Za-z][A-Za-z0-9_-]{2,}", text)]


def chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    clean = text.strip()
    if not clean:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(clean):
        end = min(len(clean), start + chunk_size)
        if end < len(clean):
            newline = clean.rfind("\n", start, end)
            space = clean.rfind(" ", start, end)
            boundary = max(newline, space)
            if boundary > start + chunk_size // 2:
                end = boundary
        chunk = clean[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(clean):
            break
        start = max(start + 1, end - overlap)
    return chunks


def load_documents(chunk_size: int = DEFAULT_CHUNK_SIZE, chunk_overlap: int = DEFAULT_CHUNK_OVERLAP) -> list[Document]:
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
            source_path = rel(path)
            doc_id = f"doc_{stable_hash(source_path)}"
            updated_at = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()
            for index, chunk in enumerate(chunk_text(text, chunk_size, chunk_overlap)):
                chunk_id = f"{doc_id}_chunk_{index:04d}"
                docs.append(
                    Document(
                        text=chunk,
                        metadata={
                            "source_path": source_path,
                            "document_type": path.suffix.lstrip("."),
                            "public_safety_status": "approved_public_file",
                            "updated_at": updated_at,
                            "doc_id": doc_id,
                            "chunk_id": chunk_id,
                            "chunk_index": index,
                            "chunk_hash": stable_hash(chunk, 20),
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
        "text_excerpt": re.sub(r"\s+", " ", doc.text).strip()[:240],
    }


def lexical_candidates(docs: list[Document], query: str, limit: int) -> list[dict[str, Any]]:
    query_terms = Counter(tokenize(query))
    scored: list[tuple[float, Document]] = []
    if not query_terms:
        return []
    for doc in docs:
        tokens = tokenize(doc.text)
        if not tokens:
            continue
        counts = Counter(tokens)
        raw = sum(counts[term] * weight for term, weight in query_terms.items())
        if not raw:
            continue
        coverage = sum(1 for term in query_terms if counts[term]) / max(len(query_terms), 1)
        phrase_boost = 1.25 if query.lower() in doc.text.lower() else 1.0
        score = (raw * (1.0 + coverage) * phrase_boost) / math.sqrt(len(tokens))
        scored.append((score, doc))
    scored.sort(key=lambda item: (-item[0], str(item[1].metadata.get("source_path", "")), str(item[1].metadata.get("chunk_id", ""))))
    return [candidate(doc, score, "lexical_score") for score, doc in scored[:limit]]


def load_embedding_cache() -> dict[str, Any]:
    if not EMBEDDING_CACHE_FILE.exists():
        return {}
    try:
        return json.loads(EMBEDDING_CACHE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_embedding_cache(cache: dict[str, Any]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    EMBEDDING_CACHE_FILE.write_text(json.dumps(cache, indent=2, sort_keys=True), encoding="utf-8")


def ollama_json(path: str, payload: dict[str, Any] | None = None, timeout: float = 2.0) -> dict[str, Any]:
    base_url = os.getenv("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL).rstrip("/")
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        f"{base_url}{path}",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST" if payload is not None else "GET",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def ollama_model_available(model_name: str) -> tuple[bool, str]:
    try:
        payload = ollama_json("/api/tags", timeout=1.2)
    except (OSError, urllib.error.URLError, TimeoutError) as exc:
        return False, f"ollama_unavailable:{exc.__class__.__name__}"
    names = {item.get("name", "").split(":", 1)[0] for item in payload.get("models", [])}
    names.update(item.get("name", "") for item in payload.get("models", []))
    if model_name in names:
        return True, "ollama_model_available"
    return False, f"embedding_model_missing:{model_name}"


def ollama_embedding(model_name: str, text: str) -> list[float]:
    payload = ollama_json(
        "/api/embeddings",
        {"model": model_name, "prompt": text[:8000]},
        timeout=float(os.getenv("ARCHFLOW_RAG_EMBED_TIMEOUT", "10")),
    )
    embedding = payload.get("embedding")
    if not isinstance(embedding, list) or not embedding:
        raise RuntimeError("ollama_embedding_empty")
    return [float(value) for value in embedding]


def cosine(left: list[float], right: list[float]) -> float:
    if not left or not right or len(left) != len(right):
        return 0.0
    numerator = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(a * a for a in left))
    right_norm = math.sqrt(sum(b * b for b in right))
    if not left_norm or not right_norm:
        return 0.0
    return numerator / (left_norm * right_norm)


def vector_candidates(docs: list[Document], query: str, limit: int, model_name: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if os.getenv("ARCHFLOW_RAG_DISABLE_VECTOR", "").lower() in {"1", "true", "yes"}:
        return [], {"vector_available": False, "reason": "disabled_by_env"}
    available, reason = ollama_model_available(model_name)
    if not available:
        return [], {"vector_available": False, "reason": reason}
    if len(docs) > VECTOR_SCAN_LIMIT:
        return [], {
            "vector_available": False,
            "reason": f"corpus_chunk_count_{len(docs)}_exceeds_scan_limit_{VECTOR_SCAN_LIMIT}",
        }

    cache = load_embedding_cache()
    cache_model = cache.get("model_name")
    if cache_model != model_name:
        cache = {"model_name": model_name, "embeddings": {}}
    embeddings: dict[str, list[float]] = cache.setdefault("embeddings", {})
    try:
        query_embedding = ollama_embedding(model_name, query)
        scored: list[tuple[float, Document]] = []
        for doc in docs:
            key = f"{doc.metadata['chunk_id']}:{doc.metadata['chunk_hash']}"
            vector = embeddings.get(key)
            if vector is None:
                vector = ollama_embedding(model_name, doc.text)
                embeddings[key] = vector
            scored.append((cosine(query_embedding, vector), doc))
        save_embedding_cache(cache)
    except (OSError, urllib.error.URLError, TimeoutError, RuntimeError, ValueError) as exc:
        return [], {"vector_available": False, "reason": f"embedding_failed:{exc.__class__.__name__}"}

    scored.sort(key=lambda item: (-item[0], str(item[1].metadata.get("source_path", "")), str(item[1].metadata.get("chunk_id", ""))))
    return [candidate(doc, score, "semantic_score") for score, doc in scored[:limit]], {
        "vector_available": True,
        "reason": "ollama_embeddings",
        "embedding_model": model_name,
    }


def normalize_scores(items: list[dict[str, Any]], key: str) -> dict[tuple[str, str], float]:
    if not items:
        return {}
    values = [max(float(item.get(key, 0.0)), 0.0) for item in items]
    max_value = max(values) if values else 0.0
    if max_value <= 0:
        return {(str(item["source_path"]), str(item["chunk_id"])): 0.0 for item in items}
    return {
        (str(item["source_path"]), str(item["chunk_id"])): max(float(item.get(key, 0.0)), 0.0) / max_value
        for item in items
    }


def merge_candidates(
    lexical: list[dict[str, Any]],
    semantic: list[dict[str, Any]],
    limit: int,
) -> list[dict[str, Any]]:
    merged: dict[tuple[str, str], dict[str, Any]] = {}
    lexical_norm = normalize_scores(lexical, "lexical_score")
    semantic_norm = normalize_scores(semantic, "semantic_score")
    for item in lexical + semantic:
        key = (str(item["source_path"]), str(item["chunk_id"]))
        merged.setdefault(key, {**item, "lexical_score": 0.0, "semantic_score": 0.0})
        merged[key].update({field: item[field] for field in item if field not in {"score"}})
    for key, item in merged.items():
        lex = lexical_norm.get(key, 0.0)
        sem = semantic_norm.get(key, 0.0)
        item["lexical_score_normalized"] = round(lex, 6)
        item["semantic_score_normalized"] = round(sem, 6)
        item["score"] = round((0.42 * lex) + (0.58 * sem), 6)
    return sorted(merged.values(), key=lambda item: (-float(item["score"]), str(item["source_path"]), str(item["chunk_id"])))[:limit]


def enforce_source_paths(results: list[dict[str, Any]]) -> None:
    for item in results:
        source_path = str(item.get("source_path", ""))
        chunk_id = str(item.get("chunk_id", ""))
        if not source_path or not chunk_id:
            raise SystemExit("llamaindex_query=fail:missing_source_path_or_chunk_id")
        if source_path.startswith("/") or "/.." in source_path or source_path.startswith(".."):
            raise SystemExit("llamaindex_query=fail:invalid_source_path")


def retrieve(
    docs: list[Document],
    query: str,
    mode: str = "hybrid",
    vector_top_k: int = DEFAULT_VECTOR_TOP_K,
    lexical_top_k: int = DEFAULT_LEXICAL_TOP_K,
    rerank_top_k: int = DEFAULT_RERANK_TOP_K,
    embedding_model: str = DEFAULT_EMBEDDING_MODEL,
) -> dict[str, Any]:
    lexical = lexical_candidates(docs, query, lexical_top_k)
    if mode in {"lexical", "smoke"}:
        results = lexical[:rerank_top_k]
        enforce_source_paths(results)
        return {
            "mode_used": mode,
            "vector_available": False,
            "vector_reason": "not_requested",
            "lexical_candidates": lexical,
            "semantic_candidates": [],
            "results": results,
        }

    semantic, vector_state = vector_candidates(docs, query, vector_top_k, embedding_model)
    if not vector_state.get("vector_available"):
        results = lexical[:rerank_top_k]
        enforce_source_paths(results)
        return {
            "mode_used": "hybrid_fallback_lexical",
            "vector_available": False,
            "vector_reason": vector_state.get("reason", "unknown"),
            "lexical_candidates": lexical,
            "semantic_candidates": [],
            "results": results,
        }

    results = merge_candidates(lexical, semantic, rerank_top_k)
    enforce_source_paths(results)
    return {
        "mode_used": "hybrid",
        "vector_available": True,
        "vector_reason": vector_state.get("reason", "available"),
        "embedding_model": vector_state.get("embedding_model", embedding_model),
        "lexical_candidates": lexical,
        "semantic_candidates": semantic,
        "results": results,
    }


def build_summary(args: argparse.Namespace, docs: list[Document], retrieval: dict[str, Any]) -> dict[str, Any]:
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "document_count": len({doc.metadata["doc_id"] for doc in docs}),
        "chunk_count": len(docs),
        "query": args.query,
        "requested_mode": args.mode,
        "mode_used": retrieval["mode_used"],
        "vector_available": retrieval["vector_available"],
        "vector_reason": retrieval["vector_reason"],
        "embedding_model": retrieval.get("embedding_model", args.embedding_model),
        "parameters": {
            "chunk_size": args.chunk_size,
            "chunk_overlap": args.chunk_overlap,
            "vector_top_k": args.vector_top_k,
            "lexical_top_k": args.lexical_top_k,
            "rerank_top_k": args.rerank_top_k,
            "fallback_to_lexical": True,
            "require_source_paths": True,
            "refuse_on_private_source": True,
        },
        "results": retrieval["results"],
        "boundary": "approved public files only",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run bounded approved-corpus LlamaIndex retrieval.")
    parser.add_argument("--query", default=DEFAULT_QUERY)
    parser.add_argument("--mode", choices=["hybrid", "lexical", "smoke"], default=os.getenv("ARCHFLOW_RAG_MODE", "hybrid"))
    parser.add_argument("--vector-top-k", type=int, default=DEFAULT_VECTOR_TOP_K)
    parser.add_argument("--lexical-top-k", type=int, default=DEFAULT_LEXICAL_TOP_K)
    parser.add_argument("--rerank-top-k", type=int, default=DEFAULT_RERANK_TOP_K)
    parser.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE)
    parser.add_argument("--chunk-overlap", type=int, default=DEFAULT_CHUNK_OVERLAP)
    parser.add_argument("--embedding-model", default=os.getenv("ARCHFLOW_RAG_EMBEDDING_MODEL", DEFAULT_EMBEDDING_MODEL))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
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
    SUMMARY_FILE.write_text(json.dumps(build_summary(args, docs, retrieval), indent=2), encoding="utf-8")

    print("llamaindex_documents=ok")
    print(f"document_count={len({doc.metadata['doc_id'] for doc in docs})}")
    print(f"chunk_count={len(docs)}")
    print("llamaindex_query=ok")
    print(f"mode_used={retrieval['mode_used']}")
    print(f"vector_available={str(retrieval['vector_available']).lower()}")
    print(f"vector_reason={retrieval['vector_reason']}")
    for item in retrieval["results"]:
        print(
            "source={source_path} chunk={chunk_id} score={score} lexical={lexical} semantic={semantic}".format(
                source_path=item["source_path"],
                chunk_id=item["chunk_id"],
                score=round(float(item.get("score", 0.0)), 6),
                lexical=round(float(item.get("lexical_score", 0.0)), 6),
                semantic=round(float(item.get("semantic_score", 0.0)), 6),
            )
        )
    print("persisted=project/local/rag_index/approved-corpus-summary.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
