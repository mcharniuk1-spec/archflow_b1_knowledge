# Dashboard Operating Manual Review

Date: 2026-07-15

Status: independent review findings reconciled into the current public/static scope

## Review method

Three read-only sidecar reviews inspected separate surfaces before integration:

1. Dashboard information architecture, interaction states, and static truth labels.
2. Jarvis input/report/download/API-boundary behavior.
3. Public skill portability, role coverage, and catalog accuracy.

The integrator owned implementation, merge order, validation, and this final reconciliation. Reviewers did not edit shared public files, install tools, call providers, or perform external writes.

## Findings and disposition

| Finding | Disposition | Evidence |
|---|---|---|
| The dashboard was strong as a static architecture map but not documentation-first enough. Inputs did not consistently state purpose, storage, example, and limitation. | Implemented. `#manual`, `#config`, and the two detailed workflow views now include explanatory paragraphs/tables and exact persistence boundaries. | `project/dashboard/app.js`, `docs/dashboard-operating-manual.md` |
| A strategic-plan navigation/link surface conflicted with the requested developer-operating manual. | Removed from dashboard header, navigation, command route, rendered route, source links, generated dashboard corpus direct entries, and static-smoke acceptance. The strategy document remains a repository artifact, not a dashboard page. | `project/dashboard/index.html`, `app.js`, generator, static smoke |
| Admin/Guest could be misunderstood as authentication or durable individual memory. | Implemented as explicit browser-local preview mode only. Guest requires local Knowledge Service preparation before Agent Control and hides API/token/catalog controls in Jarvis. | `app.js`, `jarvis.html`, `jarvis.js`, operating manual |
| Knowledge Service and Agent Control did not share a clear report handoff. | Implemented a shared browser-local activity contract containing mode, knowledge report ID/state, agent-control report ID/state, and last local report. | dashboard/Jarvis localStorage contract |
| Jarvis did not explain required inputs or produce/download a local architecture report. | Implemented report-first interaction, field-level help, local Markdown/JSON downloads, FACT/INTERPRETATION/HYPOTHESIS/GAP output, and suggested files marked as proposals. | `jarvis.html`, `jarvis.js` |
| Jarvis automatically loaded the public model catalog and could expose too much packet context to an optional API call. | Fixed. Catalog loading is explicit and Admin-only. Optional guarded review sends a minimal status descriptor, never the local report body, project reference, source boundary, or chat history. | `jarvis.js`, static smoke source assertions |
| Public role presentation covered only the small CrewAI fixture rather than the full public roster. | Fixed. Generator emits all 21 declared public role contracts; dashboard/manual renders role, mode, skills, outputs, and forbidden actions. | `project/agents/agent-roster.yaml`, `project/database/role-catalog.json` |
| Public skill usage could be mistaken for measured activity; two workflow responsibilities lacked packaged public contracts. | Fixed. Catalog labels documentation references separately from `verified_invocations`. Added and validated `archflow-knowledge-service` and `archflow-agent-control`; public package count is 12. | `skills/`, skill catalog, governance records |
| Dashboard API-base input allowed an arbitrary origin. | Fixed. Dashboard and Jarvis now accept same origin or HTTP loopback only. | `project/dashboard/app.js`, `jarvis.js` |

## Acceptance evidence

- Both new skill contracts passed the project-runtime skill validator.
- Dashboard and Jarvis JavaScript parse.
- Jarvis service and generator Python parse.
- Generated dashboard data, skill catalog, and role catalog parse as JSON.
- Public safety, workflow, guarded API, serverless owner-guard, runtime guard, and final diff checks pass.
- Permitted headless smoke renders ten dashboard routes and the Jarvis report/download contract with provider calls and writeback at zero.

## Remaining gaps

- Admin/Guest is not authentication, authorization, or a multi-user memory system.
- A static report is not repository ingestion, real knowledge-base writeback, sub-agent creation, or a provider/model execution receipt.
- A live state display requires a verified runtime event feed with run/node/timestamp/evidence/authority/writeback fields.
- Provider efficiency, durable spend/replay control, production backend, database, private corpus, and external writeback remain separate gated work.

## Review verdict

Accept for the current public/static documentation, local report, role/skill catalog, and browser-local handoff scope. Do not upgrade this verdict to provider execution, persistent runtime, external action, or multi-user product readiness.
