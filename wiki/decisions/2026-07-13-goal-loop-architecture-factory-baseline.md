# Decision - Goal, Loop, And Architecture Factory Baseline

Date: 2026-07-13

Status: accepted design baseline

## Decision

Add Goal Engineering above LangGraph and Loop Engineering, keep LangGraph as the state owner, keep Loop Engineering as a bounded repair mechanism, and use a single-writer Terra integrator with read-only Luna workers for parallel architecture work.

## Context

The existing stack had strong loop, retrieval, role, and memory boundaries but no explicit goal lifecycle, done-condition verifier, or kill-switch schema. The market package also shows that ArchFlow's durable value is maintained knowledge and execution continuity rather than first-draft PRD generation.

## Consequences

- New substantial tasks default to G1 goal contracts and L1 loops.
- Architecture templates must emit goal, dependency, role/skill, retrieval, state, verification, safety, memory, and benchmark contracts.
- External tools stay behind adopt/trial/defer/reject gates.
- WikiLLM remains canonical; Obsidian, Graphify, Nexus, Cognee, vector stores, Notion, and dashboard surfaces cannot become competing sources of truth.
- The architecture is final as a design baseline, but runtime proof remains explicit per capability.

## Alternatives rejected

- Treating prompt text or a task-board status as a sufficient goal state.
- Allowing CrewAI, a loop runner, and LangGraph to compete for workflow control.
- Installing every Google, NVIDIA, Obsidian, graph, or media tool before a measured need exists.
- Using unbounded background agents or permission-bypass hooks for memory maintenance.
