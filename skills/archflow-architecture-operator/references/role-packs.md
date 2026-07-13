# Role Packs

## Coordination tiers

| Tier | Use | Boundary |
|---|---|---|
| Watchdog | Classify risk, issue contracts, review evidence, stop/escalate. | Never edits or calls external systems. |
| Terra integrator | High-impact synthesis, dependency decisions, sole-writer integration, final reconciliation. | Must not self-approve high-risk output. |
| Luna worker | Bounded read-only research, extraction, drafting, or independent critique. | No shared-file or external-system mutation unless promoted to a separately approved writer contract. |
| Deterministic checker | Syntax, schema, tests, source-boundary and safety scans. | No judgment beyond defined rules. |
| Independent reviewer | Correctness, completeness, claims, risk, and approval decision. | Separate from the maker for high-risk work. |

Terra and Luna are role labels, not claims about a particular model. Bind them to a runtime only after availability, cost, privacy, and evaluation proof.

## Prebuilt department templates

| Template | Core roles | Required outputs |
|---|---|---|
| Knowledge architecture | Ontology architect, corpus curator, retrieval engineer, graph analyst, memory reviewer, privacy reviewer. | Authority map, source registry, retrieval benchmark, graph policy, promotion packet. |
| PRD and ICP | Discovery researcher, behavioral researcher, market analyst, product manager, PRD architect, reviewer. | Evidence cards, ICP hypothesis, PRD, acceptance criteria, task packet. |
| Engineering | Systems architect, backend, frontend, data, QA, security, SRE, reviewer. | ADR, implementation slices, tests, threat model, runbook, recovery proof. |
| Agent engineering | LLM architect, context engineer, prompt engineer, orchestration engineer, evaluation engineer, safety reviewer. | Agent contract, state graph, skill pack, eval set, trace schema, stop rules. |
| Post-training and data | Data curator, model researcher, eval scientist, privacy/safety reviewer, infrastructure planner. | Dataset card, provenance, training/eval plan, risk and cost gates. |
| Research and analytics | Research lead, source verifier, statistician, data engineer, analyst, reviewer. | Research charter, source table, reproducible analysis, confidence/gaps. |
| Content and growth | Strategist, behavioral economist, researcher, writer, SMM, SEO, designer, analyst, reviewer. | Evidence-backed brief, content system, experiments, metrics and claim gate. |
| Sales and outreach | ICP analyst, account researcher, copywriter, qualification analyst, sales operator, reviewer. | Verified target list, messages, approval gate, response and learning ledger. |
| Finance and operations | Finance analyst, pricing strategist, operations planner, compliance reviewer. | Unit economics, pricing tests, controls, scenario and approval packet. |
| Web and interactive media | UX strategist, visual designer, frontend engineer, 3D engineer, motion/video specialist, performance/a11y QA. | Storyboard, scene/runtime budget, accessible fallback, performance proof, browser QA. |
| Long-form publishing | Research editor, technical writer, citation reviewer, LaTeX/Typst build operator, accessibility reviewer. | Source-grounded manuscript, deterministic build, citation and PDF checks. |

## Skill allocation

Give each role:

- one task-specific skill;
- shared source-boundary and public-safety rules;
- a handout/closeout skill when it writes artifacts;
- no unrelated global skill inventory;
- a versioned skill card with provenance, allowed tools, forbidden actions, evaluation cases, and rollback notes.
