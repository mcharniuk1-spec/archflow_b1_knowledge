# Master Watchdog Continuation Handout

Run: `2026-07-10-watchdog-master-continuation-handoff`

Status: prepared for a new watchdog monitoring and approving agent.

## Goal

Continue the ArchFlow next-stage execution as a watchdog/supervisor agent.

The next watchdog must:

- review this handout and the prior supervisor handout;
- inspect any already-created specialist threads before duplicating work;
- initiate or resume specialist agent chats with their own subagents where needed;
- monitor evidence, repair loops, and stop conditions;
- integrate only justified changes;
- update Git after validation;
- update Notion Epics, tasks, subtasks, and Links page only after connector/target review;
- produce and verify the requested production, Railway, provider, content, market, ICP, Linear, and daily-notes outputs.

## Current Repo State

Known pushed commits from this chat:

- `135dc6f` - Founder Meeting v2 / Hermes watchdog / CAG-RAG architecture update.
- `f2a5942` - Watchdog supervisor execution lane contracts.
- `f1e7185` - Specialist thread dispatch record.

The active public project is under `public/` relative to the saved ArchFlow project. Worktree setup should enter `public/` before running Git and validation commands.

Safe setup pattern for worktree chats:

```bash
cd "$CODEX_WORKTREE_PATH"

if [ -d public/.git ]; then
  cd public
fi

python3 -m py_compile \
  api/_jarvis_contract.py \
  project/scripts/task-handout-hook.py \
  project/scripts/post-execution-skill-update.py

python3 -c "import json; json.load(open('project/dashboard/data.json')); print('dashboard_json=ok')"

git status --short
```

Safe cleanup pattern:

```bash
cd "$CODEX_WORKTREE_PATH"

if [ -d public/.git ]; then
  cd public
fi

find . -type f -name "*.pyc" -delete

git status --short
```

Do not run broad installs, provider calls, service starts, deploys, or external writes during setup.

## What Is Already Done

Founder Meeting v2 / Hermes / CAG-RAG package:

- Integrated into repo-native public-safe docs and configs.
- Added CAG/RAG context layer under `project/context/`.
- Added Hermes as planned watchdog/controller/reviewer only.
- Codex remains executor, reviewer, file editor, validator, and final integration boundary.
- Added skill governance, service operating model, market/content/sales templates, E1-E7 packet, prompt pack, architecture report, and Architecture PDF.
- Regenerated dashboard data.
- Passed local validation and public-safety checks before push.

Supervisor dispatch:

- Created `project/runs/2026-07-10-watchdog-supervisor-external-execution-lanes/`.
- Prepared six specialist lane contracts.
- Dispatched six specialist worktree chats:
  - Architecture Reliability and Jarvis Runtime Review.
  - Yushchenko OpenRouter and Model Routing Review.
  - Railway and Production Deployment Review/Execution.
  - Market, ICP, Competitor, and Content-Agent Architecture Research.
  - Content Operations, Writing Bots, Competitor Analyzer, and Post Design Mockups.
  - Notion and Linear External-Sync Review.

Thread identifiers are intentionally not stored in public files.

## What Must Be Reviewed First

Before creating new duplicate agents, the watchdog must:

1. List recent ArchFlow threads in the Codex app.
2. Find or inspect the six specialist threads from the supervisor dispatch if they exist.
3. Read each available specialist output.
4. Classify each lane as:
   - complete and ready for integration;
   - active and should be monitored;
   - blocked with reason;
   - failed/stale and should be replaced;
   - missing and should be initiated.
5. Only then create new specialist threads for missing or stale lanes.

## Required Watchdog Loop

For every lane:

1. Classify task type: Discovery, Planning, Implementation, Repair, Verification, Documentation, Deployment, Monitoring, or External Writeback.
2. Assemble CAG core from stable public project rules and the relevant run handouts.
3. Retrieve only bounded public-safe evidence from `project/`, `history/`, `skills/`, and `wiki/`.
4. Issue compact task contracts to specialist agents.
5. Require evidence before accepting completion.
6. Run repair only for failed checks, max 3 attempts.
7. Stop if the same error appears twice.
8. Stop for secrets, ambiguous external targets, provider-cost uncertainty, private IDs/URLs, unsupported claims, or unsafe production changes.

## Required Work To Complete

### 1. Architecture Reliability And Jarvis Runtime

Review Architecture 1, Architecture 2, and the new Content Agent architecture.

Required output:

- reliability matrix by stage;
- Jarvis health/chat contract review;
- current local versus online production behavior;
- safe fixes if needed;
- checks and evidence.

Must inspect:

- `api/`
- `services/jarvis-api/`
- `project/dashboard/`
- `project/workflows/`
- `project/config/model-routing.yaml`
- `project/provider-setup.md`
- `project/runs/2026-07-07-jarvis-chat-api-rebuild/agent-handout.md`

Key known fact:

- July 7 local source rebuilt Jarvis as text/chat-first with bounded attachments and voice disabled.
- Production still reported the older July 3 contract during that run.

### 2. OpenRouter And Model Routing

Act as Yushchenko model-efficiency observer.

Required output:

- current OpenRouter setup review;
- current model availability/pricing check from official/public sources;
- routing for Architecture 1, Architecture 2, Content Agent planning, content research, content writing, QA, and final review;
- provider activation gate status;
- cost/logging/budget policy.

Do not expose keys or call models with private material.

Provider/model calls may proceed only if:

- server-side secret access is available;
- explicit budget env values are present and below caps;
- payload is sanitized and public-safe;
- fresh model list is checked;
- usage/model/cost is logged without secrets;
- review gate accepts the run.

If any condition is missing, record a blocker and exact safe next command/action sequence.

### 3. Railway And Production Deployment

Required output:

- current Railway state review using official safe path;
- current production/Vercel state review;
- safe deploy or blocked deploy packet;
- `/health` and Jarvis response proof if deployed;
- rollback and verification notes.

The owner has asked to finish production deploy and Railway action. Treat that as approval to attempt only when target scope, auth, project/service linkage, and safety gates are unambiguous. Do not store deployment IDs, service domains, private URLs, account IDs, or secret values in public files.

### 4. Market, ICP, Competitor, And Content-Agent Architecture

This requires fresh web research because market/news/tool information changes.

Required output:

- market/news overview focused on PRD/ICP/product-team service buyers;
- ICP for B2B SaaS scaleups, product-led companies, 2-5 PM teams, Director/VP Product, Product Ops, Head of Product, and senior PM leaders;
- competitor positioning against Productboard, Aha, Dovetail, BuildBetter, Cycle, ChatPRD, Notion AI, Glean, Dust, status quo, junior PM/BA, and fractional product consultant;
- Content Agent architecture for trend/news intake, source review, topic scoring, planning, drafting, QA, post design, publishing, and feedback loop;
- explicit distinction between verified market facts and hypotheses.

Use current public sources and cite them in the final specialist output. Do not scrape private or login-only social data.

### 5. Content Operations, Writing Bots, Competitor Analyzer, And Designs

Required output:

- content plan covering all project stages, methods, tasks, and examples;
- separate content-planner bot and writing/editing bot roles;
- competitor-analyzer role with methods and sources for public LinkedIn, Threads, X, short-form/reels-style content, and AI automation content;
- free/safe source methods or APIs where available;
- 70/20/10 content split: 70% static educational/analytical, 20% carousel/checklist/template, 10% short video/scripted demo;
- visual post design mockups using current website/dashboard styling.

No social posting and no private account data.

### 6. Notion And Linear

Required output:

- review and apply the Notion-ready E1-E7 packet if connector scope and targets are unambiguous;
- update Notion Epics, tasks, subtasks, and the Links page based on this chat and the latest run evidence;
- add the July 4-10 Founder Daily Notes report to Notion only after target review;
- define or apply a lightweight Linear mirror strategy on free level without making Linear required.

Notion and Linear rules:

- discover connector/tool schemas before writeback;
- never store private page/database IDs or private URLs in public files;
- if target scope is unclear, produce a manual mutation packet and stop;
- Linear mirror should include only epics, current run, blockers, approvals, owner decisions, and final links.

### 7. Daily Founder Notes: July 4-10

The watchdog must verify the report in `daily-founder-notes-2026-07-04-to-2026-07-10.md`, update it if new evidence appears, and use it for Notion Links/Epics updates.

Public-safe rule:

- Use `Founder` or `owner`, not private identity names, in tracked public files.

## External Actions Approval State

The owner asked to proceed with:

- production deploy;
- Railway action;
- OpenRouter/provider activation review and possible model calls;
- Notion Epics/tasks/subtasks and Links page update;
- Linear mirror/external writeback on free/lightweight level.

Treat this as broad approval to attempt these actions, but not as permission to bypass safety checks. Stop if:

- target scope is unclear;
- credentials/secrets would be exposed;
- provider budget/model state is ambiguous;
- production target is ambiguous;
- connector schemas or IDs are not discovered safely;
- public files would contain private IDs, private URLs, or secrets.

## Required Validation Before Git Push

Run the smallest meaningful checks for touched files. Usually include:

```bash
python3 project/scripts/generate-dashboard-data.py
python3 -c "import json; json.load(open('project/dashboard/data.json')); print('dashboard_json=ok')"
project/local/venv/bin/python project/scripts/validate-workflows.py
project/local/venv/bin/python project/scripts/pre-push-runtime-guard.py
python3 -m py_compile api/_jarvis_contract.py project/scripts/task-handout-hook.py project/scripts/post-execution-skill-update.py
python3 scripts/public_safety_scan.py
git diff --check
```

Add JS syntax, Python syntax, health checks, or deployment checks when relevant.

If a check cannot run, record `GAP` with reason. Do not claim it passed.

## Final Acceptance Criteria

The next watchdog is done only when it has:

- reviewed existing specialist outputs or replaced missing/stale lanes;
- integrated justified repo changes;
- produced current Architecture/Jarvis/OpenRouter/Railway/Content/ICP/Notion/Linear evidence;
- updated and pushed Git after checks;
- updated Notion if connector/targets are safe;
- created or updated a public-safe Links/Notion update packet if direct mutation is blocked;
- produced final status with completed, partially completed, blocked, and next safe actions;
- avoided unsupported runtime, market, demand, ROI, customer, provider, and SaaS readiness claims.
