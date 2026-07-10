# Corrected Watchdog Supervisor Continuation Handout

Run: `2026-07-10-watchdog-master-continuation-handoff`

Status: corrected for the next ArchFlow Public watchdog supervisor.

## Purpose

This handout is for a new watchdog supervisor agent working inside the ArchFlow Public Git project. It must not behave like a single linear executor. It must supervise a branch-based agent orchestra:

1. create or resume specialist chats for each branch;
2. require each branch agent to use its own planning, execution, verification, and safety-review subagents or bounded subagent sections;
3. review all branch outputs and diffs;
4. merge only accepted branch work;
5. run validation;
6. push Git only after reviewed merge;
7. update Notion only after the pushed Git state is verified and separate Notion-planning agents prepare the mutation packet.

The earlier `d889d84` watchdog run is useful evidence, but it was a single integration pass. It must be reviewed, not treated as full completion of the requested branch/subagent execution model.

## Sol/Terra/Luna Token Hierarchy

The next run should use a model hierarchy to preserve the owner token budget:

- `5.6 Sol`: top watchdog supervisor. Sol thinks, decides, initiates Terra branch chats, reviews compact evidence packets, approves or blocks merges, and gates external actions. Sol should not perform token-heavy execution.
- `5.6 Terra`: branch-chat supervisor. Terra receives one architecture branch from Sol, prompts Luna subagents, reviews Luna outputs, requests repairs, and returns compact branch reports.
- `5.6 Luna`: branch subagent. Luna performs file reading, research, implementation, validation, safety scans, and artifact drafting inside each Terra branch chat.

Sol should not request full logs or large file dumps. Terra should not perform heavy work directly when Luna subagents are available. Luna should write durable outputs to files and report concise evidence, paths, checks, blockers, and merge recommendations.

## Workspace Model

The general ArchFlow workspace is the full local project folder. The public GitHub repository is the `public` folder.

Public tracked files must not store local absolute paths. When working in a new Codex chat, the operator can provide the full local path in chat setup, but public files must use repo-relative or parent-workspace descriptions only.

The watchdog must understand this boundary:

- General workspace: source of broader planning material and private/non-public context.
- Public repo: Git-tracked public-safe output and the integration boundary.
- `archflow_8_07` package: owner-approved planning package from the broader workspace; read it when available, summarize only public-safe findings into the public repo.
- Public project artifacts: the evidence that can be committed and pushed.

Do not initialize a Git repo at the broader workspace root just to make worktrees work. For branch/worktree execution, use the public repo as the Git root.

## Current Evidence To Review

Known pushed commits from this chat:

- `135dc6f` - Founder Meeting v2 / Hermes watchdog / CAG-RAG architecture update.
- `f2a5942` - Watchdog supervisor execution lane contracts.
- `f1e7185` - Specialist thread dispatch record.
- `c1385d4` - Master watchdog continuation handoff.
- `d889d84` - Watchdog supervisor integration review.

The watchdog must inspect these commits, then classify each as:

- complete and accepted;
- useful but partial;
- stale or superseded;
- conflicting with the corrected owner instruction;
- needing repair.

## Corrected Agent-Orchestra Rule

Do not frame the project as a hard division where Codex and Hermes are separate product systems that cannot share execution responsibility.

Use an agent-orchestra model:

- Watchdog role: classifies work, initiates chats, creates task contracts, monitors branches, reviews evidence, approves or blocks merges, and performs final external actions only after gates pass.
- Executor role: performs bounded implementation or research work inside a branch/chat.
- Verifier role: checks claims, diffs, tests, safety, and acceptance criteria.
- Integrator role: merges accepted branches, runs repo checks, commits, and pushes.
- External-action role: performs Notion, Railway, provider, production, Linear, or other writeback only after branch review, Git push, target/schema review, and explicit approval gates.

Codex, Hermes, or any compatible local agent runtime can fulfill these roles when available. The role contract matters more than the agent name. Do not block work because Hermes is not separately available. Do not bypass safety because Codex is available.

## Three Architecture Branches

The watchdog must split work into three primary branches. Each branch should run in a separate specialist chat/worktree when the tool supports it. If separate chats are unavailable, simulate branches as bounded sections and record the limitation.

### Branch A: Company Development Agent Architecture

Purpose:

- Build and harden the internal company operating architecture: agent roles, skills, development workflow, branch review, Git closeout, dashboard/Jarvis operator path, Railway/production gate, provider gate, and service-company operating model.

Must review:

- `project/agentic-stack.md`
- `project/workflows/`
- `project/agents/`
- `project/config/model-routing.yaml`
- `project/provider-setup.md`
- `docs/dashboard-operating-manual.md`
- `api/`
- `services/jarvis-api/`
- `project/runs/2026-07-10-watchdog-supervisor-integration-review/`

Required outputs:

- corrected development architecture description;
- Jarvis reliability and online-response review;
- Railway/production deployment status or blocker packet;
- OpenRouter/model-routing review as the Yushchenko observer;
- skill/role governance updates if needed;
- validation evidence.

### Branch B: PRD/ICP Delivery Product Architecture

Purpose:

- Define and harden the client-facing PRD/ICP delivery architecture. This is the delivery product for clients. It may be labeled Architecture 1 in dashboard language, but in the broader company architecture it is the second architecture.

Must review:

- Founder Meeting v2 / `archflow_8_07` package where available;
- `project/context/`
- `project/schemas/`
- `project/project-plan.md`
- `project/runs/2026-07-08-founder-meeting-v2-watchdog-cag-rag-integration/`
- `project/reports/2026-07-08-founder-meeting-v2-watchdog-cag-rag-architecture.md`
- `project/content/templates/`
- E1-E7 Notion-ready packets.

Required outputs:

- explicit ICP for the service company and client-product delivery;
- market and competitor analysis with source-backed claims;
- PRD/ICP service methodology;
- client delivery flow, QA gates, artifact packages, and evidence handling;
- Notion planning packet for Epics, tasks, subtasks, and Links page;
- no direct Notion mutation until after Git merge/push and watchdog review.

### Branch C: Content Agent Architecture

Purpose:

- Create the new content architecture for market/news/trend intake, competitor analysis, content planning, writing, design, QA, publishing preparation, and feedback.

Must review:

- `project/content/operations/`
- `project/content/templates/`
- `project/content/calendar/`
- `project/content/mockups/`
- current website/dashboard styling;
- public sources for relevant market/news/tool trends.

Required outputs:

- content-agent architecture with subagents for research, competitor analysis, planning, writing, editing, design, QA, and publishing preparation;
- target audience and ICP-specific content strategy;
- competitor analyzer role and source policy for public LinkedIn, X, Threads, reels/shorts-style content, and AI automation content;
- free/safe source methods or APIs where available;
- 70/20/10 content split: 70% static educational/analytical, 20% carousel/checklist/template, 10% short video/scripted demo;
- static post/carousel/script mockup specs using current styling;
- generated images or image specs only if safe and supported by the environment;
- no social posting or private account scraping.

## Branch Execution Contract

Each branch agent must receive a compact task contract with:

- branch name and purpose;
- execution type;
- goal;
- required reads;
- allowed files;
- forbidden actions;
- subagent roles required inside the branch;
- acceptance criteria;
- required evidence;
- maximum attempts: 3;
- stop condition;
- expected output format.

Every branch must include these internal subagents or bounded sections:

- Planner: scopes work and creates file/update plan.
- Executor: performs implementation or research.
- Verifier: checks claims, links, diffs, syntax, and acceptance criteria.
- Safety Reviewer: checks public-safety, unsupported claims, external-action gates, and private-data risk.
- Branch Reporter: writes the branch handoff with changed files, checks, blockers, and merge recommendation.

No branch agent may push directly to the remote. Branch agents can commit locally on their branch only if the watchdog explicitly permits it. The watchdog reviews branch diffs and validation output before merge.

## Required Work From The Next Watchdog

The watchdog must complete this sequence:

1. Discovery:
   - read public coordination rules;
   - append a starting update;
   - inspect the prior commits and run folders;
   - inspect existing specialist threads if available;
   - identify what was already done and what remains missing.
2. Branch setup:
   - create or resume three branch chats for Branch A, Branch B, and Branch C;
   - give each branch its task contract;
   - require subagents inside each branch.
3. Branch monitoring:
   - collect branch reports;
   - request one repair attempt if evidence is missing;
   - stop a branch if the same failure appears twice.
4. Integration:
   - review diffs and branch outputs;
   - merge accepted branches into the public repo;
   - resolve conflicts conservatively;
   - update the final handout and validation report.
5. Git:
   - run required checks;
   - commit and push only after checks pass.
6. Notion:
   - initiate separate Notion-planning agents to prepare Epics/tasks/subtasks/Links update packets;
   - watchdog reviews those packets;
   - only then perform Notion mutation directly if connector schemas, targets, and approval gates are unambiguous.
7. External actions:
   - Railway, production deploy, provider/model calls, Linear mirror, and social/external writeback can proceed only after target, safety, budget, and approval gates pass.

## Notion And Linear Sequencing

Notion must happen after Git, not before.

Correct sequence:

1. branch agents prepare architecture/content/ICP/update evidence;
2. watchdog reviews branches;
3. accepted branch work is merged;
4. repo checks pass;
5. Git commit is created and pushed;
6. separate Notion-planning agents prepare mutation packets for:
   - E1-E7 Epics;
   - tasks and subtasks;
   - Links page;
   - July 4-10 Daily Founder Notes;
   - current run evidence;
7. watchdog reviews the Notion packets;
8. watchdog performs Notion mutation only if connector tools, schemas, target pages/databases, and approval gates are proven;
9. Linear mirror is prepared or applied only as a lightweight optional mirror and must not become required.

If target scope is unclear, produce a manual mutation packet and stop. Do not store private Notion or Linear IDs/URLs in public files.

## External Action Gates

The owner has broadly asked to finish production deploy, Railway action, OpenRouter/provider review, Notion update, and lightweight Linear mirror. Treat that as intent, not permission to bypass gates.

Stop before external action if any of these are unclear:

- target project/service/page/database;
- connector schema;
- credentials or secret source;
- provider budget cap;
- production rollback path;
- public safety status;
- exact artifact to publish or mutate.

Do not store private IDs, private URLs, account IDs, deployment IDs, secrets, screenshots, credentials, raw private source text, or local absolute paths in tracked files.

## Current Claim Policy

Downgrade or mark as GAP any unsupported claim about:

- always-online runtime;
- Jarvis production reliability;
- Railway readiness;
- provider-backed execution;
- customer demand;
- ROI;
- paid clients;
- production autonomy;
- voice readiness;
- social performance;
- full SaaS readiness.

## Required Validation

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

Add YAML, JavaScript, Python, link, health, deployment, or provider checks when relevant. If a check cannot run, record `GAP` with reason. Do not claim it passed.

## Final Acceptance Criteria

The next watchdog is done only when it has:

- reviewed earlier work including `d889d84`;
- run or simulated three branch executions with subagent loops;
- integrated accepted branch outputs;
- merged before pushing;
- pushed Git after validation;
- prepared or performed Notion updates only after Git and target review;
- documented Railway/deploy/provider/Linear status;
- verified or corrected the July 4-10 Daily Founder Notes packet;
- produced final status with completed, partial, blocked, and next safe actions;
- avoided unsupported claims and private data leakage.
