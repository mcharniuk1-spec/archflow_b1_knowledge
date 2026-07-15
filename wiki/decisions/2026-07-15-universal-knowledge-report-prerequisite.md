# Decision - Knowledge Report Before Agent Control

Date: 2026-07-15

## Decision

Require a browser-local Knowledge Service report before Agent Control may prepare a local handoff in either Administrator or Guest preview.

## Rationale

Knowledge Service establishes the bounded objective, allowed evidence, exclusions, requested output, reviewer, and stop conditions. Agent Control must reuse that context rather than design agents around an unbounded request. A shared rule also removes a misleading difference between the Dashboard and Jarvis surfaces.

## Consequences

- The dashboard and Jarvis both hold Agent Control until `prepared_local` knowledge state exists.
- Administrator preview may show optional guarded-control documentation, but it does not bypass the sequence.
- A prepared report remains a review-required browser-local artifact, not proof of retrieval, model execution, file creation, or external action.

## Revision trigger

Revisit only if a future authenticated runtime introduces a separate, verified reviewed-report selector with provenance, authority, retention, and audit evidence.
