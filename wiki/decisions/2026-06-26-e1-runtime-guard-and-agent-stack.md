# Decision - E1 Runtime Guard And Agent Stack

Date: 2026-06-26
Status: accepted

## Context

E1.1 needs to be repeatable before E1.2 starts. The project now uses LangGraph, LlamaIndex, CrewAI, LangSmith, WikiLLM, and a local dashboard, but these layers must not blur responsibilities or leak private inputs.

## Decision

Use LangGraph as the workflow spine, LlamaIndex as approved-corpus retrieval, CrewAI as the role/task layer, LangSmith as sanitized trace observability, and WikiLLM as durable public memory.

The Git pre-push hook must run both:

- `scripts/public_safety_scan.py`
- `project/scripts/pre-push-runtime-guard.py`

The hook validates the current setup but does not install packages, run broad indexing, write to private workspaces, deploy, or publish customer-facing claims.

## Rationale

- LangGraph controls state, routing, revision loops, review gates, and approve/revise/block logic.
- CrewAI clarifies who does what, but should not own the workflow path.
- LlamaIndex helps agents find relevant public project text, but WikiLLM remains the durable memory source.
- LangSmith traces sanitized workflow runs, not raw private material.
- A pre-push guard makes breakage visible before publication.

## Consequences

- E1.2 can start from a verified runtime spine.
- Full CrewAI LLM execution is still a later proof, wrapped by LangGraph.
- Vector retrieval and broader web research remain later steps.
- The local dashboard can display readiness, but it remains a control panel, not the primary brain.
