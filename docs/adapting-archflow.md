# Adapt ArchFlow to Your Organization

Status: public implementation guide
Last verified: 2026-08-05

Start with a bounded onboarding decision, not a whole-company ingestion. The safest first case is one employee role, one current objective, one source set, one reviewed requirement, and one proposal that can be objectively accepted or blocked.

## Adaptation sequence

1. Copy the synthetic case and proposal fixtures into a local ignored workspace.
2. Define public, private, generated, and prohibited source classes.
3. Assign authority: requirement owner, maker, independent reviewer, integrator, and freshness owner.
4. Replace synthetic evidence with allowlisted sources and stable repository-relative or opaque private references.
5. Write requirements with stable IDs, state, evidence, acceptance, non-goals, conflicts, and review trigger.
6. Test one eligible local proposal plus adversarial stale, conflicting, self-reviewed, unapproved, and unverifiable proposals.
7. Add read-only lexical retrieval, then LlamaIndex document/node identity and metadata routing.
8. Evaluate TurboVec only behind the LlamaIndex adapter, with lexical fallback and the fixed promotion benchmark.
9. Add Obsidian as an optional human semantic workspace and Orbit/Graphify as structural evidence—not as unbounded ingestion or business authority.
10. Add write or external adapters only after exact approval, rollback, receipt, and readback behavior is proven.

## Configuration layers

| Layer | Safe content | Storage |
|---|---|---|
| Public defaults | schemas, roles, workflows, synthetic fixtures | Git |
| Local profile | corpus allowlist, non-secret paths, test state | ignored local files |
| Private knowledge | confidential sources, decisions, mappings | approved local vault/runtime |
| Secrets | credentials and tokens | app-native auth or OS keychain, never knowledge files |
| Generated evidence | indexes, raw receipts, logs | ignored rebuildable runtime |

## Definition of operable

A clone is operable when the provider-disabled fixture validates, failures are explicit, private adapters are optional, setup and rollback are documented, the source boundary fails closed, and a reviewer can reproduce every acceptance claim. A connected model, pretty dashboard, citation, or successful command alone does not meet this bar.

## Repository organization

Keep the machine contracts near their validators, narrative guidance under `docs/`, synthetic examples under `fixtures/`, editable diagram source in Git, reviewed public memory under `wiki/`, and private/local data outside the public repository. Preserve historical evidence instead of rewriting it to look current; point readers to one canonical status page.
