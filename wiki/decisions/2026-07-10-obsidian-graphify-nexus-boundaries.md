# Decision - Obsidian, Graphify, and Nexus Boundaries

Status: accepted
Date: 2026-07-10

## Decision

Keep the canonical AI-vault stack as one global Obsidian control room plus three scoped project vaults. Keep WikiLLM as curated durable memory, Graphify as generated structural reference, and Nexus as the live Obsidian bridge.

Do not install or activate the second-brain plugin stack in the raw ArchFlow repository workspace. Its registration in Obsidian is a workspace convenience, not evidence that it is a safe knowledge vault.

## Rationale

- All required plugins are already present in the canonical vaults.
- The raw repository contains source files and private/local material that should not be treated as human semantic memory.
- The stale global vault map, rather than missing plugins, was the main architecture defect.
- Live Nexus readiness must remain separate from file/config readiness.

## Consequences

- Future ArchFlow knowledge should route through the public WikiLLM project layer and the global `agent-infra` vault notes until a separate sanitized project vault is approved.
- Future plugin work should be driven by a verified missing capability, not by copying plugins into every registered Obsidian workspace.
- Any Nexus-dependent task must record the target vault and pass `toolManager_getTools` before using live actions.
