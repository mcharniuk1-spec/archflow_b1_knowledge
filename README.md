# ArchFlow Public Project

This folder is the clean public-safe project root for the ArchFlow reset.

All active work after the 2026-06-24 reset belongs under `project/`.
Prior work is represented only as sanitized English summaries under `history/`.

## Start Here

**ArchFlow turns scattered product knowledge into a reviewable operating system before the next high-stakes handoff.**

Choose the path that fits you:

- **Service buyer:** start with the [Knowledge Reliability Setup](project/agentic-stack.md#service-company-operating-model) and use the repository to understand the governed handoff you receive.
- **Operator or new employee:** start with the [unified operating architecture](docs/unified-operating-architecture.md) and [onboarding knowledge agent](docs/onboarding-knowledge-agent.md); the dashboard remains a legacy-compatible, browser-local projection until its separate migration plan is executed.
- **Self-hosting evaluator:** follow the [quickstart](docs/quickstart.md), review the [architecture](docs/architecture.md), and use only public-safe example data.

The product is intentionally local-first. Its current public implementation explains and validates contracts, generated catalog data, browser-local drafts, and guarded review packets. It does not claim an active hosted agent platform.

## Three-Minute Local Demo

```bash
python3 project/scripts/generate-dashboard-data.py
python3 -m http.server 8765
```

Open `http://127.0.0.1:8765/project/dashboard/#manual`, choose **Knowledge Service**, and prepare a local report. Download/review it, then use **Agent Control** to prepare a role handoff. The animated stage sequence is browser-local only. It never creates repository files, launches a subagent, calls a provider, or pushes Git.

## Documentation

- [Documentation index](docs/index.md) — canonical navigation and status/supersession legend.
- [Unified operating architecture](docs/unified-operating-architecture.md) — one knowledge case, normalized roles, evidence, validation, review, and promotion.
- [Onboarding knowledge agent](docs/onboarding-knowledge-agent.md) — role-safe employee support and requirement-validated action proposals.
- [Executed role and knowledge trace](docs/executed-role-and-knowledge-trace.md) — how research, outreach, creative, design, review, and promotion became role contracts.
- [Adapt ArchFlow](docs/adapting-archflow.md) — replace the synthetic fixture without weakening boundaries.
- [Orbit Local adapter](docs/orbit-local-integration.md) — optional code-structural evidence with a strict private runtime seam.
- [Dashboard integration plan](docs/dashboard-integration-plan.md) — future plan only; no dashboard migration is claimed.
- [Quickstart](docs/quickstart.md) — clean-clone local setup and verification.
- [Dashboard operating manual](docs/dashboard-operating-manual.md) — two-stage knowledge/agent-control flow, Jarvis prompts, configuration points, skills, roles, outputs, and limits.
- [Architecture](docs/architecture.md) — seven grouped layers and the long-term product path.
- [Operations](docs/operations.md) — input meanings, stage sequence, review-bundle workflow, and real-action gates.
- [API contract](docs/api-contract.md) — guarded API shapes and fail-closed behavior.
- [Security and data boundaries](docs/security-and-data-boundaries.md) — what may be public, local, or gated.
- [Contributing](CONTRIBUTING.md) and [security reporting](SECURITY.md).

## What Is Gated Or Not Included

- No provider-backed model execution by default.
- No autonomous files, Git changes, Git push, Notion/Nexus memory writeback, deployment, or external action from the browser.
- No customer corpus, private source ingestion, credentials, device paths, or public copy of the operator's larger private skill inventory.
- No live database or arbitrary SQL console. The dashboard Data Lab is a read-only preview over generated public JSON.
- No production, availability, ROI, demand, or continuous-monitoring claim without current evidence.

## Public Boundary

This folder is intended to be safe to push to a public Git repository.

Rules:

- Use English only.
- Use repo-relative paths only.
- Do not store personal names, private workspace links, local absolute paths, user IDs, account IDs, API keys, tokens, cookies, passwords, or raw credentials.
- Do not copy raw Notion exports, old PDFs, screenshots, Vercel metadata, API files, browser logs, or private source files into this folder.
- Store provider settings only as examples or non-secret configuration.
- Treat Codex as the operator runtime. Do not claim Codex auth is an API key for external frameworks.

## Folder Map

| Folder | Purpose |
|---|---|
| `project/` | Current post-reset project, operating rules, plan, agent stack, provider setup. |
| `history/` | Public-safe summaries and inventories of pre-reset ArchFlow work. |
| `skills/` | Skills and agent hooks used for this project. |
| `wiki/` | Public WikiLLM memory layer for project instructions, runs, decisions, issues, and insights. |

## Current Project Direction

ArchFlow is a knowledge-continuity operating system for companies that need a maintained, source-grounded company brain and bounded agent execution.

The current service wedge is:

`forcing moment -> source and ownership map -> reviewed knowledge spine -> governed agent workflows -> measured handoff`

PRDs, ICPs, content, outreach, and other execution packs are generated architectures inside that system; they are not the whole product identity.

The current public-safe implementation includes:

- a provider-disabled unified knowledge-case contract with synthetic onboarding and action-validation fixtures;
- a three-block buyer-facing website built around the seven-layer ArchFlow tower, two delivery lanes, and a disclosed planning calculator;
- a documentation-first operator dashboard for architecture, knowledge, roles, skills, workflow state, runs, and proof;
- a separate provider-disabled Jarvis surface with owner, model-allowlist, and acknowledgement checks plus a mandatory durable-control execution block;
- an E1-E8 plan whose final gated milestone is a locally installable repository, least-privilege MCP, administration plane, and lifecycle documentation.

Local implementation proof does not establish production deployment, live provider execution, validated demand, or autonomous writeback.

The two delivery lanes and numbered dashboard labels are compatibility surfaces, not the canonical system architecture. PRDs, ICPs, market research, content, outreach, and creative work are bounded role outputs inside one governed knowledge-case workflow.
