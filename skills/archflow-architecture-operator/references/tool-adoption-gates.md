# Tool Adoption Gates

Apply this gate before adding a framework, plugin, hook, model adapter, vector store, connector, MCP server, or external skill.

## Required evidence

1. Name one bounded problem that the retained stack cannot solve adequately.
2. Verify the primary source, maintainer, license, release or commit, platform fit, and support status.
3. Inspect install scripts, hooks, network use, telemetry, secret access, write scope, deletion capability, and transitive dependencies.
4. Run a static and semantic safety review. Record which checks actually ran.
5. Pin the tested version or commit and define uninstall, rollback, and fallback behavior.
6. Test in a disposable sanitized fixture with providers and external writes disabled where possible.
7. Compare with the retained baseline using predeclared metrics and equal inputs.
8. Require independent review before granting access to credentials, private data, external systems, or production.
9. Record `adopt`, `trial`, `defer`, or `reject`, the supporting evidence, limits, and review date.

## Provider adapters

Use `project/config/provider-registry.json` as the only repository provider inventory. Do not create a competing provider-routing file inside a skill or output packet. A registry entry documents a state and activation requirements; it does not prove a key exists, a model is reachable, a call is approved, or an adapter is live.

Provider evaluation must preserve the `none` fallback, keep secrets server-side, use approved sanitized inputs, set budgets, and produce readback evidence. Provider calls remain zero unless an action-specific contract explicitly authorizes them.

## Decision record

For each candidate, record:

- problem and expected benefit;
- provenance, license, and pinned version;
- capabilities and requested permissions;
- fixture and baseline;
- safety, privacy, cost, and lock-in findings;
- decision, reviewer, limits, rollback, and next review date.

Store working evidence only in a caller-supplied ignored local output directory. After independent approval, reusable conclusions may be shaped as `project/database/solution-memory-record.schema.json`. Do not promote raw traces or install logs.

## Automatic rejects

- permission bypass, hidden network calls, or silent background mutation;
- unbounded read, write, delete, indexing, or credential scope;
- unknown provenance or incompatible license;
- no pinned version, uninstall path, or provider-disabled fixture;
- duplicate orchestration or memory authority without a measured need;
- claims based only on documentation, a dashboard label, or an unverified benchmark.
