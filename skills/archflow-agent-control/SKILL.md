---
name: archflow-agent-control
description: Design a bounded ArchFlow agent-control handoff from an approved knowledge report. Use when a project needs a role map, task graph, skills and tool allowlists, shared context, reviewer separation, approval gates, stop conditions, and proposed file architecture without launching agents, editing a repository, enabling providers, or writing externally.
---

# ArchFlow Agent Control

Turn a reviewed knowledge report into an inspectable work contract. This skill designs control; it does not create a live autonomous workforce.

## Required input

Use a reviewed Knowledge Service report, then collect:

- Goal, expected artifact, and acceptance criteria.
- Allowed roles, skills, tools, and source boundary.
- Parallel lanes and sole-writer ownership for each shared artifact.
- Independent reviewer, approval gates, budget/stop conditions, and rollback requirement.

If no report is available, stop in guest mode. An administrator may reference an existing reviewed report, but must identify it explicitly.

## Workflow

1. Verify the report ID, source boundary, FACT / INTERPRETATION / HYPOTHESIS / GAP classification, and approval state.
2. Select the smallest role set from `project/agents/agent-roster.yaml`; distinguish packaged public skills from method checklists.
3. Define a LangGraph-style route: intake, classify, contract, bounded work, independent review, approval, handoff.
4. Give each role one purpose, allowed inputs, tool/skill allowlist, output schema, forbidden actions, and stop rule.
5. Produce a review packet and proposed file list marked `created: false` and `requires_operator_review: true`.

## Shared-context rule

Reuse the knowledge report by stable report ID. Do not copy raw source material into the agent packet. Preserve the original source boundary and record any new GAP or changed assumption.

## Runtime boundary

LangGraph is the routing/state contract; CrewAI role declarations are work-contract examples; LlamaIndex is bounded retrieval; WikiLLM is durable reviewed memory. None of those configuration files proves an active agent, provider call, database write, deployment, or external action.

## Forbidden actions

- Launch an agent or claim a role is always running.
- Let an executor approve its own high-risk output.
- Give parallel agents overlapping write ownership.
- Activate a provider, Git push, deployment, database mutation, Notion/Nexus write, or other external action without explicit approval and current capability proof.
