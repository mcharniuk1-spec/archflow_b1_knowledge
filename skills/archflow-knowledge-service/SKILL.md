---
name: archflow-knowledge-service
description: Prepare a source-bounded ArchFlow knowledge review packet before agent design or implementation. Use for a public repository, project brief, approved source summary, research request, or knowledge setup that needs facts, interpretations, hypotheses, gaps, provenance, reviewer questions, and an optional reviewed solution-memory candidate without ingesting private material or starting a provider, agent, repository action, or external write.
---

# ArchFlow Knowledge Service

Create a reviewable knowledge handoff, not a hidden ingestion or execution job.

## Required intake

Collect only:

- goal and decision the output must support;
- public reference or non-sensitive project label; do not fetch or clone it unless separately authorized;
- allowed evidence and explicit exclusions;
- requested output, constraints, stop conditions, and independent reviewer;
- output mode: `inline_only` or a caller-supplied Git-ignored local directory.

If the source boundary or reviewer is missing, record a GAP and prepare questions instead of inferring authority. Before a repository-local write, confirm the output target with `git check-ignore -- path/to/output`.

## Workflow

1. Read the operating rules, `project/context/cag-core.yaml`, and only the task-relevant allowlisted sources.
2. Build the smallest context capsule against `project/context/context-capsule.schema.json`.
3. Classify every meaningful statement as FACT, INTERPRETATION, HYPOTHESIS, or GAP.
4. Give every FACT a public-safe source reference and freshness state. Retrieval rank is not truth.
5. Prepare a knowledge report with objective, decision, source boundary, requested output, classifications, reviewer questions, and next safe action.
6. Mark it `review_required_not_executed`. Do not activate a provider, start agents, edit a repository, write a database, or perform external writeback.

## Handoff contract

Include a stable report ID, summary, source boundary, facts, interpretations, hypotheses, gaps, acceptance criteria, reviewer role, approval state, and next safe action. Reuse the report by ID; do not duplicate raw source material in downstream task packets.

Use `project/workflows/llamaindex-rag.yaml` only as a provider-neutral retrieval configuration and keep lexical fallback. Use `project/database/review-bundle.schema.json` only when exporting a browser-local review bundle; display metadata inside that bundle never grants authority.

After an independent `approve` verdict, shape only reusable, source-grounded meaning as a candidate that validates against `project/database/solution-memory-record.schema.json`. Validation is not promotion. Record `revise` or `block` findings instead of forcing a memory write.

## Local output boundary

Save reports, context capsules, and candidates only under the caller-supplied ignored local directory. If no safe directory was supplied, return the packet inline and do not create files. Do not rely on tracked run archives, live logs, wiki folders, dated plans, or automation state.

## Forbidden actions

- Ingest a whole device, home directory, broad workspace, or unbounded repository.
- Send private material, credential values or presence, raw transcripts, or private identifiers to a model or report.
- Present a browser-local report, retrieval result, or valid schema instance as a live knowledge-base write.
- Promote memory without an independent reviewer and proof references.
- Activate a provider, create a repository change, deploy, publish, or perform external writeback without an action-specific approval and current capability proof.
