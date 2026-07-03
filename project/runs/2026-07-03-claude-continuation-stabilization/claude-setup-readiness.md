# Run: Claude Cowork Setup Readiness

Date: 2026-07-03
Project: ArchFlow Block 1 Knowledge (public-safe)
Owner agent: Claude (Cowork)
Support tools: local filesystem, sandboxed shell, git (read), MCP registry.

## Task

Onboard Claude Cowork to the ArchFlow public-safe project: prove understanding of the operating contract, project-local skills, connector availability, safety boundary, validation path, runtime truth, and the next execution task. Setup only — no feature edits, no provider calls, no external writes, no push.

## Setup Scope Note

The setup prompt paths are relative to the git root, which in this workspace is the `public/` folder (that is where `.git` lives). All references below use `public/`-relative paths. The top-level `ArchFlow/` folder additionally holds pre-reset root files that are out of scope for current public work.

## Files Read

- `project/operating-rules.md`
- `project/live/communication/README.md`, `current-agent-notice.md`, latest `agent-communication-log.md`
- `project/project-plan.md`
- `project/agentic-stack.md`
- `project/config/model-routing.yaml`
- `project/agents/agent-roster.yaml`
- `wiki/index.md`, `wiki/memory.md`, `wiki/insights.md`
- All nine project-local skills under `skills/`.

## Skills Read And Applicability

| Skill | When to use | Applies to current setup |
|---|---|---|
| `arcagcom` | Before any parallel/shared-file edit; live-log claims and handoffs. | Yes — used to post start/complete entries. |
| `task-handout` | Substantial/multi-agent/subtask work; hook trigger. | Partial — this run is a bounded audit; readiness note serves as the handout. |
| `archflow-e1-runtime-guard` | Before push or after workflow/runtime changes. | Reference only — not pushing; guard is environment-blocked here. |
| `archflow1` | Dashboard/Jarvis/OpenRouter/Railway runtime work. | Reference only — no runtime work this run. |
| `priority-task-operator` | 00:30/06:30 priority-task automation lane. | Not this run. |
| `archflow-task-breakdown` | Decomposing epics/tasks into staged subtasks. | Useful for E1.4/E2.0A next. |
| `outquestions` | Closeout with open decision questions. | Applicable at closeout. |
| `daily-public-project-review` | Daily skill/RAG/KB retrospective. | Not this run. |
| `evening-skill-registry-update` | Nightly registry/hook sync. | Not this run. |

## MCP / Connectors Discovered

| Connector | Status | Safe current use | Notes |
|---|---|---|---|
| Local filesystem / shell | Available | Read/write public folder, run deterministic scripts. | Primary safe surface. |
| Git (local) | Available (read) | `git status`, diff, log. | Remote is `mcharniuk1-spec/archflow_b1_knowledge` over SSH. Push is gated (owner approval). A stale `.git/index.lock` could not be removed in-sandbox; harmless for read-only audit. |
| GitHub MCP | Not connected here | — | GAP: no GitHub MCP tool in this session; git CLI is the fallback. No force push, no history rewrite, no push without approval. |
| Notion | Gated (needs OAuth) | — | GAP: requires interactive authorization; unavailable in this non-interactive session. Append-evidence-only rule applies when connected; never mark Done without proof + approval. |
| Obsidian / Nexus | Not present | — | GAP: no Nexus runtime; use filesystem `wiki/` as durable memory fallback. Live writeback stays gated. |
| Figma | Gated (needs OAuth) | — | Only for explicit design/deploy-sync tasks; not needed now. |
| Vercel | Not exposed as MCP | — | Static hosted review-packet proof exists per prior runs; no production promotion without approval. |
| Railway | Not present | — | Gated always-on backend lane; not required for static proof. |
| Telegram / sender | Not present | — | External send only via approved sender + ignored env; store sanitized status only. |
| OpenRouter / provider bridge | Disabled by contract | — | Disabled until owner approval, backend/bridge, fresh model list, ledger, budget caps, reviewer. |
| Browser (Claude-in-Chrome) | Available if needed | Web read/testing | Not needed for setup. |
| MCP registry | Available | Discover connectors on request. | — |

Connectors requiring OAuth that are currently unavailable (non-interactive session): Notion, Slack, Linear, Asana, ClickUp, Monday, Figma, HubSpot, Atlassian, BigQuery, Amplitude, and others listed by the environment. These must be authorized in claude.ai connector settings or an interactive `claude mcp` / `/mcp` session before use.

## Validation Commands Run

| Check | Result |
|---|---|
| `python3 scripts/public_safety_scan.py` | PASS ("Public safety scan passed.") |
| `python3 project/scripts/generate-dashboard-data.py` | PASS ("wrote project/dashboard/data.json") |
| `python3 -c 'json.load(open("project/dashboard/data.json"))'` | PASS ("dashboard_json_ok") |
| `git diff --check` | PASS (no whitespace/conflict errors) |
| `validate-workflows.py` | BLOCKED — env |
| `pre-push-runtime-guard.py` | BLOCKED — env |
| `llamaindex-approved-corpus.py --mode smoke` | BLOCKED — env |
| `llamaindex-rag-benchmark.py` | BLOCKED — env |

Environment cause: `project/local/venv/bin/python` symlinks to a host-machine pyenv interpreter path that does not exist inside the Linux sandbox. System `python3` (3.10) lacks `pydantic`, `langgraph`, and `llama_index` (venv-only). Package installation is not permitted during setup, so these four checks were not run. This is an environment limitation, not a project defect.

## Runtime Truth Table (confirmed against files this run)

| Layer | Working assumption | Confirmation |
|---|---|---|
| Codex/local operator | Primary editor/reviewer/approval boundary. | Confirmed in `model-routing.yaml`, `operating-rules.md`. |
| WikiLLM | Durable public-safe memory in `wiki/`. | Confirmed; memory/insights current through 2026-07-03. |
| Live communication | Required channel in `project/live/communication/`. | Confirmed; latest entry 2026-07-03 (Codex split-instructions complete). |
| LlamaIndex | Bounded hybrid retrieval + lexical fallback over approved corpus. | Contract confirmed; runtime not verifiable here (env-blocked). |
| LangGraph | Workflow controller + smoke path. | Contract confirmed; runtime not verifiable here. |
| CrewAI | Role/task contract; Level-3 proof passed, not default runtime. | Confirmed in `model-routing.yaml` `crewai_level_3_proof`. |
| Dashboard | Static/browser-local + hosted provider-disabled packets. | Confirmed; `data.json` regenerated and parses. |
| Jarvis | Review-packet operation only. | Confirmed; provider-backed calls disabled. |
| Website | Static PRD/ICP positioning surface. | Confirmed in memory. |
| Notion | Task/reporting surface, not repo source of truth. | Confirmed; connector not available this session. |
| Telegram | Approved-sender external path only. | Confirmed gated. |
| OpenRouter | Disabled until approved lane. | Confirmed in config; keys only in ignored local env. |
| Railway | Future always-on lane, gated. | Confirmed. |
| Nexus | Future live bridge after schema discovery. | Confirmed; not present. |
| Vector/turbovec | Deferred until embedder/benchmark readiness. | Confirmed; 20-query benchmark is the gate. |

No row required promotion to "implemented"; no contradicting evidence found.

## Current Stage And Next Sequence

FACT: E1.1 done; E1.2 in Review pending owner acceptance; E1.3 readback/RAG readiness recorded as Review-strong; E1.4 is the next KB-method task; E2.0A is the next PRD-to-ICP dry-run. E3.1 and E4.1 are In Progress market-facing follow-ups.

Next execution sequence: **E1.4 (KB update principle) -> E2.0A (PRD-to-ICP dry-run packet) -> E3.1 (lock positioning) -> E4.1 (five-week content plan) -> Telegram task cleanup.**

## Status

Complete (setup audit).

## GAP

- venv-dependent validators (workflow validation, pre-push runtime guard, LlamaIndex smoke/benchmark) cannot run in this sandbox; fallback is deterministic filesystem checks + system-python `public_safety_scan` and dashboard JSON checks, which pass.
- No GitHub/Notion/Nexus MCP available in this non-interactive session; fallback is git CLI (read) and local `wiki/` writes; external sync stays gated.
- Provider-backed Jarvis, Railway, live Nexus writeback, vector defaulting/turbovec, dashboard-driven writeback, raw voice storage, and autonomous external updates remain gated — unchanged this run.
- Worktree was already dirty with a prior-agent continuation-stabilization run; not overwritten.

## Next Safe Action

Begin **E1.4**: read `skills/archflow-task-breakdown/SKILL.md` and the E1.3 readback artifacts under `project/runs/E1.3/2026-06-30-kb-readback/`, then draft the one-to-two-page KB update principle. Post a fresh `starting` live-log entry and claim only the E1.4 files before editing. Do not push, activate providers, or write external systems without owner approval.
