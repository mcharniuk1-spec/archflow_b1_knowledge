# GitLab Orbit Local Integration Design

Date: 2026-08-05
Lane: Orbit and knowledge integration engineer
Status: identity and install evidence updated; indexing and runtime proof remain gated

## Updated conclusion

**Leading Orbit identity: GitLab Orbit Local (`gitlab-org/orbit/knowledge-graph`). Confidence: moderate-high (0.80).**

GitLab Orbit Local is the strongest task-matched identity because it creates an on-device, queryable code graph for coding agents. It directly supports repository orientation, definition/import discovery, impact analysis, and code-grounded onboarding. Those jobs match the requested knowledge-agent architecture more closely than Recursive Labs Orbit, which is a native development environment with its own Markdown Vault and agent surfaces.

The owner-referenced Orbit attachment is still missing, so the identity is not certain. The architecture must preserve that as a GAP and must not infer any instructions from the missing attachment.

The approved seam is hybrid:

```text
GitLab Orbit Local -> code-only structural evidence from public/
Graphify           -> generated structural reference and relationship views
LlamaIndex         -> allowlisted prose/requirements retrieval
Obsidian + WikiLLM -> reviewed durable knowledge and sanitized receipts
LangGraph          -> workflow state, transitions, interrupts, and gates
Codex              -> local execution, validation, edits, promotion, and approval boundary
```

Orbit Local is an adapter, never an authority source. It must not index the project root, `private/`, any Obsidian vault, WikiLLM corpus, home/Documents scope, or another repository. The only candidate corpus is `public/`.

## Identity comparison

| Candidate | First-party behavior | Match to this task | Decision |
|---|---|---|---|
| **GitLab Orbit Local** | Builds a code-only graph from any local repository; stores it in DuckDB; exposes CLI and experimental MCP access; indexes files, definitions, imports, and cross-file references. | Strong match for repository orientation, code onboarding, structural evidence, and impact validation. | Leading identity and approved adapter design. |
| **Recursive Labs Orbit** | Native macOS development environment combining an agent, editor, browser, terminal, Markdown Vault, Git, skills, and MCP tools. | Useful execution environment, but no first-party Obsidian connector or task-specific knowledge-graph role was found. | Not the baseline integration. |
| **Orbit Audit Suite** | Markdown-based Claude Code review skills with no executable code, hook, or MCP server. | Review pack, not a knowledge or Obsidian bridge. | Not the requested integration. |
| **Obsidian Orbital** | Obsidian relation/dangling-link navigation plugin. | Naming collision only. | Do not install as a substitute. |

### FACT

- [GitLab Orbit Local](https://docs.gitlab.com/orbit/local/) runs on-device, requires no GitLab account or network connection, indexes code only, writes a local DuckDB graph, and supports CLI, `glab`, and MCP access.
- [What GitLab Orbit Local indexes](https://docs.gitlab.com/orbit/local/indexing/) says the index is scoped to the directory passed to `orbit index`; it respects `.gitignore`, records indexed repositories by absolute path, and stores files, definitions, full source content, imports, and cross-file references.
- The same indexing documentation says Orbit Local has no authorization layer; access is controlled only by operating-system permissions.
- The [schema reference](https://docs.gitlab.com/orbit/local/schema/) defines code-domain nodes for directories, files, definitions, and imported symbols, with full source text in file and definition content fields.
- The [MCP documentation](https://docs.gitlab.com/orbit/local/access/mcp/) describes a stateless stdio server using raw read-only DuckDB SQL. It also exposes an `index` tool, which can broaden the corpus and is therefore prohibited by this design.
- GitLab marks Orbit Local and its MCP surface as beta/experimental; command and configuration shapes may change.
- The integrator checksum-verified and installed pinned Orbit Local **v0.95.1** under the private runtime. No provider was activated.
- The installed binary bundles an official `orbit-local` skill. GitLab's general Orbit skill is separately pinned at **v0.22.0** and MIT-licensed. Skill presence does not grant runtime or corpus authority.
- The public repository is the only candidate index corpus. No index of the project root, private runtime, or Obsidian vault is authorized or claimed.
- Recursive Labs describes its [Orbit environment](https://www.orbit.build/how-it-works) as an agent spanning editor, browser, terminal, and its own Markdown Vault. That is a different product and does not supply a documented Obsidian knowledge-graph seam.

### INTERPRETATION

GitLab Orbit Local is a precise structural evidence source, not a company knowledge base. Its graph can answer where code lives and what definitions/imports may be affected. It cannot establish business authority, requirements validity, owner approval, freshness policy, contradiction resolution, or durable knowledge.

Because the graph stores full source content and absolute repository paths without an application authorization layer, its DuckDB file and raw query outputs are private runtime artifacts even when the indexed source is the public repository.

### HYPOTHESIS

If the missing owner attachment names GitLab Orbit, this design is directly implementable with the pinned private binary. If it names another Orbit product, the hybrid authority model remains valid, but the adapter-specific install and query steps must be revisited.

### GAP

- The owner attachment and its exact Orbit instructions are absent.
- Installation is proven, but this lane does not claim that `public/` has been indexed or that a query/MCP runtime has passed verification.
- The pinned binary's exact MCP tool surface must be checked locally because GitLab marks MCP experimental and first-party documentation has changed across versions.
- No Orbit query recipe, receipt, or Obsidian control note has yet passed independent review.
- No provider-backed use is authorized or needed for the structural adapter.

## Authority and responsibility split

| Layer | Exclusive job | What it must not become |
|---|---|---|
| GitLab Orbit Local | Queryable code-only evidence: paths, definitions, imports, references, line spans, structural impact. | Requirements authority, prose RAG, durable memory, action executor, or vault indexer. |
| Graphify | Generated repository/corpus structure, relationship discovery, graph views, and broader structural reference. | Final human synthesis or durable truth. |
| LlamaIndex | Allowlisted retrieval over approved prose, requirements, decisions, role contracts, and sanitized history. | Durable store or uncontrolled corpus indexer. |
| Obsidian/WikiLLM | Reviewed durable knowledge, decisions, ownership, freshness, contradictions, and sanitized evidence receipts. | Raw Orbit database, raw full-source mirror, or hidden runtime log. |
| LangGraph | Task state, routing, repair bounds, approval interrupts, and terminal status. | Knowledge authority or file editor. |
| Codex | Local operator, query integrator, validator, editor, reviewer coordinator, masking boundary, and promotion executor. | Automatic provider, deployment, or external-action authorization. |

Orbit and Graphify may overlap on structural claims. Neither silently wins. A disagreement becomes a contradiction record requiring source inspection. Orbit is stronger for its current parsed code snapshot and queryable definitions/imports; Graphify remains the established generated structural reference and cross-artifact relationship layer.

## Exact safe seam

### Corpus and storage boundary

1. Resolve and verify the candidate corpus root as exactly `public/`.
2. Reject the project root, `private/`, any parent directory, any Obsidian vault, any symlink escaping `public/`, and every additional repository.
3. Invoke the pinned private Orbit binary with an explicit private `--db` location rather than the default shared home-level database.
4. Keep the DuckDB file, index manifest, raw SQL, raw results, logs, and corpus mapping under ignored private runtime storage.
5. Apply restrictive operating-system permissions because Orbit Local has no internal authorization layer.
6. Never copy, attach, commit, or ingest the DuckDB file into Obsidian, WikiLLM, Graphify, LlamaIndex, public Git, or a provider prompt.

Recommended logical private layout for integrator implementation:

```text
private/runtime/orbit/
  bin/                       # pinned checksum-verified binary
  config/                    # corpus allowlist and query policy
  db/                        # private DuckDB
  recipes/                   # reviewed SQL templates
  receipts/                  # raw private receipts and result hashes
  evidence-map.local.yaml    # opaque evidence ID -> private artifact mapping
```

No directory above is created or changed by this lane.

### Query path

1. LangGraph admits a read-only structural-evidence request.
2. Codex selects an approved, versioned query recipe.
3. A wrapper validates that the recipe is a bounded read-only query, requires explicit columns and `LIMIT`, and rejects filesystem or corpus-changing actions.
4. Orbit queries the private DuckDB generated only from `public/`.
5. A sanitizer removes absolute paths, full source bodies, private runtime locations, and database metadata from the result.
6. Codex converts paths to `public/`-relative references and binds results to a workspace/index snapshot hash.
7. LangGraph and Codex combine Orbit structural evidence with LlamaIndex prose evidence and Graphify reference evidence.
8. Only a compact sanitized receipt and reviewed conclusion may be promoted to Obsidian/WikiLLM.

### MCP boundary

CLI/query-wrapper use is the baseline because it makes the allowed corpus, database, recipe, and output transformation explicit. MCP may be enabled only after separate runtime proof.

If MCP is enabled:

- expose schema and bounded read-only query operations only;
- deny or wrap the `index` tool so an agent cannot add a directory or second repository;
- require fixed database location and fixed `corpus_id`;
- reject unrestricted `SELECT *`, missing `LIMIT`, full `content` projections, manifest path projections, and result sets above the configured cap;
- do not register Orbit MCP globally when a project-scoped private registration is sufficient;
- do not proxy Nexus or any Obsidian tool through Orbit.

## Obsidian and WikiLLM receipt design

The global Obsidian control vault is not indexed. It stores governance, sanitized query recipes, and receipts that point to private evidence through opaque IDs.

Suggested vault-relative control notes for later reviewed implementation:

```text
wiki/projects/agent-infra/Orbit Query Recipe Registry.md
wiki/projects/agent-infra/Orbit Evidence Receipt Registry.md
wiki/decisions/<reviewed Orbit adapter decision>.md
```

Each recipe record contains:

- `recipe_id`, purpose, approved tables/columns, parameter names, fixed result limit;
- owner role, reviewer role, version, created/reviewed dates;
- permitted corpus `archflow-public`;
- prohibited fields such as full source content and absolute manifest paths;
- expected output schema and failure codes;
- requirement references and retirement trigger.

Each sanitized receipt contains:

- `evidence_id` and private evidence hash;
- `corpus_id: archflow-public`;
- Orbit binary version, schema hash, recipe ID/hash, and index snapshot hash;
- query time, result count, and freshness state;
- repository-relative source references and line spans only;
- owner, contradictions, requirement references, and review status;
- `raw_evidence_location: private-map-only` rather than a path;
- a wikilink to the governing recipe/decision note.

The opaque `evidence_id` is resolved only through `private/runtime/orbit/evidence-map.local.yaml`. The vault note never contains the DuckDB location, absolute repository path, raw SQL output, full source body, private source ID, or credential. This creates a durable human-auditable link to evidence without indexing or mirroring the vault.

## Required evidence metadata

Every Orbit-derived result accepted into a context capsule must include:

| Field | Requirement |
|---|---|
| `evidence_id` | Opaque stable handle; required |
| `corpus_id` | Must equal `archflow-public` |
| `source_ref` | `public/`-relative path plus line span; required |
| `symbol_ref` | Definition/import identity when applicable |
| `source_hash` | Hash of the indexed source version |
| `index_snapshot_hash` | Binds evidence to the on-disk snapshot |
| `orbit_version` | Pinned binary version |
| `schema_hash` | Detects beta schema drift |
| `recipe_id` and `recipe_hash` | Reproducible query identity |
| `authority_state` | Always `generated_structural_evidence`, never `canonical` |
| `owner_role` | Accountable reviewer/maintainer role |
| `observed_at` and `review_by` | Freshness window |
| `freshness_state` | `current`, `stale`, `unknown`, or `retired` |
| `contradictions` | Conflicting Orbit, Graphify, source, or prose claims plus status |
| `requirement_refs` | Requirements/decisions the evidence informs |
| `redaction_state` | Confirms path/content masking |
| `approval_state` | `unreviewed`, `approved`, `revise`, or `blocked` |

Missing source, owner, freshness, contradiction status, requirement reference, snapshot hash, or recipe identity is a hard failure.

## Employee onboarding retrieval

The onboarding capsule is assembled by responsibility, not by one omnibus index:

1. LlamaIndex retrieves the employee's role contract, active requirements, decisions, terminology, owner/freshness rules, and known contradictions from approved prose.
2. Orbit Local answers bounded structural questions such as where a feature is implemented, which definitions are entry points, and which imports/references connect affected files.
3. Graphify supplies the established generated structure and broader relationship context.
4. Codex reconciles the sources and records disagreements as GAP or contradiction.
5. LangGraph packages the result with action limits and the review gate.

The employee sees a minimal map: authoritative requirements, repository-relative code entry points, source/owner/freshness state, open contradictions, allowed actions, and the evidence receipt IDs. Orbit output alone cannot tell the employee what should be built or whether a decision is current.

## Action validation

For a proposed code or configuration action:

1. LlamaIndex/Obsidian establish the governing requirement, decision, owner, and permission.
2. Orbit identifies candidate definitions, imports, callers, and structurally affected files from the current `public/` snapshot.
3. Graphify supplies an independent structural comparison where applicable.
4. The validator rejects stale index snapshots, open contradictions, absent requirement references, scope expansion outside `public/`, unbounded result sets, or missing rollback/tests.
5. Codex inspects source and applies any authorized edit.
6. A separate reviewer verifies evidence, behavior, privacy, and claim scope.
7. LangGraph records accept, repair, split, escalate, or stop.

Orbit never approves the action, edits a file, changes LangGraph state, deploys, pushes, writes externally, or promotes its own result.

## Knowledge promotion

Orbit results are generated evidence, not durable knowledge. Promotion requires:

1. sanitized recipe and reproducible receipt;
2. source read-back at the recorded repository-relative path;
3. comparison with Graphify and relevant prose evidence;
4. duplicate and contradiction review;
5. named owner, freshness/review date, requirement references, and retirement condition;
6. maker-reviewer separation;
7. Codex-applied targeted WikiLLM/Obsidian edit;
8. post-write read-back and promotion receipt.

Only the reviewed conclusion and sanitized evidence reference are promoted. Raw DuckDB rows, full source content, absolute paths, local configuration, SQL traces, and runtime logs remain private.

## Public versus private/local material

| May be public | Must remain private/local and ignored |
|---|---|
| Layer architecture and threat model | Installed binary location and checksum receipt |
| Query-recipe schema and invented fixtures | Exact corpus path, database path, and OS permission details |
| Metadata schema and failure codes | DuckDB file and `_orbit_manifest` contents |
| Public-safe SQL examples using placeholders and explicit limits | Raw SQL results and full source fields |
| Verification and rollback procedure | Evidence-map, raw receipts, logs, and runtime configuration |
| Sanitized repo-relative evidence examples | Absolute paths or private source identifiers |
| Tool/version/license facts | Credentials, auth state, or provider configuration |

## Proof ladder

### Identity proof

- **Current:** GitLab Orbit Local is the leading identity at confidence 0.80.
- **Required to close GAP:** owner confirms the product or supplies the missing attachment.

### Install proof

- **Current:** pinned v0.95.1 binary checksum-verified and installed under private runtime; provider disabled.
- **Current:** bundled official `orbit-local` skill present; general Orbit skill v0.22.0 identified as MIT.
- Install proof does not prove corpus scope, index freshness, query correctness, MCP availability, or authorization.

### Configuration proof

- Resolve corpus to exactly `public/` after symlink checks.
- Use a dedicated private database path and explicit corpus allowlist.
- Confirm database, config, receipts, and evidence map are ignored and have restrictive permissions.
- Confirm no Obsidian, WikiLLM, project-root, private, parent, or second-repository path is configured.
- Review/pin installed skills before agents use them.

### Runtime proof

- Index a deterministic public-safe fixture or the approved `public/` corpus only after the corpus check passes.
- Record Orbit version, schema hash, manifest corpus ID, index snapshot hash, file/definition counts, and elapsed status without exposing absolute paths.
- Run bounded schema and query recipes and compare expected repo-relative results.
- Confirm full-content and absolute-path fields are removed from sanitized outputs.
- If MCP is tested, record actual pinned-version tool names and block corpus-changing/index operations.
- Confirm zero provider calls, zero vault reads, zero vault writes, and zero public-repository writes.

### Operational proof

- Complete one onboarding query and one action-impact query with Orbit + Graphify + LlamaIndex evidence.
- Reproduce both from recipe and snapshot hashes.
- Complete independent review, sanitized Obsidian receipt, and rollback drill.

## Deterministic verification checklist

- [ ] Owner confirms GitLab Orbit identity or missing attachment remains an explicit GAP.
- [ ] Verify pinned binary version and checksum receipt without publishing private paths.
- [ ] Verify the installed skill bundle and general skill version/license; do not auto-activate either.
- [ ] Resolve corpus root and assert it equals `public/`, is not a symlink escape, and has no additional repository sibling.
- [ ] Assert the private database path is outside `public/`, ignored, and permission-restricted.
- [ ] Negative-test project root, `private/`, parent directory, global vault, and a second repository; all must return `BLOCK_CORPUS`.
- [ ] Verify `.gitignore` exclusions and record only sanitized counts.
- [ ] Inspect schema hash and required tables for the pinned version.
- [ ] Confirm file/definition content and absolute manifest paths exist only in the private database and never in promoted output.
- [ ] Validate SQL recipes: read-only, explicit columns, fixed corpus filter, fixed `LIMIT`, no full-content or manifest-path projection.
- [ ] Verify stale index detection after a controlled fixture change.
- [ ] Compare one definition/import result with source read-back and Graphify evidence.
- [ ] Treat disagreements as contradiction records, not silent overwrite.
- [ ] If MCP is enabled, verify actual tools; deny `index` and unrestricted raw SQL through the adapter.
- [ ] Confirm provider/network mode remains disabled for the local structural path.
- [ ] Confirm no Obsidian/WikiLLM file was read by Orbit and no vault path appears in the database.
- [ ] Validate sanitized receipt fields, repo-relative paths, hashes, owner, freshness, contradictions, and requirement references.
- [ ] Resolve the receipt's opaque evidence ID through the private evidence map, then confirm the vault note itself contains no private path.
- [ ] Run the public safety scan after any public template or receipt example is added.
- [ ] Repeat query after restart and verify the same snapshot/recipe produces the same bounded result.
- [ ] Complete rollback and confirm no MCP registration, process, database reference, startup item, or vault mutation remains.

## Rollback and uninstall

1. Stop any Orbit MCP process and remove only the project-scoped Orbit MCP registration.
2. Disable the Orbit adapter and installed skills; preserve only reviewed public templates and sanitized receipts.
3. Archive hashes/status needed for audit, then move the generated DuckDB, raw receipts, and evidence map to recoverable private quarantine or delete them only with owner approval.
4. Remove the pinned binary and private configuration only after verifying the exact target.
5. Remove or retire sanitized Obsidian recipe/receipt entries through targeted reviewed edits; never delete unrelated notes.
6. Re-run corpus-name, MCP-name, process, private-database, public-safety, and vault-mutation checks.
7. Because Orbit never indexes the vault or writes durable knowledge directly, no vault-wide rebuild should be necessary.

## Admission decision

**Proceed only with a provider-disabled, read-only structural pilot over `public/`.** Installation proof for pinned GitLab Orbit Local v0.95.1 exists. Indexing, CLI/MCP query execution, Obsidian receipt creation, and any skill activation still require the deterministic corpus, privacy, schema, and reviewer gates above. Orbit Remote, project-root/private/vault indexing, provider activation, global MCP registration, and direct knowledge promotion remain prohibited.
