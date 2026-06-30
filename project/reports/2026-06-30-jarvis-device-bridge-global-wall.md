# Jarvis Device Bridge And Capture Global Wall

Date: 2026-06-30
Status: planned, not implemented
Scope: public-safe roadmap for dashboard, local operator state, voice/screen capture, and Codex/OpenAI bridge planning.

## Purpose

Create a reliable path for Jarvis to show where the active agent is running, whether a local operator bridge is connected, and how voice/screen capture can become task/report input without storing private raw material by default.

This wall does not enable live capture, model calls, deployments, or write actions. It defines the structure future agents should implement and review.

## Facts

- The current dashboard is a Vercel/static or static-enhanced visibility surface, not a live control plane.
- Codex is currently the local operator/editor/reviewer when Max runs it on his device.
- Codex app authorization is not an application API key and should not be copied into hosted services.
- OpenAI API use for application code requires an approved API key stored in a secret store or local private environment file.
- Voice and screen capture are private input channels and should default to transient processing plus reviewed summaries.

## Operating Interpretation

Jarvis should separate three states in the dashboard:

1. Static summary available: the dashboard can display last generated public-safe status.
2. Local bridge connected: Max's device is running an approved local bridge that can publish heartbeat/status and receive approved task packets.
3. Hosted model/backend active: a server-side backend and model provider are configured with approved secrets, policy, logging, and access control.

If Codex is not running locally, the dashboard must not pretend Codex is actively responding. It should show `offline`, `not connected`, or `last seen`.

## Planned Work Items

### JDB-1 - Dashboard Runtime State Panel

Add a clear dashboard panel for:

- dashboard mode: static, local bridge, hosted backend;
- local operator: Codex running, not running, last seen, current workspace;
- model provider: none, local, OpenAI, Mistral;
- queue state: idle, request pending, approval needed, executing, blocked;
- data source: generated JSON, local bridge heartbeat, backend API.

Acceptance criteria:

- Dashboard distinguishes static summaries from live state.
- The UI does not imply Codex is connected when no heartbeat exists.
- Public/shared views show only public-safe state.

### JDB-2 - Local Codex/Jarvis Bridge Contract

Define a local-only bridge that can run on Max's device when explicitly started.

Required fields:

- session id;
- workspace id;
- current thread/task state;
- heartbeat timestamp;
- allowed actions;
- approval status;
- sanitized event summary;
- output links.

Acceptance criteria:

- No raw Codex authorization is exposed.
- No automatic write action runs without approval.
- Requests from the web are queued for local approval unless explicitly allowed.

### JDB-3 - Voice And Screen Capture Policy

Plan a capture pipeline for calls and work sessions.

Default path:

- capture local audio/screen only after explicit start;
- transcribe locally or through an approved provider;
- summarize into facts, decisions, tasks, deadlines, owners, risks, and gaps;
- create task candidates in Notion and dashboard review queue;
- discard or privately retain raw material only under an explicit retention policy.

Acceptance criteria:

- Raw audio, raw transcripts, and raw screen recordings are not committed to GitHub.
- Summaries preserve source context and uncertainty.
- Capture state is visible: recording, transcribing, analyzing, waiting for approval, done, blocked.

### JDB-4 - Meeting-To-Tasks Flow

Design the PM-replacement workflow from a call or screen recording:

1. Capture input.
2. Transcribe and segment.
3. Extract decisions, tasks, deadlines, owners, dependencies, open questions, and risks.
4. Link tasks to project wall and Notion.
5. Ask for approval before persistence or assignment.
6. Update dashboard status and run note.

Acceptance criteria:

- Every task has owner, due date or gap, source summary, and confidence.
- The workflow separates facts from hypotheses.
- The dashboard shows what was created and what still needs approval.

### JDB-5 - OpenAI Provider Setup Gate

Use OpenAI only as an application model provider after secure setup.

Acceptance criteria:

- API key is created through the secure setup flow.
- Key is stored only in an approved local/private environment or provider secret store.
- `MODEL_PROVIDER=none` remains default until a task explicitly enables OpenAI.
- Provider calls over raw private capture are blocked unless Max approves the data class.

### JDB-6 - Notion And Knowledge-System Sync

Create Notion tasks and local run/decision/issue records from reviewed summaries.

Acceptance criteria:

- Notion receives reviewed tasks, not raw transcript dumps.
- WikiLLM/Obsidian receive durable decisions and summaries only.
- The dashboard displays the source path for each task/report.

## Dashboard Status Vocabulary

Use these labels consistently:

- `static_read_only`
- `local_bridge_offline`
- `local_bridge_connected`
- `codex_operator_running`
- `codex_operator_not_running`
- `model_provider_none`
- `model_provider_openai_ready`
- `voice_capture_disabled`
- `voice_capture_ready_local`
- `screen_capture_disabled`
- `screen_capture_ready_local`
- `approval_required`
- `blocked_missing_secret`
- `blocked_missing_auth`
- `blocked_policy_unapproved`

## Safety Boundary

Do not implement until these are decided:

- whether raw recordings may be stored;
- where local bridge state is stored;
- whether web requests can trigger local Codex actions directly or only create approval tasks;
- whether OpenAI may process sanitized capture summaries;
- whether a live backend is required now or after the static dashboard review.

## Recommended Next Step

Keep the current dashboard finalization lane focused. Start this bridge as a separate implementation lane after the current dashboard diff is reviewed and the access/auth gate is confirmed.