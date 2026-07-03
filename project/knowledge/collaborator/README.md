# Collaborator Knowledge Base

Date: 2026-07-03
Status: E1.6 review-ready

## Role

The collaborator knowledge base is the public-safe workspace for the collaborator agent. It keeps collaborator-specific context separate from the primary operator lane.

Use it for:

- collaborator questions and assumptions;
- review notes for product, market, delivery, and critique;
- handoff summaries from the collaborator agent;
- owner-approved task candidates;
- gaps that should be answered before Epic 2 execution.

## Operating Boundary

The collaborator agent may read public-safe project files and approved summaries. It must not ingest or store raw private material by default.

If the collaborator agent receives private material elsewhere, the output saved here must be only a sanitized summary with:

- source category;
- date;
- FACT / INTERPRETATION / HYPOTHESIS / GAP split;
- allowed next action;
- review status.

## Relationship To Other Memory Layers

| Layer | Use |
|---|---|
| This folder | Collaborator-specific public-safe summaries and questions |
| `wiki/` | Durable shared memory and run history |
| `project/runs/` | Execution proof, handouts, checks, and blockers |
| Notion | Private task/PM layer and owner review |
| Obsidian/WikiLLM outside public repo | Human-readable long-term knowledge after review |

## Current E1.6 Scope

This folder completes the collaborator side of the E1.6 split. It gives the collaborator agent a clean home without exposing private identities or raw sources in the public repository.
