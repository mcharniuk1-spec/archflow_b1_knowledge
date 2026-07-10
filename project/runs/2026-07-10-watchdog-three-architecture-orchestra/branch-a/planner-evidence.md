# Branch A Planner Evidence

Status: planning evidence only; no provider, hosting, deployment, or external action was performed.

## Role Availability Gap

GAP - Luna model selection unavailable

The collaboration interface used for this planning role exposes no model selector. The required bounded planner role was still fulfilled; this note records its repository evidence and recommended implementation boundary.

## Evidence Reviewed

- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/context-capsule.json`
- `project/runs/2026-07-10-watchdog-three-architecture-orchestra/discovery-and-integration-plan.md`
- `project/agentic-stack.md`
- `project/workflows/langgraph-controller.yaml`
- `project/workflows/crewai-crew.yaml`
- `project/workflows/llamaindex-rag.yaml`
- `project/agents/agent-roster.yaml`
- `project/agents/skills-governance.md`
- `project/provider-setup.md`
- `docs/dashboard-operating-manual.md`
- `api/_jarvis_contract.py`
- `services/jarvis-api/app.py`
- `project/runs/2026-07-10-watchdog-supervisor-integration-review/specialist-findings.md`
- `project/runs/2026-07-10-watchdog-supervisor-integration-review/external-action-status.md`

## Stage Architecture Recommendation

Treat these as roles with compatible runtime implementations, not as a hard one-runtime-per-role division. Current runtime proof and authorization determine whether a compatible runtime may fulfill the role.

| Stage | Required role | Current safe implementation | Promotion gate |
|---|---|---|---|
| Classify, assemble CAG, contract, stop | Watchdog | Planned Hermes policy or a compatible read-only controller | Independent review; no self-approval of high-risk output |
| Intake, bounded retrieval, artifact production | Executor | Codex-operated local work and static/browser-local packets | Claimed scope, approved corpus, task contract, evidence artifact |
| Technical/source checks | Verifier | Deterministic checks or a separate compatible reviewer | Maker/verifier separation for high-risk output |
| Claims, secrets, external-action boundary | Safety reviewer | AF Review plus focused public-safety scan | Block unsupported claims and unapproved side effects |
| Reconcile contradictions and decide | Integrator | Codex/lead integrator | Evidence-backed merge recommendation; preserve gaps |
| Provider, deployment, or writeback | External-action role | Disabled pending a separate approved backend or operator lane | Target, schema, secret boundary, budget/ledger, rollback, owner approval, and fresh proof |

FACT: `project/agentic-stack.md` correctly keeps Hermes non-executing and makes Codex the current operator boundary. `project/workflows/langgraph-controller.yaml` already encodes maker/verifier separation and a planned watchdog controller. The correction needed is wording that could be read as assigning execution capability permanently to a named runtime instead of assigning it to a controlled role.

INTERPRETATION: Retaining the non-executing Hermes safety boundary while allowing a compatible, independently reviewed runtime to fulfill a role preserves safety and avoids an obsolete hard division.

## Current-State Claims To Preserve

- Jarvis/dashboard: static/browser-local dashboard and provider-disabled review-packet APIs are the accepted current architecture. Browser-local configuration is a candidate packet, not a source-file or external-write mechanism.
- Jarvis voice: disabled. The current contract returns a disabled-mode packet; do not imply transcription, TTS, raw-audio storage, or voice capture.
- Always-online: Railway is a future lane, not current proof. Vercel is only documented as the static dashboard and provider-disabled serverless contract. Hosted freshness remains unverified in this branch.
- OpenRouter: no active provider runtime. `OPENROUTER_MODEL` must be explicit; `openrouter/auto` must not be reintroduced. The current API packet exposes a budget guard but no canonical provider-call ledger or actual-spend write path.
- Yushchenko: an observer and preflight/review role for model choice, tokens, budget, and ledger gaps; not an execution or approval bypass.
- CrewAI Level 3: deterministic public-safe fixture proof exists, but it is not default or provider-backed runtime proof.
- Railway/deploy: only the service root may be prepared for a future deployment; deploy action and hosted checks remain separately approved work.

## Required Gates

1. Build the CAG core and bounded retrieval capsule before broad or role-based execution.
2. Create a task contract with owned files, inputs, outputs, stop conditions, and evidence requirements before executor assignment.
3. Keep maker, verifier, safety reviewer, and integrator responsibilities independently reviewable; a maker cannot approve its own high-risk output.
4. Require explicit owner and provider approval, server-side secret handling, sanitized input, an explicit fresh model selection, budget caps, a canonical append-only provider-call ledger, and AF Review before any OpenRouter call.
5. Before a Railway or production claim, prove the exact deployed service boundary, health endpoint, auth/CORS policy, logs, provider-disabled baseline, rollback path, and current hosted result. Do not use a historical baseline as current freshness proof.
6. Before Notion, Linear, GitHub, WikiLLM, Telegram, or other durable/external writeback, require target/schema/idempotency/approval evidence and a public-safety review.
7. Run duplicate-skill and hook-governance audit before any skill or hook edit; do not introduce a new skill for a one-off method.
8. Merge only after a branch report records changed/proposed files, diff summary, checks, evidence sources, blockers, and `approve`, `revise`, or `block`.

## Source Evidence Needed Before Implementation Claims

No web/provider action was taken by this planner. The executor or verifier must refresh drift-prone public facts immediately before they are cited or used in a configuration decision:

- OpenRouter API and model catalogue/pricing: <https://openrouter.ai/docs/api-reference/overview> and <https://openrouter.ai/models>.
- Railway service/deployment and healthcheck guidance: <https://docs.railway.com/guides/healthchecks> and <https://docs.railway.com/guides/services>.

Use the URLs as cited public sources only after the role records the access date and the exact claim supported. Do not copy credentials, account details, private deployment targets, or dynamic price tables into public artifacts.

## Precise Recommended File Changes

| File | Recommendation | Acceptance criterion |
|---|---|---|
| `project/agentic-stack.md` | Add a concise role-to-compatible-runtime statement and a stage reliability matrix. Normalize `default_runtime` wording so disabled review packets cannot imply an active OpenRouter route. | Roles, proofs, and gates are distinguishable; no current-provider or always-online claim appears. |
| `project/workflows/langgraph-controller.yaml` | Add explicit role fields for executor, verifier, safety reviewer, integrator, and external-action owner. Add a decision edge that blocks external action without the full gate packet. | YAML parses; maker/verifier separation and terminal blocked state are explicit. |
| `project/workflows/crewai-crew.yaml` | Align named team definitions with role-based compatibility, Yushchenko observer-only responsibility, and canonical provider-ledger prerequisite. | YAML parses; no role bypasses Codex/AF Review gates. |
| `project/agents/agent-roster.yaml` and `project/agents/skills-by-agent.md` | Clarify that named agents describe role contracts, not permanent runtime claims; add merge/review responsibilities and ledger ownership only if an existing role covers them. | Duplicate-skill/hook audit finds no redundant skill; role/skill mapping remains consistent. |
| `project/agents/skills-governance.md` | Add the branch-review/merge evidence requirement only if absent after audit. Do not create a new skill. | Governance text preserves existing shared-skill boundaries and hook limits. |
| `project/provider-setup.md` | Replace any potentially stale model/provider descriptions with an explicit fresh-check policy, model-choice record, budget caps, ledger, server-side-only secret boundary, and activation sequence. | Provider status remains disabled; no secret or current pricing is stored. |
| `docs/dashboard-operating-manual.md` | Tighten Jarvis local/static, Vercel contract, Railway future-lane, disabled voice, and always-online status language; specify review/merge handoff behaviour. | Manual does not claim current hosted health or durable workers without new proof. |
| `api/_jarvis_contract.py` and `services/jarvis-api/app.py` | Avoid changing provider execution in this branch unless an executor has a safe test plan. If changed, return explicit disabled status by default, distinguish configured budget from measured spend, and require a canonical ledger writer before an executed-provider success status. | Python compile and Jarvis contract smoke pass; no network call occurs during checks. |

## Branch Acceptance Criteria

- All Branch A edits remain within the allowed file list and are public-safe English.
- Documentation presents named figures and systems as roles/states with compatible runtimes, while retaining independently enforced safety gates.
- The stage matrix distinguishes configured, locally proven, provider-disabled, future, and freshly hosted-verified states.
- Jarvis/dashboard wording matches static/browser-local and provider-disabled behaviour; voice remains disabled.
- OpenRouter policy names an explicit fresh selection, model route, budget cap, ledger, and observer/review path; no active runtime is claimed.
- Railway packet lists deployment prerequisites without deployment or hosted-freshness claim.
- Skills/hook audit evidence precedes any governance edit.
- Relevant Markdown/YAML/Python/JS checks, `git diff --check`, and focused public-safety review are recorded by the verifier.

## Planner Recommendation

Recommendation: revise before merge. The existing contracts contain most gates, but repeated `default_runtime` and named-runtime wording needs a focused reconciliation so disabled review packets cannot be misread as active OpenRouter or always-online capability. No implementation or external action is authorized by this planning evidence.
