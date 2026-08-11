#!/usr/bin/env python3
"""Validate the portable, provider-disabled ArchFlow workflow contracts."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, ValidationError, field_validator


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
MANIFEST_PATH = PROJECT / "dashboard" / "corpus-manifest.json"
ROLE_CATALOG_PATH = PROJECT / "database" / "role-catalog.json"
AGENT_ROSTER_PATH = PROJECT / "agents" / "agent-roster.yaml"
ROLE_PACKS_PATH = PROJECT / "agents" / "actionable-role-packs.json"

PRIVATE_PATTERNS = {
    "absolute_home_path": re.compile(r"/(?:Users|home)/[^/\s]+/"),
    "absolute_windows_home": re.compile(r"(?i)\b[A-Z]:\\Users\\[^\\\s]+\\"),
    "nonempty_secret_assignment": re.compile(
        r"(?mi)^[ \t]*(?:[A-Z0-9_]*(?:API_KEY|TOKEN|PASSWORD|SECRET|COOKIE))[ \t]*"
        r"=[ \t]*['\"]?[^'\"\s#]+"
    ),
}


class NamedYaml(BaseModel):
    name: str
    status: str
    purpose: str
    runtime: str | None = None

    @field_validator("name", "status", "purpose")
    @classmethod
    def no_blanks(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("value must not be blank")
        return value


class LangGraphWorkflow(NamedYaml):
    runtime: str
    state_schema: dict[str, Any]
    experience_projection: dict[str, Any]
    nodes: dict[str, dict[str, Any]]
    edges: list[dict[str, Any]]
    current_parameters: dict[str, Any]

    @field_validator("nodes")
    @classmethod
    def current_nodes_present(cls, value: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
        required = {
            "classify_execution",
            "intake_validate",
            "frame_objective",
            "retrieve_context",
            "ground_evidence",
            "design_execution",
            "execute_bounded_action",
            "verify_result",
            "review_gate",
            "remember_result",
            "route_outcome",
            "write_task_handout",
        }
        missing = sorted(required.difference(value))
        if missing:
            raise ValueError(f"missing current controller nodes: {', '.join(missing)}")
        return value


class LlamaIndexWorkflow(NamedYaml):
    runtime: str
    approved_corpus: dict[str, Any]
    indexing_parameters: dict[str, Any]
    retrieval_parameters: dict[str, Any]
    outputs: dict[str, str]

    @field_validator("approved_corpus")
    @classmethod
    def exact_manifest_required(cls, value: dict[str, Any]) -> dict[str, Any]:
        if value.get("manifest") != "project/dashboard/corpus-manifest.json":
            raise ValueError("approved corpus must use the exact dashboard corpus manifest")
        if str(value.get("manifest_schema_version")) != "3.0":
            raise ValueError("approved corpus manifest schema must be 3.0")
        if value.get("selection") != "manifest_entries_only":
            raise ValueError("approved corpus selection must be manifest_entries_only")
        return value


class CrewWorkflow(NamedYaml):
    runtime: str
    process: str
    agents: dict[str, dict[str, Any]]
    tasks: list[dict[str, Any]]
    execution_policy: dict[str, Any]

    @field_validator("agents")
    @classmethod
    def agents_must_not_be_empty(cls, value: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
        required = {"admission_controller", "implementation_maker", "independent_reviewer", "integrator"}
        missing = sorted(required.difference(value))
        if missing:
            raise ValueError(f"missing bounded crew roles: {', '.join(missing)}")
        return value

    @field_validator("tasks")
    @classmethod
    def tasks_must_not_be_empty(cls, value: list[dict[str, Any]]) -> list[dict[str, Any]]:
        if not value:
            raise ValueError("at least one task contract is required")
        return value


class KnowledgeIntegration(NamedYaml):
    operator: dict[str, Any]
    knowledge_layers: dict[str, dict[str, Any]]
    runtime_layers: dict[str, dict[str, Any]]
    execution_path: list[str]
    hard_rules: list[str]

    @field_validator("knowledge_layers")
    @classmethod
    def memory_layers_present(cls, value: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
        required = {"working_state", "solution_memory", "action_memory"}
        missing = sorted(required.difference(value))
        if missing:
            raise ValueError(f"missing memory layers: {', '.join(missing)}")
        return value

    @field_validator("runtime_layers")
    @classmethod
    def runtime_layers_present(cls, value: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
        required = {"langgraph", "llamaindex", "crewai"}
        missing = sorted(required.difference(value))
        if missing:
            raise ValueError(f"missing runtime layers: {', '.join(missing)}")
        return value


def checked_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    for name, pattern in PRIVATE_PATTERNS.items():
        if pattern.search(text):
            raise ValueError(f"{path.relative_to(ROOT)} contains blocked pattern: {name}")
    return text


def load_yaml(path: Path) -> dict[str, Any]:
    loaded = yaml.safe_load(checked_text(path))
    if not isinstance(loaded, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a YAML mapping")
    return loaded


def load_json(path: Path) -> dict[str, Any]:
    loaded = json.loads(checked_text(path))
    if not isinstance(loaded, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return loaded


def validate_file(path: Path, model: type[BaseModel]) -> tuple[str, dict[str, Any]]:
    data = load_yaml(path)
    model.model_validate(data)
    return path.relative_to(ROOT).as_posix(), data


def validate_manifest() -> list[str]:
    manifest = load_json(MANIFEST_PATH)
    if str(manifest.get("schema_version")) != "3.0":
        raise ValueError("project/dashboard/corpus-manifest.json schema_version must be 3.0")
    files = manifest.get("files")
    if not isinstance(files, list) or not files or not all(isinstance(item, str) for item in files):
        raise ValueError("dashboard corpus manifest files must be a non-empty string list")
    if len(files) != len(set(files)):
        raise ValueError("dashboard corpus manifest contains duplicate paths")
    for value in files:
        rel = Path(value)
        if rel.is_absolute() or ".." in rel.parts:
            raise ValueError(f"dashboard corpus manifest contains unsafe path: {value}")
        if not (ROOT / rel).is_file():
            raise ValueError(f"dashboard corpus manifest path is missing: {value}")
    return files


def canonical_role_ids() -> set[str]:
    catalog = load_json(ROLE_CATALOG_PATH)
    roles = catalog.get("roles")
    if not isinstance(roles, list) or not roles:
        raise ValueError("role catalog must contain roles")
    ids = [role.get("id") for role in roles if isinstance(role, dict)]
    if len(ids) != len(roles) or any(not isinstance(role_id, str) or not role_id for role_id in ids):
        raise ValueError("role catalog IDs must be non-empty strings")
    if len(ids) != len(set(ids)):
        raise ValueError("role catalog IDs must be unique")
    return set(ids)


def validate_role_closure(
    role_ids: set[str], langgraph: dict[str, Any], crew: dict[str, Any]
) -> tuple[int, int]:
    roster = load_yaml(AGENT_ROSTER_PATH)
    roster_agents = roster.get("agents")
    if not isinstance(roster_agents, dict):
        raise ValueError("agent roster must contain an agents mapping")
    roster_ids = set(roster_agents)
    if roster_ids != role_ids:
        missing = sorted(role_ids.difference(roster_ids))
        extra = sorted(roster_ids.difference(role_ids))
        raise ValueError(f"role catalog/roster mismatch; missing={missing} extra={extra}")

    crew_agents = crew.get("agents") or {}
    unknown_crew = sorted(set(crew_agents).difference(role_ids))
    if unknown_crew:
        raise ValueError(f"CrewAI config contains unknown roles: {', '.join(unknown_crew)}")
    unknown_task_roles = sorted(
        {
            task.get("agent")
            for task in crew.get("tasks", [])
            if task.get("agent") and task.get("agent") not in role_ids
        }
    )
    if unknown_task_roles:
        raise ValueError(f"CrewAI tasks reference unknown roles: {', '.join(unknown_task_roles)}")

    nodes = langgraph.get("nodes") or {}
    unknown_node_roles = sorted(
        {
            node.get("owner_agent")
            for node in nodes.values()
            if isinstance(node, dict)
            and node.get("owner_agent")
            and node.get("owner_agent") not in role_ids
        }
    )
    if unknown_node_roles:
        raise ValueError(f"LangGraph nodes reference unknown roles: {', '.join(unknown_node_roles)}")

    node_ids = set(nodes)
    for edge in langgraph.get("edges", []):
        if not isinstance(edge, dict):
            raise ValueError("LangGraph edges must be mappings")
        source = edge.get("from")
        target = edge.get("to")
        if source not in node_ids | {"START"}:
            raise ValueError(f"LangGraph edge has unknown source: {source}")
        if target not in node_ids | {"END"}:
            raise ValueError(f"LangGraph edge has unknown target: {target}")

    role_packs = load_json(ROLE_PACKS_PATH)
    for pack in role_packs.get("packs", []):
        if not isinstance(pack, dict):
            raise ValueError("role packs must be objects")
        referenced = set(pack.get("role_ids", []))
        referenced.update(pack.get("maker_role_ids", []))
        reviewer = pack.get("reviewer_role_id")
        if reviewer:
            referenced.add(reviewer)
        unknown = sorted(referenced.difference(role_ids))
        if unknown:
            raise ValueError(
                f"role pack {pack.get('id', '<unknown>')} references unknown roles: {', '.join(unknown)}"
            )
    return len(roster_ids), len(crew_agents)


def validate_skill_closure(manifest_files: list[str]) -> int:
    packaged_paths = sorted(
        value for value in manifest_files if value.startswith("skills/") and value.endswith("/SKILL.md")
    )
    if not packaged_paths:
        raise ValueError("dashboard corpus manifest must include packaged skills")
    packaged_ids = {Path(value).parent.name for value in packaged_paths}
    if len(packaged_ids) != len(packaged_paths):
        raise ValueError("packaged skill IDs must be unique")

    catalog = load_json(ROLE_CATALOG_PATH)
    referenced: set[str] = set()
    for role in catalog.get("roles", []):
        if isinstance(role, dict):
            referenced.update(str(item) for item in role.get("public_skill_packages", []))
    missing = sorted(referenced.difference(packaged_ids))
    if missing:
        raise ValueError(f"role catalog references unpackaged public skills: {', '.join(missing)}")
    return len(packaged_ids)


def run_negative_assertions() -> int:
    cases: list[tuple[str, type[BaseModel], dict[str, Any]]] = [
        (
            "old_manifest_schema",
            LlamaIndexWorkflow,
            {
                "name": "fixture",
                "status": "configured",
                "runtime": "local",
                "purpose": "negative fixture",
                "approved_corpus": {
                    "manifest": "project/dashboard/corpus-manifest.json",
                    "manifest_schema_version": "1.0",
                    "selection": "manifest_entries_only",
                },
                "indexing_parameters": {},
                "retrieval_parameters": {},
                "outputs": {},
            },
        ),
        (
            "missing_review_node",
            LangGraphWorkflow,
            {
                "name": "fixture",
                "status": "configured",
                "runtime": "local",
                "purpose": "negative fixture",
                "state_schema": {},
                "experience_projection": {},
                "nodes": {"intake_validate": {}},
                "edges": [],
                "current_parameters": {},
            },
        ),
        (
            "missing_independent_review_role",
            CrewWorkflow,
            {
                "name": "fixture",
                "status": "configured",
                "runtime": "local",
                "purpose": "negative fixture",
                "process": "sequential",
                "agents": {"implementation_maker": {}},
                "tasks": [{"id": "execute", "agent": "implementation_maker"}],
                "execution_policy": {},
            },
        ),
    ]
    for name, model, fixture in cases:
        try:
            model.model_validate(fixture)
        except ValidationError:
            continue
        print(f"negative_assertion_failed={name}")
        return 1
    print(f"workflow_negative_assertions=ok cases={len(cases)}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    return parser.parse_args()


def main() -> int:
    if parse_args().self_test:
        return run_negative_assertions()

    checks: list[tuple[Path, type[BaseModel]]] = [
        (PROJECT / "workflows" / "langgraph-controller.yaml", LangGraphWorkflow),
        (PROJECT / "workflows" / "llamaindex-rag.yaml", LlamaIndexWorkflow),
        (PROJECT / "workflows" / "crewai-crew.yaml", CrewWorkflow),
        (PROJECT / "workflows" / "knowledge-integration.yaml", KnowledgeIntegration),
    ]
    validated: list[str] = []
    data: dict[str, dict[str, Any]] = {}
    for path, model in checks:
        if not path.is_file():
            raise SystemExit(f"missing required config: {path.relative_to(ROOT)}")
        try:
            rel_path, parsed = validate_file(path, model)
        except (ValidationError, ValueError) as exc:
            raise SystemExit(f"validation failed for {path.relative_to(ROOT)}: {exc}") from exc
        validated.append(rel_path)
        data[rel_path] = parsed

    try:
        manifest_files = validate_manifest()
        role_ids = canonical_role_ids()
        roster_count, crew_count = validate_role_closure(
            role_ids,
            data["project/workflows/langgraph-controller.yaml"],
            data["project/workflows/crewai-crew.yaml"],
        )
        skill_count = validate_skill_closure(manifest_files)
    except (json.JSONDecodeError, yaml.YAMLError, ValueError) as exc:
        raise SystemExit(f"closure validation failed: {exc}") from exc

    print(f"workflow_validation=ok workflows={len(validated)}")
    print(f"role_closure=ok canonical={len(role_ids)} roster={roster_count} crew={crew_count}")
    print(f"skill_closure=ok packaged={skill_count}")
    for rel_path in validated:
        print(f"validated={rel_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
