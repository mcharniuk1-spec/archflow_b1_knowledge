#!/usr/bin/env python3
"""Pre-push runtime guard for the ArchFlow public project."""

from __future__ import annotations

import subprocess
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
PYTHON = PROJECT / "local" / "venv" / "bin" / "python"
REQUIRED_IMPORTS = {
    "langsmith": "LangSmith SDK",
    "langgraph": "LangGraph runtime",
    "langchain_core": "LangChain Core runtime",
    "pydantic": "Pydantic validation",
    "yaml": "PyYAML validation",
    "llama_index.core": "LlamaIndex core runtime",
    "crewai": "CrewAI runtime",
}


def runtime_env() -> dict[str, str]:
    env = os.environ.copy()
    env["HOME"] = str(PROJECT / "local" / "home")
    env["CREWAI_STORAGE_DIR"] = "archflow_e1"
    env["CREWAI_DISABLE_TELEMETRY"] = "true"
    env["CREWAI_DISABLE_TRACKING"] = "true"
    env["OTEL_SDK_DISABLED"] = "true"
    return env


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=False, env=runtime_env())


def fail(message: str) -> int:
    print(f"runtime_guard=fail:{message}")
    return 1


def main() -> int:
    if not PYTHON.exists():
        return fail("missing_project_local_venv")

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

    validation = run([str(PYTHON), "project/scripts/validate-workflows.py"])
    if validation.returncode != 0:
        print(validation.stdout.strip())
        print(validation.stderr.strip())
        return fail("workflow_validation_failed")

    for module, label in REQUIRED_IMPORTS.items():
        probe = run([str(PYTHON), "-c", f"import {module}"])
        if probe.returncode != 0:
            return fail(f"missing_{label.replace(' ', '_').lower()}")

    smoke = run([str(PYTHON), "project/scripts/langgraph-smoke-run.py"])
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

    print("runtime_guard=ok")
    print(validation.stdout.strip())
    print("langgraph_smoke=verified")
    print("llamaindex_corpus=verified")
    print("crewai_config=verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
