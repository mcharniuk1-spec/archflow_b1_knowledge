# Jarvis and Dashboard Documentation Release - Agent Handout

Date: 2026-07-15

Status: validation complete; Git publication and hosted verification pending in this handout revision

## Purpose

This release turns the public Jarvis and dashboard surfaces into a clearer developer-facing operating guide without changing their local-first safety boundary. It also adds a concise documentation path to the public landing page. It is intended for an operator or future reviewer who needs to understand the exact relationship between Knowledge Service, Agent Control, browser-local reports, and real repository work.

## Human summary

Jarvis now starts with one explicit four-stage sequence: define a request, prepare a Knowledge Service report, design Agent Control from that report, and hand a reviewed package to an authorized human operator. The guide explains each input, the downloadable outputs, Administrator and Guest preview limits, optional guarded controls, and the distinction between a prepared local package and any executed action. Advanced access and model-route material is consolidated into one reference area so it cannot compete with the core workflow.

The dashboard manual now reads as continuous documentation instead of a collection of status cards. It describes the repository, architecture, retrieval and memory layers, configuration points, skills, role contracts, data preview, workflow editor, execution-state animation, downloads, and frequently asked questions. The landing page retains its existing message and visual design while directing evaluators to the documentation path.

## Current state

- Knowledge Service is the prerequisite for Agent Control in both Administrator and Guest preview.
- The shared browser-local session stores preview mode and report/handoff references only. It is not authentication, multi-user memory, a database record, or a runtime event feed.
- Reports and handoffs remain downloadable proposals. They do not fetch a repository, launch a sub-agent, create proposed files, use a provider, push Git, deploy, or write externally.

## Decision

Agent Control now requires `sharedSession.knowledge.status === prepared_local` for every local preview mode. This removes the previous Dashboard/Jarvis inconsistency and keeps the product’s two-stage method explicit.

## Files changed

- `index.html`
- `jarvis.html`
- `jarvis.js`
- `jarvis.css`
- `docs/dashboard-operating-manual.md`
- `docs/operations.md`
- `project/dashboard/index.html`
- `project/dashboard/app.js`
- `project/dashboard/styles.css`
- `project/dashboard/README.md`
- `project/dashboard/data.json`
- `project/database/skill-catalog.json`
- `project/scripts/dashboard-static-smoke.py`
- `project/live/communication/agent-communication-log.md`

## Validation

- JavaScript syntax checks for Jarvis and Dashboard: passed.
- Python compile check for the static smoke: passed.
- Public safety scan: passed.
- Workflow validation: passed.
- Runtime guard: passed.
- Guarded Jarvis API and serverless owner-guard smoke: passed with provider calls and writeback at zero.
- Rendered static smoke: passed for ten dashboard routes and Jarvis.
- Local desktop visual checks: passed for Jarvis and Dashboard documentation layouts.

## Continuation prompt

Review the current public documentation release before adding runtime behavior. Read `project/operating-rules.md`, the live communication files, this handout, `docs/dashboard-operating-manual.md`, `jarvis.html`, `jarvis.js`, and `project/dashboard/app.js`. Preserve the two-stage prerequisite: Knowledge Service must prepare a browser-local report before Agent Control. Treat all visual stage states as browser-local unless a verified runtime event feed exists. Do not add provider execution, repository writes, authentication, private retrieval, or external writeback without a separate approved task contract, capability proof, validation, and public-safety review.

## Safety boundary

Keep private source material, credentials, device paths, private links, customer data, raw transcripts, deployment metadata, and unverified runtime claims out of this public repository, browser-local report, and release record.
