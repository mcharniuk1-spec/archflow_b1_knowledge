---
name: archflow-agent-control
description: Convert a caller-supplied, approved evidence report into a bounded role, task, permission, review, and stop contract. Use when an individual or team needs to select the smallest canonical role pack and prepare an inspectable work handoff without launching a provider, changing files, or writing externally.
---

# ArchFlow Agent Control

Design the control packet for a case. Do not execute the case.

## Input contract

Accept only a caller-supplied approved report or a validated packet from the dashboard Communication Center. Require:

- case ID, objective, decision, and expected artifact;
- approved source paths plus explicit exclusions;
- requirements, assumptions, contradictions, and gaps;
- case authority, exact targets, budget or attempt cap, and stop conditions;
- named independent reviewer and required readback.

Stop when the evidence boundary or approval state is unclear. Do not retrieve hidden workspace context to fill a missing field.

## Workflow

1. Verify the input provenance and `review_required` or approved state without changing it.
2. Read `project/system/contracts/role-catalog.json` and select the smallest suitable pack from `project/agents/actionable-role-packs.json`.
3. Bind each active role to one owned output, allowed input set, packaged skills, tool ceiling, permission mode, reviewer route, and handoff.
4. Give each shared target one writer. Parallelize only independent targets.
5. Define deterministic checks, a maximum of two repair attempts for the same failure, rollback, and terminal states.
6. Mark provider calls, Git actions, deployment, publication, durable knowledge promotion, and every other external effect as separately gated.
7. Return the packet for independent review. Do not launch the declared roles.

## Output

Return a Markdown or JSON control packet through the Communication Center, or write it to `project/local/<case-id>/agent-control-packet.*`. The local path is ignored and must not be committed.

Include the selected pack, role bindings, dependency graph, exact targets, source boundary, checks, stop rules, gates, reviewer, readback, unresolved gaps, and `state: review_required_not_executed`.

## Boundaries

- A role name or package never grants authority.
- A maker cannot approve its own high-risk output.
- Do not activate a provider, create credentials, change a repository, contact anyone, deploy, publish, or write to an external system.
- Do not copy raw personal input into the control packet.
- If a requested role or package is outside the canonical catalog, stop and request an explicit contract update rather than inventing it.
