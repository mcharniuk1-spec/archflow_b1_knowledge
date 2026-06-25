# Local Operator Dashboard

This is the Phase 2 local dashboard for ArchFlow Block 1.

It is a read-only control panel generated from public project files. It is not the project brain and it does not replace WikiLLM, Obsidian, LangSmith, GitHub, or Codex.

## Run

From the repository root:

```bash
python3 project/scripts/generate-dashboard-data.py
python3 -m http.server 8765
```

Open:

```text
http://127.0.0.1:8765/project/dashboard/
```

## What It Shows

- Overview and recent activity.
- WikiLLM memory, decisions, issues, and runs.
- Graphify status and future graph links.
- LangGraph nodes, routing, review gates, and stop logic.
- LlamaIndex-style local query test over approved public files.
- CrewAI agents, roles, tasks, and expected outputs.
- LangSmith tracing readiness and safe trace rules.
- Env/config and runtime package status.

## Boundary

The dashboard reads public-safe files and ignored local env presence only. It must not display real API keys, raw private transcripts, private workspace links, or local absolute paths.
