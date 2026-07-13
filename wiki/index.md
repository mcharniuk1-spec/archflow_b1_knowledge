# ArchFlow Public WikiLLM

This is the public WikiLLM layer for the ArchFlow Block 1 knowledge project.

It stores durable public-safe project memory, decisions, run records, issues, insights, and operating rules.

## Read Order

1. `../README.md`
2. `../AGENTS.md`
3. `../project/README.md`
4. `../project/operating-rules.md`
5. `../project/config/model-routing.yaml`
6. `memory.md`
7. `insights.md`
8. `rules/public-wikillm-contract.md`
9. latest file in `runs/`
10. open files in `issues/`
11. latest files in `decisions/`

## Current Architecture Baseline

- `../project/strategic-plan-2026-07-13.md` - knowledge-architecture-first E1-E8 plan and proof gates.
- `../project/proof-ledger.md` - canonical evidence routing, state definitions, and narrow current proof boundaries.
- `../project/reports/2026-07-13-self-supporting-agentic-architecture-review.md` - current design audit, tool decisions, and remaining runtime gaps.
- `../project/reports/2026-07-13-icp-audience-product-surface.md` - ICP translation, audience architecture, website/dashboard/Jarvis implementation, and productization path.
- `../project/knowledge/audience/icp-knowledge-continuity.md` - segmented forcing moments, buyers, channels, content, tools, and evidence-update contract.
- `../project/agents/marketing-role-pack.md` - marketing-role graph, skill assignments, gates, and evidence handoffs.
- `../project/task-contract-index-2026-07-13.md` - public-safe E1-E8 objectives, dependencies, artifacts, and proof gates.
- `../project/runs/2026-07-13-icp-product-surface/agent-handout.md` - current implementation evidence and next safe contract.
- `../project/goals/README.md` - Goal Engineering contract and maturity levels.
- `../skills/archflow-architecture-operator/SKILL.md` - reusable architecture-factory procedure.
- `decisions/2026-07-13-goal-loop-architecture-factory-baseline.md` - accepted design decision.
- `decisions/2026-07-13-icp-forcing-moment-public-surface.md` - accepted knowledge-continuity positioning and surface decision.
- `issues/2026-07-13-architecture-runtime-proof-gates.md` - open proof and adoption gates.
- `issues/2026-07-13-jarvis-durable-execution-controls.md` - atomic approval and spend-ledger blocker.
- `runs/2026-07-13-icp-product-surface.md` - durable run record for the ICP, website, dashboard, Jarvis, and task-board update.

## Project Identity

| Field | Value |
|---|---|
| Project | ArchFlow Block 1 Knowledge |
| Public repository | `mcharniuk1-spec/archflow_b1_knowledge` |
| Active work folder | `project/` |
| Public history folder | `history/` |
| Skill registry | `skills/` |
| WikiLLM folder | `wiki/` |

## Active Layers

| Layer | Status |
|---|---|
| Public repository | Published. |
| Codex operator | Primary operator and review layer. |
| Ollama | Local model execution only. |
| Qwythos | Active local model after load verification. |
| LangSmith | Tracing configured; sanitized smoke traces submitted. |
| LangGraph | Runtime installed; smoke workflow passed. |
| CrewAI | Runtime installed; config/import check passed with no LLM execution. |
| LlamaIndex | Runtime installed; approved-corpus retrieval proof passed. |
| WikiLLM | Public project memory configured in this folder. |

## Safety Boundary

This wiki must not contain:

- API keys, tokens, cookies, passwords, or raw credentials.
- Private workspace links.
- Local absolute paths.
- Raw private transcripts or exports.
- Personal identifiers not needed for public project operation.
