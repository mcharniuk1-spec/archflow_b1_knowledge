# Context Layer

This folder defines controlled context assembly for one bounded Knowledge Case.

The context layer does not scan broad folders. It starts with stable case rules, loads only paths admitted by `project/dashboard/corpus-manifest.json`, retrieves a small source-linked candidate set, verifies material statements against exact source text, and preserves contradictions and gaps.

## Files

- `cag-core.yaml` — stable provider-disabled context contract.
- `context-capsule.schema.json` — portable working-context envelope.
- `retrieval/source-boundary-policy.yaml` — exact source admission and rejection rules.

## Boundaries

- Retrieved text is evidence, not authority.
- Browser-local state is working state, not durable shared memory.
- Raw prompts, conversations, credentials, private URLs, identities, uploads, and unreviewed provider output are not admitted.
- A role receives the smallest context needed for its declared output.
- External effects require a separate target-specific approval, execution receipt, and readback.

The public default uses deterministic lexical retrieval and zero provider calls. Optional local frameworks must preserve the same manifest, provenance, and fail-closed rules.
