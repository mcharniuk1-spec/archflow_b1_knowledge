#!/usr/bin/env python3
"""Validate ArchFlow public workflow configuration files."""

from __future__ import annotations

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
        required = {"intake_validate", "review_gate", "publish_or_revise"}
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
        required = {"af_tools", "af_context", "af_manager", "af_knowledge", "af_review", "af_publisher"}
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


def main() -> int:
    checks: list[tuple[Path, type[BaseModel]]] = [
        (PROJECT / "workflows" / "langgraph-controller.yaml", LangGraphWorkflow),
        (PROJECT / "workflows" / "llamaindex-rag.yaml", LlamaIndexWorkflow),
        (PROJECT / "workflows" / "crewai-crew.yaml", CrewWorkflow),
        (PROJECT / "workflows" / "knowledge-integration.yaml", KnowledgeIntegration),
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
    for rel_path in ok:
        print(f"validated={rel_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
