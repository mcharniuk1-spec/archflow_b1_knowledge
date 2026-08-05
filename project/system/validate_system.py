#!/usr/bin/env python3
"""Provider-disabled contract, schema, authority, and fixture proof for ArchFlow."""

from __future__ import annotations

import json
import re
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parent
SUPPORTED_SCHEMA_KEYS = {
    "$schema", "$id", "title", "type", "required", "properties", "items",
    "additionalProperties", "const", "enum", "pattern", "minLength", "minItems",
}
TYPE_CHECKS = {
    "object": dict,
    "array": list,
    "string": str,
    "boolean": bool,
}
EXTERNAL_TARGETS = {
    "external_communication", "deployment", "production", "private_provider_call",
    "credential_store", "live_memory_writeback", "destructive_action",
}
EXTERNAL_SIDE_EFFECTS = {
    "external_message", "deployment", "production_change", "provider_disclosure",
    "credential_write", "live_memory_writeback", "destructive_change", "spend",
}


def load(relative: str) -> dict[str, Any]:
    with (ROOT / relative).open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_schema_definition(schema: dict[str, Any], path: str = "$") -> None:
    unknown = set(schema) - SUPPORTED_SCHEMA_KEYS
    if unknown:
        raise ValueError(f"{path} uses unsupported schema keywords: {sorted(unknown)}")
    if "type" in schema and schema["type"] not in TYPE_CHECKS:
        raise ValueError(f"{path}.type is unsupported: {schema['type']}")
    if "required" in schema and not isinstance(schema["required"], list):
        raise ValueError(f"{path}.required must be an array")
    properties = schema.get("properties", {})
    if not isinstance(properties, dict):
        raise ValueError(f"{path}.properties must be an object")
    if set(schema.get("required", [])) - set(properties):
        missing = sorted(set(schema["required"]) - set(properties))
        raise ValueError(f"{path}.required has undefined properties: {missing}")
    for name, child in properties.items():
        if not isinstance(child, dict):
            raise ValueError(f"{path}.properties.{name} must be a schema")
        validate_schema_definition(child, f"{path}.{name}")
    if "items" in schema:
        if not isinstance(schema["items"], dict):
            raise ValueError(f"{path}.items must be a schema")
        validate_schema_definition(schema["items"], f"{path}[]")


def validate_instance(value: Any, schema: dict[str, Any], path: str = "$") -> None:
    expected_type = schema.get("type")
    if expected_type and not isinstance(value, TYPE_CHECKS[expected_type]):
        raise ValueError(f"{path} must be {expected_type}")
    if "const" in schema and value != schema["const"]:
        raise ValueError(f"{path} must equal {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        raise ValueError(f"{path} must be one of {schema['enum']}")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            raise ValueError(f"{path} is shorter than minLength")
        if "pattern" in schema and re.fullmatch(schema["pattern"], value) is None:
            raise ValueError(f"{path} does not match {schema['pattern']}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            raise ValueError(f"{path} has fewer than minItems")
        if "items" in schema:
            for index, item in enumerate(value):
                validate_instance(item, schema["items"], f"{path}[{index}]")
    if isinstance(value, dict):
        properties = schema.get("properties", {})
        missing = [name for name in schema.get("required", []) if name not in value]
        if missing:
            raise ValueError(f"{path} missing required properties: {missing}")
        if schema.get("additionalProperties") is False:
            extra = sorted(set(value) - set(properties))
            if extra:
                raise ValueError(f"{path} has additional properties: {extra}")
        for name, child_schema in properties.items():
            if name in value:
                validate_instance(value[name], child_schema, f"{path}.{name}")


def validate_contracts() -> tuple[dict[str, Any], dict[str, Any], set[str]]:
    model = load("contracts/operating-model.json")
    catalog = load("contracts/role-catalog.json")
    case_schema = load("schemas/knowledge-case.schema.json")
    proposal_schema = load("schemas/action-proposal.schema.json")
    validate_schema_definition(case_schema)
    validate_schema_definition(proposal_schema)
    role_ids = {role["id"] for role in catalog["roles"]}
    required_roles = {
        "goal_and_architecture_operator", "requirements_and_market_research",
        "onboarding_guide", "designer", "action_validator", "independent_reviewer",
        "knowledge_librarian", "integrator", "surface_projection_operator",
    }
    if model["provider_default"] != "disabled" or model["writeback_default"] != "disabled":
        raise ValueError("public defaults must remain provider- and writeback-disabled")
    if not required_roles.issubset(role_ids):
        raise ValueError(f"required roles absent: {sorted(required_roles - role_ids)}")
    if not set(catalog.get("aliases", {}).values()).issubset(role_ids):
        raise ValueError("every role alias must resolve to a canonical role")
    if "Architecture 1" in model["states"] or "Architecture 2" in model["states"]:
        raise ValueError("legacy architecture labels cannot be controller states")
    return case_schema, proposal_schema, role_ids


def validate_case(case: dict[str, Any], schema: dict[str, Any], model: dict[str, Any], role_ids: set[str]) -> None:
    validate_instance(case, schema)
    if case["workflow_state"] not in model["states"]:
        raise ValueError("case workflow state is not registered")
    if case["source_boundary"]["status"] != "valid":
        raise ValueError("fixture case source boundary must be valid")
    authority = case["authority"]
    for role_field in ("requester_role", "maker_role", "reviewer_role"):
        if authority[role_field] not in role_ids:
            raise ValueError(f"case {role_field} is not a registered role")
    if authority["maker_role"] == authority["reviewer_role"]:
        raise ValueError("case must preserve maker/reviewer separation")
    evidence_ids = {item["id"] for item in case["evidence"]}
    requirement_ids = {item["id"] for item in case["requirements"]}
    for requirement in case["requirements"]:
        if not set(requirement["evidence_refs"]).issubset(evidence_ids):
            raise ValueError(f"requirement {requirement['id']} has unknown evidence")
        if requirement["reviewer_role"] not in role_ids:
            raise ValueError(f"requirement {requirement['id']} has unknown reviewer")
        if "superseded_by" in requirement and requirement["superseded_by"] not in requirement_ids:
            raise ValueError(f"requirement {requirement['id']} has unknown supersession target")


def evaluate(case: dict[str, Any], proposal: dict[str, Any], role_ids: set[str]) -> dict[str, Any]:
    reasons: list[str] = []
    requirements = {f"{item['id']}@{item['version']}": item for item in case["requirements"]}
    decisions = {f"{item.get('id')}@{item.get('version')}": item for item in case["decisions"]}
    referenced = set(proposal["requirement_refs"])
    coverage = {item["requirement_ref"]: item["status"] for item in proposal["coverage"]}

    if proposal["case_id"] != case["case_id"]:
        reasons.append("CASE_MISMATCH")
    if proposal["actor_role"] not in role_ids:
        reasons.append("UNKNOWN_ACTOR_ROLE")
    if proposal["review"]["maker_role"] != proposal["actor_role"]:
        reasons.append("MAKER_ACTOR_MISMATCH")
    case_authority = case["authority"]
    if proposal["review"]["maker_role"] != case_authority["maker_role"]:
        reasons.append("CASE_MAKER_MISMATCH")
    if proposal["review"]["reviewer_role"] != case_authority["reviewer_role"]:
        reasons.append("CASE_REVIEWER_MISMATCH")
    if proposal["review"]["maker_role"] == proposal["review"]["reviewer_role"]:
        reasons.append("SELF_REVIEW_FOR_CASE")
    for reference in referenced:
        requirement = requirements.get(reference)
        if requirement is None:
            reasons.append("UNKNOWN_REQUIREMENT")
        elif requirement["state"] != "approved":
            reasons.append("STALE_OR_UNAPPROVED_REQUIREMENT")
    if set(coverage) != referenced or any(status in {"gap", "exception"} for status in coverage.values()):
        reasons.append("REQUIREMENT_COVERAGE_INVALID")
    for reference in proposal["decision_refs"]:
        decision = decisions.get(reference)
        if decision is None or decision.get("state") != "approved":
            reasons.append("STALE_OR_UNKNOWN_DECISION")

    permission = proposal["permission_scope"]
    target_class = proposal["target"]["class"]
    target_ref = proposal["target"]["ref"]
    operation = permission["operation"]
    if permission["target_class"] != target_class:
        reasons.append("TARGET_CLASS_MISMATCH")
    allowed = [
        rule for rule in case["authority"]["allowed_actions"]
        if rule["actor_role"] == proposal["actor_role"]
        and rule["operation"] == operation
        and rule["target_class"] == target_class
    ]
    if len(allowed) != 1 or operation in case_authority["forbidden_actions"]:
        reasons.append("OUT_OF_AUTHORITY")
    target_path = PurePosixPath(target_ref)
    if target_path.is_absolute() or ".." in target_path.parts or "\\" in target_ref:
        reasons.append("TARGET_REF_INVALID")
    elif len(allowed) == 1 and not any(target_ref.startswith(prefix) for prefix in allowed[0]["target_prefixes"]):
        reasons.append("TARGET_OUTSIDE_ALLOWED_PREFIX")
    if permission["status"] != "allowed":
        reasons.append("PROPOSAL_PERMISSION_NOT_ALLOWED")

    external = target_class in EXTERNAL_TARGETS or bool(set(proposal["side_effects"]) & EXTERNAL_SIDE_EFFECTS)
    high_risk = external or proposal["review"]["risk"] == "high"
    if high_risk and proposal["review"]["maker_role"] == proposal["review"]["reviewer_role"]:
        reasons.append("SELF_REVIEW_FOR_HIGH_RISK")
    if proposal["review"]["reviewer_role"] not in role_ids:
        reasons.append("UNKNOWN_REVIEWER_ROLE")
    derived_approval = external or (len(allowed) == 1 and allowed[0]["approval_class"] == "target_specific_owner")
    approval = proposal["approval"]
    if approval["required"] != derived_approval:
        reasons.append("APPROVAL_POLICY_MISMATCH")
    if derived_approval and approval["status"] != "approved":
        reasons.append("TARGET_SPECIFIC_APPROVAL_MISSING")
    verification = proposal["verification_plan"]
    if verification["readback"].strip().lower() in {"", "none", "none."}:
        reasons.append("READBACK_MISSING")
    if proposal["reversibility"] == "irreversible" and proposal["rollback"].strip().lower().startswith("no reliable"):
        reasons.append("IRREVERSIBLE_WITHOUT_COMPENSATION")

    return {
        "proposal_id": proposal["proposal_id"],
        "verdict": "eligible" if not reasons else "blocked",
        "reasons": sorted(set(reasons)),
        "executed": False,
    }


def main() -> int:
    case_schema, proposal_schema, role_ids = validate_contracts()
    model = load("contracts/operating-model.json")
    case = load("fixtures/onboarding-case.json")
    validate_case(case, case_schema, model, role_ids)

    eligible_proposal = load("fixtures/action-proposal-eligible.json")
    blocked_proposal = load("fixtures/action-proposal-blocked.json")
    spoof_proposal = load("fixtures/action-proposal-authority-spoof.json")
    target_escape_proposal = load("fixtures/action-proposal-target-escape.json")
    reviewer_spoof_proposal = load("fixtures/action-proposal-reviewer-spoof.json")
    for proposal in (eligible_proposal, blocked_proposal, spoof_proposal):
        validate_instance(proposal, proposal_schema)
    eligible = evaluate(case, eligible_proposal, role_ids)
    blocked = evaluate(case, blocked_proposal, role_ids)
    spoof = evaluate(case, spoof_proposal, role_ids)
    target_escape = evaluate(case, target_escape_proposal, role_ids)
    validate_instance(reviewer_spoof_proposal, proposal_schema)
    reviewer_spoof = evaluate(case, reviewer_spoof_proposal, role_ids)
    if eligible["verdict"] != "eligible":
        raise ValueError(f"eligible fixture failed: {eligible}")
    blocked_expected = {
        "STALE_OR_UNAPPROVED_REQUIREMENT", "OUT_OF_AUTHORITY",
        "SELF_REVIEW_FOR_HIGH_RISK", "TARGET_SPECIFIC_APPROVAL_MISSING", "READBACK_MISSING",
    }
    if blocked["verdict"] != "blocked" or not blocked_expected.issubset(set(blocked["reasons"])):
        raise ValueError(f"blocked fixture did not fail closed: {blocked}")
    spoof_expected = {
        "UNKNOWN_ACTOR_ROLE", "OUT_OF_AUTHORITY", "SELF_REVIEW_FOR_HIGH_RISK",
        "UNKNOWN_REVIEWER_ROLE", "APPROVAL_POLICY_MISMATCH", "TARGET_SPECIFIC_APPROVAL_MISSING",
    }
    if spoof["verdict"] != "blocked" or not spoof_expected.issubset(set(spoof["reasons"])):
        raise ValueError(f"authority spoof did not fail closed: {spoof}")
    target_schema_rejected = False
    try:
        validate_instance(target_escape_proposal, proposal_schema)
    except ValueError:
        target_schema_rejected = True
    if not target_schema_rejected or target_escape["verdict"] != "blocked" or "TARGET_REF_INVALID" not in target_escape["reasons"]:
        raise ValueError(f"target escape did not fail closed: {target_escape}")
    reviewer_expected = {"CASE_REVIEWER_MISMATCH", "SELF_REVIEW_FOR_CASE"}
    if reviewer_spoof["verdict"] != "blocked" or not reviewer_expected.issubset(set(reviewer_spoof["reasons"])):
        raise ValueError(f"reviewer spoof did not fail closed: {reviewer_spoof}")

    malformed_rejected = False
    try:
        validate_instance(load("fixtures/action-proposal-malformed.json"), proposal_schema)
    except ValueError:
        malformed_rejected = True
    if not malformed_rejected:
        raise ValueError("malformed nested proposal unexpectedly passed schema validation")

    print(json.dumps({
        "status": "pass",
        "provider_mode": "disabled",
        "writeback": False,
        "schema_validation": "definitions_checked_and_applied",
        "malformed_fixture": "rejected",
        "target_escape_schema": "rejected",
        "results": [eligible, blocked, spoof, target_escape, reviewer_spoof],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
