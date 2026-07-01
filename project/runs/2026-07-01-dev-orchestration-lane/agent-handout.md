# Agent Handout: Dev Orchestration Lane

Date: 2026-07-01
Owner lane: Lane 2 Dev Orchestration
Status: validation reviewed for redeploy

## Lane Contract

Lane 2 keeps the agent system operable: workflow health, schema control, review gates, dashboard/runtime correctness, and safe tool integration.

AF role ownership:

- `af_tools/dev`: dashboard and workflow artifact checks.
- `af_context/dev`: status synthesis of model routing and deployment boundaries.
- `af_review`: no false backend, provider, Railway, or writeback claims.
- `af_publisher`: runbook, run notes, and completion evidence.

## FACT

- `project/workflows/langgraph-controller.yaml`, `project/workflows/crewai-crew.yaml`, and related workflow files validate with the repo-local workflow validator.
- Runtime guard reports workflow, LangGraph, LlamaIndex corpus, and CrewAI config as verified.
- LangGraph smoke reaches local approved state. External trace upload produced DNS warnings in this environment and should not be treated as runtime/provider proof.
- Exact global Python CrewAI config check fails because `crewai` is not installed in global Python.
- Repo-local venv CrewAI config check passes without LLM execution.
- Chrome dashboard static smoke passed after approved local browser/server permissions: `routes=8 provider_calls=0 writeback=0`.
- No Railway runtime config files were found.

## INTERPRETATION

The static dashboard/workflow lane is structurally healthy enough for local source validation and has browser-smoke proof for the static dashboard.

## HYPOTHESIS

The safest closeout is to treat repo-local Python as canonical for workflow/CrewAI validation and keep provider/backend/writeback work gated until an approved bridge exists.

## GAP

- Decision on whether to install CrewAI into global Python or update docs to require repo-local venv for `crewai-config-check.py`.
- Final reconciliation of older open `starting` or `in progress` entries in the live communication log before merge-ready status.

## Validation Summary

Passed:

- dashboard JS syntax;
- dashboard data generation and JSON parse;
- public safety scan;
- workflow validation;
- runtime guard;
- LangGraph smoke local approval;
- CrewAI config through repo-local venv;
- root JS/JSON checks;
- asset reference check with Vercel rewrite awareness;
- route HEAD checks except plain `/dashboard` under Python simple server.
- Chrome dashboard static smoke after approval;
- fresh desktop/mobile screenshot captures;
- homepage and quiz mobile overflow checks.

Blocked or failed:

- global Python CrewAI import;
- local `/dashboard` rewrite under Python simple server.

## Next Safe Action

Messi should commit, push, redeploy, and update Notion with the final commit. Do not claim OpenRouter execution, Railway runtime, provider-backed Jarvis, or durable writeback until an approved backend/local bridge exists and logs model calls with model ID, prompt version, route, input summary, token estimate, cost bucket, and review decision.
