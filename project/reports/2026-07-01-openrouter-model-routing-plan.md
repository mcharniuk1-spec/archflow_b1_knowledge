# OpenRouter Model Routing Plan

Date: 2026-07-01

Status: specification only. OpenRouter runtime remains disabled until explicit approval and an approved local bridge or backend exists.

## Purpose

This plan defines how ArchFlow should use OpenRouter economically and reliably after provider activation is approved. It does not activate cloud model calls.

The architecture is simple:

1. Codex remains the operator, file editor, reviewer, and approval boundary.
2. LangGraph controls state, routing, stop conditions, and review gates.
3. WikiLLM and Obsidian remain the durable memory layers.
4. OpenRouter becomes a future server-side model router only for sanitized packets.
5. Claude, Gemini, and OpenAI frontier models handle planning, long reasoning, strategy, and review.
6. Cheaper models handle bounded execution, extraction, classification, drafting, and code variants.

## Activation Boundary

FACT: The current public project must not call OpenRouter from static browser code.

FACT: Cloud model keys must stay out of public files, frontend code, prompts, logs, screenshots, dashboard JSON, and generated artifacts.

INTERPRETATION: This plan is a routing contract for a future approved bridge. It is not a runtime claim.

GAP: Exact model IDs and pricing must be refreshed from the OpenRouter models endpoint before activation because model aliases and preview names change.

Latest model references verified from OpenRouter public model pages (2026-07-02):

- `openai/gpt-5.5`: `5 / 30` USD per million tokens (input/output), `1M` context, text+image input; released `Apr 24, 2026`.
- `~anthropic/claude-opus-latest`: aliases to latest Claude Opus family model (reported `Claude Opus 4.8`).
- `~anthropic/claude-fable-latest`: aliases to latest Claude Fable family model and should be used for qualification-only paths.
- `qwen/qwen3.6-plus`: `0.325 / 1.95` USD per million tokens, `1M` context, released `Apr 2, 2026` (35% discount shown on OpenRouter page).
- `moonshotai/kimi-k2-thinking`: `0.60 / 2.50` USD per million tokens, `262K` context, released `Nov 6, 2025`.
- `mistralai/mistral-medium-3.1`: `0.40 / 2` USD per million tokens, `131K` context, released `Aug 13, 2025`.
- `mistralai/mistral-small-3.2-24b-instruct-2506`: `0.075 / 0.20` USD per million tokens, `128K` context.
- `mistralai/codestral-2508`: `0.30 / 0.90` USD per million tokens, `256K` context.

## Frontier Council

Use the strongest available Claude, Gemini, and OpenAI models together for high-stakes work:

- strategy and architecture
- high-impact direction changes
- long-context synthesis
- payment verdicts
- public claim approval
- final PRD or ICP judgment
- outreach policy and offer framing

Do not use the frontier council for bulk extraction, formatting, routine summaries, first-draft variants, or simple code completion.

### Claude Family

Target role: artifact quality, long-form reasoning, PRD review, writing, agentic critique.

Preferred target models:

- `~anthropic/claude-opus-latest` (currently `anthropic/claude-opus-4.8`)
- `anthropic/claude-opus-4.7`
- `anthropic/claude-opus-4.6`
- `anthropic/claude-sonnet-4.6`
- `anthropic/claude-sonnet-4.5`
- `anthropic/claude-haiku-4.5` for cheaper Claude-family checks

Good qualities:

- Strong instruction following.
- Strong structured document judgment.
- Good at making strategy readable and operational.
- Good reviewer for PRDs, positioning, and public-safe text.

Poor qualities:

- Too expensive for repetitive extraction.
- Can over-polish uncertain claims.
- Needs strict source and hypothesis labels for market work.

Use Claude for:

- PRD and KB review.
- positioning and website message quality.
- final editorial pass.
- outreach tone and clarity.
- Review of any output that becomes public-facing.

### Gemini Family

Target role: long-context comparison, multimodal review, broad alternative generation, fast large-context scanning.

Preferred target models:

- `google/gemini-3.1-pro-preview`
- `google/gemini-3-flash-preview`
- `google/gemini-3.1-flash-lite-preview`
- `google/gemini-2.5-flash-lite`
- `google/gemma-4-31b-it` as a cheap Google-family baseline

Good qualities:

- Useful for comparing many artifacts or source summaries.
- Strong fit for multimodal or visual review when approved.
- Good alternative-generation model for strategy options.
- Flash tiers are useful when speed matters.

Poor qualities:

- Preview model IDs can shift.
- Needs schema constraints for repeatable outputs.
- Final claims still need checker review.

Use Gemini for:

- source comparison and research synthesis support.
- visual/UI or page review after website work.
- analytics assumptions comparison.
- Second-opinion strategy review in the frontier council.

### OpenAI Family

Target role: structured reasoning, conservative verdicts, scoring, schema design, and final decision review.

Preferred target models:

- `openai/gpt-5.5`
- `~openai/gpt-latest` (alias for latest OpenAI frontier model)
- `openai/gpt-5.4-pro`
- `openai/gpt-5.4-mini`
- `openai/gpt-5.4-nano`
- `openai/gpt-oss-120b` for open-model comparison if available

Good qualities:

- Strong for structured plans and scorecards.
- Good for conservative yes/no decisions.
- Useful for routing logic, schemas, and final verdict checks.
- Strong fit for ROI variance and payment/governance evidence judgment.

Poor qualities:

- Expensive for repeated drafting.
- Overkill for routine transformations.
- Exact model availability must be verified before wiring.

Use OpenAI primarily for:

- ICP scoring design and consistency checks.
- ROI and funnel logic.
- Payment verdicts.
- Final architecture consistency checks.

### Fable (Technical Qualifier)

Target role: technical qualification for high-specificity, approval-gated, and architecture-sensitive decisions.

Preferred target models:

- `~anthropic/claude-fable-latest`

Good qualities:

- Deep technical reasoning on narrow, high-risk questions.
- Good fit for qualification packets that need explicit approval before final verdict.
- Supports technical traceability when evidence and assumptions are contested.

Poor qualities:

- Not available for routine extraction or high-volume batch work.
- Must be explicitly enabled after OpenRouter model-list refresh.
- Budget is not for routine calls.

Use for:

- ROI variance edge-case and sensitivity stress checks that affect decisions.
- Payment verdict or gating decisions requiring technical qualification.
- Security/compliance or architecture qualification packets before final approval.

## Execution Pool

Execution models are allowed to produce intermediate work only. They do not approve public claims, pricing, memory promotion, architecture changes, or outreach.

### Kimi

Models:

- `moonshotai/kimi-k2-thinking`

Good qualities:

- Strong coding and multi-step execution drafts.
- Useful for implementation variants.
- Good at decomposing work into subtasks.

Poor qualities:

- Not the final business judge.
- Not the final public safety reviewer.
- Can over-infer if sources are weak.

Use for:

- code drafts
- implementation options
- workflow decomposition

### Qwen

Models:

- `qwen/qwen3.6-plus`
- `qwen/qwen3-235b-a22b`

Good qualities:

- Economical bulk processing.
- Strong schema-filling candidate.
- Useful for extraction, classification, and normalization.

Poor qualities:

- Not final positioning.
- Not final privacy or demand judgment.
- Needs sampled review on bulk work.

Use for:

- account evidence card drafts
- source tagging
- public-source normalization
- batch extraction

### Mistral

Models:

- `mistralai/mistral-medium-3.1`
- `mistralai/mistral-small-3.2-24b-instruct-2506`
- `mistralai/codestral-2508`
- `mistralai/mistral-large` only when activation-time pricing justifies it

Good qualities:

- Efficient quality passes.
- Concise synthesis.
- Good developer support through Codestral.

Poor qualities:

- Should not be sole final strategy judge.
- Needs a stronger checker for public claims.
- Not enough alone for payment/governance verdicts.

Use for:

- cleaned draft summaries
- copy variants
- concise research synthesis
- code completion

### DeepSeek

Models:

- `deepseek/deepseek-v4-pro`
- `deepseek/deepseek-v4-flash`
- `deepseek/deepseek-r1`

Good qualities:

- Cost-effective reasoning drafts.
- Technical analysis and failure-mode exploration.
- Useful alternate solution generator.

Poor qualities:

- Not final public copy.
- Not privacy/legal approval.
- Must cite source IDs for factual claims.

Use for:

- technical breakdowns
- alternate architecture options
- failure-mode analysis

### GLM / Z.ai

Models:

- `z-ai/glm-5`

Good qualities:

- Good economical long-context execution candidate.
- Useful for first-pass corpus maps.
- Useful for batch summaries.

Poor qualities:

- Not final architecture decision maker.
- Not payment verdict model.
- Needs checker review for memory promotion.

Use for:

- long-context batch synthesis
- first-pass research maps
- cheap agentic workflow drafts

### Llama

Models:

- `meta-llama/llama-3.3-70b-instruct`

Good qualities:

- Useful open-model baseline.
- Good for simple classification and fallback drafting.
- Helps compare closed-model outputs.

Poor qualities:

- Weaker for complex long-context strategy.
- Not the final quality bar.
- Less suited to subtle positioning.

Use for:

- baseline comparison
- simple classifiers
- low-risk draft fallback

### Perplexity

Models:

- `perplexity/sonar-pro`
- `perplexity/sonar`

Good qualities:

- Current public-source discovery.
- Useful for cited research starting points.
- Good for market scan input.

Poor qualities:

- Not final truth.
- Sources need independent review.
- Not for private or approval-gated research.

Use for:

- public web research starting points
- current-source discovery
- market input packets

### Other Optional Executors

Use these only when the activation-time model list and pricing make them worthwhile:

- `minimax/minimax-m2.5` for alternative drafts.
- `inception/mercury-2` for speed-first low-risk transformations.
- `x-ai/grok-4.3` for contrarian review only.

## Role + Land-Graph Node Routing

Map execution, review, and planner models by CrewAI role and LangGraph land-graph node/path.

### 2026-07-03 E1.2.8 Provider Correction

The active provider path is OpenRouter, not OpenAI. The E1.2.8 testmeeting provider comparison is mapped to `yushchenko.source_scope_gate`, not to an Epic label.

Selection result:

- Provider: OpenRouter.
- Route: `yushchenko.source_scope_gate`.
- Query shape: `land_graph(source_graph -> prd_blocks_graph -> risk_gate_graph)`.
- Selected execution model: `qwen/qwen3.6-plus`.
- Fallback execution model: `qwen/qwen3-235b-a22b`.
- Selection reason: first available Yushchenko source-scope execution model with 1M context and low input cost.
- Estimated cost: about `0.00794` USD.
- Raw private source sent: false.

This confirms the current rule: model optimization is performed per role and LangGraph node. Epic-level model assignment is prohibited.

### Yushchenko

- `source_scope_gate` (`source_graph -> prd_blocks_graph -> risk_gate_graph`)
  - Plan: `~openai/gpt-latest` then `anthropic/claude-opus-4.7`.
  - Execute: `qwen/qwen3.6-plus`, `qwen/qwen3-235b-a22b`.
  - Review: `anthropic/claude-sonnet-4.6`, `~openai/gpt-latest`.
- `research_hypothesis_graph` (`source_crosswalk_graph -> hypothesis_graph -> evidence_graph`)
  - Plan: `~openai/gpt-latest` then `~anthropic/claude-opus-latest`.
  - Execute: `qwen/qwen3.6-plus`, `qwen/qwen3-235b-a22b`, `deepseek/deepseek-v4-flash`.
  - Review: `anthropic/claude-sonnet-4.6`, `~openai/gpt-latest`.
- `roi_metrics_node` (`metrics_graph -> scenario_graph -> variance_gate_graph`)
  - Plan: `~openai/gpt-latest`, `google/gemini-3.1-pro-preview`, `anthropic/claude-opus-4.7`.
  - Fable gate: `~anthropic/claude-fable-latest` for contested technical math.
  - Execute: `qwen/qwen3.6-plus`, `qwen/qwen3-235b-a22b`, `deepseek/deepseek-v4-pro`.
  - Review: `openai/gpt-5.5`, `anthropic/claude-sonnet-4.6`.
- `payment_node` (`value_graph -> risk_graph -> governance_graph -> signoff_graph`)
  - Plan: `~openai/gpt-latest`, `anthropic/claude-opus-4.7`, `google/gemini-3.1-pro-preview`.
  - Fable gate: `~anthropic/claude-fable-latest`.
  - Execute: `qwen/qwen3.6-plus`, `qwen/qwen3-235b-a22b`.
  - Review: `openai/gpt-5.5`, `anthropic/claude-opus-4.7`.

### Jesus

- `prd_verdict_node` (`source_graph -> prd_blocks_graph -> risk_gate_graph`)
  - Plan: `~openai/gpt-latest`, `anthropic/claude-opus-latest`.
  - Execute: `qwen/qwen3.6-plus`, `qwen/qwen3-235b-a22b`.
  - Review: `anthropic/claude-sonnet-4.6`, `~openai/gpt-latest`.
- `payment_review_node` (`value_graph -> risk_graph -> governance_graph -> signoff_graph`)
  - Plan: `~openai/gpt-latest`, `anthropic/claude-opus-latest`, `google/gemini-3.1-pro-preview`.
  - Fable gate: `~anthropic/claude-fable-latest` if qualification is requested.
  - Execute: `qwen/qwen3.6-plus`, `qwen/qwen3-235b-a22b`.
  - Review: `openai/gpt-5.5`, `anthropic/claude-opus-4.7`.

### Messi

- `offer_positioning_node` (`offer_graph -> narrative_graph -> compliance_gate_graph`)
  - Plan: `anthropic/claude-opus-latest`, `~openai/gpt-latest`.
  - Execute: `moonshotai/kimi-k2-thinking`, `mistralai/mistral-medium-3.1`, `qwen/qwen3.6-plus`.
  - Review: `google/gemini-3-flash-preview`, `anthropic/claude-sonnet-4.6`.
- `outreach_node` (`message_graph -> channel_graph -> approval_graph`)
  - Plan: `anthropic/claude-opus-latest`, `~openai/gpt-latest`.
  - Execute: `mistralai/mistral-medium-3.1`, `mistralai/mistral-small-3.2-24b-instruct-2506`.
  - Review: `anthropic/claude-sonnet-4.6`, `~openai/gpt-latest`.
- `style_and_copy_node` (`brief_graph -> draft_graph -> style_graph`)
  - Plan: `anthropic/claude-opus-latest`, `~openai/gpt-latest`.
  - Execute: `mistralai/mistral-small-3.2-24b-instruct-2506`, `minimax/minimax-m2.5`, `qwen/qwen3.6-plus`.
  - Review: `anthropic/claude-sonnet-4.6`.

### Ronaldo

- `source_risk_node` (`source_graph -> prd_blocks_graph -> risk_gate_graph`)
  - Plan: `google/gemini-3.1-pro-preview`, `~openai/gpt-latest`.
  - Execute: `moonshotai/kimi-k2-thinking`, `qwen/qwen3.6-plus`.
  - Review: `anthropic/claude-sonnet-4.6`.
- `website_technical_node` (`offer_graph -> narrative_graph -> compliance_gate_graph`)
  - Plan: `anthropic/claude-opus-latest`, `~openai/gpt-latest`.
  - Execute: `mistralai/mistral-medium-3.1`, `moonshotai/kimi-k2-thinking`, `qwen/qwen3.6-plus`.
  - Review: `anthropic/claude-sonnet-4.6`.

### LOL

- `research_graph_node` (`source_crosswalk_graph -> hypothesis_graph -> evidence_graph`)
  - Plan: `~openai/gpt-latest`, `anthropic/claude-opus-latest`, `google/gemini-3.1-pro-preview`.
  - Execute: `qwen/qwen3.6-plus`, `perplexity/sonar-pro`, `deepseek/deepseek-v4-flash`.
  - Review: `openai/gpt-5.5`, `anthropic/claude-sonnet-4.6`.
- `positioning_graph_node` (`offer_graph -> narrative_graph -> compliance_gate_graph`)
  - Plan: `~openai/gpt-latest`, `anthropic/claude-opus-latest`.
  - Execute: `moonshotai/kimi-k2-thinking`, `qwen/qwen3.6-plus`.
  - Review: `anthropic/claude-sonnet-4.6`, `google/gemini-3-flash-preview`.
- `content_review_node` (`brief_graph -> draft_graph -> style_graph`)
  - Plan: `~openai/gpt-latest`, `anthropic/claude-opus-latest`.
  - Execute: `minimax/minimax-m2.5`, `qwen/qwen3.6-plus`.
  - Review: `anthropic/claude-sonnet-4.6`.

### Theory

- `research_hypothesis_node` (`source_crosswalk_graph -> hypothesis_graph -> evidence_graph`)
  - Plan: `~openai/gpt-latest`, `google/gemini-3.1-pro-preview`.
  - Execute: `qwen/qwen3.6-plus`, `deepseek/deepseek-v4-pro`, `perplexity/sonar-pro`.
  - Review: `anthropic/claude-sonnet-4.6`, `~openai/gpt-latest`.
- `roi_node` (`metrics_graph -> scenario_graph -> variance_gate_graph`)
  - Plan: `google/gemini-3.1-pro-preview`, `~openai/gpt-latest`.
  - Execute: `qwen/qwen3.6-plus`, `deepseek/deepseek-v4-pro`.
  - Review: `openai/gpt-5.5`.

### Security

- `technical_qualification_node` (`data_model_query -> dependency_graph -> qualification_graph -> approval_graph`)
  - Plan: `~anthropic/claude-fable-latest` only.
  - Fable gate: `~anthropic/claude-fable-latest`.
  - Execute: `~anthropic/claude-fable-latest`.
  - Review: `anthropic/claude-opus-4.7`.

## Maker Checker Pattern

Default flow:

1. Cheap executor creates structured intermediate output.
2. Deterministic parser checks JSON/schema/source IDs.
3. Codex checks file safety and project fit.
4. Frontier reviewer runs only when escalation threshold is hit.
5. Human approval is required before publication, memory promotion, outreach, provider activation, or payment verdict.

Escalate to frontier review when:

- output affects public claims
- output changes strategy, architecture, or memory contract
- source evidence conflicts
- confidence is low
- an account reaches outreach threshold
- pricing or payment verdict is affected
- user explicitly requests strongest-model review

## Budget And Reliability Rules

Budget:

- Routine work uses no frontier council.
- Substantial strategy work may use one to two calls per frontier family.
- Payment or architecture verdict uses one call per family plus Codex final review.
- Research and discovery tasks use cheap execution first and sampled frontier review.

Reliability:

- Refresh OpenRouter model list before activation.
- Use capability tiers when exact aliases are unavailable.
- Retry transient provider failures once.
- Repair schema failures once, then send to reviewer.
- Stop on unclear source boundary, budget cap, provider outage, or human approval requirement.

## Required Log Fields

Every model call must log:

- timestamp
- task_role_and_langgraph_node
- query shape and graph node path
- model ID
- model role
- prompt version
- source IDs used
- output artifact
- cost estimate
- decision
- reviewer model ID
- human gate required

## Reviewer Prompt For Future Agents

```text
Review the ArchFlow OpenRouter model-routing spec as a strict architecture and cost reviewer.

Assume cloud model runtime is disabled until explicit approval and a backend/local bridge exists. The spec may describe future cloud routing, but must not imply live provider availability, exposed credentials, or frontend access to model APIs.

Check provider boundaries, cost discipline, maker/checker separation, role-node fit, public-safety gates, unsupported model-name risk, frontier-model overuse, budget caps, retry rules, fallback behavior, and whether deterministic scripts or local models should replace model calls.

Return severity-ranked issues with required corrections. Do not edit files unless explicitly assigned.
```

## Decision

Adopt this as the future model-routing contract for ArchFlow planning and execution. Keep OpenRouter disabled until the bridge/backend, secret storage, model list refresh, budget controls, and approval gates exist.
