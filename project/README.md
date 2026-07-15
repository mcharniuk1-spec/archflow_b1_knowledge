# Current Project

This is the active ArchFlow project after the 2026-06-24 reset.

## Mission

Build a repeatable public-safe knowledge-continuity system that converts fragmented company material into maintained knowledge and governed execution:

1. Identify the forcing moment, objective, authority, corpus, owners, and stop conditions.
2. Assemble source-grounded context with facts, interpretations, hypotheses, and gaps kept distinct.
3. Connect bounded retrieval, semantic knowledge, generated structure, and durable reviewed memory.
4. Route work through explicit role, skill, state, approval, verification, and repair contracts.
5. Produce task-specific architectures such as PRD, ICP, content, outreach, research, or engineering packs.
6. Promote only reviewed knowledge deltas and record proof, rollback, and the next safe action.

## Active Folders

| Folder | Purpose |
|---|---|
| `config/` | Public-safe provider and model configuration templates. |
| `workflows/` | LangGraph, CrewAI, and LlamaIndex workflow contracts. |
| `loops/` | Loop Engineering contract, state schema, budget, run log, and readiness review. |
| `goals/` | Goal Engineering contracts, lifecycles, authority, and stop conditions. |
| `knowledge/` | Public-safe audience and role-specific knowledge routing. |
| `agents/` | Role, skill, routing, and marketing-division contracts. |
| `dashboard/` | Documentation-first operator console and browser-local workflow editor. |
| `outputs/` | Output document templates for proof runs. |
| `reports/` | Setup and review reports by layer. |
| `prompts/` | Reusable public-safe prompts. |
| `scripts/` | Public-safe helper scripts. |
| `runs/` | Future public-safe run summaries. |

## Current Status

- The E1-E8 strategic spine centers knowledge continuity, with PRD/ICP and marketing execution treated as generated workflow architectures.
- LangGraph owns orchestration state; Goal Engineering defines observable completion; Loop Engineering repairs bounded work; WikiLLM remains canonical durable public memory.
- Obsidian is the human semantic layer, Graphify is generated structure, Nexus is a live bridge only after current runtime proof, and LlamaIndex is bounded retrieval with lexical rollback.
- Cognee, TurboVec, provider-backed Jarvis, autonomous writeback, and the E8 installable product remain gated candidates rather than default runtime claims.
- The local/public website, dashboard, and guarded Jarvis contracts have implementation and browser/API-contract proof. Production freshness, live owner-authenticated provider execution, durable spend enforcement, and validated demand remain unproven.
- The current ICP is a 30-75-person product-led B2B SaaS hypothesis led by enterprise-readiness, onboarding, and key-person-departure forcing moments. It requires primary interviews and paid-start evidence.

## Local Surfaces

The repository root serves the three-block website. The dashboard explains and edits browser-local architecture packets; it is not a shadow source of truth. The separate Jarvis page prepares guarded model requests; it does not prove provider activation or permit direct writeback.

Run it from the repository root:

```bash
python3 project/scripts/generate-dashboard-data.py
python3 -m http.server 8765
```

Open `http://127.0.0.1:8765/project/dashboard/`.

Other local routes:

- website: `http://127.0.0.1:8765/`
- Jarvis: `http://127.0.0.1:8765/jarvis`

Authoritative state remains in repository contracts, reviewed run artifacts, and WikiLLM. Browser-local edits and exports are review candidates only.

## Public Product Navigation

- **Knowledge Service:** turns an approved source boundary into a reviewed PRD, ICP, decision, research, or backlog packet.
- **Agent Control:** turns an approved request into role contracts, task contracts, review gates, and a handoff for an approved operator.
- **Data Lab:** exposes only a read-only preview over generated public JSON; it is not a live database or arbitrary SQL console.

Use the root [quickstart](../docs/quickstart.md) for a clean clone, the [operations guide](../docs/operations.md) for every dashboard input and stage, and the [architecture guide](../docs/architecture.md) for the short-term service and long-term toolkit view.
