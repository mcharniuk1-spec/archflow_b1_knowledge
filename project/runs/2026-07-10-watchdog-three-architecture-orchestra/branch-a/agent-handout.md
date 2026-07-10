# Branch A Agent Handout - Company Development Agent Architecture

Status: review complete; merge recommendation: `revise`.

## Purpose

This handout records Branch A's documentation/configuration hardening for the company-development agent architecture. It is for the watchdog integrator or a later bounded reviewer. The work reconciles named runtime bindings with role-based authority while preserving every existing public-safety, maker-checker, approval, provider, deployment, and writeback gate.

## Human Summary

Branch A now treats watchdog, executor, verifier, safety-reviewer, integrator, and external-action labels as permission contracts. A compatible runtime may fulfil a bounded role only through that role's task contract, evidence duties, forbidden actions, and independent review requirements. The current Codex and planned Hermes bindings remain documented, but neither runtime identity is treated as permanent authority or as an authorization to activate providers, deploy, or write externally.

The Jarvis/dashboard and Railway wording was made intentionally conservative. The repository documents static/browser-local packets, provider-disabled review contracts, and historical deployment evidence, but this branch does not claim a current hosted endpoint, availability, continuous monitoring, active provider, current model, remaining budget, or always-online service.

OpenRouter policy now requires an activation-time model/capability/pricing review, cost/usage capture, a ledger path, Yushchenko observer review, independent safety review, and owner approval. Railway material is a prerequisite packet only: deployment-time health evidence is explicitly distinct from continuous monitoring and availability evidence.

## Current State

- Role/runtime consistency scan: complete; see `consistency-scan.md`.
- Branch evidence roles: Planner, Executor, Verifier, Safety Reviewer, and Branch Reporter each produced an evidence artifact.
- GAP: Luna model selection was unavailable in the collaboration API; real bounded subagents were used and each recorded `GAP - Luna model selection unavailable`.
- Runtime state: configuration/documentation only. Hosted freshness, provider activation, Railway action, external writeback, commit, and push were not performed.
- Merge recommendation: `revise`, because dependency-backed checks and current runtime/provider evidence are not available in this run.

## Agent Continuation Prompt

Review Branch A under `project/runs/2026-07-10-watchdog-three-architecture-orchestra/branch-a/` and the changed governing/configuration files listed below. Preserve the role-contract interpretation and all current stop gates. Do not treat the documentation update as approval to call a provider, deploy Railway, write externally, commit, or push. Confirm that the integrator keeps Branch A-owned changes separate from inherited worktree changes. If runtime validation is proposed, stop unless the owner has approved a new bounded packet that proves target/service mapping, secret isolation, model selection, cost ledger, health/observability, rollback, and post-action verification.

## Execution Trace

1. Read the branch context capsule, integration plan, task contracts, governing rules, task-handout skill, live communication state, and relevant architecture/configuration contracts.
2. Logged Branch A start and two scope updates in the append-only live communication log.
3. Used real bounded Planner, Executor, Verifier, Safety Reviewer, and Branch Reporter subagents; no model selector was exposed.
4. Refreshed official OpenRouter and Railway documentation for drift-prone activation and healthcheck facts, without calling providers or deployment systems.
5. Added role/runtime, provider/ledger, Railway prerequisite, historical-hosted-status, and governance wording only in the authorized Branch A scope.
6. Ran static validation and public-safety checks; recorded unavailable dependency-backed checks as blockers rather than runtime proof.

## Decisions

- Roles govern authority; current named runtime bindings do not. A runtime fulfilling another bounded role must obey that role's contract and cannot self-approve high-risk output.
- The watchdog remains non-executing regardless of compatible runtime choice.
- OpenRouter remains disabled pending a separate approved activation packet. Yushchenko remains an observer/preflight role, not an approval or execution bypass.
- Railway healthchecks are deployment-time checks only. Any always-online claim requires separately recorded current availability, observability, auth, persistence, recovery, and ownership evidence.
- No new skill or hook was created. The duplicate-skill and hook-governance audit found the nine local skill contracts aligned with the registry.

## Artifacts

- `branch-report.md`: final evidence summary and `revise` recommendation.
- `consistency-scan.md`: required governing/config consistency review with FACT, INTERPRETATION, and GAP.
- `official-source-evidence.md`: current official OpenRouter and Railway reference interpretation.
- `railway-prerequisite-packet.md`: deployment and availability prerequisites without authorization.
- `planner-evidence.md`, `executor-evidence.md`, `verifier-evidence.md`, and `safety-review-evidence.md`: bounded role evidence.

## Validation

- Pass: `git diff --check`.
- Pass: Ruby YAML parse for the changed CAG, roster, LangGraph, and CrewAI files.
- Pass: Python syntax compilation of Jarvis/API modules.
- Pass: Railway JSON parse.
- Pass: JavaScript syntax check of the dashboard script.
- Pass: `python3 scripts/public_safety_scan.py`.
- Blocked: `python3 project/scripts/validate-workflows.py` because the active interpreter lacks the YAML dependency; no installation was authorized.
- Blocked: `python3 project/scripts/jarvis-api-contract-smoke.py` because FastAPI is unavailable in the active interpreter; no suitable approved environment was available.

## Next Actions

1. The watchdog integrator reviews the Branch A report and accepts only the scoped documentation/configuration changes that preserve the `revise` boundary.
2. If runtime proof is needed, request a distinct owner-approved validation task; do not reuse this branch as runtime proof.
3. Before any future OpenRouter action, refresh official model metadata and pricing, select a model, define the hard budget and ledger, and route through independent safety and owner approval.
4. Before any future Railway action or availability claim, prove the exact service, current endpoint, healthcheck, auth/CORS, logging, monitoring, recovery, and post-action state.

## Safety Boundary

Do not copy secrets, key values, private target details, local paths, account/deployment identifiers, raw private material, or dynamic price tables into public artifacts. Do not call providers, deploy, publish, push, mutate Notion/Linear, or write externally without a separately approved, evidence-backed action packet.
