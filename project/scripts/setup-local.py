#!/usr/bin/env python3
"""Plan, install, or verify the local ArchFlow setup profiles.

The default command is read-only. Package installation requires --install and
never configures credentials, starts a service, calls a provider, or deploys.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import venv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
LOCAL_ROOT = PROJECT / "local"
PROVIDER_REGISTRY_PATH = PROJECT / "config" / "provider-registry.json"

PROFILES = {
    "core": {
        "requirements": [],
        "locks": [],
        "purpose": "Zero-key knowledge-case validation, generated dashboard data, and static control room.",
        "python": ">=3.11",
        "checks": [
            ["project/system/validate_system.py"],
            ["project/scripts/generate-dashboard-data.py"],
            ["project/scripts/validate-dashboard-data.py"],
        ],
    },
    "validation": {
        "requirements": ["project/requirements-dev.txt"],
        "locks": ["project/requirements-validation.lock.txt"],
        "purpose": "YAML and Pydantic workflow validation plus public-safety checks.",
        "python": ">=3.11",
        "checks": [
            ["project/scripts/validate-workflows.py"],
            ["scripts/public_safety_scan.py"],
        ],
    },
    "agentic": {
        "requirements": ["project/requirements-agentic.txt"],
        "locks": ["project/requirements-agentic.lock.txt"],
        "purpose": "Provider-disabled LangGraph, CrewAI contract, and LlamaIndex lexical engineering checks.",
        "python": "3.12",
        "checks": [
            ["project/scripts/langgraph-smoke-run.py"],
            ["project/scripts/crewai-config-check.py"],
            ["project/scripts/llamaindex-approved-corpus.py", "--mode", "lexical"],
        ],
    },
    "jarvis": {
        "requirements": ["services/jarvis-api/requirements-dev.txt"],
        "locks": ["services/jarvis-api/requirements-dev.lock.txt"],
        "purpose": "Provider-disabled FastAPI review-packet service and contract smoke.",
        "python": ">=3.11",
        "checks": [
            ["project/scripts/jarvis-api-contract-smoke.py"],
            ["project/scripts/jarvis-serverless-owner-guard-smoke.py"],
        ],
    },
}


def selected_profiles(name: str) -> list[str]:
    return list(PROFILES) if name == "all" else [name]


def provider_registry() -> dict:
    try:
        registry = json.loads(PROVIDER_REGISTRY_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"setup=fail:provider_registry:{error}") from error
    if registry.get("schema_version") != "3.0" or not isinstance(registry.get("adapters"), list):
        raise SystemExit("setup=fail:provider_registry_schema")
    return registry


def safe_venv_path(raw: str) -> Path:
    candidate = Path(raw)
    if not candidate.is_absolute():
        candidate = ROOT / candidate
    candidate = candidate.resolve()
    local_root = LOCAL_ROOT.resolve()
    if candidate == local_root or local_root not in candidate.parents:
        raise SystemExit("setup=fail:venv_must_be_below_project/local")
    return candidate


def python_in(venv_path: Path) -> Path:
    return venv_path / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")


def install_profiles(profile_names: list[str], venv_path: Path, locked: bool) -> Path:
    python_path = python_in(venv_path)
    if not python_path.exists():
        venv_path.parent.mkdir(parents=True, exist_ok=True)
        venv.EnvBuilder(with_pip=True, clear=False).create(venv_path)
    requirement_paths = []
    for profile_name in profile_names:
        requirement_key = "locks" if locked else "requirements"
        for requirement in PROFILES[profile_name][requirement_key]:
            path = ROOT / requirement
            if path not in requirement_paths:
                requirement_paths.append(path)
    if requirement_paths:
        command = [str(python_path), "-m", "pip", "install"]
        for path in requirement_paths:
            command.extend(["-r", str(path)])
        subprocess.run(command, cwd=ROOT, check=True)
    return python_path


def verify_profiles(profile_names: list[str], python_path: Path, timeout_seconds: int) -> None:
    for profile_name in profile_names:
        for check in PROFILES[profile_name]["checks"]:
            command = [str(python_path), *check]
            try:
                subprocess.run(command, cwd=ROOT, check=True, timeout=timeout_seconds)
            except subprocess.TimeoutExpired as error:
                check_name = Path(check[0]).name
                raise SystemExit(
                    f"setup=fail:check_timeout:{profile_name}:{check_name}:{timeout_seconds}s"
                ) from error


def main() -> int:
    registry = provider_registry()
    adapter_ids = [str(item.get("id")) for item in registry["adapters"] if item.get("id")]
    parser = argparse.ArgumentParser(description="Plan or prepare the local ArchFlow toolchain.")
    parser.add_argument("--profile", choices=[*PROFILES, "all"], default="core")
    parser.add_argument("--venv", default="project/local/venv-setup")
    parser.add_argument("--install", action="store_true", help="Create the isolated environment and install tracked requirements.")
    parser.add_argument("--locked", action="store_true", help="Install the reviewed Python 3.12 candidate lock instead of resolving direct pins.")
    parser.add_argument("--verify", action="store_true", help="Run the bounded checks for the selected profile.")
    parser.add_argument("--timeout", type=int, default=60, help="Maximum seconds for each verification command.")
    parser.add_argument(
        "--provider-plan",
        choices=[*adapter_ids, "all"],
        default="none",
        help="Show a non-secret activation contract. This never checks or creates credentials.",
    )
    args = parser.parse_args()

    names = selected_profiles(args.profile)
    venv_path = safe_venv_path(args.venv)
    selected_adapters = registry["adapters"] if args.provider_plan == "all" else [
        item for item in registry["adapters"] if item.get("id") == args.provider_plan
    ]
    plan = {
        "status": "planned",
        "profile": args.profile,
        "profiles": [
            {
                "name": name,
                "purpose": PROFILES[name]["purpose"],
                "python": PROFILES[name]["python"],
                "requirements": PROFILES[name]["requirements"],
                "candidate_locks": PROFILES[name]["locks"],
                "checks": PROFILES[name]["checks"],
            }
            for name in names
        ],
        "venv": venv_path.relative_to(ROOT).as_posix(),
        "provider_calls": False,
        "service_start": False,
        "external_writeback": False,
        "install_requested": args.install,
        "locked_install": args.locked,
        "verify_requested": args.verify,
        "check_timeout_seconds": args.timeout,
        "provider_plan": {
            "registry": PROVIDER_REGISTRY_PATH.relative_to(ROOT).as_posix(),
            "credential_values_read": False,
            "credential_presence_checked": False,
            "adapters": selected_adapters,
        },
    }
    python_path = Path(sys.executable)
    if args.install:
        if "agentic" in names and sys.version_info[:2] != (3, 12):
            raise SystemExit(
                "setup=fail:agentic_install_requires_python_3_12:run_with_python3.12"
            )
        python_path = install_profiles(names, venv_path, args.locked)
    elif args.profile != "core" and args.verify:
        candidate = python_in(venv_path)
        if not candidate.exists():
            raise SystemExit("setup=fail:profile_environment_missing_use_--install")
        python_path = candidate

    if args.verify:
        verify_profiles(names, python_path, args.timeout)
        plan["status"] = "verified"
    elif args.install:
        plan["status"] = "installed"
    print(json.dumps(plan, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
