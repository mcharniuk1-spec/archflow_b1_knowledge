# ArchFlow Knowledge Base Split

Date: 2026-07-03
Status: E1.6 review-ready public-safe structure

## Purpose

This folder defines the public-safe split between the primary operator knowledge base and the collaborator knowledge base. It is a routing layer, not a raw source archive.

The split exists so each operator/agent can keep role-specific context, decisions, questions, and handoffs without mixing private notes, credentials, raw transcripts, or unreviewed claims into the public project.

## Folders

| Folder | Role | Write rule |
|---|---|---|
| `primary-operator/` | Lead operator context, decisions, approvals, final integration notes | Reviewed summaries only |
| `collaborator/` | Collaborator-agent context, open questions, review notes, and handoff instructions | Reviewed summaries only |

## Common Rules

- Keep all text English-only.
- Use public-safe role labels, not private personal names.
- Do not store raw transcripts, private documents, private URLs, account IDs, screenshots, credentials, or API keys.
- Store only summaries, decisions, questions, gaps, task candidates, and links to public-safe repo artifacts.
- Promote durable facts to WikiLLM only after review.
- Treat Notion, private vault notes, and raw meeting files as source zones, not public storage.

## Relationship To Epic 1

E1.6 is complete for review when this split exists, each folder has instructions, and the dashboard/report state points future agents to the correct role boundary. It is not a new raw-memory system and it does not replace WikiLLM, Obsidian, Notion, or the public run notes.
