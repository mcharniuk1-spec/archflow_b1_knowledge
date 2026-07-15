# Decision: Report First, Agent Control Second

Date: 2026-07-15

Status: accepted for the current public/static surface

## Decision

The public dashboard and Jarvis must prepare a source-bounded Knowledge Service report before presenting an Agent Control handoff. The handoff reuses the report ID and source boundary, rather than re-ingesting or copying raw context.

## Rationale

The sequence makes provenance, reviewer questions, gaps, and authority visible before roles/tools/files are proposed. It also avoids a UI that looks like it can create an autonomous agent system from an unreviewed prompt.

## Consequences

- Guest preview is held at Agent Control until a local knowledge report exists.
- Admin/Guest remains browser-local and is not authentication or durable user memory.
- Downloads are local proposals; proposed files are marked for operator review and remain uncreated.
- Provider, Git, deployment, database, and external writeback stay behind separate approval/capability gates.
