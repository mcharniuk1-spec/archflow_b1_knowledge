# Operating Rules

These rules apply to the generic public ArchFlow tool. A local workspace may add stricter private rules, but it must not weaken the source, authority, review, or external-action boundaries below.

## Public and language boundary

Keep tracked product files in English and public-safe. Do not commit:

- personal names, email addresses, identity allowlist values, or private account identifiers;
- keys, tokens, cookies, passwords, certificates, credential values, or credential-presence signals;
- local absolute paths, private URLs, raw transcripts, customer material, unpublished data, or private exports;
- browser profiles, screenshots containing user input, recovery bundles, run archives, or generated structural indexes;
- claims of customers, ROI, speed, memory savings, billed-token savings, production quality, or safety without an exact public comparator and limitation.

Translate a non-English source only when the source may be used, and retain only the approved public-safe summary with its provenance.

## Source and memory boundary

The dashboard and retrieval scripts may read only the exact files listed in `project/dashboard/corpus-manifest.json`. Every retrieved result must return a repository-relative source path. A model response, vector match, or generated graph is evidence to verify—not authority.

Maintain reusable knowledge through the solution-memory and action-memory schemas in `project/database/`. Promote only reviewed meaning with source lineage, owner, freshness, contradictions, and supersession. Raw prompts, transient preferences, personal context, and unreviewed outputs do not become durable memory.

## Case and role rule

Every meaningful run starts with a bounded case:

- objective and decision supported;
- allowed and excluded sources;
- current requirements and acceptance checks;
- one owner per output;
- tools, skills, exact targets, and forbidden effects;
- independent reviewer, retry cap, stop, rollback, and recovery;
- expected evidence, receipt, and next safe action.

Use the smallest functional role pack that owns the output, its checks, review, and integration. The 21-role roster is configuration, not an always-running team. A role, skill, authentication session, tool availability, or model name never expands case authority.

## State and loop rule

LangGraph is the canonical state-owner contract. A compatible runtime may implement its nodes, but the state envelope, reducers, interrupts, attempt caps, and terminal states remain explicit.

Use the bounded loop:

1. Research the admitted sources and name gaps.
2. Define the task, roles, tools, checks, reviewer, and stop conditions.
3. Produce one candidate in the claimed scope.
4. Run deterministic maker checks.
5. Freeze the candidate for an independent approve, revise, or block verdict.
6. Repair only exact findings and stop at the declared retry cap.
7. Execute one external action only after its separate gate.
8. Read back the exact target and record the result.
9. Promote only reviewed reusable meaning.

If the same blocker repeats without new evidence, authority is unclear, or the retry/budget cap is reached, stop and hand off instead of looping.

## Parallel work and communication

Before parallel edits, create a caller-supplied local communication packet under ignored `project/local/communication/` or use the browser Communication Center. Record the objective, source boundary, file claims, output, reviewer, blockers, and next action. One writer owns each shared target at a time.

Do not commit accumulated chat logs or operator history. A reusable handoff belongs in the versioned packet or execution-report schema; ephemeral coordination stays local and ignored.

## Evidence and reporting

Substantial work produces a packet that validates against `project/database/run-envelope.schema.json` or an equivalent public contract. It distinguishes documented, configured, locally tested, independently reviewed, approved action, read back, promoted, blocked, and not recorded.

Maker and independent reviewer must be different contracts for consequential work. The integrator owns conflict resolution, merge order, final validation, and handoff. None may self-approve a high-risk result.

## Provider and external-action rule

The provider registry defaults to `none`. Credential names may be documented, but values stay server-side. Authentication identifies an administrator and grants no provider or write authority.

Require a separate exact approval before any provider call on non-public material, dependency installation, Git mutation, deployment, production promotion, publication, message send, database mutation, external writeback, or irreversible/destructive action. The action packet must name the target, operation, data class, budget, side effects, rollback, replay protection, reviewer, and readback.

A successful command is not proof of the external outcome. Completion requires target readback or an explicit unknown result.
