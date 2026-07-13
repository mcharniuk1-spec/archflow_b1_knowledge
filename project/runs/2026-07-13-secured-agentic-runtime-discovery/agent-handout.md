# Agent Handout - Secured Agentic Runtime Integration

## Purpose

This handout preserves the discovery and approval boundary for the next ArchFlow operator. It covers private/public knowledge separation, instruction history, LangGraph persistence, LlamaIndex retrieval, TurboVec evaluation, and bounded parallel execution.

## Human summary

The current system is more mature than a blank setup: LangGraph, LlamaIndex, CrewAI, and LangSmith are installed in the project-local runtime; public WikiLLM, CAG/RAG rules, Goal and Loop contracts, and a public-safe live communication system exist. A local provider-disabled Jarvis API is also healthy.

The missing layer is operational proof for the owner's new request. TurboVec and Cognee are not installed, vector retrieval is not active, LangGraph has no proven durable always-on controller, and Codex cannot become an always-on worker from prompt text alone. The existing July 13 architecture package correctly labels those capabilities as trial, planned, or blocked.

The recommended design keeps the Git-backed public repository fully standalone and places private sources, private indexes, raw traces when approved, exact instruction history, and durable runtime state in a sibling private ArchFlow layer. A reviewed one-way promotion gate may derive sanitized public summaries without creating a private runtime dependency.

No implementation was performed because the next steps require explicit owner choices about private storage, persistent background execution, external coordination records, and network package installation.

## Current state

- Status: discovery complete; approval pending.
- Public repository: active unrelated changes and recent lane handoffs must be preserved.
- LangGraph: installed and fixture-proven narrowly; continuous controller unproven.
- LlamaIndex: installed; bounded lexical retrieval proven.
- TurboVec: not installed; pre-1.0 benchmark candidate.
- Provider calls and external writeback: disabled.
- Parallel subagents: not dispatched because their required coordination writes and implementation scopes are not yet approved.

## Agent continuation prompt

Continue the secured ArchFlow agentic runtime integration after the owner answers the approval question. Read the public operating rules, live communication notice and latest log, the July 13 architecture baseline, and this run folder. Recheck Git status and active file claims. Register every parallel lane before editing. Preserve unrelated changes. First create and hash the private instruction-history snapshot; then implement the private/public boundary; then run model-disabled LangGraph persistence fixtures; then install and benchmark a pinned TurboVec LlamaIndex adapter only if explicitly approved. Keep the public repository standalone. Do not call providers, deploy, push, write externally, or move raw private data into the public repository. Require an independent safety reviewer before promoting any new default.

## Execution trace

1. Loaded ArchFlow, public project, WikiLLM, global-vault, RAG, decision-wall, resetup, and LangGraph strategic-system contracts.
2. Reviewed live public claims and avoided active shared-file scopes.
3. Queried the current Graphify structure.
4. Verified project-local package availability and the saved retrieval benchmark.
5. Verified the local Jarvis health state with providers and writeback disabled.
6. Reviewed current official LangGraph, LlamaIndex, and TurboVec integration/security surfaces.
7. Produced the discovery summary, task contracts, implementation plan, and this handout.

## Decisions

- Recommended, not yet approved: sibling private ArchFlow domain outside the public repository.
- Accepted from the existing baseline: LangGraph is the only state owner; CrewAI remains subordinate; LlamaIndex is retrieval; WikiLLM is reviewed memory; TurboVec is a trial under LlamaIndex.
- Deferred: persistent background monitor, TurboVec installation, coordination writes outside the repository, and instruction replacement.

## Artifacts

- `discovery-summary.md` - verified current state and recommended security boundary.
- `task-contracts.md` - bounded parallel lanes, authority, forbidden actions, and merge order.
- `implementation-plan.md` - phased implementation and proof gates.
- `agent-handout.md` - human summary and copy-ready continuation prompt.

## Validation

- Read-only runtime/package inspection: complete.
- Local Jarvis health check: pass with providers and writeback disabled.
- Existing retrieval benchmark inspection: pass for lexical fallback; vector gate remains blocked.
- Scoped public safety scan and diff checks: required after this packet is written.
- Implementation/runtime tests: intentionally not run before owner approval.

## Next actions

1. Obtain owner approval for the four gated choices.
2. Register the integrator and read-only worker lanes.
3. Snapshot and hash the previous instruction system.
4. Build the private/public boundary and model-disabled LangGraph fixture.
5. Run the pinned TurboVec trial only after the dependency gate passes.

## Safety boundary

Do not place raw private sources, credentials, private URLs, local paths, account identifiers, raw recordings, raw transcripts, or private runtime state in the public repository. Do not interpret a configured prompt, workflow YAML, health endpoint, or package import as continuous runtime proof.
