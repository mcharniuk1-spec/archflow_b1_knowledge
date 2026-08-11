#!/usr/bin/env python3
"""Run small provider-disabled measurements for the generic public core."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
FIXTURE_PATH = PROJECT / "benchmarks" / "actionable-agents-v3-fixtures.json"
OUTPUT_PATH = PROJECT / "benchmarks" / "actionable-agents-v3-results.json"
RETRIEVAL_PATH = PROJECT / "scripts" / "llamaindex-approved-corpus.py"
ROLE_CATALOG_PATH = PROJECT / "database" / "role-catalog.json"
ROLE_PACKS_PATH = PROJECT / "agents" / "actionable-role-packs.json"


def read_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError(f"expected object: {path.relative_to(ROOT)}")
    return value


def import_retrieval():
    spec = importlib.util.spec_from_file_location("archflow_benchmark_retrieval", RETRIEVAL_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("retrieval module unavailable")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def percent_reduction(baseline: int, candidate: int) -> float:
    if baseline <= 0 or candidate < 0 or candidate > baseline:
        raise RuntimeError("invalid reduction denominator")
    return (baseline - candidate) / baseline


def semantic_gate(packet: dict) -> str:
    objective = str(packet.get("objective", "")).strip()
    output = str(packet.get("requested_output", "")).strip()
    reviewer = str(packet.get("reviewer", "")).strip()
    maker = str(packet.get("maker", "")).strip()
    text_parts = [str(packet.get(key, "")) for key in ("public_reference", "allowed_evidence")]
    email_parts = packet.get("synthetic_email_parts")
    if isinstance(email_parts, list) and len(email_parts) == 2:
        text_parts.append(f"{email_parts[0]}@{email_parts[1]}")
    secret_parts = packet.get("synthetic_secret_parts")
    if isinstance(secret_parts, list) and len(secret_parts) == 3:
        text_parts.append(f"{secret_parts[0]}_{secret_parts[1]}={secret_parts[2]}")
    text = "\n".join(text_parts)
    unsafe = re.search(r"@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|\b(?:api[_-]?key|token|secret|password)\s*[=:]", text, re.IGNORECASE)
    if not objective or not output or not reviewer or unsafe:
        return "reject"
    if maker and maker.casefold() == reviewer.casefold():
        return "reject"
    if packet.get("external_action") is True and packet.get("external_approval") is not True:
        return "reject"
    return "accept"


def run_retrieval(fixtures: list[dict]) -> tuple[dict, int, int]:
    retrieval = import_retrieval()
    documents = retrieval.load_documents(chunk_size=800, chunk_overlap=120)
    by_chunk = {document.metadata["chunk_id"]: document for document in documents}
    manifest_paths = retrieval.load_corpus_manifest_paths()
    baseline_per_task = sum(path.stat().st_size for path in manifest_paths)
    results = []
    candidate_total = 0
    for fixture in fixtures:
        candidates = retrieval.lexical_candidates(documents, fixture["query"], 5)
        candidate_bytes = sum(len(by_chunk[item["chunk_id"]].text.encode("utf-8")) for item in candidates)
        candidate_total += candidate_bytes
        sources = [item["source_path"] for item in candidates]
        results.append(
            {
                "id": fixture["id"],
                "expected_source": fixture["expected_source"],
                "expected_source_hit_at_5": fixture["expected_source"] in sources,
                "candidate_bytes": candidate_bytes,
                "baseline_bytes": baseline_per_task,
                "source_paths": sources,
            }
        )
    baseline_total = baseline_per_task * len(fixtures)
    hits = sum(item["expected_source_hit_at_5"] for item in results)
    return {"fixture_count": len(results), "hits_at_5": hits, "results": results}, baseline_total, candidate_total


def run_role_activation(pack_ids: list[str]) -> tuple[dict, int, int]:
    role_count = len(read_object(ROLE_CATALOG_PATH).get("roles", []))
    packs = {item["id"]: item for item in read_object(ROLE_PACKS_PATH).get("packs", [])}
    results = []
    candidate_total = 0
    for pack_id in pack_ids:
        if pack_id not in packs:
            raise RuntimeError(f"unknown role pack: {pack_id}")
        count = len(set(packs[pack_id].get("role_ids", [])))
        candidate_total += count
        results.append({"pack_id": pack_id, "candidate_role_slots": count, "baseline_role_slots": role_count})
    return {"fixture_count": len(results), "role_catalog_count": role_count, "results": results}, role_count * len(results), candidate_total


def run_semantic_gates(fixtures: list[dict]) -> dict:
    results = []
    for fixture in fixtures:
        observed = semantic_gate(fixture.get("packet", {}))
        results.append({"id": fixture["id"], "expected": fixture["expected"], "observed": observed, "pass": observed == fixture["expected"]})
    return {"fixture_count": len(results), "passed": sum(item["pass"] for item in results), "results": results}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    parser.add_argument("--measured-at", default="")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Recompute with the committed timestamp and fail on any result drift without rewriting the file.",
    )
    args = parser.parse_args()
    expected = read_object(args.output) if args.check else None
    fixtures = read_object(FIXTURE_PATH)
    retrieval, context_baseline, context_candidate = run_retrieval(fixtures.get("retrieval", []))
    activation, role_baseline, role_candidate = run_role_activation(fixtures.get("role_activation", []))
    gates = run_semantic_gates(fixtures.get("semantic_gates", []))
    context_reduction = percent_reduction(context_baseline, context_candidate)
    role_reduction = percent_reduction(role_baseline, role_candidate)
    status = "pass" if retrieval["hits_at_5"] == retrieval["fixture_count"] and gates["passed"] == gates["fixture_count"] and context_reduction >= 0.8 and role_reduction >= 0.7 else "fail"
    measured_at = (
        str(expected.get("measured_at", ""))
        if expected is not None
        else args.measured_at or datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    )
    if not measured_at:
        raise RuntimeError("committed benchmark has no measured_at value")
    payload = {
        "schema_version": "3.0",
        "fixture_id": fixtures.get("fixture_id"),
        "fixture_sha256": sha256(FIXTURE_PATH),
        "measured_at": measured_at,
        "status": status,
        "provider_calls": 0,
        "external_writes": 0,
        "context_input": {"baseline_bytes": context_baseline, "candidate_bytes": context_candidate, "reduction": context_reduction, **retrieval},
        "role_activation": {"baseline_role_slots": role_baseline, "candidate_role_slots": role_candidate, "reduction": role_reduction, **activation},
        "semantic_gates": gates,
        "publication_metrics": [
            {
                "label": "Context input",
                "value": f"{context_reduction * 100:.1f}% lower",
                "comparator": f"Top-five lexical context chunks versus all {retrieval['fixture_count']} full-manifest packets; {context_candidate:,} vs {context_baseline:,} UTF-8 bytes.",
                "limitation": "Input-byte measurement on fixed synthetic tasks; not model-exact tokens, billed tokens, durable-memory size, latency, or answer quality.",
            },
            {
                "label": "Role activation",
                "value": f"{role_reduction * 100:.1f}% fewer",
                "comparator": f"Smallest declared role packs versus all-role fan-out; {role_candidate} vs {role_baseline} role slots across {activation['fixture_count']} tasks.",
                "limitation": "Contract selection measurement; not wall-clock speed, labor savings, or production throughput.",
            },
            {
                "label": "Source recall",
                "value": f"{retrieval['hits_at_5']}/{retrieval['fixture_count']}",
                "comparator": "Expected canonical source present in the deterministic lexical top five for each fixed query.",
                "limitation": "Source-hit fixture only; not semantic answer accuracy or representative production recall.",
            },
            {
                "label": "Semantic gates",
                "value": f"{gates['passed']}/{gates['fixture_count']}",
                "comparator": "Expected accept/reject decision for one valid and seven unsafe or incomplete packets.",
                "limitation": "Bounded abuse fixtures; not a real-world safety rate or proof against unknown attacks.",
            },
        ],
        "limitations": [
            "No provider was called and no external system was written.",
            "The context comparator deliberately uses a full-manifest packet and is not a claim about a prior release.",
            "All percentages are fixture-specific and must be rerun when the manifest, roles, fixtures, or selection logic changes.",
        ],
    }
    if expected is not None:
        if expected != payload:
            print("actionable_agents_benchmark=fail:committed_result_drift")
            return 1
    else:
        args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=True, sort_keys=True) + "\n", encoding="utf-8")
    print(f"actionable_agents_benchmark={status}")
    print(f"context_input_reduction={context_reduction * 100:.1f}%")
    print(f"role_activation_reduction={role_reduction * 100:.1f}%")
    print(f"source_recall={retrieval['hits_at_5']}/{retrieval['fixture_count']}")
    print(f"semantic_gates={gates['passed']}/{gates['fixture_count']}")
    print("provider_calls=0")
    print("external_writes=0")
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
