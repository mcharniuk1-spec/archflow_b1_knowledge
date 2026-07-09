# Task Contracts

Run: `2026-07-08-founder-meeting-v2-watchdog-cag-rag-integration`

## Contract Template

- Title:
- Execution type:
- Goal:
- Context:
- Allowed files:
- Forbidden actions:
- Acceptance criteria:
- Required evidence:
- Maximum attempts:
- Stop condition:
- Expected output format:

## Architecture Reviewer

- Title: Architecture Reviewer
- Execution type: Discovery / Planning
- Goal: Review current LangGraph, CrewAI, Codex, Hermes, Jarvis, dashboard, CAG/RAG, writeback, provider, and Railway architecture.
- Context: Public project architecture and owner package are planning sources; runtime claims require repo evidence.
- Allowed files: `archflow_8_07/**`, `project/agentic-stack.md`, `project/workflows/**`, `project/agents/**`, `project/config/**`, `services/jarvis-api/**`, `api/**`, relevant reports/runs.
- Forbidden actions: edits, provider calls, deploys, pushes, external writeback.
- Acceptance criteria: return architecture delta, risks, file update recommendations, and evidence.
- Required evidence: repo-relative file references and clear claim boundaries.
- Maximum attempts: 1.
- Stop condition: missing source or need for external side effect.
- Expected output format: FACT / INTERPRETATION / HYPOTHESIS / GAP plus recommendations.

## Package Diff Analyst

- Title: Package Diff Analyst
- Execution type: Discovery / Planning
- Goal: Compare package files against repo state and detect duplication, conflicts, stale assumptions, and missing integration points.
- Context: Package is latest owner-approved planning source but must be adapted, not blindly copied.
- Allowed files: `archflow_8_07/**`, current public project architecture, workflow, agent, skill, task, content, report, and KB files.
- Forbidden actions: edits, mutation of package source, network, external writeback.
- Acceptance criteria: package-to-repo mapping table.
- Required evidence: package files inspected and repo targets.
- Maximum attempts: 1.
- Stop condition: missing source or private data exposure risk.
- Expected output format: mapping table plus conflicts/gaps.
- Outcome: timed out and closed; Codex completed the mapping locally.

## CAG/RAG Architect

- Title: CAG/RAG Architect
- Execution type: Planning / Architecture
- Goal: Define Controlled Context Assembly Generation plus bounded RAG.
- Context: CAG stable context capsules are distinct from task-specific RAG retrieval.
- Allowed files: `archflow_8_07/**`, `project/workflows/llamaindex-rag.yaml`, KB principle reports, current context/schema locations.
- Forbidden actions: edits, broad ingestion, private-source copying, provider calls.
- Acceptance criteria: schema/procedure updates and retrieval boundary rules.
- Required evidence: current RAG contract and package prompt/schema references.
- Maximum attempts: 1.
- Stop condition: missing source or unsafe data requirement.
- Expected output format: FACT / INTERPRETATION / HYPOTHESIS / GAP plus recommended structure.

## Skills Governance Reviewer

- Title: Skills Governance Reviewer
- Execution type: Planning / Governance
- Goal: Review current skills, role-specific skills, shared skills, duplicate skills, hook triggers, and new-skill admission rules.
- Context: Hermes/reviewers may inspect all skills; subagents receive role-specific skills only.
- Allowed files: `project/agents/**`, `skills/**/SKILL.md`, `skills/skills-used.md`, `.codex/hooks.json`, hook scripts.
- Forbidden actions: edits, automatic skill creation, raw prompt storage, broad rewrites.
- Acceptance criteria: duplicate audit, registry updates, hook governance recommendations.
- Required evidence: parse/check outcomes and file references.
- Maximum attempts: 1.
- Stop condition: duplicate cannot be reconciled safely.
- Expected output format: audit, recommendations, files to edit/avoid, checks.

## Service Operations Strategist

- Title: Service Operations Strategist
- Execution type: Planning / Documentation
- Goal: Define productized service company operating model and evidence handling.
- Context: Service-first, not SaaS-first; demand claims require E6/E7 evidence.
- Allowed files: `archflow_8_07/**`, `project/project-plan.md`, content/service docs, output templates.
- Forbidden actions: edits, pricing claims as proven, customer/demand overclaims.
- Acceptance criteria: operations model updates, QA gates, artifact package plan.
- Required evidence: package reports and repo task state.
- Maximum attempts: 1.
- Stop condition: missing owner decision for offer/pricing.
- Expected output format: operating model, offer ladder, QA gates, artifacts, onboarding, evidence rules.

## Market And Content Strategist

- Title: Market And Content Strategist
- Execution type: Sales/Content / Planning
- Goal: Update ICP, audience, competitor positioning, sales strategy, content engine, static templates, text posts, carousel templates, and 10% video rule.
- Context: Latest owner rule is 70% static educational/analytical, 20% carousel/checklist/template, 10% short video.
- Allowed files: `archflow_8_07/**`, `project/content/templates/**`, `project/project-plan.md`, market/content docs.
- Forbidden actions: publication, outreach, validated-demand claims, provider/runtime claims.
- Acceptance criteria: market/content/sales updates and template plan.
- Required evidence: current content library and package prompt/report references.
- Maximum attempts: 1.
- Stop condition: publication or outreach needed.
- Expected output format: positioning, competitor map, sales motion, content mix, target files.

## E1-E7 PM Reviewer

- Title: E1-E7 PM Reviewer
- Execution type: Task-Board Update / Planning
- Goal: Prepare Notion-ready E1-E7 task updates without mutating Notion.
- Context: Keep E1-E7 spine and add Founder Meeting v2/Hermes/CAG/RAG updates.
- Allowed files: `archflow_8_07/**`, `project/project-plan.md`, workflows, agents, reports, run evidence.
- Forbidden actions: Notion mutation, Linear dependency, external writeback.
- Acceptance criteria: each E1-E7 block has purpose, status, keep/revise/add tasks, checkboxes, acceptance criteria, evidence, blockers, owner decisions.
- Required evidence: package files and repo files inspected.
- Maximum attempts: 1.
- Stop condition: external task-board mutation required.
- Expected output format: Notion-ready Markdown blocks.

## Final QA Reviewer

- Title: Final QA Reviewer
- Execution type: Verification
- Goal: Review final implementation for public safety, unsupported claims, runtime overclaims, duplicated architecture, broken links, file consistency, and validation results.
- Context: Run only after implementation and checks.
- Allowed files: changed files and validation artifacts.
- Forbidden actions: edits, external side effects.
- Acceptance criteria: approve/revise/block decision with evidence.
- Required evidence: changed-file list, check results, file references.
- Maximum attempts: 1.
- Stop condition: unsafe data or repeated failed check.
- Expected output format: decision, findings, required fixes, residual risks.
