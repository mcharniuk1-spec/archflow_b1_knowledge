# Dashboard Operating Manual - Agent Handout

Date: 2026-07-15

Status: completed for the current public/static documentation and validation scope

## Outcome

The current public dashboard now has a working `#manual` route and current documentation explaining:

- Knowledge Service and Agent Control usage;
- browser-local Administrator/Guest preview labels and their limits;
- a local Knowledge Service report followed by an Agent Control handoff, shared by report ID across dashboard and Jarvis;
- Jarvis field-by-field instructions, local Markdown/JSON downloads, explicit model-catalog loading, and a no-report-body API boundary;
- the parallel-chat communication contract;
- file claims, reviewers, evidence labels, stop rules, and merge handoff;
- current architecture, test evidence, production boundaries, and next gates.

## Files changed in this lane

- `project/dashboard/app.js`
- `project/scripts/dashboard-static-smoke.py`
- `project/dashboard/README.md`
- `docs/dashboard-operating-manual.md`
- `project/reports/20260715-public-product-operations-architecture-report.md`
- `project/reports/20260715-architecture-test-results.md`
- `project/reports/20260715-current-state-and-execution-plan.md`
- `project/strategic-plan-2026-07-13.md`
- `project/dashboard/data.json`
- `project/database/skill-catalog.json`
- `project/database/role-catalog.json`
- `project/reports/20260715-dashboard-operating-manual-review.md`
- `project/live/communication/agent-communication-log.md`
- `skills/archflow-knowledge-service/`
- `skills/archflow-agent-control/`

Existing unrelated environment-example changes and other active run artifacts were preserved.

## Evidence

- `node --check project/dashboard/app.js`: pass.
- `python3 scripts/public_safety_scan.py`: pass.
- Dashboard JSON parse: pass after regeneration.
- `project/local/venv/bin/python project/scripts/validate-workflows.py`: pass.
- `project/local/venv/bin/python project/scripts/jarvis-api-contract-smoke.py`: pass; 18 endpoint cases, five owner-guard cases, replay blocked, provider calls zero, writeback zero.
- `project/local/venv/bin/python project/scripts/jarvis-serverless-owner-guard-smoke.py`: pass.
- `python3 project/scripts/pre-push-runtime-guard.py`: pass.
- `project/local/venv/bin/python project/scripts/dashboard-static-smoke.py --timeout 20 --retries 2`: pass; ten routes, provider calls zero, writeback zero.
- The same smoke now renders the Jarvis report/download source contract and confirms no automatic public-catalog load; it exits successfully with `jarvis_static=ok`.

## Boundaries

The result proves the public static/browser-local architecture and guarded contracts. It does not prove live provider execution, provider token/cost efficiency, continuous hosted freshness, real subagent launch, private-corpus ingestion, durable multi-user memory, production database behavior, or external writeback.

## Next safe action

The current request authorizes Git commit and push. Before publishing, rerun final generated-data, public-safety, smoke, and diff checks; stage every approved public file while preserving inherited environment-example edits.
