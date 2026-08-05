# Dashboard Integration Delivery and Next Runtime Plan

Status: public dashboard migration implemented; runtime persistence remains gated
Verified baseline: 2026-08-05

The previous plan has been executed for the public static repository. The dashboard is now the primary non-technical interface to the unified knowledge crew.

## Delivered migration

| Previous surface | Delivered replacement |
|---|---|
| Architecture 1 / Architecture 2 selector | One Knowledge Case and adaptive workflow packs |
| Separate Knowledge Service and Agent Control products | One Work view from goal through handoff |
| Standalone Jarvis brain/chat | Embedded deterministic Taras onboarding guidance |
| Tool/topic navigation | Today, Work, Knowledge, Team, Review, Set up |
| Large developer catalog as the home page | Employee mission, evidence boundary, reviewer, next action |
| Unstructured role panels | Twenty-one stable roles with Ukrainian call names and explicit ownership/prohibitions |
| Generic graph blocks | Six human phases backed by the typed LangGraph lifecycle |
| Hidden configuration assumptions | Visible LlamaIndex, TurboVec, CrewAI, LangGraph, Obsidian, Orbit, and privacy boundaries |
| Image legend with vague verbs | Four exact labeled diagrams with editable SVG sources |

## Public dashboard truth

The Crew Desk:

- loads fixed public JSON contracts;
- stores drafts/examples in browser local storage;
- exports JSON review packets;
- accepts a same-origin or HTTP-loopback bridge proposal only;
- calls no provider;
- writes to no external system;
- has no public checkpointer;
- cannot grant permission, approve requirements, or prove execution.

## Runtime integration plan

The following steps are intentionally not activated by browser configuration:

1. Add authenticated team identity and map users to responsibility roles without treating roles as permissions.
2. Add SQLite for a local single-user profile only after schema migration and recovery proof.
3. Add PostgreSQL for team state only after tenancy isolation, backup, restore, retention, and replay proof.
4. Bind `thread_id` to `case_id` and test interrupt/resume with idempotent action IDs.
5. Add an allowlisted LlamaIndex index with exact document/node metadata and deterministic lexical fallback.
6. Pilot TurboVec only after the fixed 20-query promotion gate passes.
7. Add optional Obsidian and Orbit adapters with private/local configuration and sanitized reference return.
8. Add authenticated write adapters one at a time, each with exact approval, rollback, receipt, and readback.
9. Add provider routing only with server-side secrets, bounded budgets, provider disclosure rules, and outcome evaluation.

## Dashboard acceptance

- Six primary routes render at desktop, tablet, and mobile.
- Text wraps without overlap; fields and perimeter spacing remain aligned.
- The mobile navigation has six reachable targets and minimum touch sizing.
- Forms are keyboard accessible and preserve visible focus.
- Reduced-motion mode disables nonessential animation.
- User input is escaped before rendering.
- The local bridge rejects arbitrary remote origins.
- `/jarvis` redirects to `#today`.
- Every state label distinguishes configured, tested, gated, and executed.

## Rollback

The previous dashboard remains in Git history. Roll back only through a reviewed Git revert; do not restore the old two-architecture terminology or standalone Jarvis as current architecture.
