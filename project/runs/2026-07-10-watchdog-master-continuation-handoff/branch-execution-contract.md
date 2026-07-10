# Branch Execution Contract For The Watchdog Supervisor

Run: `2026-07-10-watchdog-master-continuation-handoff`

Status: required support contract for the next watchdog supervisor.

## Objective

Force the next watchdog run to use monitored branch execution rather than a single-pass review. The watchdog must create or resume separate branch chats for the three architectures, require subagent loops inside each branch, review branch evidence, merge accepted work, push Git, then handle Notion and other external actions.

## Model Hierarchy

This contract assumes the top watchdog chat runs as `5.6 Sol`.

Use model roles this way:

- `5.6 Sol`: top-level watchdog supervisor. Sol decides, budgets tokens, initiates branch chats, reviews compact Terra packets, approves or blocks merges, and gates external actions. Sol must not perform token-heavy execution.
- `5.6 Terra`: branch supervisor. Sol initiates one Terra chat per branch. Terra gives instructions, creates Luna subagent prompts, reviews Luna outputs, requests repairs, and sends compact branch reports to Sol.
- `5.6 Luna`: branch subagent model. Luna performs file reads, research, edits, checks, verification, safety scans, and draft artifacts inside each Terra branch chat.

Token rule:

- Sol should never ask Terra for full logs or raw file dumps.
- Terra should never do broad execution directly when Luna subagents are available.
- Luna should write durable outputs to files and return concise evidence, changed paths, checks, blockers, and merge recommendation.

## Branch Naming

Recommended branch/chat names:

- `watchdog/company-development-architecture`
- `watchdog/prd-icp-delivery-architecture`
- `watchdog/content-agent-architecture`

If the Codex app creates worktree branches with different names, record the actual branch names in the watchdog run handout. Do not store thread IDs in public files if they reveal private app metadata.

## Global Branch Rules

Every branch agent must:

- read the public coordination rules before edits;
- append a starting update before edits;
- stay inside the allowed file scope;
- avoid private data, local absolute paths, private URLs, account IDs, deployment IDs, secrets, screenshots, and raw private source text;
- use public-safe summaries when reading broader workspace context;
- create a branch handout under its own run folder;
- run relevant checks;
- report evidence, blockers, and merge recommendation.

Every branch agent must not:

- push to the remote;
- mutate Notion, Linear, Railway, production, Telegram, Figma, or social channels;
- call paid/model providers unless the watchdog separately approves a sanitized gated smoke test;
- claim customer demand, ROI, paid clients, full SaaS readiness, always-online runtime, provider runtime, voice readiness, or production reliability without current evidence.

## Internal Subagent Loop

Each branch chat must be a `5.6 Terra` chat and must run these internal roles using `5.6 Luna`. If real subagent tools are unavailable, the Terra chat must simulate Luna roles as bounded sections and say so.

### Planner

Execution type: Discovery and Planning.

Required model: `5.6 Luna`.

Goal:

- map prior evidence, identify files to touch, define acceptance criteria, and propose the smallest safe implementation.

Required output:

- scope;
- file list;
- risks;
- checks;
- open questions;
- go/no-go decision.

### Executor

Execution type: Implementation or Documentation.

Required model: `5.6 Luna`.

Goal:

- perform only the approved branch changes.

Required output:

- files changed;
- summary of changes;
- implementation evidence.

### Verifier

Execution type: Verification.

Required model: `5.6 Luna`.

Goal:

- verify syntax, config validity, links, dashboard regeneration, public-safety, and branch-specific acceptance criteria.

Required output:

- checks run;
- pass/fail/GAP;
- exact failure messages if any;
- repair recommendation.

### Safety Reviewer

Execution type: Review.

Required model: `5.6 Luna`.

Goal:

- review private-data risk, unsupported claims, external-action gates, and public-safe wording.

Required output:

- approve, revise, or block;
- issues by severity;
- required fixes.

### Branch Reporter

Execution type: Documentation.

Required model: `5.6 Luna`, reviewed by `5.6 Terra`.

Goal:

- write the final branch handoff and recommend merge, revise, or block.

Required output:

- branch status;
- changed files;
- evidence;
- checks;
- unresolved risks;
- merge recommendation.

## Branch A Contract: Company Development Agent Architecture

Execution type: Discovery, Planning, Implementation, Verification, Documentation, Deployment only if gates pass.

Goal:

- harden the internal company development architecture and operating method.

Required reads:

- `project/agentic-stack.md`
- `project/workflows/langgraph-controller.yaml`
- `project/workflows/crewai-crew.yaml`
- `project/agents/agent-roster.yaml`
- `project/agents/skills-by-agent.md`
- `project/config/model-routing.yaml`
- `project/provider-setup.md`
- `docs/dashboard-operating-manual.md`
- `api/_jarvis_contract.py`
- `services/jarvis-api/`
- `project/runs/2026-07-10-watchdog-supervisor-integration-review/`

Allowed files:

- `project/agentic-stack.md`
- `project/workflows/`
- `project/agents/`
- `project/config/`
- `project/provider-setup.md`
- `docs/dashboard-operating-manual.md`
- `api/`
- `services/jarvis-api/`
- own run folder
- live communication log

Acceptance criteria:

- company development architecture is explicit;
- Jarvis/dashboard reliability is reviewed with evidence;
- OpenRouter/model routing is explicit and gated;
- Railway/deploy path is either executed safely or blocked with exact prerequisites;
- skills/roles governance is safe for general project execution;
- no unsupported runtime claims remain.

## Branch B Contract: PRD/ICP Delivery Product Architecture

Execution type: Discovery, Planning, Documentation, Implementation where safe.

Goal:

- harden the client-facing PRD/ICP delivery architecture and service methodology.

Required reads:

- Founder Meeting v2 package if available through the broader workspace;
- `project/context/`
- `project/schemas/`
- `project/project-plan.md`
- `project/runs/2026-07-08-founder-meeting-v2-watchdog-cag-rag-integration/`
- `project/reports/2026-07-08-founder-meeting-v2-watchdog-cag-rag-architecture.md`
- `project/runs/2026-07-08-founder-meeting-v2-watchdog-cag-rag-integration/notion-e1-e7-update-packet.md`
- `project/content/templates/`

Allowed files:

- `project/context/`
- `project/schemas/`
- `project/project-plan.md`
- `project/reports/`
- `project/content/templates/`
- own run folder
- live communication log

Acceptance criteria:

- service ICP is explicit;
- buyer profiles and pains are explicit;
- competitor positioning is source-backed and cautious;
- delivery method from messy source material to PRD/ICP/backlog/DoD/task handoff is explicit;
- E1-E7 Notion planning packet is reviewed or updated;
- no Notion mutation occurs before Git push and watchdog review.

## Branch C Contract: Content Agent Architecture

Execution type: Discovery, Planning, Implementation, Verification, Documentation.

Goal:

- build the content architecture and initial content production system.

Required reads:

- `project/content/operations/`
- `project/content/templates/`
- `project/content/calendar/`
- `project/content/mockups/`
- current public website/dashboard style files;
- current public sources for market/news/tool trends when research is needed.

Allowed files:

- `project/content/`
- `docs/`
- `project/dashboard/`
- own run folder
- live communication log

Acceptance criteria:

- content agent architecture is explicit;
- research, competitor analysis, planning, writing, editing, design, QA, publishing-prep, and feedback roles are defined;
- public-source and free/safe source policy is defined for LinkedIn, X, Threads, reels/shorts-style content, and AI-automation content;
- 70/20/10 content plan exists;
- post/carousel/video-script design specs align with current styling;
- no social posting or private account scraping occurs.

## Merge Gate

The watchdog may merge a branch only if:

- branch reporter recommends merge or revise-with-fixed-evidence;
- verifier checks pass or gaps are explicitly acceptable;
- safety reviewer approves;
- branch diff is reviewed;
- no external action was taken without gates;
- no private/sensitive material appears in public files.

If two branches edit the same file, the watchdog must resolve conflicts manually, preserve the stricter safety wording, rerun checks, and record the merge decision in the final run handout.

## Push Gate

Before push:

```bash
git status --short
git diff --check
python3 scripts/public_safety_scan.py
python3 project/scripts/generate-dashboard-data.py
python3 -c "import json; json.load(open('project/dashboard/data.json')); print('dashboard_json=ok')"
project/local/venv/bin/python project/scripts/validate-workflows.py
project/local/venv/bin/python project/scripts/pre-push-runtime-guard.py
```

Add syntax checks for changed Python, JavaScript, YAML, and JSON files. Record `GAP` for unavailable checks.

## Notion Gate

Notion mutation is allowed only after:

- accepted branches are merged;
- Git checks pass;
- Git commit is pushed;
- separate Notion-planning agents prepare update packets;
- watchdog reviews packets;
- connector tools and schemas are discovered;
- target pages/databases are unambiguous;
- private IDs/URLs are not written to public files.

If any gate fails, produce a manual Notion update packet and stop.

## Final Handoff Template

The watchdog final handoff must include:

- status;
- branch list and branch outcomes;
- subagents used;
- files changed;
- merge decisions;
- checks and results;
- Git commit and push result;
- Notion state;
- Linear state;
- Railway/deploy/provider state;
- content/ICP/design state;
- Daily Founder Notes state;
- risks and blockers;
- next safe action.
