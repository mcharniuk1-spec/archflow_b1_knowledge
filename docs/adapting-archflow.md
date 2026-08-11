# Adapt ArchFlow to Your Organization

Status: public implementation guide
Last verified: 2026-08-11

Start with a bounded onboarding decision, not a whole-organization ingestion. The safest first case is one contributor or team responsibility, one current objective, one source set, one reviewed requirement, and one proposal that can be objectively accepted or blocked.

## Adaptation sequence

1. Copy the synthetic case and proposal fixtures into a local ignored workspace.
2. Define public, private, generated, and prohibited source classes.
3. Assign authority: requirement owner, maker, independent reviewer, integrator, and freshness owner.
4. Replace synthetic evidence with allowlisted sources and stable repository-relative or opaque private references.
5. Write requirements with stable IDs, state, evidence, acceptance, non-goals, conflicts, and review trigger.
6. Test one eligible local proposal plus adversarial stale, conflicting, self-reviewed, unapproved, and unverifiable proposals.
7. Add read-only lexical retrieval, then LlamaIndex document/node identity and metadata routing.
8. Evaluate any semantic or vector adapter only behind the retrieval contract, with lexical fallback and a fixed promotion benchmark.
9. Add an optional human review workspace and structural index only as bounded evidence—not as unbounded ingestion or business authority.
10. Add write or external adapters only after exact approval, rollback, receipt, and readback behavior is proven.

## Configuration layers

| Layer | Safe content | Storage |
|---|---|---|
| Public defaults | schemas, roles, workflows, synthetic fixtures | Git |
| Local profile | corpus allowlist, non-secret paths, test state | ignored local files |
| Private knowledge | confidential sources, decisions, mappings | organization-controlled private store |
| Secrets | credentials and tokens | app-native auth or OS keychain, never knowledge files |
| Generated evidence | indexes, raw receipts, logs | ignored rebuildable runtime |

## Definition of operable

A clone is operable when the provider-disabled fixture validates, failures are explicit, private adapters are optional, setup and rollback are documented, the source boundary fails closed, and a reviewer can reproduce every acceptance claim. A connected model, pretty dashboard, citation, or successful command alone does not meet this bar.

## Repository organization

Keep machine contracts near their validators, narrative guidance under `docs/`, synthetic examples under `fixtures/`, editable diagram source in Git, and reviewed reusable meaning in the retained solution/action-memory schemas. Keep private or local data outside the public repository. Replace or supersede stale guidance explicitly instead of carrying an operational archive into the product corpus.
