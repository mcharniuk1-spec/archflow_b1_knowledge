# Daily Skill Retrospective And RAG Knowledge Review

Automation ID: `daily-skill-rag-knowledge-review`

Status: active in Codex app automation.

Schedule: daily at 22:30.

Contract source: `project/agents/agent-roster.yaml` (`daily_skill_rag_retrospective` job lane).

Purpose

Run the end-of-day review lane that checks skills, knowledgebase writeback health, RAG corpus boundaries, and recurring inefficiency patterns so each next day starts with a tighter operating plan.

Scope

Read:

- `project/runs/`
- `project/agents/model-efficiency-advice.md`
- `project/agents/model-efficiency-issues.md`
- `skills/daily-public-project-review/SKILL.md`
- `skills/skills-used.md`
- `project/agentic-stack.md`
- `project/scripts/llamaindex-approved-corpus.py` command summary or output (if present),
- `project/live/communication/agent-communication-log.md`,
- `wiki/memory.md`
- `wiki/insights.md`
- `wiki/log.md`.

Write:

- `project/runs/<run-id>/run-summary.md`,
- `project/runs/<run-id>/agent-handout.md`,
- `wiki/log.md`,
- `wiki/memory.md` (only when recurring constraints repeat and are likely stable),
- `wiki/insights.md` (for durable cross-run inefficiency rules),
- `project/live/communication/agent-communication-log.md`.

## Long-Term Knowledge Update Gate

This lane must update long-term knowledge surfaces when recurring non-value patterns repeat across cycles:

- move repeated inefficiency definitions to `wiki/insights.md`,
- mirror durable cross-run constraints into `wiki/memory.md`,
- add a short constraint note to `project/live/communication/agent-communication-log.md`,
- and only return to execution mode if constraints are re-assessed or a new explicit override is approved.

## Required Review Sections

Each execution should produce explicit sections for:

1. Skills effectiveness review:
   - which skills were used,
   - which were useful,
   - and which were bypassed.
2. RAG/KB boundary checks:
   - approved public corpus,
   - query/retrieval quality evidence,
   - knowledgebase impact and corpus delta.
3. Day scope check:
   - all same-day public runs that should inform this review.
4. Inefficiency review:
   - tools or approaches that repeatedly add latency, ambiguity, or low signal,
   - severity as low/medium/high,
   - lane-local blacklist updates with owner decision,
   - and a cross-lane comparison to avoid keeping redundant approaches active.

## Safety and Quality Constraints

- This lane is review-only unless the prompt explicitly asks for edits.
- No provider API calls.
- No local absolute paths or secrets.
- No raw private source text.
- RAG evidence must remain bounded to approved public source folders:
  - `project/`
  - `history/`
  - `skills/`
  - `wiki/`

## Failure Handling

- If no run source exists for a prior run, add a `GAP` and continue with prior-day evidence.
- If RAG summary files are missing, record blocked status and request a bounded retrieval smoke run in the next scheduled plan.
- If the "do-not-repeat" list grows repeatedly, escalate as a durable memory update note.
