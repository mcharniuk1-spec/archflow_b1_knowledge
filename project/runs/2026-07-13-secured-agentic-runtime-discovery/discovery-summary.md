# Secured Agentic Runtime Integration Discovery

Date: 2026-07-13
Status: discovery complete; implementation approval pending

## Goal

Define the next ArchFlow operating architecture without weakening the public repository boundary or confusing documented contracts with active runtime proof.

## FACT

- The public repository is the only Git-backed ArchFlow root. The containing private workspace is not a Git repository.
- The public repository has active unrelated changes and agent-owned work. This discovery did not edit those shared areas.
- A July 13 architecture-resetup package already establishes Goal Engineering, bounded Loop Engineering, LangGraph state ownership, Terra/Luna coordination, tool-adoption gates, and a benchmark contract as a design baseline.
- The project-local runtime currently imports LangGraph `1.2.6`, LlamaIndex `0.14.23`, CrewAI `1.15.0`, and LangSmith `0.9.2`.
- TurboVec and Cognee are not installed in the project-local runtime.
- The saved 20-query retrieval benchmark reports 20/20 lexical and hybrid-path hits with source-path filtering, but vector search was unavailable. The hybrid path fell back to lexical retrieval.
- A local Jarvis API health endpoint is reachable with `model_provider=none`, provider calls disabled, external writeback disabled, and CrewAI marked proof-passed but not the default runtime.
- Current LangGraph proof is bounded smoke/fixture execution. Continuous state monitoring, durable checkpoints, autonomous Codex dispatch, and an always-on LangGraph controller are not proven.
- The current public corpus policy explicitly excludes private, raw, secret, temporary, and local-runtime folders.
- The current TurboVec release is pre-1.0 alpha software. Its LlamaIndex adapter supports local persistence, stable external IDs, metadata filtering, and async methods, but it must be trialed and benchmarked before default use.

## INTERPRETATION

The reliable architecture is a two-domain system with one-way reviewed promotion:

1. A standalone public domain containing public-safe rules, workflows, code, fixtures, reports, and WikiLLM memory.
2. A private ArchFlow domain outside the public Git repository containing private sources, raw traces when approved, private indexes, durable runtime state, and exact instruction snapshots.
3. A promotion gate that can derive sanitized public summaries from reviewed private artifacts but never makes the public runtime depend on the private domain.

LangGraph should own task and approval state. LlamaIndex should remain the retrieval abstraction. TurboVec should be a version-pinned vector-store candidate under LlamaIndex, not a second memory system. WikiLLM should remain the reviewed knowledge layer for each visibility domain. Graphify remains generated structure, and Nexus remains an optional live bridge whose runtime must be proved separately.

Prompt text alone cannot make the system continuously active. Reliable enforcement requires project routing files, a routing-only hook, executable preflight checks, a durable LangGraph checkpointer, a heartbeat/health contract, and a separately authorized local service or scheduler.

## HYPOTHESIS

- A model-disabled local LangGraph controller using durable SQLite checkpoints can provide safe continuous state and recovery monitoring without provider calls or external writeback.
- A private TurboVec/LlamaIndex trial using stable document, chunk, and visibility metadata can reduce index size or latency without reducing the existing 20-query retrieval result.
- Single-writer integration with bounded read-only parallel workers will reduce contradictions while preserving review independence.

These hypotheses require paired benchmarks and must not be promoted as facts before measurement.

## GAP

- The owner has not yet approved the physical private-domain location.
- Persistent background execution would require authorization for a local service definition outside the public repository and an explicit stop/uninstall path.
- The strategic-system parallel-agent protocol requires coordination records outside this repository; those writes are not yet approved in this run.
- Installing TurboVec requires a network package install, version pin, dependency review, rollback, sanitized fixture, and independent review.
- No current mechanism can make the Codex desktop app itself an always-on worker. A local LangGraph service can monitor and queue work, but Codex execution still occurs through an active approved Codex session unless a separate provider-backed bridge is approved.

## Security decision

Recommended boundary: keep the public repository as a complete standalone product and create a sibling private ArchFlow layer outside it. Do not place raw private material under the public repository, even in an ignored folder. Use generated, sanitized, source-labeled promotion packets when selected private knowledge must inform the public project.

No instruction replacement, package install, persistent service, private-data movement, external writeback, deploy, push, or provider call occurred in this discovery.
