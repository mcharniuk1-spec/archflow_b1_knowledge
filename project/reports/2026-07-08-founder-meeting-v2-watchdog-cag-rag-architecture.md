# Founder Meeting v2 Watchdog/CAG-RAG Architecture Report

Status: public-safe architecture report.

Generated: 2026-07-08.

Run folder: `project/runs/2026-07-08-founder-meeting-v2-watchdog-cag-rag-integration/`

## Executive Summary

ArchFlow now has a documented final architecture direction for the Founder Meeting v2 package:

- Codex remains the executor, reviewer, file editor, validator, and final integration boundary.
- Hermes is planned as watchdog/controller/reviewer, not executor.
- CAG is Controlled Context Assembly Generation: stable, compact context before task work.
- RAG is bounded, task-specific retrieval into the capsule from approved public-safe corpus only.
- LlamaIndex remains retrieval, not memory.
- WikiLLM remains durable reviewed memory after promotion.
- CrewAI organizes roles and proof packages, but is not the default autonomous runtime.
- LangGraph owns route/state/gate architecture.
- Dashboard/Jarvis are operator/control surfaces, not the primary brain.
- Provider calls, external writeback, Notion mutation, Telegram, Railway, Linear, Figma, Git push, deploy, and production promotion remain blocked without explicit owner approval.

The project is service-first: customer discovery -> evidence-backed PRD -> task packet -> KB handoff. It is not yet validated SaaS demand.

## Current Working Architecture

### Layer Stack

```text
Codex local operator
  -> Hermes planned watchdog/controller/reviewer
  -> CAG/RAG context capsule
  -> LangGraph path/state/review gates
  -> LlamaIndex bounded retrieval
  -> CrewAI role/task definitions and proof-only runtime
  -> AF Review
  -> public-safe repo artifacts, run handout, and optional owner-approved external actions
```

### What Works Now

| Area | Current working state |
|---|---|
| Public project rules | `AGENTS.md`, `project/operating-rules.md`, live communication rule, and public-safety rules exist. |
| LangGraph | Workflow config exists and now includes planned Hermes/CAG nodes. Prior smoke state remains recorded. |
| CrewAI | Role/task config exists. Level 3 direct CrewAI proof passed on a tiny public-safe deterministic fixture, but is not default runtime. |
| LlamaIndex | Bounded retrieval config exists with approved corpus, lexical fallback, and benchmark requirements. |
| Dashboard/Jarvis | Hosted/provider-disabled review-packet surface exists from E1.7; provider calls and writeback remain zero unless approved. |
| Skills | Project-local skill registry exists; governance now distinguishes shared and role-specific skill visibility. |
| CAG/RAG | New context schema, CAG core, source-boundary policy, and run capsule exist under `project/context/`. |
| E1-E7 | Project plan and Notion-ready task packet now include Founder Meeting v2/Hermes/CAG/RAG updates. |
| Content/sales | Template library now includes ICP, competitor, discovery call, qualification, diagnostic offer, calendar, and 70/20/10 distribution templates. |

### What Does Not Work Or Is Not Activated

- Hermes is not a running autonomous service.
- Provider-backed Jarvis is not active by default.
- Durable writeback to Notion, WikiLLM, Obsidian, Nexus, GitHub, Telegram, Linear, Railway, or production is not active.
- Linear is not required.
- CrewAI is not default autonomous execution.
- Full vector defaulting is not active until retrieval benchmark requirements pass.
- Voice/raw transcript persistence is not active.
- SaaS readiness, validated customer demand, guaranteed ROI, and paid customer claims are not proven.

## Hermes Watchdog Controller

Hermes is a future controller layer with these permissions:

- classify execution type and risk;
- assemble stable CAG core;
- request task-specific RAG evidence;
- build or review context capsules;
- generate bounded task contracts;
- review evidence;
- decide accept, repair, split, escalate, or stop.

Hermes is forbidden from:

- executing code;
- editing files;
- deploying;
- mutating task boards or external systems;
- activating providers;
- storing secrets;
- approving its own high-risk output.

Codex remains the execution boundary.

## CAG/RAG Method

### CAG

CAG means Controlled Context Assembly Generation. It is a stable context packet for a task or run.

It includes:

- project operating rules;
- live communication constraints;
- founder meeting methodology;
- current architecture boundaries;
- role and skill maps;
- E1-E7 state;
- gated claims;
- acceptance criteria;
- stop conditions.

Files:

- `project/context/README.md`
- `project/context/cag-core.yaml`
- `project/context/context-capsule.schema.json`
- `project/context/capsules/2026-07-08-founder-meeting-v2-watchdog-cag-rag-integration.json`

### RAG

RAG is bounded retrieval into the capsule. It must return repo-relative source paths and metadata.

Approved corpus:

- `project/`
- `history/`
- `skills/`
- `wiki/`

Forbidden by default:

- raw private exports;
- ignored local runtime data;
- secrets;
- private URLs;
- raw transcripts;
- screenshots;
- account IDs;
- deployment IDs;
- personal identifiers;
- absolute local paths.

LlamaIndex handles retrieval. WikiLLM handles durable reviewed memory only after promotion.

## LangGraph

LangGraph controls path, state, conditional routing, review loops, and approval gates.

New planned controller nodes:

- `classify_execution`
- `assemble_cag_core`
- `build_context_capsule`
- `assign_task_contract`
- `decide_next_action`

Important boundary: adding these nodes is a configuration/architecture update. It does not mean Hermes is executing runtime code.

## CrewAI

CrewAI organizes roles and tasks:

- AF Tools
- AF Context
- AF Discovery
- AF PRD Architect
- AF Task Translator
- AF Manager
- AF Research
- AF Knowledge
- AF Copy
- AF Review
- AF Publisher
- Hermes Watchdog as planned controller role

Current runtime status:

- Level 1 configured roles: active.
- Level 2 LangGraph-wrapped workers: target architecture after approval.
- Level 3 direct CrewAI runtime: proof passed on deterministic public-safe fixture; not default runtime.

## Dashboard And Jarvis

Dashboard/Jarvis are operator/control surfaces.

Current honest label:

- provider-disabled hosted review-packet surface exists;
- provider calls are zero unless explicitly approved;
- writeback is zero unless explicitly approved.

The dashboard is not the project brain. Repo YAML/Markdown, run packets, and reviewed memory remain sources of truth.

## MCPs And External Connectors

No MCP or connector writeback is activated by this report.

External surfaces remain approval-gated:

- Notion mutation.
- WikiLLM/Obsidian/Nexus durable writeback.
- Telegram send.
- Railway action.
- Figma sync.
- Git push.
- Vercel or production deployment.
- Linear mirror.
- Provider calls.

If approved later, each external action needs a separate task contract, source boundary, evidence, review gate, and handoff.

## Skills Distribution

### Inspect-All Roles

These roles may inspect all skills:

- Hermes Watchdog.
- Codex / Lead Integrator.
- AF Review.
- AF Knowledge.
- Assigned skills-governance reviewer.

### Shared Project Skills

- `arcagcom`: live communication and file claims.
- `archflow1`: dashboard/Jarvis/provider/Railway boundaries.
- `task-handout`: durable handout and continuation prompt.
- `outquestions`: owner decisions and next-stage gates.

### Role-Specific Examples

- AF Discovery: JTBD, 90-day story, customer forces, source boundary.
- AF PRD Architect: evidence-backed requirements, DoD, acceptance criteria.
- AF Task Translator: task packet, checkbox subtasks, blockers, owner decisions.
- AF Review: public safety, claim support, runtime boundary.
- AF Publisher: publication packets only; external publication is owner-gated.

## Knowledge And Logs

Knowledge layers:

- Run artifacts: `project/runs/...`
- Reports: `project/reports/`
- Public project memory: `wiki/memory.md`, `wiki/insights.md`, `wiki/log.md`
- Durable reviewed memory: WikiLLM after promotion rules pass

Live coordination:

- `project/live/communication/agent-communication-log.md`
- `project/live/communication/current-agent-notice.md`
- `project/live/communication/README.md`

This run used live-log start and scope-update entries before implementation.

## Service Company Model

Offer ladder:

1. Discovery Diagnostic.
2. PRD Rescue Sprint.
3. Monthly PRD/KB Operating Retainer.

Every client-facing artifact needs:

- source boundary;
- facts separated from hypotheses;
- source refs for material claims;
- no raw private material;
- measurable acceptance criteria;
- Definition of Done;
- current alternatives;
- buyer trigger/anxiety/workaround;
- task packet;
- AF Review verdict.

## Market, Content, And Sales

Primary ICP:

- B2B SaaS scaleups and product-led companies.
- Roughly 50-500 employees.
- Teams with 2-5 PMs.
- Buyers: Director/VP Product, Head of Product, Product Ops, and senior PM leaders.

Content mix:

- 70% static educational/analytical.
- 20% carousel/checklist/template.
- 10% short video/scripted demo.

Competitor categories:

- Productboard / Aha / Cycle.
- Dovetail / BuildBetter.
- ChatPRD.
- Notion AI / Glean / Dust.
- Status quo.
- Junior PM/BA.
- Fractional product consultant.

Demand boundary:

- Attention is not demand.
- Validated demand requires payment, prepayment, approved paid start, or firm paid intent with source packet, scope, timeline, and budget-owner path.

## Prompt Pack

The run folder contains adapted prompt files 01-09:

- Codex system prompt.
- ArchFlow Codex configuration prompt.
- Hermes watchdog prompt.
- CAG/RAG context capsule prompt.
- Subagent task contract prompt.
- Skill registry/hook governance prompt.
- Market/content/sales prompt.
- E1-E7 Notion update prompt.
- Final Git/website/dashboard/KB publish prompt.

## Validation Plan

Required checks:

- YAML parse for changed workflow and roster files.
- JSON parse for context schema, capsule, and dashboard data.
- Python compile for changed Python files.
- Dashboard data regeneration.
- Public safety scan.
- `git diff --check`.
- Final QA reviewer.

## Remaining Risks

- Provider-backed runtime can be misunderstood unless labels remain precise.
- CAG capsules can become stale if core rules change without regeneration.
- Content attention may be confused with demand unless E5/E7 metrics stay separated.
- External writeback remains blocked until explicit owner approval and a separate task contract.

## Approval-Gated Next Actions

Prepare but do not execute without explicit approval:

1. Show Git status and diff summary.
2. Run final public safety and validation checks.
3. Regenerate dashboard data if required.
4. Update KB/log/run handout.
5. Commit changes.
6. Push to Git.
7. Update website/dashboard/report links if deployment path requires it.
8. Prepare or perform Notion E1-E7 update only if connector access and explicit approval exist.
