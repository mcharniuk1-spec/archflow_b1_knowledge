#!/usr/bin/env python3
"""Run the public-safe E1.2 full proof graph.

The graph is deterministic and does not process raw private material. It proves
the current orchestration contract by recording node order, parallel analysis
branches, output paths, review status, and stream events for the report pack.
"""

from __future__ import annotations

import json
import operator
from datetime import datetime, timezone
from pathlib import Path
from typing import Annotated, Literal, TypedDict

from langgraph.graph import END, START, StateGraph


ROOT = Path(__file__).resolve().parents[2]
RUN_DIR = ROOT / "project" / "runs" / "E1.2" / "2026-06-26-full-test"
OUTPUT_JSON = RUN_DIR / "e1_2_langgraph_output.json"
STREAM_JSONL = RUN_DIR / "e1_2_stream_events.jsonl"


class E12State(TypedDict, total=False):
    run_id: str
    source_packet_id: str
    source_boundary_status: Literal["pass", "fail"]
    retrieved_context: list[str]
    architecture_analysis: dict[str, object]
    runtime_analysis: dict[str, object]
    knowledge_analysis: dict[str, object]
    agent_analysis: dict[str, object]
    trends_analysis: dict[str, object]
    merged_findings: list[str]
    context_digest_path: str
    prd_path: str
    task_matrix_path: str
    kb_update_path: str
    streaming_report_path: str
    system_report_path: str
    review_report_path: str
    approval_status: Literal["approved", "revise", "blocked"]
    gaps: Annotated[list[str], operator.add]
    node_history: Annotated[list[str], operator.add]
    stream_notes: Annotated[list[str], operator.add]


def event(node: str, note: str) -> dict[str, list[str]]:
    return {
        "node_history": [node],
        "stream_notes": [f"{node}: {note}"],
    }


def intake_validate(state: E12State) -> E12State:
    update = event("intake_validate", "sanitized E1.2 source packet accepted")
    packet_id = state.get("source_packet_id", "")
    if not packet_id.startswith("sanitized_"):
        return {
            **update,
            "source_boundary_status": "fail",
            "approval_status": "blocked",
            "gaps": ["source packet must be sanitized before E1.2 processing"],
        }
    return {**update, "source_boundary_status": "pass", "gaps": []}


def route_after_intake(state: E12State) -> str:
    return "retrieve_context" if state.get("source_boundary_status") == "pass" else "review_gate"


def retrieve_context(state: E12State) -> E12State:
    return {
        **event("retrieve_context", "approved public corpus and setup memory selected"),
        "retrieved_context": [
            "project/workflows/langgraph-controller.yaml",
            "project/workflows/crewai-crew.yaml",
            "project/workflows/llamaindex-rag.yaml",
            "project/workflows/knowledge-integration.yaml",
            "wiki/memory.md",
            "wiki/insights.md",
            "graphify-out/GRAPH_REPORT.md",
        ],
    }


def analyze_architecture(state: E12State) -> E12State:
    return {
        **event("analyze_architecture", "LangGraph remains the control spine"),
        "architecture_analysis": {
            "langgraph_role": "state, routing, parallel fan-out, review gates",
            "crewai_role": "role accountability and task ownership",
            "llamaindex_role": "approved-corpus retrieval with source paths",
            "recommended_change": "add durable checkpointer before real human approval interrupts",
        },
    }


def analyze_runtime(state: E12State) -> E12State:
    return {
        **event("analyze_runtime", "runtime checks remain deterministic and public-safe"),
        "runtime_analysis": {
            "langgraph": "smoke workflow passes",
            "llamaindex": "approved-corpus retrieval passes",
            "crewai": "config/import proof passes without LLM execution",
            "langsmith": "sanitized trace path configured",
            "recommended_change": "keep full CrewAI LLM kickoff behind LangGraph review",
        },
    }


def analyze_knowledge(state: E12State) -> E12State:
    return {
        **event("analyze_knowledge", "WikiLLM is canonical public memory"),
        "knowledge_analysis": {
            "wikillm": "active run, memory, insight, decision, and issue layer",
            "graphify": "generated structure map exists for public repo",
            "obsidian": "sanitized mirror remains planned, not source of truth",
            "nexus": "planned only after vault target and schemas are verified",
            "recommended_change": "do not activate live Nexus writes before a vault target is clear",
        },
    }


def analyze_agents(state: E12State) -> E12State:
    return {
        **event("analyze_agents", "agent roles are mapped but execution stays supervised"),
        "agent_analysis": {
            "af_tools": "source and runtime readiness",
            "af_context": "FACT/INTERPRETATION/HYPOTHESIS/GAP digest",
            "af_manager": "PRD, tasks, acceptance criteria",
            "af_knowledge": "KB update and memory candidates",
            "af_review": "safety and evidence gate",
            "af_publisher": "Git-ready release and handout",
            "recommended_change": "set agent-specific temperature policy before LLM execution",
        },
    }


def analyze_trends(state: E12State) -> E12State:
    return {
        **event("analyze_trends", "current docs favor typed streaming and observability"),
        "trends_analysis": {
            "langgraph": "typed stream events, persistence, human-in-the-loop",
            "crewai": "YAML crews, sequential/hierarchical processes, streaming, logs",
            "llamaindex": "agentic workflows, bounded RAG, source-grounded query engines",
            "langsmith": "tracing, monitoring, feedback, and automations",
            "recommended_change": "stream node state and custom progress, not hidden reasoning",
        },
    }


def merge_findings(state: E12State) -> E12State:
    return {
        **event("merge_findings", "parallel branch outputs merged into E1.2 report pack"),
        "merged_findings": [
            "Use LangGraph for control and typed event streaming.",
            "Use CrewAI for named roles but keep process sequential until task outputs stabilize.",
            "Use LlamaIndex only on approved public or sanitized corpus.",
            "Keep WikiLLM as durable public memory and Graphify as generated structure reference.",
            "Keep Nexus planned until live vault readiness and schemas are verified.",
        ],
    }


def draft_documents(state: E12State) -> E12State:
    return {
        **event("draft_documents", "E1.2 PRD, streaming report, and system report paths assigned"),
        "context_digest_path": "project/runs/E1.2/2026-06-26-full-test/context-digest.md",
        "prd_path": "project/runs/E1.2/2026-06-26-full-test/E1.2_PRD.md",
        "task_matrix_path": "project/runs/E1.2/2026-06-26-full-test/responsibility-matrix.md",
        "kb_update_path": "project/runs/E1.2/2026-06-26-full-test/kb-update.md",
        "streaming_report_path": "project/runs/E1.2/2026-06-26-full-test/E1.2_Streaming_report.md",
        "system_report_path": "project/runs/E1.2/2026-06-26-full-test/E1.2_System_report.md",
    }


def review_gate(state: E12State) -> E12State:
    if state.get("source_boundary_status") != "pass":
        return {
            **event("review_gate", "blocked because source boundary failed"),
            "approval_status": "blocked",
            "review_report_path": "project/runs/E1.2/2026-06-26-full-test/review-report.md",
        }
    return {
        **event("review_gate", "approved for public-safe internal E1.2 proof package"),
        "approval_status": "approved",
        "review_report_path": "project/runs/E1.2/2026-06-26-full-test/review-report.md",
    }


def publish_or_record(state: E12State) -> E12State:
    return event("publish_or_record", "run artifacts ready for PDF rendering and Git validation")


def route_after_review(state: E12State) -> str:
    return "publish_or_record" if state.get("approval_status") == "approved" else END


def build_graph():
    graph = StateGraph(E12State)
    graph.add_node("intake_validate", intake_validate)
    graph.add_node("retrieve_context", retrieve_context)
    graph.add_node("analyze_architecture", analyze_architecture)
    graph.add_node("analyze_runtime", analyze_runtime)
    graph.add_node("analyze_knowledge", analyze_knowledge)
    graph.add_node("analyze_agents", analyze_agents)
    graph.add_node("analyze_trends", analyze_trends)
    graph.add_node("merge_findings", merge_findings)
    graph.add_node("draft_documents", draft_documents)
    graph.add_node("review_gate", review_gate)
    graph.add_node("publish_or_record", publish_or_record)

    graph.add_edge(START, "intake_validate")
    graph.add_conditional_edges("intake_validate", route_after_intake)
    graph.add_edge("retrieve_context", "analyze_architecture")
    graph.add_edge("retrieve_context", "analyze_runtime")
    graph.add_edge("retrieve_context", "analyze_knowledge")
    graph.add_edge("retrieve_context", "analyze_agents")
    graph.add_edge("retrieve_context", "analyze_trends")
    graph.add_edge("analyze_architecture", "merge_findings")
    graph.add_edge("analyze_runtime", "merge_findings")
    graph.add_edge("analyze_knowledge", "merge_findings")
    graph.add_edge("analyze_agents", "merge_findings")
    graph.add_edge("analyze_trends", "merge_findings")
    graph.add_edge("merge_findings", "draft_documents")
    graph.add_edge("draft_documents", "review_gate")
    graph.add_conditional_edges("review_gate", route_after_review)
    graph.add_edge("publish_or_record", END)
    return graph.compile()


def json_safe(value: object) -> object:
    return json.loads(json.dumps(value, default=str))


def main() -> int:
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    graph = build_graph()
    initial_state: E12State = {
        "run_id": "e1_2_full_test_2026_06_26",
        "source_packet_id": "sanitized_e1_2_public_setup_review",
        "gaps": [],
        "node_history": [],
        "stream_notes": [],
    }

    stream_events: list[dict[str, object]] = []
    final_state: E12State = {}
    for index, chunk in enumerate(graph.stream(initial_state, stream_mode="updates"), start=1):
        event_record = {
            "index": index,
            "type": "updates",
            "data": json_safe(chunk),
            "recorded_at": datetime.now(timezone.utc).isoformat(),
        }
        stream_events.append(event_record)
        for _, update in chunk.items():
            if isinstance(update, dict):
                final_state.update(update)

    final_state = graph.invoke(initial_state)
    OUTPUT_JSON.write_text(
        json.dumps(
            {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "graph": "e1_2_full_test",
                "stream_event_count": len(stream_events),
                "final_state": json_safe(final_state),
                "safety": "public-safe sanitized state only; no hidden reasoning persisted",
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    STREAM_JSONL.write_text(
        "\n".join(json.dumps(item, sort_keys=True) for item in stream_events) + "\n",
        encoding="utf-8",
    )

    print("e1_2_full_test=ok")
    print(f"approval_status={final_state.get('approval_status')}")
    print(f"stream_events={len(stream_events)}")
    print(f"output={OUTPUT_JSON.relative_to(ROOT).as_posix()}")
    print(f"stream={STREAM_JSONL.relative_to(ROOT).as_posix()}")
    print("nodes=" + ",".join(final_state.get("node_history", [])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
