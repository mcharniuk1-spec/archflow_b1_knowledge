# Obsidian, Graphify, and Nexus Setup Review

Date: 2026-07-10
Status: reviewed and locally aligned

## Result

The canonical Obsidian second-brain stack is present and structurally consistent across the global control vault and the three active project vaults. No community-plugin reinstall was justified: all four canonical vaults already contain the required visual and Nexus plugins, with the same core Graph/Canvas baseline.

The main defect was architectural documentation drift. The global vault map described an older single-vault state even though the separate project vaults were registered and configured. That map, the Graphify registry, the graph-view scope, and the Nexus status note were aligned with the verified state.

The refreshed Graphify artifacts were passed through the public-output sanitizer so generated source provenance cannot reintroduce local filesystem paths into the public repository.

## FACT

- Canonical community plugins observed in all four AI vaults: `nexus`, `juggl`, `infranodus-graph-view`, and `3d-graph`.
- Observed plugin versions: Nexus 5.9.4, Juggl 1.5.0, InfraNodus Graph View 0.9.10, and 3D Graph 1.0.5.
- Core Graph, Canvas, backlinks, properties, templates, search, and navigation plugins are enabled in all four canonical vaults.
- The vault configuration verifier passes for all four canonical vaults.
- Real Estate Nexus returned both MCP tool listing and `toolManager_getTools`; Global, Have Website, and Ukraine Dairy Value Chain Thesis had no live socket during this check.
- The public repository Graphify code graph and HTML fallback were refreshed on 2026-07-10: 6,671 nodes, 6,755 edges, and 650 communities.

## INTERPRETATION

- Obsidian is the human-facing control room and project-memory layer.
- WikiLLM is the curated durable agent-memory layer.
- Graphify is generated structural reference and must remain scoped per repository or approved corpus.
- Nexus is a live bridge, not proof of configuration by itself; connector/config, app activation, socket initialize, and tool-manager response are separate gates.
- The registered ArchFlow repository workspace is not a curated second-brain vault. Its raw repository content must not be pulled into the canonical Graphify/Nexus vault stack.

## HYPOTHESIS

- After the three missing vault windows are opened or reloaded, the existing plugin/config baseline should be sufficient to restore their live Nexus sockets without a network reinstall.

## GAP

- Global, Have Website, and Ukraine Dairy Value Chain Thesis need an Obsidian/Nexus reload followed by both Nexus verifiers.
- The refreshed public Graphify output is code-structural; no provider-backed semantic extraction was activated in this review.
- A dedicated ArchFlow project vault does not currently exist. If one is wanted, it should be created as a separate sanitized vault rather than converting the raw repository workspace into a knowledge vault.

## Checks

- `node tools/verify-ai-vault-stack.js`: pass.
- `node tools/verify-nexus-multi-vault.js`: Real Estate `tools_list_response`; three other canonical sockets missing.
- `node tools/verify-nexus-tool-calls.js`: Real Estate `tool_call_response`; three other canonical sockets missing.
- Graphify query over the public repository: pass; existing graph used for orientation.
- `project/scripts/sanitize-graphify-public-output.py`: pass.
- Public YAML/JSON/safety validation: pass after the Graphify refresh and sanitization.
