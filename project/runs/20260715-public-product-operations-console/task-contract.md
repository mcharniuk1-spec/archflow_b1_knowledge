# Public product operations console task contract

## Goal

Make the public ArchFlow website, dashboard, Jarvis, documentation, role/skill catalog, and browser-local data model accurately explain and safely demonstrate a knowledge service and bounded agent architecture.

## Observable done condition

The public dashboard shows a stage-by-stage execution model, clear per-input Jarvis help, explicit agent-control and knowledge-service boundaries, browser-local export/download of a review packet, an inspectable public data schema with read-only SQL-like query examples, and a truthful portable skill catalog. Public docs and README explain personal setup without relying on owner data.

## Authority boundary

Public-safe static/browser-local implementation only. No private corpus ingestion, provider execution, live database, autonomous file mutation, Nexus/Notion/GitHub writeback, deployment, or Git push is authorized by this task.

## Evidence states

- Existing dashboard and Jarvis public surfaces: proven static/browser-local.
- LangGraph/controller, role, retrieval, and promotion contracts: review/proven only where cited by public artifacts.
- Live provider, durable database, writeback, and autonomous subagent execution: blocked or planned.

## Task graph

1. UI/interaction audit (read-only) -> integration design.
2. Skills/agents portability audit (read-only) -> public catalog decision.
3. Documentation/product audit (read-only) -> README and operation-doc plan.
4. Integrator implements public-safe dashboard, Jarvis, data/schema, docs, and exports.
5. Independent reviewer checks claims, usability, public safety, and regression evidence.

## Roles and stop rules

- UI reviewer: no edits; assess existing interaction surface and propose the smallest coherent state model.
- Skills reviewer: no edits; inventory portable public skills and identify path/secret risks.
- Product-doc reviewer: no edits; audit product claims and setup documentation.
- Integrator: owns final public implementation.
- Reviewer: validates only after integration; does not repair without a new scoped handoff.

Stop if a public file would require private data, a third-party installation, a provider call, or an external write. Stop and record any mismatch between public UI claims and verified local evidence.
