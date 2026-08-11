#!/usr/bin/env python3
"""Validate the generic ArchFlow Knowledge Operator projection."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
DASHBOARD = PROJECT / "dashboard"
DATA_PATH = DASHBOARD / "data.json"
DATA_JS_PATH = DASHBOARD / "data.js"
MANIFEST_PATH = DASHBOARD / "corpus-manifest.json"
CATALOG_PATH = PROJECT / "database" / "skill-catalog.json"
GENERATOR_PATH = PROJECT / "scripts" / "generate-dashboard-data.py"
LLAMAINDEX_PATH = PROJECT / "scripts" / "llamaindex-approved-corpus.py"

FORBIDDEN_DATA_PATTERNS = {
    "local_absolute_path": re.compile(r"/(?:Users|home)/", re.IGNORECASE),
    "email_address": re.compile(r"@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "credential_value": re.compile(r"\b(?:api[_-]?key|token|secret|password)\s*[=:]\s*[^<\s]+", re.IGNORECASE),
    "project_history": re.compile(r"(?:project|wiki)/(?:runs|reports|live|decisions|issues)/", re.IGNORECASE),
    "browser_role_toggle": re.compile(r"(?:admin|guest)[ _-]preview", re.IGNORECASE),
}

def fail(message: str) -> None:
    raise SystemExit(f"dashboard_data=fail:{message}")


def read_object(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"invalid_json:{path.name}:{error}")
    if not isinstance(value, dict):
        fail(f"json_object_required:{path.name}")
    return value


def import_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(f"module_import:{path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_data_js(data: dict) -> None:
    raw = DATA_JS_PATH.read_text(encoding="utf-8")
    prefix = "window.ARCHFLOW_PUBLIC_DATA = "
    if not raw.startswith(prefix) or not raw.endswith(";\n"):
        fail("data_js_wrapper")
    try:
        parsed = json.loads(raw[len(prefix) : -2])
    except json.JSONDecodeError:
        fail("data_js_json")
    if parsed != data:
        fail("data_js_parity")


def main() -> int:
    required = (DATA_PATH, DATA_JS_PATH, MANIFEST_PATH, CATALOG_PATH, GENERATOR_PATH, LLAMAINDEX_PATH)
    if not all(path.is_file() for path in required):
        fail("missing_required_file")

    data = read_object(DATA_PATH)
    manifest = read_object(MANIFEST_PATH)
    catalog = read_object(CATALOG_PATH)
    raw = DATA_PATH.read_text(encoding="utf-8")

    if data.get("schema_version") != "3.0" or manifest.get("schema_version") != "3.0":
        fail("schema_version")
    if DATA_PATH.stat().st_size > 300_000 or DATA_JS_PATH.stat().st_size > 320_000:
        fail("payload_size_budget")
    if not data.get("product", {}).get("description") or len(data.get("workflow", [])) != 5:
        fail("product_contract")
    validate_data_js(data)

    for name, pattern in FORBIDDEN_DATA_PATTERNS.items():
        if pattern.search(raw):
            fail(f"forbidden_data:{name}")
    manifest_files = manifest.get("files")
    if not isinstance(manifest_files, list) or not manifest_files or len(manifest_files) != len(set(manifest_files)):
        fail("manifest_files")
    forbidden_zones = ("history/", "project/runs/", "project/reports/", "project/live/", "wiki/runs/", "wiki/decisions/", "wiki/issues/", "private/")
    if any(str(path).casefold().startswith(forbidden_zones) for path in manifest_files):
        fail("manifest_forbidden_zone")

    corpus = data.get("corpus", {})
    corpus_items = corpus.get("items", [])
    if corpus.get("document_count") != len(manifest_files) or [item.get("path") for item in corpus_items] != manifest_files:
        fail("corpus_manifest_parity")
    for item in corpus_items:
        path = ROOT / str(item.get("path", ""))
        if not path.is_file() or digest(path) != item.get("sha256") or path.stat().st_size != item.get("bytes"):
            fail(f"corpus_hash:{item.get('path')}")

    skills = data.get("skill_catalog", {}).get("items", [])
    if data.get("skill_catalog", {}).get("packaged_count") != 10 or len(skills) != 10 or catalog != data.get("skill_catalog"):
        fail("skill_catalog_count_or_parity")
    skill_ids = {item.get("id") for item in skills}
    if len(skill_ids) != len(skills):
        fail("skill_ids")
    for item in skills:
        path = ROOT / str(item.get("path", ""))
        if not path.is_file() or digest(path) != item.get("content_sha256"):
            fail(f"skill_hash:{item.get('id')}")
        if not item.get("workflow_stage") or not item.get("expected_output") or item.get("safe_to_share") is not True:
            fail(f"skill_contract:{item.get('id')}")

    roles = data.get("role_catalog", {}).get("roles", [])
    role_ids = {role.get("id") for role in roles}
    if not roles or len(role_ids) != len(roles) or None in role_ids:
        fail("role_ids")
    for role in roles:
        packages = set(role.get("public_skill_packages", []))
        methods = set(role.get("method_checklists", []))
        declared = set(role.get("skills", []))
        if packages & methods or packages | methods != declared or not packages.issubset(skill_ids):
            fail(f"role_skill_classification:{role.get('id')}")

    packs = data.get("actionable_role_packs", {}).get("packs", [])
    if not packs:
        fail("role_packs")
    for pack in packs:
        selected = set(pack.get("role_ids", []))
        makers = set(pack.get("maker_role_ids", []))
        reviewer = pack.get("reviewer_role_id")
        if not selected or not selected.issubset(role_ids) or not makers.issubset(selected) or reviewer not in selected or reviewer in makers:
            fail(f"role_pack_boundary:{pack.get('id')}")

    providers = data.get("provider_registry", {})
    adapters = providers.get("adapters", [])
    if providers.get("default_provider") != "none" or providers.get("default_observability") != "off":
        fail("provider_defaults")
    if providers.get("credential_values_serialized") is not False or providers.get("credential_presence_serialized") is not False:
        fail("provider_credential_boundary")
    if not adapters or any(adapter.get("browser_access") is not False for adapter in adapters):
        fail("provider_browser_boundary")

    boundaries = data.get("boundaries", {})
    expected_false = ("browser_identity_storage", "credential_values_serialized", "credential_presence_serialized", "project_runs_indexed", "personal_memory_indexed")
    if boundaries.get("provider_calls") != 0 or boundaries.get("external_writes") != 0 or any(boundaries.get(key) is not False for key in expected_false):
        fail("public_boundary")

    evidence = data.get("performance_evidence", {})
    if evidence.get("provider_calls") != 0 or evidence.get("external_writes") != 0:
        fail("performance_boundary")
    for metric in evidence.get("metrics", []):
        if not metric.get("label") or not metric.get("value") or not metric.get("comparator") or not metric.get("limitation"):
            fail("performance_metric_contract")

    generator = import_module(GENERATOR_PATH, "archflow_dashboard_generator_v3")
    generator_paths = [path.relative_to(ROOT).as_posix() for path in generator.load_corpus_manifest_paths()]
    if generator_paths != manifest_files or data.get("source_revision") != generator.dashboard_source_revision():
        fail("generator_parity")
    llamaindex = import_module(LLAMAINDEX_PATH, "archflow_llamaindex_v3")
    retrieval_paths = [path.relative_to(ROOT).as_posix() for path in llamaindex.load_corpus_manifest_paths()]
    if retrieval_paths != manifest_files:
        fail("retrieval_manifest_parity")

    app = (DASHBOARD / "app.js").read_text(encoding="utf-8")
    index = (DASHBOARD / "index.html").read_text(encoding="utf-8")
    for marker in ("viewerMode", "Admin preview", "Guest preview", "webkitSpeechRecognition", "SpeechSynthesisUtterance"):
        if marker in app or marker in index:
            fail(f"dead_or_unsafe_ui:{marker}")
    retired_token_pattern = r"JARVIS[_-]" + r"OWNER[_-]" + r"TOKEN"
    if re.search(retired_token_pattern, app + index, re.IGNORECASE):
        fail("dead_or_unsafe_ui:retired_owner_token")
    if "./data.js" not in index or REPOSITORY_URL not in index:
        fail("offline_or_github_link")

    print("dashboard_data=ok")
    print(f"schema_version={data['schema_version']}")
    print(f"source_revision={data['source_revision']}")
    print(f"payload_bytes={DATA_PATH.stat().st_size}")
    print(f"corpus_count={corpus['document_count']}")
    print(f"skill_count={len(skills)}")
    print(f"role_count={len(roles)}")
    print(f"benchmark_status={evidence.get('status')}")
    print("provider_calls=0")
    print("external_writes=0")
    return 0


REPOSITORY_URL = "https://github.com/mcharniuk1-spec/archflow_b1_knowledge"


if __name__ == "__main__":
    raise SystemExit(main())
