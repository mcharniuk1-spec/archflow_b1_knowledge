# Skills By Agent

Only skills used or set up for this public project are listed here.

## Skill Governance

Purpose: keep skills explicit, deduplicated, role-aware, and reviewable.

Rules:

- Hermes, Codex, AF Review, and AF Knowledge may inspect all skills.
- Bounded subagents receive only role-specific skills plus shared coordination skills named in their task contract.
- Do not create new `SKILL.md` files for conceptual methods until the checklist in [`skills-governance.md`](skills-governance.md) is satisfied.
- Shared project skills are allowed to appear under multiple roles when they carry coordination or closeout responsibilities.

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

## AF Discovery

Purpose: turn approved customer/product source packets into founder-meeting discovery evidence.

Skills set up:

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

- public-safety-review
- secret-and-path-scan
- english-only-check
- claim-status-check
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
