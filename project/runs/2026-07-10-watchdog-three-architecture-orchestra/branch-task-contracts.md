# Branch Task Contracts

Status: dispatched through separate worktree chats.

## Shared Contract

Each branch supervisor must use `5.6 Luna` subagents for Planner, Executor, Verifier, Safety Reviewer, and Branch Reporter roles when subagent tools are available. The branch must not push, deploy, activate providers, mutate Notion or Linear, publish social content, or store private material. Maximum three repair attempts; stop if the same error appears twice.

If the subagent API does not expose a model selector, use bounded real subagents anyway and record `GAP - Luna model selection unavailable` rather than skipping the required roles.

Every branch report must list files changed or proposed, diff summary, checks, source evidence, blockers, and one merge recommendation: `approve`, `revise`, or `block`.

## Branch A - Company Development Agent Architecture

Execution type: Discovery, Planning, Implementation, Verification, Documentation.

Allowed files:

- `AGENTS.md`
- `project/operating-rules.md`
- `project/agentic-stack.md`
- `project/workflows/`
- `project/agents/`
- `project/context/cag-core.yaml`
- `project/provider-setup.md`
- `docs/dashboard-operating-manual.md`
- `api/`
- `services/jarvis-api/`
- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/branch-a/`
- append-only status entries in `project/live/communication/agent-communication-log.md`

Required outcome: role-based company architecture, stage-by-stage reliability matrix, honest Jarvis/dashboard/always-online status, explicit OpenRouter model-choice and budget policy, Railway/deploy prerequisite packet, skills governance, and merge workflow. Do not claim current hosted proof without a current safe check.

## Branch B - PRD/ICP Delivery Product Architecture

Execution type: Discovery, Planning, Documentation, safe implementation.

Allowed files:

- `project/reports/2026-07-10-prd-icp-delivery-product-architecture.md`
- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/branch-b/`
- append-only status entries in `project/live/communication/agent-communication-log.md`

Required outcome: explicit service ICP and buyers; source-backed competitor analysis covering the required tool and human alternatives; discovery-to-evidence-to-PRD/ICP/backlog/DoD/task-handoff method; artifact package and QA gates; refreshed E1-E7 planning packet; Notion-ready Epics/tasks/subtasks/Links plan. Use current public sources for drift-prone competitor facts and cite them in the report. Do not mutate Notion.

## Branch C - Content Agent Architecture

Execution type: Discovery, Planning, Implementation, Verification, Documentation.

Allowed files:

- `project/content/architecture/`
- `project/content/calendar/2026-07-watchdog-initial-content-plan.md`
- `project/content/mockups/2026-07-watchdog-visual-specs.md`
- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/branch-c/`
- append-only status entries in `project/live/communication/agent-communication-log.md`

Required outcome: trend/news intake, competitor content analyzer, public-source method for LinkedIn/X/Threads/reels/shorts-style and AI-automation content, content planner, writer/editor, design/mockup, QA/publishing-preparation, feedback loop, 70/20/10 initial plan, and public-safe visual specifications aligned with the current website/dashboard style. No posting or private account scraping.
