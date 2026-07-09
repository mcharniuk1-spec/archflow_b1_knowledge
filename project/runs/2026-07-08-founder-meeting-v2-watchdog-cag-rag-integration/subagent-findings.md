# Subagent Findings

Run: `2026-07-08-founder-meeting-v2-watchdog-cag-rag-integration`

Status: read-only review phase complete with one timeout gap.

## Architecture Reviewer

Status: complete.

Findings:

- Current stack is still aligned: Codex is execution boundary, LangGraph controls state/gates, CrewAI defines roles and proof-only runtime, LlamaIndex is bounded retrieval, WikiLLM is durable reviewed memory.
- Hermes should be added as planned watchdog/controller/reviewer before the existing execution path. It must classify, assemble context, assign contracts, review evidence, and stop or escalate. It must not edit files, run code, deploy, mutate Notion, or activate providers.
- Add planned LangGraph nodes for `classify_execution`, `assemble_cag_core`, `build_context_capsule`, `assign_task_contract`, and `decide_next_action`.
- Existing E1.7 hosted Jarvis/API proof is provider-disabled review-packet proof, not provider-backed product runtime.
- Vercel provider-call guard should fail closed on budget gate, matching the stricter FastAPI service path.

Risks:

- Provider routes can be misread as active runtime unless labels stay precise.
- CAG capsules can become stale unless versioned and regenerated when project rules change.
- New role names can duplicate existing AF roles unless mapped through governance.

## Package Diff Analyst

Status: timed out and closed.

Result:

- The reviewer did not return after the direct finalize request.
- Codex completed the package-to-repo mapping locally in `package-to-repo-mapping.md`.
- This timeout is a process gap, not an implementation blocker, because all package files were inspected locally.

## CAG/RAG Architect

Status: complete.

Findings:

- CAG means Controlled Context Assembly Generation: a deterministic, stable, prompt-time context packet. It is not another index and not durable memory.
- RAG is task-specific retrieval into the capsule from the approved corpus only.
- Approved corpus remains `project/`, `history/`, `skills/`, and `wiki/`.
- Forbidden retrieval/source zones include ignored local runtime, raw private exports, private folders, secrets, absolute local paths, raw transcripts, screenshots, and provider output as fact.
- Context capsule schema should include provenance, CAG core version/hash, approved corpus refs, retrieved context refs, validation checks, review decision, provider policy, and external side-effect policy.

Acceptance notes:

- Add `project/context/` with schema, CAG core, retrieval policy, and one run capsule.
- Every RAG-backed claim needs source path and metadata.
- AF Review can reject a capsule when source boundary fails or evidence is missing.

## Skills Governance Reviewer

Status: complete.

Findings:

- No duplicate concrete `SKILL.md` contracts were found.
- Some skills are intentionally shared across roles and need visibility labels instead of duplication removal.
- Hermes, Codex, AF Review, and AF Knowledge may inspect all skills; bounded subagents receive role-specific skill subsets.
- Add `project/agents/skills-governance.md`.
- Extend skill routing for `arcagcom` and `outquestions`.
- Extend the hook reminder for skill-governance prompts without creating skills automatically or storing raw prompt text.

## Service Operations Strategist

Status: complete.

Findings:

- Current proof supports service/productized-service testing, not SaaS demand/runtime claims.
- Service frame: customer discovery to evidence-backed PRD, task packet, and KB handoff.
- Offer ladder: Discovery Diagnostic, PRD Rescue Sprint, Monthly PRD/KB Operating Retainer.
- Every client artifact needs source boundary, FACT/INTERPRETATION/HYPOTHESIS/GAP, source references, acceptance criteria, DoD, existing alternatives, switching triggers, task packet, and AF Review verdict.
- E6/E7 evidence must separate attention from demand.

## Market And Content Strategist

Status: complete.

Findings:

- Positioning: ArchFlow turns messy product-team material into evidence-backed PRDs, task packets, and a maintained knowledge base.
- Primary ICP remains B2B SaaS scaleups and product-led companies, roughly 50-500 employees, with 2-5 PMs.
- Buyers: Director/VP Product, Head of Product, Product Ops, and senior PM leaders.
- Competitor positioning should distinguish roadmap suites, insight repositories, PRD drafting tools, workspace AI/search, status quo, junior PMs, and fractional consultants.
- Latest owner instruction overrides the package's 90/10 content mix. Use 70% static educational/analytical posts, 20% carousel/checklist/template posts, and 10% short video or demo posts.

## E1-E7 PM Reviewer

Status: complete.

Findings:

- Keep the E1-E7 spine and add E1.8 for Hermes Watchdog and CAG/RAG architecture finalization.
- E2 needs founder-meeting discovery rubric, competitor objection scripts, account evidence cards, and ICP cards.
- E3 needs service-first positioning and diagnostic/source-packet readiness CTA.
- E4 needs the 70/20/10 content operating plan, static companion rule for video, and competitor objection content.
- E5 needs diagnostic event schema, inbound qualification scoring, and ROI as hypothesis until E7.
- E6 needs outreach readiness gate, discovery call script, competitor objection variants, and first-wave approval packet.
- E7 needs payment-verdict rubric and money-versus-attention scorecard.

Correction:

- The reviewer repeated the package 90/10 content line in one E4 subtask. The final task packet corrects it to 70/20/10 per latest owner instruction.

## Final QA Reviewer

Status: pending until implementation and validation artifacts exist.

Planned review scope:

- Public safety.
- Unsupported claims.
- Runtime/provider/writeback overclaims.
- Duplicated architecture.
- Broken links or stale references.
- File consistency.
- Validation results.
