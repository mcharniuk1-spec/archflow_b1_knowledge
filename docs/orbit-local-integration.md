# Orbit Local Structural-Evidence Adapter

Status: optional public contract; private wrapper proven directly; client reload/tool discovery pending
Leading product identity: GitLab Orbit Local, confidence 0.80
Last verified: 2026-08-05
Owner attachment status: missing; identity remains an explicit gap

Orbit Local is an optional code-structure adapter. It helps an onboarding or implementation case locate files, definitions, imports, references, and likely structural impact. It is not the knowledge base, requirements authority, prose RAG, action validator, or executor.

## Safe division of responsibility

```text
Orbit Local       code-only structural evidence from the public repository
Graphify          generated structural reference and relationship comparison
LlamaIndex        allowlisted prose, requirement, and decision retrieval
Obsidian/WikiLLM  reviewed durable knowledge and sanitized receipts
LangGraph         state, routing, review, repair, and approval gates
Codex             scoped local execution, validation, masking, and promotion
```

## Corpus boundary

- Index one clean, explicitly allowlisted public-code snapshot, never a parent folder.
- Do not index private project material, an Obsidian vault, WikiLLM, a home/Documents scope, credentials, or a second repository.
- Treat the DuckDB, manifest, full source fields, absolute paths, queries, logs, and raw results as private local runtime data.
- Use operating-system permissions; Orbit Local does not add an application authorization layer.
- Store only repository-relative references and sanitized receipt metadata in reviewed knowledge.

## Baseline access

The private integration uses a pinned command-line binary, one private database, and a clean snapshot of the allowlisted public code paths. Before each query, the constrained wrapper checks that the database has exactly one corpus, the snapshot is clean, the indexed commit matches, and the allowlisted source/snapshot hashes match. The wrapper exposes status and bounded repository maps only; raw SQL and corpus-changing `index` are absent.

## Sanitized evidence receipt

An accepted Orbit observation carries:

- opaque evidence ID;
- `corpus_id: archflow-public`;
- repository-relative file and line span;
- symbol reference when relevant;
- Orbit version, schema hash, index snapshot hash, and query recipe hash;
- owner, observed/review dates, freshness, contradictions, requirement links;
- `authority_state: generated_structural_evidence`;
- redaction and independent-review status.

Raw evidence is resolved through a private map. The public or Obsidian receipt contains no local absolute path, DuckDB location, full source body, private identifier, or credential.

## Onboarding and action use

For onboarding, prose retrieval supplies the current requirement and rationale; Orbit suggests repository entry points; Graphify provides an independent structural comparison; the source file is read exactly; conflicts become gaps. For a proposed change, Orbit can identify likely affected definitions and imports, but the action validator still checks requirement coverage, role permission, rollback, tests, reviewer, and approval.

## Verification ladder

1. Confirm product identity and pin version/checksum.
2. Prove the corpus resolves to exactly the approved public repository and the database stays outside it.
3. Run bounded schema and query recipes with no full-content projection.
4. Convert paths to repository-relative form and compare a result with exact source plus Graphify.
5. Prove stale-index detection, restart reproducibility, and rollback.
6. Promote one sanitized receipt only after independent privacy and evidence review.

Orbit is currently beta. Version pinning, schema checks, and re-verification on upgrade are mandatory.

The direct MCP process passes initialize, tool-list, status, bounded map, and traversal-denial checks. The Obsidian/Cursor clients must be reloaded before the newly configured server can be claimed as live-discoverable in those clients.
