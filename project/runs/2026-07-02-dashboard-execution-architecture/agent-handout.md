# Dashboard Execution Architecture Handout

Date: 2026-07-02
Audience: next ArchFlow public project operator

## Title And Purpose

This handout records Prompt 1.2: the operational execution architecture for the Jarvis dashboard. Use it before starting Prompt 2.

## Human Summary

Prompt 1.2 defined the execution contract that Prompt 2 should render and implement as a static/browser-local dashboard MVP. A follow-up Level 3 CrewAI proof pass executed one deterministic local CrewAI fixture and integrated its status into the contract and dashboard schema.

The dashboard has two screens. `(1) PRD/ICP Flow` is the product-service path that turns approved product-team material into a context digest, PRD, task matrix, evidence cards, acceptance criteria, decision log, review packet, and handoff. `(2) Agent Orchestra` is the operator path that shows roles, assignments, bounded worker outputs, review gates, blockers, handoffs, and final decisions.

The most important boundary is execution level. Level 1 configured roles are active as YAML/docs. Level 2 LangGraph-wrapped role execution is the intended architecture. Level 3 direct CrewAI runtime is now `proof_passed_not_default_runtime` for a tiny deterministic local fixture only. OpenRouter is server-side only and remains disabled until backend/local-bridge, secret, ledger, budget, and review gates pass.

Owner budget update: OpenRouter may be planned with a 5.00 USD daily cap and must always stay under 2.00 USD per run. The config uses 1.99 USD as the hard per-run threshold and requires stop-and-ask behavior above the cap.

Level 3 clarification: direct CrewAI runtime was blocked only because proof was missing. The proof pass now exists under `project/runs/2026-07-02-crewai-level-3-proof/`. It used a tiny public-safe PRD/ICP fixture, ledger, budget guard, deterministic output path, AF Review, public-safety scan, workflow validation, and runtime guard. Its status is `proof_passed_not_default_runtime`; a later owner approval is still required before any default/provider-backed CrewAI runtime.

Prompt 2 can now proceed only as a static/browser-local MVP implementation against this contract. It cannot activate provider calls, Railway/backend, direct CrewAI execution, Nexus/Notion/GitHub/WikiLLM writeback, Telegram, owner-device voice proof, production promotion, or Figma sync.

## Current State

Task status:

- Prompt 1 consolidation: complete.
- Prompt 1.2 execution architecture: complete after this handout and live-log completion entry.
- Prompt 2: allowed only after reading this handout, the architecture report, and the latest live communication log.

Main artifacts:

- `project/reports/2026-07-02-dashboard-execution-architecture.md`
- `project/runs/2026-07-02-dashboard-execution-architecture/agent-handout.md`
- `wiki/runs/2026-07-02-dashboard-execution-architecture.md`

Config contracts updated:

- `project/agentic-stack.md`
- `project/agents/agent-roster.yaml`
- `project/workflows/langgraph-controller.yaml`
- `project/workflows/crewai-crew.yaml`
- `project/config/model-routing.yaml`

Runtime readiness:

- Static/browser-local dashboard proof exists from prior runs.
- LangGraph config and smoke proof exist from prior runs.
- CrewAI config/import proof exists.
- Direct CrewAI deterministic local fixture proof passed under `project/runs/2026-07-02-crewai-level-3-proof/`.
- No active OpenRouter runtime evidence exists.
- No canonical provider-backed model-call ledger exists.
- Backend/local bridge, live writeback, owner-device voice proof, Telegram, and production promotion remain gated.

## Agent Continuation Prompt

```text
You are continuing ArchFlow Prompt 2 after Prompt 1 and Prompt 1.2.

Work in the public project. First read:
- project/operating-rules.md
- project/live/communication/README.md
- project/live/communication/current-agent-notice.md
- the latest entries in project/live/communication/agent-communication-log.md
- project/reports/2026-07-02-jarvis-dashboard-icp-task-consolidation.md
- project/reports/2026-07-02-dashboard-execution-architecture.md
- project/runs/2026-07-02-dashboard-execution-architecture/agent-handout.md
- project/agentic-stack.md
- project/workflows/langgraph-controller.yaml
- project/workflows/crewai-crew.yaml
- project/config/model-routing.yaml

Goal: implement only the static/browser-local Jarvis dashboard MVP against the Prompt 1.2 contract. Render two screens: (1) PRD/ICP Flow and (2) Agent Orchestra. Show Level 1 configured roles, Level 2 LangGraph-wrapped target architecture, and Level 3 direct CrewAI as proof_passed_not_default_runtime. Show OpenRouter as server-side and disabled until backend/local-bridge, secret, ledger, budget, and review gates pass.

Before editing, inspect git status and live file claims, then append a starting entry to the live communication log.

Allowed: dashboard UI/schema/data work, browser-local packets, runtime labels, local export packets, generated dashboard data, static smoke tests, and validation.

Blocked without separate approval: OpenRouter/provider activation, Railway/backend/local bridge, default/provider-backed CrewAI runtime, live Nexus/Notion/GitHub/WikiLLM writeback, Telegram delivery, raw voice persistence, owner-device voice proof, production promotion, and Figma sync.

Required checks: public safety scan, JS syntax, dashboard JSON parse, workflow validation, runtime guard if local runtime allows it, dashboard static smoke, and git diff hygiene.
```

## Execution Trace

FACT:

- Read the public operating rules, live communication contract, current notice, and latest communication log.
- Appended a starting entry and writing update before editing shared files.
- Read Prompt 1 outputs and current dashboard, LangGraph, CrewAI, OpenRouter, role, and model-efficiency evidence.
- Ran six bounded read-only reviewer lanes for Screen 1, Screen 2, LangGraph, CrewAI, OpenRouter/backend, and Prompt 2 readiness.
- Integrated reviewer findings into config/docs and this report set.

INTERPRETATION:

- The static dashboard should render an execution contract, not imply autonomous runtime.
- LangGraph remains the controller.
- CrewAI has a deterministic local Level 3 proof package, but is not the default or provider-backed runtime.
- OpenRouter routing is useful only after a server-side route and canonical ledger exist.

GAP:

- No provider-backed model-call ledger.
- No backend/local bridge.
- No provider runtime.
- No default/provider-backed CrewAI runtime proof.
- No live writeback.
- No production/voice/Telegram proof.

## Decisions

- Keep Prompt 2 limited to static/browser-local dashboard MVP work.
- Treat Level 1 configured roles as active.
- Treat Level 2 LangGraph-wrapped role execution as the target architecture.
- Treat Level 3 direct CrewAI runtime as proof_passed_not_default_runtime for the deterministic local fixture only.
- Treat OpenRouter logging as an activation blocker, not a later improvement.
- Set OpenRouter budget policy to 5.00 USD per day and always under 2.00 USD per run.
- Keep Level 3 at proof_passed_not_default_runtime until a later approval explicitly promotes default/provider-backed runtime.
- Keep browser config edits as exportable review packets, not direct source writes.

## Artifacts

| Artifact | Purpose |
|---|---|
| `project/reports/2026-07-02-dashboard-execution-architecture.md` | Main Prompt 1.2 architecture report and Prompt 2 readiness decision. |
| `project/agentic-stack.md` | Human-readable stack contract and two-screen execution model. |
| `project/agents/agent-roster.yaml` | Operator role mapping, status model, blocker model, and runtime labels. |
| `project/workflows/langgraph-controller.yaml` | Two-lane LangGraph screen contract and disabled boundaries. |
| `project/workflows/crewai-crew.yaml` | CrewAI execution levels, task policy, and dashboard/operator roles. |
| `project/config/model-routing.yaml` | OpenRouter disabled-state behavior, ledger schema, and activation gates. |
| `project/runs/2026-07-02-crewai-level-3-proof/` | Direct CrewAI deterministic fixture proof, ledger, budget guard, AF Review, and dashboard state. |
| `wiki/runs/2026-07-02-dashboard-execution-architecture.md` | Durable public WikiLLM run note. |

## Validation

Checks run:

- Pass: `python3 project/scripts/generate-dashboard-data.py`
- Pass with project-local runtime: `project/local/venv/bin/python project/scripts/validate-workflows.py`
- Pass with project-local runtime: `project/local/venv/bin/python project/scripts/crewai-config-check.py`
- Pass: dashboard JSON parse.
- Pass: `node --check project/dashboard/app.js`
- Pass: `python3 scripts/public_safety_scan.py`
- Pass: `git diff --check`
- Pass: `project/local/venv/bin/python project/scripts/pre-push-runtime-guard.py`
- Pass after approved unsandboxed rerun: `project/local/venv/bin/python project/scripts/dashboard-static-smoke.py`, with eight rendered routes, zero provider calls, and zero writeback.

Initial system-Python workflow and CrewAI checks failed because system Python lacked `yaml`; the project-local runtime checks passed.

## Next Actions

1. Finish validation for Prompt 1.2.
2. Append the live-log completion entry.
3. Start Prompt 2 only after reading this handout and classifying dirty worktree ownership.
4. Implement static/browser-local dashboard changes only.
5. Add a model-call ledger before any future OpenRouter activation.

## Safety Boundary

Do not store secrets, credential values, raw private source text, local absolute paths, private URLs, account identifiers, raw screenshots, raw voice/audio, or unapproved uploaded document bodies in public files. Use repo-relative paths and public-safe summaries only.
