---
name: priority-task-operator
description: Select the highest-priority actionable task from a caller-supplied plan and prepare a bounded execution handoff. Use when an individual or team needs deterministic urgency-and-importance ranking, dependency and blocker filtering, transparent rationale, stop conditions, and local review artifacts without relying on a dated project plan, scheduler, task-board connector, tracked run archive, or external write.
---

# Priority Task Operator

Select one next task from explicit inputs. Do not discover work from hidden memory, old plans, recurring automation, or an external task board.

## Required input

Require:

- a caller-supplied JSON plan that validates against [priority-plan.schema.json](references/priority-plan.schema.json);
- a named reviewer and current decision horizon;
- either `inline_only` or a caller-supplied Git-ignored local output directory;
- any caller-specific tie-break rule, or acceptance of the default rule below.

Do not fetch a plan or connector state automatically. Before writing under a repository, confirm the target with `git check-ignore -- path/to/output`. If the plan, reviewer, or safe output mode is missing, return a GAP and stop.

## Eligibility

Exclude `done` and `cancelled`. Treat a task as not actionable when its status is `blocked`, its blocker list is non-empty, or one of its declared dependencies is not complete in the supplied plan. Keep excluded tasks in the rationale so a reviewer can see why they were not selected.

Never reinterpret a task's risk level as permission. Provider calls, credential use, Git push, deployment, publication, destructive actions, and external writes require their own action-specific approval.

## Default deterministic ranking

Sort actionable unfinished tasks by:

1. importance, descending;
2. urgency, descending;
3. status order: `in_progress`, `review`, `todo`, `backlog`;
4. due date, earliest first, with no date after dated tasks;
5. task ID, ascending.

Use only the values in the supplied plan. If the caller needs a different policy, record it before ranking and apply it consistently to every task.

## Handoff

Prepare:

- selected task and the ordered eligible list;
- excluded tasks with reason;
- one-line importance and urgency rationale;
- source-plan hash or stable caller reference;
- dependencies, blockers, risk, allowed actions, forbidden actions, and stop conditions;
- expected artifact, validation checks, independent reviewer, and next safe action;
- provider calls and external writes, both zero unless separately executed and evidenced.

Write `selected-task.json` and `task-handoff.md` only inside the supplied ignored output directory, or return both inline. A handoff is not task completion.

## External-system boundary

If the caller requests a task-board, Git hosting, messaging, or knowledge-system follow-up, represent it as a proposed action with target class, required approval, rollback, and readback check. Do not connect, send, push, publish, or mark external state from this skill.

Use `project/database/action-receipt.schema.json` only after an approved action actually ran. Use `task-handout` for a human-readable continuation summary and `arcagcom` for active coordination.

## Done criteria

- The input plan is caller-supplied and schema-valid.
- The selected task is actionable under the declared dependencies and blockers.
- Ranking and exclusions are reproducible from the supplied fields.
- The reviewer, gates, checks, and stop conditions are explicit.
- Local outputs are ignored or returned inline.
- No provider, external write, or completion claim was inferred from the handoff.
