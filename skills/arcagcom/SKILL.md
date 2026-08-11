---
name: arcagcom
description: Coordinate parallel or role-based ArchFlow work with public-safe file claims, state updates, handoffs, and conflict stops. Use before shared-file edits, multi-agent execution, reviewer handoff, integration, Git closeout, or any task that needs the dashboard Communication Center or a portable local coordination packet.
---

# Arcagcom

Coordinate active work without depending on a tracked live log or a project-history archive.

## Choose the communication surface

Use one of these surfaces and name it in the task contract:

- **Communication Center:** use the dashboard `#communication` view for browser-local intake and handoff. Treat it as a local projection, not a durable runtime, approval, or external write.
- **Portable packet:** validate a JSON packet against [communication-packet.schema.json](references/communication-packet.schema.json) and save it only to a caller-supplied output directory that is ignored by Git.
- **Inline-only:** return the same fields in the active conversation when no safe local output directory was supplied.

Before writing under the repository, confirm the target is ignored with `git check-ignore -- path/to/output`. If the check fails, use inline-only mode or stop with a GAP. Never create a new tracked coordination directory by default.

## Starting packet

Publish `state: starting` before editing. Include:

- bounded task and role;
- claimed files and allowed actions;
- forbidden actions and authority boundary;
- expected output;
- known blockers;
- next safe action.

Claim only the files needed for the task. If another active packet claims the same file, stop and coordinate before editing.

## Update packet

Publish `state: update` before expanding scope, touching a newly shared file, changing an evidence claim, or approaching an action that needs separate approval. Preserve the original packet ID or link it through `parent_packet_id`.

The packet records coordination; it never grants authority. Provider calls, credential access, deployment, Git push, external writeback, destructive cleanup, or production changes still need their own approved contract.

## Completion packet

Publish `complete`, `blocked`, or `handoff` with:

- changed files and evidence references;
- checks run and their results;
- checks skipped with reasons;
- remaining gaps and gates;
- next safe action.

For a substantial handoff, use `task-handout` with the same caller-supplied ignored output directory or return the handout inline. Do not route the handout into tracked run archives.

## Public-safety boundary

Use repository-relative references in packet content. Never include secrets, credential values or presence, private URLs, local absolute paths, account identifiers, raw private source text, screenshots, transcripts, browser logs, or personal identities.

The Communication Center and portable packets may summarize an approved public source boundary. They must not ingest, fetch, clone, send, approve, deploy, publish, or mutate an external system.

## Integration checks

Before closeout:

1. Reconcile active packets and confirm every claimed shared file has one current writer.
2. Confirm makers did not approve their own high-risk output.
3. Run the smallest relevant syntax, schema, safety, and workflow checks.
4. Run `git diff --check` when repository files changed.
5. Record any external-action or provider gate as pending unless current readback evidence proves completion.

Do not force a Git update or delete a branch merely because coordination packets are complete.
