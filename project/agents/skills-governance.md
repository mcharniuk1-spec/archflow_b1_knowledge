# Skills Governance

Status: active governance policy.

This file defines how ArchFlow skills are reviewed, mapped, and passed to agents.

## Core Rule

Do not create a new skill because a method appears once. Add or update a skill only when repeated evidence shows the method is reusable, no existing skill covers the same job, and AF Review can verify the scope.

Hermes, Codex, AF Review, AF Knowledge, and an assigned skills-governance reviewer may inspect all skills. Bounded subagents receive only the role-specific skills needed for their task plus shared coordination rules.

## Current Contracted Skills

These have project-local `SKILL.md` contracts or are project-recognized skill contracts:

- `arcagcom`
- `archflow1`
- `archflow-task-breakdown`
- `archflow-e1-runtime-guard`
- `daily-public-project-review`
- `evening-skill-registry-update`
- `outquestions`
- `priority-task-operator`
- `task-handout`

## Shared Project Skills

- `arcagcom`: live communication, file claims, handoffs, and merge gates.
- `archflow1`: dashboard/Jarvis/runtime/provider/Railway boundaries.
- `task-handout`: durable run handout and continuation prompt.
- `outquestions`: owner decisions, blocked gates, and next-stage questions.

Shared does not mean universal execution authority. Shared skills carry coordination and closeout context; task execution still follows the assigned role contract.

## Role-Specific Visibility

| Role | Skill visibility |
|---|---|
| Hermes Watchdog | May inspect all skills; uses classification, context capsule, task contract, evidence review, and stop rules only. |
| Codex / Lead Integrator | May inspect all skills; edits and validates files within claimed scope. |
| AF Review | May inspect all skills for safety, evidence, and duplicate checks. |
| AF Knowledge | May inspect all skills for KB promotion and memory candidates. |
| AF Discovery | Discovery, JTBD, 90-day stories, customer forces, source boundary, shared coordination. |
| AF PRD Architect | PRD, evidence-backed requirements, DoD, acceptance criteria, review packet, shared coordination. |
| AF Task Translator | `archflow-task-breakdown`, task packets, Notion-ready Markdown, blocker/approval gates, shared coordination. |
| AF Publisher | Publication review, Git-ready packets, `task-handout`, `outquestions`; external publication remains owner-gated. |
| Bounded subagent | Only the skills named in its task contract. |

## Role / Runtime Separation

Roles define authority, evidence, and forbidden actions; they do not reserve work for one named model, framework, or agent brand. A compatible runtime may fulfil watchdog, executor, verifier, safety-reviewer, integrator, or external-action roles only when its task contract grants the same bounded authority and it meets the evidence gates for that role.

- The watchdog role remains non-executing even when fulfilled by a compatible controller.
- Maker and verifier remain separate for substantial work.
- A safety reviewer must be independently assigned for public-safety and claim review.
- The current Codex operator is the active local executor and final integrator, but that assignment is not an automatic provider/runtime activation.
- An external-action role is disabled by default and needs action-specific owner approval, target proof, and post-action verification.

## Governance Audit - 2026-07-10

Scope: duplicate-skill and hook-governance audit before this Branch A architecture update. Result: the nine discovered project-local `SKILL.md` contracts match the current contracted-skill registry; no duplicate contract or unregistered mandatory hook was identified. No skill or hook file is added, removed, or edited by this branch.

## Add-Skill Checklist

- Unique name.
- No existing skill covers the same job.
- Purpose and trigger conditions are explicit.
- Forbidden actions are explicit.
- Evidence and validation requirements are explicit.
- Owner role is named.
- Examples or expected output shape are included.
- Role mapping is added to `project/agents/skills-by-agent.md`.
- Machine-readable mapping is added to `project/agents/agent-roster.yaml` when relevant.
- Hook trigger is documented if mandatory.
- Public safety scan and relevant parses pass.
- Run handout records the change.

## Hook Governance

The hook is a reminder system, not an automation authority. It may emit reminders for task handouts and skill-governance prompts. It must not store raw prompts, create skills automatically, rewrite `SKILL.md`, or mutate external systems.

Skill-governance prompts should trigger an audit before edits when they ask to add, update, deduplicate, route, or govern skills or hooks.

## Duplicate Boundaries

- `task-handout` records durable handoff and continuation context.
- `outquestions` records owner decisions and next-stage gates.
- `arcagcom` coordinates live active work.
- `evening-skill-registry-update` syncs registry/hook maintenance.
- `daily-public-project-review` performs day-level retrospective.
- `archflow1` records dashboard/Jarvis/runtime boundaries.
- `archflow-e1-runtime-guard` validates the runtime spine before push.

Do not remove shared usage just because multiple roles list the same shared skill.
