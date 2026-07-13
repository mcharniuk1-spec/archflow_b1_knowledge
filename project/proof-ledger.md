# ArchFlow Proof Ledger Router

Status: active routing index. This file points to current evidence; it does not replace source artifacts.

## Evidence states

- Proven: current artifact and reproducible check support the narrow claim.
- Review: artifact exists but acceptance or independent review remains open.
- Planned: design or task exists without execution proof.
- Blocked: a named gap prevents safe progress.
- Superseded: retained for lineage but not active truth.

## Canonical evidence order

1. Current operating and safety rules.
2. `project/strategic-plan-2026-07-13.md` for the active epic and milestone structure.
3. `project/project-plan.md` for historical E1-E7 proof and status detail.
4. The relevant `project/runs/` source artifact and its checks.
5. `wiki/decisions/`, `wiki/issues/`, and `wiki/runs/` for durable reviewed state.
6. `wiki/memory.md` and `wiki/insights.md` only for promoted reusable conclusions.
7. The external task board as an execution mirror, not as proof by itself.

When two surfaces disagree, prefer the newest reviewed source artifact with a reproducible check, record the conflict, and update the routing/summary layer without deleting history.

## Current narrow proofs

| Capability | Evidence state | Proof boundary |
|---|---|---|
| Public-safe WikiLLM and operating rules | Proven | Repository files and safety scan; no private-vault claim. |
| LangGraph provider-disabled fixtures | Proven narrowly | Existing saved fixtures; not provider-backed or continuously available. |
| LlamaIndex approved-corpus lexical retrieval | Proven narrowly | Source-path retrieval/readback; vector-default performance unproven. |
| CrewAI configuration/import | Proven narrowly | Configuration and import only; direct provider-backed team execution unproven. |
| Loop Engineering | Proven at L1 | State, caps, maker/checker, stop rules, run log, and handout. |
| Goal Engineering | Planned at G1 | Contract exists; provider-disabled architecture-factory fixture pending. |
| Obsidian/Graphify/Nexus | Mixed | File/config and one-vault live proof exist; all-vault tool-call proof does not. |
| Cognee, TurboVec, destructive command hook | Planned or blocked | Adoption and benchmark gates not passed. |
| Buyer and payment validation | Blocked | Primary buyer and paid-intent evidence absent. |

## Runtime wording

- `provider-disabled`: zero network/cloud model calls; deterministic tools are allowed. A local model requires an explicit `local-model-enabled` contract.
- `model-disabled`: zero network/cloud and local model calls.
- `provider-backed`: requires current model route, key isolation, budget, trace, privacy, review, and rollback proof.
