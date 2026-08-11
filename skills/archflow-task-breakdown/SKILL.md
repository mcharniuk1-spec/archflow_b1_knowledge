---
name: archflow-task-breakdown
description: Turn a caller-supplied approved objective into ordered, verifiable task packets with dependencies, sole-writer ownership, acceptance checks, approval gates, and handoffs. Use when an individual or team needs a portable research, definition, action, review, or knowledge-maintenance plan without relying on a task board, scheduler, provider, or private workspace.
---

# ArchFlow Task Breakdown

Create the smallest task graph that can reach an observable result.

## Required input

Require the caller to provide:

- objective, decision, required artifact, and done conditions;
- approved evidence paths and exclusions;
- available role IDs, exact targets, dependencies, and existing blockers;
- authority limits, reviewer, budget or attempt cap, and stop conditions.

If these fields are incomplete, expose the gap before sequencing work. Do not infer authority or search unrelated local material.

## Workflow

1. Restate the objective as one measurable outcome and list explicit non-goals.
2. Choose the relevant stage: research, define, act, review, or remember.
3. Use `project/agents/actionable-role-packs.json` when one of its four packs fits. Otherwise select the smallest custom role set allowed by the canonical catalog.
4. Split work into tasks that each have one owner, one output, one target set, and one verification result.
5. Order dependencies before dependants. Parallelize only tasks with non-overlapping targets.
6. Add source, permission, provider, external-action, reviewer, rollback, and readback gates where applicable.
7. Stop after the same failed repair repeats twice, authority changes, a file conflict appears, or required evidence is missing.

## Task packet

For every task include:

- ID and concise title;
- purpose and dependency IDs;
- approved inputs and exclusions;
- canonical role owner and packaged skills;
- exact output and target path;
- acceptance check and evidence to retain;
- forbidden effects, repair limit, stop rule, reviewer, and handoff.

Use FACT, INTERPRETATION, HYPOTHESIS, and GAP only when the distinction affects a decision.

## Output

Return the task graph through the dashboard Communication Center, or write it to `project/local/<case-id>/task-graph.md`. The local path is ignored and must not be committed.

The graph is a proposal until reviewed. It must not start a role, install a dependency, activate a provider, create credentials, mutate an external system, push Git, deploy, publish, or promote durable knowledge.
