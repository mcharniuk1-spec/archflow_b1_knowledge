---
name: outquestions
description: Turn caller-supplied execution evidence into a concise outcome summary, blocking decisions, actionable gaps, and the next safe gate. Use after bounded planning, implementation, review, observation, release preparation, or an approved external action when another person must decide what can happen next.
---

# Outquestions

Close a bounded piece of work without turning uncertainty into a completion claim.

## Required input

Accept only the caller-supplied case objective, artifact list, check results, receipts, approval state, and known gaps. Do not search unrelated project history or infer what happened from a status label.

## Workflow

1. State what changed and why it matters in two or three plain paragraphs.
2. List exact repo-relative artifacts or public target labels. Never include credentials, personal identifiers, private URLs, or machine paths.
3. Separate blocking decisions from optional refinements. For each blocking question, explain what changes for each answer.
4. Name the smallest safe next action and the evidence required before it starts.
5. Use FACT, INTERPRETATION, HYPOTHESIS, and GAP where the distinction affects the decision.
6. Keep provider activation, external write, publication, deployment, Git action, and durable knowledge promotion behind their separate gates.

## Output

Return the result through the dashboard Communication Center, or write it to `project/local/<case-id>/outquestions.md`. The local path is ignored and must not be committed.

Use this shape:

```md
## Outcome

...

## Artifacts and evidence

- ...

## Blocking decisions

1. Question?
   Why it matters:
   If approved:
   If not approved:

## Optional refinements

- ...

## Next safe gate

Action:
Required evidence and approval:

## Risks and gaps

- FACT:
- INTERPRETATION:
- HYPOTHESIS:
- GAP:
```

## Reliability boundary

Do not call work ready when required checks, review, approval, rollback, or readback are missing. Do not ask the caller to repeat a decision already evidenced in the supplied packet. Never perform the next action from this skill; expose the gate and hand it to the authorized role.
