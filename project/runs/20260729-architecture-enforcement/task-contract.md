# Task Contract: Architecture Enforcement And Readiness Repair

Status: superseded — closed by architecture consolidation
Date: 2026-07-29
Authority: owner-authorized local repair and architecture enforcement only

## Objective

Repair the two reviewed fail-open readiness defects and make the existing ArchFlow architecture mandatory at run admission. Every run must declare its state path, adaptive role pack, knowledge boundary, evidence level, stop rule, and approval gates before Codex acts on it.

## Mandatory Architecture

- LangGraph: deterministic admission/state routing and bounded approval transitions.
- CrewAI: adaptive role/task plan derived from the run profile; no default provider-backed execution.
- LlamaIndex: allowlisted retrieval with source paths and lexical fallback.
- TurboVec: isolated candidate backend only; it cannot become default until dependency, filter, persistence, and paired benchmark gates pass.
- WikiLLM: reviewed durable memory, never an unreviewed runtime write target.
- Codex: local executor and final integrator under the admitted task contract.

This historical task is closed by supersession. Closure means its requirements were migrated into the canonical Knowledge Case, role catalog, run profiles, and E1–E8 matrix; it does not claim provider runtime or production readiness.

## Canonical Role Lanes At Closure

| Lane | Canonical role | Exclusive scope |
| --- | --- | --- |
| A | Mykola / `verifier` | deterministic readiness checks and exact readback; no repair |
| B | Bohdan / `admission_controller` | profile, admission envelope, minimum roles, and stop rules; no project edits |
| C | Solomiia / `source_and_context_operator` | bounded LlamaIndex retrieval and optional TurboVec trial evidence; no promotion |
| D | Halyna / `independent_reviewer` | read-only correctness, safety, claim, and regression verdict |
| Integration | Maksym / `integrator` | merge order, shared surfaces, receipts, and owner handoff; no self-approval |

## Acceptance Criteria

1. `provider_mode` fails closed unless explicitly `disabled` for the provider-disabled profile.
2. Monitor-only and executor-local-deterministic policy are separately enforced and documented.
3. Status output exposes only an allowlisted public-safe schema.
4. Run admission produces a deterministic LangGraph state record and role plan for each declared run type.
5. The E1-E8 matrix covers required states, role combinations, retrieval modes, review gates, and external-action boundaries.
6. CrewAI roles are adapted by profile rather than treated as fixed authority or a default autonomous runtime.
7. TurboVec has an honest adopted/trial/deferred status backed by isolated evidence, not a configuration claim.
8. An independent reviewer approves the repair and labels any remaining gap.

## Forbidden Actions

- Provider/local-model calls, tracing submission, network or external writeback.
- Persistent-service start, stop, reload, install, or reconciliation.
- Queue/checkpoint/task-payload mutation.
- Deployment, publication, account access, Git push, or production promotion.
- Private source ingestion or public/private boundary weakening.

## TurboVec Gate

The owner requested TurboVec integration. The implementation may use a pinned, isolated private environment only after the existing dependency is checked. Promotion requires stable IDs, allowlist filters, persistence/rebuild proof, lexical comparison, paired benchmark, and independent review. A missing package or failed gate is `defer`, not a silent fallback or false integration claim.

## Done Definition

The local system can prove its admission and readiness policy before a run starts. It remains provider-disabled and action-gated until separate approvals are recorded.

The active replacement is `project/architecture/e1-e8-role-state-matrix.md`; this file is not a required CAG reference for new admissions.
