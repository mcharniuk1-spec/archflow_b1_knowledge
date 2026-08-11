#!/usr/bin/env python3
"""Validate the CrewAI contract without running an LLM task."""

from __future__ import annotations

import argparse
import importlib.metadata
import importlib.util
import os
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
CONFIG = PROJECT / "workflows" / "crewai-crew.yaml"


def configure_local_crewai_runtime() -> None:
    local_home = PROJECT / "local" / "home"
    local_home.mkdir(parents=True, exist_ok=True)
    os.environ["CREWAI_STORAGE_DIR"] = str(local_home / "crewai")
    os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
    os.environ["CREWAI_DISABLE_TRACKING"] = "true"
    os.environ["OTEL_SDK_DISABLED"] = "true"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--deep-import",
        action="store_true",
        help="Import CrewAI core classes. This can be slow and is not part of the default provider-disabled setup check.",
    )
    args = parser.parse_args()
    configure_local_crewai_runtime()

    data = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    agents = data.get("agents", {})
    tasks = data.get("tasks", [])
    task_agent_ids = {task.get("agent") for task in tasks}
    missing_agents = sorted(agent_id for agent_id in task_agent_ids if agent_id not in agents)
    if missing_agents:
        raise SystemExit(f"crewai_config=fail:missing_task_agents:{','.join(missing_agents)}")

    if importlib.util.find_spec("crewai") is None:
        raise SystemExit("crewai_config=fail:distribution_not_discoverable")
    version = importlib.metadata.version("crewai")

    if args.deep_import:
        from crewai import Agent, Crew, Task

        if not {Agent, Crew, Task}:
            raise SystemExit("crewai_config=fail:core_classes_missing")
        print("crewai_deep_import=ok")
    else:
        print("crewai_deep_import=not_run")

    print(f"crewai_distribution={version}")
    print("crewai_module=discoverable")
    print("crewai_config=ok")
    print(f"agent_count={len(agents)}")
    print(f"task_count={len(tasks)}")
    print("storage_boundary=project/local/home")
    print("llm_execution=not_run")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
