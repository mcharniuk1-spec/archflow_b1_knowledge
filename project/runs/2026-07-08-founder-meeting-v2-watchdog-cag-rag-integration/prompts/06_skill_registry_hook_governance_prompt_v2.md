# Skill Registry And Hook Governance Prompt v2

Use this when adding, updating, or reviewing ArchFlow skills.

## Goal

Make skill use explicit, deduplicated, role-aware, and reviewable.

Hermes, Codex, AF Review, and AF Knowledge may inspect all skills. Bounded subagents receive only their role-specific skills and shared coordination rules.

## Read First

- `project/agents/skills-governance.md`
- `project/agents/skills-by-agent.md`
- `project/agents/agent-roster.yaml`
- `skills/skills-used.md`
- relevant `skills/*/SKILL.md`
- `.codex/hooks.json`
- hook scripts if hook behavior changes

## Add Or Update A Skill Only If

1. No existing skill covers the same job.
2. The skill has a unique name.
3. `SKILL.md` defines purpose, when to use, forbidden actions, evidence, validation, owner role, and examples.
4. The skill is mapped to roles.
5. The hook trigger is documented if mandatory.
6. AF Review passes.

## Required Outputs

- Duplicate-skill audit.
- Proposed registry changes.
- Role-specific skill map.
- Hook recommendation or patch.
- Validation checks.
- Run handout update.

## Forbidden

- No automatic new skill creation from one run.
- No raw prompt storage.
- No broad rewrite of all skill files to backfill a checklist.
