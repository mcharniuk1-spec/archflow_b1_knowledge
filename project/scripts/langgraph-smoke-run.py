#!/usr/bin/env python3
"""Run a public-safe LangGraph smoke workflow.

The workflow uses sanitized state only. If the ignored LangSmith env file is
present, the run is traced without sending raw private material or secrets.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph


ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT / "project" / ".env.langsmith.local"


class ArchFlowState(TypedDict, total=False):
    run_id: str
    source_packet_id: str
    source_boundary_status: Literal["pass", "fail"]
    retrieved_context: list[str]
    context_digest_path: str
    prd_path: str
    task_matrix_path: str
    kb_update_path: str
    review_report_path: str
    approval_status: Literal["approved", "revise", "blocked"]
    gaps: list[str]
    node_history: list[str]
    revision_loops: int


def load_env(path: Path) -> bool:
    if not path.exists():
        return False
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))
    return bool(os.environ.get("LANGSMITH_API_KEY"))


def with_history(state: ArchFlowState, node_name: str) -> ArchFlowState:
    return {**state, "node_history": [*state.get("node_history", []), node_name]}


def intake_validate(state: ArchFlowState) -> ArchFlowState:
    updated = with_history(state, "intake_validate")
    packet_id = updated.get("source_packet_id", "")
    if not packet_id.startswith("sanitized_"):
        return {
            **updated,
            "source_boundary_status": "fail",
            "approval_status": "blocked",
            "gaps": [*updated.get("gaps", []), "source packet must be sanitized before runtime processing"],
        }
    return {**updated, "source_boundary_status": "pass"}


def retrieve_context(state: ArchFlowState) -> ArchFlowState:
    updated = with_history(state, "retrieve_context")
    return {
        **updated,
        "retrieved_context": [
            "approved public workflow config",
            "approved public agent roster",
            "approved public WikiLLM memory",
        ],
    }


def write_context_digest(state: ArchFlowState) -> ArchFlowState:
    updated = with_history(state, "write_context_digest")
    return {**updated, "context_digest_path": "project/outputs/templates/context-digest.md"}


def run_crew_prd(state: ArchFlowState) -> ArchFlowState:
    updated = with_history(state, "run_crew_prd")
    return {
        **updated,
        "prd_path": "project/outputs/templates/prd.md",
        "task_matrix_path": "project/outputs/templates/responsibility-matrix.md",
    }


def write_kb_update(state: ArchFlowState) -> ArchFlowState:
    updated = with_history(state, "write_kb_update")
    return {**updated, "kb_update_path": "project/outputs/templates/knowledge-base-update.md"}


def review_gate(state: ArchFlowState) -> ArchFlowState:
    updated = with_history(state, "review_gate")
    if updated.get("source_boundary_status") != "pass":
        return {
            **updated,
            "approval_status": "blocked",
            "review_report_path": "project/outputs/templates/review-report.md",
        }
    return {
        **updated,
        "approval_status": "approved",
        "review_report_path": "project/outputs/templates/review-report.md",
    }


def publish_or_revise(state: ArchFlowState) -> ArchFlowState:
    return with_history(state, "publish_or_revise")


def after_intake(state: ArchFlowState) -> str:
    return "retrieve_context" if state.get("source_boundary_status") == "pass" else "review_gate"


def after_review(state: ArchFlowState) -> str:
    if state.get("approval_status") == "approved":
        return "publish_or_revise"
    if state.get("approval_status") == "revise" and state.get("revision_loops", 0) < 2:
        return "write_context_digest"
    return END


def build_graph():
    graph = StateGraph(ArchFlowState)
    graph.add_node("intake_validate", intake_validate)
    graph.add_node("retrieve_context", retrieve_context)
    graph.add_node("write_context_digest", write_context_digest)
    graph.add_node("run_crew_prd", run_crew_prd)
    graph.add_node("write_kb_update", write_kb_update)
    graph.add_node("review_gate", review_gate)
    graph.add_node("publish_or_revise", publish_or_revise)

    graph.add_edge(START, "intake_validate")
    graph.add_conditional_edges("intake_validate", after_intake)
    graph.add_edge("retrieve_context", "write_context_digest")
    graph.add_edge("write_context_digest", "run_crew_prd")
    graph.add_edge("run_crew_prd", "write_kb_update")
    graph.add_edge("write_kb_update", "review_gate")
    graph.add_conditional_edges("review_gate", after_review)
    graph.add_edge("publish_or_revise", END)
    return graph.compile()


def main() -> int:
    trace_requested = load_env(ENV_FILE)
    if trace_requested:
        os.environ.setdefault("LANGSMITH_TRACING", "true")
        os.environ.setdefault("LANGSMITH_PROJECT", "ArchFlow")

    compiled = build_graph()

    def run() -> ArchFlowState:
        return compiled.invoke(
            {
                "run_id": "langgraph_smoke_001",
                "source_packet_id": "sanitized_june24_next_steps",
                "revision_loops": 0,
                "gaps": [],
            }
        )

    if trace_requested:
        from langsmith import traceable

        traced_run = traceable(
            name="archflow_langgraph_smoke_run",
            project_name=os.environ["LANGSMITH_PROJECT"],
            tags=["archflow", "langgraph", "public-safe", "smoke"],
        )(run)
        result = traced_run()
        trace_status = "submitted"
    else:
        result = run()
        trace_status = "skipped_missing_local_env"

    print("langgraph_smoke=ok")
    print(f"approval_status={result.get('approval_status')}")
    print(f"nodes={','.join(result.get('node_history', []))}")
    print(f"langsmith_trace={trace_status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
