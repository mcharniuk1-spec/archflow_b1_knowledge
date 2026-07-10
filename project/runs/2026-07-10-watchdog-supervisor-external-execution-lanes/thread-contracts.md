# Thread Contracts

Run: `2026-07-10-watchdog-supervisor-external-execution-lanes`

These contracts are for separate Codex specialist threads created by the supervisor. Thread identifiers are not stored in this public file.

## 2026-07-10 Correction Note

These six specialist lanes are prior evidence and planning material, not the final controlling execution shape. The corrected watchdog supervisor must map these lanes into the three required architecture branches defined in `project/runs/2026-07-10-watchdog-master-continuation-handoff/branch-execution-contract.md`:

- Company Development Agent Architecture.
- PRD/ICP Delivery Product Architecture.
- Content Agent Architecture.

The watchdog must review any existing lane outputs, but branch execution, branch review, merge-before-push, and Notion-after-Git sequencing now control the next run.

## Shared Context For All Threads

Start from the current ArchFlow public project. The active public project root is `public/`.

Required reads before edits:

- `AGENTS.md`
- `project/operating-rules.md`
- `project/live/communication/README.md`
- `project/live/communication/current-agent-notice.md`
- latest entries in `project/live/communication/agent-communication-log.md`
- `project/runs/2026-07-08-founder-meeting-v2-watchdog-cag-rag-integration/agent-handout.md`
- `project/reports/2026-07-08-founder-meeting-v2-watchdog-cag-rag-architecture.md`
- `project/agentic-stack.md`
- `project/config/model-routing.yaml`

## 1. Architecture Reliability And Jarvis Runtime Review

Execution type: Discovery, Verification, Repair, Documentation.

Goal:

- Review the architecture stage by stage and make sure Architecture 1, Architecture 2, and the planned Content Agent architecture have reliable Jarvis/control-surface behavior.

Allowed files:

- `api/`
- `services/jarvis-api/`
- `project/dashboard/`
- `project/workflows/`
- `project/config/`
- `project/agentic-stack.md`
- `project/provider-setup.md`
- own run folder under `project/runs/`
- live communication log

Forbidden actions:

- No production deploy.
- No provider/model call.
- No external writeback.
- No secrets or private URLs in public files.

Acceptance criteria:

- Reliability matrix for each stage.
- Jarvis health/chat contract reviewed.
- Architecture 1, Architecture 2, and Content Agent stage boundaries clarified.
- Local/static checks run where relevant.
- Any safe local fixes are implemented and verified.

## 2. Yushchenko OpenRouter And Model Routing Review

Execution type: Discovery, Verification, Repair, Documentation.

Goal:

- Review OpenRouter setup and update model-choice policy for Architecture 1, Architecture 2, and Content Agent workflows.

Allowed files:

- `api/_jarvis_contract.py`
- `project/config/model-routing.yaml`
- `project/provider-setup.md`
- `project/agentic-stack.md`
- `project/workflows/`
- own run folder under `project/runs/`
- live communication log

Forbidden actions:

- Do not print or store provider keys.
- Do not call models with private material.
- Do not make repeated paid/provider calls.
- Stop if model list, budget caps, or secret access are ambiguous.

Acceptance criteria:

- Fresh provider/model availability is checked from safe public sources or official API if network is approved.
- Model routing is explicit for planning, execution, review, content research, content writing, and final QA.
- Provider activation gate is reviewed and hardened if needed.
- One sanitized smoke call may be performed only if all gates are met; otherwise record a blocked action with exact missing prerequisites.

## 3. Railway And Production Deployment Review/Execution

Execution type: Discovery, Verification, Deployment, Repair, Documentation.

Goal:

- Review and, if safe, finish Railway/Jarvis and production deployment work so Jarvis can respond online with evidence.

Allowed files:

- `services/jarvis-api/`
- `api/`
- `vercel.json`
- `project/provider-setup.md`
- `project/config/`
- `project/runs/`
- live communication log

Forbidden actions:

- Do not expose deployment IDs, private URLs, account IDs, or secret values in public files.
- Do not promote production if public safety fails.
- Do not activate provider calls unless the provider lane proves gates.
- Stop if project/service linkage is ambiguous.

Acceptance criteria:

- Current deployment architecture reviewed.
- Railway project/service state checked using official safe path if available.
- Production deploy performed only if target and safety are unambiguous.
- `/health` and Jarvis response proof captured in public-safe wording.
- If deployment cannot safely proceed, create exact blocker packet and next command sequence.

## 4. Market, ICP, Competitor, And Content-Agent Architecture Research

Execution type: Discovery, Planning, Documentation.

Goal:

- Build current market, ICP, competitor, and content-agent architecture evidence for the ArchFlow service company.

Allowed files:

- `project/content/`
- `project/reports/`
- `project/project-plan.md`
- `project/agents/`
- `project/workflows/`
- own run folder under `project/runs/`
- live communication log

Forbidden actions:

- No unsupported claims of demand, ROI, customers, or paid validation.
- No scraping private/social profile data.
- No external posting or writeback.

Acceptance criteria:

- Current market research uses fresh web sources where required.
- ICP is explicit for B2B SaaS scaleups, product-led companies, teams with 2-5 PMs, and senior product/product-ops buyers.
- Competitor analysis includes Productboard, Aha, Dovetail, BuildBetter, Cycle, ChatPRD, Notion AI, Glean, Dust, status quo, junior PM/BA, and fractional product consultant.
- Defines Content Agent architecture, trend/news intake, source review, content planning, writing, QA, and publication gates.

## 5. Content Operations, Writing Bots, Competitor Analyzer, And Post Design Mockups

Execution type: Planning, Implementation, Documentation, Verification.

Goal:

- Turn the current project work into a concrete content plan, writing-bot architecture, competitor-analyzer role, and visual post design mockups using current website styling.

Allowed files:

- `project/content/`
- `project/dashboard/`
- `docs/`
- `project/runs/`
- safe generated assets under `project/content/`
- live communication log

Forbidden actions:

- No social posting.
- No use of private social account data.
- No unsupported customer/demand/ROI claims.
- No design assets that require private screenshots.

Acceptance criteria:

- Content plan covers project methods, architecture, stages, tasks, examples, and service offer.
- Separate planning and writing bot roles are defined.
- Competitor analyzer role includes sources, methods, and free/safe API or public-source options for LinkedIn, Threads, X, reels/shorts-style content, and AI-automation content.
- Static/educational, carousel/checklist/template, and short video/scripted demo split follows 70/20/10.
- Post design mockups or image assets are created and checked against current styling.

## 6. Notion And Linear External-Sync Review

Execution type: Discovery, Planning, Documentation, External Writeback only if safe.

Goal:

- Review Notion mutation needs and define a lightweight Linear mirror strategy that is useful on a free level without overloading the operating system.

Allowed files:

- `project/runs/`
- `project/project-plan.md`
- `project/live/communication/`
- optional public-safe task packets under `project/`

Forbidden actions:

- No private page/database IDs in public files.
- No mutation if connector scope or target is ambiguous.
- No paid Linear requirement.
- No migration that makes Linear required.

Acceptance criteria:

- Notion-ready mutation packet is reviewed.
- If safe connector access and target are available, mutation may be performed without storing private IDs in tracked files.
- Linear mirror defines only the minimum helpful objects: epics, current run, blockers, approvals, owner decisions, and final links.
- If writeback is not safe, create exact safe packet for manual/executor follow-up.
