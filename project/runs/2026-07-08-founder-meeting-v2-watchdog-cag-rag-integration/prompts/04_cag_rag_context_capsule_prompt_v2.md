# CAG/RAG Context Capsule Prompt v2

Build a context capsule before any subagent is prompted.

## CAG Core

CAG means Controlled Context Assembly Generation. It is a stable, compact context packet for one run or task. It is not a vector index, a memory store, or broad ingestion.

CAG includes:

- Project operating rules.
- Founder meeting methodology.
- Current architecture boundaries.
- Role and skill maps.
- Source boundaries.
- E1-E7 state.
- Gated claims and stop conditions.
- Acceptance criteria.

## RAG Layer

RAG retrieves task-specific evidence from the approved public-safe corpus. Retrieval must return source paths and metadata or it is not accepted as evidence.

Approved default corpus:

- `project/`
- `history/`
- `skills/`
- `wiki/`

Forbidden by default:

- ignored local runtime data;
- raw private exports;
- secrets or credentials;
- raw transcripts or screenshots;
- private URLs;
- absolute local paths;
- provider output as fact.

## Capsule Fields

Use `project/context/context-capsule.schema.json`.

The capsule must include run ID, goal, execution type, risk, CAG refs, RAG refs, facts, interpretations, hypotheses, gaps, allowed files, forbidden actions, role assignments, acceptance criteria, evidence requirements, stop conditions, provider policy, side-effect policy, and review decision.

## Output Rule

Subagents receive only the context needed for their task. Do not paste whole repo history.
