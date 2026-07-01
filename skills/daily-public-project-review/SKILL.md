---
name: daily-public-project-review
description: Run a daily retrospective over skills, tool usage, RAG retrieval state, and knowledgebase updates so the next cycle carries forward evidence and excludes recurring low-value work.
---

# Daily Skill Retrospective And RAG Knowledge Review

## Purpose

Use this skill as the second daily lane after the evening maintenance pass. It reviews what changed during the day and verifies:

- which skills were used and were useful,
- whether each skill output supported the current ArchFlow thesis and knowledgebase contract,
- what changed in retrieval quality,
- which tool paths repeatedly wasted time,
- and what should be carried into the next day's plan.

## When To Use

- In the daily routine that follows evening registry/hook maintenance.
- After major public runs, knowledgebase packets, or model-efficiency notes.
- When scheduled reviewers detect repeated no-op runs or recurring noise.

## Required Inputs

Read at least:

- `project/runs/`
- `project/agents/model-efficiency-advice.md`
- `project/agents/model-efficiency-issues.md`
- `project/agentic-stack.md`
- `project/agents/agent-roster.yaml`
- `skills/skills-used.md`
- `wiki/memory.md`
- `wiki/insights.md`
- `wiki/log.md`
- `project/live/communication/agent-communication-log.md`
- `project/live/communication/README.md` (local communication guide).

Optional:

- `project/local/rag_index/approved-corpus-summary.json` if a retrieval check exists.

## Retrospective Workflow

1. **Collect and normalize day evidence**
   - Pull the day's run artifacts from `project/runs/`.
   - Mark each run status as `complete`, `blocked`, or `no-op`.
   - Pull every scheduled/public-facing skill output from the same day into one review list.
   - Prefer FACT-checked sources from run summaries and handouts.
2. **Skills effectiveness review**
   - List which registered skills ran, were referenced, and were not used.
   - For each used skill, record output usefulness, reuse value, and failure points.
   - If a skill is repeatedly unused but kept in schedules without reason, mark it for reassessment and do not call it "healthy".
3. **RAG and knowledgebase review**
   - Confirm retrieval still points to approved corpus folders.
   - Confirm no unbounded source is introduced.
   - Confirm any corpus update is reflected in `skills/` and `project/agentic-stack.md` if it changes retrieval assumptions.
   - Record one concise KB impact sentence per domain touched.
4. **Inefficiency review**
   - Record tools or approaches that repeatedly add latency, ambiguity, or low signal.
   - Mark each inefficiency with severity: low/medium/high.
   - Keep a minimal blacklist and an owner decision for each candidate exclusion.
   - Compare this lane's pattern against the evening maintenance lane and mark redundant approaches as "do not repeat" unless a named owner exception is approved.
5. **Knowledgebase/Memory impact review**
   - Note what changed in KB inputs, memory candidates, and durable log files.
   - Confirm the global knowledge gate was updated only for repeated constraints or durable strategy changes.
   - Move repeated durable constraints to `wiki/insights.md` when confirmed for the defined run pattern.
6. **Tomorrow handoff**
   - Publish 3 ordered recommendations for the next day.
   - Include a "do not repeat" list for ineffective steps.
   - Add a one-line constraint note to `project/live/communication/agent-communication-log.md`.

## Cross-Lane Inefficiency And Tool Limitation Section

Use this section to explicitly block repetitive and non-productive tools unless a single explicit exception exists:

- full `rg` on large folders when changed paths are known,
- repeated deep reruns of unchanged retrieval jobs,
- full `graphify` or generated report refreshes without source edits,
- blind `curl` pings to local/public endpoints as proof of readiness,
- browser visual checks in non-visual tasks.

Do not treat these as successful progress evidence without evidence:

- one-token/noise prompts that only restate yesterday,
- retries that change command order but not output,
- "successfully skipped" checks when no validation file was generated.

## Output

Produce:

- Daily retrospective table with:
  - Facts observed,
  - Skill use outcomes,
  - RAG/KB state,
  - Inefficiency list,
  - Tool blacklist updates.
- A short `HYPOTHESIS` section only for non-certain findings.
- A concrete list of owner actions for next day.

## Long-Term Knowledge Update Gate

If the same inefficient approach appears in 2+ consecutive runs:

- add it to a lane-local do-not-repeat list,
- mirror into `wiki/insights.md` as durable knowledge,
- and record a short durable decision in `wiki/memory.md` if it changes operating direction.

## Done Criteria

- The daily review links to at least one skill registry source file, one RAG/KB source, and one run artifact.
- Inefficient or irrelevant tools are marked and either deferred or blacklisted.
- A plain-English summary is produced for the following day's operator and for long-term global knowledge memory.
