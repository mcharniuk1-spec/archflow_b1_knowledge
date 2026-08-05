#!/usr/bin/env python3
"""Provider-disabled contract, schema, authority, and fixture proof for ArchFlow."""

from __future__ import annotations

import copy
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parent
REPO = PROJECT.parent
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


def load_repo(relative: str) -> dict[str, Any]:
    with (REPO / relative).open(encoding="utf-8") as handle:
        return json.load(handle)


def expect_rejected(label: str, callback: Any) -> None:
    try:
        callback()
    except (ValueError, KeyError, TypeError):
        return
    raise ValueError(f"negative fixture unexpectedly passed: {label}")


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


def validate_contracts() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], set[str]]:
    model = load("contracts/operating-model.json")
    catalog = load("contracts/role-catalog.json")
    case_schema = load("schemas/knowledge-case.schema.json")
    proposal_schema = load("schemas/action-proposal.schema.json")
    binding_schema = load("schemas/role-task-binding.schema.json")
    validate_schema_definition(case_schema)
    validate_schema_definition(proposal_schema)
    validate_schema_definition(binding_schema)
    states = model["states"]
    schema_states = case_schema["properties"]["workflow_state"]["enum"]
    if schema_states != states:
        raise ValueError("Knowledge Case schema state enum must exactly equal the ordered controller state registry")
    phase_states = [state for values in model["display_phases"].values() for state in values]
    if len(phase_states) != len(set(phase_states)) or set(phase_states) != set(states):
        raise ValueError("display phases must contain every canonical state exactly once")
    role_ids = validate_role_catalog(catalog)
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
    validate_run_profiles(catalog, model, role_ids)
    return case_schema, proposal_schema, binding_schema, catalog, role_ids


def validate_role_catalog(catalog: dict[str, Any]) -> set[str]:
    roles = catalog["roles"]
    if catalog.get("schema_version") != "3.0.0" or len(roles) != 21:
        raise ValueError("canonical role catalog must contain 21 schema-v3 roles")
    role_ids = {role["id"] for role in roles}
    if len(role_ids) != len(roles):
        raise ValueError("canonical role IDs must be unique")
    skill_catalog = load_repo("project/database/skill-catalog.json")
    skill_ids = {item["id"] for item in skill_catalog["items"]}
    tool_ids = set(catalog["tool_capabilities"])
    permission_modes = set(catalog["permission_modes"])
    required_role_fields = {"id", "call_name", "title", "lane", "goal", "purpose", "owns", "forbidden", "task_defaults"}
    required_defaults = {"inputs", "owned_output", "allowed_skills", "allowed_tools", "permission_mode", "reviewer_route", "handoff_to"}
    outputs: set[str] = set()
    call_names: set[str] = set()
    side_effect_tools = {"edit_claimed_targets", "perform_exact_external_action", "perform_owner_approved_git_action"}
    for role in roles:
        missing = required_role_fields - set(role)
        if missing:
            raise ValueError(f"role {role.get('id')} missing fields: {sorted(missing)}")
        if re.fullmatch(r"[A-Za-z]+", role["call_name"]) is None or role["call_name"] in call_names:
            raise ValueError(f"role call name must be unique English letters: {role['call_name']}")
        call_names.add(role["call_name"])
        defaults = role["task_defaults"]
        missing_defaults = required_defaults - set(defaults)
        if missing_defaults or "allowed_actions" in defaults:
            raise ValueError(f"role {role['id']} has invalid task defaults: {sorted(missing_defaults)}")
        if not defaults["inputs"] or not defaults["owned_output"]:
            raise ValueError(f"role {role['id']} needs inputs and one owned output")
        if defaults["owned_output"] in outputs:
            raise ValueError(f"owned output has more than one role: {defaults['owned_output']}")
        outputs.add(defaults["owned_output"])
        if not set(defaults["allowed_skills"]).issubset(skill_ids):
            raise ValueError(f"role {role['id']} references an unregistered public skill")
        if not set(defaults["allowed_tools"]).issubset(tool_ids):
            raise ValueError(f"role {role['id']} references an unregistered tool capability")
        if defaults["permission_mode"] not in permission_modes:
            raise ValueError(f"role {role['id']} has an unknown permission mode")
        route = defaults["reviewer_route"]
        if not route or route[-1] != "@case_owner" or role["id"] in route:
            raise ValueError(f"role {role['id']} reviewer route must terminate at the owner without self-review")
        if not set(route[:-1]).issubset(role_ids):
            raise ValueError(f"role {role['id']} reviewer route contains an unknown role")
        if defaults["handoff_to"] != route[0]:
            raise ValueError(f"role {role['id']} handoff must equal the first reviewer route target")
        if role["lane"] in {"reviewer", "validator", "verifier"} and set(defaults["allowed_tools"]) & side_effect_tools:
            raise ValueError(f"review role {role['id']} cannot receive mutation or external action tools")
        if "perform_exact_external_action" in defaults["allowed_tools"] and defaults["permission_mode"] != "external_action_exact_approval":
            raise ValueError(f"role {role['id']} external action tool requires exact approval mode")
        if "perform_owner_approved_git_action" in defaults["allowed_tools"] and defaults["permission_mode"] != "git_action_exact_approval":
            raise ValueError(f"role {role['id']} Git tool requires exact approval mode")
    graph = {
        role["id"]: [target for target in role["task_defaults"]["reviewer_route"] if target != "@case_owner"]
        for role in roles
    }
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(role_id: str) -> None:
        if role_id in visiting:
            raise ValueError(f"reviewer-route cycle detected at {role_id}")
        if role_id in visited:
            return
        visiting.add(role_id)
        for target in graph[role_id]:
            visit(target)
        visiting.remove(role_id)
        visited.add(role_id)

    for role_id in graph:
        visit(role_id)
    if not set(catalog.get("aliases", {}).values()).issubset(role_ids):
        raise ValueError("every role alias must resolve to a canonical role")
    return role_ids


def validate_run_profiles(catalog: dict[str, Any], model: dict[str, Any], role_ids: set[str]) -> None:
    policy = load_repo("project/architecture/run-profiles.yaml")
    expected_profiles = {"documentation", "research", "architecture", "runtime", "retrieval", "content", "review", "external_action"}
    if set(policy["profiles"]) != expected_profiles:
        raise ValueError("run profile IDs drifted from the approved eight-profile set")
    role_map = {role["id"]: role for role in catalog["roles"]}
    referenced: set[str] = {policy["controller_role"]}
    canonical_states = set(model["states"])
    for profile_id, profile in policy["profiles"].items():
        packs = [profile["role_pack"]]
        if profile.get("monitor_role_pack"):
            packs.append(profile["monitor_role_pack"])
        for pack in packs:
            if len(pack) != len(set(pack)):
                raise ValueError(f"profile {profile_id} contains duplicate roles")
            referenced.update(pack)
        if len(profile["role_pack"]) < profile["minimum_roles"]:
            raise ValueError(f"profile {profile_id} does not meet its minimum role count")
        if profile["reviewer_role"] not in profile["role_pack"]:
            raise ValueError(f"profile {profile_id} omits its reviewer")
        for key in ("entry_state", "review_gate", "terminal_state"):
            if profile[key] not in canonical_states:
                raise ValueError(f"profile {profile_id} uses an unknown canonical state")
        monitor = profile.get("monitor_role_pack", [])
        if monitor and any(role_map[role_id]["lane"] in {"maker", "integrator"} for role_id in monitor):
            raise ValueError(f"profile {profile_id} monitor pack cannot contain maker or integrator roles")
    if not referenced.issubset(role_ids) or set(policy["roles"]) != referenced:
        raise ValueError("active admission roles must exactly equal profile packs plus the controller")
    for role_id, projected in policy["roles"].items():
        canonical = role_map[role_id]
        if projected["call_name"] != canonical["call_name"] or projected["title"] != canonical["title"]:
            raise ValueError(f"admission projection drifted for role {role_id}")
        if projected["authority"] != canonical["owns"] or projected["forbidden"] != canonical["forbidden"]:
            raise ValueError(f"admission authority drifted for role {role_id}")
    for epic in policy["epics"].values():
        if epic["entry_state"] not in canonical_states:
            raise ValueError("epic entry state is not canonical")
    for state in policy["admission_envelope"]["states"]:
        if not state["id"].startswith("admission.") or state["workflow_state"] not in canonical_states:
            raise ValueError("admission envelope must be namespaced and project only to canonical states")
    required_refs = policy["required_cag_references"]
    if any("20260729-architecture-enforcement/task-contract.md" in ref for ref in required_refs):
        raise ValueError("superseded July contract cannot remain a required CAG reference")
    missing_refs = [ref for ref in required_refs if not (REPO / ref).exists()]
    if missing_refs:
        raise ValueError(f"required CAG references are missing: {missing_refs}")


def validate_knowledge_crew() -> dict[str, Any]:
    crew = load("contracts/knowledge-crew-config.json")
    catalog = load("contracts/role-catalog.json")
    workflows = load("contracts/role-workflows.json")
    model = load("contracts/operating-model.json")

    roles = catalog["roles"]
    role_ids = {role["id"] for role in roles}
    call_names = [role["call_name"] for role in roles]
    if len(call_names) != len(set(call_names)):
        raise ValueError("role call names must be unique")
    if any(re.fullmatch(r"[A-Za-z]+", name) is None for name in call_names):
        raise ValueError("public role call names must use English letters only")
    if [layer["id"] for layer in crew["layers"]] != [f"L{number}" for number in range(1, 8)]:
        raise ValueError("knowledge crew must define exactly ordered layers L1-L7")
    for layer in crew["layers"]:
        unknown = set(layer["primary_roles"]) - role_ids
        if unknown:
            raise ValueError(f"{layer['id']} has unknown primary roles: {sorted(unknown)}")

    capsule = crew["perception_capsule"]
    section_budget = sum(section["budget"] for section in capsule["sections"])
    if section_budget != capsule["maximum_tokens"] or capsule["maximum_tokens"] != 12000:
        raise ValueError("perception capsule section budgets must exactly equal the 12,000-token ceiling")
    if "stop_before_dropping_current_requirements" not in capsule["overflow_order"]:
        raise ValueError("context overflow must fail closed before dropping current requirements")

    llamaindex = crew["frameworks"]["llamaindex"]
    ingestion = llamaindex["ingestion"]
    retrieval = llamaindex["retrieval"]
    if (ingestion["chunk_size"], ingestion["chunk_overlap"]) != (800, 120):
        raise ValueError("public LlamaIndex baseline must remain chunk_size 800 / overlap 120")
    required_retrieval = {
        "lexical_top_k": 5,
        "vector_top_k": 5,
        "rerank_top_k": 5,
        "final_source_limit": 8,
        "require_source_paths": True,
        "require_exact_read_for_action": True,
        "fallback_to_lexical": True,
        "refuse_private_match": True,
    }
    for key, expected in required_retrieval.items():
        if retrieval.get(key) != expected:
            raise ValueError(f"LlamaIndex retrieval parameter {key} must be {expected!r}")

    turbovec = crew["frameworks"]["turbovec"]
    gate = turbovec["promotion_gate"]
    if turbovec["default_backend_changed"] is not False:
        raise ValueError("TurboVec cannot become the public default from the isolated trial")
    if turbovec["current_evidence"]["verdict"] != "optional_trial_not_default":
        raise ValueError("TurboVec public evidence must remain calibrated as optional_trial_not_default")
    if turbovec["current_evidence"].get("public_receipt") != "project/reports/20260713-secured-runtime-architecture-report.md":
        raise ValueError("TurboVec exact public metrics require the named public receipt")
    if "lexical_recall_at_3" in turbovec["current_evidence"] or "fixture_documents" in turbovec["current_evidence"]:
        raise ValueError("TurboVec current evidence cannot publish unmatched document or lexical-baseline values")
    if gate["fixed_query_count"] < 20 or gate["citation_retention"] != 1.0:
        raise ValueError("TurboVec promotion gate requires at least 20 fixed queries and full citation retention")
    if "lexical" not in turbovec["fallback"]:
        raise ValueError("TurboVec requires a lexical fallback")

    crewai = crew["frameworks"]["crewai"]
    if any((crewai["memory"], crewai["planning"], crewai["delegation_default"])):
        raise ValueError("CrewAI public defaults must keep memory, planning, and delegation disabled")
    if crewai["cache"] is not True or crewai["maximum_parallel_tasks"] != 3:
        raise ValueError("CrewAI cache and bounded parallel defaults drifted")

    langgraph = crew["frameworks"]["langgraph"]
    if langgraph["checkpointer"]["public_demo"] != "none" or langgraph["checkpointer"]["thread_id"] != "case_id":
        raise ValueError("public LangGraph checkpointer must remain none and thread_id must remain case_id")
    if "external_action_approval" not in langgraph["interrupts"]:
        raise ValueError("LangGraph must interrupt before external action")
    if "action_id" not in langgraph["idempotency"]:
        raise ValueError("LangGraph side effects must declare action_id replay protection")

    if workflows.get("schema_version") != "3.0.0" or workflows.get("role_reference") != "canonical_machine_id":
        raise ValueError("workflow packs must use the schema-v3 canonical role reference")
    for pack in workflows["packs"]:
        unknown_roles = set(pack["roles"]) - role_ids
        if unknown_roles:
            raise ValueError(f"workflow {pack['id']} has unknown role IDs: {sorted(unknown_roles)}")
        if len(pack["roles"]) != len(set(pack["roles"])):
            raise ValueError(f"workflow {pack['id']} contains duplicate role IDs")
        for key in ("methods", "inputs", "outputs", "done"):
            if not pack.get(key):
                raise ValueError(f"workflow {pack['id']} is missing {key}")
    required_packs = {
        "employee_onboarding", "requirements_research", "task_planning", "outreach",
        "content_and_copy", "design", "implementation", "reporting",
        "knowledge_maintenance", "release_and_external_action",
    }
    pack_ids = {pack["id"] for pack in workflows["packs"]}
    if not required_packs.issubset(pack_ids):
        raise ValueError(f"required workflow packs absent: {sorted(required_packs - pack_ids)}")

    section_ids = {section["id"] for section in crew["dashboard_sections"]}
    if section_ids != {"today", "work", "knowledge", "team", "review", "setup"}:
        raise ValueError("dashboard section contract drifted")
    if model["configuration_refs"]["knowledge_crew"] != "project/system/contracts/knowledge-crew-config.json":
        raise ValueError("operating model must route to the knowledge crew contract")
    if model["adapters"]["external_actions"] != "disabled_until_exact_owner_approval":
        raise ValueError("external action adapter must fail closed")

    return {
        "layers": len(crew["layers"]),
        "roles": len(roles),
        "workflow_packs": len(workflows["packs"]),
        "context_tokens": capsule["maximum_tokens"],
        "turbovec": turbovec["current_evidence"]["verdict"],
        "crewai_provider_runtime": crewai["runtime_status"],
        "langgraph_public_checkpointer": langgraph["checkpointer"]["public_demo"],
    }


def validate_role_binding(
    binding: dict[str, Any],
    binding_schema: dict[str, Any],
    case: dict[str, Any],
    catalog: dict[str, Any],
    role_ids: set[str],
) -> None:
    validate_instance(binding, binding_schema)
    role_map = {role["id"]: role for role in catalog["roles"]}
    role = role_map.get(binding["role_id"])
    if role is None:
        raise ValueError(f"binding {binding['binding_id']} uses an unknown role")
    defaults = role["task_defaults"]
    exact_matches = {
        "call_name": role["call_name"],
        "role_goal": role["goal"],
        "inputs": defaults["inputs"],
        "owned_output": defaults["owned_output"],
        "allowed_skills": defaults["allowed_skills"],
        "allowed_tools": defaults["allowed_tools"],
        "forbidden_actions": role["forbidden"],
        "reviewer_route": defaults["reviewer_route"],
    }
    for key, expected in exact_matches.items():
        if binding[key] != expected:
            raise ValueError(f"binding {binding['binding_id']} drifted from canonical {key}")
    if binding["case_id"] != case["case_id"]:
        raise ValueError(f"binding {binding['binding_id']} uses a different case")
    boundary = binding["permission_boundary"]
    if boundary["authority_ref"] != "case.authority" or boundary["mode"] != defaults["permission_mode"]:
        raise ValueError(f"binding {binding['binding_id']} attempted to expand or alter authority")
    expected_forbidden_ref = f"role_catalog.roles.{role['id']}.forbidden"
    if boundary["forbidden_actions_ref"] != expected_forbidden_ref:
        raise ValueError(f"binding {binding['binding_id']} has an invalid forbidden-actions reference")
    if binding["handoff"]["to"] != binding["reviewer_route"][0] or binding["handoff"]["to"] != defaults["handoff_to"]:
        raise ValueError(f"binding {binding['binding_id']} handoff does not match its reviewer route")
    binding_fields = set(binding_schema["properties"])
    unknown_payload_fields = set(binding["handoff"]["payload"]) - binding_fields
    if unknown_payload_fields:
        raise ValueError(
            f"binding {binding['binding_id']} handoff references unknown fields: {sorted(unknown_payload_fields)}"
        )
    expected_payload = ["case_id", "binding_id", "role_id", "owned_output", "source_refs", "requirement_refs", "exact_targets", "deterministic_checks", "known_gaps", "stop_conditions"]
    if binding["handoff"]["payload"] != expected_payload:
        raise ValueError(f"binding {binding['binding_id']} handoff payload drifted")
    route_roles = set(binding["reviewer_route"]) - {"@case_owner"}
    if not route_roles.issubset(role_ids) or binding["role_id"] in route_roles or binding["reviewer_route"][-1] != "@case_owner":
        raise ValueError(f"binding {binding['binding_id']} has an invalid reviewer route")
    source_refs = {item["source_ref"] for item in case["evidence"]}
    requirement_refs = {f"{item['id']}@{item['version']}" for item in case["requirements"]}
    if not set(binding["source_refs"]).issubset(source_refs):
        raise ValueError(f"binding {binding['binding_id']} contains an unknown source reference")
    if not set(binding["requirement_refs"]).issubset(requirement_refs):
        raise ValueError(f"binding {binding['binding_id']} contains an unknown requirement reference")
    gap_refs = {item["id"] for item in case["gaps"]}
    if not set(binding["known_gaps"]).issubset(gap_refs):
        raise ValueError(f"binding {binding['binding_id']} contains an unknown gap reference")
    target_required_modes = {"local_mutation_exact_targets", "external_action_exact_approval", "git_action_exact_approval"}
    if boundary["mode"] in target_required_modes and not binding["exact_targets"]:
        raise ValueError(f"binding {binding['binding_id']} requires an exact target")
    if boundary["mode"] in {"external_action_exact_approval", "git_action_exact_approval"}:
        approved_targets = {item["exact_target"] for item in case["approvals"] if item["state"] == "approved"}
        if not set(binding["exact_targets"]).issubset(approved_targets):
            raise ValueError(f"binding {binding['binding_id']} lacks target-specific approval")


def expected_case_roles(case: dict[str, Any], workflows: dict[str, Any], catalog: dict[str, Any]) -> tuple[set[str], set[str]]:
    pack_ids = {binding["workflow_pack_id"] for binding in case["role_task_bindings"]}
    if len(pack_ids) != 1:
        raise ValueError("a fixture case must materialize exactly one workflow pack")
    pack_id = next(iter(pack_ids))
    pack = next((item for item in workflows["packs"] if item["id"] == pack_id), None)
    if pack is None:
        raise ValueError("case role binding uses an unknown workflow pack")
    base = set(pack["roles"])
    selected = set(base)
    for key in ("requester_role", "maker_role", "reviewer_role"):
        selected.add(case["authority"][key])
    for task in case["tasks"]:
        selected.update((task["owner_role"], task["reviewer_role"]))
    selected.discard("@case_owner")
    role_map = {role["id"]: role for role in catalog["roles"]}
    queue = list(selected)
    while queue:
        current = queue.pop(0)
        role = role_map.get(current)
        if role is None:
            raise ValueError(f"case closure contains unknown role: {current}")
        for target in role["task_defaults"]["reviewer_route"]:
            if target != "@case_owner" and target not in selected:
                selected.add(target)
                queue.append(target)
    return base, selected


def validate_case(
    case: dict[str, Any],
    schema: dict[str, Any],
    binding_schema: dict[str, Any],
    model: dict[str, Any],
    catalog: dict[str, Any],
    role_ids: set[str],
) -> None:
    validate_instance(case, schema)
    if case["workflow_state"] not in model["states"]:
        raise ValueError("case workflow state is not registered")
    if case["source_boundary"]["status"] != "valid":
        raise ValueError("fixture case source boundary must be valid")
    matching_phases = [
        phase for phase, states in model["display_phases"].items()
        if case["workflow_state"] in states
    ]
    if matching_phases != [case["display_phase"]]:
        raise ValueError("fixture display phase must match the controller state projection")
    authority = case["authority"]
    owner_capable_roles = role_ids | {"@case_owner"}
    for role_field in ("requester_role", "accountable_owner_role", "maker_role", "reviewer_role"):
        if authority[role_field] not in owner_capable_roles:
            raise ValueError(f"case {role_field} is not a registered role")
    if authority["requester_role"] == "@case_owner" or authority["maker_role"] == "@case_owner" or authority["reviewer_role"] == "@case_owner":
        raise ValueError("requester, maker, and reviewer must be canonical roles")
    if authority["maker_role"] == authority["reviewer_role"]:
        raise ValueError("case must preserve maker/reviewer separation")
    for allowed in authority["allowed_actions"]:
        if allowed["actor_role"] not in role_ids:
            raise ValueError("allowed action actor must be a canonical role")
    evidence_ids = {item["id"] for item in case["evidence"]}
    requirement_ids = {item["id"] for item in case["requirements"]}
    requirement_versions = {f"{item['id']}@{item['version']}" for item in case["requirements"]}
    if any(not item["exact_read"] for item in case["evidence"]):
        raise ValueError("fixture action evidence must record an exact source read")
    for claim in case["claims"]:
        if not set(claim["evidence_refs"]).issubset(evidence_ids):
            raise ValueError(f"claim {claim['id']} has unknown evidence")
        if not set(claim.get("counter_evidence_refs", [])).issubset(evidence_ids):
            raise ValueError(f"claim {claim['id']} has unknown counter-evidence")
        if claim["owner_role"] not in owner_capable_roles:
            raise ValueError(f"claim {claim['id']} has unknown owner")
    for evidence in case["evidence"]:
        if evidence["owner_role"] not in owner_capable_roles:
            raise ValueError(f"evidence {evidence['id']} has unknown owner")
    for requirement in case["requirements"]:
        if not set(requirement["evidence_refs"]).issubset(evidence_ids):
            raise ValueError(f"requirement {requirement['id']} has unknown evidence")
        if requirement["reviewer_role"] not in role_ids:
            raise ValueError(f"requirement {requirement['id']} has unknown reviewer")
        if requirement["owner_role"] not in owner_capable_roles:
            raise ValueError(f"requirement {requirement['id']} has unknown owner")
        if "superseded_by" in requirement and requirement["superseded_by"] not in requirement_ids:
            raise ValueError(f"requirement {requirement['id']} has unknown supersession target")
    for task in case["tasks"]:
        if not set(task["requirement_refs"]).issubset(requirement_versions):
            raise ValueError(f"task {task['id']} has unknown requirement versions")
        if task["owner_role"] not in role_ids or task["reviewer_role"] not in role_ids:
            raise ValueError(f"task {task['id']} uses an unknown role")
        if task["owner_role"] == task["reviewer_role"]:
            raise ValueError(f"task {task['id']} violates maker/reviewer separation")
    for contradiction in case["contradictions"]:
        if contradiction["owner_role"] not in owner_capable_roles:
            raise ValueError(f"contradiction {contradiction['id']} has unknown owner")
        if contradiction["state"] == "open" and case["workflow_state"] in {"execution_ready", "executed", "accepted_result"}:
            raise ValueError("an open contradiction cannot advance to execution or acceptance")
    for collection in ("decisions", "gaps", "approvals"):
        for item in case[collection]:
            if item["owner_role"] not in owner_capable_roles:
                raise ValueError(f"{collection} item {item['id']} has unknown owner")
    if case["review"]["maker_role"] not in role_ids or case["review"]["reviewer_role"] not in role_ids:
        raise ValueError("case review uses an unknown role")
    if case["review"]["maker_role"] == case["review"]["reviewer_role"]:
        raise ValueError("case review cannot be self-review")
    if case["knowledge"]["freshness_owner"] not in owner_capable_roles:
        raise ValueError("case knowledge freshness owner is unknown")

    workflows = load("contracts/role-workflows.json")
    base_roles, expected_roles = expected_case_roles(case, workflows, catalog)
    bindings = case["role_task_bindings"]
    bound_roles = {binding["role_id"] for binding in bindings}
    if len(bound_roles) != len(bindings) or bound_roles != expected_roles:
        raise ValueError("case bindings must exactly equal the base pack plus deterministic review closure")
    owned_outputs: set[str] = set()
    for binding in bindings:
        validate_role_binding(binding, binding_schema, case, catalog, role_ids)
        expected_kind = "base" if binding["role_id"] in base_roles else "review_closure"
        if binding["base_or_closure"] != expected_kind:
            raise ValueError(f"binding {binding['binding_id']} has the wrong base/closure label")
        if binding["owned_output"] in owned_outputs:
            raise ValueError(f"case has duplicate output ownership: {binding['owned_output']}")
        owned_outputs.add(binding["owned_output"])


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
    case_schema, proposal_schema, binding_schema, catalog, role_ids = validate_contracts()
    crew_proof = validate_knowledge_crew()
    model = load("contracts/operating-model.json")
    case = load("fixtures/onboarding-case.json")
    validate_case(case, case_schema, binding_schema, model, catalog, role_ids)

    bad_state = copy.deepcopy(case)
    bad_state["workflow_state"] = "unknown_parallel_state"
    expect_rejected("unknown workflow state", lambda: validate_instance(bad_state, case_schema))
    binding_seed = case["role_task_bindings"][0]
    bad_role = copy.deepcopy(binding_seed)
    bad_role["role_id"] = "unknown_role"
    expect_rejected("unknown binding role", lambda: validate_role_binding(bad_role, binding_schema, case, catalog, role_ids))
    bad_call_name = copy.deepcopy(binding_seed)
    bad_call_name["call_name"] = "NotTaras"
    expect_rejected("binding call-name drift", lambda: validate_role_binding(bad_call_name, binding_schema, case, catalog, role_ids))
    bad_authority = copy.deepcopy(binding_seed)
    bad_authority["permission_boundary"]["authority_ref"] = "case.role_override"
    expect_rejected("binding authority spoof", lambda: validate_role_binding(bad_authority, binding_schema, case, catalog, role_ids))
    bad_self_review = copy.deepcopy(binding_seed)
    bad_self_review["reviewer_route"] = [bad_self_review["role_id"], "@case_owner"]
    bad_self_review["handoff"]["to"] = bad_self_review["role_id"]
    expect_rejected("binding self review", lambda: validate_role_binding(bad_self_review, binding_schema, case, catalog, role_ids))
    bad_handoff_payload = copy.deepcopy(binding_seed)
    bad_handoff_payload["handoff"]["payload"].append("unknown_payload_field")
    expect_rejected(
        "unknown handoff payload field",
        lambda: validate_role_binding(bad_handoff_payload, binding_schema, case, catalog, role_ids),
    )

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
        "canonical_role_bindings": len(case["role_task_bindings"]),
        "negative_role_state_fixtures": 6,
        "malformed_fixture": "rejected",
        "target_escape_schema": "rejected",
        "knowledge_crew": crew_proof,
        "results": [eligible, blocked, spoof, target_escape, reviewer_spoof],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
