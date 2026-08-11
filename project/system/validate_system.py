#!/usr/bin/env python3
"""Deterministic, provider-disabled validation for the public ArchFlow V3 core."""

from __future__ import annotations

import copy
import json
import re
from datetime import datetime, timedelta
from pathlib import Path, PurePosixPath
from typing import Any, Callable


SYSTEM = Path(__file__).resolve().parent
REPO = SYSTEM.parent.parent
STATES = ["frame", "ground", "design", "execute", "verify", "remember", "handoff"]
SCHEMA_FILES = {
    "knowledge-case.schema.json": SYSTEM / "schemas/knowledge-case.schema.json",
    "role-task-binding.schema.json": SYSTEM / "schemas/role-task-binding.schema.json",
    "action-proposal.schema.json": SYSTEM / "schemas/action-proposal.schema.json",
}
SUPPORTED_SCHEMA_KEYS = {
    "$schema", "$id", "$ref", "title", "type", "required", "properties",
    "items", "additionalProperties", "const", "enum", "pattern", "minLength",
    "minItems",
}
TYPE_CHECKS = {"object": dict, "array": list, "string": str, "boolean": bool}
MAX_SCHEMA_DEPTH = 24
MAX_INSTANCE_DEPTH = 32
MAX_COLLECTION_ITEMS = 256
MAX_STRING_LENGTH = 20_000
EXTERNAL_TARGETS = {"external_communication", "deployment", "production", "credential_store"}
EXTERNAL_EFFECTS = {"external_message", "deployment", "production_change", "credential_write"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle, object_pairs_hook=strict_object)
    require(isinstance(value, dict), f"{path.name} must contain one JSON object")
    return value


def system_json(relative: str) -> dict[str, Any]:
    return read_json(SYSTEM / relative)


def repo_json(relative: str) -> dict[str, Any]:
    return read_json(REPO / relative)


SCHEMAS = {name: read_json(path) for name, path in SCHEMA_FILES.items()}


def validate_schema_definition(
    schema: dict[str, Any],
    path: str = "$",
    depth: int = 0,
    refs: tuple[str, ...] = (),
) -> None:
    require(depth <= MAX_SCHEMA_DEPTH, f"{path} exceeds the schema depth limit")
    unknown = set(schema) - SUPPORTED_SCHEMA_KEYS
    require(not unknown, f"{path} uses unsupported schema keywords: {sorted(unknown)}")
    if "$ref" in schema:
        require(set(schema) == {"$ref"}, f"{path} must not combine $ref with other keywords")
        reference = schema["$ref"]
        require(reference in SCHEMAS, f"{path} uses a non-local or unknown $ref")
        require(reference not in refs, f"{path} contains a schema-reference cycle")
        validate_schema_definition(SCHEMAS[reference], f"{path}->$ref", depth + 1, refs + (reference,))
        return
    expected_type = schema.get("type")
    require(expected_type is None or expected_type in TYPE_CHECKS, f"{path} has an unsupported type")
    if expected_type == "object":
        require(schema.get("additionalProperties") is False, f"{path} object must fail closed")
        properties = schema.get("properties")
        require(isinstance(properties, dict), f"{path}.properties must be an object")
        required = schema.get("required", [])
        require(isinstance(required, list) and all(isinstance(item, str) for item in required), f"{path}.required must be string array")
        require(len(required) == len(set(required)), f"{path}.required contains duplicates")
        require(set(required).issubset(properties), f"{path}.required references undefined properties")
        for key, child in properties.items():
            require(isinstance(child, dict), f"{path}.{key} must be a schema object")
            validate_schema_definition(child, f"{path}.{key}", depth + 1, refs)
    else:
        require("properties" not in schema and "required" not in schema and "additionalProperties" not in schema, f"{path} has object-only keywords")
    if expected_type == "array":
        items = schema.get("items")
        require(isinstance(items, dict), f"{path}.items must be a bounded schema")
        validate_schema_definition(items, f"{path}[]", depth + 1, refs)
    else:
        require("items" not in schema and "minItems" not in schema, f"{path} has array-only keywords")
    if "pattern" in schema:
        require(expected_type == "string", f"{path}.pattern requires string type")
        re.compile(schema["pattern"])
    if "minLength" in schema:
        require(expected_type == "string" and isinstance(schema["minLength"], int) and schema["minLength"] >= 0, f"{path}.minLength is invalid")
    if "minItems" in schema:
        require(isinstance(schema["minItems"], int) and 0 <= schema["minItems"] <= MAX_COLLECTION_ITEMS, f"{path}.minItems is invalid")
    if "enum" in schema:
        enum = schema["enum"]
        require(isinstance(enum, list) and enum, f"{path}.enum must be a non-empty array")
        require(len(enum) == len({json.dumps(item, sort_keys=True) for item in enum}), f"{path}.enum contains duplicates")


def validate_instance(value: Any, schema: dict[str, Any], path: str = "$", depth: int = 0) -> None:
    require(depth <= MAX_INSTANCE_DEPTH, f"{path} exceeds the instance depth limit")
    if "$ref" in schema:
        validate_instance(value, SCHEMAS[schema["$ref"]], path, depth + 1)
        return
    expected_type = schema.get("type")
    if expected_type:
        require(isinstance(value, TYPE_CHECKS[expected_type]), f"{path} must be {expected_type}")
    if "const" in schema:
        require(value == schema["const"] and type(value) is type(schema["const"]), f"{path} must equal {schema['const']!r}")
    if "enum" in schema:
        require(value in schema["enum"], f"{path} is outside the declared enum")
    if isinstance(value, str):
        require(len(value) <= MAX_STRING_LENGTH, f"{path} exceeds the string limit")
        require(len(value) >= schema.get("minLength", 0), f"{path} is shorter than minLength")
        if "pattern" in schema:
            require(re.search(schema["pattern"], value) is not None, f"{path} does not match its pattern")
    if isinstance(value, list):
        require(len(value) <= MAX_COLLECTION_ITEMS, f"{path} exceeds the array limit")
        require(len(value) >= schema.get("minItems", 0), f"{path} has too few items")
        for index, item in enumerate(value):
            validate_instance(item, schema["items"], f"{path}[{index}]", depth + 1)
    if isinstance(value, dict):
        require(len(value) <= MAX_COLLECTION_ITEMS, f"{path} exceeds the object limit")
        properties = schema["properties"]
        missing = [key for key in schema.get("required", []) if key not in value]
        require(not missing, f"{path} is missing required properties: {missing}")
        extra = sorted(set(value) - set(properties))
        require(not extra, f"{path} has additional properties: {extra}")
        for key, item in value.items():
            validate_instance(item, properties[key], f"{path}.{key}", depth + 1)


def expect_rejected(label: str, action: Callable[[], None]) -> None:
    try:
        action()
    except (ValueError, KeyError, TypeError):
        return
    raise ValueError(f"negative mutation unexpectedly passed: {label}")


def safe_relative_path(value: str) -> bool:
    path = PurePosixPath(value)
    return bool(value) and not path.is_absolute() and ".." not in path.parts and "\\" not in value


def goal_required_types() -> dict[str, str]:
    schema_path = REPO / "project/goals/goal-state.schema.yaml"
    required: dict[str, str] = {}
    in_required_fields = False
    for line in schema_path.read_text(encoding="utf-8").splitlines():
        if line == "required_fields:":
            in_required_fields = True
            continue
        if in_required_fields and line and not line.startswith(" "):
            break
        if not in_required_fields or not line.strip():
            continue
        match = re.fullmatch(r"  ([a-z][a-z0-9_]*): ([a-z0-9_]+)", line)
        require(match is not None, "goal schema required_fields must use one scalar type per field")
        key, value_type = match.groups()
        require(key not in required, f"duplicate goal schema field: {key}")
        required[key] = value_type
    require(required, "goal schema required_fields are missing")
    return required


def goal_template_entries(text: str) -> dict[str, tuple[str, str]]:
    lines = text.splitlines()
    entries: dict[str, tuple[str, str]] = {}
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        match = re.fullmatch(r"([a-z][a-z0-9_]*):(.*)", line)
        require(match is not None, f"goal template line {index + 1} must start a top-level field")
        key, raw_inline = match.groups()
        require(key not in entries, f"duplicate goal template field: {key}")
        inline = raw_inline.strip()
        child_lines: list[str] = []
        cursor = index + 1
        while cursor < len(lines) and not re.fullmatch(r"[a-z][a-z0-9_]*:.*", lines[cursor]):
            if lines[cursor].strip() and not lines[cursor].lstrip().startswith("#"):
                child_lines.append(lines[cursor])
            cursor += 1
        if inline == "[]":
            shape = "list"
        elif inline:
            shape = "scalar"
        else:
            require(child_lines, f"goal template field {key} must not be empty")
            if all(re.fullmatch(r"  - .+", child) for child in child_lines):
                shape = "list"
            elif all(re.fullmatch(r"  [a-z][a-z0-9_]*:.*", child) for child in child_lines):
                shape = "mapping"
            else:
                raise ValueError(f"goal template field {key} has an unsupported YAML shape")
        entries[key] = (shape, inline)
        index = cursor
    return entries


def validate_goal_template(text: str) -> None:
    required = goal_required_types()
    entries = goal_template_entries(text)
    require(set(entries) == set(required), "goal template fields must exactly match goal-state.schema.yaml")
    scalar_types = {
        "string", "iso_datetime", "integer_or_unset", "number",
        "proven_review_planned_blocked_superseded",
        "draft_ready_running_verifying_complete_blocked_paused_superseded_cancelled",
    }
    for key, value_type in required.items():
        shape, inline = entries[key]
        if value_type == "list":
            require(shape == "list", f"goal template field {key} must be a list")
        elif value_type == "integer":
            require(shape == "scalar" and re.fullmatch(r"[0-9]+", inline) is not None, f"goal template field {key} must be an integer")
        else:
            require(value_type in scalar_types and shape == "scalar" and bool(inline), f"goal template field {key} must be a scalar {value_type}")
            if value_type == "integer_or_unset":
                require(inline == "unset" or re.fullmatch(r"[0-9]+", inline) is not None, f"goal template field {key} must be an integer or unset")
            if value_type == "number":
                require(re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", inline) is not None, f"goal template field {key} must be a non-negative number")
            if value_type == "iso_datetime":
                normalized = inline.strip("\"'")
                require(
                    re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", normalized) is not None,
                    f"goal template field {key} must be an explicit UTC ISO datetime",
                )
                try:
                    parsed = datetime.fromisoformat(normalized.replace("Z", "+00:00"))
                except ValueError as error:
                    raise ValueError(
                        f"goal template field {key} must be a valid calendar datetime"
                    ) from error
                require(
                    parsed.tzinfo is not None and parsed.utcoffset() == timedelta(0),
                    f"goal template field {key} must use UTC",
                )
    require(entries["evidence_state"][1] == "planned", "goal template evidence state must begin planned")
    require(entries["lifecycle_state"][1] == "draft", "goal template lifecycle must begin draft")


def validate_state_model(model: dict[str, Any]) -> None:
    require(model.get("schema_version") == "3.0", "operating model must use schema 3.0")
    require(model.get("states") == STATES, "controller states must be the exact ordered seven-state chain")
    transitions = model.get("transitions")
    require(isinstance(transitions, list) and len(transitions) == 6, "seven states require exactly six transitions")
    gates: list[str] = []
    for index, transition in enumerate(transitions):
        require(set(transition) == {"from", "to", "gate"}, "transition keys drifted")
        require(transition["from"] == STATES[index] and transition["to"] == STATES[index + 1], "transition order drifted")
        require(isinstance(transition["gate"], str) and transition["gate"], "every transition requires a gate")
        gates.append(transition["gate"])
    require(len(gates) == len(set(gates)), "transition gates must be unique")
    projected = [state for phase in model["experience_projection"].values() for state in phase]
    require(projected == STATES, "Research-Define-Act-Handoff projection must preserve state order")
    require(model.get("provider_default") == "none", "public provider default must be none")
    require(model.get("writeback_default") == "disabled", "public writeback default must be disabled")


def validate_skills(skill_catalog: dict[str, Any]) -> set[str]:
    items = skill_catalog.get("items")
    require(isinstance(items, list) and len(items) == 10 and skill_catalog.get("packaged_count") == 10, "public skill catalog must contain exactly ten packages")
    skill_ids = {item.get("id") for item in items}
    require(None not in skill_ids and len(skill_ids) == 10, "public skill IDs must be unique")
    for item in items:
        skill_id = item["id"]
        require(re.fullmatch(r"[a-z][a-z0-9-]*", skill_id) is not None, f"invalid skill ID: {skill_id}")
        require(item.get("path") == f"skills/{skill_id}/SKILL.md", f"skill {skill_id} has a non-portable path")
        skill_path = REPO / item["path"]
        require(skill_path.is_file() and not skill_path.is_symlink(), f"skill {skill_id} package is missing")
        require(len(skill_path.read_text(encoding="utf-8")) >= 100, f"skill {skill_id} package is empty")
        require(item.get("portable") is True and item.get("safe_to_share") is True, f"skill {skill_id} is not public-portable")
        require(re.fullmatch(r"[0-9a-f]{64}", item.get("content_sha256", "")) is not None, f"skill {skill_id} has an invalid content hash")
    return skill_ids


MODE_CEILINGS = {
    "read_draft_only": {"read_contracts", "read_allowlisted_sources", "query_bounded_retrieval", "query_structural_index", "draft_local_artifact", "run_deterministic_checks"},
    "local_mutation_exact_targets": {"read_contracts", "read_allowlisted_sources", "draft_local_artifact", "edit_claimed_targets", "run_deterministic_checks", "run_browser_qa", "write_run_receipt", "readback_exact_target"},
    "review_only_frozen_candidate": {"read_contracts", "read_allowlisted_sources", "run_deterministic_checks", "run_browser_qa", "write_review_verdict"},
    "verification_only_no_repair": {"read_contracts", "run_deterministic_checks", "run_browser_qa", "readback_exact_target"},
    "knowledge_candidate_only": {"read_contracts", "read_allowlisted_sources", "propose_knowledge_candidate", "readback_exact_target"},
    "browser_local_only": {"read_contracts", "run_browser_qa", "export_browser_packet"},
    "observation_only": {"read_contracts", "observe_runtime", "draft_local_artifact"},
    "external_action_exact_approval": {"read_contracts", "perform_exact_external_action", "readback_exact_target"},
    "git_action_exact_approval": {"read_contracts", "run_deterministic_checks", "perform_owner_approved_git_action", "readback_exact_target"},
}


def validate_roles(catalog: dict[str, Any], skill_catalog: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], set[str]]:
    require(catalog.get("schema_version") == "3.0.0", "canonical role catalog must use schema 3.0.0")
    roles = catalog.get("roles")
    require(isinstance(roles, list) and len(roles) == 21, "canonical role catalog must contain exactly 21 roles")
    skill_ids = validate_skills(skill_catalog)
    role_map = {role.get("id"): role for role in roles}
    require(None not in role_map and len(role_map) == 21, "canonical role IDs must be unique")
    tool_ids = set(catalog.get("tool_capabilities", {}))
    permission_modes = set(catalog.get("permission_modes", {}))
    require(permission_modes == set(MODE_CEILINGS), "permission mode registry drifted")
    require(tool_ids == set().union(*MODE_CEILINGS.values()), "tool registry and permission ceilings must close exactly")
    role_keys = {"id", "call_name", "title", "lane", "goal", "purpose", "owns", "forbidden", "task_defaults"}
    default_keys = {"inputs", "owned_output", "allowed_skills", "allowed_tools", "permission_mode", "reviewer_route", "handoff_to"}
    outputs: set[str] = set()
    calls: set[str] = set()
    used_skills: set[str] = set()
    for role_id, role in role_map.items():
        require(set(role) == role_keys, f"role {role_id} keys drifted")
        require(re.fullmatch(r"[a-z][a-z0-9_]*", role_id) is not None, f"invalid role ID: {role_id}")
        require(re.fullmatch(r"[A-Za-z]+", role["call_name"]) is not None and role["call_name"] not in calls, f"invalid or duplicate call name for {role_id}")
        calls.add(role["call_name"])
        defaults = role["task_defaults"]
        require(set(defaults) == default_keys, f"role {role_id} task-default keys drifted")
        require(defaults["owned_output"] not in outputs, f"owned output is not unique: {defaults['owned_output']}")
        outputs.add(defaults["owned_output"])
        skills = set(defaults["allowed_skills"])
        tools = set(defaults["allowed_tools"])
        require(len(skills) == len(defaults["allowed_skills"]) and skills.issubset(skill_ids), f"role {role_id} has invalid skills")
        require(len(tools) == len(defaults["allowed_tools"]) and tools.issubset(tool_ids), f"role {role_id} has invalid tools")
        used_skills.update(skills)
        mode = defaults["permission_mode"]
        require(tools.issubset(MODE_CEILINGS[mode]), f"role {role_id} exceeds its permission/tool ceiling")
        route = defaults["reviewer_route"]
        require(route and route[-1] == "@case_owner" and role_id not in route and len(route) == len(set(route)), f"role {role_id} has an invalid reviewer route")
        require(set(route[:-1]).issubset(role_map), f"role {role_id} reviewer route contains an unknown role")
        require(defaults["handoff_to"] == route[0], f"role {role_id} handoff does not match its reviewer route")
        if role["lane"] in {"reviewer", "validator", "verifier"}:
            require(not tools.intersection({"edit_claimed_targets", "perform_exact_external_action", "perform_owner_approved_git_action", "draft_local_artifact"}), f"review role {role_id} has a mutation tool")
    require(used_skills == skill_ids, "all and only the ten public skills must be referenced by canonical roles")
    for item in skill_catalog["items"]:
        require(set(item.get("recommended_role_ids", [])).issubset(role_map), f"skill {item['id']} recommends an unknown role")
    require(set(catalog.get("aliases", {}).values()).issubset(role_map), "every role alias must resolve canonically")

    graph = {role_id: role["task_defaults"]["reviewer_route"][:-1] for role_id, role in role_map.items()}
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(role_id: str) -> None:
        require(role_id not in visiting, f"reviewer-route cycle detected at {role_id}")
        if role_id in visited:
            return
        visiting.add(role_id)
        for target in graph[role_id]:
            visit(target)
        visiting.remove(role_id)
        visited.add(role_id)

    for role_id in graph:
        visit(role_id)
    return role_map, skill_ids


def validate_dashboard_projection(role_map: dict[str, dict[str, Any]], projection: dict[str, Any]) -> None:
    require(projection.get("path") == "project/system/contracts/role-catalog.json", "dashboard role projection must name its canonical source")
    rows = projection.get("roles")
    require(isinstance(rows, list) and len(rows) == 21, "dashboard must project exactly 21 roles")
    projected = {row.get("id"): row for row in rows}
    require(set(projected) == set(role_map), "dashboard and canonical role IDs must match exactly")
    for role_id, role in role_map.items():
        row = projected[role_id]
        defaults = role["task_defaults"]
        expected = {
            "title": role["title"],
            "lane": role["lane"],
            "goal": role["goal"],
            "purpose": role["purpose"],
            "outputs": role["owns"],
            "forbidden_actions": role["forbidden"],
            "public_skill_packages": defaults["allowed_skills"],
            "method_checklists": defaults["allowed_tools"],
            "permission_mode": defaults["permission_mode"],
            "reviewer_route": defaults["reviewer_route"],
        }
        for key, value in expected.items():
            require(row.get(key) == value, f"dashboard role projection drifted for {role_id}.{key}")
        require(row.get("skills") == row["public_skill_packages"] + row["method_checklists"], f"dashboard skill partition drifted for {role_id}")


def validate_packs(packs_doc: dict[str, Any], role_map: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    require(packs_doc.get("schema_version") == "3.0", "actionable packs must use schema 3.0")
    packs = packs_doc.get("packs")
    expected = {
        "research_to_decision": "research",
        "definition_to_task_graph": "define",
        "responsive_product_change": "act",
        "reviewed_memory_update": "remember",
    }
    require(isinstance(packs, list) and len(packs) == 4, "there must be exactly four actionable role packs")
    pack_map = {pack.get("id"): pack for pack in packs}
    require(set(pack_map) == set(expected), "actionable role pack IDs drifted")
    for pack_id, pack in pack_map.items():
        roles = pack["role_ids"]
        makers = pack["maker_role_ids"]
        reviewer = pack["reviewer_role_id"]
        require(pack["stage"] == expected[pack_id], f"pack {pack_id} stage drifted")
        require(roles and len(roles) == len(set(roles)) and set(roles).issubset(role_map), f"pack {pack_id} has invalid roles")
        require(makers and len(makers) == len(set(makers)) and set(makers).issubset(roles), f"pack {pack_id} has invalid makers")
        require(all(role_map[role_id]["lane"] == "maker" for role_id in makers), f"pack {pack_id} maker lane drifted")
        require(reviewer == "independent_reviewer" and reviewer in roles and reviewer not in makers, f"pack {pack_id} lacks maker/reviewer separation")
        require("admission_controller" in roles and "integrator" in roles, f"pack {pack_id} lacks control or integration")
        require(isinstance(pack.get("output"), str) and pack["output"] and isinstance(pack.get("stop"), str) and pack["stop"], f"pack {pack_id} lacks output or stop rule")
    return pack_map


def validate_manifest_and_crew(crew: dict[str, Any], model: dict[str, Any], role_map: dict[str, dict[str, Any]]) -> set[str]:
    require(crew.get("schema_version") == "3.0", "knowledge crew must use schema 3.0")
    controller = crew["controller"]
    require(controller["state_source"] == "project/system/contracts/operating-model.json", "knowledge crew state source drifted")
    require(controller["role_source"] == "project/system/contracts/role-catalog.json", "knowledge crew role source drifted")
    require(controller["role_pack_source"] == "project/agents/actionable-role-packs.json", "knowledge crew role-pack source drifted")
    require(controller["provider_default"] == "none" and controller["writeback_default"] == "disabled", "knowledge crew must remain provider- and writeback-disabled")
    layers = crew.get("layers")
    require(isinstance(layers, list) and [layer.get("id") for layer in layers] == [f"L{i}" for i in range(1, 8)], "knowledge crew must contain ordered layers L1-L7")
    for layer in layers:
        require(layer["primary_roles"] and set(layer["primary_roles"]).issubset(role_map), f"layer {layer['id']} has unknown roles")
    frameworks = crew["frameworks"]
    require(frameworks["langgraph"]["default"] == "provider_disabled" and frameworks["langgraph"]["checkpointer"] == "none", "LangGraph public default drifted")
    crewai = frameworks["crewai"]
    require(crewai["default"] == "contract_only" and crewai["memory"] is False and crewai["planning"] is False and crewai["delegation"] is False and crewai["maximum_parallel_tasks"] == 3, "CrewAI public ceiling drifted")
    retrieval = frameworks["llamaindex"]
    require(retrieval == {
        "role": "optional framework import around the exact-manifest retrieval contract",
        "default": "deterministic_lexical",
        "manifest": "project/dashboard/corpus-manifest.json",
        "chunk_size": 800,
        "chunk_overlap": 120,
        "top_k": 5,
        "require_source_path": True,
        "require_chunk_hash": True,
    }, "exact-manifest lexical retrieval contract drifted")
    jarvis = frameworks["jarvis"]
    require(jarvis["default"] == "provider_disabled" and jarvis["packet_in_url"] is False, "Jarvis must remain a provider-disabled local packet composer")

    manifest = repo_json(retrieval["manifest"])
    require(manifest.get("schema_version") == "3.0", "corpus manifest must use schema 3.0")
    files = manifest.get("files")
    require(isinstance(files, list) and files and len(files) == len(set(files)), "corpus manifest must be an exact unique file list")
    excluded = ("project/runs/", "project/reports/", "project/live/", "project/history/", "project/local/", "private/")
    for item in files:
        require(isinstance(item, str) and safe_relative_path(item) and not any(char in item for char in "*?[]"), f"unsafe manifest entry: {item!r}")
        require(not item.startswith(excluded), f"excluded source class entered manifest: {item}")
        source = REPO / item
        require(source.is_file() and not source.is_symlink() and source.resolve().is_relative_to(REPO.resolve()), f"manifest source is missing or escapes the repository: {item}")
    require(model["configuration_refs"]["knowledge_crew"] == "project/system/contracts/knowledge-crew-config.json", "operating model knowledge-crew route drifted")
    return set(files)


def validate_binding(binding: dict[str, Any], case: dict[str, Any], role_map: dict[str, dict[str, Any]], pack: dict[str, Any]) -> None:
    validate_instance(binding, SCHEMAS["role-task-binding.schema.json"])
    require(binding["case_id"] == case["case_id"] and binding["role_pack_id"] == pack["id"], "binding case or pack drifted")
    role = role_map.get(binding["role_id"])
    require(role is not None, "binding references an unknown role")
    defaults = role["task_defaults"]
    require(binding["owned_output"] == defaults["owned_output"], "binding output expands or changes canonical ownership")
    require(binding["allowed_skills"] == defaults["allowed_skills"], "binding skill ceiling drifted")
    require(binding["allowed_tools"] == defaults["allowed_tools"], "binding tool ceiling drifted")
    require(binding["permission_mode"] == defaults["permission_mode"], "binding permission mode drifted")
    expected_reviewer = "@case_owner" if binding["role_id"] == pack["reviewer_role_id"] else pack["reviewer_role_id"]
    require(binding["reviewer_role_id"] == expected_reviewer and binding["reviewer_role_id"] in defaults["reviewer_route"], "binding reviewer route drifted or self-review was introduced")
    require(binding["reviewer_role_id"] != binding["role_id"], "binding cannot self-review")
    target_modes = {"local_mutation_exact_targets", "external_action_exact_approval", "git_action_exact_approval"}
    require(bool(binding["exact_targets"]) == (binding["permission_mode"] in target_modes), "binding exact-target requirement drifted")
    require(all(safe_relative_path(target) for target in binding["exact_targets"]), "binding target escapes the public local boundary")


def validate_case(case: dict[str, Any], role_map: dict[str, dict[str, Any]], pack_map: dict[str, dict[str, Any]], manifest_files: set[str]) -> None:
    validate_instance(case, SCHEMAS["knowledge-case.schema.json"])
    require(case["workflow_state"] in STATES and case["source_boundary"]["status"] == "pass", "case must use an admitted canonical state")
    require(set(case["source_boundary"]["allowed_sources"]).issubset(manifest_files), "case source boundary exceeds the exact manifest")
    pack = pack_map.get(case["role_pack_id"])
    require(pack is not None, "case references an unknown actionable role pack")
    require(case["roles"]["makers"] == pack["maker_role_ids"], "case maker projection drifted from its role pack")
    require(case["roles"]["reviewer"] == pack["reviewer_role_id"] and case["roles"]["integrator"] == "integrator", "case review or integration role drifted")
    bindings = case["role_task_bindings"]
    bound_ids = [binding["role_id"] for binding in bindings]
    require(len(bound_ids) == len(set(bound_ids)) and set(bound_ids) == set(pack["role_ids"]), "case bindings must close exactly over the selected role pack")
    require(len({binding["owned_output"] for binding in bindings}) == len(bindings), "case bindings must preserve sole output ownership")
    for binding in bindings:
        validate_binding(binding, case, role_map, pack)
    requirement_refs = {f"{item['id']}@{item['version']}" for item in case["requirements"]}
    require(len(requirement_refs) == len(case["requirements"]), "case requirement versions must be unique")
    allowed_operations: set[str] = set()
    for action in case["authority"]["allowed_actions"]:
        require(action["actor_role"] in bound_ids, "case authority references an unbound actor")
        require(all(safe_relative_path(prefix) for prefix in action["target_prefixes"]), "case authority target prefix escapes")
        allowed_operations.add(action["operation"])
    require(allowed_operations.isdisjoint(case["authority"]["forbidden_operations"]), "case allowed and forbidden operations overlap")


def evaluate_proposal(case: dict[str, Any], proposal: dict[str, Any], role_map: dict[str, dict[str, Any]]) -> dict[str, Any]:
    reasons: set[str] = set()
    requirements = {f"{item['id']}@{item['version']}": item for item in case["requirements"]}
    if proposal["case_id"] != case["case_id"]:
        reasons.add("CASE_MISMATCH")
    if proposal["actor_role"] not in role_map:
        reasons.add("UNKNOWN_ACTOR_ROLE")
    if proposal["review"]["maker_role"] != proposal["actor_role"]:
        reasons.add("MAKER_ACTOR_MISMATCH")
    if proposal["review"]["reviewer_role"] not in role_map:
        reasons.add("UNKNOWN_REVIEWER_ROLE")
    if proposal["review"]["reviewer_role"] != case["roles"]["reviewer"]:
        reasons.add("CASE_REVIEWER_MISMATCH")
    if proposal["review"]["maker_role"] == proposal["review"]["reviewer_role"]:
        reasons.add("SELF_REVIEW")
    for reference in proposal["requirement_refs"]:
        requirement = requirements.get(reference)
        if requirement is None:
            reasons.add("UNKNOWN_REQUIREMENT")
        elif requirement["state"] != "approved":
            reasons.add("UNAPPROVED_REQUIREMENT")
    coverage = {item["requirement_ref"]: item["status"] for item in proposal["coverage"]}
    if len(coverage) != len(proposal["coverage"]) or set(coverage) != set(proposal["requirement_refs"]) or set(coverage.values()).intersection({"gap", "exception"}):
        reasons.add("REQUIREMENT_COVERAGE_INVALID")

    permission = proposal["permission_scope"]
    target_class = proposal["target"]["class"]
    target_ref = proposal["target"]["ref"]
    operation = permission["operation"]
    if permission["target_class"] != target_class:
        reasons.add("TARGET_CLASS_MISMATCH")
    matching = [
        action for action in case["authority"]["allowed_actions"]
        if action["actor_role"] == proposal["actor_role"]
        and action["operation"] == operation
        and action["target_class"] == target_class
    ]
    if len(matching) != 1 or operation in case["authority"]["forbidden_operations"]:
        reasons.add("OUT_OF_AUTHORITY")
    if not safe_relative_path(target_ref):
        reasons.add("TARGET_REF_INVALID")
    elif len(matching) == 1 and not any(target_ref.startswith(prefix) for prefix in matching[0]["target_prefixes"]):
        reasons.add("TARGET_OUTSIDE_ALLOWED_PREFIX")
    if permission["status"] != "allowed":
        reasons.add("PROPOSAL_PERMISSION_NOT_ALLOWED")

    external = target_class in EXTERNAL_TARGETS or bool(set(proposal["side_effects"]).intersection(EXTERNAL_EFFECTS))
    approval_required = external or (len(matching) == 1 and matching[0]["approval_required"])
    if proposal["approval"]["required"] != approval_required:
        reasons.add("APPROVAL_POLICY_MISMATCH")
    if approval_required and proposal["approval"]["status"] != "approved":
        reasons.add("TARGET_SPECIFIC_APPROVAL_MISSING")
    if any(proposal["effect_budget"].values()) or proposal["execute"] is not False:
        reasons.add("NONZERO_EFFECT_OR_EXECUTION")
    if proposal["verification_plan"]["readback"].strip().lower() in {"", "none", "none."}:
        reasons.add("READBACK_MISSING")
    if proposal["reversibility"] == "irreversible" and proposal["rollback"].lower().startswith("no reliable"):
        reasons.add("IRREVERSIBLE_WITHOUT_COMPENSATION")
    return {"proposal_id": proposal["proposal_id"], "verdict": "eligible" if not reasons else "blocked", "reasons": sorted(reasons), "executed": False}


def validate_proposals(case: dict[str, Any], role_map: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    schema = SCHEMAS["action-proposal.schema.json"]
    fixtures = {
        name: system_json(f"fixtures/action-proposal-{name}.json")
        for name in ("eligible", "blocked", "authority-spoof", "reviewer-spoof", "target-escape", "malformed")
    }
    for name in ("eligible", "blocked", "authority-spoof", "reviewer-spoof"):
        validate_instance(fixtures[name], schema)
    expect_rejected("target escape schema", lambda: validate_instance(fixtures["target-escape"], schema))
    expect_rejected("malformed proposal schema", lambda: validate_instance(fixtures["malformed"], schema))
    results = [evaluate_proposal(case, fixtures[name], role_map) for name in ("eligible", "blocked", "authority-spoof", "reviewer-spoof", "target-escape")]
    by_name = {result["proposal_id"]: result for result in results}
    require(by_name["proposal-onboarding-packet"]["verdict"] == "eligible", f"eligible proposal failed: {by_name['proposal-onboarding-packet']}")
    expected = {
        "proposal-onboarding-send": {"UNKNOWN_REQUIREMENT", "OUT_OF_AUTHORITY", "SELF_REVIEW", "PROPOSAL_PERMISSION_NOT_ALLOWED", "TARGET_SPECIFIC_APPROVAL_MISSING", "READBACK_MISSING"},
        "proposal-authority-spoof": {"UNKNOWN_ACTOR_ROLE", "UNKNOWN_REVIEWER_ROLE", "OUT_OF_AUTHORITY", "SELF_REVIEW", "APPROVAL_POLICY_MISMATCH", "TARGET_SPECIFIC_APPROVAL_MISSING"},
        "proposal-reviewer-spoof": {"CASE_REVIEWER_MISMATCH", "SELF_REVIEW"},
        "proposal-target-escape": {"TARGET_REF_INVALID"},
    }
    for proposal_id, required_reasons in expected.items():
        result = by_name[proposal_id]
        require(result["verdict"] == "blocked" and required_reasons.issubset(result["reasons"]), f"{proposal_id} did not fail closed: {result}")
    return results


def main() -> int:
    for name, schema in SCHEMAS.items():
        validate_schema_definition(schema, name, refs=(name,))
    model = system_json("contracts/operating-model.json")
    crew = system_json("contracts/knowledge-crew-config.json")
    catalog = system_json("contracts/role-catalog.json")
    skill_catalog = repo_json("project/database/skill-catalog.json")
    projection = repo_json("project/database/role-catalog.json")
    packs_doc = repo_json("project/agents/actionable-role-packs.json")
    validate_state_model(model)
    role_map, skill_ids = validate_roles(catalog, skill_catalog)
    validate_dashboard_projection(role_map, projection)
    pack_map = validate_packs(packs_doc, role_map)
    manifest_files = validate_manifest_and_crew(crew, model, role_map)
    case = system_json("fixtures/onboarding-case.json")
    validate_case(case, role_map, pack_map, manifest_files)
    results = validate_proposals(case, role_map)
    goal_template_text = (REPO / "project/goals/goal-template.yaml").read_text(encoding="utf-8")
    validate_goal_template(goal_template_text)

    bad_state = copy.deepcopy(case)
    bad_state["workflow_state"] = "parallel_unknown"
    expect_rejected("unknown case state", lambda: validate_instance(bad_state, SCHEMAS["knowledge-case.schema.json"]))
    bad_tool = copy.deepcopy(case["role_task_bindings"][0])
    bad_tool["allowed_tools"].append("perform_exact_external_action")
    expect_rejected("binding tool escalation", lambda: validate_binding(bad_tool, case, role_map, pack_map[case["role_pack_id"]]))
    bad_reviewer = copy.deepcopy(case["role_task_bindings"][1])
    bad_reviewer["reviewer_role_id"] = bad_reviewer["role_id"]
    expect_rejected("binding self review", lambda: validate_binding(bad_reviewer, case, role_map, pack_map[case["role_pack_id"]]))
    bad_case = copy.deepcopy(case)
    bad_case["roles"]["makers"].append("independent_reviewer")
    expect_rejected("reviewer inserted as maker", lambda: validate_case(bad_case, role_map, pack_map, manifest_files))
    bad_schema = {"type": "string", "format": "uri"}
    expect_rejected("unsupported schema keyword", lambda: validate_schema_definition(bad_schema))
    bad_goal_template = goal_template_text.replace("done_condition:", "done_conditions:", 1)
    expect_rejected("goal template field drift", lambda: validate_goal_template(bad_goal_template))
    bad_goal_timestamp = goal_template_text.replace('updated_at: "1970-01-01T00:00:00Z"', "updated_at: unset", 1)
    expect_rejected("goal template timestamp drift", lambda: validate_goal_template(bad_goal_timestamp))
    bad_goal_calendar = goal_template_text.replace('updated_at: "1970-01-01T00:00:00Z"', 'updated_at: "1970-13-40T25:61:61Z"', 1)
    expect_rejected("goal template impossible calendar", lambda: validate_goal_template(bad_goal_calendar))

    print(json.dumps({
        "status": "pass",
        "states": STATES,
        "transitions": 6,
        "knowledge_layers": 7,
        "canonical_roles": len(role_map),
        "public_skills": len(skill_ids),
        "actionable_role_packs": len(pack_map),
        "dashboard_role_projection": "exact",
        "retrieval": {"mode": "deterministic_lexical", "chunk_size": 800, "chunk_overlap": 120, "top_k": 5, "source_paths": True, "chunk_hashes": True},
        "case": {"id": case["case_id"], "bindings": len(case["role_task_bindings"]), "schema_version": case["schema_version"]},
        "goal_template": "schema_exact",
        "proposal_results": results,
        "negative_mutations": 13,
        "provider_calls": 0,
        "network_calls": 0,
        "external_writes": 0,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
