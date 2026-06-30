# Run: Onyx Dashboard Voice Hosting Execution Plan

Date: 2026-06-30
Status: planned, task-created, repo-updated

## Task

Turn the June 30 Onyx, live dashboard, voice layer, and hosting plan into executable project structure:

- create Notion tasks for the dashboard/voice/hosting plan
- create a separate GloomyLord task for PRD, research templates, monitoring templates, backlog, ideas summary, and visual social report design
- add a reusable `outquestions` skill for execution reports and next-stage decision questions
- update the public GitHub project with a public-safe run record and decision baseline

## Execution Summary

The plan remains staged. ArchFlow stays the workflow brain; Onyx is not promoted into the core runtime. The next implementation path is a hosted read-only dashboard first, then a live API/worker service only when the state model, auth boundary, and secret policy are explicit. Voice starts local and read-only before any command can write to files, Notion, GitHub, deployments, outreach, or memory.

The dashboard direction follows the current project shape. The existing dashboard is static and generated from public project files, so the first live step is Vercel/static hosting. Railway becomes relevant only for always-on services such as run state APIs, background queues, websocket or server-sent-event streams, and voice/background workers.

The content/reporting direction is separated from the infrastructure direction. GloomyLord is assigned to define the PRD, research templates, daily/weekly monitoring templates, backlog, ideas summary, and project-step report design. The social reporting system must make task progress understandable through 1-6 slide public-safe carousels plus platform-specific post text.

## Decisions Recorded

FACT: ArchFlow remains the source-of-truth workflow and memory system.

FACT: The live dashboard is a control surface, not canonical memory.

FACT: GitHub stores source and public-safe examples only. Real credentials belong in provider secret stores or ignored local files.

INTERPRETATION: Vercel is the best first hosting target for the static dashboard; Railway is better for long-running agent API, worker, queue, and voice services.

HYPOTHESIS: A PAUL-style dashboard-builder role can speed up dashboard schema and analytics design if AF Review keeps it inside source, privacy, and evidence gates.

GAP: PAUL, CharlieOS, Onyx production, and external managed agents still need concrete runtime, credential, and retention review before adoption.

## Notion Tasks Created

The task board was updated with:

- `E1.3.9 - Live dashboard, voice layer, hosting, and Onyx execution plan`
- `E1.3.10 - GloomyLord planning package: PRD, templates, monitoring, backlog, ideas, and social reports`

The tasks are linked to the existing E1 epic in the private Notion workspace. Public GitHub notes do not include private page URLs.

## Skill Added

- `skills/outquestions/SKILL.md`

Purpose: after every substantial run, produce a short execution report plus the questions and gates needed to move reliably to the next stage.

## Immediate Next Steps

1. Confirm the dashboard publication boundary: public, private-link, or auth-gated.
2. Define the read-only dashboard build route and Vercel static hosting shape.
3. Define the live API/worker contract before using Railway.
4. Define the local voice skeleton commands and approval rules.
5. Let GloomyLord complete the template/reporting package before content generation starts.
6. Use `outquestions` after each execution to keep decisions explicit.

## Blocking Questions

1. Should the first hosted dashboard be public, hidden-link only, or auth-gated?
2. Should Railway wait until voice/background workers exist, or should the API skeleton be created earlier?
3. Should voice mode be push-to-talk only at first?
4. Which tasks are eligible for public social reports?
5. Who approves public-safe carousel text before publishing?

## Checks

- Public repo remained English-only for new files.
- No credentials, private Notion URLs, local paths, or raw screenshots were added.
- The new skill is registered in the public skill registry and agent skill map.
