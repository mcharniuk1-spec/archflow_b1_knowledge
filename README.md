# ArchFlow Public Project

This folder is the clean public-safe project root for the ArchFlow reset.

All active work after the 2026-06-24 reset belongs under `project/`.
Prior work is represented only as sanitized English summaries under `history/`.

## Start Here

**ArchFlow turns scattered product knowledge into a reviewable operating system before the next high-stakes handoff.**

Choose the path that fits you:

- **Service buyer:** start with the [Knowledge Reliability Setup](project/agentic-stack.md#service-company-operating-model) and use the repository to understand the governed handoff you receive.
- **Operator:** open the [dashboard](project/dashboard/) to inspect the Knowledge Service and Agent Control flows, then download a browser-local review bundle for an approved operator.
- **Self-hosting evaluator:** follow the [quickstart](docs/quickstart.md), review the [architecture](docs/architecture.md), and use only public-safe example data.

The product is intentionally local-first. Its current public implementation explains and validates contracts, generated catalog data, browser-local drafts, and guarded review packets. It does not claim an active hosted agent platform.

## Three-Minute Local Demo

```bash
python3 project/scripts/generate-dashboard-data.py
python3 -m http.server 8765
```

Open `http://127.0.0.1:8765/project/dashboard/`, choose **Operations**, and prepare a review bundle. The animated stage sequence is a browser-local preparation preview. It never creates repository files, launches a subagent, calls a provider, or pushes Git.

## Documentation

- [Quickstart](docs/quickstart.md) — clean-clone local setup and verification.
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

- a three-block buyer-facing website built around the seven-layer ArchFlow tower, two delivery lanes, and a disclosed planning calculator;
- a documentation-first operator dashboard for architecture, knowledge, roles, skills, workflow state, runs, and proof;
- a separate provider-disabled Jarvis surface with owner, model-allowlist, and acknowledgement checks plus a mandatory durable-control execution block;
- an E1-E8 plan whose final gated milestone is a locally installable repository, least-privilege MCP, administration plane, and lifecycle documentation.

Local implementation proof does not establish production deployment, live provider execution, validated demand, or autonomous writeback.
