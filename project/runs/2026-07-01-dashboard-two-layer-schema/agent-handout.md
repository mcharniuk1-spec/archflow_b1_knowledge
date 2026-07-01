# Agent Handout: Two-Layer Dashboard Schema Control Panel

## Title And Purpose

Use this handout when continuing the dashboard/Jarvis work after the July 1 two-layer schema UI pass.

## Human Summary

The dashboard now separates the service-product path from the internal control-system path:

- `(1) PRD/ICP Flow` is the externally showable product-service workflow.
- `(2) Agent Orchestra` is the local agentic control workflow.

Each screen uses a draggable block schema. Clicking a node opens a large node control panel for inputs, outputs, connections, dropdown configuration, interpreted run logs, prompts, system prompt, comments, safety, and business-fit fields.

The dashboard is still static/browser-local. It creates review packets and local state only. It does not call providers, store raw transcripts, write to WikiLLM/Obsidian/Notion/GitHub, deploy, or run a backend queue.

The independent review pass found and fixed reliability issues: queueing from the node panel now saves current form edits first, stale localStorage schemas are reset when they do not match the current graph version, connect mode is isolated to the active schema screen, and node-panel section controls no longer mutate the dashboard route hash.

## Current State

Status: implemented, architecture reviewer approved.

Primary files:

- `project/dashboard/app.js`
- `project/dashboard/styles.css`
- `project/dashboard/index.html`
- `project/dashboard/README.md`
- `project/runs/2026-07-01-dashboard-two-layer-schema/run-summary.md`

## Continuation Prompt

```text
Continue ArchFlow dashboard review from the July 1 two-layer schema pass. Inspect #service and #schema in project/dashboard/. Verify that the two paradigms are explicit, nodes are draggable and clickable, the node control panel covers inputs/outputs/connections/config/logs/prompts/comments/safety, and static/offline/provider/writeback boundaries are honest. Do not activate providers, install third-party tools, deploy, write external systems, or store raw private material. Record findings as FACT, INTERPRETATION, HYPOTHESIS, and GAP, then approve or list required fixes.
```

## Evidence

FACT: The UI contains separate tabs and deep links for `#service` and `#schema`.

FACT: Node config now uses dropdown controls instead of raw JSON editing.

FACT: The node panel records both operational fields and product/business fields.

FACT: Third-party memory/design/safety tools were reviewed as references only and not installed.

FACT: Subagents reviewed implementation, UX, and public-safety/runtime boundaries. Their findings were integrated into the dashboard code, generator, and run notes.

INTERPRETATION: The current shape is ready for reviewer inspection and interactive browser QA.

GAP: Interactive browser click-through of the large node control modal is still needed before merge/deploy if visual acceptance is required.

FACT: The parallel architecture reviewer approved this pass on 2026-07-01 and no further dashboard design help is needed for this pass.

## Validation

- Pass: dashboard JavaScript syntax.
- Pass: schema static smoke over both graph defaults.
- Pass: dashboard data regeneration and JSON parse.
- Pass: public safety scan.
- Pass: workflow validation.
- Pass: pre-push runtime guard.
- Pass: diff whitespace check.

## Safety Boundary

Keep this branch public-safe. Do not add secrets, private URLs, account IDs, local absolute paths, raw transcripts, screenshots of private systems, or personal identifiers to public artifacts.

Confidence: medium-high.
