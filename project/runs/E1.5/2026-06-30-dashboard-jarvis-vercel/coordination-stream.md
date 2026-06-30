# Coordination Stream: Dashboard Jarvis Vercel Shell

Date: 2026-06-30

## Parallel Agents

Content agent:

- Created the E1.5 content-template package under `project/content/templates/`.
- Added a content-template run summary and handout.
- Did not touch dashboard code.

Deployment/access sidecar:

- Confirmed current dashboard is static HTML/CSS/JS with generated `data.json`.
- Recommended deploying from the public repo root so `/project/dashboard/` links keep working.
- Confirmed Vercel hidden-link is acceptable only for public-safe read-only data.
- Confirmed Railway should wait for live API, SSE/websocket, voice execution, uploads, workers, private state, or durable writes.

Parallel integration thread:

- Reported that a local Mistral key exists in protected private files.
- Instruction applied: do not read, expose, copy, commit, or deploy secret-bearing files.
- Requested current E1.3/E1.4/E1.5/E2/E5 status and changed-file/blocker report before merge.

## Main Executor Work

- Added Jarvis dashboard shell.
- Added Vercel headers and deploy ignore file.
- Added root rewrites for `/` and `/dashboard`.
- Changed browser packets/events to session-only storage.
- Changed file intake to metadata-only packets.
- Regenerated dashboard data.
- Ran local HTTP and visual QA.
- Deployed a Vercel preview; unauthenticated route checks redirect to Vercel SSO.
- Canonical review route: `https://public-mcharniuk1-4994-mcharniuk1-4994s-projects.vercel.app/project/dashboard/`.
- Noted Vercel CLI side effect: an initial deploy without `--prod` landed as target `production`; the explicit `--target preview` deployment is the only review target.

## Merge Notes

- Public repo changes are in dashboard, content templates, run notes, and Vercel config only.
- Do not write deployment IDs, org IDs, local env values, or provider keys into public files.
- `Iam/langgraph/course-support` remains local planning state unless moved or tracked later.
- Coordinate before adding E2.0 docs to the public repo so generated dashboard activity and Notion status remain aligned.
