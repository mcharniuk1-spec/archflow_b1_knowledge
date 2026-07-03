#!/usr/bin/env python3
"""Benchmark bounded approved-corpus retrieval over fixed public queries."""

from __future__ import annotations

import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
OUTPUT_DIR = PROJECT / "local" / "rag_index"
REPORT_JSON = OUTPUT_DIR / "approved-corpus-benchmark.json"
REPORT_MD = OUTPUT_DIR / "approved-corpus-benchmark.md"
RETRIEVER_PATH = PROJECT / "scripts" / "llamaindex-approved-corpus.py"


QUERIES = [
    ("public safety local paths credentials", ["project/operating-rules.md", "README.md", "wiki/rules/public-wikillm-contract.md", "project/reports/2026-06-25-layer-setup-report.md", "wiki/index.md"]),
    ("LangGraph path state review gate", ["project/workflows/langgraph-controller.yaml", "project/agentic-stack.md"]),
    ("CrewAI AF Review AF Manager roles", ["project/workflows/crewai-crew.yaml", "project/agentic-stack.md", "project/runs/E1.2/2026-06-26-full-test/responsibility-matrix.md", "project/runs/E1.2/2026-06-26-full-test/E1.2_Streaming_report.md"]),
    ("LlamaIndex approved corpus source paths", ["project/workflows/llamaindex-rag.yaml", "project/runs/E1.2/2026-06-26-full-test/retrieval-log.md", "project/runs/E1.3/2026-06-30-kb-readback/source-registry.md", "project/agentic-stack.md"]),
    ("turbovec stable source ids metadata benchmark", ["project/workflows/llamaindex-rag.yaml", "project/workflows/knowledge-integration.yaml", "wiki/memory.md", "project/agentic-stack.md", "project/runs/E1.3/2026-06-30-kb-readback/source-registry.md"]),
    ("Graphify generated structure map", ["project/workflows/knowledge-integration.yaml", "project/README.md", "wiki/memory.md", "project/reports/2026-06-25-dashboard-setup-and-operation-report.md", "project/runs/E1.2/2026-06-26-full-test/E1.2_System_report.md"]),
    ("WikiLLM memory decisions issues insights runs", ["wiki/index.md", "wiki/memory.md", "project/workflows/knowledge-integration.yaml"]),
    ("Jarvis dashboard API provider disabled review packet", ["project/README.md", "project/agentic-stack.md", "wiki/memory.md", "wiki/log.md", "project/runs/2026-07-03-vercel-jarvis-connection/agent-handout.md", "project/live/communication/agent-communication-log.md"]),
    ("OpenRouter budget guard provider approval", ["project/config/model-routing.yaml", "project/agentic-stack.md", "wiki/log.md", "project/runs/yushchenko-model-efficiency/2026-07-02-1402-model-efficiency-report.md", "project/reports/2026-07-02-dashboard-execution-architecture.md"]),
    ("E1.2 proof PRD streaming report system report", ["project/README.md", "wiki/log.md", "wiki/memory.md", "project/project-plan.md", "project/runs/2026-07-02-e1-2-testmeeting-dashboard-architecture/notion-update-packet.md", "project/runs/E1.2/2026-06-26-notion-sync/next-steps-e1-2.md"]),
    ("E1.3 readback KB proof dashboard voice gate", ["wiki/memory.md", "wiki/log.md", "project/runs/E1.3/2026-06-30-kb-readback/agent-handout.md"]),
    ("market research engine evidence ICP source grades", ["project/workflows/market-research-engine.yaml", "project/project-plan.md"]),
    ("Loop Engineering max revision loops attempts report only", ["project/loops/LOOP.md", "project/agentic-stack.md"]),
    ("task handout hook public safe agent handout", ["skills/task-handout/SKILL.md", "project/operating-rules.md"]),
    ("live agent communication claims complete handoff", ["project/live/communication/README.md", "project/operating-rules.md"]),
    ("provider setup Ollama Qwythos gemma fallback", ["project/provider-setup.md", "project/README.md"]),
    ("LangSmith tracing observability key present local ignored", ["project/langsmith-setup.md", "project/README.md", "project/workflows/knowledge-integration.yaml"]),
    ("Cognee operational recall deferred until readback", ["project/workflows/knowledge-integration.yaml", "project/agentic-stack.md"]),
    ("static Vercel dashboard Railway always on backend gated", ["project/README.md", "wiki/log.md", "wiki/memory.md", "project/runs/E1.5/2026-06-30-dashboard-jarvis-vercel/agent-handout.md", "project/runs/2026-07-03-vercel-jarvis-connection/agent-handout.md"]),
    ("PRD ICP service output Architecture 1 agent control Architecture 2", ["project/agentic-stack.md", "project/runs/2026-07-02-e1-2-testmeeting-dashboard-architecture/agent-handout.md", "project/runs/E1.2/2026-07-02-testmeeting-local/E1.2.8_Local_Streaming_report.md"]),
]


def load_retriever() -> Any:
    spec = importlib.util.spec_from_file_location("archflow_llamaindex_retriever", RETRIEVER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("retriever_import_failed")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def source_hit(results: list[dict[str, Any]], expected_sources: list[str]) -> bool:
    returned = {str(item.get("source_path", "")) for item in results}
    return any(expected in returned for expected in expected_sources)


def validate_source_paths(results: list[dict[str, Any]]) -> bool:
    for item in results:
        source_path = str(item.get("source_path", ""))
        chunk_id = str(item.get("chunk_id", ""))
        if not source_path or not chunk_id:
            return False
        if source_path.startswith("/") or source_path.startswith("..") or "/.." in source_path:
            return False
    return True


def main() -> int:
    retriever = load_retriever()
    docs = retriever.load_documents()
    if not docs:
        raise SystemExit("rag_benchmark=fail:no_documents")

    rows: list[dict[str, Any]] = []
    lexical_hits = 0
    hybrid_hits = 0
    source_path_pass = True
    vector_available = False
    vector_reasons: set[str] = set()

    for query, expected_sources in QUERIES:
        lexical = retriever.retrieve(docs, query, mode="lexical", lexical_top_k=5, rerank_top_k=5)
        hybrid = retriever.retrieve(docs, query, mode="hybrid", vector_top_k=5, lexical_top_k=5, rerank_top_k=5)
        lexical_hit = source_hit(lexical["results"], expected_sources)
        hybrid_hit = source_hit(hybrid["results"], expected_sources)
        lexical_hits += int(lexical_hit)
        hybrid_hits += int(hybrid_hit)
        source_path_pass = source_path_pass and validate_source_paths(lexical["results"]) and validate_source_paths(hybrid["results"])
        vector_available = vector_available or bool(hybrid.get("vector_available"))
        vector_reasons.add(str(hybrid.get("vector_reason", "unknown")))
        rows.append(
            {
                "query": query,
                "expected_sources": expected_sources,
                "lexical_hit": lexical_hit,
                "hybrid_hit": hybrid_hit,
                "hybrid_mode_used": hybrid.get("mode_used"),
                "vector_available": hybrid.get("vector_available"),
                "vector_reason": hybrid.get("vector_reason"),
                "lexical_sources": [item["source_path"] for item in lexical["results"]],
                "hybrid_sources": [item["source_path"] for item in hybrid["results"]],
            }
        )

    total = len(QUERIES)
    lexical_recall = lexical_hits / total
    hybrid_recall = hybrid_hits / total
    no_regression = hybrid_hits >= lexical_hits
    benchmark_pass = source_path_pass and no_regression and hybrid_recall >= 0.70
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "pass" if benchmark_pass else "fail",
        "query_count": total,
        "recall_at_5": {
            "lexical": round(lexical_recall, 4),
            "hybrid": round(hybrid_recall, 4),
        },
        "hits": {
            "lexical": lexical_hits,
            "hybrid": hybrid_hits,
        },
        "source_path_filtering_pass": source_path_pass,
        "no_hybrid_regression": no_regression,
        "vector_available": vector_available,
        "vector_reasons": sorted(vector_reasons),
        "full_vector_default_gate": "blocked_until_vector_available_and_benchmark_passes"
        if not vector_available
        else "benchmark_passed_for_current_local_vector_state",
        "rows": rows,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    REPORT_MD.write_text(
        "\n".join(
            [
                "# Approved Corpus Retrieval Benchmark",
                "",
                f"Status: {payload['status']}",
                f"Queries: {total}",
                f"Lexical recall@5: {lexical_hits}/{total} ({lexical_recall:.2f})",
                f"Hybrid recall@5: {hybrid_hits}/{total} ({hybrid_recall:.2f})",
                f"Vector available: {str(vector_available).lower()}",
                f"Vector reasons: {', '.join(sorted(vector_reasons))}",
                f"Source-path filtering: {'pass' if source_path_pass else 'fail'}",
                f"Regression check: {'pass' if no_regression else 'fail'}",
                "",
            ]
        ),
        encoding="utf-8",
    )

    status = "pass" if benchmark_pass else "fail"
    print(f"rag_benchmark={status}")
    print(f"queries={total}")
    print(f"lexical_recall_at_5={lexical_hits}/{total}")
    print(f"hybrid_recall_at_5={hybrid_hits}/{total}")
    print(f"source_path_filtering={'pass' if source_path_pass else 'fail'}")
    print(f"hybrid_regression={'pass' if no_regression else 'fail'}")
    print(f"vector_available={str(vector_available).lower()}")
    print(f"vector_reasons={','.join(sorted(vector_reasons))}")
    print("report=project/local/rag_index/approved-corpus-benchmark.json")
    return 0 if benchmark_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
