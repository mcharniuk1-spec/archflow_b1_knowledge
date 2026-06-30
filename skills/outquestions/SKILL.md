---
name: outquestions
description: Use this skill after each substantial ArchFlow execution, planning pass, Notion task update, GitHub update, dashboard/voice/hosting step, or multi-agent run to produce an execution report with the critical open questions, decisions, owner choices, and next-stage gates needed to move reliably.
metadata:
  short-description: Report execution outcomes and next-stage decision questions
---

# Outquestions

Use this skill when an ArchFlow run needs more than a status note. It turns completed work into a compact execution report plus the questions that must be answered before the next stage starts.

## Trigger

Run this skill after:

- a Notion task or GitHub update
- a dashboard, voice, hosting, Onyx, or agent workflow planning pass
- a multi-agent or sidecar-agent run
- a public-facing content/reporting task
- any execution where the next stage depends on owner decisions

## Output Shape

Write these sections:

1. **What changed**
   - 2-5 plain paragraphs.
   - Explain the action, why it matters, and what is now easier or safer.

2. **Artifacts**
   - List created or updated files, pages, tasks, reports, or commits.
   - Use repo-relative paths for public repo artifacts.
   - Do not include raw private URLs, secrets, private IDs, or local machine paths in public output.

3. **Decision Questions**
   - Group questions by theme.
   - Each question must explain why it matters and what changes depending on the answer.
   - Separate blocking decisions from optional refinements.

4. **Next Stage Gate**
   - State the smallest next action that can be executed safely.
   - State what must be true before live deployment, external writes, public posting, or memory promotion.

5. **Risks And Gaps**
   - Mark each as FACT, INTERPRETATION, HYPOTHESIS, or GAP when uncertainty matters.
   - Include only actionable risks.

## Question Types

Use these categories when relevant:

- **Audience**: Who is this for?
- **Proof**: What evidence is enough?
- **Scope**: What is included, excluded, or deferred?
- **Privacy**: What must stay local/private?
- **Owner**: Who approves the next step?
- **Runtime**: What runs locally, on Vercel, on Railway, or in another tool?
- **Memory**: What becomes durable WikiLLM/Obsidian memory?
- **Design**: What visual system, layout, or style is required?
- **Publishing**: Which channels, cadence, and CTA are approved?

## Reliability Rules

- Do not phrase unanswered decisions as decisions.
- Do not call a workflow ready if it still lacks owner approval, runtime proof, or secret-policy proof.
- Do not move from read-only/status mode to write/action mode without a gate.
- Keep public notes English-only and public-safe.
- Prefer direct, concrete questions over broad brainstorm lists.

## Short Template

```md
## What changed

...

## Artifacts

- ...

## Blocking questions

1. Question?
   Why it matters:
   If yes:
   If no:

## Optional questions

- ...

## Next stage gate

Smallest safe next action:
Gate before live/public/write action:

## Risks and gaps

- FACT:
- INTERPRETATION:
- HYPOTHESIS:
- GAP:
```
