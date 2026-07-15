# ArchFlow Architecture and Setup Test Results

Date: 2026-07-15

Status: current validation record for the public architecture and dashboard manual update

## Result summary

FACT: The current public setup passes the bounded static/browser-local validation suite after the `#manual` route and smoke-test contract were reconciled.

FACT: The final rendered smoke passed all ten current dashboard routes and the Jarvis report/download static contract with `provider_calls=0` and `writeback=0`.

INTERPRETATION: The architecture is operationally efficient for deterministic setup, explanation, review, and handoff checks. This does not establish provider-backed model efficiency, continuous runtime availability, or commercial effectiveness.

## Current checks

| Check | Command / environment | Result | Meaning |
|---|---|---|---|
| Public safety | `python3 scripts/public_safety_scan.py` | PASS | No public-safety violation detected in the current public corpus. |
| Dashboard JavaScript | `node --check project/dashboard/app.js` | PASS | Current manual route and dashboard code parse. |
| Dashboard data | Python JSON parse of `project/dashboard/data.json` | PASS; 1,102,997 bytes | Generated public data is structurally readable. |
| Workflow contracts | `project/local/venv/bin/python project/scripts/validate-workflows.py` | PASS | LangGraph, LlamaIndex, CrewAI, knowledge integration, market research, and model-routing contracts validate. |
| Jarvis API contract | `project/local/venv/bin/python project/scripts/jarvis-api-contract-smoke.py` | PASS | `endpoints=18 owner_guard_cases=5 replay_blocked=1 cors_403=1 provider_calls=0 writeback=0`. |
| Serverless owner guard | `project/local/venv/bin/python project/scripts/jarvis-serverless-owner-guard-smoke.py` | PASS | Owner, acknowledgement, allowlist, durable-control, and replay gates hold; provider calls remain zero. |
| Runtime guard | `python3 project/scripts/pre-push-runtime-guard.py` | PASS | `runtime_guard=ok`, LangGraph smoke verified, LlamaIndex corpus verified, CrewAI config verified. |
| Dashboard and Jarvis render smoke | `project/local/venv/bin/python project/scripts/dashboard-static-smoke.py --timeout 20 --retries 2`, permitted headless Chrome | PASS | `routes=10 jarvis_static=ok provider_calls=0 writeback=0`. Includes `#manual`, the report/download flow, explicit catalog load, Guest guard source contract, and removed-plan assertion. |
| Diff hygiene | `git diff --check` | PASS | Final text-integrity check passed before commit. |

## Environment-specific failures recorded honestly

The same checks were attempted with the system Python and the current sandbox:

- System Python workflow validation could not import `yaml`; the project virtual environment passed the same check.
- System Python Jarvis API smoke could not import `fastapi`; the project virtual environment passed the same check.
- Sandbox headless browser/server startup returned `Operation not permitted`; the permitted headless Chrome run then passed the ten-route smoke.

These are environment/dependency observations, not architecture failures. The project virtual environment is the documented execution path for the Python-backed checks.

## Historical supporting evidence

- [`project/runs/2026-07-13-icp-product-surface/qa-report.md`](../runs/2026-07-13-icp-product-surface/qa-report.md) records prior desktop/mobile QA, 18-endpoint Jarvis contract proof, owner-guard proof, retrieval checks, and the earlier eight-route dashboard surface.
- [`project/runs/20260715-public-product-operations-console/agent-handout.md`](../runs/20260715-public-product-operations-console/agent-handout.md) records the public console release checks and the ten-route result before the operating-manual route reconciliation.
- [`project/runs/yushchenko-model-efficiency/2026-07-02-1402-model-efficiency-report.md`](../runs/yushchenko-model-efficiency/2026-07-02-1402-model-efficiency-report.md) records the local deterministic ledger evidence and the absence of OpenRouter runtime evidence.
- [`project/agents/model-efficiency-issues.md`](../agents/model-efficiency-issues.md) records the open canonical-ledger, provider-runtime, pricing-drift, and telemetry gaps.

## Efficiency evidence

Proved:

- one bounded local test suite validates multiple architecture layers without provider spend;
- the local deterministic proof ledger records measured token fields and zero provider cost for its own fixture;
- owner and replay gates fail closed rather than silently activating external execution;
- the dashboard render test covers ten routes plus the Jarvis local report/download and no-auto-catalog contract, and explicitly asserts zero provider calls and zero writeback;
- the current route/test mismatch was detected and repaired before the final render pass.

Not proved:

- OpenRouter or other provider token efficiency;
- comparative model quality, latency, or cost;
- persistent runtime throughput, uptime, or queue performance;
- efficiency of live parallel agents, because no live agent execution was activated in this public run.

## Release verdict

Verdict: **PASS for the public static/browser-local architecture and documentation scope.**

This verdict does not authorize provider activation, deployment, external writeback, production promotion, private-corpus ingestion, or a claim of paid/customer/ROI validation.
