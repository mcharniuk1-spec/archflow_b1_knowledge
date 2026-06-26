# Current Project

This is the active ArchFlow project after the 2026-06-24 reset.

## Mission

Build a repeatable public-safe system that converts messy work material into execution assets:

1. Source material: dialogue, chat, meeting notes, transcript, or planning note.
2. Structured context: facts, interpretations, hypotheses, gaps.
3. PRD: goal, scope, inputs, outputs, acceptance criteria.
4. Task plan: owners, responsibilities, timeline, blockers.
5. Knowledge base update: reusable project memory and decisions.
6. Review gate: public-safety, evidence, and next-action check.

## Active Folders

| Folder | Purpose |
|---|---|
| `config/` | Public-safe provider and model configuration templates. |
| `workflows/` | LangGraph, CrewAI, and LlamaIndex workflow contracts. |
| `dashboard/` | Phase 2 local read-only operator dashboard. |
| `outputs/` | Output document templates for proof runs. |
| `reports/` | Setup and review reports by layer. |
| `prompts/` | Reusable public-safe prompts. |
| `scripts/` | Public-safe helper scripts. |
| `runs/` | Future public-safe run summaries. |

## Current Status

The plan has been imported from the private project board as an English public-safe summary.
Codex authentication is the main operator and publication path for this setup.
Ollama is connected for local minor/background tasks.
Qwythos is installed and now generates text through Ollama.
`gemma4:e4b` remains the verified local fallback model.
LangSmith tracing is configured for project ID `057edf33-a328-4186-9425-3306186149ef`; keys stay only in ignored local env files.
LangGraph is installed and has passed a sanitized smoke workflow.
LlamaIndex is installed and has passed approved-corpus retrieval over public files.
CrewAI is installed and has passed config/import validation without LLM task execution.
Graphify output exists for the public repository.

## Local Dashboard

The local dashboard is a read-only Phase 2 control panel, not the primary project brain.
It reads public project files and ignored local env presence, then displays WikiLLM memory, recent run/report activity, LangGraph nodes, CrewAI roles, LlamaIndex corpus boundaries, LangSmith readiness, and env/package status.

Run it from the repository root:

```bash
python3 project/scripts/generate-dashboard-data.py
python3 -m http.server 8765
```

Open `http://127.0.0.1:8765/project/dashboard/`.
