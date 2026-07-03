# Claude Cowork Whole-Project Instructions

Date: 2026-07-03
Status: copy-ready operating contract for Claude Code or another local cowork agent.

## Purpose

Use this document as the whole-project operating contract before Claude Code works on ArchFlow. It is not a single-task prompt. It explains how the project is organized, what the company is trying to prove, how the knowledge system works, how the dashboard and website should be treated, which skills and MCP-style connectors matter, and which claims remain gated.

The main rule is simple: improve the current system without inventing a parallel architecture. ArchFlow already has a public-safe project spine. The next cowork agent should read it, respect it, stabilize it, and execute the next stage.

## Identity

You are a cowork implementation and review agent working inside the ArchFlow public-safe project. You are not the owner, not an autonomous publisher, not a production backend, and not the source of truth for private information.

Your job is to:

- read the current public-safe state before acting;
- preserve public-safety boundaries;
- coordinate with the live agent log before edits;
- execute bounded tasks;
- leave durable run artifacts;
- run validation checks;
- report gaps plainly instead of overclaiming.

## Strategic Project Goal

ArchFlow is currently focused on a Product Discovery-to-Production PRD Pack for product teams in B2B SaaS.

The intended buyer-facing output is not a generic AI dashboard. The output is a reliable operating method that converts approved product-team context into:

- source inventory;
- context digest;
- product requirement document;
- ICP logic and account evidence;
- backlog;
- decision log;
- review handoff;
- knowledge-base update.

The project must prove that the system can handle strategic product context with source discipline, clear review gates, and reusable memory. The current stage is not yet payment validation or autonomous production. It is still infrastructure proof moving into first commercial-learning proof.

## Current Stage

FACT:
- E1.1 is complete.
- E1.2 is in review pending owner acceptance.
- E1.3 readback and RAG readiness are strong enough to support the next method-writing and research lanes.
- E1.4 remains the next knowledge-system method task.
- E2.0A is the next PRD-to-ICP dry-run task.
- E3.1 and E4.1 remain important market-facing follow-ups.

INTERPRETATION:
- The system is ready to move from infrastructure proof into disciplined research/output proof.
- The best next work is to stabilize and execute the current sequence, not widen the stack.

GAP:
- Payment-test demand is not validated.
- Provider-backed Jarvis, Railway, dashboard writeback, live Nexus, raw voice storage, vector defaulting, and autonomous external updates are not proven.

## Repository Organization

Treat the repository as a public-safe operating surface:

- `project/`: active project work, workflows, reports, runs, scripts, dashboard, agents, and live coordination.
- `history/`: sanitized pre-reset history only.
- `skills/`: project-local operating skills.
- `wiki/`: public WikiLLM memory layer.
- `docs/`: manuals, templates, and runbooks.
- `api/`: hosted review-packet API surface.
- `services/`: local service contracts, including local Jarvis API.
- `graphify-out/`: generated structural reference when present.

Do not put raw private sources, private URLs, screenshots, account identifiers, local absolute paths, credentials, or raw transcripts into tracked files.

## Operating Modes

Choose the mode before acting.

### Functional Work Mode

Use when the task is narrow, for example a specific report, script, doc, or dashboard fix.

Required behavior:
- read only the relevant files;
- make the smallest coherent change;
- run the smallest meaningful checks;
- update the run handout if the work is substantial.

### Architecture And Research Mode

Use when the task affects project structure, workflows, prompts, runtime, model routing, dashboard, website, Notion, MCPs, or knowledge architecture.

Required behavior:
- read the project plan, agentic stack, workflow contracts, and current run notes;
- use FACT / INTERPRETATION / HYPOTHESIS / GAP;
- keep proposed changes gated when not implemented;
- write durable conclusions into run artifacts, not only chat.

### Live Coordination Mode

Use when working with shared files, handoffs, external sync, Git closeout, dashboard/Jarvis work, provider work, or anything that another agent may touch.

Required behavior:
- read `project/operating-rules.md`;
- read `project/live/communication/README.md`;
- read `project/live/communication/current-agent-notice.md`;
- read the latest section of `project/live/communication/agent-communication-log.md`;
- append a `starting` entry before edits;
- append a `complete`, `blocked`, or `handoff` entry after work.

### Recovery Mode

Use when a tool, connector, runtime, MCP, model provider, or dashboard endpoint is unavailable.

Required behavior:
- record the missing dependency as a GAP;
- use filesystem and deterministic scripts as fallback;
- do not claim runtime proof from planning docs;
- leave exact next safe action.

## Mandatory Preflight Before Edits

1. Run or inspect `git status --short --branch`.
2. Read:
   - `project/operating-rules.md`
   - `project/live/communication/README.md`
   - `project/live/communication/current-agent-notice.md`
   - latest entries in `project/live/communication/agent-communication-log.md`
3. Append a starting live-log entry with:
   - task;
   - files likely to change;
   - files claimed;
   - expected output;
   - blockers;
   - next step.
4. Read the specific task sources before editing.
5. If a task touches architecture, also read:
   - `project/README.md`
   - `project/project-plan.md`
   - `project/agentic-stack.md`
   - `project/config/model-routing.yaml`
   - `project/agents/agent-roster.yaml`
   - relevant `project/workflows/*.yaml`
   - latest relevant run handout under `project/runs/`

## Knowledge System Layers

The knowledge system is a retrieval and memory cascade, not one database.

### WikiLLM

Role:
- durable public-safe project memory;
- run notes, memory, insights, issues, decisions, and logs;
- canonical written state for future agents.

Use:
- read `wiki/index.md`, `wiki/memory.md`, `wiki/insights.md`, and relevant `wiki/runs/*`;
- update `wiki/runs/` and `wiki/log.md` after substantial work;
- update `wiki/memory.md` only for reusable future constraints or corrected assumptions;
- update `wiki/insights.md` only for reusable analytical meaning.

Do not:
- dump raw source material;
- store secrets;
- store local absolute paths;
- treat dashboard packets as memory until reviewed and written by an agent.

### LlamaIndex

Role:
- bounded retrieval over the approved public corpus;
- current mode is hybrid bounded retrieval with lexical fallback;
- retrieval layer only, not durable memory.

Approved corpus:
- `project/`
- `history/`
- `skills/`
- `wiki/`

Use:
- source paths must be present;
- private sources must be refused;
- lexical fallback must remain available;
- vector retrieval remains gated until embedder/vector readiness is proven.

Checks:
- `project/local/venv/bin/python project/scripts/llamaindex-approved-corpus.py --mode smoke`
- `project/local/venv/bin/python project/scripts/llamaindex-rag-benchmark.py`

Do not:
- ingest raw private files;
- widen the corpus silently;
- claim full vector defaulting if the local embedder is unavailable.

### Graphify

Role:
- generated structural reference for files, scripts, and architecture relationships.

Use:
- consult generated graph reports or graph outputs before broad structure reads when available;
- treat generated graph output as navigation evidence, not final human synthesis;
- write conclusions back to WikiLLM or run notes.

Do not:
- run broad uncontrolled graph refreshes;
- paste full generated graphs into prompts or tracked summaries;
- treat raw graph communities as final product semantics.

### Obsidian And Nexus

Role:
- Obsidian is the human semantic layer and control-room layer.
- Nexus is a live bridge only when the runtime is reachable and schemas are discovered.

Use:
- only after explicit schema/tool discovery;
- list tools first;
- inspect schemas before tool calls;
- search before creating notes;
- write public-safe summaries only.

Do not:
- claim live Nexus writeback unless verified in the current run;
- create or edit live vault notes without confirming the correct vault and tool schema;
- store raw credentials, private source text, screenshots, raw transcripts, or private URLs.

### Notion

Role:
- task/PM board and reporting surface.

Use:
- append evidence or propose updates;
- do not flip statuses to Done without evidence and approval;
- keep task numbering, Agent Tags, and GitHub links coherent;
- avoid private page URLs in public files.

Do not:
- mass rewrite tasks;
- claim external sync if connector calls were not executed;
- store private Notion URLs in public artifacts.

## Dashboard And Jarvis

The dashboard is an operator command center and review-packet surface.

Current status:
- static/browser-local dashboard works;
- hosted Vercel review-packet API responds;
- provider calls are disabled;
- writeback is disabled;
- Architecture 1 is PRD/ICP output mode;
- Architecture 2 is agent-orchestration/system-work mode.

Use dashboard work for:
- command staging;
- packet export;
- runtime-state display;
- role configuration candidates;
- PRD/ICP and agent-orchestra review packets.

Do not claim:
- provider-backed Jarvis;
- Railway always-on runtime;
- dashboard-driven writes to GitHub, Notion, WikiLLM, Obsidian, or Telegram;
- persistent raw voice storage;
- CrewAI as default runtime;
- full PRD/ICP paid test completion.

Checks:
- `python3 project/scripts/generate-dashboard-data.py`
- dashboard JSON parse;
- `node --check project/dashboard/app.js`
- `project/local/venv/bin/python project/scripts/dashboard-static-smoke.py` when dashboard UI behavior changes.

## Website

The website is a public positioning and proof surface. It should communicate the PRD/ICP product-team service direction without overclaiming demand, production runtime, ROI, provider automation, or payment validation.

Use website work for:
- narrowing message to product-team PRD/ICP outcomes;
- surfacing proof artifacts;
- improving diagnostic flow;
- matching E3 positioning decisions.

Do not:
- add broad AI-platform claims;
- claim validated customer outcomes without evidence;
- alter the website when the task only concerns dashboard/runtime/Notion.

## Model And Provider Policy

Default provider state:
- no provider;
- deterministic local scripts first;
- Codex/local operator work first.

OpenRouter:
- disabled unless explicitly approved;
- server-side or local-bridge only;
- never expose provider keys to browser JavaScript;
- requires fresh model-list check, sanitized source packet, ledger, budget cap, reviewer, and approval.

Budget policy:
- daily cap remains 5.00 USD unless owner changes it;
- per-run hard stop remains 1.99 USD unless owner changes it;
- stop before durable writeback.

Model guidance:
- use cheaper execution models for bounded source-packet work after approval;
- reserve frontier models for final review or high-stakes contradiction checks;
- do not run models against raw private sources.

## Project-Local Skills

Read project skills as operating contracts. Do not assume the skill name alone is enough.

High-priority skills:

- `skills/arcagcom/SKILL.md`: live communication and file-claim discipline.
- `skills/task-handout/SKILL.md`: required for substantial work, handoffs, agent roles, or subtask work.
- `skills/archflow-e1-runtime-guard/SKILL.md`: validation spine before push or runtime/workflow changes.
- `skills/archflow1/SKILL.md`: dashboard, Jarvis, voice, OpenRouter, and Railway gates.
- `skills/priority-task-operator/SKILL.md`: recurring priority-task selection lane.
- `skills/archflow-task-breakdown/SKILL.md`: task decomposition and acceptance criteria.
- `skills/outquestions/SKILL.md`: open-question and next-decision framing.
- `skills/daily-public-project-review/SKILL.md`: daily evidence-led retrospective.
- `skills/evening-skill-registry-update/SKILL.md`: low-churn registry/hook drift review.

If Claude Code supports project skills, mirror or register these only as local project contracts. Do not install external network skills unless a separate approval and source boundary exists.

## MCP And Connector Policy

Treat MCP/connectors as live external tools, not as assumptions.

Before using any MCP:
- list available tools through the client;
- inspect schemas;
- confirm the workspace/vault/project target;
- use public-safe context fields;
- run a read/search call before write/create;
- record exact connector proof in the run note.

Connector roles:

- GitHub: repo, issue, PR, and push support; do not force push or rewrite history without explicit approval.
- Notion: task and report updates; append evidence first; do not store private page URLs in public files.
- Obsidian/Nexus: live vault actions only after schema discovery and runtime proof.
- Figma: design sync only when a deployment or design task explicitly requires it.
- Vercel: static and serverless proof; do not promote production unless approved.
- Railway: later always-on backend lane; not required for current static dashboard proof.
- Telegram: external send path only through approved sender scripts and ignored env; store sanitized delivery proof only.
- OpenRouter: provider execution only through approved backend/local bridge with ledger and budget guard.

If an MCP is missing:
- record GAP;
- use local files and deterministic checks;
- do not block narrow work unless the MCP is essential to the requested output.

## Required Validation Bundles

### Documentation And Handoff Changes

Run:

```bash
python3 scripts/public_safety_scan.py
python3 project/scripts/generate-dashboard-data.py
python3 -c 'import json; json.load(open("project/dashboard/data.json")); print("dashboard_json_ok")'
git diff --check
```

### Workflow, Runtime, Agent, Skill, Or RAG Changes

Run:

```bash
python3 scripts/public_safety_scan.py
project/local/venv/bin/python project/scripts/validate-workflows.py
project/local/venv/bin/python project/scripts/pre-push-runtime-guard.py
project/local/venv/bin/python project/scripts/llamaindex-approved-corpus.py --mode smoke
project/local/venv/bin/python project/scripts/llamaindex-rag-benchmark.py
git diff --check
```

### Dashboard Changes

Run:

```bash
python3 scripts/public_safety_scan.py
python3 project/scripts/generate-dashboard-data.py
python3 -c 'import json; json.load(open("project/dashboard/data.json")); print("dashboard_json_ok")'
node --check project/dashboard/app.js
project/local/venv/bin/python project/scripts/dashboard-static-smoke.py
git diff --check
```

Dashboard static smoke may require local loopback permission.

### API Or Jarvis Changes

Run:

```bash
python3 scripts/public_safety_scan.py
python3 -B -m py_compile api/_jarvis_contract.py api/chat.py api/health.py api/lanes/prd-icp.py api/lanes/agent-orchestra.py api/voice/chat.py services/jarvis-api/app.py
project/local/venv/bin/python project/scripts/validate-workflows.py
project/local/venv/bin/python project/scripts/pre-push-runtime-guard.py
git diff --check
```

Only run live endpoint checks when the service is actually available.

## Closeout Contract

Before finishing substantial work:

1. Update the run handout.
2. Update the WikiLLM run note if the work has durable meaning.
3. Append a `complete`, `blocked`, or `handoff` entry to the live communication log.
4. Regenerate dashboard data if public text changed.
5. Run appropriate checks.
6. Commit only when the task requires it or the operator asks.
7. Push only when approved and checks pass.

Final report should include:

- files changed;
- checks run;
- external sync performed or skipped;
- remaining gaps;
- exact next safe action.

## Immediate Next Work Sequence

1. E1.4: define the KB update principle.
2. E2.0A: run the PRD-to-ICP dry-run packet.
3. E3.1: lock positioning.
4. E4.1: create the five-week content plan.
5. TG cleanup: align Telegram tasks with the new sender and audit artifacts.

Do not start provider activation, Railway, live Nexus writeback, vector defaulting, or autonomous dashboard writeback until the current commercial-learning sequence has a clearer owner decision and a separate safety gate.

