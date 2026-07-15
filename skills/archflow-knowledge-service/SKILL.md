---
name: archflow-knowledge-service
description: Prepare a source-bounded ArchFlow knowledge report before agent design or implementation. Use for a public repository, project brief, approved source summary, PRD/ICP request, or knowledge-base setup that needs facts, interpretations, hypotheses, gaps, provenance, outputs, and an owner review gate without ingesting private material or starting a provider, agent, repository, or external write.
---

# ArchFlow Knowledge Service

Create a reviewable knowledge handoff, not a hidden ingestion or execution job.

## Required intake

Collect only:

- Goal and decision the output must support.
- Public repository reference or non-sensitive project label. Do not clone or fetch it unless separately authorized.
- Allowed evidence and explicit exclusions.
- Requested output, constraints, stop conditions, and named reviewer.

If the source boundary or reviewer is missing, record a GAP and prepare questions rather than inferring authority.

## Workflow

1. Read the project routing, operating rules, CAG core, and relevant public WikiLLM indexes.
2. Build the smallest context capsule. Classify every meaningful statement as FACT, INTERPRETATION, HYPOTHESIS, or GAP.
3. State provenance and freshness for every FACT; do not treat retrieval rank as truth.
4. Prepare an architecture report with the objective, source boundary, requested outputs, classification, reviewer questions, and next safe action.
5. Mark the report `review_required_not_executed`. Do not create files, activate a provider, write a database, or promote memory automatically.

## Handoff contract

The report must let Agent Control reuse the approved context without re-collecting it. Include a stable report ID, summary, source boundary, facts, interpretations, hypotheses, gaps, and approval state.

Use `project/workflows/llamaindex-rag.yaml` only as a configuration contract. Use `project/context/cag-core.yaml` for stable context. Record durable, reviewed conclusions through the public WikiLLM contract after the appropriate approval.

## Forbidden actions

- Ingest a whole device, home directory, or unbounded repository.
- Send private material, credentials, tokens, or raw transcripts to a model or report.
- Present a browser-local report as a live knowledge-base write.
- Activate a provider, create a repository change, or perform external writeback without an explicit action-specific approval.
