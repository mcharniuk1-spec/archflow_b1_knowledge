# ArchFlow Content Template Library

Status: active template library
Default ICP: B2B SaaS product leaders for the Product Discovery-to-Production PRD Pack
Default channel: LinkedIn first, then adapted excerpts for X and Threads after review
Default voice: ArchFlow company content first
Default visual style: product-system and research-lab

## Purpose

These templates turn executed ArchFlow work into public-safe content planning assets. They are not publish-ready copy by themselves. Each execution still needs artifact evidence, evidence labels, AF Review, and owner approval before publication.

## Template Set

| Template | Use after | Output |
|---|---|---|
| `carousel-template.md` | A proof run, review gate, or method step has artifact evidence | LinkedIn carousel plan with slide copy, visual notes, and approval gate |
| `implementation-proof-post-template.md` | A task produces a working artifact, validation result, or reviewed process proof | Company post showing what was implemented and how it was checked |
| `dashboard-update-template.md` | Dashboard status, read-only evidence, or reporting surface changes | Public-safe dashboard update without private state or fake live claims |
| `research-check-task-template.md` | A research, ICP, market-signal, or account-evidence task runs | Evidence-card style research/check task write-up |
| `review-gate-template.md` | AF Review or another gate approves, blocks, or requests edits | Review verdict with issue list and required next action |
| `after-execution-report-template.md` | Any executed task needs durable reporting | Run report with proof, outputs, checks, approvals, and save locations |

## Global Defaults

- Audience: Directors or VPs of Product, Heads of Product, Product Ops leads, and senior PM leaders in B2B SaaS scaleups.
- Offer frame: raw product-team material becomes a reviewed PRD, backlog, acceptance criteria, decision log, and KB handoff.
- Content identity: ArchFlow company content first, not personal build-in-public content.
- Evidence labels: FACT, INTERPRETATION, HYPOTHESIS, GAP.
- Allowed style: source boundaries, artifact before/after blocks, redaction bars, source-status chips, simple process diagrams, proof cards.
- Blocked style: private screenshots, raw transcripts, private links, credentials, operational IDs, local paths, customer logos, named target accounts, fake dashboards, demand or ROI claims before E6/E7 proof.

## Save Locations After Each Execution

For each executed content task:

1. Save the raw execution report under `project/runs/<epic>/<date-run-name>/` or the active run folder.
2. Save the content planning artifact under `project/content/templates/` only if it is reusable.
3. Save one-off draft plans under the relevant run folder, for example `project/runs/E1.5/<date-run-name>/carousel-plan.md`.
4. Add AF Review output beside the draft as `review-gate.md` before owner approval.
5. Publish nowhere until owner approval is recorded in the run folder.

## Minimum Approval Checklist

- Public-safe source artifacts exist and are repo-relative.
- Each meaningful claim has an evidence label.
- No private links, secrets, raw transcripts, personal identifiers, local paths, or unapproved screenshots are present.
- Demand, customer proof, revenue, or ROI claims are absent unless E6/E7 evidence exists.
- AF Review has approved safety, claim status, English-only text, and audience fit.
- Owner approval is recorded before any post, carousel, or dashboard-linked publication.
