# Obsidian, Graphify, and Nexus Setup Review

Date: 2026-07-10
Status: complete with live-runtime gaps

## FACT

- The canonical four-vault Obsidian stack is configured and passes the local file/config verifier.
- The required community plugin baseline is already present: Nexus, Juggl, InfraNodus Graph View, and 3D Graph.
- Core Graph/Canvas and navigation support are enabled across the canonical vaults.
- The Real Estate vault passed Nexus socket initialization and `toolManager_getTools` verification.
- Global, Have Website, and Ukraine Dairy Value Chain Thesis did not expose live sockets during this check.
- The ArchFlow repository workspace is registered with Obsidian but is not a curated second-brain vault.

## INTERPRETATION

The correct architecture is a global human control room plus scoped project vaults, with WikiLLM as curated durable memory, Graphify as generated structural reference, and Nexus as the live bridge. Plugin installation is not the current blocker; runtime reload and live socket validation are.

## HYPOTHESIS

Reloading the three missing Obsidian vault windows should restore their sockets without reinstalling the existing plugins.

## GAP

- Three canonical Nexus runtimes remain unverified live.
- The public Graphify code graph and HTML fallback were refreshed under the public-only scope; semantic/provider extraction remains disabled.
- The generated Graphify artifacts were sanitized for local path safety and passed the public-safety scan.
- No dedicated sanitized ArchFlow Obsidian vault exists; the raw repository workspace must remain outside the canonical knowledge graph.

## Checks

- `node tools/verify-ai-vault-stack.js`: pass.
- `node tools/verify-nexus-multi-vault.js`: one live socket, three missing.
- `node tools/verify-nexus-tool-calls.js`: one successful tool-manager response, three not reachable.
- Existing Graphify query: pass.
- Public YAML/JSON/diff/safety checks: pass.
