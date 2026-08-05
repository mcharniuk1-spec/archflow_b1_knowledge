# Decision: One Knowledge Case with Orbit as Structural Evidence

Date: 2026-08-05
Status: accepted; implementation independently approved
Decision owner: project architecture authority
Review: independent architecture review completed with APPROVE after bounded repairs

## Decision

ArchFlow uses one Knowledge Case Controller for onboarding, knowledge support, requirements, role work, action validation, result verification, and knowledge promotion.

The former numbered architectures are compatibility labels only. PRD, ICP, and market research are projections produced by the bounded `requirements_and_market_research` role. They do not own system state or execution authority.

GitLab Orbit Local is an optional private adapter for code-structural evidence over one allowlisted public-code snapshot only. It is not a durable knowledge store, prose retriever, requirement authority, validator, or executor. Raw Orbit data remains private; only sanitized reviewed evidence receipts may enter Obsidian/WikiLLM or public Git.

## Why

The old split duplicated state between knowledge production and agent work even though both depended on the same source boundary, owner, requirements, review, permissions, receipts, and handoff. A single case lets a new employee see current knowledge, propose work, and receive a deterministic requirement/permission verdict before action.

## Consequences

- Role contracts become versioned data and role names do not grant authority.
- Every material proposal links to current requirements and decisions.
- Designer, outreach, copy, implementation, review, integration, and knowledge promotion remain separate responsibilities.
- Maker/reviewer separation is mandatory for substantial or high-risk work.
- Obsidian stores reviewed knowledge and sanitized receipts; it is never indexed by Orbit.
- The dashboard migration is a separate future action and cannot be inferred from this decision.
- The missing owner Orbit attachment remains an explicit identity gap.

## Revisit when

- the missing Orbit attachment identifies a different product;
- Orbit changes schema, storage, authorization, or MCP behavior;
- the public controller implementation requires a breaking schema change;
- a reviewed dashboard migration retires legacy packet compatibility.
