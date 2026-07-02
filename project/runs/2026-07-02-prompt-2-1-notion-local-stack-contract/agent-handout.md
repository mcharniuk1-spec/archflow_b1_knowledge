# Prompt 2.1 Notion And Local Jarvis Stack Contract Handout

## Title And Purpose

This handout records Prompt 2.1 after Prompt 2 completed and was merged to `main`.

Use it to continue Notion/task architecture, local Jarvis stack operation, or Prompt 3 coordination without reopening the whole chat.

## Human Summary

Prompt 2.1 clarified the operating layer around the Jarvis dashboard rather than activating new runtime. The work creates two project-local skills: `arcagcom` for parallel-agent communication and `archflow1` for local Jarvis stack operation.

The local Jarvis manual now explains how Dashboard Screen 1, Dashboard Screen 2, `jarvis-api`, LangGraph, CrewAI, OpenRouter, STT, TTS, and Railway relate. It carries forward the owner-decision gates: full PRD/ICP test cycle, FastAPI dependency/runtime proof, OpenRouter activation/budget ledger, and Railway/Telegram/production/Figma/writeback decisions.

Notion optimization is handled as evidence-backed clarification. Duplicate-looking E1.3.8/E1.3.9/E1.3.10/JDB rows are mapped by meaning. No page was deleted, no private URLs were stored, and no runtime/provider status was upgraded without proof.

## Current State

Task status: complete for skills, docs, report, and append-only Notion/task clarification scope.

Main artifacts:

- `skills/arcagcom/SKILL.md`
- `skills/archflow1/SKILL.md`
- `docs/dashboard-local-jarvis-stack-manual.md`
- `project/reports/2026-07-02-prompt-2-1-notion-local-stack-contract.md`
- `wiki/runs/2026-07-02-prompt-2-1-notion-local-stack-contract.md`

Runtime state:

- Dashboard static/browser-local surface remains reliable.
- `jarvis-api` remains a provider-disabled contract.
- FastAPI runtime proof remains dependency-gated.
- OpenRouter remains disabled.
- CrewAI Level 3 remains `proof_passed_not_default_runtime`.
- Railway, Telegram, production/Figma sync, dashboard-driven writeback, and full PRD/ICP test cycle remain owner-gated.

## Agent Continuation Prompt

Continue from Prompt 2.1. Read `project/operating-rules.md`, `project/live/communication/README.md`, the latest communication log, this handout, `project/reports/2026-07-02-prompt-2-1-notion-local-stack-contract.md`, `skills/arcagcom/SKILL.md`, and `skills/archflow1/SKILL.md`.

Goal: keep Notion/task state, dashboard runtime claims, and Prompt 3 coordination aligned without activating gated runtime.

First steps:

1. Confirm whether Prompt 3 has posted a completion or handoff update.
2. If Prompt 3 changed website files, review branch relation and conflicts before any final merge.
3. Keep OpenRouter, FastAPI dependency install, Railway, Telegram, production/Figma sync, and dashboard-driven writeback approval-gated.
4. Run public safety and runtime guard before push.

Stop condition: stop before provider calls, dependency installs, external sends, production promotion, or full PRD/ICP test execution unless owner approval is explicit.

## Execution Trace

FACT:

- Prompt 2 was already on `main` at commit `9f0dd60`.
- `arcagcom` and `archflow1` were created as project-local skills.
- The local dashboard/Jarvis manual was created.
- A duplicate/drift map was created for the shorthand task confusion.
- Notion updates were scoped to exact rows and kept append-only or note-only.

INTERPRETATION:

- The current task board is best optimized by clarifying row meanings, not by deleting history.
- JDB-8, JDB-9, and JDB-10 are Done only for static/browser-local scope.
- E1.3.9 and secure dashboard gate remain Review because live runtime gates are not complete.

GAP:

- FastAPI runtime proof still needs approved dependency install and service start.
- Full PRD/ICP test cycle still needs owner approval.
- Provider-backed budget ledger does not exist because provider calls remain disabled.
- Telegram send remains deferred.

## Decisions

- Keep duplicate-looking E1.3.x rows, but clarify their purpose and blocker.
- Keep `MODEL_PROVIDER=none` as the safe default.
- Keep CrewAI Level 3 as proof-only, not default runtime.
- Treat Prompt 3 as the website visual/code lane.

## Artifacts

| Artifact | Purpose |
|---|---|
| `skills/arcagcom/SKILL.md` | Live-agent communication and Prompt 2.1/Prompt 3 coordination skill. |
| `skills/archflow1/SKILL.md` | Local Jarvis stack operating skill. |
| `docs/dashboard-local-jarvis-stack-manual.md` | Dashboard/local backend/manual operating guide. |
| `project/reports/2026-07-02-prompt-2-1-notion-local-stack-contract.md` | Notion drift map, status interpretation, owner gates, and review result. |
| `wiki/runs/2026-07-02-prompt-2-1-notion-local-stack-contract.md` | Durable public WikiLLM run note. |

## Validation

Checks passed:

- `python3 scripts/public_safety_scan.py`
- `python3 project/scripts/generate-dashboard-data.py`
- dashboard JSON parse
- `node --check project/dashboard/app.js`
- Python syntax compile for Jarvis API and dashboard scripts
- `project/local/venv/bin/python project/scripts/validate-workflows.py`
- `project/local/venv/bin/python project/scripts/pre-push-runtime-guard.py`
- dashboard static smoke: `routes=8`, `provider_calls=0`, `writeback=0`
- `git diff --check`

Dependency-gated:

- FastAPI live runtime proof remains blocked until owner-approved dependency install and service start.

## Next Actions

1. Wait for explicit owner approval before full PRD/ICP test cycle.
2. Install FastAPI dependencies only after owner approval.
3. Activate OpenRouter only after server-side secret, fresh pricing, ledger, and budget guard proof.
4. Keep Railway, Telegram, production/Figma sync, and dashboard-driven writeback gated.

## Safety Boundary

Do not store secrets, private URLs, raw Notion content, Telegram IDs, local absolute paths, raw transcripts, screenshots, credentials, or account identifiers in public files.
