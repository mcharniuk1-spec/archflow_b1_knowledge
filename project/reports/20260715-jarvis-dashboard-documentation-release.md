# Jarvis and Dashboard Documentation Release

Date: 2026-07-15

Status: public/static release evidence; publication result appended after Git and Vercel verification

## Scope

This report records a documentation-first update to the public landing page, Dashboard, and Jarvis. It preserves the current visual language and existing product information while making the operating method, fields, outputs, controls, state animation, and runtime boundaries easier to understand.

## Delivered interface changes

### Jarvis

Jarvis now leads with a four-stage operating sequence: define the request, prepare a Knowledge Service report, create an Agent Control handoff from that report, and hand a reviewed package to an authorized operator. Every request field explains its purpose, storage, example use, and limit. The page explains Administrator and Guest preview, report and JSON-handoff downloads, model candidates, API base, owner-token constraints, and why an optional guarded review is not a provider-execution claim.

The former set of separate access, route, catalog, and truth-boundary panels is now one reference area. This keeps advanced controls available but visually subordinate to the documented workflow.

### Dashboard

The Dashboard defaults to the operating manual. The manual is continuous developer documentation for the repository, Knowledge Service, Agent Control, parallel coordination, Admin/Guest preview, knowledge layers, configuration parameters, public skills, role contracts, Jarvis prompts, data preview, and FAQ. Detailed views retain their dedicated explanations for workflow editing, retrieval, architecture layers, configuration, and evidence.

The visible execution sequence continues to distinguish idle, active, and completed browser-local stages. A stage light or movement represents local packet preparation only; it is not a live-agent claim.

### Landing page

The existing public product story remains intact. Its navigation and system-delivery copy now explicitly direct evaluators to the documentation path before they open controls.

## Consistency correction

FACT: Jarvis already required a Knowledge Service report before Agent Control, but the Dashboard allowed Administrator preview to begin Agent Control without that report.

Resolution: both Dashboard modes now require `prepared_local` Knowledge Service state before Agent Control starts. This preserves the explicit sequence: source-bounded context first, bounded agent design second, human-reviewed execution outside the static surface.

## Validation evidence

- public safety scan: passed;
- workflow validation: passed;
- runtime guard: passed;
- Jarvis API contract smoke: passed with provider calls and writeback at zero;
- serverless owner-guard smoke: passed;
- rendered static smoke: passed for ten dashboard routes and Jarvis with provider calls and writeback at zero;
- desktop visual inspection: passed for Jarvis and Dashboard layouts.

## Known limits

The release does not add authentication, individual persistent memory, private-repository retrieval, provider execution, cost telemetry, durable storage, database writes, agent launch, Git changes, deployment controls, or external writeback. Those remain subject to independent capability proof and approval.
