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

## Live Agent Communication Rule

All parallel or role-based ArchFlow public project work must use `project/live/communication/` as the shared active communication channel.

Before starting or continuing work, each agent must read:

- `project/live/communication/README.md`
- `project/live/communication/current-agent-notice.md`
- the latest entries in `project/live/communication/agent-communication-log.md`

Before editing files, each agent must append a short starting update to `project/live/communication/agent-communication-log.md` with the task, files likely to change, files claimed, expected output, blockers, and next step.

During work, agents must announce scope changes and coordinate before editing files another agent has claimed. After work, agents must append a complete, blocked, or handoff update with files changed, checks, gaps, and next action.

For substantial work, still create or update the relevant `project/runs/<run-id>/agent-handout.md`. The live communication folder coordinates active work; run handouts record durable completion state.

## Actor And Reviewer Rule

For substantial dashboard, website, provider, deployment, memory, or architecture work, Jesus/Codex must use an explicit Actor plus Reviewer split when subagent tools are available:

- Actor: owns a bounded implementation or planning slice with a clear file scope.
- Reviewer: audits evidence, safety, completion claims, and remaining gaps without editing files unless explicitly assigned a separate fix.

The lead integrator remains responsible for merge order, conflict review, validation, durable run notes, and final owner handoff. Actor and Reviewer file claims must be recorded in `project/live/communication/agent-communication-log.md` before edits.

## Task Handout Hook Rule

The project prompt hook checks every submitted prompt for handout triggers. If it emits `TASK_HANDOUT_HOOK_TRIGGER=required`, the active agent must read `skills/task-handout/SKILL.md` before continuing.

The skill is mandatory when:

- A prompt directly asks for a handout, handoff, continuation prompt, or hook trigger.
- The work uses one or more AF agents, agent roles, reviewer/helper agents, LangGraph plus CrewAI routing, or parallel/multi-agent execution.
- The work solves, updates, creates, reviews, or starts one or more subtasks.

The hook does not store raw prompt text and does not create handouts automatically. It writes only an ignored local trigger marker. The executing agent creates or updates `agent-handout.md` beside the relevant run artifacts after outputs and checks exist.

## Approval Rule

Ask for approval before:

- Starting `ollama serve`.
- Creating a real `.env.local`.
- Running a model against non-public source text.
- Installing dependencies from the network.
- Writing outside this public folder.
- Publishing or pushing to a remote Git repository.
