# Functional Roles and Portable Skills

This directory is the human-readable projection of the canonical role contract in `project/system/contracts/role-catalog.json`. It contains 21 responsibility roles. They are jobs to be activated by a bounded case, not personalities, permanent processes, provider assignments, or independent authority.

The machine catalog remains authoritative for each role's goal, owned output, allowed tools, permission ceiling, forbidden actions, reviewer route, and handoff. `agent-roster.yaml` mirrors only the stable presentation fields: ID, title, lane, permission mode, packaged skills, and membership in the four smallest-responsible role packs.

## Four role packs

`actionable-role-packs.json` defines the reusable distributions. Choose the smallest pack that covers the requested outcome:

| Pack | Use it for | Required result |
|---|---|---|
| `research_to_decision` | Source-bounded research for a named decision | Source-linked facts, interpretations, hypotheses, gaps, and review |
| `definition_to_task_graph` | Goal, architecture, and task definition | Testable goal, sole-writer ownership, gates, checks, and handoff |
| `responsive_product_change` | A bounded product or interface change | Claimed implementation, deterministic verification, independent review, and integration |
| `reviewed_memory_update` | A reusable knowledge update | Provenance-bearing solution or action-memory candidate with freshness and supersession rules |

An individual can coordinate several contracts, but a high-risk maker cannot approve the same output. A team can bind different people or compatible runtimes to the same role IDs. In both modes, the case contract supplies authority and exact targets; the roster does not.

## Packages versus methods

The repository includes exactly ten portable skill packages, each backed by a `skills/<id>/SKILL.md` contract. They can be assigned only where the canonical catalog lists them. Terms such as source verification, acceptance-criteria writing, dependency mapping, or responsive testing are method capabilities. A method name does not claim that an additional skill package or tool is installed.

See `skills-by-agent.md` for the exact package-to-role projection and `skills-governance.md` for admission, validation, output, and deactivation rules.

## Operating path

Prepare an approved case in **Project** or Jarvis, inspect the proposed roles in **Roles & Skills**, and pass the packet through the dashboard **Communication Center**. Local artifacts may be written under ignored `project/local/` paths. Provider calls, external writes, publication, deployment, Git actions, and durable knowledge promotion stay behind their separate approval, review, rollback, and readback gates.
