# ArchFlow Loop Operating Contract

Status: L1 report-only by default

Purpose: make ArchFlow agent runs bounded, reviewable, and stoppable before they write memory, change external systems, publish content, or influence outreach.

## Scope

Applies to E1-E7 workflows that use one or more agent roles, solve one or more subtasks, perform research, update memory, prepare public output, or create outreach/copy.

## Current Loop Level

| Level | Meaning | ArchFlow status |
|---|---|---|
| L0 | Draft-only one-off run | Allowed for low-risk notes. |
| L1 | Report-only loop with state, review, and handout | Default for E1, E2, E4, E5, E6, and E7. |
| L2 | Assisted local file changes after review | Allowed for public-safe repo docs/configs. |
| L3 | Unattended automation | Not allowed before payment verdict and explicit approval. |

## Required State

Every loop run needs:

- `run_id`
- `task_id`
- source IDs and allowed corpus
- phase
- attempt count
- max attempts
- maker agent
- verifier agent
- files read
- files written
- unsupported claims
- gaps
- approval status
- blocked reason when blocked
- next human action

## Attempt Caps

- `max_revision_loops`: 2
- `max_attempts_per_item`: 3
- Same maker/verifier for high-risk output: block
- Source boundary failure: block immediately
- No new evidence or no actionable item: early exit with run log

## Human Gates

Human approval is required before:

- writing outside the public project
- writing to Notion
- writing to live Obsidian/Nexus
- sending outreach
- publishing website or public claims
- sending private material to any cloud model
- starting broad ingestion

## Maker/Checker Rule

AF Manager, AF Research, and AF Copy can draft. AF Review approves, rejects, or blocks. A maker cannot approve its own final output.

## Memory Rule

WikiLLM is canonical. LlamaIndex/turbovec indexes are rebuildable retrieval artifacts. Cognee is a future operational memory layer only after E1.3 readback passes and AF Review approves the memory packet.

## Stop Conditions

Stop and write a blocked handout when:

- private or raw source material cannot be safely summarized
- a public/client claim lacks evidence
- a loop repeats without new evidence
- budget or model cap is reached
- role verification is stale or missing before outreach
- Notion or external write scope is unclear
