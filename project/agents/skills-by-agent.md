# Skills By Agent

Only skills used or set up for this public project are listed here.

## Skill Governance

Purpose: keep skills explicit, deduplicated, role-aware, and reviewable.

Rules:

- Hermes, Codex, AF Review, and AF Knowledge may inspect all skills.
- Bounded subagents receive only role-specific skills plus shared coordination skills named in their task contract.
- Do not create new `SKILL.md` files for conceptual methods until the checklist in [`skills-governance.md`](skills-governance.md) is satisfied.
- Shared project skills are allowed to appear under multiple roles when they carry coordination or closeout responsibilities.
- Backticked catalog names and linked project-local paths are executable skill packages. Plain names are project methods/checklists unless a task contract resolves them to an installed package.

## Role / Runtime Binding

The named entries below are current role bindings and skill visibility records, not permanent authority assignments to a particular runtime, provider, model, or branded agent. A compatible runtime may fulfil a bounded role only when it follows that role's task contract, evidence duties, and forbidden actions. A runtime may not approve its own high-risk output merely because it fulfils more than one role.

## Hermes Watchdog

Purpose: planned controller/reviewer layer for classification, context capsules, task contracts, evidence review, and stop decisions.

Skills set up:

- execution-type-classification
- cag-core-assembly
- context-capsule-review
- task-contract-writing
- evidence-review
- stop-rule-enforcement

Boundary: Hermes does not execute code, edit files, deploy, mutate external systems, activate providers, or approve its own high-risk output.

## Goal Architect And Architecture Operator

Purpose: turn one objective into a verifiable goal, then generate or review a parameterized agent architecture without confusing design, fixture proof, and runtime proof.

Skills set up:

- [`archflow-architecture-operator`](../../skills/archflow-architecture-operator/SKILL.md) - defines authority, goal, context, task graph, role packs, loops, verification, memory promotion, tool adoption, and benchmark gates.
- goal-contract-writing
- acceptance-criteria-writing
- budget-and-kill-switch-design
- agent-security-governance
- skill-creator

Boundary: the role may design a tool or role architecture but may not install external code, activate a provider, or claim performance improvement without the adoption and benchmark gates.

## Terra Integrator And Luna Workers

Purpose: use one high-impact integrator and bounded workers without creating concurrent writers or ambiguous responsibility.

Skills set up:

- Terra: `archflow-architecture-operator`, `archflow-task-breakdown`, `task-handout`, evidence reconciliation, and the specific task-board or artifact skill.
- Luna: one task-specific skill, source-boundary control, and FACT / INTERPRETATION / HYPOTHESIS / GAP reporting.

Boundary: Luna workers are read-only by default. Terra is the sole writer for a shared artifact or external task-board mutation. A separate AF Review role verifies high-risk output.

## AF Tools

Purpose: inspect allowed sources and tools without broad ingestion.

Skills set up:

- public-source-inventory
- provider-readiness-check
- ollama-local-check
- git-publication-check
- [`archflow-e1-runtime-guard`](../../skills/archflow-e1-runtime-guard/SKILL.md) - validates the E1 runtime spine before Git push.

## Shared Project Coordination

Purpose: keep all public project agents aligned on live communication, file claims, local dashboard/Jarvis runtime boundaries, and gated activation rules.

Skills set up:

- [`arcagcom`](../../skills/arcagcom/SKILL.md) - coordinates public project agents through the live communication log, file claims, handoffs, and Prompt 2.1 / Prompt 3 merge gates.
- [`archflow1`](../../skills/archflow1/SKILL.md) - defines the local Jarvis dashboard stack contract, provider-disabled runtime boundaries, voice path, OpenRouter budget gates, and Railway migration gates.

## Knowledge Service And Agent Control

Purpose: make the public two-stage method explicit. Knowledge Service prepares the source-bounded report first; Agent Control consumes that reviewed report to propose roles, skills, routes, gates, and handoff files.

Skills set up:

- [`archflow-knowledge-service`](../../skills/archflow-knowledge-service/SKILL.md) - collects a bounded objective, evidence boundary, FACT / INTERPRETATION / HYPOTHESIS / GAP classification, requested outputs, reviewer questions, and a local report without hidden ingestion or execution.
- [`archflow-agent-control`](../../skills/archflow-agent-control/SKILL.md) - turns a reviewed report into a bounded role map, tool/skill allowlists, maker-reviewer split, stop rules, and proposed files marked for operator review.

Boundary: the dashboard and Jarvis can prepare and download local reports. They cannot launch agents, fetch a repository, authenticate a guest, create files, activate a model provider, or write to Git, a database, Notion, Nexus, or a deployment target.

## AF Context

Purpose: turn approved source material into structured English context.

Skills set up:

- notion-spec-to-implementation
- notion-knowledge-capture
- english-public-summary
- fact-interpretation-hypothesis-gap
- cag-core-assembly
- bounded-rag-evidence-selection

## AF Manager

Purpose: convert context into PRD, milestones, owners, and execution tasks.

Skills set up:

- [`archflow-task-breakdown`](../../skills/archflow-task-breakdown/SKILL.md) - decomposes ArchFlow epics and Notion tasks into staged subtasks, gates, checks, and public-safe reports.
- [`task-handout`](../../skills/task-handout/SKILL.md) - creates readable execution handouts and continuation prompts for the next agent.
- [`outquestions`](../../skills/outquestions/SKILL.md) - reports execution outcomes and the questions/gates needed before moving to the next stage.
- prd-from-dialogue
- responsibility-assignment-extraction
- milestone-planning
- acceptance-criteria-writing
- [`archflow-architecture-operator`](../../skills/archflow-architecture-operator/SKILL.md) when the requested output is a reusable role architecture rather than a one-off task list.

## AF Discovery

Purpose: turn approved customer/product source packets into founder-meeting discovery evidence.

Skills set up:

- `customer-journey-map`
- `discovery-process`
- jtbd-discovery
- ninety-day-story-extraction
- customer-forces-analysis
- five-whys
- source-boundary-control

## AF PRD Architect

Purpose: turn approved discovery evidence into evidence-backed PRD artifacts.

Skills set up:

- prd-from-dialogue
- evidence-backed-requirements
- definition-of-done-writing
- acceptance-criteria-writing
- review-gate-preparation

## AF Task Translator

Purpose: convert reviewed specs/PRDs into task packets, checkbox subtasks, blockers, and owner-decision gates.

Skills set up:

- [`archflow-task-breakdown`](../../skills/archflow-task-breakdown/SKILL.md)
- spec-to-tasks-logic
- task-packet-writing
- notion-ready-markdown
- blocker-and-approval-gate-writing

## AF Research

Purpose: turn approved market sources into account evidence cards, pain maps, ICP scoring, and target shortlists.

Skills set up:

- market-structure-analysis
- research-source-triage
- account-evidence-card-writing
- job-signal-analysis
- review-mining
- icp-scoring
- `company-research`
- `deep-research`
- `decision-mapping`

## AF Knowledge

Purpose: write reusable KB updates and keep public history clean.

Skills set up:

- knowledge-base-update
- [`task-handout`](../../skills/task-handout/SKILL.md) - records human-readable run context, decisions, artifacts, checks, and next actions.
- [`outquestions`](../../skills/outquestions/SKILL.md) - turns completed work into decision questions, risk notes, and next-stage gates.
- sanitized-history-writing
- source-boundary-control
- agent-memory-candidate-writing

## AF Copy

Purpose: draft positioning, content, proposal, and outreach copy only from approved evidence.

Skills set up:

- source-grounded-copywriting
- positioning-synthesis
- content-planning
- outreach-message-drafting
- claim-status-check
- `content-strategy`
- `content-research-writer`
- `copywriting`
- copy-editing

## AF ABM Channel

Purpose: prepare the narrowest evidence-backed path to a verified buyer without autonomous contact.

Skills set up:

- `acquisition-channel-advisor`
- `company-research`
- `customer-journey-map`
- cohort segmentation
- outreach-sequence-design
- CRM hygiene

Boundary: this role may create a reviewed warm-intro, LinkedIn, or email packet. It may not scrape private data, send, connect, follow, enrich in bulk, or mark contact/demand without owner-approved evidence.

## AF Growth Evidence

Purpose: keep attention, conversation, proposal, paid intent, and payment as separate measurable stages.

Skills set up:

- `data-analytics-insight`
- `forecast-validation-and-backtesting`
- `business-health-diagnostic`
- funnel instrumentation
- ROI scenario modeling
- payment-stage classification

Boundary: modeled recovery is not observed savings. The role must show cohort definitions, denominators, missing events, and evidence state and may not invent conversion, causal, revenue, or ROI claims.

## AF Product Packaging Engineer

Purpose: package a validated service contract as an installable repository, least-privilege MCP, admin control plane, and lifecycle documentation after E8.0 and E7.4 pass.

Skills set up:

- `backend-api-architecture`
- `codebase-design`
- `code-clarity-and-docs`
- `agent-security-governance`
- `deployment-observability`
- `debugging-checklist`
- `browser-qa-performance-a11y`

Boundary: this role cannot start productization from desk research alone, enable write tools by default, store secrets, skip uninstall/rollback proof, or approve its own release.

The cross-role sequence, shared state, and stop rules are defined in [`marketing-role-pack.md`](marketing-role-pack.md).


## GloomyLord

Purpose: internal visual/reporting sidecar for public-safe process reports, dashboard proof cards, and carousel template structures.

Skills set up:

- public-reporting-gate
- carousel-structure-design
- evidence-labeling
- dashboard-proof-card-design

Boundary: internal by default; public-facing branding, post copy, and carousel publication require AF Review and owner approval.

## AF Review

Purpose: block unsafe or unsupported outputs before handoff.

Skills set up:

- `agent-security-governance`
- public-safety-review
- secret-and-path-scan
- english-only-check
- claim-status-check
- privacy-and-access-scope review
- source-freshness review
- anti-ICP enforcement
- [`outquestions`](../../skills/outquestions/SKILL.md) - verifies unanswered decisions are visible before approval.

## AF Publisher

Purpose: prepare Git-ready public releases.

Skills set up:

- git-clean-repo-publication
- github-remote-publication
- publication-review-reporting
- [`task-handout`](../../skills/task-handout/SKILL.md) - prepares the public-safe handout that future operators can use after publication or review.
- [`outquestions`](../../skills/outquestions/SKILL.md) - closes publication work with decision questions and next-stage gates.

## Automation

Purpose: keep the skill registry current every evening.

Skills set up:

- [`evening-skill-registry-update`](../../skills/evening-skill-registry-update/SKILL.md) - verifies registry/hook drift and updates scheduled public files only when necessary.
- [`daily-public-project-review`](../../skills/daily-public-project-review/SKILL.md) - produces end-of-day skill, tool, RAG, and knowledgebase retrospective notes plus blacklist updates.
- [`priority-task-operator`](../../skills/priority-task-operator/SKILL.md) - ranks all tasks by urgency + importance, selects one top-priority action, and generates a PitAgent handoff + reliability packet.
- archflow-e1-runtime-guard
- task-handout
- outquestions
