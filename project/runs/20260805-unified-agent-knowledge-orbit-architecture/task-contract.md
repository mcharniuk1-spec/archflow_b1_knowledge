# Unified Agent Knowledge and Orbit Architecture Task Contract

Run: `20260805-unified-agent-knowledge-orbit-architecture`

## State and boundary

- State: architecture/research plus private local integration.
- Public scope: reusable, English-only system architecture, role contracts, onboarding knowledge workflow, documentation, repository visuals, dashboard integration plan only, and public-safe examples.
- Private scope: local knowledge routing and Orbit/Obsidian integration. No private source text, device paths, account identifiers, credentials, or provider secrets may enter the public repository.
- Explicit exclusions: dashboard implementation, deployment, production promotion, provider activation, automated outreach, publication, or uncontrolled corpus ingestion.

## Outcome

Replace the old numbered-architecture framing with one governed operating workflow. Market research and PRD creation become a bounded `requirements-and-market-research` role inside that workflow. The primary product becomes a reliable, source-grounded onboarding and action-support knowledge agent that validates proposed work against reviewed requirements and project decisions.

## Acceptance criteria

1. Public/private seams and promotion gates are explicit and testable.
2. Orbit has a documented and locally operable Obsidian integration with fail-closed behavior and no secret persistence.
3. All historically executed roles are normalized into reusable role contracts, including research, PRD, pain analysis, outreach qualification/copy, publication creative, designer, reviewer, knowledge librarian, and integrator.
4. Role outputs retain evidence paths, authority, owner, freshness, contradictions, requirement references, approval status, and receipts.
5. Public documentation supports clean-clone adaptation without the owner's private environment.
6. Layered architecture visuals are public-safe, legible, and versioned in the repository.
7. Dashboard work is limited to a future integration plan.
8. Independent architecture, evidence, design, and privacy review reaches PASS or records explicit gaps.
9. The public safety scan and focused architecture checks pass after the final public edit.
10. Only this run's intended changes are committed and pushed.

## Bounded lanes

| Lane | Role | Exclusive output scope | Evidence requirement | Forbidden actions | Stop condition |
|---|---|---|---|---|---|
| A | System architecture engineer | `lanes/system-architecture-audit.md` | Repo-relative sources and FACT/INTERPRETATION/HYPOTHESIS/GAP | Shared-file edits, dashboard edits, provider execution | Role/state/retrieval/gate proposal complete |
| B | Orbit and knowledge integration engineer | `lanes/orbit-integration-design.md` | Local configuration evidence kept private; public conclusions sanitized | Live vault mutation before integrator approval, secret reads, public private-path leakage | Integration seam and verification plan complete |
| C | Repository research and information architect | `lanes/public-repository-benchmark.md` | Current first-party repository/documentation links and claim status | Copying third-party text, dashboard edits, private ingestion | Benchmark and reusable documentation pattern complete |
| D | Codex integrator and designer | Final architecture, deterministic diagrams, generated art, private integration, tests, and merge | Admission receipt, lane handoffs, visual inspection, test receipts | Self-approval, unrelated worktree changes | Maker artifacts integrated and reviewer gate ready |
| E | Independent reviewer | `independent-review.md` | Maker artifact references, safety checklist, verdict, gaps | Repairing maker output or approving own work | PASS, REVISE, or BLOCK verdict recorded |

Maximum repair attempts: three. The same failure twice stops the run.

## Owner approval record

The owner explicitly requested architecture transformation, private/local Orbit integration, public repository documentation and visuals, and Git push. This does not authorize deployment, production promotion, provider calls, social publication, outreach execution, or destructive cleanup.
