# Claude Execution Prompt

Date: 2026-07-03
Status: copy-ready prompt for actual project work after setup readiness is complete.

## Copy This Prompt Into Claude Code For Execution

You are Claude Code continuing ArchFlow after completing the setup/readiness pass. Work as a senior system architect/operator and pragmatic implementation agent. Your goal is to execute the next safe project task while preserving the knowledge system, public-safety boundary, dashboard truth, and live coordination discipline.

Do not restart from scratch. Use the existing project structure and run artifacts.

## Execution Goal

Primary next task:

Complete E1.4: define the principle for building and updating the knowledge base.

Secondary task only after E1.4 is complete and validated:

Run E2.0A: create the local PRD-to-ICP dry-run outcome packet.

Do not start E3.1, E4.1, provider activation, Railway, vector defaulting, Nexus writeback, dashboard writeback, or autonomous external sync until the primary task is complete or explicitly reprioritized.

## Required Context Files

Read these first:

```text
project/operating-rules.md
project/live/communication/README.md
project/live/communication/current-agent-notice.md
project/live/communication/agent-communication-log.md
project/README.md
project/project-plan.md
project/agentic-stack.md
project/config/model-routing.yaml
project/agents/agent-roster.yaml
project/workflows/knowledge-integration.yaml
project/workflows/llamaindex-rag.yaml
project/workflows/market-research-engine.yaml
wiki/index.md
wiki/memory.md
wiki/insights.md
wiki/log.md
project/runs/2026-07-03-claude-continuation-stabilization/claude-cowork-whole-project-instructions.md
project/runs/2026-07-03-claude-continuation-stabilization/claude-project-setup-prompt.md
project/runs/2026-07-03-claude-continuation-stabilization/system-review-stabilization-plan.md
project/runs/2026-07-03-claude-continuation-stabilization/project-checkup-evidence.md
project/runs/2026-07-03-hybrid-rag-jarvis-readiness/agent-handout.md
project/runs/2026-07-03-daily-founder-notes/current-state-report.md
```

Read these skills:

```text
skills/arcagcom/SKILL.md
skills/task-handout/SKILL.md
skills/archflow-e1-runtime-guard/SKILL.md
skills/archflow1/SKILL.md
skills/archflow-task-breakdown/SKILL.md
skills/outquestions/SKILL.md
```

## Before Edits

1. Run:

```bash
git status --short --branch
```

2. Check whether another agent has claimed the same files in the live communication log.

3. Append a `starting` entry to:

```text
project/live/communication/agent-communication-log.md
```

4. Claim only the files you will edit. For E1.4, likely files are:

```text
project/reports/<date>-kb-update-principle.md
project/runs/<date>-kb-update-principle/agent-handout.md
wiki/runs/<date>-kb-update-principle.md
wiki/log.md
project/dashboard/data.json
project/live/communication/agent-communication-log.md
```

5. If you need to change workflow or script files, announce scope expansion first.

## E1.4 Expected Output

Create a clear public-safe KB update principle report, suggested path:

```text
project/reports/<date>-kb-update-principle.md
```

The report must define:

- what counts as durable project knowledge;
- what stays as transient run evidence;
- what stays private and must never be ingested;
- how WikiLLM, LlamaIndex, Graphify, Notion, Obsidian/Nexus, dashboard packets, and Telegram evidence relate;
- how agents decide whether to write `wiki/memory.md`, `wiki/insights.md`, `wiki/runs/`, issues, or decisions;
- how to keep the KB useful for tracebacks without becoming noisy;
- how to keep source paths and provenance in retrieval outputs;
- how to handle wrong actions, bad captures, credential-boundary mistakes, or provider/runtime confusion;
- how to record FACT / INTERPRETATION / HYPOTHESIS / GAP;
- how to close a run with checks, handout, dashboard data, and live-log completion.

The report must be detailed enough that a new agent can update the KB correctly without reading chat history.

## E1.4 Required Structure

Use this structure:

```text
# KB Update Principle

Date:
Status:

## Executive Rule

## Layer Responsibilities

## What Becomes Durable Knowledge

## What Does Not Become Durable Knowledge

## Source And Provenance Rules

## Retrieval Rules

## WikiLLM Writing Rules

## Dashboard Packet Rules

## Notion And External Sync Rules

## Error And Traceback Rules

## Agent Workflow

## Validation

## Acceptance Criteria

## Next Actions
```

## E1.4 Acceptance Criteria

The task is acceptable when:

- it preserves public-safe boundaries;
- it explains WikiLLM as durable memory and LlamaIndex as retrieval only;
- it keeps Graphify as generated structural reference;
- it keeps Nexus/Obsidian gated unless schema/tool proof exists;
- it explains when to write memory, insight, issue, decision, run, and log files;
- it defines how dashboard packets become durable knowledge only after agent review;
- it includes a traceback section for credential-boundary and wrong-capture corrections;
- it includes checks and next safe action;
- validation passes.

## E2.0A Expected Output

Only start after E1.4 is complete.

Create a local PRD-to-ICP dry-run packet using approved public-safe sources only.

Expected artifacts:

```text
project/runs/<date>-prd-icp-dry-run/source-boundary.md
project/runs/<date>-prd-icp-dry-run/account-evidence-card-schema.md
project/runs/<date>-prd-icp-dry-run/source-grade-rubric.md
project/runs/<date>-prd-icp-dry-run/icp-profile-outline.md
project/runs/<date>-prd-icp-dry-run/executive-decision.md
project/runs/<date>-prd-icp-dry-run/agent-handout.md
wiki/runs/<date>-prd-icp-dry-run.md
```

Use:

```text
project/runs/2026-07-03-claude-continuation-stabilization/templates/prd-icp-service-template.md
project/workflows/market-research-engine.yaml
docs/prd-icp-output-template.md
```

No provider calls by default.

## Model And Provider Rules

Default:

- do not call providers;
- use local deterministic scripts and source-grounded writing;
- use Codex/Claude as local operators only.

OpenRouter is allowed only if the owner explicitly approves a separate provider run. If approved:

1. Refresh model availability from the official model list.
2. Use sanitized source packets only.
3. Record a model-call ledger.
4. Keep browser JavaScript away from provider keys.
5. Enforce daily and per-run budget caps.
6. Assign reviewer.
7. Stop before durable writeback.

Do not use provider output as fact without source-grounded review.

## MCP And Connector Rules During Execution

Before using a connector:

- list tools;
- inspect schemas;
- search/read before write;
- confirm target workspace/project/vault;
- record proof;
- avoid private URLs and IDs in tracked files.

During this execution:

- GitHub: local Git is enough unless issue/PR sync is explicitly requested.
- Notion: prepare update candidates; do not flip task state without owner approval.
- Obsidian/Nexus: do not use unless live schema/tool proof is explicitly requested.
- Telegram: do not send unless explicitly requested and using approved sender.
- OpenRouter: disabled unless explicitly approved.
- Railway/Vercel/Figma: not needed for E1.4.

## Validation Commands

For E1.4 documentation work, run:

```bash
python3 scripts/public_safety_scan.py
python3 project/scripts/generate-dashboard-data.py
python3 -c 'import json; json.load(open("project/dashboard/data.json")); print("dashboard_json_ok")'
git diff --check
```

If you touch workflows, runtime, skills, or RAG, also run:

```bash
project/local/venv/bin/python project/scripts/validate-workflows.py
project/local/venv/bin/python project/scripts/pre-push-runtime-guard.py
project/local/venv/bin/python project/scripts/llamaindex-approved-corpus.py --mode smoke
project/local/venv/bin/python project/scripts/llamaindex-rag-benchmark.py
```

If you touch dashboard UI, also run:

```bash
node --check project/dashboard/app.js
project/local/venv/bin/python project/scripts/dashboard-static-smoke.py
```

## Closeout Required

Before final response:

1. Update or create `project/runs/<run-id>/agent-handout.md`.
2. Update `wiki/runs/<run-id>.md`.
3. Append to `wiki/log.md`.
4. Append `complete`, `blocked`, or `handoff` to the live communication log.
5. Regenerate `project/dashboard/data.json` if public text changed.
6. Run validation.
7. Leave a concise final response with:
   - files changed;
   - checks run;
   - blockers/gaps;
   - next safe action.

Do not push unless explicitly approved for this execution.

## Stop Conditions

Stop and ask for direction if:

- a task requires private raw source ingestion;
- an MCP write is needed but schema discovery is unavailable;
- a provider call is needed but no approval/ledger/budget exists;
- a public file would need private URLs, IDs, credentials, or local absolute paths;
- another agent has claimed the same files;
- validation fails and the fix would require broad refactor;
- the task drifts into Railway, provider-backed Jarvis, dashboard writeback, vector defaulting, or live Nexus without explicit approval.

## Final Output Style

Use:

```text
FACT:
- ...

INTERPRETATION:
- ...

GAP:
- ...

FILES:
- ...

CHECKS:
- ...

NEXT SAFE ACTION:
- ...
```

Keep chat concise. Put detailed durable content into files.

