#!/usr/bin/env python3
"""Run the mandatory public core guard and optional framework-runtime proof.

Every push verifies the provider-disabled, standard-library public core.
Dependency-backed LangGraph, LlamaIndex, and CrewAI checks run only when
ARCHFLOW_VERIFY_OPTIONAL_RUNTIME=1 is explicitly set.
"""

from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
RUNTIME_PYTHON = PROJECT / "local" / "venv" / "bin" / "python"
OPTIONAL_RUNTIME_FLAG = "ARCHFLOW_VERIFY_OPTIONAL_RUNTIME"
CAPSULE_PATH = PROJECT / "runs" / "20260805-responsive-knowledge-crew-dashboard" / "context-capsule.json"
RUN_PROFILES_PATH = PROJECT / "architecture" / "run-profiles.yaml"


def runtime_env() -> dict[str, str]:
    env = os.environ.copy()
    storage_dir = PROJECT / "local" / "crewai-storage"
    storage_dir.mkdir(parents=True, exist_ok=True)
    env["CREWAI_STORAGE_DIR"] = str(storage_dir)
    env["CREWAI_DISABLE_TELEMETRY"] = "true"
    env["CREWAI_DISABLE_TRACKING"] = "true"
    env["OTEL_SDK_DISABLED"] = "true"
    return env


def run(
    cmd: list[str],
    *,
    timeout_seconds: int = 120,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            cmd,
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
            env=env,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired as exc:
        return subprocess.CompletedProcess(
            cmd,
            124,
            exc.stdout or "",
            exc.stderr or f"command exceeded {timeout_seconds} seconds",
        )


def fail(message: str, result: subprocess.CompletedProcess[str] | None = None) -> int:
    if result is not None:
        if result.stdout.strip():
            print(result.stdout.strip())
        if result.stderr.strip():
            print(result.stderr.strip())
    print(f"runtime_guard=fail:{message}")
    return 1


def require_ok(
    label: str,
    cmd: list[str],
    *,
    timeout_seconds: int = 120,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    result = run(cmd, timeout_seconds=timeout_seconds, env=env)
    if result.returncode == 124:
        raise RuntimeError(f"{label}_timeout")
    if result.returncode != 0:
        raise RuntimeError(f"{label}_failed\n{result.stdout}\n{result.stderr}")
    return result


def load_object(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError(f"release_scope_not_object:{path.relative_to(ROOT).as_posix()}")
    return value


def validate_repo_path(raw: str) -> str:
    if not raw or raw.startswith("/") or "\\" in raw:
        raise RuntimeError(f"release_scope_invalid_path:{raw}")
    normalized = raw.rstrip("/")
    path = PurePosixPath(normalized)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise RuntimeError(f"release_scope_invalid_path:{raw}")
    if path.parts[0] in {".git", "private", "secrets"}:
        raise RuntimeError(f"release_scope_forbidden_path:{raw}")
    return normalized


def validate_admitted_paths(changed_paths: set[str], allowed_entries: list[str]) -> None:
    exact: set[str] = set()
    prefixes: set[str] = set()
    for raw in allowed_entries:
        normalized = validate_repo_path(raw)
        if raw.endswith("/"):
            prefixes.add(normalized + "/")
        else:
            exact.add(normalized)
    outside: list[str] = []
    for raw in sorted(changed_paths):
        normalized = validate_repo_path(raw)
        if normalized in exact or any(normalized.startswith(prefix) for prefix in prefixes):
            continue
        outside.append(normalized)
    if outside:
        raise RuntimeError(f"unadmitted_release_paths:{','.join(outside)}")


def git_changed_paths() -> set[str] | None:
    if not (ROOT / ".git").exists():
        return None
    commands = (
        ["git", "diff", "--name-only", "--relative", "--"],
        ["git", "diff", "--cached", "--name-only", "--relative", "--"],
        ["git", "ls-files", "--others", "--exclude-standard"],
    )
    paths: set[str] = set()
    for command in commands:
        result = run(command, timeout_seconds=30)
        if result.returncode != 0:
            raise RuntimeError(f"release_scope_git_inventory_failed:{' '.join(command)}")
        paths.update(line.strip() for line in result.stdout.splitlines() if line.strip())
    return paths


def verify_release_scope() -> None:
    capsule = load_object(CAPSULE_PATH)
    profiles = load_object(RUN_PROFILES_PATH)
    capsule_refs = [item["source_path"] for item in capsule.get("cag_core_refs", [])]
    required_refs = profiles.get("required_cag_references")
    if capsule_refs != required_refs:
        raise RuntimeError("release_scope_cag_refs_do_not_match_canonical_admission")
    allowed_entries = capsule.get("allowed_files")
    if not isinstance(allowed_entries, list) or not all(isinstance(item, str) for item in allowed_entries):
        raise RuntimeError("release_scope_allowed_files_invalid")
    changed = git_changed_paths()
    if changed is None:
        print("release_scope_git_inventory=not_available_non_git_snapshot")
    else:
        validate_admitted_paths(changed, allowed_entries)
        print(f"release_scope_changed_paths=admitted:{len(changed)}")
    try:
        validate_admitted_paths({"unadmitted-release-probe.txt"}, allowed_entries)
    except RuntimeError as exc:
        if not str(exc).startswith("unadmitted_release_paths:"):
            raise
    else:
        raise RuntimeError("release_scope_negative_path_unexpectedly_admitted")
    print("release_scope_negative_path=rejected")


def verify_public_core() -> None:
    verify_release_scope()
    required_paths = [
        ROOT / "skills" / "archflow-task-breakdown" / "SKILL.md",
        ROOT / "skills" / "archflow-e1-runtime-guard" / "SKILL.md",
        ROOT / "skills" / "task-handout" / "SKILL.md",
        PROJECT / "system" / "validate_system.py",
        PROJECT / "scripts" / "dashboard-static-smoke.py",
        PROJECT / "scripts" / "validate-workflows.py",
        PROJECT / "scripts" / "langgraph-smoke-run.py",
        PROJECT / "scripts" / "llamaindex-approved-corpus.py",
        PROJECT / "scripts" / "crewai-config-check.py",
    ]
    missing = [path.relative_to(ROOT).as_posix() for path in required_paths if not path.exists()]
    if missing:
        raise RuntimeError(f"missing_required_paths:{','.join(missing)}")

    require_ok(
        "system_contract",
        [sys.executable, "project/system/validate_system.py"],
        timeout_seconds=60,
    )
    require_ok(
        "dashboard_static_contract",
        [sys.executable, "project/scripts/dashboard-static-smoke.py", "--skip-browser"],
        timeout_seconds=60,
    )

    dev_specs_present = all(
        importlib.util.find_spec(module) is not None for module in ("yaml", "pydantic")
    )
    if dev_specs_present:
        require_ok(
            "workflow_schema_validation",
            [sys.executable, "project/scripts/validate-workflows.py"],
            timeout_seconds=60,
        )
        print("workflow_schema_validation=verified")
    else:
        print("workflow_schema_validation=skipped_optional_dev_dependencies")

    print("public_core_guard=ok")


def verify_optional_framework_runtime() -> None:
    if os.environ.get(OPTIONAL_RUNTIME_FLAG) != "1":
        print("optional_framework_runtime=not_requested")
        return
    if not RUNTIME_PYTHON.exists():
        raise RuntimeError("optional_runtime_requested_but_project_local_venv_missing")

    env = runtime_env()
    require_ok(
        "workflow_schema_validation_optional_runtime",
        [str(RUNTIME_PYTHON), "project/scripts/validate-workflows.py"],
        timeout_seconds=120,
        env=env,
    )
    require_ok(
        "langgraph_smoke",
        [str(RUNTIME_PYTHON), "project/scripts/langgraph-smoke-run.py"],
        timeout_seconds=180,
        env=env,
    )
    require_ok(
        "llamaindex_corpus",
        [str(RUNTIME_PYTHON), "project/scripts/llamaindex-approved-corpus.py"],
        timeout_seconds=180,
        env=env,
    )
    require_ok(
        "crewai_config",
        [str(RUNTIME_PYTHON), "project/scripts/crewai-config-check.py"],
        timeout_seconds=180,
        env=env,
    )
    print("optional_framework_runtime=verified")
    print("provider_calls=0")
    print("external_writeback=0")


def main() -> int:
    try:
        verify_public_core()
        verify_optional_framework_runtime()
    except RuntimeError as exc:
        return fail(str(exc))

    print("runtime_guard=ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
