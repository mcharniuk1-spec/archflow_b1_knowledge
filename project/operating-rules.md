# Operating Rules

## Language Rule

All project knowledge, prompts, summaries, inputs, and outputs in this public folder must be in English.

If a source is in another language, translate it into English and store only the translated public-safe summary.

## Public-Safety Rule

Do not store:

- Personal names or private identities.
- API keys, tokens, cookies, passwords, private credentials, or credential values.
- Local absolute paths.
- User IDs, workspace IDs, account IDs, project IDs, deployment IDs, or private Notion page URLs.
- Raw private Notion exports, emails, transcripts, browser logs, screenshots, PDFs, office documents, or database dumps.
- Claims that imply paying customers, production outcomes, or validated ROI unless supported by public evidence.

## Folder Rule

All current project work goes under `project/`.

Pre-reset history goes under `history/` as summaries, timelines, and sanitized inventories only.

## Source Rule

Private sources can be read for understanding, but public files must contain only:

- English summaries.
- Public-safe task names.
- Public-safe dates and status.
- Tool names and non-secret model names.
- Repo-relative file references.

## Agentic Stack Rule

Use this layering:

- LangGraph controls path, state, routing, and review gates.
- CrewAI organizes named team roles and task handoff.
- LlamaIndex handles bounded retrieval and RAG.
- Codex remains the local operator and approval boundary.
- Ollama is the local model provider once approved and started.

## Approval Rule

Ask for approval before:

- Starting `ollama serve`.
- Creating a real `.env.local`.
- Running a model against non-public source text.
- Installing dependencies from the network.
- Writing outside this public folder.
- Publishing or pushing to a remote Git repository.
