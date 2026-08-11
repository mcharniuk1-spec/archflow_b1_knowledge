#!/usr/bin/env python3
"""Generate the generic public ArchFlow Knowledge Operator payload.

The generator reads one exact manifest and a small set of canonical public
contracts. It never reads ignored files, environment values, Git metadata,
project runs, reports, conversations, local paths, or credential state.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
DASHBOARD = PROJECT / "dashboard"
MANIFEST_PATH = DASHBOARD / "corpus-manifest.json"
ROLE_CATALOG_PATH = PROJECT / "database" / "role-catalog.json"
SYSTEM_ROLE_CATALOG_PATH = PROJECT / "system" / "contracts" / "role-catalog.json"
ROLE_PACKS_PATH = PROJECT / "agents" / "actionable-role-packs.json"
PROVIDER_REGISTRY_PATH = PROJECT / "config" / "provider-registry.json"
BENCHMARK_PATH = PROJECT / "benchmarks" / "actionable-agents-v3-results.json"
SKILL_CATALOG_PATH = PROJECT / "database" / "skill-catalog.json"

SKILL_IDS = (
    "arcagcom",
    "archflow-agent-control",
    "archflow-architecture-operator",
    "archflow-e1-runtime-guard",
    "archflow-knowledge-service",
    "archflow-task-breakdown",
    "humanize-writing",
    "outquestions",
    "priority-task-operator",
    "task-handout",
)

SKILL_META = {
    "arcagcom": ("coordinate", "public-safe file claim, live update, and handoff"),
    "archflow-agent-control": ("define", "bounded role, task, gate, and proposed-artifact handoff"),
    "archflow-architecture-operator": ("define", "architecture, role, retrieval, verification, memory, and benchmark contracts"),
    "archflow-e1-runtime-guard": ("review", "provider-disabled runtime and public-safety validation report"),
    "archflow-knowledge-service": ("research", "source-bounded report with facts, interpretations, hypotheses, and gaps"),
    "archflow-task-breakdown": ("define", "ordered task packets with dependencies, gates, and acceptance checks"),
    "humanize-writing": ("publish", "fact-preserving natural public copy"),
    "outquestions": ("review", "critical decisions, blocking questions, risks, and next-stage gate"),
    "priority-task-operator": ("act", "highest-priority bounded operator handoff"),
    "task-handout": ("remember", "durable completion, checks, blockers, and next safe action"),
}

FORBIDDEN_PATH_PARTS = {
    "history",
    "runs",
    "reports",
    "live",
    ".git",
    "private",
    "local",
}

FORBIDDEN_TEXT = (
    re.compile(r"/(?:Users|home)/", re.IGNORECASE),
    re.compile(r"\b(?:api[_-]?key|token|secret|password)\s*[=:]\s*[^<\s]+", re.IGNORECASE),
    re.compile(r"@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError(f"expected JSON object: {rel(path)}")
    return value


def validate_manifest_entry(entry: object) -> Path:
    if not isinstance(entry, str) or not entry or entry.strip() != entry:
        raise RuntimeError("manifest path must be a non-empty normalized string")
    relative = Path(entry)
    if relative.is_absolute() or ".." in relative.parts or "\\" in entry or relative.as_posix() != entry:
        raise RuntimeError(f"unsafe manifest path: {entry}")
    if FORBIDDEN_PATH_PARTS.intersection(part.casefold() for part in relative.parts):
        raise RuntimeError(f"forbidden manifest zone: {entry}")
    if relative.suffix.casefold() not in {".md", ".yaml", ".yml", ".json"}:
        raise RuntimeError(f"unsupported manifest type: {entry}")
    path = ROOT / relative
    if not path.is_file():
        raise RuntimeError(f"missing manifest source: {entry}")
    return path


def load_corpus_manifest_paths() -> list[Path]:
    manifest = read_json(MANIFEST_PATH)
    if manifest.get("schema_version") != "3.0":
        raise RuntimeError("corpus manifest schema_version must be 3.0")
    entries = manifest.get("files")
    if not isinstance(entries, list) or not entries:
        raise RuntimeError("corpus manifest requires a non-empty files list")
    paths: list[Path] = []
    seen: set[str] = set()
    for entry in entries:
        path = validate_manifest_entry(entry)
        path_text = rel(path)
        if path_text in seen:
            raise RuntimeError(f"duplicate manifest source: {path_text}")
        seen.add(path_text)
        paths.append(path)
    return paths


def public_text_check(path: Path, text: str) -> None:
    for pattern in FORBIDDEN_TEXT:
        if pattern.search(text):
            raise RuntimeError(f"public-safety pattern in manifest source: {rel(path)}")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def title_for(path: Path, text: str) -> str:
    for line in text.splitlines()[:80]:
        if line.startswith("# "):
            return line[2:].strip()[:160]
    return path.stem.replace("-", " ").replace("_", " ").title()


def description_for_skill(text: str) -> str:
    match = re.search(r"(?m)^description:\s*(.+)$", text[:1800])
    if match:
        return match.group(1).strip().strip('"\'')[:480]
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip() and not part.lstrip().startswith(("---", "#"))]
    return re.sub(r"\s+", " ", paragraphs[0])[:480] if paragraphs else "Portable public operating contract."


def build_skill_catalog(roles: list[dict[str, Any]]) -> dict[str, Any]:
    recommended: dict[str, list[str]] = {skill_id: [] for skill_id in SKILL_IDS}
    for role in roles:
        role_id = str(role.get("id", ""))
        for skill_id in role.get("public_skill_packages", []):
            if skill_id in recommended and role_id:
                recommended[skill_id].append(role_id)

    items: list[dict[str, Any]] = []
    for skill_id in SKILL_IDS:
        path = ROOT / "skills" / skill_id / "SKILL.md"
        if not path.is_file():
            raise RuntimeError(f"missing packaged skill: {rel(path)}")
        text = path.read_text(encoding="utf-8")
        public_text_check(path, text)
        stage, output = SKILL_META[skill_id]
        items.append(
            {
                "id": skill_id,
                "name": title_for(path, text),
                "description": description_for_skill(text),
                "path": rel(path),
                "workflow_stage": stage,
                "expected_output": output,
                "portable": True,
                "safe_to_share": True,
                "permissions": ["read approved sources", "prepare bounded artifacts", "report evidence and gaps"],
                "forbidden_actions": ["infer authority", "store secrets", "self-approve high-risk work", "write externally without a separate gate"],
                "recommended_role_ids": sorted(recommended[skill_id]),
                "content_sha256": sha256_bytes(path.read_bytes()),
            }
        )
    return {"packaged_count": len(items), "items": items}


def build_role_projection() -> dict[str, Any]:
    """Project the one canonical machine catalog into dashboard-friendly fields."""

    canonical = read_json(SYSTEM_ROLE_CATALOG_PATH)
    if canonical.get("schema_version") != "3.0.0":
        raise RuntimeError("canonical role catalog schema_version must be 3.0.0")
    source_roles = canonical.get("roles")
    if not isinstance(source_roles, list) or len(source_roles) != 21:
        raise RuntimeError("canonical role catalog must contain exactly 21 roles")

    roles: list[dict[str, Any]] = []
    seen: set[str] = set()
    for source in source_roles:
        role_id = str(source.get("id", ""))
        defaults = source.get("task_defaults") or {}
        packages = [str(item) for item in defaults.get("allowed_skills", [])]
        methods = [str(item) for item in defaults.get("allowed_tools", [])]
        if not role_id or role_id in seen:
            raise RuntimeError("canonical role IDs must be unique and non-empty")
        if not set(packages).issubset(SKILL_IDS):
            raise RuntimeError(f"canonical role references an unregistered public skill: {role_id}")
        if set(packages).intersection(methods):
            raise RuntimeError(f"role package and method classifications overlap: {role_id}")
        seen.add(role_id)
        roles.append(
            {
                "id": role_id,
                "title": str(source.get("title", "")),
                "lane": str(source.get("lane", "")),
                "provider": "compatible_runtime_after_task_contract",
                "mode": f"{source.get('lane', 'bounded')}_role_contract",
                "goal": str(source.get("goal", "")),
                "purpose": str(source.get("purpose", "")),
                "skills": [*packages, *methods],
                "outputs": [str(item) for item in source.get("owns", [])],
                "forbidden_actions": [str(item) for item in source.get("forbidden", [])],
                "public_skill_packages": packages,
                "method_checklists": methods,
                "permission_mode": str(defaults.get("permission_mode", "")),
                "reviewer_route": [str(item) for item in defaults.get("reviewer_route", [])],
            }
        )
    return {
        "path": rel(SYSTEM_ROLE_CATALOG_PATH),
        "scope": "One canonical 21-role capability and authority catalog projected for the public dashboard.",
        "roles": roles,
    }


def sanitize_provider_registry(registry: dict[str, Any]) -> dict[str, Any]:
    adapters = []
    for adapter in registry.get("adapters", []):
        adapters.append(
            {
                "id": adapter.get("id"),
                "label": adapter.get("label"),
                "state": adapter.get("state"),
                "purpose": adapter.get("purpose"),
                "browser_access": False,
                "activation_requirements": adapter.get("activation_requirements", []),
                "implementation": adapter.get("implementation"),
                "documentation_url": adapter.get("documentation_url"),
                "secret_names": adapter.get("secret_names", []),
            }
        )
    return {
        "schema_version": registry.get("schema_version", "3.0"),
        "default_provider": "none",
        "default_observability": "off",
        "credential_policy": registry.get("credential_policy"),
        "credential_values_serialized": False,
        "credential_presence_serialized": False,
        "adapters": adapters,
    }


def default_metrics() -> list[dict[str, Any]]:
    return [
        {
            "label": "Benchmark status",
            "value": "Not measured",
            "comparator": "Curated V3 manifest against a declared baseline",
            "limitation": "Run the fixed provider-disabled benchmark before publishing a percentage.",
        },
        {
            "label": "Provider calls",
            "value": "0",
            "comparator": "Public generator and validators",
            "limitation": "A disabled boundary, not a speed or quality claim.",
        },
        {
            "label": "External writes",
            "value": "0",
            "comparator": "Public generator and validators",
            "limitation": "Downloads and local drafts are not external actions.",
        },
    ]


def build_performance_evidence() -> dict[str, Any]:
    if not BENCHMARK_PATH.is_file():
        return {"status": "not_measured_for_v3", "measured_at": None, "provider_calls": 0, "external_writes": 0, "metrics": default_metrics(), "path": rel(BENCHMARK_PATH)}
    result = read_json(BENCHMARK_PATH)
    metrics = result.get("publication_metrics")
    if not isinstance(metrics, list) or not metrics:
        raise RuntimeError("V3 benchmark requires publication_metrics")
    if result.get("provider_calls") != 0 or result.get("external_writes") != 0:
        raise RuntimeError("V3 public benchmark must remain provider-disabled and write-free")
    return {
        "status": result.get("status"),
        "measured_at": result.get("measured_at"),
        "fixture_id": result.get("fixture_id"),
        "provider_calls": 0,
        "external_writes": 0,
        "metrics": metrics,
        "limitations": result.get("limitations", []),
        "path": rel(BENCHMARK_PATH),
        "content_sha256": sha256_bytes(BENCHMARK_PATH.read_bytes()),
    }


def product_payload() -> dict[str, Any]:
    return {
        "category": "Knowledge continuity and agent operations",
        "description": (
            "ArchFlow is a public, local-first operating kit for turning a bounded objective and approved evidence into an inspectable plan, a role-safe execution path, independent review, and maintained knowledge. "
            "It gives an individual operator or a small team one shared structure for research, definition, action, validation, handoff, and learning. The static core works without an API key; authentication, model providers, observability, deployment, and external writeback remain separate server-side extensions with explicit proof, budget, approval, rollback, and readback gates."
        ),
        "audience": "Founders, operators, product teams, researchers, and small delivery teams that need repeatable AI-assisted work without hidden state, uncontrolled context, or personal project memory in the public tool.",
        "pains": [
            {"title": "Context resets", "description": "Teams repeatedly reconstruct background because current decisions, sources, and superseded assumptions are mixed together."},
            {"title": "Unclear ownership", "description": "An agent name or long prompt does not define who owns the output, who reviews it, or when work must stop."},
            {"title": "Invisible execution", "description": "A convincing response can look complete even when no artifact, check, approval, action, or readback exists."},
            {"title": "Tool sprawl", "description": "Providers and automations are often added before their data boundary, budget, failure mode, and rollback are understood."},
            {"title": "Unmaintained memory", "description": "Raw history grows while current, reusable guidance becomes harder to find, verify, and supersede."},
        ],
    }


def workflow_payload() -> list[dict[str, str]]:
    return [
        {"step": "01", "title": "Research", "description": "Admit a bounded source set, retrieve evidence, verify exact passages, and preserve provenance and gaps."},
        {"step": "02", "title": "Define", "description": "State the decision, acceptance criteria, authority, roles, outputs, reviewer, and stop conditions."},
        {"step": "03", "title": "Act", "description": "Run the smallest responsible route and hold external effects behind a separate approval gate."},
        {"step": "04", "title": "Review", "description": "Freeze the candidate and verify it independently against requirements and deterministic checks."},
        {"step": "05", "title": "Remember", "description": "Promote only reusable conclusions with source lineage, ownership, freshness, and supersession."},
    ]


def corpus_payload(paths: list[Path]) -> dict[str, Any]:
    items = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        public_text_check(path, text)
        items.append({"path": rel(path), "title": title_for(path, text), "bytes": len(path.read_bytes()), "sha256": sha256_bytes(path.read_bytes())})
    return {"manifest": rel(MANIFEST_PATH), "document_count": len(items), "items": items}


def dashboard_source_revision(paths: list[Path] | None = None) -> str:
    paths = paths or load_corpus_manifest_paths()
    skill_paths = [ROOT / "skills" / skill_id / "SKILL.md" for skill_id in SKILL_IDS]
    inputs = [
        MANIFEST_PATH,
        *paths,
        SYSTEM_ROLE_CATALOG_PATH,
        ROLE_PACKS_PATH,
        PROVIDER_REGISTRY_PATH,
        *([BENCHMARK_PATH] if BENCHMARK_PATH.is_file() else []),
        *skill_paths,
        Path(__file__),
        DASHBOARD / "index.html",
        DASHBOARD / "app.js",
        DASHBOARD / "styles.css",
    ]
    digest = hashlib.sha256()
    for path in inputs:
        digest.update(rel(path).encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return f"sha256:{digest.hexdigest()}"


def build_dashboard(
    generated_at: str,
    role_catalog: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    paths = load_corpus_manifest_paths()
    role_catalog = role_catalog or build_role_projection()
    roles = role_catalog.get("roles")
    if not isinstance(roles, list) or not roles:
        raise RuntimeError("role catalog requires roles")
    role_ids = [str(role.get("id", "")) for role in roles]
    if not all(role_ids) or len(role_ids) != len(set(role_ids)):
        raise RuntimeError("role IDs must be unique and non-empty")
    role_packs = read_json(ROLE_PACKS_PATH)
    selected = {role_id for pack in role_packs.get("packs", []) for role_id in pack.get("role_ids", [])}
    unknown = sorted(selected - set(role_ids))
    if unknown:
        raise RuntimeError(f"role packs reference unknown roles: {', '.join(unknown)}")
    skill_catalog = build_skill_catalog(roles)
    provider_registry = sanitize_provider_registry(read_json(PROVIDER_REGISTRY_PATH))
    data = {
        "schema_version": "3.0",
        "generated_at": generated_at,
        "source_revision": dashboard_source_revision(paths),
        "product": product_payload(),
        "workflow": workflow_payload(),
        "role_catalog": {"scope": role_catalog.get("scope"), "roles": roles},
        "skill_catalog": skill_catalog,
        "actionable_role_packs": role_packs,
        "provider_registry": provider_registry,
        "performance_evidence": build_performance_evidence(),
        "corpus": corpus_payload(paths),
        "boundaries": {
            "provider_calls": 0,
            "external_writes": 0,
            "browser_identity_storage": False,
            "credential_values_serialized": False,
            "credential_presence_serialized": False,
            "project_runs_indexed": False,
            "personal_memory_indexed": False,
        },
    }
    return data, skill_catalog


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DASHBOARD / "data.json")
    parser.add_argument("--js-output", type=Path, default=DASHBOARD / "data.js")
    parser.add_argument("--skill-output", type=Path, default=SKILL_CATALOG_PATH)
    parser.add_argument("--role-output", type=Path, default=ROLE_CATALOG_PATH)
    parser.add_argument("--generated-at", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    generated_at = args.generated_at or datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    role_catalog = build_role_projection()
    role_serialized = json.dumps(role_catalog, indent=2, ensure_ascii=True, sort_keys=True) + "\n"
    ROLE_CATALOG_PATH.write_text(role_serialized, encoding="utf-8")
    if args.role_output.resolve() != ROLE_CATALOG_PATH.resolve():
        args.role_output.write_text(role_serialized, encoding="utf-8")
    data, skill_catalog = build_dashboard(generated_at, role_catalog)
    serialized = json.dumps(data, indent=2, ensure_ascii=True, sort_keys=True) + "\n"
    args.output.write_text(serialized, encoding="utf-8")
    args.js_output.write_text(f"window.ARCHFLOW_PUBLIC_DATA = {json.dumps(data, ensure_ascii=True, sort_keys=True)};\n", encoding="utf-8")
    args.skill_output.write_text(json.dumps(skill_catalog, indent=2, ensure_ascii=True, sort_keys=True) + "\n", encoding="utf-8")
    print("dashboard_generate=ok")
    print(f"source_revision={data['source_revision']}")
    print(f"corpus_count={data['corpus']['document_count']}")
    print(f"skill_count={data['skill_catalog']['packaged_count']}")
    print(f"role_count={len(data['role_catalog']['roles'])}")
    print(f"benchmark_status={data['performance_evidence']['status']}")
    print("provider_calls=0")
    print("external_writes=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
