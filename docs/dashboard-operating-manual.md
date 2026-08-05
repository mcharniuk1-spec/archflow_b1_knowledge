# Crew Desk Operating Manual

Status: current public dashboard
Last verified: 2026-08-05

The Crew Desk is ArchFlow's non-technical, browser-local operating surface. It prepares cases and review packets from the public contracts. It does not run an agent, contact a provider, change a file, checkpoint a live graph, or perform an external action.

## Start locally

```bash
python3 project/scripts/generate-dashboard-data.py
python3 -m http.server 4173
```

Open `http://127.0.0.1:4173/project/dashboard/#today`.

Opening `index.html` directly may block contract loading because browsers restrict local file fetches.

## Today

Today shows:

- current mission;
- employee/actor role;
- evidence boundary;
- independent reviewer;
- next safe action;
- six-phase progress;
- role/workflow/layer counts;
- the first-30-minute onboarding path.

Ask Taras is deterministic local guidance. It maps task language to a workflow pack and returns the questions required before work. It does not synthesize project truth or call a model.

## Work

Create one mission with:

- goal and decision;
- employee/actor role;
- expected output;
- allowed evidence boundary;
- workflow pack;
- risk;
- independent reviewer;
- stop condition.

Save stores the draft in this browser. Export creates a JSON review packet. Neither advances a live graph.

The selected workflow pack materializes and displays every role's goal, required inputs, one owned output, skill/tool ceilings, permission mode, reviewer route, handoff, and readiness gaps. Base-pack roles are distinguished from roles added to close the review chain. An approved runtime may adjust the crew only by rematerializing the same schema; it must keep one owner per output and a different reviewer.

## Knowledge

Knowledge explains:

- all seven layers;
- exact framework jobs and authority boundaries;
- the 12,000-token context budget;
- four labeled architecture views;
- research and delivery methods;
- Skill Spectre and the Video Spectre inspection pattern.

Tool parameter truth:

- LlamaIndex chunk `800`, overlap `120`, lexical/vector/rerank `5/5/5`, final sources `8`;
- source paths and exact read required;
- lexical fallback required;
- TurboVec is optional `4-bit`, not default;
- CrewAI sequential, memory off, cache on, planning off, parallel maximum `3`;
- LangGraph public checkpointer `none`, `thread_id = case_id`.

## Team

Search all twenty-one call names, titles, role IDs, goals, required inputs, owned outputs, skills, tool ceilings, permission modes, reviewer routes, handoffs, and forbidden actions. Filter by any of the ten workflow packs; filtering includes review-closure roles.

The call name is for communication. The role ID is the durable machine contract. Neither grants authority beyond the case.

## Review

The trace follows:

`request → source boundary → requirements → role work → action validation → independent review → receipt → knowledge`

Fail-closed gates cover:

- source boundary and exact read;
- approved requirement coverage;
- maker/reviewer separation;
- target-specific approval interrupt;
- idempotent action ID;
- exact readback.

The browser-local receipt notebook is an example UX only. Durable receipts belong to the controller/checkpointer and run record.

## Set up

Set up creates a local proposal for:

- same-origin or HTTP-loopback bridge;
- allowed/excluded corpus;
- LlamaIndex chunk/ranking parameters;
- optional TurboVec candidate request;
- requested LangGraph checkpointer mode.

The public effective state stays provider-disabled, writeback-disabled, and checkpointer-none.

Allowed bridge examples:

```text
http://127.0.0.1:8787
http://localhost:8787
```

Arbitrary remote origins are rejected. Never enter a credential, token, private URL, account ID, or raw private path.

## Local storage

The following browser-local values may exist:

- mission draft;
- setup proposal;
- Taras question draft;
- example receipts.

Use the reset/clear controls or browser site-data settings to remove them. Do not use the dashboard for sensitive data.

## Compatibility

- `/dashboard` redirects to `/project/dashboard/`.
- `/jarvis` redirects to `/project/dashboard/#today`.
- Old hash routes map to the closest current view but are not shown in navigation.

## Verification

```bash
python3 project/system/validate_system.py
python3 project/scripts/generate-dashboard-data.py
node --check project/dashboard/app.js
python3 project/scripts/dashboard-static-smoke.py --skip-browser
python3 project/scripts/dashboard-static-smoke.py
```

The full smoke renders Today, Work, Knowledge, Team, Review, and Set up in headless Chrome. It also validates role names, counts, diagrams, redirects, origin restrictions, and absence of the old architecture selector.

## Troubleshooting

| Symptom | Meaning | Safe response |
|---|---|---|
| Contracts unavailable | Static files were not served or a JSON path failed | Start the local server from repository root |
| Bridge URL rejected | It is not same-origin or HTTP loopback | Use `127.0.0.1`/`localhost`; do not weaken the check |
| TurboVec says requested but gated | Browser selection is not runtime promotion | Run the representative benchmark and independent review |
| SQLite/PostgreSQL selected but effective state is none | Selection is a proposal | Prove migration/recovery in the target environment |
| Packet downloaded but no work happened | Correct public behavior | Hand it to an approved operator/controller |
| `/jarvis` opens Today | Correct compatibility behavior | Use embedded Taras guidance |
