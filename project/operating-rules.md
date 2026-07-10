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

- Watchdog, executor, verifier, safety-reviewer, integrator, and external-action labels are role contracts rather than permanent runtime assignments. A compatible runtime may fulfil one only under a bounded task contract that preserves the role's authority, evidence requirements, and forbidden actions.
- Hermes is the current planned watchdog/controller/reviewer label. A compatible watchdog plans, classifies, assigns, reviews, and stops; it does not execute code, edit files, deploy, mutate task boards, activate providers, write externally, or approve its own high-risk output.
- CAG assembles stable project context before task-specific retrieval and subagent prompting.
- LangGraph controls path, state, routing, and review gates.
- CrewAI organizes named team roles and task handoff.
- LlamaIndex handles bounded retrieval and RAG; it is not durable memory.
- WikiLLM remains durable reviewed memory after promotion.
- Codex remains the current local executor, reviewer, file editor, validator, final integrator, and approval boundary. That current assignment is not an automatic provider, deployment, or external-action authorization.
- Ollama is the local model provider once approved and started.

## Watchdog Execution Rule

For broad, architecture, multi-agent, task-board, market/content/sales, provider, dashboard, or KB work, use a watchdog loop:

1. Classify execution type and risk.
2. Assemble CAG core from stable rules, roles, skills, architecture, E1-E7 state, and gated claims.
3. Retrieve task-specific RAG evidence only from the approved public corpus when needed.
4. Build a compact context capsule.
5. Create bounded task contracts before assigning subagents.
6. Require evidence before completion.
7. Accept, repair, split, escalate, or stop.

Maximum repair attempts per task: 3. If the same error appears twice, stop and escalate.

## CAG/RAG Source Rule

Approved default retrieval corpus:

- `project/`
- `history/`
- `skills/`
- `wiki/`

RAG results without repo-relative source paths are not evidence. Do not retrieve from or store raw private exports, local runtime data, secrets, private URLs, raw transcripts, screenshots, account IDs, deployment IDs, personal identifiers, or absolute local paths in public files.

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

For substantial dashboard, website, provider, deployment, memory, or architecture work, the lead integrator must use an explicit Actor plus Reviewer split when subagent tools are available. The current Codex/Jesus binding does not make runtime identity itself the authority for either role:

- Actor: owns a bounded implementation or planning slice with a clear file scope.
- Reviewer: audits evidence, safety, completion claims, and remaining gaps without editing files unless explicitly assigned a separate fix.

The lead integrator remains responsible for merge order, conflict review, validation, durable run notes, and final owner handoff. A compatible runtime may fulfil Actor, Reviewer, or Integrator only when the task contract keeps their file scope, maker-checker separation, evidence duties, and approval gates intact. Actor and Reviewer file claims must be recorded in `project/live/communication/agent-communication-log.md` before edits.

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
- Deploying, promoting production, mutating Notion, mirroring to Linear, sending Telegram, taking Railway action, syncing Figma, or performing any external writeback.
