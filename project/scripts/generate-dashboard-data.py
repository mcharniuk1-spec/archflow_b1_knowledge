#!/usr/bin/env python3
"""Generate the compact, public-safe Crew Desk snapshot.

The dashboard reads canonical JSON contracts directly. This snapshot supplies
only repository status, counts, public source links, and calibrated gaps.
It never reads private folders, environment files, credentials, or raw vaults.
"""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
CONTRACTS = PROJECT / "system" / "contracts"
OUTPUT = PROJECT / "dashboard" / "data.json"


def load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain an object")
    return value


def git_value(*args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return completed.stdout.strip() if completed.returncode == 0 else "unavailable"


def main() -> int:
    crew = load(CONTRACTS / "knowledge-crew-config.json")
    roles = load(CONTRACTS / "role-catalog.json")
    workflows = load(CONTRACTS / "role-workflows.json")
    controller = load(CONTRACTS / "operating-model.json")
    turbovec = crew["frameworks"]["turbovec"]

    data = {
        "schema_version": "2.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_commit": git_value("rev-parse", "--short=12", "HEAD"),
        "project": {
            "name": "ArchFlow Responsive Knowledge Crew",
            "goal": crew["product_goal"],
            "status": crew["status"],
            "controller": controller["authority"],
            "dashboard": "primary_non_technical_browser_local_projection",
        },
        "truth_state": {
            "provider_runtime": "disabled",
            "writeback": "disabled",
            "external_actions": "disabled_until_exact_owner_approval",
            "public_checkpointer": crew["frameworks"]["langgraph"]["checkpointer"]["public_demo"],
            "turbovec": turbovec["current_evidence"]["verdict"],
            "obsidian": "optional_local_human_workspace",
            "orbit": "optional_private_local_structural_adapter",
        },
        "counts": {
            "layers": len(crew["layers"]),
            "roles": len(roles["roles"]),
            "workflow_packs": len(workflows["packs"]),
            "research_methods": len(crew["research_methods"]),
            "context_token_ceiling": crew["perception_capsule"]["maximum_tokens"],
        },
        "layers": [
            {
                "id": layer["id"],
                "name": layer["name"],
                "outputs": layer["outputs"],
            }
            for layer in crew["layers"]
        ],
        "roles": [
            {
                "id": role["id"],
                "call_name": role["call_name"],
                "title": role["title"],
                "owns": role["owns"],
            }
            for role in roles["roles"]
        ],
        "workflow_packs": [
            {
                "id": pack["id"],
                "label": pack["label"],
                "roles": pack["roles"],
                "outputs": pack["outputs"],
            }
            for pack in workflows["packs"]
        ],
        "retrieval_baseline": {
            "chunk_size": crew["frameworks"]["llamaindex"]["ingestion"]["chunk_size"],
            "chunk_overlap": crew["frameworks"]["llamaindex"]["ingestion"]["chunk_overlap"],
            **crew["frameworks"]["llamaindex"]["retrieval"],
        },
        "turbovec_evidence": {
            "version": turbovec["version_evidence"],
            "bit_width": turbovec["bit_width"],
            "public_receipt": turbovec["current_evidence"]["public_receipt"],
            "queries": turbovec["current_evidence"]["queries"],
            "checks": turbovec["current_evidence"]["checks"],
            "candidate_recall_at_3": turbovec["current_evidence"]["candidate_recall_at_3"],
            "candidate_mrr": turbovec["current_evidence"]["candidate_mrr"],
            "lexical_baseline": turbovec["current_evidence"]["lexical_baseline"],
            "verdict": turbovec["current_evidence"]["verdict"],
            "promotion_gate": turbovec["promotion_gate"],
        },
        "public_sources": [
            {
                "name": "LangGraph persistence",
                "url": "https://docs.langchain.com/oss/python/langgraph/persistence",
            },
            {
                "name": "LangGraph interrupts",
                "url": "https://docs.langchain.com/oss/python/langgraph/interrupts",
            },
            {
                "name": "LlamaIndex ingestion pipeline",
                "url": "https://docs.llamaindex.ai/en/v0.10.17/module_guides/loading/ingestion_pipeline/root.html",
            },
            {
                "name": "LlamaIndex documents and nodes",
                "url": "https://docs.llamaindex.ai/en/v0.10.19/module_guides/loading/documents_and_nodes/root.html",
            },
            {
                "name": "CrewAI documentation",
                "url": "https://docs.crewai.com/",
            },
            {
                "name": "Obsidian plugin security",
                "url": "https://obsidian.md/help/plugin-security",
            },
            {
                "name": "TurboVec repository",
                "url": "https://github.com/RyanCodrai/turbovec",
            },
        ],
        "gaps": [
            "TurboVec evidence is a small synthetic isolated trial; it is not the public default.",
            "The public dashboard has no live provider, writeback, or checkpointer.",
            "SQLite and PostgreSQL persistence require migration, backup, and recovery proof in their target environment.",
            "Orbit and Obsidian are optional local integrations; the portable repository cannot claim their live state.",
            "Graphify output must be regenerated whenever its recorded source commit is stale.",
            "Skill Spectre semantic scanning and a public Video Spectre execution are not proved.",
        ],
        "configuration_refs": {
            "crew": "project/system/contracts/knowledge-crew-config.json",
            "roles": "project/system/contracts/role-catalog.json",
            "workflows": "project/system/contracts/role-workflows.json",
            "controller": "project/system/contracts/operating-model.json",
            "case_schema": "project/system/schemas/knowledge-case.schema.json",
        },
    }
    OUTPUT.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"dashboard_data={OUTPUT.relative_to(ROOT)}")
    print(f"layers={data['counts']['layers']}")
    print(f"roles={data['counts']['roles']}")
    print(f"workflow_packs={data['counts']['workflow_packs']}")
    print("private_inputs=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
