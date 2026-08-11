#!/usr/bin/env python3
"""Run the deterministic, provider-disabled ArchFlow controller smoke."""

from __future__ import annotations

import argparse
from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph


class ArchFlowState(TypedDict, total=False):
    run_id: str
    source_packet_id: str
    source_boundary_status: Literal["pass", "fail"]
    objective: str
    decision_supported: str
    retrieved_context: list[str]
    evidence_refs: list[str]
    role_pack_id: str
    maker_role_id: str
    reviewer_role_id: str
    authority_state: Literal["approved_for_local_execution", "not_approved"]
    artifact_ref: str
    verification_checks: list[str]
    review_verdict: Literal["approve", "revise", "block"]
    memory_decision: Literal["solution_candidate", "working_only", "exclude"]
    next_safe_action: str
    gaps: list[str]
    node_history: list[str]
    revision_count: int


def with_history(state: ArchFlowState, node_name: str) -> ArchFlowState:
    return {**state, "node_history": [*state.get("node_history", []), node_name]}


def classify_execution(state: ArchFlowState) -> ArchFlowState:
    return {
        **with_history(state, "classify_execution"),
        "role_pack_id": "responsive_product_change",
        "maker_role_id": "implementation_maker",
        "reviewer_role_id": "independent_reviewer",
        "authority_state": "approved_for_local_execution",
    }


def intake_validate(state: ArchFlowState) -> ArchFlowState:
    updated = with_history(state, "intake_validate")
    if not updated.get("source_packet_id", "").startswith("approved_public_"):
        return {
            **updated,
            "source_boundary_status": "fail",
            "review_verdict": "block",
            "memory_decision": "exclude",
            "gaps": [*updated.get("gaps", []), "source packet is outside the approved public fixture boundary"],
        }
    return {**updated, "source_boundary_status": "pass"}


def frame_objective(state: ArchFlowState) -> ArchFlowState:
    return {
        **with_history(state, "frame_objective"),
        "objective": "Prepare a responsive dashboard correction packet from approved public contracts.",
        "decision_supported": "Whether the candidate satisfies the declared responsive and safety checks.",
    }


def retrieve_context(state: ArchFlowState) -> ArchFlowState:
    return {
        **with_history(state, "retrieve_context"),
        "retrieved_context": [
            "project/dashboard/corpus-manifest.json",
            "project/database/role-catalog.json",
            "project/agents/actionable-role-packs.json",
            "project/database/solution-memory-record.schema.json",
            "project/database/action-receipt.schema.json",
        ],
    }


def ground_evidence(state: ArchFlowState) -> ArchFlowState:
    return {
        **with_history(state, "ground_evidence"),
        "evidence_refs": [
            "project/dashboard/corpus-manifest.json",
            "project/workflows/langgraph-controller.yaml",
        ],
    }


def design_execution(state: ArchFlowState) -> ArchFlowState:
    return with_history(state, "design_execution")


def execute_bounded_action(state: ArchFlowState) -> ArchFlowState:
    return {
        **with_history(state, "execute_bounded_action"),
        "artifact_ref": "memory://approved-public-fixture/artifact",
    }


def verify_result(state: ArchFlowState) -> ArchFlowState:
    checks = [
        "source_boundary_passed",
        "maker_reviewer_separated",
        "provider_calls_zero",
        "network_calls_zero",
        "external_writes_zero",
    ]
    return {**with_history(state, "verify_result"), "verification_checks": checks}


def review_gate(state: ArchFlowState) -> ArchFlowState:
    updated = with_history(state, "review_gate")
    maker = updated.get("maker_role_id")
    reviewer = updated.get("reviewer_role_id")
    if updated.get("source_boundary_status") != "pass" or not updated.get("evidence_refs"):
        return {**updated, "review_verdict": "block", "memory_decision": "exclude"}
    if not maker or not reviewer or maker == reviewer:
        return {
            **updated,
            "review_verdict": "block",
            "memory_decision": "exclude",
            "gaps": [*updated.get("gaps", []), "maker and reviewer must be separate"],
        }
    return {**updated, "review_verdict": "approve"}


def remember_result(state: ArchFlowState) -> ArchFlowState:
    updated = with_history(state, "remember_result")
    decision: Literal["solution_candidate", "working_only", "exclude"]
    decision = "solution_candidate" if updated.get("review_verdict") == "approve" else "exclude"
    return {**updated, "memory_decision": decision}


def route_outcome(state: ArchFlowState) -> ArchFlowState:
    updated = with_history(state, "route_outcome")
    return {**updated, "next_safe_action": "present_reviewed_local_packet"}


def write_task_handout(state: ArchFlowState) -> ArchFlowState:
    return with_history(state, "write_task_handout")


def after_intake(state: ArchFlowState) -> str:
    return "frame_objective" if state.get("source_boundary_status") == "pass" else "write_task_handout"


def after_design(state: ArchFlowState) -> str:
    if state.get("authority_state") == "approved_for_local_execution":
        return "execute_bounded_action"
    return "write_task_handout"


def after_review(state: ArchFlowState) -> str:
    if state.get("review_verdict") == "approve":
        return "remember_result"
    if state.get("review_verdict") == "revise" and state.get("revision_count", 0) < 2:
        return "design_execution"
    return "write_task_handout"


def build_graph():
    graph = StateGraph(ArchFlowState)
    graph.add_node("classify_execution", classify_execution)
    graph.add_node("intake_validate", intake_validate)
    graph.add_node("frame_objective", frame_objective)
    graph.add_node("retrieve_context", retrieve_context)
    graph.add_node("ground_evidence", ground_evidence)
    graph.add_node("design_execution", design_execution)
    graph.add_node("execute_bounded_action", execute_bounded_action)
    graph.add_node("verify_result", verify_result)
    graph.add_node("review_gate", review_gate)
    graph.add_node("remember_result", remember_result)
    graph.add_node("route_outcome", route_outcome)
    graph.add_node("write_task_handout", write_task_handout)

    graph.add_edge(START, "classify_execution")
    graph.add_edge("classify_execution", "intake_validate")
    graph.add_conditional_edges("intake_validate", after_intake)
    graph.add_edge("frame_objective", "retrieve_context")
    graph.add_edge("retrieve_context", "ground_evidence")
    graph.add_edge("ground_evidence", "design_execution")
    graph.add_conditional_edges("design_execution", after_design)
    graph.add_edge("execute_bounded_action", "verify_result")
    graph.add_edge("verify_result", "review_gate")
    graph.add_conditional_edges("review_gate", after_review)
    graph.add_edge("remember_result", "route_outcome")
    graph.add_edge("route_outcome", "write_task_handout")
    graph.add_edge("write_task_handout", END)
    return graph.compile()


def invoke_fixture(source_packet_id: str) -> ArchFlowState:
    return build_graph().invoke(
        {
            "run_id": "public_fixture_001",
            "source_packet_id": source_packet_id,
            "revision_count": 0,
            "gaps": [],
        }
    )


def run_self_test() -> int:
    accepted = invoke_fixture("approved_public_fixture_001")
    rejected = invoke_fixture("unapproved_fixture_001")
    accepted_ok = (
        accepted.get("review_verdict") == "approve"
        and accepted.get("memory_decision") == "solution_candidate"
        and "execute_bounded_action" in accepted.get("node_history", [])
    )
    rejected_ok = (
        rejected.get("review_verdict") == "block"
        and rejected.get("memory_decision") == "exclude"
        and "execute_bounded_action" not in rejected.get("node_history", [])
    )
    if not accepted_ok or not rejected_ok:
        print("langgraph_smoke_self_test=fail")
        return 1
    print("langgraph_smoke_self_test=ok cases=2")
    print("provider_calls=0 network_calls=0 external_writes=0")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="Run one accepted and one rejected fixture.")
    return parser.parse_args()


def main() -> int:
    if parse_args().self_test:
        return run_self_test()
    result = invoke_fixture("approved_public_fixture_001")
    if result.get("review_verdict") != "approve":
        print("langgraph_smoke=fail")
        return 1
    print("langgraph_smoke=ok")
    print(f"review_verdict={result.get('review_verdict')}")
    print(f"memory_decision={result.get('memory_decision')}")
    print(f"nodes={','.join(result.get('node_history', []))}")
    print("provider_calls=0 network_calls=0 external_writes=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
