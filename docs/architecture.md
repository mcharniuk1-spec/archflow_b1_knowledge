# Architecture

ArchFlow is designed as a knowledge-continuity operating system: it preserves the context needed to make decisions, then gives bounded workers a reviewable way to act on that context.

## Product view

**Short term:** a scoped Knowledge Reliability Setup for a real forcing moment—an ownership change, product handoff, enterprise-readiness push, onboarding problem, or key-person departure. The result is a source/owner map, reviewed knowledge spine, governed workflow, and operator handoff.

**Long term:** an installable local-first operating toolkit that can run approved role/task workflows against a bounded corpus with explicit evidence, approval, safety, and recovery controls.

The second is a product direction. This repository does not present it as a hosted autonomous service today.

## Seven grouped layers

1. **Authority and Goal** — identifies the owner, success test, constraints, budget, and forbidden actions.
2. **Context and Knowledge** — assembles an approved context capsule through routing rules, WikiLLM, Graphify, and bounded LlamaIndex retrieval.
3. **Plan and Orchestration** — uses LangGraph contracts for typed routing, checkpoints, review nodes, and stop conditions.
4. **Execution and Roles** — gives CrewAI-style roles and other workers a bounded source/tool/output contract; the role name is not execution authority.
5. **Loop and Verification** — separates the maker from an independent reviewer and stops repair loops within declared limits.
6. **Memory and External Gate** — promotes reviewed knowledge deliberately and keeps Git, deployment, providers, and external writeback behind explicit approval.
7. **Measurement and Optimization** — compares quality, reliability, retrieval, latency, cost, and recovery only on declared fixtures.

## How the layers work together

```text
approved request
  -> authority and task contract
  -> bounded context capsule
  -> LangGraph route and role contracts
  -> candidate artifact
  -> independent review
  -> approved handoff or blocked next action
  -> reviewed memory candidate and measured improvement proposal
```

LlamaIndex is the bounded retrieval layer, not durable memory. WikiLLM is the curated durable-memory layer. Graphify is generated structural reference, not final business truth. Nexus is a live vault bridge only when its runtime and schemas are proved. TurboVec/Cognee remain optional, gated evaluation candidates rather than defaults.

## Public console truth boundary

The dashboard can explain contracts, edit browser-local drafts, preview public catalog data, and download review bundles. It cannot prove a runtime event without a fresh state record containing a run ID, node ID, state, timestamp, evidence reference, authority scope, and writeback state. It cannot create repository files or act on external systems by itself.

See the [operations guide](operations.md) for the stage-by-stage operator flow.
