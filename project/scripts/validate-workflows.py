#!/usr/bin/env python3
"""Validate ArchFlow public workflow configuration files."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field, ValidationError, field_validator


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"


PRIVATE_PATTERNS = {
    "local_home_path": re.compile(re.escape("/" + "Users/")),
    "private_workspace_owner": re.compile(re.escape("get" + "apple")),
    "private_notion_url": re.compile(re.escape("app" + ".notion" + ".com")),
    "nonempty_secret_env": re.compile(
        r"(?m)^[ \t]*(?:LANGSMITH_API_KEY|OPENAI_API_KEY|ANTHROPIC_API_KEY|"
        r"GITHUB_TOKEN|GH_TOKEN|AWS_SECRET_ACCESS_KEY)[ \t]*=[ \t]*['\"]?[^'\"\s#]+"
    ),
}


class NamedYaml(BaseModel):
    name: str
    status: str
    runtime: str | None = None
    purpose: str

    @field_validator("name", "status")
    @classmethod
    def no_blanks(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("value must not be blank")
        return value


class LangGraphWorkflow(NamedYaml):
    runtime: str
    state_schema: dict[str, Any]
    nodes: dict[str, dict[str, Any]]
    edges: list[dict[str, Any]]
    current_parameters: dict[str, Any]

    @field_validator("nodes")
    @classmethod
    def required_nodes_present(cls, value: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
        required = {"admit_case", "assemble_perception", "validate_action", "independent_review", "readback_result", "close_case"}
        missing = sorted(required.difference(value))
        if missing:
            raise ValueError(f"missing required nodes: {', '.join(missing)}")
        return value


class LlamaIndexWorkflow(NamedYaml):
    runtime: str
    approved_corpus: dict[str, list[str]]
    indexing_parameters: dict[str, Any]
    retrieval_parameters: dict[str, Any]
    outputs: dict[str, str]

    @field_validator("approved_corpus")
    @classmethod
    def corpus_has_include_and_exclude(cls, value: dict[str, list[str]]) -> dict[str, list[str]]:
        if not value.get("include"):
            raise ValueError("approved corpus include list is required")
        if not value.get("exclude"):
            raise ValueError("approved corpus exclude list is required")
        return value


class CrewWorkflow(NamedYaml):
    runtime: str
    process: str
    agents: dict[str, dict[str, Any]]
    tasks: list[dict[str, Any]]

    @field_validator("agents")
    @classmethod
    def required_agents_present(cls, value: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
        required = {
            "admission_controller", "source_and_context_operator",
            "requirements_and_market_research", "onboarding_guide",
            "designer", "action_validator", "independent_reviewer",
            "knowledge_librarian", "integrator", "surface_projection_operator",
        }
        missing = sorted(required.difference(value))
        if missing:
            raise ValueError(f"missing required agents: {', '.join(missing)}")
        return value


class KnowledgeIntegration(NamedYaml):
    operator: dict[str, Any]
    knowledge_layers: dict[str, dict[str, Any]]
    runtime_layers: dict[str, dict[str, Any]]
    execution_path: list[str]
    hard_rules: list[str]


class ModelRouting(BaseModel):
    provider_mode: str
    providers: dict[str, dict[str, Any]]
    routing: dict[str, str]

    @field_validator("providers")
    @classmethod
    def required_providers_present(cls, value: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
        required = {"codex_operator", "ollama_local", "cloud_api", "langsmith_observability"}
        missing = sorted(required.difference(value))
        if missing:
            raise ValueError(f"missing required providers: {', '.join(missing)}")
        return value


def load_yaml(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    for name, pattern in PRIVATE_PATTERNS.items():
        if pattern.search(text):
            raise ValueError(f"{path.relative_to(ROOT)} contains blocked pattern: {name}")
    loaded = yaml.safe_load(text)
    if not isinstance(loaded, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a YAML mapping")
    return loaded


def validate_file(path: Path, model: type[BaseModel]) -> str:
    data = load_yaml(path)
    model.model_validate(data)
    return path.relative_to(ROOT).as_posix()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


def validate_canonical_projections() -> int:
    catalog = load_json(PROJECT / "system" / "contracts" / "role-catalog.json")
    crew_contract = load_json(PROJECT / "system" / "contracts" / "knowledge-crew-config.json")
    workflow_packs = load_json(PROJECT / "system" / "contracts" / "role-workflows.json")
    binding_schema = load_json(PROJECT / "system" / "schemas" / "role-task-binding.schema.json")
    crew_yaml = load_yaml(PROJECT / "workflows" / "crewai-crew.yaml")
    llama_yaml = load_yaml(PROJECT / "workflows" / "llamaindex-rag.yaml")

    role_map = {role["id"]: role for role in catalog["roles"]}
    if set(crew_yaml["agents"]) != set(role_map):
        raise ValueError("CrewAI agents must exactly equal the canonical role catalog")
    for role_id, agent in crew_yaml["agents"].items():
        role = role_map[role_id]
        if agent.get("call_name") != role["call_name"] or agent.get("role") != role["title"] or agent.get("goal") != role["goal"]:
            raise ValueError(f"CrewAI projection drifted for role {role_id}")
    required_task_fields = set(binding_schema.get("required", []))
    binding_properties = set(binding_schema.get("properties", {}))
    if required_task_fields != binding_properties:
        raise ValueError("canonical role binding must declare every property required for exact CrewAI projection")
    if set(crew_yaml.get("task_contract_required", [])) != required_task_fields:
        raise ValueError("CrewAI task contract must exactly match the canonical role binding fields")
    for pack in workflow_packs["packs"]:
        if not set(pack["roles"]).issubset(role_map):
            raise ValueError(f"workflow pack {pack['id']} uses a noncanonical role reference")

    llama_contract = crew_contract["frameworks"]["llamaindex"]
    for key in ("chunk_size", "chunk_overlap"):
        if llama_yaml["indexing_parameters"].get(key) != llama_contract["ingestion"][key]:
            raise ValueError(f"LlamaIndex {key} drifted from the canonical contract")
    retrieval_keys = {
        "lexical_top_k", "vector_top_k", "rerank_top_k", "final_source_limit",
        "require_source_paths", "require_exact_read_for_action", "refuse_private_match", "fallback_to_lexical",
    }
    for key in retrieval_keys:
        if llama_yaml["retrieval_parameters"].get(key) != llama_contract["retrieval"][key]:
            raise ValueError(f"LlamaIndex retrieval parameter {key} drifted")
    turbovec = crew_contract["frameworks"]["turbovec"]
    candidate = llama_yaml["vector_candidate"]
    if candidate["current_verdict"] != turbovec["current_evidence"]["verdict"] or candidate["bit_width"] != turbovec["bit_width"]:
        raise ValueError("TurboVec candidate status drifted from the canonical contract")
    for key in ("public_receipt", "queries", "checks", "candidate_recall_at_3", "candidate_mrr", "lexical_baseline", "verdict"):
        if candidate["isolated_evidence"].get(key) != turbovec["current_evidence"].get(key):
            raise ValueError(f"TurboVec isolated evidence drifted at {key}")
    if any(key in candidate["isolated_evidence"] for key in ("fixture_documents", "lexical_recall_at_3")):
        raise ValueError("TurboVec public projection contains unsupported comparison metrics")
    return len(required_task_fields)


def main() -> int:
    checks: list[tuple[Path, type[BaseModel]]] = [
        (PROJECT / "workflows" / "langgraph-controller.yaml", LangGraphWorkflow),
        (PROJECT / "workflows" / "llamaindex-rag.yaml", LlamaIndexWorkflow),
        (PROJECT / "workflows" / "crewai-crew.yaml", CrewWorkflow),
        (PROJECT / "workflows" / "knowledge-integration.yaml", KnowledgeIntegration),
        (PROJECT / "workflows" / "market-research-engine.yaml", NamedYaml),
        (PROJECT / "config" / "model-routing.yaml", ModelRouting),
    ]
    ok: list[str] = []
    for path, model in checks:
        if not path.exists():
            raise SystemExit(f"missing required config: {path.relative_to(ROOT)}")
        try:
            ok.append(validate_file(path, model))
        except (ValidationError, ValueError) as exc:
            raise SystemExit(f"validation failed for {path.relative_to(ROOT)}: {exc}") from exc

    try:
        binding_field_count = validate_canonical_projections()
    except ValueError as exc:
        raise SystemExit(f"canonical projection validation failed: {exc}") from exc

    skill = ROOT / "skills" / "archflow-task-breakdown" / "SKILL.md"
    guard_skill = ROOT / "skills" / "archflow-e1-runtime-guard" / "SKILL.md"
    handout_skill = ROOT / "skills" / "task-handout" / "SKILL.md"
    handout_hook = ROOT / ".codex" / "hooks.json"
    handout_script = PROJECT / "scripts" / "task-handout-hook.py"
    if not skill.exists():
        raise SystemExit("missing required skill: skills/archflow-task-breakdown/SKILL.md")
    if not guard_skill.exists():
        raise SystemExit("missing required skill: skills/archflow-e1-runtime-guard/SKILL.md")
    if not handout_skill.exists():
        raise SystemExit("missing required skill: skills/task-handout/SKILL.md")
    if not handout_hook.exists():
        raise SystemExit("missing required hook config: .codex/hooks.json")
    if not handout_script.exists():
        raise SystemExit("missing required hook script: project/scripts/task-handout-hook.py")

    print("workflow_validation=ok")
    print(f"crewai_role_binding_fields=exact:{binding_field_count}")
    print("canonical_role_task_and_retrieval_projection=ok")
    for rel_path in ok:
        print(f"validated={rel_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
