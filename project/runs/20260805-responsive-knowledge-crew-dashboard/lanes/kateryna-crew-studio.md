# Kateryna Lane — Configurable Crew Studio

Status: complete design alternative; provider-disabled; no implementation claim

Optimization target: self-hosters and administrators who need to configure sources, retrieval, roles, skills, LangGraph gates, CrewAI task contracts, a local bridge, and auditable receipts without putting credentials or raw private source material in the browser.

## Recommendation

Use **ArchFlow Crew Studio** as the administrator workspace inside the single Knowledge Case Controller. It should be a case-first control plane, not another architecture and not a second knowledge store. The default screen opens one case, shows its truth state, and exposes five bounded work areas: **Sources**, **Crew**, **Flow**, **Bridge**, and **Receipts**. Jarvis becomes a contextual **Operator** drawer attached to that case. It can explain, validate, and prepare a review packet; it cannot own a role, expand authority, or execute an action.

This alternative is deliberately optimized for configuration depth. It should be the administrator mode of the integrated product, while the employee-facing mode can project a smaller task-oriented view from the same case packet.

## Evidence Classification

### FACT

- The admitted run requires one case/state spine, a responsive browser-local dashboard, public-safe import/export, an approved local-bridge path, embedded Jarvis, Ukrainian call names written in English letters, deterministic verification, and no provider execution or external writeback. Evidence: `project/runs/20260805-responsive-knowledge-crew-dashboard/task-contract.md:20-56`.
- The unified operating architecture already supersedes Architecture 1/2 as top-level concepts and defines one controller, one case, many bounded roles. Evidence: `docs/unified-operating-architecture.md:3-31`.
- The approved dashboard migration direction is case-based and requires private evidence to appear only as a source class plus a sanitized opaque receipt. Evidence: `docs/dashboard-integration-plan.md:9-29`.
- The committed dashboard has nine primary tabs and twelve detailed tabs before the hidden legacy Jarvis route. The navigation then adds a dedicated Jarvis link and an Admin/Guest switch. Evidence: `project/dashboard/app.js:1-28` and `project/dashboard/app.js:1422-1452`.
- The committed CSS is 3,839 lines and contains two `:root` blocks, five `.sidebar` blocks, six `.view` blocks, six `.topbar` blocks, and three separate `@media (max-width: 760px)` blocks. These counts were reproduced by static source inspection.
- The committed responsive cascade assigns `width: 100vw` to `.view` and nested hero components while `.view` also receives inline padding. It also globally hides horizontal overflow. Evidence: `project/dashboard/styles.css:1044-1063`, `project/dashboard/styles.css:1249-1254`, and `project/dashboard/styles.css:3672-3678`.
- The final mobile fullscreen rule changes the schema workspace back to `overflow: hidden`, after an earlier mobile rule made it scrollable. Evidence: `project/dashboard/styles.css:3652-3656` and `project/dashboard/styles.css:3834-3838`.
- Role forms use repeated implicit labels such as “Objective”, “Responsibility”, and “Tools” without role-specific accessible names, descriptions, or inline validation wiring. Evidence: `project/dashboard/app.js:1936-1971`.
- The generic table helper emits no caption and no `scope="col"` on headers. Evidence: `project/dashboard/app.js:1480-1486`.
- The root view is one large `aria-live="polite"` region, so route replacement can cause a screen reader to receive the whole dashboard as a live update. Evidence: `project/dashboard/index.html:50`.
- Jarvis currently exists as a top-bar destination, a navigation destination, a hidden legacy dashboard route, and a large retained implementation in `app.js`. Evidence: `project/dashboard/index.html:40-47`, `project/dashboard/app.js:28`, `project/dashboard/app.js:1444-1447`, and `project/dashboard/app.js:2190-2463`.
- A non-refresh Jarvis submission attempts the configured bridge automatically and includes recent conversation plus staged attachment excerpts. The file path reads up to 6,000 characters from text-like files. This is not proof of a leak, but it does not meet the new goal of keeping raw private material out of the browser projection. Evidence: `project/dashboard/app.js:1102-1145`, `project/dashboard/app.js:2162-2185`, and `project/dashboard/app.js:2626-2676`.
- Chat messages are persisted in `localStorage` with no count cap before an explicit clear. Evidence: `project/dashboard/app.js:1221-1249`.
- The current configuration screen supports save and export but has no config import control or import validation path. Evidence: `project/dashboard/app.js:3678-3730` plus a source-wide static search that found no config-import marker.
- The generated dashboard data is dated 2026-07-15 and still exposes older role titles such as Goal Architect, Terra Integrator, and Luna Worker, while the canonical 2026-08-05 role contract uses normalized stable IDs. Evidence: `project/dashboard/data.json:2`, `project/dashboard/data.json:10179-10241`, and `project/system/contracts/role-catalog.json:17-126`.
- Focus-visible styling, a skip link, keyboard activation for graph nodes, keyboard move buttons, dialog focus trapping, focus return, reduced-motion rules, and a mobile stage-list alternative already exist. Evidence: `project/dashboard/index.html:13`, `project/dashboard/styles.css:56-80`, `project/dashboard/styles.css:1025-1037`, `project/dashboard/app.js:2913-2959`, and `project/dashboard/app.js:3370-3406`.

### INTERPRETATION

- The current dashboard contains useful contracts, but it behaves like accumulated documentation, legacy workflow tooling, and Jarvis controls sharing one shell. Administrators must translate between many routes to answer one operational question: “Is this case configured safely enough to export or hand to an approved operator?”
- Overflow is often suppressed rather than structurally prevented. That can make a screenshot appear contained while borders, table columns, or fullscreen content are clipped.
- The existing role and prompt editors are technically editable, but their repeated cards do not make authority conflicts, missing reviewers, source scope, or forbidden actions easy to compare.
- A visible Admin switch and a connected API pill can imply security or runtime authority even though the surrounding documentation says they are only browser-local previews.
- The safest self-hosted interface is not a browser-based secret manager. It is a public-safe control plane that exchanges opaque capability handles and signed or hashed receipts with an approved local bridge.

### HYPOTHESIS

- A five-area case studio will let an administrator complete initial configuration and identify blockers faster than the current twenty-one-route navigation because the source, role, task, gate, bridge, and receipt relationships remain visible under one case header.
- A split “contract editor + consequence preview” will reduce unsafe configuration changes because every changed parameter immediately states its effect, required evidence, and rollback.
- Making the stage list primary and the freeform canvas secondary will improve keyboard and mobile completion without removing the visual graph for expert desktop users.
- A contextual Operator drawer will preserve Jarvis guidance while preventing it from appearing to be a separate brain or authority source.

### GAP

- This lane could run JavaScript syntax and JSON parsing checks, but the sandbox blocked the committed headless Chrome smoke with `Operation not permitted`. Current rendered overflow, 200%/400% zoom, focus order, and screen-reader behavior therefore remain unverified in this lane.
- No representative administrator has completed the proposed source-to-receipt workflow, so comprehension and time-to-configure remain hypotheses.
- The exact private local-bridge authentication mechanism is not implemented in this lane. The UI contract below requires loopback-only binding, exact-origin checks, and a browser-unreadable session, but runtime proof remains an implementation gate.
- TurboVec has bounded trial evidence only. The Studio must keep it disabled as a default until the fixed paired benchmark, provenance, filtering, persistence, lexical fallback, and independent verdict pass.

## Audit Of The Committed Dashboard

| Priority | Area | Finding | Required response |
|---|---|---|---|
| P0 | Browser privacy | File selection can read a bounded text excerpt in the page, and ordinary Jarvis submission attempts a bridge request containing conversation and attachment data. This conflicts with the new dashboard truth rule for private corpus material. | Remove arbitrary source-body upload from the Studio. Register public-safe source descriptors or bridge-issued opaque handles. Add an explicit payload review before every bridge submission. |
| P1 | Jarvis separation | Jarvis appears in global status, global navigation, a hidden legacy route, and a standalone route. | Retain one contextual Operator drawer. Mark Jarvis as a projection helper with zero role authority. Keep any old route only as a compatibility redirect or read-only legacy notice. |
| P1 | Navigation and alignment | Nine primary plus twelve secondary tabs overload the sidebar and become a horizontally scrolling mobile strip. | Collapse navigation to Case, Sources, Crew, Flow, Bridge, and Receipts. Move framework-specific views into the relevant area. |
| P1 | Mobile perimeter | Nested `100vw` components inside a padded `.view` can extend beyond the content box; global `overflow-x: hidden` masks the result. | Use `width: 100%`, `min-width: 0`, container padding tokens, and component-level scroll regions. Never use `100vw` for a normal nested panel. |
| P1 | Mobile fullscreen | The final fullscreen rule hides schema-workspace overflow. Earlier stage-list rules allow content to grow, so a later hidden parent can make lower controls unreachable. | Give fullscreen one scroll owner. On mobile, use a full-screen stage sheet with a sticky action bar and `overflow-y: auto`; do not expose canvas as the default. |
| P1 | CSS predictability | Repeated roots, selector blocks, breakpoints, and late cascade corrections create conflicting ownership of layout. | Rebuild around one token block, one base layout, and mobile-first breakpoints. Remove late correction layers after visual parity is established. |
| P1 | Accessibility announcements | The entire dynamic view is live. Tables lack captions and scoped headers. Validation and connection states lack dedicated status/alert semantics. | Announce only the changed status node. Add captions, header scope, focusable scroll wrappers, `aria-describedby`, `aria-invalid`, `role="status"`, and `role="alert"`. |
| P1 | Touch and zoom | Mobile navigation and top-bar controls drop to 34px height, and several proof labels use 10px text. | Use a 44px minimum interactive target, 12px minimum supporting labels, and verify at 200% and 400% zoom. |
| P2 | Form labels and inputs | Repeated implicit labels are valid HTML but ambiguous across many role cards. Inputs lack names, unique help, constraints, dirty state, and field-level errors. | Use one fieldset per role, a legend containing the Ukrainian call name and stable ID, explicit `for`/`id`, persistent help/error slots, and section-level validation. |
| P2 | Table responsiveness | Many dense tables depend on horizontal scroll and `:has()` containment; the scroll region is not consistently named or keyboard focusable. | Convert essential rows to definition cards below 720px. Keep only true matrices scrollable, with a caption, `tabindex="0"`, label, shadow/gradient overflow affordance, and frozen first column on wide screens. |
| P2 | Perimeter spacing | Normal content has no stable maximum reading width, while inline `margin-top` styles and multiple padding overrides produce irregular vertical rhythm. | Use 16/20/24/32px perimeter tokens, a 72ch prose measure, a 1240px form/data measure, and an unconstrained graph canvas inside its own viewport. |
| P2 | Import/export | Configuration can be exported but cannot be safely imported, compared, migrated, or rolled back. | Add schema-validated import with secret-key rejection, diff preview, conflict handling, and a local rollback snapshot. |
| P2 | Role truth | The generated role projection predates the normalized role catalog and Ukrainian display names. | Generate the dashboard roster from the canonical stable IDs and a reviewed call-name mapping. Show old aliases only in migration metadata. |

## Interface Shape

The Studio exposes a small behavioral surface even though it contains deep configuration:

```text
open_case(case_packet)                 -> admitted case or explicit blocker
edit_draft(section, change)            -> local candidate + consequence preview
validate_draft()                       -> errors, warnings, required evidence, digest
connect_bridge(loopback_descriptor)    -> capability receipt or fail-closed state
export_packet(kind)                    -> config, review, or receipt bundle
```

This surface hides framework file locations, schema migrations, validation ordering, secret isolation, compatibility aliases, receipt normalization, and source-handle resolution. The UI still shows the resulting contract and evidence; it does not make implementation detail the administrator’s navigation model.

### Administrator usage example

1. Open one case and confirm owner, risk, run profile, provider state, writeback state, and stop conditions.
2. Register public sources or bridge-issued opaque source handles; inspect freshness, authority, and exclusions.
3. Configure the selected crew. Resolve missing responsibility, source, skill, output, reviewer, or forbidden-action fields.
4. Tune retrieval under locked provenance and lexical-fallback rules.
5. Arrange LangGraph stages and attach CrewAI task contracts to each bounded work stage.
6. Validate. Repair blockers before connecting a local bridge.
7. Test the bridge handshake. Review the exact capability list; no provider or write capability is accepted silently.
8. Export a public-safe review packet and receipt bundle. An approved operator applies any repository or runtime change.

## Information Architecture

### Persistent case bar

One sticky 64px case bar contains:

- case title and opaque `case_id`;
- truth state: Draft, Validated, Review required, Blocked, or Receipt verified;
- risk and run profile;
- provider state and writeback state, both explicit and disabled by default;
- dirty-change count;
- **Validate draft** and **Export** actions;
- an **Operator** button that opens the contextual Jarvis drawer.

There is no global “Run agents” button. A future executable action must appear only after a bridge capability receipt, a target-specific approval interrupt, and a reviewable action packet exist.

### Six navigation destinations

1. **Case** — objective, done conditions, state, requirements, decisions, blockers, and approval class.
2. **Sources** — source registry, source class, authority, owner, freshness, exclusions, exact-source policy, retrieval profile, and knowledge destinations.
3. **Crew** — role responsibilities, inputs, outputs, sources, skills, tools, permissions, reviewer route, handoff, and lifecycle.
4. **Flow** — LangGraph stages and gates, CrewAI task contracts, repair paths, parallel claims, validation, and optional desktop graph.
5. **Bridge** — local setup, health/capability handshake, safe test fixtures, and disconnected/incompatible states.
6. **Receipts** — append-only-looking projection of config, validation, execution, review, approval, readback, and knowledge-promotion receipts. Browser-local receipts remain visibly unsigned/local.

Frameworks are placed where administrators use them:

- LlamaIndex and optional TurboVec live under **Sources → Retrieval**.
- WikiLLM and Obsidian live under **Sources → Knowledge destinations**.
- Orbit/Graphify live under **Sources → Structural evidence**.
- Skills and CrewAI live under **Crew**.
- LangGraph lives under **Flow**.
- Jarvis lives in the **Operator** drawer and nowhere in the system-authority hierarchy.

## Desktop Layout

```text
┌──────────────────────────── one case bar ────────────────────────────┐
│ case / state / risk / provider off / writeback off / Validate / Export│
├──────────────┬──────────────────────────────────┬─────────────────────┤
│ 248px rail   │ flexible workbench               │ 360px context pane  │
│ Case         │ selected editor                  │ consequences         │
│ Sources      │ form / stage list / matrix       │ blockers             │
│ Crew         │                                  │ evidence required    │
│ Flow         │                                  │ receipt preview      │
│ Bridge       │                                  │                     │
│ Receipts     │                                  │                     │
├──────────────┴──────────────────────────────────┴─────────────────────┤
│ contextual Operator drawer overlays the context pane when requested  │
└──────────────────────────────────────────────────────────────────────┘
```

- At 1440px and wider: 248px rail, `minmax(0, 1fr)` workbench, 360px context pane, 24px outer gutters, 20px internal gaps.
- At 1024-1439px: 216px rail plus workbench. Context and Operator become mutually exclusive 400px drawers so the main editor never falls below 600px.
- Prose is capped at 72ch. Form and table content is capped at 1240px. The graph is the only intentionally unconstrained surface and owns its own pan/scroll viewport.

## Tablet And Mobile Layout

- At 768-1023px: one 56px app bar, a navigation sheet, one-column workbench, and a bottom action tray that appears only when the draft is dirty. The context pane becomes an inline “Consequences and evidence” accordion after the edited section.
- At 0-767px: one 56px sticky header, 16px perimeter, 12px component gaps, single-column forms, and no nested `100vw` elements.
- The mobile Flow view defaults to an ordered stage list. Each stage opens a full-screen sheet with one scroll owner. Canvas is available only through an explicit “Open visual graph” action and remains read-only on narrow screens.
- Matrices become cards with label/value pairs. True comparison grids retain horizontal scrolling inside a named, focusable region.
- Action bars wrap in source order; primary action comes last in DOM and remains visually last. No fixed bottom composer covers content.
- The Operator is a full-screen sheet on mobile with a visible close button, context summary, payload preview, and return focus.
- Minimum interactive height is 44px. Long IDs, paths, and hashes use `overflow-wrap: anywhere`; human prose uses normal word wrapping and never `word-break: break-all`.

## Visual System

The visual metaphor is an **equipment studio**: calm neutral work surfaces, explicit patch points, and visible safety interlocks. It should feel configurable without resembling a command-line terminal.

| Token | Value | Use |
|---|---|---|
| Canvas | `#F4F1E9` | Warm, low-glare application background. |
| Surface | `#FFFEFA` | Forms, tables, drawers. |
| Ink | `#17201D` | Primary text and selected navigation. |
| Muted ink | `#56645F` | Supporting text; verify 4.5:1 on its surface. |
| Local/capable | `#087A78` | Connected local capability, always paired with text/icon. |
| Draft/change | `#8B5E00` | Unvalidated or review-required state. |
| Blocked | `#A43D45` | Blocking error, always paired with “Blocked” and an explanation. |
| Structural | `#4957A6` | Graph routes, source relationships, stable IDs. |
| Focus | `#0B66C3` | 3px focus ring with 2px offset. |
| Radius | 10px / 14px | Controls / panels. |
| Grid | 4px base; 8/12/16/20/24/32 | Spacing and perimeter rhythm. |

- Use the system sans stack for labels and prose, and the system monospace stack only for machine IDs, paths, hashes, JSON pointers, and receipt digests.
- Body copy is 15-16px at 1.55 line-height. Supporting copy is at least 12px. Page titles use 30/36px desktop and 24/30px mobile.
- No status relies on color. Every state has an icon, label, and one-sentence consequence.
- Avoid decorative gradients behind dense form content. Reserve elevation for drawers, dialogs, and the selected stage.

## Source And Retrieval Studio

### Source registry

Every source row shows:

- source label and opaque source ID;
- class: public repository, reviewed knowledge note, generated structural index, or approved private handle;
- authority state, owner, freshness, supersession, and access boundary;
- allowed operations: metadata, exact read, lexical retrieval, vector candidate, or structural query;
- public-safe evidence receipt;
- exclusion reason when blocked.

The browser must never accept a raw private path, `.env` file, vault body, token, cookie, or unrestricted directory. A private installation registers those server-side and returns an opaque handle plus sanitized metadata. Public repo-relative paths may be displayed because they are already within the approved public corpus.

### Retrieval parameters

Start from the committed safe contract:

- include: `project/`, `history/`, `skills/`, `wiki/`;
- exclude: `.git/`, `project/.env.local`, `project/local/`, `raw/`, `source_exports/`, `secrets/`, `private/`, `tmp/`;
- chunk size 800 and overlap 120;
- vector, lexical, and rerank top-k all 5;
- source paths required;
- private-source refusal on;
- lexical fallback locked on;
- contradictory current claims return a GAP instead of silent synthesis.

These values come from `project/workflows/llamaindex-rag.yaml:23-69`. Each field displays “what changes”, “valid range”, “proof required”, and “rollback”. Cross-field validation blocks overlap greater than or equal to chunk size, non-positive top-k, rerank larger than the available candidate set, missing source-path enforcement, or disabled lexical fallback.

TurboVec appears as **Candidate: off**. Enabling a draft configuration does not make it default. The UI requires the twenty-query paired benchmark, no regression against lexical retrieval, stable IDs, fixed embeddings, allowlist filters, persistence integrity, lexical fallback, and independent verdict before a promotion control is even shown. Evidence: `project/workflows/llamaindex-rag.yaml:89-114`.

## Crew, Roles, And Skills

### Role card contract

Every role editor is a fieldset with this legend shape:

`Kateryna · Designer`

`designer` · configured contract · not running

Required fields:

- responsibility and purpose;
- inputs and expected outputs;
- allowed source classes and exact-source requirement;
- allowed tools and packaged skills;
- forbidden actions;
- maker/reviewer route;
- claimed files or target class;
- handoff target;
- stop and escalation conditions;
- proof state and last reviewed receipt.

The Crew matrix blocks self-review, duplicate ownership of a shared write target, missing output schema, missing reviewer, permission expansion through a tool, and a human name that does not map to a stable role ID.

### Human-facing call-name rule

Call name always comes first; the stable ID remains the machine authority underneath. Role names do not grant permission.

| Call name | Stable role ID |
|---|---|
| Yaromyr | `goal_and_architecture_operator` |
| Bohdan | `admission_controller` |
| Solomiia | `source_and_context_operator` |
| Oksana | `requirements_and_market_research` |
| Taras | `onboarding_guide` |
| Danylo | `task_and_handoff_planner` |
| Olena | `positioning_and_copy_maker` |
| Andrii | `qualification_and_channel_planner` |
| Kateryna | `designer` |
| Dmytro | `implementation_maker` |
| Iryna | `action_validator` |
| Mykola | `verifier` |
| Halyna | `independent_reviewer` |
| Larysa | `knowledge_librarian` |
| Maksym | `integrator` |
| Pavlo | `external_action_operator` |
| Nazar | `release_operator` |
| Zoriana | `growth_and_outcome_analyst` |
| Ostap | `observability_and_efficiency_observer` |
| Marta | `surface_projection_operator` |
| Roman | `product_packaging_engineer` |

The mapping is grounded in `README.md:62-92` and `project/system/contracts/role-catalog.json:17-126`. Jarvis is a product surface called **Operator**, not a role agent and not a permission-bearing identity.

### Skill lifecycle

Each skill moves through an explicit rail:

`Discover → Inspect → Deduplicate → Scan → Normalize → Test → Allowlist → Assign → Observe → Update → Deprecate → Roll back`

The skill record shows source, version/hash, license state, permission request, hook/network behavior, duplicate decision, sanitized fixture, static scan receipt, semantic scan state, role assignments, last observed use, supersession, and rollback. Skill Spectre may show its recorded static scan only; semantic scanning stays **Unavailable / not claimed** until a receipt exists.

## Flow: LangGraph Gates And CrewAI Task Contracts

The primary Flow editor is an ordered stage list with a selected-stage inspector. The visual canvas is an optional desktop projection of the same data, never a second schema.

### LangGraph stage fields

- stable node ID and human title;
- entry condition and required case state;
- required evidence and source receipts;
- selected role and reviewer;
- pass, repair, approval-wait, block, and stop routes;
- maximum attempts and maximum same-failure count;
- checkpoint policy;
- side effects and rollback;
- output receipt type.

Gate nodes use a distinct interlock treatment and always answer: **what is checked, which evidence proves it, who decides, what happens on failure, and what remains prohibited**.

### CrewAI task fields

- task ID and purpose;
- role call name plus stable role ID;
- allowed context projection;
- allowed tools and skills;
- dependencies and parallel file claim;
- expected output schema;
- acceptance criteria;
- reviewer route;
- provider/memory/cache/planning state;
- handoff and receipt.

Safe defaults are sequential process, memory off, provider off, planning off, cache only when freshness policy allows it, no external action, and a separate reviewer for high-risk output. CrewAI organizes the contract; LangGraph owns case state, route, repair, and approval interrupts.

## Embedded Operator / Jarvis Treatment

The button label is **Operator**. The drawer header reads:

`Operator · Jarvis guidance`

`Explains this case. Cannot execute, approve, or expand access.`

The drawer always receives the current `case_id`, selected section, validation errors, public-safe source descriptors, and unsaved-change summary. It does not receive browser chat history, arbitrary file bodies, raw private paths, or provider credentials.

Operator actions are constrained verbs:

- Explain this field.
- Find missing responsibility.
- Compare draft to safe defaults.
- Draft reviewer questions.
- Prepare a public-safe review packet.
- Show the exact bridge payload.

There is no generic implicit send. **Prepare** builds a local preview. **Send to local bridge** is a separate action that displays destination class, fields, byte size, source handles, provider state, writeback state, and excluded fields. The operator must confirm that exact payload. Every response states whether it is local guidance, bridge validation, or a verified receipt.

## Public-Safe Config Import And Export

### Three distinct downloads

1. **Configuration draft** — editable settings and compatibility metadata; status `configured_not_executed`.
2. **Review packet** — normalized diff, validation result, evidence requirements, owner questions, and proposed changes; status `review_required_not_executed`.
3. **Receipt bundle** — immutable projection of receipts already present; it never upgrades their proof state.

All three use a versioned envelope such as:

```text
schema: archflow.crew-studio.v1
kind: configuration | review_packet | receipt_bundle
case_id: opaque public-safe ID
truth_state: configured_not_executed
config_digest: sha256 of canonical public-safe fields
sections: sources, retrieval, roles, skills, graph, crew_tasks, bridge_requirements
excluded: secrets, raw source text, private paths, chat history, action tokens
```

### Import sequence

1. Select one `.json` packet explicitly.
2. Parse in memory; apply a strict size cap and schema/version allowlist.
3. Reject the entire packet if forbidden key names or secret-shaped values appear. Show JSON pointers and reason, never the rejected values.
4. Normalize stable IDs and legacy aliases without upgrading status.
5. Validate cross-references, role/reviewer separation, source boundary, retrieval rules, gate routes, and receipt state.
6. Show a section-by-section diff: Added, Changed, Removed, Conflict, or Ignored.
7. Require explicit choices for conflicts. Default to keeping the current value.
8. Save only a public-safe local draft and one rollback snapshot.
9. Revalidate and export; repository files remain unchanged.

Import never accepts `.env`, YAML with secret-bearing provider fields, arbitrary source documents, receipt claims without their evidence, or a packet whose schema is newer than the supported reader. An older supported version gets a migration preview and retains original compatibility metadata.

## Local Bridge Setup Without Browser Secrets

### Safe connection contract

- The bridge binds to loopback only unless a separately reviewed deployment exists.
- The dashboard accepts only its own origin or an allowlisted loopback origin.
- Provider keys, vault credentials, tokens, cookies, private paths, and raw source contents remain in the bridge process, OS keychain, or ignored server environment.
- The dashboard has no credential, token, key, or password field.
- Pairing occurs through an explicit local action outside the page. The recommended browser session is an `HttpOnly`, `SameSite=Strict` cookie scoped by the bridge; JavaScript must not be able to read a bearer secret.
- CORS allows the exact dashboard origin, rejects `null` and wildcard origins, and limits methods and headers.
- Requests use opaque source/capability handles and public-safe packets. Responses return capability metadata and sanitized receipts, not filesystem paths or raw private bodies.
- A bridge reporting provider or writeback enabled when the case expects disabled is treated as incompatible and blocked.

### Setup flow

1. The page opens **Disconnected — configuration still available**. It does not poll a bridge automatically.
2. The administrator starts the approved bridge using its documented local command and completes any out-of-browser pairing.
3. In **Bridge**, choose Same origin or Loopback and enter only the origin. The UI rejects paths, query strings, embedded credentials, non-loopback HTTP hosts, and unapproved origins.
4. **Test connection** requests health, version, schema versions, provider state, writeback state, supported validators, source-handle classes, and receipt capability.
5. The Studio displays the exact capabilities and mismatches. Nothing is enabled automatically.
6. **Accept capabilities for this session** stores only the safe origin, bridge fingerprint, expiry, and capability IDs.
7. A validation request shows the exact public-safe payload before send and records a bridge health/validation receipt after response.

## Safe Defaults

| Area | Default |
|---|---|
| Provider | Disabled; no browser provider controls. |
| Writeback and external action | Disabled; target-specific approval required later. |
| Bridge | Disconnected; manual health check only. |
| Browser persistence | Session-only draft by default; explicit “keep public-safe draft on this device” opt-in. |
| Chat/history | No persistent free-form chat history. |
| Raw source content | Never stored or displayed by the public Studio. |
| Retrieval | Approved corpus only; source paths required; lexical fallback locked on. |
| TurboVec | Candidate off; promotion controls hidden until benchmark receipts pass. |
| CrewAI | Sequential; memory off; provider off; planning off. |
| LangGraph repair | Maximum three attempts; stop after the same failure twice. |
| Roles | Least privilege; output and reviewer required; maker cannot approve own high-risk output. |
| Knowledge promotion | Blocked until accepted result, lineage, freshness, supersession, and independent review exist. |
| Export | `configured_not_executed` unless a stronger receipt is imported and verified without status inflation. |

## Error And Empty States

| State | UI response | Recovery |
|---|---|---|
| No case | Calm empty state with “Import public-safe case” and “Create local draft”. | Create/import; no bridge required. |
| Dashboard data unavailable | Preserve the shell, show last verified timestamp if one exists, and mark all runtime cards Unknown. | Retry or import a validated packet. |
| Storage unavailable/quota exceeded | Keep the draft in memory; show a persistent warning before navigation. | Export now or clear an explicit public-safe draft. |
| Import malformed | Block before mutation; list schema errors by JSON pointer. | Fix externally or choose another packet. |
| Forbidden key/value detected | Reject whole import and never echo the value. | Use a sanitized config export. |
| Unsupported version | No partial application. | Use a supported migrator or update the Studio. |
| Source denied | Show source class and policy reason only. | Remove it or obtain a reviewed source-boundary decision. |
| Retrieval invalid | Mark the exact fields and the downstream effect. | Restore safe defaults or correct values. |
| Role self-review or overlapping claim | Block validation and highlight both contracts. | Assign Halyna or another valid independent reviewer contract; give one maker the shared target. |
| Orphan/looping graph route | Focus the affected stage and show the missing terminal/repair path. | Repair route and revalidate. |
| Bridge unreachable | Keep all drafting available; never imply runtime failure. | Check local process/origin, then test again. |
| Bridge incompatible | Display expected versus received version/capability without accepting it. | Update bridge or choose a compatible profile. |
| Provider/writeback unexpectedly enabled | Red interlock; no payload leaves the page. | Disable it server-side and obtain a fresh health receipt. |
| Receipt stale or digest mismatch | Keep visible but label Unverified/Stale. | Re-run the named check and attach a new receipt. |

Errors use `role="alert"` only when action is blocked. Non-blocking validation and connection progress use a small `role="status"` region. Focus moves to the error summary after submit and each summary item links to the invalid field.

## Receipt Design

The Receipts view is a filterable chronological ledger with these required fields:

- receipt ID, case ID, receipt type, schema version, and UTC timestamp;
- truth state: configured, validated, executed, verified, approved, blocked, or stale;
- actor call name plus stable role ID;
- independent reviewer call name plus stable role ID when required;
- config digest and parent/superseded receipt;
- source handles and evidence references;
- checks, results, repair attempt, and same-failure count;
- provider-call count and writeback count;
- exact action/target class, side effects, rollback, and readback when execution is actually proved;
- output references and next safe action.

Browser-created receipts are labeled **Local / unsigned / not execution proof**. Bridge or runtime receipts are labeled by their actual verifier and verification method. The UI never presents a hash as approval, a successful command as acceptance, or a configuration as execution.

## Accessibility Contract

- One `h1` per route, logical heading order, and landmarks for header, primary navigation, main editor, context pane, and Operator drawer.
- Skip links to main editor, section navigation, and Operator.
- Explicit `label[for]` and control IDs. Repeated role fields include the call name in the accessible description.
- `fieldset` and `legend` for role, source, retrieval, bridge, and gate groups.
- `aria-describedby` for help/error text; `aria-invalid` only after validation.
- Dedicated small live regions. Never place the entire route container in `aria-live`.
- Native buttons for actions; no `role="button"` when a button can be used.
- Keyboard reorder controls and stage list provide full graph editing without drag.
- Modal/drawer focus trap, initial focus on the heading or first error, Escape close, inert background, and focus restoration.
- Table captions, `scope="col"`, responsive card labels, and named focusable scroll regions.
- Visible focus at least 3px; 44px targets; no focus obscured by sticky headers.
- Status icon plus text, WCAG AA contrast, reduced motion, forced-colors support, and no essential animation.
- Verification at keyboard-only, 200% zoom, 400% zoom/reflow, reduced motion, and screen-reader landmark/form navigation.

## Verification Checklist

### Deterministic structure

- [ ] Dashboard HTML parses and exposes one case entry point.
- [ ] JavaScript syntax passes.
- [ ] Data/config/receipt fixtures parse against versioned schemas.
- [ ] Generated role projection contains exactly 21 canonical stable IDs and 21 unique Ukrainian call names.
- [ ] No legacy alias appears as the primary human-facing role name.
- [ ] Source, retrieval, role, skill, graph, task, bridge, and receipt cross-references validate.
- [ ] Public-safety and secret/path scans pass on source, fixtures, and rendered DOM snapshots.

### Responsive and visual

- [ ] Screenshots at 360×800, 390×844, 768×1024, 1024×768, 1280×800, 1440×900, and 1920×1080.
- [ ] `document.documentElement.scrollWidth === document.documentElement.clientWidth` on every normal route.
- [ ] Only named graph/matrix regions may scroll horizontally.
- [ ] No clipped border or asymmetric gutter at 360/390px.
- [ ] Form fields remain at least 280px when placed side by side; otherwise they stack.
- [ ] Long IDs, paths, hashes, skill names, and receipt messages wrap without covering controls.
- [ ] Mobile stage sheet exposes every field and action with one vertical scroll owner.
- [ ] Operator drawer and sticky bars do not obscure focused content or the final receipt row.

### Interaction and state

- [ ] Dirty, saved-local, validated, review-required, blocked, stale, and verified states are distinguishable by text and icon.
- [ ] Import follows parse → scan → normalize → diff → confirm → validate; invalid import changes nothing.
- [ ] One-click rollback restores the prior public-safe local draft.
- [ ] Config, review, and receipt exports are separate and preserve truth state.
- [ ] Browser reload does not silently upgrade, execute, or promote a draft.
- [ ] Admin/Guest wording is removed or explicitly renamed Preview; no view mode implies authentication.

### Bridge and privacy

- [ ] No credential, password, provider key, owner token, cookie, private path, or raw-source field exists in the DOM.
- [ ] Only same-origin or allowlisted loopback origins pass validation.
- [ ] Initial load makes zero bridge, provider, or writeback requests.
- [ ] Connection test sends no case/source body.
- [ ] Every later send requires exact payload preview and explicit confirmation.
- [ ] CORS wildcard, null origin, embedded URL credentials, remote HTTP host, and provider-enabled mismatch fail closed.
- [ ] Export excludes raw text, chat history, secrets, tokens, absolute paths, private URLs, account IDs, and runtime databases.
- [ ] Browser-local receipts identify themselves as unsigned and non-execution proof.

### Accessibility

- [ ] Automated accessibility scan returns no critical/serious findings.
- [ ] Keyboard-only flow completes source configuration, role editing, stage reordering, validation, import diff, bridge test, and export.
- [ ] Screen reader announces page title, section, changed status, field error, dialog open/close, and receipt result once.
- [ ] Every table has a caption and scoped headers.
- [ ] Every repeated field has a unique accessible name and description.
- [ ] 200% zoom retains two-column layouts only when they fit; 400% reflows to one column without page-level horizontal scroll.
- [ ] Reduced-motion and forced-colors modes preserve state and focus visibility.

### Checks Completed In This Lane

- PASS — `node --check project/dashboard/app.js`.
- PASS — `project/dashboard/data.json` parses as JSON.
- PASS — static source audit counted the current route and CSS-cascade surface and confirmed no committed config-import marker.
- GAP — current headless Chrome smoke could not start in this sandbox (`Operation not permitted`); no new rendered screenshot or accessibility verdict is claimed.

## Trade-offs

- Crew Studio is deeper than an employee task desk. Progressive disclosure, safe presets, consequence previews, and a guided setup checklist are required to prevent administrator fatigue.
- Keeping secrets and raw private sources out of the browser limits rich preview. The benefit is a cleaner public/private boundary; the cost is dependence on sanitized bridge receipts and exact-source handles.
- A stage-list-first editor is less visually free than a canvas. It is more reliable for keyboard, mobile, validation, diffing, and deterministic export. The canvas remains a desktop projection.
- Import diffing and receipt truth states add implementation work, but they prevent silent overwrite and proof inflation—both core risks for a self-hosted administration plane.
- Browser-local drafting remains a convenience, not a source of truth. Versioned repository contracts and reviewed runtime receipts still own durable state.

## Final Recommendation To The Integrator

Adopt the Crew Studio structure for the **administrator/configuration mode** of the unified dashboard: one case bar; Sources, Crew, Flow, Bridge, and Receipts; a stage-list-first workflow editor; and one contextual Operator drawer. Preserve the strongest existing pieces—skip/focus behavior, keyboard node movement, dialog focus management, source-boundary language, and browser-local export—but replace the accumulated route map, duplicated responsive cascade, implicit Jarvis send path, persistent free-form chat, and export-only configuration model.

The minimum integration slice should include: canonical role/call-name projection, safe retrieval defaults, role and task contract editors, LangGraph gate validation, separate config/review/receipt packets, manual loopback bridge health with no credentials in the page, and mobile/a11y checks that measure overflow instead of hiding it.

## Repo-Relative Evidence

- `project/runs/20260805-responsive-knowledge-crew-dashboard/task-contract.md`
- `project/runs/20260805-responsive-knowledge-crew-dashboard/context-capsule.json`
- `docs/unified-operating-architecture.md`
- `docs/dashboard-integration-plan.md`
- `project/system/contracts/operating-model.json`
- `project/system/contracts/role-catalog.json`
- `project/workflows/langgraph-controller.yaml`
- `project/workflows/crewai-crew.yaml`
- `project/workflows/llamaindex-rag.yaml`
- `project/agents/skills-governance.md`
- `project/dashboard/index.html`
- `project/dashboard/styles.css`
- `project/dashboard/app.js`
- `project/dashboard/data.json`
- `project/scripts/dashboard-static-smoke.py`
- `project/reports/20260715-architecture-test-results.md`
