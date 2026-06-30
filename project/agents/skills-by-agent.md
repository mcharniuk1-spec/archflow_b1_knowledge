# Skills By Agent

Only skills used or set up for this public project are listed here.

## AF Tools

Purpose: inspect allowed sources and tools without broad ingestion.

Skills set up:

- public-source-inventory
- provider-readiness-check
- ollama-local-check
- git-publication-check
- [`archflow-e1-runtime-guard`](../../skills/archflow-e1-runtime-guard/SKILL.md) - validates the E1 runtime spine before Git push.

## AF Context

Purpose: turn approved source material into structured English context.

Skills set up:

- notion-spec-to-implementation
- notion-knowledge-capture
- english-public-summary
- fact-interpretation-hypothesis-gap

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

- evening-skill-registry-update
- daily-public-project-review
- archflow-e1-runtime-guard
- task-handout
- outquestions
