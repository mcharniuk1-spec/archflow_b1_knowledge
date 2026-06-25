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
LangSmith tracing is configured for project ID `057edf33-a328-4186-9425-3306186149ef` and awaits the API key in an ignored local env file.
LangGraph, CrewAI, and LlamaIndex are configured as workflow contracts, but their runtime packages are not installed yet.
