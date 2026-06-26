#!/usr/bin/env python3
"""Validate CrewAI config without running LLM tasks."""

from __future__ import annotations

import os
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
CONFIG = PROJECT / "workflows" / "crewai-crew.yaml"


def configure_local_crewai_runtime() -> None:
    local_home = PROJECT / "local" / "home"
    local_home.mkdir(parents=True, exist_ok=True)
    os.environ["HOME"] = str(local_home)
    os.environ["CREWAI_STORAGE_DIR"] = "archflow_e1"
    os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
    os.environ["CREWAI_DISABLE_TRACKING"] = "true"
    os.environ["OTEL_SDK_DISABLED"] = "true"


def main() -> int:
    configure_local_crewai_runtime()

    from crewai import Agent, Crew, Task

    data = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    agents = data.get("agents", {})
    tasks = data.get("tasks", [])
    task_agent_ids = {task.get("agent") for task in tasks}
    missing_agents = sorted(agent_id for agent_id in task_agent_ids if agent_id not in agents)
    if missing_agents:
        raise SystemExit(f"crewai_config=fail:missing_task_agents:{','.join(missing_agents)}")

    if not {Agent, Crew, Task}:
        raise SystemExit("crewai_config=fail:core_classes_missing")

    print("crewai_import=ok")
    print("crewai_config=ok")
    print(f"agent_count={len(agents)}")
    print(f"task_count={len(tasks)}")
    print("storage_boundary=project/local/home")
    print("llm_execution=not_run")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
