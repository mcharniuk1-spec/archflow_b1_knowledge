#!/usr/bin/env python3
"""Run a provider-disabled smoke proof against canonical case states and roles.

The fixtures are synthetic. The graph starts no provider, submits no trace,
writes no checkpoint, and performs no external action.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph


ROOT = Path(__file__).resolve().parents[2]
SYSTEM = ROOT / "project" / "system"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


MODEL = load_json(SYSTEM / "contracts" / "operating-model.json")
CATALOG = load_json(SYSTEM / "contracts" / "role-catalog.json")
FIXTURE = load_json(SYSTEM / "fixtures" / "onboarding-case.json")
REGISTERED_STATES = set(MODEL["states"])
REGISTERED_ROLES = {role["id"] for role in CATALOG["roles"]}


class KnowledgeCaseState(TypedDict, total=False):
    case_id: str
    scenario: Literal["eligible", "repair", "approval_wait", "blocked_source"]
    source_boundary_status: Literal["valid", "invalid"]
    workflow_state: str
    display_phase: str
    maker_role: str
    reviewer_role: str
    requirements_current: bool
    repair_attempts: int
    action_id: str
    receipts: list[str]
    gaps: list[str]
    node_history: list[str]
    executed: bool


def phase_for(state_name: str) -> str:
    matches = [
        phase
        for phase, states in MODEL["display_phases"].items()
        if state_name in states
    ]
    if len(matches) != 1:
        raise ValueError(f"canonical state has no unique display phase: {state_name}")
    return matches[0]


def transition(
    state: KnowledgeCaseState,
    node: str,
    state_name: str,
    *,
    receipt: str | None = None,
    gap: str | None = None,
) -> KnowledgeCaseState:
    if state_name not in REGISTERED_STATES:
        raise ValueError(f"unregistered workflow state: {state_name}")
    receipts = list(state.get("receipts", []))
    gaps = list(state.get("gaps", []))
    if receipt:
        receipts.append(receipt)
    if gap:
        gaps.append(gap)
    return {
        **state,
        "workflow_state": state_name,
        "display_phase": phase_for(state_name),
        "receipts": receipts,
        "gaps": gaps,
        "node_history": [*state.get("node_history", []), node],
        "executed": False,
    }


def admit_case(state: KnowledgeCaseState) -> KnowledgeCaseState:
    if state.get("source_boundary_status") != "valid":
        return transition(
            state,
            "admit_case",
            "blocked",
            receipt="admission:blocked",
            gap="source boundary rejected",
        )
    return transition(
        state,
        "admit_case",
        "admission_checked",
        receipt="admission:pass",
    )


def assemble_perception(state: KnowledgeCaseState) -> KnowledgeCaseState:
    return transition(
        state,
        "assemble_perception",
        "context_bound",
        receipt="perception:canonical_fixture_exact_read",
    )


def plan_role_work(state: KnowledgeCaseState) -> KnowledgeCaseState:
    return transition(
        state,
        "plan_role_work",
        "work_planning",
        receipt="role_plan:canonical_roles",
    )


def specialist_work(state: KnowledgeCaseState) -> KnowledgeCaseState:
    return transition(
        state,
        "specialist_work",
        "proposal_ready",
        receipt="candidate:synthetic_local_documentation",
    )


def validate_action(state: KnowledgeCaseState) -> KnowledgeCaseState:
    if state.get("maker_role") not in REGISTERED_ROLES:
        return transition(state, "validate_action", "blocked", gap="maker role is not canonical")
    if state.get("reviewer_role") not in REGISTERED_ROLES:
        return transition(state, "validate_action", "blocked", gap="reviewer role is not canonical")
    if state.get("maker_role") == state.get("reviewer_role"):
        return transition(state, "validate_action", "blocked", gap="maker and reviewer must differ")
    if not state.get("requirements_current"):
        return transition(state, "validate_action", "blocked", gap="requirement is not current")

    scenario = state.get("scenario")
    if scenario == "repair":
        attempts = state.get("repair_attempts", 0)
        if attempts >= MODEL["repair_policy"]["maximum_attempts"]:
            return transition(state, "validate_action", "blocked", gap="repair limit reached")
        return transition(
            state,
            "validate_action",
            "repair",
            receipt="validation:repair",
        )
    if scenario == "approval_wait":
        action_id = state.get("action_id", "")
        if not action_id.startswith("action-"):
            return transition(state, "validate_action", "blocked", gap="action_id missing")
        return transition(
            state,
            "validate_action",
            "approval_wait",
            receipt=f"validation:approval_wait:{action_id}",
        )
    return transition(
        state,
        "validate_action",
        "proposal_validated",
        receipt="validation:eligible",
    )


def deterministic_verify(state: KnowledgeCaseState) -> KnowledgeCaseState:
    return transition(
        state,
        "deterministic_verify",
        "proposal_validated",
        receipt="verification:pass",
    )


def independent_review(state: KnowledgeCaseState) -> KnowledgeCaseState:
    return transition(
        state,
        "independent_review",
        "proposal_validated",
        receipt="independent_review:approve",
    )


def readback_result(state: KnowledgeCaseState) -> KnowledgeCaseState:
    return transition(
        state,
        "readback_result",
        "accepted_result",
        receipt="readback:exact_local_artifact",
    )


def promotion_review(state: KnowledgeCaseState) -> KnowledgeCaseState:
    return transition(
        state,
        "promotion_review",
        "promotion_review",
        receipt="knowledge_promotion:no_promotion_fixture",
    )


def close_case(state: KnowledgeCaseState) -> KnowledgeCaseState:
    return transition(
        state,
        "close_case",
        "closed",
        receipt="terminal:closed",
    )


def after_admission(state: KnowledgeCaseState) -> str:
    return END if state.get("workflow_state") == "blocked" else "assemble_perception"


def after_validation(state: KnowledgeCaseState) -> str:
    if state.get("workflow_state") in {"blocked", "repair", "approval_wait"}:
        return END
    return "deterministic_verify"


def build_graph():
    graph = StateGraph(KnowledgeCaseState)
    graph.add_node("admit_case", admit_case)
    graph.add_node("assemble_perception", assemble_perception)
    graph.add_node("plan_role_work", plan_role_work)
    graph.add_node("specialist_work", specialist_work)
    graph.add_node("validate_action", validate_action)
    graph.add_node("deterministic_verify", deterministic_verify)
    graph.add_node("independent_review", independent_review)
    graph.add_node("readback_result", readback_result)
    graph.add_node("promotion_review", promotion_review)
    graph.add_node("close_case", close_case)

    graph.add_edge(START, "admit_case")
    graph.add_conditional_edges("admit_case", after_admission)
    graph.add_edge("assemble_perception", "plan_role_work")
    graph.add_edge("plan_role_work", "specialist_work")
    graph.add_edge("specialist_work", "validate_action")
    graph.add_conditional_edges("validate_action", after_validation)
    graph.add_edge("deterministic_verify", "independent_review")
    graph.add_edge("independent_review", "readback_result")
    graph.add_edge("readback_result", "promotion_review")
    graph.add_edge("promotion_review", "close_case")
    graph.add_edge("close_case", END)
    return graph.compile()


def base_case(scenario: str) -> KnowledgeCaseState:
    authority = FIXTURE["authority"]
    maker_role = authority["maker_role"]
    reviewer_role = authority["reviewer_role"]
    if maker_role not in REGISTERED_ROLES or reviewer_role not in REGISTERED_ROLES:
        raise SystemExit("langgraph_smoke=fail:fixture_role_not_canonical")
    return {
        "case_id": FIXTURE["case_id"],
        "scenario": scenario,
        "source_boundary_status": "invalid" if scenario == "blocked_source" else "valid",
        "workflow_state": "request_received",
        "display_phase": phase_for("request_received"),
        "maker_role": maker_role,
        "reviewer_role": reviewer_role,
        "requirements_current": True,
        "repair_attempts": 1,
        "action_id": "action-synthetic-approval",
        "receipts": [],
        "gaps": [],
        "node_history": [],
        "executed": False,
    }


def assert_result(name: str, result: KnowledgeCaseState, expected_state: str) -> None:
    if result.get("workflow_state") != expected_state:
        raise SystemExit(f"langgraph_smoke=fail:{name}_state")
    if result.get("workflow_state") not in REGISTERED_STATES:
        raise SystemExit(f"langgraph_smoke=fail:{name}_unregistered_state")
    if result.get("executed"):
        raise SystemExit(f"langgraph_smoke=fail:{name}_external_action")


def main() -> int:
    graph = build_graph()
    eligible = graph.invoke(base_case("eligible"))
    blocked = graph.invoke(base_case("blocked_source"))
    repair = graph.invoke(base_case("repair"))
    approval_wait = graph.invoke(base_case("approval_wait"))

    assert_result("eligible", eligible, "closed")
    assert_result("blocked", blocked, "blocked")
    assert_result("repair", repair, "repair")
    assert_result("approval_wait", approval_wait, "approval_wait")

    if "independent_review:approve" not in eligible.get("receipts", []):
        raise SystemExit("langgraph_smoke=fail:independent_review_missing")
    if "readback:exact_local_artifact" not in eligible.get("receipts", []):
        raise SystemExit("langgraph_smoke=fail:readback_missing")
    if any("execution:" in receipt for receipt in approval_wait.get("receipts", [])):
        raise SystemExit("langgraph_smoke=fail:approval_wait_executed")

    print("langgraph_smoke=ok")
    print("canonical_states=verified")
    print("canonical_roles=verified")
    print("eligible_state=closed")
    print("blocked_state=blocked")
    print("repair_state=repair")
    print("approval_state=approval_wait")
    print("independent_review=verified")
    print("readback=verified")
    print("provider_calls=0")
    print("checkpoint_writes=0")
    print("external_actions=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
