#!/usr/bin/env python3
"""Send one public-safe LangSmith smoke trace.

This script reads the ignored local env file and sends only sanitized metadata.
It does not call any cloud model.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT / "project" / ".env.langsmith.local"


def load_env(path: Path) -> None:
    if not path.exists():
        raise SystemExit(f"Missing local env file: {path.relative_to(ROOT)}")
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def main() -> int:
    load_env(ENV_FILE)
    if not os.environ.get("LANGSMITH_API_KEY"):
        raise SystemExit("LANGSMITH_API_KEY is blank in the ignored local env file.")

    try:
        from langsmith import traceable
    except ModuleNotFoundError:
        raise SystemExit("LangSmith SDK is not installed in the active Python environment.")

    os.environ.setdefault("LANGSMITH_TRACING", "true")
    os.environ.setdefault("LANGSMITH_PROJECT", "ArchFlow")

    @traceable(
        name="archflow_public_smoke_trace",
        project_name=os.environ["LANGSMITH_PROJECT"],
        tags=["archflow", "public-safe", "smoke", "ollama-only"],
    )
    def smoke_trace() -> dict[str, str]:
        return {
            "status": "ok",
            "scope": "public-safe-smoke-trace",
            "model_execution": "ollama-only",
            "cloud_model_call": "false",
        }

    smoke_trace()
    print("langsmith_smoke_trace=submitted")
    print("project=ArchFlow")
    print("model_execution=ollama_only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
