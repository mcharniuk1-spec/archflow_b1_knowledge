# Operations Guide

Status: current Crew Desk workflow

## One operating surface

The Crew Desk projects one Knowledge Case. Browser-local drafts are not authentication, durable memory, runtime events, or execution receipts.

Use:

- **Today** to understand the current mission and ask Taras for deterministic workflow guidance.
- **Work** to define the goal, role, output, evidence boundary, workflow pack, risk, reviewer, and stop condition.
- **Knowledge** to understand sources, framework parameters, diagrams, research methods, and skill governance.
- **Team** to inspect role responsibilities and select the smallest workflow pack.
- **Review** to follow evidence → requirement → maker → validator → independent reviewer → receipt → promotion.
- **Set up** to prepare a bounded local configuration proposal.

## Mission sequence

1. Orient the case and authority.
2. Assemble stable CAG plus task-specific evidence.
3. Reconcile facts, interpretations, hypotheses, contradictions, and gaps.
4. Approve current requirement versions and acceptance checks.
5. Select the smallest responsible crew.
6. Produce a reviewable candidate and verification plan.
7. Validate requirements, authority, effects, rollback, and readback.
8. Run deterministic checks and independent review.
9. Interrupt for target-specific approval when required.
10. Perform at most one approved action.
11. Read back the exact target.
12. Propose reusable meaning for reviewed promotion.

## Review-packet handoff

The browser export includes the case, selected workflow pack, local configuration proposal, and explicit zero-action boundary.

```text
browser-local mission
  -> JSON review packet
  -> approved controller/operator admission
  -> exact retrieval and requirement validation
  -> scoped maker work
  -> deterministic verification
  -> independent review
  -> optional exact approval/action
  -> readback and receipt
```

The packet is not a Git patch, changed file, model response, database row, approval, or action receipt.

## Real runtime event

A live projection requires at least:

- case/run ID;
- node and state;
- observed timestamp;
- evidence/requirement references;
- actor and authority scope;
- provider and writeback state;
- receipt/readback reference.

Without this state, the UI must say configured, browser-local, gated, or unknown—not live.

## Manager/owner interrupts

Stop for:

- missing requirement owner;
- material contradiction;
- stale or private source without authority;
- external communication;
- private-data provider use;
- irreversible/destructive change;
- production/deployment/release;
- credentials, spend, or durable external writeback.

Resume only with a JSON-safe exact decision. Side effects occur after the interrupt and use an idempotent action ID.

## Knowledge update

After an accepted result, Larysa searches for duplicates and prepares a promotion candidate with source, requirement, decision, result, owner, review date, and supersession. Raw traces and secrets are excluded.

See [Crew Desk manual](dashboard-operating-manual.md) and [responsive architecture](responsive-knowledge-crew-architecture.md).
