# Dashboard Role Configuration

Status: source contract for Screen 2 role panels

## Editable Safe Fields

- role objective
- responsibility
- tools
- model route
- budget mode
- output artifact
- review gate
- status
- handoff target

Browser edits are candidates only. Source files are updated only through Codex or an approved backend endpoint.

## Required Roles

| Role | Primary responsibility | Default runtime state |
|---|---|---|
| Jesus | Lead integrator, merge order, final validation, Git push packet, handout | Codex operator |
| LOL | Dashboard UI/UX, Screen 1, Screen 2, role panels, composer, voice states, block schema controls | Codex operator |
| Ronaldinho | Backend/API, LangGraph, CrewAI, OpenRouter, env, Railway, voice, runtime claim review | Codex operator |
| Messi | Notion/GitHub/project closeout, E1/E1.3.9 status, report links, task evidence | Codex operator |
| Ronaldo | Product surface and ICP consistency | Codex operator |
| Yushchenko | Model budget, OpenRouter ledger, token/cost discipline | OpenRouter gated |
| Theory subagent | FreePRD, PRD theory, ICP theory, discovery-call theory | Codex operator |
| Security subagent | Env variables, Telegram migration, secret scan | Codex operator |
| Actor | Bounded implementation or review slice | Codex operator |
| AF Tools | Source/tool/runtime readiness | Codex operator |
| AF Knowledge | WikiLLM/public memory packets | Codex operator |
| AF Publisher | Git/deploy/release packet after approval | Gated |
| AF Review | Public-safety and claim review | Required gate |
| CrewAI role workers | Configured role/task workers and proof branch | proof_passed_not_default_runtime |

## Stages

Intake -> Role Assignment -> Active Work -> QA Gate -> Docs/Reports -> Git/Deploy -> Notion/Memory -> Final Decision.
