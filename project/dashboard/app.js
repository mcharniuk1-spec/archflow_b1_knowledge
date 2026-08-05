/* ArchFlow Crew Desk
 *
 * A provider-disabled, browser-local projection of the public knowledge-crew
 * contracts. It prepares review packets; it does not run agents, contact a
 * model, mutate repository files, or perform an external action.
 */

const ROUTES = [
  { id: "today", label: "Today", icon: "01", eyebrow: "Employee knowledge crew", title: "Today", summary: "Your next safe action, its evidence, and its reviewer." },
  { id: "work", label: "Work", icon: "02", eyebrow: "One case spine", title: "Start and drive work", summary: "Turn a goal into a bounded mission, review route, and readback." },
  { id: "knowledge", label: "Knowledge", icon: "03", eyebrow: "Source-visible perception", title: "Knowledge ecosystem", summary: "See what each layer contributes, what it cannot decide, and how context stays current." },
  { id: "team", label: "Team", icon: "04", eyebrow: "Adaptive responsibilities", title: "Roles and workflow packs", summary: "Select the smallest responsible crew and inspect every ownership boundary." },
  { id: "review", label: "Review", icon: "05", eyebrow: "Requirements before action", title: "Trace, validate, and read back", summary: "Follow evidence through requirements, maker work, independent review, and receipts." },
  { id: "setup", label: "Set up", icon: "06", eyebrow: "Portable local configuration", title: "Connect your own system", summary: "Configure bounded retrieval and a safe local bridge without exposing private data." },
];

const LEGACY_ROUTES = {
  manual: "today",
  overview: "today",
  architecture: "knowledge",
  agents: "team",
  operations: "work",
  data: "knowledge",
  runs: "review",
  reference: "knowledge",
  service: "work",
  schema: "work",
  config: "setup",
  wikillm: "knowledge",
  graphify: "knowledge",
  langgraph: "review",
  llamaindex: "knowledge",
  crewai: "team",
  langsmith: "review",
  env: "setup",
  gates: "review",
  history: "review",
  jarvis: "today",
};

const STORE = {
  caseDraft: "archflow.crewDesk.caseDraft.v2",
  settings: "archflow.crewDesk.settings.v2",
  receipts: "archflow.crewDesk.receipts.v2",
  guide: "archflow.crewDesk.guideDraft.v2",
};

const DEFAULT_CASE = {
  case_id: "case-local-draft",
  goal: "",
  employee_role: "New employee or operator",
  output: "",
  evidence_boundary: "Public project contracts and reviewed project knowledge only",
  reviewer: "Halyna — Independent Reviewer",
  stop_condition: "Stop when authority, current requirements, or source evidence is missing.",
  known_gaps: [],
  risk: "medium",
  workflow_pack: "employee_onboarding",
  state: "request_received",
  updated_at: null,
};

const DEFAULT_SETTINGS = {
  bridge_base: "http://127.0.0.1:8787",
  chunk_size: 800,
  chunk_overlap: 120,
  lexical_top_k: 5,
  vector_top_k: 5,
  rerank_top_k: 5,
  final_source_limit: 8,
  turbovec_candidate: false,
  checkpointer: "none",
  allowed_corpus: "project/, skills/, wiki/, sanitized examples/",
  excluded_corpus: "private/, secrets/, raw/, local runtime, credentials",
};

const DIAGRAMS = [
  {
    file: "knowledge-crew-tower.png",
    source: "knowledge-crew-tower.svg",
    title: "Seven-layer knowledge crew",
    description: "The knowledge and database spine on the left, role-controlled work in the centre, and accountable outputs on the right.",
  },
  {
    file: "context-input-flow.png",
    source: "context-input-flow.svg",
    title: "Input and perception flow",
    description: "How rules, role responsibility, requirements, retrieved evidence, exact reads, and gaps become one source-visible context capsule.",
  },
  {
    file: "output-receipt-flow.png",
    source: "output-receipt-flow.svg",
    title: "Output, validation, and receipts",
    description: "How candidate work is checked against requirements and authority before one approved action and an exact readback.",
  },
  {
    file: "onboarding-teamwork-flow.png",
    source: "onboarding-teamwork-flow.svg",
    title: "Employee onboarding and teamwork",
    description: "The first mission, contextual support, role handoffs, manager interrupts, review, learning, and maintained knowledge loop.",
  },
];

const PHASES = [
  ["01", "Orient", "Goal, role, authority"],
  ["02", "Perceive", "Sources and context"],
  ["03", "Commit", "Requirements and done"],
  ["04", "Work", "Smallest responsible crew"],
  ["05", "Gate", "Validate, review, approve"],
  ["06", "Learn", "Readback and promotion"],
];

const view = document.querySelector("#view");
const nav = document.querySelector("#nav");
const notice = document.querySelector("#notice");
const pageEyebrow = document.querySelector("#pageEyebrow");
const pageTitle = document.querySelector("#pageTitle");
const pageSummary = document.querySelector("#pageSummary");
const exportHeader = document.querySelector("#exportHeader");

let contracts = null;
let caseDraft = readStored(STORE.caseDraft, DEFAULT_CASE);
let settings;
try {
  settings = normalizeImportedSettings(readStored(STORE.settings, DEFAULT_SETTINGS));
} catch (_error) {
  settings = Object.assign({}, DEFAULT_SETTINGS);
  localStorage.removeItem(STORE.settings);
}
let receipts = readStored(STORE.receipts, []);
let roleFilter = "";
let packFilter = "all";
let activeRoute = normalizeRoute(window.location.hash.replace(/^#/, "") || "today");

function normalizeRoute(raw) {
  const candidate = LEGACY_ROUTES[raw] || raw;
  return ROUTES.some(function (route) { return route.id === candidate; }) ? candidate : "today";
}

function readStored(key, fallback) {
  try {
    const raw = localStorage.getItem(key);
    return raw ? Object.assign({}, fallback, JSON.parse(raw)) : Object.assign({}, fallback);
  } catch (_error) {
    return Object.assign({}, fallback);
  }
}

function saveStored(key, value) {
  localStorage.setItem(key, JSON.stringify(value));
}

function escapeHtml(value) {
  return String(value == null ? "" : value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function sentence(value) {
  return String(value || "").replace(/_/g, " ");
}

function titleCase(value) {
  return sentence(value).replace(/\b\w/g, function (character) { return character.toUpperCase(); });
}

function list(items, className) {
  const values = Array.isArray(items) ? items : [];
  return '<div class="' + (className || "token-list") + '">' + values.map(function (item) {
    return '<span class="token">' + escapeHtml(sentence(item)) + "</span>";
  }).join("") + "</div>";
}

function badge(text, tone) {
  return '<span class="badge ' + escapeHtml(tone || "neutral") + '">' + escapeHtml(text) + "</span>";
}

function sectionHeading(title, copy, actions) {
  return '<header class="section-heading"><div><h2>' + escapeHtml(title) + "</h2><p>" + escapeHtml(copy) + '</p></div><div class="section-actions">' + (actions || "") + "</div></header>";
}

function downloadJson(filename, value) {
  const payload = JSON.stringify(value, null, 2);
  const blob = new Blob([payload], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = filename;
  document.body.appendChild(anchor);
  anchor.click();
  anchor.remove();
  URL.revokeObjectURL(url);
}

function showNotice(message, tone) {
  notice.hidden = false;
  notice.textContent = message;
  notice.classList.toggle("warning", tone === "warning");
  window.setTimeout(function () { notice.hidden = true; }, 5000);
}

function currentPacket() {
  const pack = workflowById(caseDraft.workflow_pack);
  return {
    schema_version: "2.0.0",
    kind: "archflow_local_review_packet",
    generated_at: new Date().toISOString(),
    boundary: {
      provider_called: false,
      writeback_performed: false,
      external_action_performed: false,
      authority: "browser-local proposal only",
    },
    case: caseDraft,
    selected_workflow: pack,
    role_task_bindings: materializeRoleTaskBindings(pack),
    settings: settings,
    receipt_count: receipts.length,
    configuration_refs: {
      crew: "project/system/contracts/knowledge-crew-config.json",
      roles: "project/system/contracts/role-catalog.json",
      workflows: "project/system/contracts/role-workflows.json",
      controller: "project/system/contracts/operating-model.json",
      role_task_binding_schema: "project/system/schemas/role-task-binding.schema.json",
      knowledge_case_schema: "project/system/schemas/knowledge-case.schema.json",
    },
  };
}

function workflowById(id) {
  if (!contracts) return null;
  return contracts.workflows.packs.find(function (pack) { return pack.id === id; }) || contracts.workflows.packs[0];
}

function roleByName(name) {
  if (!contracts) return null;
  return contracts.roles.roles.find(function (role) { return role.call_name === name; }) || null;
}

function roleForMachineId(id) {
  if (!contracts) return null;
  return contracts.roles.roles.find(function (role) { return role.id === id; }) || null;
}

function roleLabel(id) {
  const role = roleForMachineId(id);
  return role ? role.call_name + " — " + role.title : id === "@case_owner" ? "Case owner" : id;
}

function selectedRoleEntries(pack) {
  if (!pack) return [];
  const base = new Set(pack.roles);
  const selected = new Set(pack.roles);
  const queue = pack.roles.slice();
  while (queue.length) {
    const role = roleForMachineId(queue.shift());
    if (!role || !role.task_defaults) continue;
    role.task_defaults.reviewer_route.forEach(function (next) {
      if (next === "@case_owner" || selected.has(next)) return;
      selected.add(next);
      queue.push(next);
    });
  }
  return Array.from(selected).map(function (id) {
    return { role: roleForMachineId(id), base_or_closure: base.has(id) ? "base" : "review_closure" };
  }).filter(function (entry) { return Boolean(entry.role); });
}

function materializeRoleTaskBindings(pack) {
  if (!pack) return [];
  const sourceRefs = [];
  const requirementRefs = [];
  const exactTargets = [];
  return selectedRoleEntries(pack).map(function (entry) {
    const role = entry.role;
    const defaults = role.task_defaults;
    return {
      binding_id: "binding-" + caseDraft.case_id.replace(/^case-/, "") + "-" + role.id.replace(/_/g, "-"),
      case_id: caseDraft.case_id,
      workflow_pack_id: pack.id,
      base_or_closure: entry.base_or_closure,
      role_id: role.id,
      call_name: role.call_name,
      role_goal: role.goal,
      inputs: defaults.inputs.slice(),
      source_refs: sourceRefs.slice(),
      requirement_refs: requirementRefs.slice(),
      owned_output: defaults.owned_output,
      expected_output: caseDraft.output ? caseDraft.output + " — " + sentence(defaults.owned_output) : sentence(defaults.owned_output),
      allowed_skills: defaults.allowed_skills.slice(),
      allowed_tools: defaults.allowed_tools.slice(),
      permission_boundary: {
        authority_ref: "case.authority",
        mode: defaults.permission_mode,
        exact_targets_ref: "binding.exact_targets",
        forbidden_actions_ref: "role_catalog.roles." + role.id + ".forbidden",
        rule: "intersection_only_no_authority_expansion",
      },
      forbidden_actions: role.forbidden.slice(),
      exact_targets: exactTargets.slice(),
      deterministic_checks: pack.done.slice(),
      known_gaps: Array.isArray(caseDraft.known_gaps) ? caseDraft.known_gaps.slice() : [],
      reviewer_route: defaults.reviewer_route.slice(),
      handoff: {
        to: defaults.handoff_to,
        payload: ["case_id", "binding_id", "role_id", "owned_output", "source_refs", "requirement_refs", "exact_targets", "deterministic_checks", "known_gaps", "stop_conditions"],
      },
      stop_conditions: [caseDraft.stop_condition],
    };
  });
}

function bindingReadiness(binding) {
  const missing = [];
  if (!binding.source_refs.length) missing.push("exact source refs");
  if (!binding.requirement_refs.length) missing.push("approved requirement refs");
  if (["local_mutation_exact_targets", "external_action_exact_approval", "git_action_exact_approval"].includes(binding.permission_boundary.mode) && !binding.exact_targets.length) missing.push("exact targets");
  return missing;
}

function renderNav() {
  nav.innerHTML = ROUTES.map(function (route) {
    const active = route.id === activeRoute;
    return '<a href="#' + route.id + '" class="' + (active ? "active" : "") + '"' + (active ? ' aria-current="page"' : "") + '><span class="nav-icon" aria-hidden="true">' + route.icon + "</span><span>" + route.label + "</span></a>";
  }).join("");
}

function renderHeader() {
  const route = ROUTES.find(function (item) { return item.id === activeRoute; }) || ROUTES[0];
  pageEyebrow.textContent = route.eyebrow;
  pageTitle.textContent = route.title;
  pageSummary.textContent = route.summary;
}

function phaseRail(activeIndex) {
  return '<div class="progress-rail" aria-label="Case progress">' + PHASES.map(function (phase, index) {
    const className = index < activeIndex ? "done" : index === activeIndex ? "active" : "";
    return '<div class="progress-step ' + className + '"><span>' + phase[0] + "</span><strong>" + phase[1] + "</strong><small>" + phase[2] + "</small></div>";
  }).join("") + "</div>";
}

function renderToday() {
  const pack = workflowById(caseDraft.workflow_pack);
  const missionTitle = caseDraft.goal || "Turn one reviewed requirement into one safe, reviewable action.";
  const nextAction = caseDraft.goal
    ? "Confirm the evidence boundary and requirement owner, then prepare the role-safe packet."
    : "Start a case with the goal, role, evidence boundary, reviewer, and stop condition.";
  return [
    '<section class="hero-grid">',
      '<article class="panel mission-card">',
        '<div class="mission-meta">',
          badge("Browser-local draft", "green"),
          badge(pack ? pack.label : "Employee onboarding", ""),
          badge("Provider disabled", "coral"),
        "</div>",
        '<h2>' + escapeHtml(missionTitle) + "</h2>",
        '<p class="mission-lead">ArchFlow keeps the employee, evidence, responsibility, requirements, review, and outcome on one case spine. It prepares the next safe action; it does not silently execute it.</p>',
        '<div class="mission-actions"><a class="primary-button" href="#work">Start or update this work</a><a class="secondary-button" href="#knowledge">See the evidence route</a></div>',
        '<div class="mission-facts">',
          '<div class="mission-fact"><span>Role</span><strong>' + escapeHtml(caseDraft.employee_role) + "</strong></div>",
          '<div class="mission-fact"><span>Evidence</span><strong>' + escapeHtml(caseDraft.evidence_boundary) + "</strong></div>",
          '<div class="mission-fact"><span>Reviewer</span><strong>' + escapeHtml(caseDraft.reviewer) + "</strong></div>",
          '<div class="mission-fact"><span>Next safe action</span><strong>' + escapeHtml(nextAction) + "</strong></div>",
        "</div>",
      "</article>",
      '<aside class="card guide-card" aria-labelledby="taras-title">',
        '<div class="guide-person"><span class="avatar" aria-hidden="true">TA</span><div><h2 id="taras-title">Ask Taras</h2><div class="role-id">Contextual onboarding guide · deterministic local guidance</div></div></div>',
        '<p>Describe what you need to do or what is unclear. Taras will point to a workflow and the questions that must be answered before work—not generate company truth or call a model.</p>',
        '<form class="guide-question" id="guideForm"><label class="field"><span>Your question</span><textarea id="guideInput" maxlength="1600" placeholder="Example: I need to research a new customer problem and turn it into requirements.">' + escapeHtml(localStorage.getItem(STORE.guide) || "") + '</textarea></label><button class="primary-button" type="submit">Prepare guidance</button></form>',
        '<div class="guide-result" id="guideResult">Start with the role, decision, approved sources, expected output, reviewer, and the condition that should stop the work.</div>',
      "</aside>",
    "</section>",
    '<section class="panel section">',
      sectionHeading("One responsive operating flow", "Every role sees the same case at the right resolution. LangGraph controls state; responsibilities and evidence control the content."),
      phaseRail(caseDraft.goal ? 1 : 0),
    "</section>",
    '<section class="panel section">',
      sectionHeading("System at a glance", "Counts come from the public contracts, not a live runtime claim."),
      '<div class="metric-grid">',
        '<div class="metric"><span>Layer contracts</span><strong>' + contracts.crew.layers.length + '</strong><small>Authority through maintained knowledge</small></div>',
        '<div class="metric"><span>Named roles</span><strong>' + contracts.roles.roles.length + '</strong><small>Ukrainian call names in English letters</small></div>',
        '<div class="metric"><span>Workflow packs</span><strong>' + contracts.workflows.packs.length + '</strong><small>Onboarding, research, outreach, design, delivery, and more</small></div>',
        '<div class="metric"><span>External actions</span><strong>0</strong><small>This public dashboard prepares packets only</small></div>',
      "</div>",
    "</section>",
    '<section class="panel section">',
      sectionHeading("First 30 minutes", "A new employee learns the source, responsibility, smallest safe task, and review route before being asked to deliver."),
      '<div class="three-col">',
        '<article class="card"><span class="eyebrow">0–10 minutes</span><h3>Orient to the role</h3><p>Read the role purpose, owned outputs, forbidden actions, evidence boundary, and manager/reviewer route.</p></article>',
        '<article class="card"><span class="eyebrow">10–20 minutes</span><h3>Trace one real requirement</h3><p>Open the current source, identify its owner and freshness, and distinguish a fact from an interpretation or gap.</p></article>',
        '<article class="card"><span class="eyebrow">20–30 minutes</span><h3>Complete one safe mission</h3><p>Prepare a reviewable artifact, run the defined check, send it to a different reviewer, and record the readback.</p></article>',
      "</div>",
    "</section>",
  ].join("");
}

function renderWork() {
  const pack = workflowById(caseDraft.workflow_pack);
  const bindings = materializeRoleTaskBindings(pack);
  const packOptions = contracts.workflows.packs.map(function (item) {
    return '<option value="' + escapeHtml(item.id) + '"' + (item.id === caseDraft.workflow_pack ? " selected" : "") + ">" + escapeHtml(item.label) + "</option>";
  }).join("");
  const roleCards = bindings.map(function (binding, index) {
    const missing = bindingReadiness(binding);
    const route = binding.reviewer_route.map(roleLabel).join(" → ");
    return '<article class="trace-item role-binding" data-step="' + String(index + 1).padStart(2, "0") + '"><div class="binding-title"><div><h3>' + escapeHtml(binding.call_name + " — " + roleForMachineId(binding.role_id).title) + '</h3><span class="machine-id">' + escapeHtml(binding.role_id) + '</span></div>' + badge(binding.base_or_closure === "base" ? "Selected pack" : "Review closure", binding.base_or_closure === "base" ? "green" : "") + '</div><p>' + escapeHtml(binding.role_goal) + '</p><dl class="binding-grid"><div><dt>Owned output</dt><dd>' + escapeHtml(sentence(binding.owned_output)) + '</dd></div><div><dt>Permission</dt><dd>' + escapeHtml(sentence(binding.permission_boundary.mode)) + '</dd></div><div><dt>Inputs</dt><dd>' + escapeHtml(binding.inputs.map(sentence).join(" · ")) + '</dd></div><div><dt>Skills</dt><dd>' + escapeHtml(binding.allowed_skills.length ? binding.allowed_skills.join(" · ") : "No reviewed public skill assigned") + '</dd></div><div><dt>Tool ceiling</dt><dd>' + escapeHtml(binding.allowed_tools.map(sentence).join(" · ")) + '</dd></div><div><dt>Reviewer route</dt><dd>' + escapeHtml(route) + '</dd></div><div><dt>Handoff</dt><dd>' + escapeHtml(roleLabel(binding.handoff.to)) + ' · fixed evidence payload</dd></div><div><dt>Readiness gaps</dt><dd>' + escapeHtml(missing.length ? missing.join(" · ") : "No contract gaps") + '</dd></div></dl><p class="contract-rule">Authority = case authority ∩ role ceiling ∩ available capabilities ∩ exact targets − denials.</p></article>';
  }).join("");
  return [
    '<section class="panel">',
      sectionHeading("Create one mission card", "Required fields make the work reviewable. Drafts stay in this browser until exported.", '<button class="secondary-button" id="resetCase" type="button">Reset local draft</button>'),
      '<div id="caseErrors" class="error-summary" hidden></div>',
      '<form id="caseForm">',
        '<div class="field-grid">',
          '<label class="field full"><span>Goal and decision</span><textarea name="goal" maxlength="1600" required placeholder="What must change, for whom, and what decision will this support?">' + escapeHtml(caseDraft.goal) + '<\/textarea><small>Use one observable outcome. Do not include credentials or raw private material.</small></label>',
          '<label class="field"><span>Employee or actor role</span><input name="employee_role" maxlength="180" required value="' + escapeHtml(caseDraft.employee_role) + '"><small>The responsibility being supported—not an identity or permission grant.</small></label>',
          '<label class="field"><span>Expected output</span><input name="output" maxlength="240" required value="' + escapeHtml(caseDraft.output) + '" placeholder="Example: evidence-backed requirement brief"><small>Name the reviewable artifact.</small></label>',
          '<label class="field full"><span>Allowed evidence boundary</span><textarea name="evidence_boundary" maxlength="1000" required>' + escapeHtml(caseDraft.evidence_boundary) + '<\/textarea><small>Exact source classes and exclusions; retrieval does not expand this boundary.</small></label>',
          '<label class="field"><span>Workflow pack</span><select name="workflow_pack">' + packOptions + '</select><small>The smallest pack can be changed after review.</small></label>',
          '<label class="field"><span>Risk</span><select name="risk"><option value="low"' + (caseDraft.risk === "low" ? " selected" : "") + '>Low — local reversible draft</option><option value="medium"' + (caseDraft.risk === "medium" ? " selected" : "") + '>Medium — shared or consequential</option><option value="high"' + (caseDraft.risk === "high" ? " selected" : "") + '>High — external, private, or irreversible</option></select></label>',
          '<label class="field"><span>Independent reviewer</span><input name="reviewer" maxlength="180" required value="' + escapeHtml(caseDraft.reviewer) + '"><small>The maker must not be the final reviewer.</small></label>',
          '<label class="field"><span>Stop condition</span><textarea name="stop_condition" maxlength="300" required>' + escapeHtml(caseDraft.stop_condition) + '<\/textarea><small>Name the missing authority, evidence, or risk that stops work.</small></label>',
        "</div>",
        '<div class="form-actions"><button class="primary-button" type="submit">Save browser-local mission</button><button class="secondary-button" type="button" id="preparePacket">Export review packet</button></div>',
      "</form>",
    "</section>",
    '<section class="panel section">',
      sectionHeading("Selected crew and handoff order", pack ? pack.trigger : "Choose a workflow pack."),
      '<div class="trace-layout"><div class="trace-chain">' + roleCards + '</div><aside class="card trace-aside"><h3>' + escapeHtml(pack ? pack.label : "No pack") + '</h3><dl><div><dt>Methods</dt><dd>' + escapeHtml(pack ? pack.methods.map(sentence).join(" · ") : "") + '</dd></div><div><dt>Outputs</dt><dd>' + escapeHtml(pack ? pack.outputs.map(sentence).join(" · ") : "") + '</dd></div><div><dt>Done when</dt><dd>' + escapeHtml(pack ? pack.done.join(" · ") : "") + '</dd></div></dl></aside></div>',
    "</section>",
    '<section class="panel section">',
      sectionHeading("Case state", "The display is a projection of typed LangGraph states. Saving a browser draft does not advance a live graph."),
      phaseRail(caseDraft.goal ? 1 : 0),
      '<div class="callout warning" style="margin-top:16px"><strong>Execution boundary:</strong> this screen can structure and export a mission. A real worker/controller must re-admit the packet, retrieve exact sources, validate authority, checkpoint the case, and create an execution receipt.</div>',
    "</section>",
  ].join("");
}

function frameworkRows() {
  const order = ["wikillm", "obsidian", "llamaindex", "turbovec", "orbit_and_graphify", "crewai", "langgraph", "dashboard"];
  return order.map(function (id) {
    const tool = contracts.crew.frameworks[id];
    let parameters = "";
    if (id === "llamaindex") {
      parameters = "800 / 120 chunks · lexical 5 · vector 5 · rerank 5 · exact read required";
    } else if (id === "turbovec") {
      parameters = "4-bit candidate · 20-query promotion gate · lexical fallback · optional trial";
    } else if (id === "crewai") {
      parameters = "sequential default · memory off · cache on · planning off · parallel max 3";
    } else if (id === "langgraph") {
      parameters = "typed reducers · thread_id = case_id · per-invocation subgraphs · interrupts";
    } else {
      parameters = tool.authority || "Projection only";
    }
    return '<tr><td data-label="System"><strong>' + escapeHtml(titleCase(id)) + '</strong></td><td data-label="Exact job">' + escapeHtml(tool.job) + '</td><td data-label="Public parameters">' + escapeHtml(parameters) + '</td></tr>';
  }).join("");
}

function renderKnowledge() {
  const layers = contracts.crew.layers.map(function (layer) {
    const roles = layer.primary_roles.map(function (id) {
      const role = roleForMachineId(id);
      return role ? role.call_name : id;
    });
    return '<article class="layer-card"><div class="layer-id">' + escapeHtml(layer.id) + '</div><div><h3>' + escapeHtml(layer.name) + '</h3><p>' + escapeHtml(layer.purpose) + '</p>' + list(roles) + '</div><div class="layer-output"><strong>Delivers</strong><br>' + escapeHtml(layer.outputs.join(" · ")) + '</div></article>';
  }).join("");
  const diagrams = DIAGRAMS.map(function (diagram) {
    return '<article class="card diagram-card"><a href="../assets/architecture/' + diagram.source + '" target="_blank" rel="noreferrer"><img src="../assets/architecture/' + diagram.file + '" alt="' + escapeHtml(diagram.title + ". " + diagram.description) + '"></a><div class="diagram-copy"><h3>' + escapeHtml(diagram.title) + '</h3><p>' + escapeHtml(diagram.description) + '</p><p><a href="../assets/architecture/' + diagram.source + '" target="_blank" rel="noreferrer">Open editable labeled SVG</a></p></div></article>';
  }).join("");
  const budgets = contracts.crew.perception_capsule.sections.map(function (section) {
    return '<div class="list-row"><div><h3>' + escapeHtml(titleCase(section.id)) + '</h3><p>' + escapeHtml(section.content) + '</p></div><span class="truth-label configured">' + section.budget.toLocaleString() + ' tokens</span></div>';
  }).join("");
  const methods = contracts.crew.research_methods.map(function (method) {
    return '<article class="card"><span class="eyebrow">' + escapeHtml(titleCase(method.id)) + '</span><p>' + escapeHtml(method.use) + '</p></article>';
  }).join("");
  return [
    '<section class="panel">',
      sectionHeading("Seven connected layers", "Databases and tools do not become a new architecture. Each performs one bounded job inside the same employee case."),
      '<div class="layer-stack">' + layers + '</div>',
    "</section>",
    '<section class="panel section">',
      sectionHeading("What each system actually does", "Connectivity is not authority. Every retrieved or generated result remains candidate evidence until exact-source and requirement checks pass."),
      '<div style="overflow-x:auto"><table class="tool-table"><thead><tr><th>System</th><th>Exact job</th><th>Public parameters</th></tr></thead><tbody>' + frameworkRows() + '</tbody></table></div>',
      '<div class="callout" style="margin-top:16px"><strong>Whole-project perception:</strong> stable CAG carries rules and role responsibility; LlamaIndex returns allowlisted nodes with metadata; TurboVec may accelerate the vector-candidate step after its benchmark gate; Orbit and Graphify point to structural entry points; exact source reads preserve authority and provenance. TurboVec never replaces the knowledge base or citations.</div>',
    "</section>",
    '<section class="panel section">',
      sectionHeading("Context capsule budget", "The 12,000-token ceiling compresses summaries, never provenance or current requirements."),
      '<div class="split"><div class="card list">' + budgets + '</div><div class="card"><h3>Overflow order</h3><p>Drop duplicate snippets → replace low-authority excerpts with citations → summarize prior receipts → ask to narrow scope → stop before dropping current requirements.</p><h3>Required lineage</h3><p>Every material claim keeps source reference, authority state, observed date, review date, and exact-read status.</p><h3>Retrieval fallback</h3><p>Deterministic lexical retrieval remains available when embeddings or TurboVec are absent, stale, or ineligible.</p></div></div>',
    "</section>",
    '<section class="panel section">',
      sectionHeading("Architecture views", "Each view uses exact text overlays on an editable SVG. The source artwork remains separate for future visual changes."),
      '<div class="diagram-grid">' + diagrams + '</div>',
    "</section>",
    '<section class="panel section">',
      sectionHeading("Research methods built into role work", "Requirements, market analysis, outreach, copy, design, and reports share evidence discipline but use different specialist methods."),
      '<div class="card-grid">' + methods + '</div>',
    "</section>",
    '<section class="panel section">',
      sectionHeading("Skill cleaning and updates", "A skill is discovered, quarantined, inspected, deduplicated, normalized, fixture-tested, reviewed, allowlisted, assigned, observed, updated, deprecated, then removed."),
      '<div class="split"><article class="card"><h3>Skill Spectre</h3><p>' + escapeHtml(contracts.crew.skill_lifecycle.skill_spectre.job) + '</p><p><strong>Current evidence:</strong> ' + escapeHtml(contracts.crew.skill_lifecycle.skill_spectre.current_evidence) + '. Semantic scanning is not proved.</p></article><article class="card"><h3>Video Spectre pattern</h3><p>' + escapeHtml(contracts.crew.skill_lifecycle.video_spectre_pattern.job) + '</p><p><strong>Current evidence:</strong> pattern only; no public tool execution record is claimed.</p></article></div>',
    "</section>",
  ].join("");
}

function renderRoleCard(role) {
  const defaults = role.task_defaults;
  return '<article class="card role-card" data-role-name="' + escapeHtml((role.call_name + " " + role.title + " " + role.id).toLowerCase()) + '"><header><span class="avatar" aria-hidden="true">' + escapeHtml(role.call_name.slice(0, 2).toUpperCase()) + '</span><div><h3>' + escapeHtml(role.call_name + " — " + role.title) + '</h3><div class="machine-id">' + escapeHtml(role.id) + '</div></div></header><p><strong>Goal:</strong> ' + escapeHtml(role.goal) + '</p><p>' + escapeHtml(role.purpose) + '</p><dl class="binding-grid compact"><div><dt>Owned output</dt><dd>' + escapeHtml(sentence(defaults.owned_output)) + '</dd></div><div><dt>Permission</dt><dd>' + escapeHtml(sentence(defaults.permission_mode)) + '</dd></div><div><dt>Required inputs</dt><dd>' + escapeHtml(defaults.inputs.map(sentence).join(" · ")) + '</dd></div><div><dt>Skills</dt><dd>' + escapeHtml(defaults.allowed_skills.length ? defaults.allowed_skills.join(" · ") : "No reviewed public skill assigned") + '</dd></div><div><dt>Tool ceiling</dt><dd>' + escapeHtml(defaults.allowed_tools.map(sentence).join(" · ")) + '</dd></div><div><dt>Reviewer route</dt><dd>' + escapeHtml(defaults.reviewer_route.map(roleLabel).join(" → ")) + '</dd></div><div><dt>Handoff</dt><dd>' + escapeHtml(roleLabel(defaults.handoff_to)) + '</dd></div></dl><div class="role-section"><strong>Owns</strong>' + list(role.owns) + '</div><div class="role-section"><strong>Must not</strong><div class="token-list">' + role.forbidden.map(function (item) { return '<span class="token forbidden">' + escapeHtml(sentence(item)) + '</span>'; }).join("") + '</div></div><p class="contract-rule">Capability ceiling only; never a permission grant.</p></article>';
}

function renderTeam() {
  const visibleRoles = contracts.roles.roles.filter(function (role) {
    const textMatch = !roleFilter || (role.call_name + " " + role.title + " " + role.id + " " + role.owns.join(" ")).toLowerCase().includes(roleFilter.toLowerCase());
    const pack = packFilter === "all" ? null : workflowById(packFilter);
    const packMatch = !pack || selectedRoleEntries(pack).some(function (entry) { return entry.role.id === role.id; });
    return textMatch && packMatch;
  });
  const packButtons = ['<button class="chip-button ' + (packFilter === "all" ? "active" : "") + '" data-pack-filter="all" type="button">All roles</button>'].concat(contracts.workflows.packs.map(function (pack) {
    return '<button class="chip-button ' + (packFilter === pack.id ? "active" : "") + '" data-pack-filter="' + escapeHtml(pack.id) + '" type="button">' + escapeHtml(pack.label) + '</button>';
  })).join("");
  const packDetails = contracts.workflows.packs.map(function (pack) {
    const baseRoles = pack.roles.map(roleLabel).join(" → ");
    const closureRoles = selectedRoleEntries(pack).filter(function (entry) { return entry.base_or_closure === "review_closure"; }).map(function (entry) { return roleLabel(entry.role.id); }).join(" → ");
    return '<details' + (pack.id === caseDraft.workflow_pack ? " open" : "") + '><summary>' + escapeHtml(pack.label) + '</summary><div class="details-body"><p><strong>Trigger:</strong> ' + escapeHtml(pack.trigger) + '</p><p><strong>Base roles:</strong> ' + escapeHtml(baseRoles) + '</p><p><strong>Review closure:</strong> ' + escapeHtml(closureRoles || "Already contained in the base pack") + '</p><p><strong>Methods:</strong> ' + escapeHtml(pack.methods.map(sentence).join(" · ")) + '</p><p><strong>Outputs:</strong> ' + escapeHtml(pack.outputs.map(sentence).join(" · ")) + '</p><p><strong>Done:</strong> ' + escapeHtml(pack.done.join(" · ")) + '</p></div></details>';
  }).join("");
  return [
    '<section class="panel">',
      sectionHeading("Responsive role crew", "Roles are durable responsibility contracts, not personas and not permanent runtime authority."),
      '<div class="role-toolbar"><label class="field" style="flex:1 1 260px"><span>Find a responsibility</span><input id="roleSearch" type="search" value="' + escapeHtml(roleFilter) + '" placeholder="Search Oksana, design, outreach, verification…"></label><span class="truth-label configured">' + visibleRoles.length + ' of ' + contracts.roles.roles.length + ' roles</span></div>',
      '<div class="filter-row" style="margin:14px 0 18px">' + packButtons + '</div>',
      '<div class="card-grid" id="roleGrid">' + visibleRoles.map(renderRoleCard).join("") + '</div>',
    "</section>",
    '<section class="panel section">',
      sectionHeading("Adaptive workflow packs", "The controller selects the smallest pack that owns the required outputs, check, approval, or handoff. A pack is a starting contract, not a fixed crew."),
      packDetails,
    "</section>",
    '<section class="panel section">',
      sectionHeading("Communication protocol", "Every handoff carries the same minimum evidence so employees and agents can continue without reconstructing hidden context."),
      '<div class="three-col"><article class="card"><h3>Maker handoff</h3><p>Case ID, goal, role, requirement versions, source refs, exact files, candidate artifact, checks, known gaps, and stop conditions.</p></article><article class="card"><h3>Reviewer verdict</h3><p>Approve, revise, or block; exact finding; violated requirement or boundary; evidence; and the smallest repair request.</p></article><article class="card"><h3>Learning handoff</h3><p>Exact result, readback, reusable meaning, lineage, owner, freshness date, supersession, and retrieval regression check.</p></article></div>',
    "</section>",
  ].join("");
}

function traceItems() {
  const requirementState = caseDraft.goal ? "Draft mission prepared; exact requirements still require retrieval and owner confirmation." : "No goal has been captured.";
  return [
    ["01", "Request and authority", caseDraft.goal || "Capture one bounded goal.", caseDraft.employee_role],
    ["02", "Source boundary", caseDraft.evidence_boundary, "LlamaIndex allowlist + exact reads"],
    ["03", "Requirement versions", requirementState, "Oksana prepares · requirement owner approves"],
    ["04", "Role work", caseDraft.output || "Expected output not yet named.", workflowById(caseDraft.workflow_pack)?.label || "Pack not selected"],
    ["05", "Action validation", "Iryna checks requirement coverage, permissions, side effects, rollback, verification, and readback.", "No execution from dashboard"],
    ["06", "Independent review", "Halyna reviews the frozen candidate; the maker applies any repair.", caseDraft.reviewer],
    ["07", "Receipt and knowledge", "Record the exact result and readback. Larysa may propose durable meaning with lineage and freshness.", receipts.length + " browser-local receipt(s)"],
  ];
}

function renderReview() {
  const trace = traceItems().map(function (item) {
    return '<div class="trace-item" data-step="' + item[0] + '"><h3>' + escapeHtml(item[1]) + '</h3><p>' + escapeHtml(item[2]) + '</p><div class="token-list" style="margin-top:8px"><span class="token">' + escapeHtml(item[3]) + '</span></div></div>';
  }).join("");
  const receiptRows = receipts.length ? receipts.map(function (receipt) {
    return '<div class="list-row"><div><h3>' + escapeHtml(receipt.id) + '</h3><p>' + escapeHtml(receipt.summary) + '</p></div><span class="truth-label tested">' + escapeHtml(receipt.created_at.slice(0, 10)) + '</span></div>';
  }).join("") : '<p>No local receipt has been recorded. A packet export is not an execution receipt.</p>';
  return [
    '<section class="panel">',
      sectionHeading("End-to-end trace", "The same case ID links the employee request, sources, requirement versions, role work, verdict, approval, action, readback, and knowledge candidate.", '<button class="secondary-button" id="downloadReview" type="button">Download review packet</button>'),
      '<div class="trace-layout"><div class="trace-chain">' + trace + '</div><aside class="card trace-aside"><h3>Current truth state</h3><dl><div><dt>Case</dt><dd>' + escapeHtml(caseDraft.case_id) + '</dd></div><div><dt>Provider</dt><dd>Disabled</dd></div><div><dt>Writeback</dt><dd>Disabled</dd></div><div><dt>Execution</dt><dd>Not performed</dd></div><div><dt>Review</dt><dd>' + escapeHtml(caseDraft.goal ? "Packet can be prepared" : "Missing goal/output") + '</dd></div></dl></aside></div>',
    "</section>",
    '<section class="panel section">',
      sectionHeading("Fail-closed review gates", "A graph transition may control sequence, but it cannot turn missing evidence or permission into truth."),
      '<div class="status-table">',
        '<div class="status-row"><strong>Source boundary</strong><p>Every source class is allowlisted; private matches are refused; material action requires an exact read.</p><span class="truth-label configured">required</span></div>',
        '<div class="status-row"><strong>Requirement coverage</strong><p>All applicable approved requirement versions are covered or an owner-approved exception is recorded.</p><span class="truth-label configured">required</span></div>',
        '<div class="status-row"><strong>Maker / reviewer</strong><p>The person or agent producing a consequential candidate cannot provide its final independent verdict.</p><span class="truth-label configured">separate</span></div>',
        '<div class="status-row"><strong>Approval interrupt</strong><p>External, private, irreversible, or otherwise high-risk actions pause with a JSON-safe summary and exact target.</p><span class="truth-label gated">owner gate</span></div>',
        '<div class="status-row"><strong>Idempotent action</strong><p>Side effects occur after the interrupt and use an action ID so resumed nodes cannot repeat them silently.</p><span class="truth-label configured">required</span></div>',
        '<div class="status-row"><strong>Readback</strong><p>Command success is not the result. The target state is read back and attached to the receipt.</p><span class="truth-label configured">required</span></div>',
      "</div>",
    "</section>",
    '<section class="panel section">',
      sectionHeading("Browser-local receipt notebook", "This notebook is only a UX fixture. Durable receipts belong to the controller/checkpointer and run record."),
      '<div class="split"><form class="card" id="receiptForm"><label class="field"><span>Verified result summary</span><textarea name="summary" maxlength="800" required placeholder="Record only a public-safe result that was independently verified."></textarea></label><div class="form-actions"><button class="secondary-button" type="submit">Add local example receipt</button><button class="danger-button" id="clearReceipts" type="button">Clear local receipts</button></div></form><div class="card list" id="receiptList">' + receiptRows + '</div></div>',
    "</section>",
  ].join("");
}

function renderSetup() {
  const configPreview = {
    boundary: "public browser-local proposal",
    llamaindex: {
      chunk_size: settings.chunk_size,
      chunk_overlap: settings.chunk_overlap,
      lexical_top_k: settings.lexical_top_k,
      vector_top_k: settings.vector_top_k,
      rerank_top_k: settings.rerank_top_k,
      final_source_limit: settings.final_source_limit,
      require_source_paths: true,
      require_exact_read_for_action: true,
      fallback_to_lexical: true,
    },
    turbovec: {
      requested_candidate: settings.turbovec_candidate,
      effective_status: settings.turbovec_candidate ? "requested_but_runtime_must_pass_gate" : "off",
      bit_width: 4,
      default_backend_changed: false,
    },
    langgraph: {
      requested_checkpointer: settings.checkpointer,
      effective_public_demo: "none",
      thread_id: "case_id",
    },
    crewai: {
      process: "sequential",
      memory: false,
      cache: true,
      planning: false,
      maximum_parallel_tasks: 3,
    },
  };
  return [
    '<section class="panel">',
      sectionHeading("Portable installation boundary", "The public repository runs as a static local dashboard. Runtime adapters stay optional, least-privilege, and outside Git.", '<label class="secondary-button">Import configuration<input id="importConfigFile" type="file" accept="application/json,.json" hidden></label><button class="secondary-button" id="exportConfig" type="button">Export local configuration</button>'),
      '<div class="split"><article class="card"><h3>1. Serve the public project locally</h3><p>From the repository root, run a static server and open the Crew Desk route.</p><pre class="config-code">python3 -m http.server 4173\n\nhttp://127.0.0.1:4173/project/dashboard/#today</pre></article><article class="card"><h3>2. Connect an optional local bridge</h3><p>The dashboard accepts only its own origin or plain HTTP loopback. The browser still does not activate providers or write to the bridge.</p><pre class="config-code">http://127.0.0.1:8787\nhttp://localhost:8787</pre></article></div>',
    "</section>",
    '<section class="panel section">',
      sectionHeading("Retrieval and state configuration", "These browser settings produce a review proposal. The real runtime must validate, benchmark, migrate, and read back its own configuration."),
      '<form id="settingsForm">',
        '<div class="settings-group"><h3>Local bridge</h3><p>Never put tokens, credentials, private URLs, or account identifiers in this field.</p><div class="field-grid"><label class="field full"><span>Bridge base</span><input name="bridge_base" value="' + escapeHtml(settings.bridge_base) + '" required><small>Same origin or HTTP 127.0.0.1 / localhost only.</small></label><label class="field full"><span>Allowed corpus</span><textarea name="allowed_corpus" required>' + escapeHtml(settings.allowed_corpus) + '<\/textarea></label><label class="field full"><span>Excluded corpus</span><textarea name="excluded_corpus" required>' + escapeHtml(settings.excluded_corpus) + '<\/textarea></label></div></div>',
        '<div class="settings-group"><h3>LlamaIndex perception</h3><p>Document/node identities and metadata remain authoritative; rankings are candidate evidence.</p><div class="field-grid three"><label class="field"><span>Chunk size</span><input type="number" name="chunk_size" min="256" max="2000" value="' + settings.chunk_size + '"></label><label class="field"><span>Chunk overlap</span><input type="number" name="chunk_overlap" min="0" max="400" value="' + settings.chunk_overlap + '"></label><label class="field"><span>Final source limit</span><input type="number" name="final_source_limit" min="1" max="20" value="' + settings.final_source_limit + '"></label><label class="field"><span>Lexical top-k</span><input type="number" name="lexical_top_k" min="1" max="20" value="' + settings.lexical_top_k + '"></label><label class="field"><span>Vector top-k</span><input type="number" name="vector_top_k" min="1" max="20" value="' + settings.vector_top_k + '"></label><label class="field"><span>Rerank top-k</span><input type="number" name="rerank_top_k" min="1" max="20" value="' + settings.rerank_top_k + '"></label></div></div>',
        '<div class="settings-group"><h3>Optional TurboVec candidate</h3><p>TurboVec sits behind the LlamaIndex vector-store adapter. It does not store authority or replace lexical fallback, node metadata, citations, or exact reads.</p><label class="checkbox-row"><input type="checkbox" name="turbovec_candidate"' + (settings.turbovec_candidate ? " checked" : "") + '><span><strong>Request the 4-bit candidate for a qualifying local runtime.</strong><br>The runtime must still pass the fixed 20-query recall, citation, metadata-filter, persistence-parity, and independent-review gate.</span></label></div>',
        '<div class="settings-group"><h3>LangGraph checkpoint proposal</h3><p>The public demo has no checkpointer. SQLite requires local migration/recovery proof; PostgreSQL requires team tenancy, backup, and recovery proof.</p><label class="field"><span>Requested runtime mode</span><select name="checkpointer"><option value="none"' + (settings.checkpointer === "none" ? " selected" : "") + '>None — public/static default</option><option value="sqlite"' + (settings.checkpointer === "sqlite" ? " selected" : "") + '>SQLite — proposed local single-user</option><option value="postgresql"' + (settings.checkpointer === "postgresql" ? " selected" : "") + '>PostgreSQL — proposed team runtime</option></select></label></div>',
        '<div class="form-actions"><button class="primary-button" type="submit">Save browser-local proposal</button><button class="danger-button" id="resetSettings" type="button">Reset local settings</button></div>',
      "</form>",
    "</section>",
    '<section class="panel section">',
      sectionHeading("Effective public contract", "Provider and writeback stay disabled regardless of browser selections."),
      '<pre class="config-code" id="configPreview">' + escapeHtml(JSON.stringify(configPreview, null, 2)) + '</pre>',
    "</section>",
    '<section class="panel section">',
      sectionHeading("Obsidian, WikiLLM, Orbit, and Graphify", "The portable repository remains useful without any private vault. Local adapters add bounded capabilities without copying private knowledge into Git."),
      '<div class="card-grid"><article class="card"><h3>WikiLLM</h3><p>Portable reviewed memory: indexes, run summaries, decisions, issues, insights, and append-only lineage.</p></article><article class="card"><h3>Obsidian</h3><p>Optional human semantic workspace. Community plugins are privileged local code: review, pin, back up, and keep restricted-mode fallback.</p></article><article class="card"><h3>Orbit</h3><p>Optional local structural adapter for an allowlisted corpus. Its results point to exact files; they never decide requirements or permission.</p></article><article class="card"><h3>Graphify</h3><p>Generated relationship reference for definitions, paths, dependencies, and likely blast radius. Regenerate when its source commit is stale.</p></article></div>',
    "</section>",
  ].join("");
}

function guideAdvice(query) {
  const text = query.toLowerCase();
  let pack = contracts.workflows.packs.find(function (item) { return item.id === "employee_onboarding"; });
  if (/research|market|requirement|customer|pain|prd|icp/.test(text)) pack = workflowById("requirements_research");
  else if (/outreach|message|contact|lead|channel/.test(text)) pack = workflowById("outreach");
  else if (/design|visual|interface|image|layout/.test(text)) pack = workflowById("design");
  else if (/write|copy|content|caption/.test(text)) pack = workflowById("content_and_copy");
  else if (/code|implement|fix|build|test/.test(text)) pack = workflowById("implementation");
  else if (/report|metric|analysis|decision/.test(text)) pack = workflowById("reporting");
  else if (/publish|deploy|send|push|external/.test(text)) pack = workflowById("release_and_external_action");
  else if (/task|plan|daily|handoff/.test(text)) pack = workflowById("task_planning");
  return "Suggested pack: " + pack.label + ". Start by confirming: decision owner; approved and excluded sources; current requirement; exact output; maker; different reviewer; stop condition; and whether any private, external, or irreversible action requires an interrupt. Suggested roles: " + pack.roles.map(roleLabel).join(" → ") + ".";
}

function validateBridge(value) {
  let parsed;
  try {
    parsed = new URL(String(value || "").trim(), window.location.origin);
  } catch (_error) {
    throw new Error("Enter a valid same-origin or loopback URL.");
  }
  const sameOrigin = parsed.origin === window.location.origin;
  const loopback = parsed.protocol === "http:" && (parsed.hostname === "127.0.0.1" || parsed.hostname === "localhost");
  if (!sameOrigin && !loopback) throw new Error("Bridge base must be this origin or HTTP 127.0.0.1 / localhost.");
  return parsed.origin;
}

function normalizeImportedSettings(payload) {
  const source = payload && typeof payload === "object" && payload.settings && typeof payload.settings === "object"
    ? payload.settings
    : payload;
  if (!source || typeof source !== "object" || Array.isArray(source)) throw new Error("Configuration must be a JSON object.");
  const allowed = new Set(Object.keys(DEFAULT_SETTINGS));
  const unknown = Object.keys(source).filter(function (key) { return !allowed.has(key); });
  if (unknown.length) throw new Error("Unknown configuration fields: " + unknown.join(", ") + ".");
  if (Object.prototype.hasOwnProperty.call(source, "turbovec_candidate") && typeof source.turbovec_candidate !== "boolean") {
    throw new Error("turbovec_candidate must be a JSON boolean.");
  }
  const next = Object.assign({}, DEFAULT_SETTINGS, source);
  next.bridge_base = validateBridge(next.bridge_base);
  ["chunk_size", "chunk_overlap", "lexical_top_k", "vector_top_k", "rerank_top_k", "final_source_limit"].forEach(function (key) {
    next[key] = Number(next[key]);
    if (!Number.isInteger(next[key])) throw new Error(key + " must be an integer.");
  });
  if (next.chunk_size < 256 || next.chunk_size > 2000) throw new Error("chunk_size must be between 256 and 2000.");
  if (next.chunk_overlap < 0 || next.chunk_overlap >= next.chunk_size) throw new Error("chunk_overlap must be non-negative and smaller than chunk_size.");
  ["lexical_top_k", "vector_top_k", "rerank_top_k", "final_source_limit"].forEach(function (key) {
    if (next[key] < 1 || next[key] > 20) throw new Error(key + " must be between 1 and 20.");
  });
  if (!["none", "sqlite", "postgresql"].includes(next.checkpointer)) throw new Error("Unknown checkpointer proposal.");
  if (typeof next.turbovec_candidate !== "boolean") throw new Error("turbovec_candidate must be a JSON boolean.");
  next.allowed_corpus = String(next.allowed_corpus || "").slice(0, 2000);
  next.excluded_corpus = String(next.excluded_corpus || "").slice(0, 2000);
  if (!next.allowed_corpus || !next.excluded_corpus) throw new Error("Allowed and excluded corpus fields are required.");
  return next;
}

function bindEvents() {
  const guideForm = document.querySelector("#guideForm");
  if (guideForm) guideForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const input = document.querySelector("#guideInput");
    const query = input.value.trim();
    localStorage.setItem(STORE.guide, query);
    document.querySelector("#guideResult").textContent = query ? guideAdvice(query) : "Describe the task or uncertainty first.";
  });

  const caseForm = document.querySelector("#caseForm");
  if (caseForm) caseForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const data = Object.fromEntries(new FormData(caseForm).entries());
    const missing = ["goal", "employee_role", "output", "evidence_boundary", "reviewer", "stop_condition"].filter(function (key) { return !String(data[key] || "").trim(); });
    const errors = document.querySelector("#caseErrors");
    if (missing.length) {
      errors.hidden = false;
      errors.textContent = "Complete the required fields: " + missing.map(titleCase).join(", ") + ".";
      return;
    }
    errors.hidden = true;
    caseDraft = Object.assign({}, caseDraft, data, { updated_at: new Date().toISOString(), state: "context_bound" });
    saveStored(STORE.caseDraft, caseDraft);
    showNotice("Mission saved in this browser. No provider or external system was contacted.");
    render();
  });

  const preparePacket = document.querySelector("#preparePacket");
  if (preparePacket) preparePacket.addEventListener("click", function () { downloadJson("archflow-case-review-packet.json", currentPacket()); });
  const resetCase = document.querySelector("#resetCase");
  if (resetCase) resetCase.addEventListener("click", function () {
    localStorage.removeItem(STORE.caseDraft);
    caseDraft = Object.assign({}, DEFAULT_CASE);
    showNotice("The browser-local mission draft was reset.");
    render();
  });

  const roleSearch = document.querySelector("#roleSearch");
  if (roleSearch) roleSearch.addEventListener("input", function () {
    roleFilter = roleSearch.value;
    render();
    const next = document.querySelector("#roleSearch");
    if (next) {
      next.focus();
      next.setSelectionRange(roleFilter.length, roleFilter.length);
    }
  });
  document.querySelectorAll("[data-pack-filter]").forEach(function (button) {
    button.addEventListener("click", function () {
      packFilter = button.getAttribute("data-pack-filter") || "all";
      render();
    });
  });

  const downloadReview = document.querySelector("#downloadReview");
  if (downloadReview) downloadReview.addEventListener("click", function () { downloadJson("archflow-review-packet.json", currentPacket()); });
  const receiptForm = document.querySelector("#receiptForm");
  if (receiptForm) receiptForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const summary = String(new FormData(receiptForm).get("summary") || "").trim();
    if (!summary) return;
    receipts = Array.isArray(receipts) ? receipts : [];
    receipts.unshift({ id: "local-receipt-" + Date.now(), summary: summary, created_at: new Date().toISOString(), durable: false });
    saveStored(STORE.receipts, receipts);
    showNotice("Example receipt stored in this browser only.");
    render();
  });
  const clearReceipts = document.querySelector("#clearReceipts");
  if (clearReceipts) clearReceipts.addEventListener("click", function () {
    receipts = [];
    localStorage.removeItem(STORE.receipts);
    showNotice("Browser-local example receipts were cleared.");
    render();
  });

  const settingsForm = document.querySelector("#settingsForm");
  if (settingsForm) settingsForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const data = Object.fromEntries(new FormData(settingsForm).entries());
    try {
      data.bridge_base = validateBridge(data.bridge_base);
    } catch (error) {
      showNotice(error.message, "warning");
      return;
    }
    ["chunk_size", "chunk_overlap", "lexical_top_k", "vector_top_k", "rerank_top_k", "final_source_limit"].forEach(function (key) {
      data[key] = Number(data[key]);
    });
    data.turbovec_candidate = new FormData(settingsForm).has("turbovec_candidate");
    if (data.chunk_overlap >= data.chunk_size) {
      showNotice("Chunk overlap must be smaller than chunk size.", "warning");
      return;
    }
    settings = Object.assign({}, DEFAULT_SETTINGS, data);
    saveStored(STORE.settings, settings);
    showNotice("Configuration proposal saved in this browser. Runtime defaults were not changed.");
    render();
  });
  const exportConfig = document.querySelector("#exportConfig");
  if (exportConfig) exportConfig.addEventListener("click", function () {
    downloadJson("archflow-local-configuration-proposal.json", { schema_version: "1.0.0", settings: settings, provider: "disabled", writeback: "disabled" });
  });
  const importConfigFile = document.querySelector("#importConfigFile");
  if (importConfigFile) importConfigFile.addEventListener("change", async function () {
    const file = importConfigFile.files && importConfigFile.files[0];
    if (!file) return;
    if (file.size > 65536) {
      showNotice("Configuration files must be 64 KB or smaller.", "warning");
      importConfigFile.value = "";
      return;
    }
    try {
      settings = normalizeImportedSettings(JSON.parse(await file.text()));
      saveStored(STORE.settings, settings);
      showNotice("Validated configuration imported into this browser. Runtime defaults were not changed.");
      render();
    } catch (error) {
      showNotice("Import rejected: " + error.message, "warning");
      importConfigFile.value = "";
    }
  });
  const resetSettings = document.querySelector("#resetSettings");
  if (resetSettings) resetSettings.addEventListener("click", function () {
    settings = Object.assign({}, DEFAULT_SETTINGS);
    localStorage.removeItem(STORE.settings);
    showNotice("Browser-local configuration was reset.");
    render();
  });
}

function render() {
  renderNav();
  renderHeader();
  const renderers = {
    today: renderToday,
    work: renderWork,
    knowledge: renderKnowledge,
    team: renderTeam,
    review: renderReview,
    setup: renderSetup,
  };
  view.innerHTML = renderers[activeRoute]();
  bindEvents();
  document.title = ROUTES.find(function (route) { return route.id === activeRoute; }).title + " | ArchFlow Crew Desk";
}

async function loadContracts() {
  view.innerHTML = document.querySelector("#loadingTemplate").innerHTML;
  const paths = [
    "../system/contracts/knowledge-crew-config.json",
    "../system/contracts/role-catalog.json",
    "../system/contracts/role-workflows.json",
    "../system/contracts/operating-model.json",
    "./data.json",
  ];
  const values = await Promise.all(paths.map(async function (path) {
    const response = await fetch(path, { cache: "no-store" });
    if (!response.ok) throw new Error(path + " returned " + response.status);
    return response.json();
  }));
  contracts = { crew: values[0], roles: values[1], workflows: values[2], controller: values[3], snapshot: values[4] };
}

window.addEventListener("hashchange", function () {
  activeRoute = normalizeRoute(window.location.hash.replace(/^#/, ""));
  if (window.location.hash !== "#" + activeRoute) history.replaceState(null, "", "#" + activeRoute);
  render();
  view.focus({ preventScroll: true });
  window.scrollTo({ top: 0, behavior: "smooth" });
});

exportHeader.addEventListener("click", function () {
  downloadJson("archflow-local-review-packet.json", currentPacket());
});

loadContracts()
  .then(function () {
    if (window.location.hash !== "#" + activeRoute) history.replaceState(null, "", "#" + activeRoute);
    render();
  })
  .catch(function (error) {
    view.innerHTML = '<section class="panel"><span class="eyebrow">Contracts unavailable</span><h2>Serve the repository locally, then reload.</h2><p>The Crew Desk loads JSON contracts with browser fetch. Opening the HTML as a local file may block those requests.</p><pre class="config-code">python3 -m http.server 4173\n\nhttp://127.0.0.1:4173/project/dashboard/#today</pre><p class="callout warning"><strong>Load error:</strong> ' + escapeHtml(error.message) + '</p></section>';
  });
