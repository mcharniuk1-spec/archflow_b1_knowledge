# Public Product Operations Architecture Report

Date: 2026-07-15

Scope: public website, dashboard, Jarvis, role/skill presentation, generated catalog, setup documentation, and operational truth boundaries.

## Executive product position

ArchFlow should be marketed now as a **Knowledge Reliability Setup** for a forcing moment: it turns fragmented product knowledge into a source/owner map, reviewed knowledge spine, governed workflow, and operator handoff. Its long-term direction is a local-first, installable operating toolkit. This is a more credible product path than claiming a hosted autonomous-agent platform before runtime, persistence, and action controls exist.

The public interface therefore prioritizes explainability, controlled handoff, and visible gates. It deliberately distinguishes a configured contract from observed execution.

## Layer-by-layer architecture

| Layer | Product ability | Current public proof | Required next gate |
|---|---|---|---|
| Authority and Goal | Bind request to an owner, scope, stop rule, and approval boundary. | Public goal and workflow contracts. | Task-specific operator acceptance. |
| Context and Knowledge | Build the smallest source-grounded context capsule. | Public WikiLLM, Graphify reference, LlamaIndex contract, lexical fallback description. | Bounded-corpus and retrieval evaluation for any new corpus. |
| Plan and Orchestration | Route work through typed LangGraph nodes, checkpoints, and stop conditions. | Controller contract and bounded fixtures. | Sanitized runtime events for live status. |
| Execution and Roles | Define worker sources, tools, outputs, reviewer, and forbidden actions. | Role registry and ten reviewed public skills. | Approved executor/task contract before file work. |
| Loop and Verification | Separate maker from reviewer and cap repair. | Public loop and review contracts. | Representative independent fixtures. |
| Memory and External Gate | Promote reviewed knowledge and hold actions for approval. | WikiLLM/run contracts and browser-local bundle boundary. | Current target proof plus action-specific approval. |
| Measurement and Optimization | Compare quality, reliability, retrieval, and cost. | Benchmark schema and model-efficiency policies. | A canonical public-safe event/ledger sample. |

## Product surfaces

### Knowledge Service

This is the buyer-facing source-to-output lane. An operator provides an approved source boundary, outcome, artifact contract, and reviewer. The lane creates a reviewable PRD, ICP, decision, research, backlog, or knowledge packet with facts, interpretations, hypotheses, and gaps kept distinct.

### Agent Control

This is the operator-facing control plane. It defines roles, skill visibility, source/tool allowlists, task contracts, parallel boundaries, review gates, and handoff targets. A browser draft is not a launched subagent. Real file creation remains the responsibility of an approved executor operating under a claimed scope and reviewer separation.

### Jarvis

Jarvis is a guarded review-packet interface. Each input now explains what it is, why it is needed, an example, storage boundary, and capability limit. Submitting a request may reach a guarded endpoint if available, but the current default remains fail-closed: no provider use, no fabricated model response, and no durable writeback.

### Dashboard data and export

The Data Lab makes the public catalog inspectable through a deliberately limited SQL-like `SELECT ... FROM ... LIMIT ...` preview. It reads generated public JSON only. Browser-local workflow state can be downloaded as a review bundle with a truth boundary; it is not a patch, repository mutation, commit, or deployment artifact.

## Skills and agent packaging

The repository has ten reviewed project-local skill contracts. They are now generated into a machine-readable catalog with content hashes, portability status, permission boundary, and `verified_invocations: null`. The latter is intentional: no public-safe invocation telemetry exists, and documentation references are not usage metrics.

The local private inventory is not copied into the product. It contains overlapping variants and local-environment assumptions that have not passed redistribution, path, secret, provenance, license, fixture, and reviewer gates. Future skills enter the public catalog only after those gates.

## Runtime and data truth model

The stage animation is an interaction aid for browser-local packet preparation. The console may claim a live workflow stage only after it receives a fresh sanitized event with `run_id`, `workflow_kind`, `node_id`, `state`, `observed_at`, `evidence_ref`, `authority_scope`, and `writeback_state`.

Today the data model has three represented storage layers: generated public JSON, browser-local drafts, and downloaded review bundles. A private runtime store and an authenticated database are not exposed. A future SQLite/DuckDB evidence ledger needs migrations, read-only access, row/time limits, auditing, backup/restore proof, and isolation from private source corpora before it becomes a real feature.

## Documentation and installability

The public docs now provide a clean-clone path using standard Python, product navigation for service buyers/operators/evaluators, architecture and operations guides, API/security boundaries, contribution rules, and security reporting guidance. The prior instructions that depended on an ignored project-local virtual environment have been removed from the main quickstart.

## Verified during this release

- public dashboard data generated and parsed;
- public-safety scan passed;
- workflow contracts validated in the existing local project runtime;
- dashboard and Jarvis JavaScript syntax passed;
- guarded Jarvis API and serverless owner-guard contract checks passed with provider calls and writeback at zero;
- rendered dashboard smoke passed across ten routes with provider calls and writeback at zero.

## Gaps and recommendations

1. Build a sanitized event-feed adapter before representing any stage as live runtime state.
2. Keep the static Data Lab bounded until a local evidence-ledger implementation meets its control requirements.
3. Record public-safe skill invocation events before publishing usage counts.
4. Select a software license before representing the repository as ready for third-party redistribution.
5. Treat Git commit/push, deployment, provider activation, and external writeback as separate owner-approved releases.
