# ArchFlow Unified Knowledge Agent

Status: implemented and independently approved
Authority: `project/strategic-plan-2026-07-13.md` plus the admitted 2026-08-05 run
Last verified: 2026-08-05
Supersedes: numbered `Architecture 1` / `Architecture 2` as top-level architecture labels

ArchFlow runs one governed knowledge case from question to evidence, reviewed requirements, role-safe work, action validation, result verification, and selective knowledge promotion.

PRDs, ICPs, market reports, onboarding maps, outreach packs, and creative briefs are projections of the same reviewed case. They are not separate architectures or independent sources of truth.

## What is runnable now

The public proof is local, deterministic, synthetic, and provider-disabled:

```bash
python3 project/system/validate_system.py
```

The command checks and applies the versioned schemas, cross-checks the role catalog and controller states, evaluates five action proposals, and rejects malformed and target-escape packets at the schema boundary. One proposal must be eligible; stale/unknown-authority, target-escape, and reviewer-spoof proposals must be blocked.

The validator does not invoke a model, index private data, change project files, use Obsidian, start a service, or execute either proposal.

## Canonical public contracts

- `contracts/operating-model.json` — one state machine and its fail-closed gates.
- `contracts/role-catalog.json` — normalized role authority, including requirements/market research, onboarding support, design, outreach, review, and promotion.
- `schemas/knowledge-case.schema.json` — shared case packet.
- `schemas/action-proposal.schema.json` — proposal-to-requirement validation packet.
- `fixtures/` — synthetic onboarding and adversarial examples.
- `validate_system.py` — standard-library validation and verdict proof.

## Authority model

The controller owns transitions. Roles produce bounded candidates. Requirements and decisions authorize intent. Tools prove only connectivity. A maker cannot approve its own high-risk output. Orbit and Graphify provide generated structural evidence, LlamaIndex retrieves bounded prose, and Obsidian/WikiLLM retain reviewed durable knowledge.

## Private seam

The public project does not require a private vault, private runtime, absolute device path, credential, or personal configuration. A private installation may implement adapters behind these contracts, but only sanitized reviewed conclusions may cross into public Git.

## Current limits

- The dashboard is not migrated in this architecture run.
- GitLab Orbit Local is a beta structural adapter and is optional.
- The fixture proves contract behavior, not production autonomy, model quality, live Obsidian access, or external action.
- Legacy dashboard/report labels remain compatibility residue until the plan in `docs/dashboard-integration-plan.md` is separately approved and executed.
