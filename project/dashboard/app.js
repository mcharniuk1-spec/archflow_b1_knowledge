/* ArchFlow Knowledge Operator V3
 *
 * Public, provider-disabled dashboard projection. The browser can prepare and
 * download bounded packets; it cannot fetch a repository, run an agent,
 * authorize a provider, write a file, or perform an external action.
 */

const REPOSITORY_URL = "https://github.com/mcharniuk1-spec/archflow_b1_knowledge";
const HOSTED_ORIGIN = "https://www.arch-flow.dev";
const STORAGE_PREFIX = "archflow.public.v3.";
const STORAGE = {
  migration: `${STORAGE_PREFIX}legacy-cleared`,
  caseDraft: `${STORAGE_PREFIX}case-draft`,
  events: `${STORAGE_PREFIX}events`,
  handoff: `${STORAGE_PREFIX}handoff`,
};

const PRIMARY_ROUTES = [
  { id: "manual", label: "Documentation", glyph: "01" },
  { id: "operations", label: "Project", glyph: "02" },
  { id: "agents", label: "Roles & Skills", glyph: "03" },
  { id: "setup", label: "Setup", glyph: "04" },
  { id: "runs", label: "Evidence", glyph: "05" },
];

const TECHNICAL_ROUTES = [
  { id: "architecture", label: "Four Schemas", glyph: "AR" },
  { id: "knowledge", label: "Knowledge & Memory", glyph: "KM" },
  { id: "workflow", label: "Research → Define → Act", glyph: "WF" },
  { id: "configuration", label: "Configuration", glyph: "CF" },
];

const ROUTES = [...PRIMARY_ROUTES, ...TECHNICAL_ROUTES, { id: "communication", label: "Communication", glyph: "CM", hidden: true }];
const ROUTE_ALIASES = {
  today: "manual",
  overview: "architecture",
  case: "operations",
  service: "workflow",
  schema: "workflow",
  config: "configuration",
  data: "configuration",
  reference: "manual",
  llamaindex: "knowledge",
  crewai: "agents",
  langgraph: "workflow",
  gates: "runs",
  jarvis: "communication",
};

const PAGE_META = {
  manual: {
    kicker: "Product documentation",
    title: "Start with one bounded decision",
    description: "Use a clear source boundary, accountable roles, visible state, independent review, and maintained knowledge to move from research to action without losing control.",
  },
  operations: {
    kicker: "Project dashboard",
    title: "Frame the work before agents touch it",
    description: "Prepare one public-safe case contract, inspect its state, and route it to the Communication Center for review.",
  },
  communication: {
    kicker: "Communication Center",
    title: "Turn Jarvis input into an inspectable handoff",
    description: "Review browser-local work packets, notifications, owners, reviewers, stop conditions, and the next safe action in one place.",
  },
  agents: {
    kicker: "Actionable roles and portable skills",
    title: "Assign responsibility, not personalities",
    description: "Each role has a bounded job, allowed inputs, expected output, reviewer, escalation rule, and stop condition.",
  },
  setup: {
    kicker: "Individual and team setup",
    title: "Run the zero-key core first",
    description: "Start with the static dashboard and deterministic validators. Add authentication, local retrieval, providers, and observability only through separate gates.",
  },
  runs: {
    kicker: "Measured evidence",
    title: "Publish comparators, not impressive-sounding claims",
    description: "Every metric names its fixture, denominator, comparator, date, and limitation. Missing proof remains a gap.",
  },
  architecture: {
    kicker: "Four architecture schemas",
    title: "See how context, work, proof, and learning connect",
    description: "The four diagrams are distributed across the dashboard by user task and remain available together here at full resolution.",
  },
  knowledge: {
    kicker: "Bounded knowledge system",
    title: "Keep useful memory without keeping everything",
    description: "Stable rules, approved sources, task retrieval, exact reads, receipts, and reviewed promotion have different jobs and retention boundaries.",
  },
  workflow: {
    kicker: "State-driven execution",
    title: "Research, define, act, review, remember",
    description: "A typed state envelope carries evidence and decisions through bounded loops; an action gate remains separate from authentication and planning.",
  },
  configuration: {
    kicker: "Explicit configuration",
    title: "Know which layer each setting changes",
    description: "The public repository stores schemas, defaults, and environment-variable names—never credential values, identity allowlists, or local project context.",
  },
};

const DIAGRAMS = [
  {
    id: "tower",
    source: "../assets/architecture/knowledge-crew-tower.svg",
    title: "Seven-layer knowledge crew",
    placement: "System map",
    description: "Shows source systems, seven accountable operating layers, and the verified output each layer must hand forward.",
  },
  {
    id: "input",
    source: "../assets/architecture/context-input-flow.svg",
    title: "Input and perception flow",
    placement: "Knowledge & Memory",
    description: "Shows how stable rules, role responsibility, current requirements, retrieved evidence, exact reads, and gaps become a source-visible context capsule.",
  },
  {
    id: "output",
    source: "../assets/architecture/output-receipt-flow.svg",
    title: "Output, validation, and receipts",
    placement: "Evidence",
    description: "Shows how candidate work passes requirement, authority, maker-check, independent-review, exact-action, readback, and knowledge-promotion gates.",
  },
  {
    id: "teamwork",
    source: "../assets/architecture/onboarding-teamwork-flow.svg",
    title: "Onboarding and teamwork",
    placement: "Roles & Communication",
    description: "Shows orientation, the first mission, role-safe context, the smallest responsible crew, review, learning, interrupts, and repair handoffs.",
  },
];

const DEFAULT_CASE = {
  schema_version: "3.0",
  kind: "archflow_public_case",
  objective: "",
  decision: "",
  public_reference: "",
  allowed_evidence: "Public documentation and explicitly approved source summaries.",
  exclusions: "Credentials, private URLs, customer material, raw transcripts, and local paths.",
  requested_output: "",
  reviewer: "Independent reviewer",
  constraints: "No provider calls or external writes. Stop when evidence, authority, or the source boundary is unclear.",
  state: "draft",
  updated_at: null,
};

const DEFAULT_DATA = {
  schema_version: "3.0",
  generated_at: null,
  product: {
    category: "Knowledge continuity and agent operations",
    description: "ArchFlow is a public, local-first operating kit for turning a bounded objective and approved evidence into an inspectable plan, a role-safe execution path, independent review, and maintained knowledge. It gives individuals and teams one shared structure for research, definition, action, validation, handoff, and learning without treating a model response as proof that work happened.",
    audience: "Founders, operators, product teams, researchers, and small delivery teams that need repeatable AI-assisted work without hidden state or uncontrolled context.",
    pains: [
      { title: "Context resets", description: "People and agents repeatedly rebuild the same background because decisions, sources, and superseded assumptions are mixed together." },
      { title: "Unclear ownership", description: "Agent names and long prompts do not establish who owns an output, who reviews it, or when work must stop." },
      { title: "Invisible execution", description: "A chat response can look finished even when no file, check, approval, action, or readback exists." },
      { title: "Tool sprawl", description: "Providers, retrieval systems, and automations are added before their data boundary, budget, rollback, and failure mode are understood." },
      { title: "Unmaintained memory", description: "Raw history grows while current guidance becomes harder to find, verify, and supersede." },
    ],
  },
  workflow: [
    { step: "01", title: "Research", description: "Admit a bounded source set, label evidence and gaps, and preserve provenance." },
    { step: "02", title: "Define", description: "State the decision, acceptance criteria, authority, roles, outputs, and stop conditions." },
    { step: "03", title: "Act", description: "Run the smallest responsible route and keep external effects behind a separate approval gate." },
    { step: "04", title: "Review", description: "Freeze the candidate and verify it independently against requirements and deterministic checks." },
    { step: "05", title: "Remember", description: "Promote only reusable conclusions with source lineage, owner, freshness, and supersession." },
  ],
  role_catalog: { roles: [] },
  skill_catalog: { items: [], packaged_count: 0 },
  performance_evidence: {
    measured_at: null,
    metrics: [
      { label: "Context input", value: "98.6% lower", comparator: "Top-five lexical chunks versus four full-manifest packets; 15,001 vs 1,055,632 UTF-8 bytes.", limitation: "Fixed input-byte fixture; not billed tokens, memory, latency, or answer quality." },
      { label: "Role activation", value: "75.0% fewer", comparator: "Smallest declared role packs versus all-role fan-out; 21 vs 84 role slots.", limitation: "Contract selection; not wall-clock speed, labor saved, or throughput." },
      { label: "Source recall", value: "4/4", comparator: "Expected canonical source in deterministic lexical top five.", limitation: "Source-hit fixture; not production answer accuracy." },
      { label: "Semantic gates", value: "8/8", comparator: "Expected decision for one valid and seven unsafe or incomplete packets.", limitation: "Bounded fixtures; not a real-world safety rate." },
    ],
  },
};

const view = document.querySelector("#view");
const nav = document.querySelector("#nav");
const pageKicker = document.querySelector("#pageKicker");
const pageTitle = document.querySelector("#pageTitle");
const pageDescription = document.querySelector("#pageDescription");
const generatedAt = document.querySelector("#generatedAt");
const liveStatus = document.querySelector("#liveStatus");
const refreshButton = document.querySelector("#refreshData");
const adminButton = document.querySelector("#adminAccess");
const jarvisLink = document.querySelector("#jarvisLink");

let data = null;
let activeRoute = normalizeRoute(window.location.hash.replace(/^#/, "") || "manual");
let caseDraft = loadJson(STORAGE.caseDraft, DEFAULT_CASE);
let authSession = { authenticated: false, role: "public", csrf: "" };
let importedHandoff = null;

function normalizeRoute(value) {
  const candidate = ROUTE_ALIASES[value] || value;
  return ROUTES.some((route) => route.id === candidate) ? candidate : "manual";
}

function escapeHtml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function safeArray(value) {
  return Array.isArray(value) ? value : [];
}

function loadJson(key, fallback) {
  try {
    const parsed = JSON.parse(localStorage.getItem(key) || "null");
    return parsed && typeof parsed === "object" ? { ...fallback, ...parsed } : { ...fallback };
  } catch (_error) {
    return { ...fallback };
  }
}

function saveCase() {
  localStorage.setItem(STORAGE.caseDraft, JSON.stringify(caseDraft));
}

function clearLegacyBrowserMemory() {
  if (localStorage.getItem(STORAGE.migration) === "complete") return;
  const legacyPrefixes = ["archflow.jarvis.", "archflow.dashboard.", "archflow.crewDesk."];
  const legacyExact = new Set(["archflow.sharedSession"]);
  for (let index = localStorage.length - 1; index >= 0; index -= 1) {
    const key = localStorage.key(index);
    if (key && (legacyExact.has(key) || legacyPrefixes.some((prefix) => key.startsWith(prefix)))) {
      localStorage.removeItem(key);
    }
  }
  localStorage.setItem(STORAGE.migration, "complete");
}

function protocolAwareJarvisUrl() {
  return window.location.protocol === "file:" ? "../../jarvis.html" : "/jarvis.html";
}

function authStartUrl() {
  const isHosted = window.location.origin === HOSTED_ORIGIN;
  return isHosted ? "/api/auth/google/start" : `${HOSTED_ORIGIN}/api/auth/google/start`;
}

function formatDate(value) {
  if (!value) return "static public projection";
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? "static public projection" : date.toLocaleString();
}

function badge(value, tone = "neutral") {
  return `<span class="badge ${escapeHtml(tone)}">${escapeHtml(value)}</span>`;
}

function table(headers, rows) {
  return `<div class="table-wrap"><table><thead><tr>${headers.map((header) => `<th>${escapeHtml(header)}</th>`).join("")}</tr></thead><tbody>${rows.map((row) => `<tr>${row.map((cell) => `<td>${cell}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`;
}

function diagramCard(diagram, compact = false) {
  return `<article class="diagram-card-v3 ${compact ? "compact" : ""}">
    <a class="diagram-preview-v3" href="${diagram.source}" target="_blank" rel="noreferrer">
      <img src="${diagram.source}" alt="${escapeHtml(`${diagram.title}. ${diagram.description}`)}" loading="lazy" />
    </a>
    <div class="diagram-copy-v3"><span class="eyebrow">${escapeHtml(diagram.placement)}</span><h3>${escapeHtml(diagram.title)}</h3><p>${escapeHtml(diagram.description)}</p><a class="button" href="${diagram.source}" target="_blank" rel="noreferrer">Open full-resolution SVG</a></div>
  </article>`;
}

function eventRecord(title, detail, tone = "ok") {
  const events = loadEventList();
  events.unshift({ title: String(title).slice(0, 100), detail: String(detail).slice(0, 500), tone, at: new Date().toISOString() });
  localStorage.setItem(STORAGE.events, JSON.stringify(events.slice(0, 20)));
}

function loadEventList() {
  try {
    const parsed = JSON.parse(localStorage.getItem(STORAGE.events) || "[]");
    return Array.isArray(parsed) ? parsed : [];
  } catch (_error) {
    return [];
  }
}

function validateHandoff(raw) {
  if (!raw || typeof raw !== "object") return null;
  const clean = {
    schema_version: "3.0",
    kind: "archflow_public_handoff",
    objective: String(raw.objective || "").trim().slice(0, 1200),
    decision: String(raw.decision || "").trim().slice(0, 1200),
    public_reference: String(raw.public_reference || "").trim().slice(0, 500),
    allowed_evidence: String(raw.allowed_evidence || "").trim().slice(0, 1800),
    exclusions: String(raw.exclusions || "").trim().slice(0, 1800),
    requested_output: String(raw.requested_output || "").trim().slice(0, 1000),
    reviewer: String(raw.reviewer || "Independent reviewer").trim().slice(0, 300),
    constraints: String(raw.constraints || "").trim().slice(0, 1800),
    created_at: String(raw.created_at || "").slice(0, 80),
    state: "review_required",
  };
  return clean.objective && clean.requested_output ? clean : null;
}

function readHandoff() {
  if (importedHandoff) return importedHandoff;
  try {
    importedHandoff = validateHandoff(JSON.parse(sessionStorage.getItem(STORAGE.handoff) || "null"));
    sessionStorage.removeItem(STORAGE.handoff);
    return importedHandoff;
  } catch (_error) {
    sessionStorage.removeItem(STORAGE.handoff);
    return null;
  }
}

function downloadJson(filename, payload) {
  const blob = new Blob([`${JSON.stringify(payload, null, 2)}\n`], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = filename;
  document.body.appendChild(anchor);
  anchor.click();
  anchor.remove();
  URL.revokeObjectURL(url);
}

function renderNav() {
  const primary = PRIMARY_ROUTES.map((route) => `<button type="button" class="${activeRoute === route.id ? "active" : ""}" data-route="${route.id}"><span class="glyph">${route.glyph}</span><span>${escapeHtml(route.label)}</span></button>`).join("");
  const technical = TECHNICAL_ROUTES.map((route) => `<button type="button" class="${activeRoute === route.id ? "active" : ""}" data-route="${route.id}"><span class="glyph">${route.glyph}</span><span>${escapeHtml(route.label)}</span></button>`).join("");
  nav.innerHTML = `<div class="nav-group"><span class="nav-group-label">Workspace</span>${primary}</div><details class="nav-details" ${TECHNICAL_ROUTES.some((route) => route.id === activeRoute) ? "open" : ""}><summary>Technical views</summary><div class="secondary">${technical}</div></details><a class="nav-jarvis-link" href="${protocolAwareJarvisUrl()}"><span class="glyph">JV</span><span><strong>Jarvis</strong><small>Prepare a public-safe handoff</small></span></a>`;
  nav.querySelectorAll("[data-route]").forEach((button) => button.addEventListener("click", () => navigate(button.dataset.route)));
}

function navigate(route) {
  activeRoute = normalizeRoute(route);
  if (window.location.hash.replace(/^#/, "") !== activeRoute) window.location.hash = activeRoute;
  render();
  view.focus({ preventScroll: true });
  window.scrollTo({ top: 0, behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" });
}

function renderHeader() {
  const meta = PAGE_META[activeRoute] || PAGE_META.manual;
  pageKicker.textContent = meta.kicker;
  pageTitle.textContent = meta.title;
  pageDescription.innerHTML = `<span>${escapeHtml(meta.description)}</span>`;
  generatedAt.textContent = `Generated ${formatDate(data?.generated_at)}`;
  liveStatus.textContent = "Provider-disabled public core";
  liveStatus.className = "pill live-pill ok";
  adminButton.textContent = authSession.authenticated ? "Admin verified · Sign out" : "Admin access";
  adminButton.setAttribute("aria-label", authSession.authenticated ? "Administrator session verified. Sign out." : "Sign in with the configured administrator account");
  jarvisLink.href = protocolAwareJarvisUrl();
}

function renderManual() {
  const product = data.product || DEFAULT_DATA.product;
  const pains = safeArray(product.pains).length ? product.pains : DEFAULT_DATA.product.pains;
  const workflow = safeArray(data.workflow).length ? data.workflow : DEFAULT_DATA.workflow;
  view.innerHTML = `
    <section class="product-hero" aria-labelledby="product-title">
      <div class="product-hero-copy"><span class="eyebrow">${escapeHtml(product.category || DEFAULT_DATA.product.category)}</span><h2 id="product-title">A practical operating system for human + agent work.</h2><p class="product-description">${escapeHtml(product.description || DEFAULT_DATA.product.description)}</p><div class="hero-actions"><a class="primary" href="#operations">Start a project case</a><a class="button" href="#architecture">See the four schemas</a><a class="button" href="${REPOSITORY_URL}" target="_blank" rel="noreferrer">GitHub repository</a></div></div>
      <aside class="product-position"><span class="product-index">AF / B1</span><strong>Designed for individual operators and small teams.</strong><p>${escapeHtml(product.audience || DEFAULT_DATA.product.audience)}</p><div class="product-state-row"><span>Core</span><b>Zero-key and local-first</b></div><div class="product-state-row"><span>State</span><b>Visible and reviewable</b></div><div class="product-state-row"><span>Providers</span><b>Off by default</b></div><div class="product-state-row"><span>Memory</span><b>Curated, not accumulated</b></div></aside>
    </section>
    <section class="product-section"><div class="product-section-heading"><span class="eyebrow">Why it exists</span><h2>The hard part is not generating output. It is preserving the chain from evidence to decision.</h2><p>ArchFlow removes repeated context reconstruction, unclear agent ownership, invisible execution, uncontrolled integrations, and raw history that masquerades as useful memory.</p></div><div class="pain-grid">${pains.map((pain, index) => `<article class="pain-card"><span>${String(index + 1).padStart(2, "0")}</span><h3>${escapeHtml(pain.title)}</h3><p>${escapeHtml(pain.description)}</p></article>`).join("")}</div></section>
    <section class="product-section journey-section"><div class="product-section-heading"><span class="eyebrow">Operating sequence</span><h2>Research → define → act → review → remember.</h2><p>Every stage has an input, owner, expected output, stop condition, and evidence requirement. Authentication identifies an administrator; it never replaces approval for provider use, Git, deployment, spend, or writeback.</p></div><div class="journey-grid">${workflow.map((item) => `<article class="journey-card"><span>${escapeHtml(item.step)}</span><h3>${escapeHtml(item.title)}</h3><p>${escapeHtml(item.description)}</p></article>`).join("")}</div><div class="journey-actions"><a class="primary" href="#operations">Prepare one case</a><a class="button" href="#communication">Open Communication Center</a><a class="button" href="#setup">Set up the tool</a></div></section>
    <section class="product-section"><div class="product-section-heading"><span class="eyebrow">How to read the system</span><h2>Four schemas, each placed where it helps a user decide.</h2><p>The diagrams are not decoration and do not claim runtime activity. Each explains one operational relationship, while the surrounding text supplies the actionable instructions.</p></div><div class="diagram-grid-v3">${DIAGRAMS.map((diagram) => diagramCard(diagram, true)).join("")}</div></section>
    <section class="product-section boundary-section"><div class="product-section-heading"><span class="eyebrow">Public boundary</span><h2>Useful by default. Powerful only after proof.</h2><p>The repository ships generic contracts, portable skills, schemas, validators, documentation, and public-safe examples. It does not ship personal memory, client context, credentials, local paths, raw transcripts, or implicit authority.</p></div><div class="boundary-grid"><article><h3>Browser</h3><p>Prepares local drafts, handoffs, and downloads. It does not fetch repositories or run providers.</p></article><article><h3>Runtime</h3><p>LangGraph owns state; roles own bounded outputs; independent review remains separate.</p></article><article><h3>Integrations</h3><p>Environment names are documented. Values stay server-side and every activation is gated.</p></article><article><h3>Memory</h3><p>Only reviewed reusable meaning is promoted with lineage, freshness, and supersession.</p></article></div></section>`;
}

function renderOperations() {
  view.innerHTML = `
    <section class="docs-hero compact"><div><span class="eyebrow">One case spine</span><h2>Define the decision, evidence, output, reviewer, and stop rule.</h2></div><p>This form is browser-local. A public reference is a label only: the dashboard does not fetch, clone, inspect, upload, or send it.</p></section>
    <div class="docs-grid two project-layout-v3">
      <form class="panel case-form-v3" id="caseForm"><div class="section-header"><div><span class="eyebrow">Case contract</span><h2 class="section-title">Prepare a bounded case</h2></div>${badge(caseDraft.state || "draft", caseDraft.state === "review_required" ? "warn" : "neutral")}</div>
        ${field("objective", "Objective", "What outcome should this case produce?", caseDraft.objective, true)}
        ${field("decision", "Decision supported", "What decision will the output help someone make?", caseDraft.decision)}
        ${field("public_reference", "Public repository reference or safe label", "https://github.com/example/project or a non-sensitive label", caseDraft.public_reference)}
        ${field("allowed_evidence", "Allowed evidence", "Name the exact public or approved source boundary.", caseDraft.allowed_evidence, false, true)}
        ${field("exclusions", "Excluded material", "Credentials, private files, raw transcripts, unpublished data…", caseDraft.exclusions, false, true)}
        ${field("requested_output", "Requested output", "Architecture report, research brief, implementation plan…", caseDraft.requested_output, true)}
        ${field("reviewer", "Independent reviewer", "A role or team, never the maker self-approving", caseDraft.reviewer)}
        ${field("constraints", "Constraints and stop conditions", "Authority, budget, safety, delivery, and rollback boundaries", caseDraft.constraints, false, true)}
        <div class="row-actions case-actions-v3"><button class="primary" type="submit">Prepare review packet</button><button class="button" id="resetCase" type="button">Reset draft</button><button class="button" id="downloadCase" type="button">Download JSON</button></div>
      </form>
      <div class="project-side-v3"><section class="panel"><span class="eyebrow">State trace</span><h2 class="section-title">What happens next</h2><ol class="state-list-v3"><li><strong>Frame</strong><span>Objective, decision, authority, source boundary.</span></li><li><strong>Ground</strong><span>Evidence, provenance, contradictions, gaps.</span></li><li><strong>Define</strong><span>Roles, outputs, checks, reviewer, stop conditions.</span></li><li><strong>Act</strong><span>Smallest bounded route; side effects remain gated.</span></li><li><strong>Verify</strong><span>Requirements, deterministic checks, independent verdict.</span></li><li><strong>Remember</strong><span>Promote reusable meaning only after review.</span></li></ol></section><section class="panel"><span class="eyebrow">Handoff</span><h2 class="section-title">Communication is part of execution</h2><p>Jarvis and this case form return structured packets to one Communication Center. Nothing is hidden in a URL or treated as durable memory.</p><div class="row-actions"><a class="primary" href="#communication">Open Communication Center</a><a class="button" href="${protocolAwareJarvisUrl()}">Open Jarvis</a></div></section></div>
    </div>`;
  bindCaseForm();
}

function field(name, label, placeholder, value, required = false, multiline = false) {
  const control = multiline ? `<textarea id="${name}" name="${name}" rows="4" placeholder="${escapeHtml(placeholder)}" ${required ? "required" : ""}>${escapeHtml(value)}</textarea>` : `<input id="${name}" name="${name}" type="text" placeholder="${escapeHtml(placeholder)}" value="${escapeHtml(value)}" ${required ? "required" : ""} />`;
  return `<label class="field-v3" for="${name}"><span>${escapeHtml(label)}${required ? " *" : ""}</span>${control}</label>`;
}

function bindCaseForm() {
  const form = document.querySelector("#caseForm");
  form?.addEventListener("input", () => {
    const values = new FormData(form);
    for (const key of Object.keys(DEFAULT_CASE)) if (values.has(key)) caseDraft[key] = String(values.get(key)).slice(0, 2400);
    caseDraft.updated_at = new Date().toISOString();
    saveCase();
  });
  form?.addEventListener("submit", (event) => {
    event.preventDefault();
    const packet = validateHandoff({ ...caseDraft, created_at: new Date().toISOString() });
    if (!packet) return showInlineError(form, "Objective and requested output are required.");
    caseDraft = { ...caseDraft, state: "review_required", updated_at: packet.created_at };
    saveCase();
    sessionStorage.setItem(STORAGE.handoff, JSON.stringify(packet));
    eventRecord("Case packet prepared", "A browser-local review packet is ready in the Communication Center.");
    navigate("communication");
  });
  document.querySelector("#resetCase")?.addEventListener("click", () => {
    caseDraft = { ...DEFAULT_CASE };
    saveCase();
    eventRecord("Case draft cleared", "Only the ArchFlow V3 browser-local case draft was reset.", "warn");
    renderOperations();
  });
  document.querySelector("#downloadCase")?.addEventListener("click", () => downloadJson("archflow-public-case.json", { ...caseDraft, boundary: publicBoundary() }));
}

function showInlineError(form, message) {
  form.querySelector(".form-error-v3")?.remove();
  const error = document.createElement("p");
  error.className = "form-error-v3";
  error.setAttribute("role", "alert");
  error.textContent = message;
  form.prepend(error);
}

function publicBoundary() {
  return { provider_calls: 0, external_writes: 0, repository_fetches: 0, authority: "browser-local proposal only" };
}

function renderCommunication() {
  const handoff = readHandoff();
  const events = loadEventList();
  view.innerHTML = `
    <section class="docs-hero compact"><div><span class="eyebrow">Jarvis → dashboard</span><h2>One communication surface, one visible state.</h2></div><p>Jarvis can prepare a public-safe packet and return it here. This browser session is not an account, a message bus, a database, or durable project memory.</p></section>
    <div class="proof-state-grid communication-summary-v3">${summaryCard("Incoming packet", handoff ? "Ready for review" : "None", handoff ? "Validated V3 handoff in this tab" : "Open Jarvis or prepare a project case", handoff ? "ok" : "warn")}${summaryCard("Administrator", authSession.authenticated ? "Verified" : "Public mode", authSession.authenticated ? "Server session; actions still separately gated" : "No browser-selectable role", authSession.authenticated ? "ok" : "neutral")}${summaryCard("Provider calls", "0", "Disabled in the public flow", "ok")}${summaryCard("External writes", "0", "Downloads and navigation only", "ok")}</div>
    <div class="docs-grid two communication-layout-v3">
      <section class="panel"><div class="section-header"><div><span class="eyebrow">Current handoff</span><h2 class="section-title">${handoff ? escapeHtml(handoff.objective) : "No packet waiting"}</h2></div>${handoff ? badge("review required", "warn") : badge("empty", "neutral")}</div>${handoff ? table(["Field", "Value"], [["Decision", escapeHtml(handoff.decision || "Not stated")], ["Public reference", escapeHtml(handoff.public_reference || "Safe label only")], ["Allowed evidence", escapeHtml(handoff.allowed_evidence)], ["Exclusions", escapeHtml(handoff.exclusions)], ["Requested output", escapeHtml(handoff.requested_output)], ["Reviewer", escapeHtml(handoff.reviewer)], ["Stop conditions", escapeHtml(handoff.constraints)]]) : `<div class="empty-state-v3"><p>Prepare a packet in Jarvis or in the Project dashboard. No content is transmitted automatically.</p><div class="row-actions"><a class="primary" href="${protocolAwareJarvisUrl()}">Open Jarvis</a><a class="button" href="#operations">Prepare a case</a></div></div>`}${handoff ? `<div class="row-actions"><button class="primary" id="acceptHandoff" type="button">Use in project case</button><button class="button" id="downloadHandoff" type="button">Download packet</button><button class="button" id="clearHandoff" type="button">Clear from this tab</button></div>` : ""}</section>
      <section class="panel"><span class="eyebrow">Notifications</span><h2 class="section-title">Local activity, stated honestly</h2><div class="event-list-v3">${events.length ? events.map((event) => `<article><span class="status-dot-v3 ${escapeHtml(event.tone)}"></span><div><strong>${escapeHtml(event.title)}</strong><p>${escapeHtml(event.detail)}</p><time>${escapeHtml(formatDate(event.at))}</time></div></article>`).join("") : `<p class="muted">No local V3 activity yet. Events describe browser actions only.</p>`}</div></section>
    </div>
    <section class="panel" style="margin-top:16px"><span class="eyebrow">Communication contract</span><h2 class="section-title">Every handoff answers the same seven questions.</h2>${table(["Question", "Required answer"], [["Why?", "Objective and decision supported"], ["From what?", "Allowed sources, exclusions, provenance, and gaps"], ["Owned by whom?", "One maker for each output and an independent reviewer"], ["What is produced?", "Named artifact with acceptance criteria"], ["What may change?", "Exact tool, target, side effect, approval, and rollback"], ["When must it stop?", "Evidence, authority, budget, safety, retry, and conflict boundaries"], ["What becomes memory?", "Only reviewed reusable meaning with lineage and freshness"]].map((row) => row.map(escapeHtml)))}</section>`;
  if (handoff) bindCommunication(handoff);
}

function bindCommunication(handoff) {
  document.querySelector("#acceptHandoff")?.addEventListener("click", () => {
    caseDraft = { ...caseDraft, ...handoff, kind: DEFAULT_CASE.kind, state: "review_required", updated_at: new Date().toISOString() };
    saveCase();
    eventRecord("Jarvis handoff accepted", "The validated packet now populates the browser-local project case.");
    navigate("operations");
  });
  document.querySelector("#downloadHandoff")?.addEventListener("click", () => downloadJson("archflow-jarvis-handoff.json", { ...handoff, boundary: publicBoundary() }));
  document.querySelector("#clearHandoff")?.addEventListener("click", () => {
    sessionStorage.removeItem(STORAGE.handoff);
    importedHandoff = null;
    eventRecord("Handoff cleared", "The Jarvis packet was removed from this tab only.", "warn");
    renderCommunication();
  });
}

function summaryCard(label, value, note, tone = "neutral") {
  return `<article class="card ${escapeHtml(tone)}"><span class="card-label">${escapeHtml(label)}</span><strong class="card-value">${escapeHtml(value)}</strong><p>${escapeHtml(note)}</p></article>`;
}

function renderAgents() {
  const roles = safeArray(data.role_catalog?.roles);
  const skills = safeArray(data.skill_catalog?.items);
  const fallbackRoles = [
    ["Lead integrator", "Owns scope, merge order, conflicts, final checks, and handoff", "Integrated candidate and next safe action"],
    ["Research operator", "Builds source-labeled evidence and records contradictions as gaps", "Evidence packet and source ledger"],
    ["Task planner", "Defines dependencies, one writer per target, checks, stop, and rollback", "Bounded task contract"],
    ["Implementation operator", "Changes only assigned files and runs focused checks", "Candidate artifact and maker evidence"],
    ["Independent reviewer", "Freezes the candidate and returns approve, revise, or block", "Verdict with exact findings"],
    ["Knowledge curator", "Deduplicates and promotes reusable meaning with lineage", "Maintained knowledge update"],
  ];
  const roleRows = roles.length ? roles.map((role) => [escapeHtml(role.title || role.id), escapeHtml(role.responsibility || role.objective || "Bounded task-contract responsibility"), escapeHtml(safeArray(role.outputs).join(", ") || role.outputArtifact || "Named artifact and handoff")]) : fallbackRoles.map((row) => row.map(escapeHtml));
  view.innerHTML = `
    <section class="docs-hero compact"><div><span class="eyebrow">Functional contracts</span><h2>A role exists to own an output, not to decorate an org chart.</h2></div><p>The public repository uses functional identifiers. Personal call names, private team context, and identity-bearing defaults are excluded.</p></section>
    <div class="proof-state-grid">${summaryCard("Role contracts", String(roles.length || fallbackRoles.length), "Activated only by a bounded task contract", "ok")}${summaryCard("Packaged skills", String(data.skill_catalog?.packaged_count ?? skills.length), "Portable public SKILL.md contracts", "ok")}${summaryCard("Self approval", "Forbidden", "Maker and independent reviewer stay separate", "ok")}${summaryCard("Always-running agents", "0", "The roster is configuration, not activity", "ok")}</div>
    <section class="panel" style="margin-top:16px"><div class="section-header"><div><span class="eyebrow">Actionable agent structure</span><h2 class="section-title">Responsibility → input → output → reviewer → stop</h2></div><a class="button" href="#configuration">Open configuration</a></div>${table(["Functional role", "Responsibility", "Expected output"], roleRows)}</section>
    <section class="panel" style="margin-top:16px"><div class="section-header"><div><span class="eyebrow">Portable skills</span><h2 class="section-title">Load the smallest relevant method set</h2></div>${badge(`${data.skill_catalog?.packaged_count ?? skills.length} packaged`, "ok")}</div><p>A skill is a reusable operating contract with trigger, inputs, procedure, outputs, permissions, forbidden actions, validation, and handoff. It does not grant a provider key, filesystem scope, or external authority.</p><div class="skill-grid-v3">${(skills.length ? skills : [{ name: "Knowledge service", description: "Frame a decision and source boundary." }, { name: "Task breakdown", description: "Create bounded work contracts and exclusive file ownership." }, { name: "Agent control", description: "Map roles, tools, sources, gates, and stop conditions." }, { name: "Runtime guard", description: "Hold provider and external actions until exact gates pass." }, { name: "Task handout", description: "Leave durable completion, checks, gaps, and next action." }]).map((skill) => `<article><span class="eyebrow">Skill contract</span><h3>${escapeHtml(skill.name || skill.id)}</h3><p>${escapeHtml(skill.description || "See the packaged SKILL.md contract.")}</p></article>`).join("")}</div></section>
    <section class="panel" style="margin-top:16px"><div class="section-header"><div><span class="eyebrow">Teamwork distribution</span><h2 class="section-title">Join only when you own an output, check, approval, or handoff.</h2></div></div>${diagramCard(DIAGRAMS[3])}</section>`;
}

function renderSetup() {
  view.innerHTML = `
    <section class="docs-hero compact"><div><span class="eyebrow">Three setup tiers</span><h2>The core works without an API key.</h2></div><p>Credentials never enter the repository, browser storage, dashboard data, screenshots, or logs. Platform integration is a server-side extension with its own proof and rollback.</p></section>
    <div class="setup-grid">
      <article class="setup-card"><div class="setup-card-head"><span>01</span><div><h3>Static public core</h3><small>Individual use · zero keys</small></div></div><p>Documentation, four schemas, case contracts, Communication Center, downloads, and public validation.</p><pre class="code-block">python3 -m http.server 8765\n# open /project/dashboard/</pre></article>
      <article class="setup-card"><div class="setup-card-head"><span>02</span><div><h3>Validated local runtime</h3><small>Individual or team development</small></div></div><p>Add isolated validation, bounded retrieval, state-machine fixtures, role contracts, and provider-disabled Jarvis API checks.</p><pre class="code-block">python3 -m venv .venv\n.venv/bin/pip install -r project/requirements-validation.lock.txt\n.venv/bin/python project/scripts/validate-workflows.py</pre></article>
      <article class="setup-card"><div class="setup-card-head"><span>03</span><div><h3>Gated integrations</h3><small>Server-side only</small></div></div><p>Add Google administrator auth, selected provider adapters, observability, or external writeback only after negative tests, budget rules, approval, and readback.</p><pre class="code-block">ARCHFLOW_AUTH_ENABLED\nGOOGLE_OAUTH_CLIENT_ID\nGOOGLE_OAUTH_CLIENT_SECRET\nARCHFLOW_ADMIN_GOOGLE_SUBJECTS\nARCHFLOW_AUTH_SECRET\nARCHFLOW_PROVIDER_MODE=none</pre></article>
    </div>
    <section class="panel setup-checklist-v3"><div class="section-header"><div><span class="eyebrow">First useful run</span><h2 class="section-title">Set up the system in this order</h2></div><a class="button" href="${REPOSITORY_URL}" target="_blank" rel="noreferrer">Open GitHub</a></div>${table(["Step", "Action", "Proof"], [["1", "Clone the public tool and inspect the security boundary.", "No personal data, secrets, or local paths in the tracked snapshot."], ["2", "Run static and workflow validators with providers disabled.", "Deterministic checks pass from a clean environment."], ["3", "Create one case with explicit allowed and excluded sources.", "Review packet names the decision, output, reviewer, and stop."], ["4", "Assign the smallest role and skill set.", "One owner per output; independent reviewer separate."], ["5", "Run the bounded route and collect maker evidence.", "State trace, checks, gaps, and proposed action are inspectable."], ["6", "Approve one external action only if required.", "Exact target, authority, rollback, and readback receipt."], ["7", "Promote only reusable meaning.", "Lineage, freshness, and supersession are recorded."]].map((row) => row.map(escapeHtml)))}</section>
    <section class="panel"><div class="section-header"><div><span class="eyebrow">Administrator boundary</span><h2 class="section-title">Sign-in is server-enforced and fail-closed</h2></div>${badge(authSession.authenticated ? "verified session" : "public mode", authSession.authenticated ? "ok" : "warn")}</div><p>The public UI has no Admin/Guest switch. Google authorization may establish one short-lived, server-signed administrator session. The allowlist and identity stay outside Git. Authentication still does not approve provider execution, spend, deployment, Git mutation, or writeback.</p><button class="button" id="setupAdminAccess" type="button">${authSession.authenticated ? "Sign out administrator session" : "Start administrator sign-in"}</button></section>`;
  document.querySelector("#setupAdminAccess")?.addEventListener("click", handleAdminAccess);
}

function renderRuns() {
  const evidence = data.performance_evidence || DEFAULT_DATA.performance_evidence;
  const metrics = safeArray(evidence.metrics).length ? evidence.metrics : DEFAULT_DATA.performance_evidence.metrics;
  view.innerHTML = `
    <section class="docs-hero compact"><div><span class="eyebrow">Measured ${escapeHtml(evidence.measured_at || "bounded fixtures")}</span><h2>Evidence is useful only when the denominator is visible.</h2></div><p>The public benchmark is provider-disabled and compares exact local fixtures. It does not establish billed-token savings, memory savings, production speed, ROI, or universal quality.</p></section>
    <div class="metric-grid-v3">${metrics.map((metric) => `<article><span>${escapeHtml(metric.label)}</span><strong>${escapeHtml(metric.value)}</strong><p><b>Comparator:</b> ${escapeHtml(metric.comparator || "See benchmark record")}</p><p><b>Limit:</b> ${escapeHtml(metric.limitation || "Bounded fixture only")}</p></article>`).join("")}</div>
    <section class="panel" style="margin-top:16px"><div class="section-header"><div><span class="eyebrow">Proof ladder</span><h2 class="section-title">Configured is not executed; executed is not externally applied.</h2></div></div>${table(["State", "Required evidence", "What it does not prove"], [["Documented", "Maintained explanation and source link", "Runtime availability"], ["Configured", "Parseable contract and explicit defaults", "That a service ran"], ["Locally tested", "Deterministic fixture and result", "Representative production quality"], ["Independently reviewed", "Frozen hash and separate verdict", "Authority to release"], ["Approved action", "Exact target, actor, operation, data class, rollback", "Observed outcome"], ["Read back", "Target state after the action", "Long-term reliability"], ["Promoted knowledge", "Reviewed meaning, lineage, owner, freshness", "That raw history should be retained"]].map((row) => row.map(escapeHtml)))}</section>
    <section class="panel" style="margin-top:16px"><div class="section-header"><div><span class="eyebrow">Output and receipt schema</span><h2 class="section-title">A successful command is not a result receipt.</h2></div></div>${diagramCard(DIAGRAMS[2])}</section>`;
}

function renderArchitecture() {
  view.innerHTML = `<section class="docs-hero compact"><div><span class="eyebrow">Complete visual system</span><h2>Four views, one operating model.</h2></div><p>Each SVG is editable and public-safe. Numeric labels inside a schema describe current configuration defaults or bounded examples; they are not universal performance claims.</p></section><div class="diagram-grid-v3 full">${DIAGRAMS.map((diagram) => diagramCard(diagram)).join("")}</div><section class="panel architecture-distribution-v3"><span class="eyebrow">Dashboard distribution</span><h2 class="section-title">Place the diagram next to the decision it explains.</h2>${table(["Dashboard area", "Schema", "Question answered"], [["System map", "Seven-layer knowledge crew", "Which layer owns this transition and output?"], ["Knowledge & Memory", "Input and perception", "Which sources may enter the context capsule?"], ["Evidence", "Output, validation, and receipts", "What proof is required before action and promotion?"], ["Roles & Communication", "Onboarding and teamwork", "Who joins, what do they own, and when must they escalate?"]].map((row) => row.map(escapeHtml)))}</section>`;
}

function renderKnowledge() {
  view.innerHTML = `<section class="docs-hero compact"><div><span class="eyebrow">Source-visible context</span><h2>Retrieval finds evidence; review decides what becomes knowledge.</h2></div><p>The public tool uses a retrieval cascade rather than treating one vector database as memory. Every layer has a source, responsibility, exclusion, and fallback.</p></section><section class="panel">${diagramCard(DIAGRAMS[1])}</section><div class="docs-grid two" style="margin-top:16px"><section class="panel"><span class="eyebrow">Read path</span><h2 class="section-title">Smallest useful context first</h2><ol class="state-list-v3"><li><strong>Routing</strong><span>Identify project, authority, and safety boundary.</span></li><li><strong>Stable context</strong><span>Load compact rules and current decisions.</span></li><li><strong>Graph reference</strong><span>Inspect structure before broad file reads.</span></li><li><strong>Task retrieval</strong><span>Search an explicit source allowlist with provenance.</span></li><li><strong>Exact read</strong><span>Verify the source passage before relying on it.</span></li><li><strong>Context capsule</strong><span>Carry facts, interpretations, hypotheses, gaps, and source refs.</span></li></ol></section><section class="panel"><span class="eyebrow">Memory policy</span><h2 class="section-title">Keep meaning, not exhaust</h2>${table(["Keep", "Exclude", "Promotion rule"], [["Reviewed decisions, stable constraints, reusable methods, current source routes", "Secrets, identities, raw transcripts, transient preferences, local paths, duplicate run noise", "Search duplicates; preserve provenance; record owner and freshness; supersede instead of silently overwriting"]].map((row) => row.map(escapeHtml)))}</section></div>`;
}

function renderWorkflow() {
  const stages = [
    ["01", "Research", "Admit sources, retrieve evidence, verify exact passages, label gaps.", "Evidence packet"],
    ["02", "Define", "Bind objective, decision, acceptance, roles, skills, tools, reviewer, and stop.", "Task and run envelope"],
    ["03", "Act", "Execute the smallest bounded route; interrupt before any unauthorized side effect.", "Candidate artifact"],
    ["04", "Review", "Freeze, check requirements and safety, then approve, revise, or block.", "Independent verdict"],
    ["05", "Read back", "Observe the exact target after an approved action; do not infer success.", "Result receipt"],
    ["06", "Remember", "Promote reusable conclusions with lineage, owner, date, and supersession.", "Maintained knowledge"],
  ];
  view.innerHTML = `<section class="docs-hero compact"><div><span class="eyebrow">Typed run envelope</span><h2>State tracing connects every loop.</h2></div><p>LangGraph is the state owner; roles are bounded workers; retrieval supplies evidence; review controls advancement; external action remains a distinct gate.</p></section><div class="workflow-grid-v3">${stages.map((stage) => `<article><span>${stage[0]}</span><h3>${stage[1]}</h3><p>${stage[2]}</p><strong>${stage[3]}</strong></article>`).join("")}</div><section class="panel" style="margin-top:16px"><h2 class="section-title">One run envelope</h2><pre class="code-block">run_id · objective · decision · source_boundary · context_capsule\nstate · node · attempt · role_contracts · tool_allowlist\nexpected_outputs · acceptance_criteria · reviewer · stop_conditions\nauthority · provider_state · spend_cap · writeback_state\nevidence_refs · maker_checks · reviewer_verdict · action_receipt\nknowledge_candidates · gaps · next_safe_action</pre></section><section class="panel" style="margin-top:16px"><span class="eyebrow">Loop rules</span>${table(["Loop", "May continue when", "Must stop when"], [["Research", "New evidence changes the decision or closes a named gap", "Source boundary is exhausted or evidence quality cannot improve"], ["Define", "A requirement or ownership conflict remains resolvable", "Authority, acceptance criteria, or reviewer is missing"], ["Maker repair", "Reviewer supplied an exact finding and repair scope", "Retry cap is reached or the same blocker repeats without new evidence"], ["External action", "Exact approval, target, rollback, and replay protection pass", "Any field is ambiguous, credential state is unproved, or readback cannot be performed"]].map((row) => row.map(escapeHtml)))}</section>`;
}

function renderConfiguration() {
  view.innerHTML = `<section class="docs-hero compact"><div><span class="eyebrow">Configuration layers</span><h2>Portable defaults, private values, explicit activation.</h2></div><p>Git stores names and contracts. Secret values and administrator identities remain in the deployment platform or approved secret manager.</p></section>${table(["Layer", "Public repository", "Private runtime", "Activation proof"], [["Dashboard", "Routes, public data schema, four SVGs, browser packet schema", "None required for static use", "Five-width browser checks"], ["Authentication", "OIDC routes, cookie/CSRF contract, environment names", "Google client, admin subject allowlist, session secret", "Negative tests plus live callback/readback"], ["Retrieval", "Corpus manifest, chunk/top-k defaults, provenance schema", "Optional embeddings or vector adapter", "Fixed-query benchmark and source recall"], ["State controller", "Run envelope, nodes, routes, gates, retry and stop rules", "Optional checkpoint store", "Deterministic route and recovery fixtures"], ["Roles and skills", "Functional roster, packaged skill contracts, reviewer separation", "Optional provider adapters", "Role/task mapping validator"], ["Providers", "Registry states and budget-gate schema", "Provider key and exact allowlist", "Single-call test, spend ledger, replay guard"], ["External actions", "Approval and receipt schema", "Target-specific credentials", "Exact action plus target readback"]].map((row) => row.map(escapeHtml)))}<section class="panel" style="margin-top:16px"><span class="eyebrow">Environment names only</span><h2 class="section-title">Administrator setup</h2><pre class="code-block">ARCHFLOW_AUTH_ENABLED\nGOOGLE_OAUTH_CLIENT_ID\nGOOGLE_OAUTH_CLIENT_SECRET\nARCHFLOW_AUTH_ORIGIN\nARCHFLOW_AUTH_SECRET\nARCHFLOW_AUTH_SESSION_EPOCH\nARCHFLOW_ADMIN_GOOGLE_SUBJECTS\nARCHFLOW_ADMIN_EMAILS\nARCHFLOW_AUTH_SESSION_TTL_SECONDS</pre><p>No endpoint reports whether these values exist. Missing configuration fails closed.</p></section>`;
}

function render() {
  if (!data) return;
  renderNav();
  renderHeader();
  if (activeRoute === "manual") renderManual();
  if (activeRoute === "operations") renderOperations();
  if (activeRoute === "communication") renderCommunication();
  if (activeRoute === "agents") renderAgents();
  if (activeRoute === "setup") renderSetup();
  if (activeRoute === "runs") renderRuns();
  if (activeRoute === "architecture") renderArchitecture();
  if (activeRoute === "knowledge") renderKnowledge();
  if (activeRoute === "workflow") renderWorkflow();
  if (activeRoute === "configuration") renderConfiguration();
}

async function loadData(force = false) {
  if (!force && window.ARCHFLOW_PUBLIC_DATA) return structuredClone(window.ARCHFLOW_PUBLIC_DATA);
  if (window.location.protocol !== "file:") {
    const response = await fetch(`./data.json${force ? `?t=${Date.now()}` : ""}`, { cache: "no-store", credentials: "same-origin" });
    if (!response.ok) throw new Error(`Dashboard data returned ${response.status}.`);
    return response.json();
  }
  if (window.ARCHFLOW_PUBLIC_DATA) return structuredClone(window.ARCHFLOW_PUBLIC_DATA);
  return structuredClone(DEFAULT_DATA);
}

async function refreshData(force = false) {
  try {
    data = { ...structuredClone(DEFAULT_DATA), ...(await loadData(force)) };
    render();
  } catch (error) {
    data = structuredClone(DEFAULT_DATA);
    render();
    liveStatus.textContent = "Fallback public data";
    view.insertAdjacentHTML("afterbegin", `<div class="docs-callout warning" role="status"><strong>Data fallback</strong><p>${escapeHtml(error.message)} The generic built-in documentation remains available.</p></div>`);
  }
}

async function refreshAuth() {
  if (window.location.protocol === "file:") {
    authSession = { authenticated: false, role: "public", csrf: "" };
    renderHeader();
    return;
  }
  try {
    const response = await fetch("/api/auth/session", { cache: "no-store", credentials: "same-origin" });
    const payload = response.ok ? await response.json() : {};
    authSession = {
      authenticated: payload.authenticated === true && payload.role === "administrator",
      role: payload.authenticated === true ? "administrator" : "public",
      csrf: typeof payload.csrf === "string" ? payload.csrf : "",
    };
  } catch (_error) {
    authSession = { authenticated: false, role: "public", csrf: "" };
  }
  renderHeader();
}

async function handleAdminAccess() {
  if (!authSession.authenticated) {
    window.location.assign(authStartUrl());
    return;
  }
  try {
    const response = await fetch("/api/auth/logout", { method: "POST", credentials: "same-origin", headers: { "X-ArchFlow-CSRF": authSession.csrf } });
    if (!response.ok) throw new Error("Sign-out was rejected.");
    authSession = { authenticated: false, role: "public", csrf: "" };
    eventRecord("Administrator signed out", "The server session ended; the dashboard returned to public mode.");
    render();
  } catch (error) {
    liveStatus.textContent = error.message;
    liveStatus.className = "pill live-pill warn";
  }
}

clearLegacyBrowserMemory();
jarvisLink.href = protocolAwareJarvisUrl();
document.querySelector("#githubLink").href = REPOSITORY_URL;
refreshButton.addEventListener("click", () => refreshData(true));
adminButton.addEventListener("click", handleAdminAccess);
window.addEventListener("hashchange", () => {
  activeRoute = normalizeRoute(window.location.hash.replace(/^#/, "") || "manual");
  render();
  view.focus({ preventScroll: true });
});
window.addEventListener("pageshow", () => {
  if (activeRoute === "communication") renderCommunication();
});

Promise.all([refreshData(false), refreshAuth()]).catch(() => refreshData(false));
