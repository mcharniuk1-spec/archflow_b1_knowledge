#!/usr/bin/env python3
"""Pre-push runtime guard for the ArchFlow public project."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
PYTHON = Path(sys.executable).resolve()
REQUIRED_IMPORTS = {
    "langgraph": "LangGraph runtime",
    "pydantic": "Pydantic validation",
    "yaml": "PyYAML validation",
}
EXECUTION_REPORT_ROOT = PROJECT / "local" / "execution-reports"

# CrewAI and LlamaIndex deep imports are explicit opt-in checks. The bounded
# distribution/config and exact-corpus checks below are deterministic and do
# not activate optional integration discovery, telemetry, models, or providers.


def runtime_env() -> dict[str, str]:
    env = os.environ.copy()
    secret_suffixes = ("_API_KEY", "_TOKEN", "_PASSWORD", "_SECRET", "_COOKIE")
    for key in list(env):
        if key.upper().endswith(secret_suffixes):
            env.pop(key, None)
    env["ARCHFLOW_LOCAL_RUNTIME_HOME"] = str(PROJECT / "local" / "home")
    env["CREWAI_STORAGE_DIR"] = str(PROJECT / "local" / "home" / "archflow_e1")
    env["CREWAI_DISABLE_TELEMETRY"] = "true"
    env["CREWAI_DISABLE_TRACKING"] = "true"
    env["OTEL_SDK_DISABLED"] = "true"
    return env


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=False, env=runtime_env())


def fail(message: str) -> int:
    print(f"runtime_guard=fail:{message}")
    return 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--execution-report",
        action="append",
        default=[],
        help="Validate an explicit file under project/local/execution-reports. May be supplied more than once.",
    )
    return parser.parse_args()


def selected_execution_reports(explicit: list[str]) -> list[Path]:
    selected: set[Path] = set()
    for value in explicit:
        candidate = Path(value)
        resolved = (candidate if candidate.is_absolute() else ROOT / candidate).resolve()
        try:
            resolved.relative_to(EXECUTION_REPORT_ROOT.resolve())
        except ValueError as exc:
            raise ValueError(
                "execution reports must be explicit files under project/local/execution-reports"
            ) from exc
        if resolved.name != "execution-report.md":
            raise ValueError("execution report filename must be execution-report.md")
        if not resolved.is_file():
            raise ValueError("execution report does not exist under the ignored local report root")
        selected.add(resolved)
    return sorted(selected)


def main() -> int:
    args = parse_args()
    if not PYTHON.exists():
        return fail("missing_python_runtime")

    for path in [
        ROOT / "skills" / "archflow-task-breakdown" / "SKILL.md",
        ROOT / "skills" / "archflow-e1-runtime-guard" / "SKILL.md",
        PROJECT / "scripts" / "langgraph-smoke-run.py",
        PROJECT / "scripts" / "llamaindex-approved-corpus.py",
        PROJECT / "scripts" / "crewai-config-check.py",
        PROJECT / "scripts" / "validate-workflows.py",
    ]:
        if not path.exists():
            return fail(f"missing_{path.relative_to(ROOT).as_posix()}")

    validation_self_test = run([str(PYTHON), "project/scripts/validate-workflows.py", "--self-test"])
    if validation_self_test.returncode != 0:
        print(validation_self_test.stdout.strip())
        print(validation_self_test.stderr.strip())
        return fail("workflow_validation_self_test_failed")

    validation = run([str(PYTHON), "project/scripts/validate-workflows.py"])
    if validation.returncode != 0:
        print(validation.stdout.strip())
        print(validation.stderr.strip())
        return fail("workflow_validation_failed")

    for module, label in REQUIRED_IMPORTS.items():
        probe = run([str(PYTHON), "-c", f"import {module}"])
        if probe.returncode != 0:
            return fail(f"missing_{label.replace(' ', '_').lower()}")

    smoke = run([str(PYTHON), "project/scripts/langgraph-smoke-run.py", "--self-test"])
    if smoke.returncode != 0:
        print(smoke.stdout.strip())
        print(smoke.stderr.strip())
        return fail("langgraph_smoke_failed")

    corpus = run([str(PYTHON), "project/scripts/llamaindex-approved-corpus.py"])
    if corpus.returncode != 0:
        print(corpus.stdout.strip())
        print(corpus.stderr.strip())
        return fail("llamaindex_corpus_failed")

    crew = run([str(PYTHON), "project/scripts/crewai-config-check.py"])
    if crew.returncode != 0:
        print(crew.stdout.strip())
        print(crew.stderr.strip())
        return fail("crewai_config_failed")

    report_validator = PROJECT / "scripts" / "validate-execution-report.py"
    try:
        execution_reports = selected_execution_reports(args.execution_report)
    except ValueError as exc:
        return fail(str(exc).replace(" ", "_"))
    if execution_reports:
        if not report_validator.exists():
            return fail("missing_project/scripts/validate-execution-report.py")
        report_check = run([str(PYTHON), str(report_validator), *[str(path) for path in execution_reports]])
        if report_check.returncode != 0:
            print(report_check.stdout.strip())
            print(report_check.stderr.strip())
            return fail("execution_report_validation_failed")

    print("runtime_guard=ok")
    print(validation_self_test.stdout.strip())
    print(validation.stdout.strip())
    print("langgraph_smoke=verified")
    print("llamaindex_corpus=verified")
    print("crewai_config=verified")
    print(f"execution_reports=verified:{len(execution_reports)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
