---
name: task-handout
description: Create a public-safe execution handout after substantial work, multi-agent routing, subtask execution, review, or a requested continuation. Use when another operator needs a readable human summary plus an agent-ready continuation prompt grounded in changed files, decisions, validation evidence, open gaps, authority limits, and the next safe action.
---

# Task Handout

Create a human-readable bridge from completed evidence to the next bounded action. A handout summarizes work; it does not replace state, review, receipt, or solution-memory contracts.

## Required input

Collect only public-safe information:

1. goal, scope, and current stage;
2. files created or changed;
3. task and subtask status;
4. decisions and their evidence;
5. checks and outcomes;
6. gaps, deferred work, and pending gates;
7. exact continuation boundary, reviewer, and stop conditions;
8. output mode: `inline_only` or a caller-supplied Git-ignored local directory.

Do not reconstruct missing evidence from chat assumptions. If status cannot be proved, mark it as a GAP.

## Output boundary

When a local artifact is requested, require the caller to supply the output directory. Before writing inside a repository, confirm the path with `git check-ignore -- path/to/output`. Save the handout there as `agent-handout.md`. If the path is not ignored or no path was supplied, return the handout inline and do not create a file.

Do not depend on tracked run folders, live-log archives, wiki folders, dated plans, prompt hooks, or automation state.

## Required structure

1. **Title and purpose** — identify the task and intended next operator.
2. **Human summary** — use two to five clear paragraphs explaining what changed, why it matters, and what remains.
3. **Current state** — separate configured, locally checked, executed, independently reviewed, externally verified, blocked, and not recorded.
4. **Continuation prompt** — provide a copy-ready goal, context references, constraints, first steps, expected outputs, review gate, and stop conditions.
5. **Execution trace** — summarize the sequence and label meaningful FACT, INTERPRETATION, HYPOTHESIS, and GAP statements.
6. **Decisions** — record accepted and deferred decisions with rationale.
7. **Artifacts** — use repository-relative or packet-relative references and explain each artifact's purpose.
8. **Validation** — list pass, fail, skipped, and pending checks; explain every skip.
9. **Next actions** — order the smallest safe steps and name role ownership.
10. **Safety boundary** — state what must not be ingested, copied, published, logged, or executed.

## Contract links

- Reference the canonical run state with `project/database/run-envelope.schema.json` when one exists.
- Reference independent browser-local review with `project/database/review-bundle.schema.json`; its display fields do not grant authority.
- Reference verified actions with `project/database/action-receipt.schema.json` only when the action and readback occurred.
- Reference reusable reviewed meaning with `project/database/solution-memory-record.schema.json`; a candidate is not automatically promoted.
- Reference active coordination packets produced by `arcagcom` rather than copying their full history.

## Writing rules

- Keep the handout in English and readable for a human first.
- Link to artifacts instead of duplicating large bodies or traces.
- Preserve exact facts, hashes, measured denominators, commands, and limitations.
- Never include secrets, credential values or presence, personal identities, private URLs, local absolute paths, account identifiers, raw private source text, or unapproved screenshots and transcripts.
- Do not turn a prepared handoff, valid schema instance, configured adapter, or local check into a claim of external completion.

## Done criteria

A new operator can identify the goal, locate approved artifacts, understand what was actually verified, see the remaining gates, continue without repeating discovery, and avoid exceeding the original authority. Local output is either proven ignored or was not written.
