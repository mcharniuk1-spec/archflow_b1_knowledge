# Skills And Methods Used

This project uses the following skills and methods.

## Used In This Setup

| Skill or Method | Use |
|---|---|
| Notion spec-to-implementation | Read the private project board and convert it into an implementation plan. |
| Notion knowledge capture | Extract reusable project knowledge without copying private raw content. |
| [`archflow-task-breakdown`](archflow-task-breakdown/SKILL.md) | Break ArchFlow epics and parent tasks into staged subtasks, gates, and public-safe execution outputs. |
| [`archflow-e1-runtime-guard`](archflow-e1-runtime-guard/SKILL.md) | Validate the E1 runtime spine and connect the saved skill workflow to the Git pre-push hook. |
| [`evening-skill-registry-update`](evening-skill-registry-update/SKILL.md) | Keep registry files, handout hook wiring, and run-note targets synchronized for recurring maintenance. |
| [`daily-public-project-review`](daily-public-project-review/SKILL.md) | Review daily skill use, RAG/KB drift, and recurring inefficiency patterns before the next cycle starts. |
| [`priority-task-operator`](priority-task-operator/SKILL.md) | Select highest-priority actionable task by urgency and importance, create a PitAgent handoff packet, and prepare KB/Notion/GitHub follow-up evidence. |
| [`task-handout`](task-handout/SKILL.md) | Produce readable human summaries and copy-ready continuation prompts after substantial executions. |
| [`outquestions`](outquestions/SKILL.md) | Report what changed after each substantial execution and list the decision questions required before the next stage. |
| ArchFlow resetup contract | Preserve the June 24 company reset and Block 1 direction. |
| Loop Engineering operating contract | Keep agent workflows bounded with state, attempt caps, budget, maker/checker separation, and stop conditions. |
| Market evidence engine | Turn E2 into account universe, public-signal extraction, scoring, role verification, and reviewed ICP/output handoff. |
| Public-safety review | Keep public files free of secrets, personal data, local paths, and private IDs. |
| Ollama local check | Start local Ollama, list models, and run public-safe smoke tests. |
| Git publication flow | Initialize and publish only the public project folder. |

## Planned For Execution

| Skill or Method | Use |
|---|---|
| AF Graph | Run controlled Block 1 workflows. |
| AF RAG | Query approved project knowledge. |
| AF Crew | Split work across named agent roles. |
| AF Research | Build evidence cards, pain maps, ICP scorecards, and target shortlists. |
| AF Copy | Draft positioning, content, and outreach only from approved evidence. |
| AF Review | Approve or block output before handoff. |
| E1 runtime guard | Pre-push runtime validation for workflow YAML, LangGraph, LlamaIndex, CrewAI, and saved skills. |
| Outquestions | End each substantial run with next-stage decision questions, gates, risks, and a clear nontechnical report. |

## Inefficiency And Relevance Controls

For recurring daily maintenance and retrospective lanes:

- Do not use broad search or full-folder reindexing as the default proof of correctness.
- Do not re-run full retrieval index generation unless corpus source files changed.
- Do not run full `graphify` refresh or browser automation in registry-only maintenance.
- Do not treat provider checks or model-provider probes as registry evidence.
- Do not include full-stack model-efficiency or provider evidence collection in this lane unless execution actually changed provider/runtime contracts.
- If an approach is repeatedly non-impactful across three scheduled runs, mark it as "do not repeat without exception" and move the constraint to wiki memory in `wiki/insights.md`.

Allowed default checks are:

- targeted file diffs,
- YAML/JSON parse on edited files,
- hook alignment checks,
- concise run-note generation for no-op or changed states.

## Lane-Specific Irrelevance Blacklist (Not to Reuse by Default)

- `playwright` for registry-only runs.
- `curl`/REST smoke in this lane when no endpoint change occurred.
- broad `graphify` refresh for no-source-change cycles.
- model-provider calls in registry and retrospective review lanes.
- full-repo scans for already scoped daily changes.

## Agent Roles

| Role | Output |
|---|---|
| Tools Analyzer | Source inventory, extraction plan, tool gaps. |
| Context Analyzer | Context digest, facts, interpretations, hypotheses, gaps. |
| Manager / PRD Agent | PRD, backlog, owner matrix, metrics. |
| Research Agent | Account evidence cards, competitor gaps, pain maps, ICP scoring. |
| Knowledge Agent | KB update packet and memory candidates. |
| Copy Agent | Website positioning, content angles, outreach drafts, proposal copy. |
| Reviewer | Final approval or blocked status. |
| Evening registry automation | Skill registry refresh, validation, and run-note upkeep. |
| Task handout | Agent-readable handoff prompt and human execution summary after large runs. |
| Outquestions reporter | Decision questions and stage gates after each substantial execution. |

## Per-Agent Skill Registry

See `project/agents/skills-by-agent.md`.

This project intentionally publishes only the skills used or set up for ArchFlow agents. It does not publish the operator's full private skill inventory.
