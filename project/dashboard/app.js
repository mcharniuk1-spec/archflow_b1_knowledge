const tabs = [
  { id: "overview", label: "Overview", glyph: "OV" },
  { id: "wikillm", label: "WikiLLM Memory", glyph: "WK" },
  { id: "graphify", label: "Graphify", glyph: "GF" },
  { id: "langgraph", label: "LangGraph Runs", glyph: "LG" },
  { id: "llamaindex", label: "LlamaIndex Query", glyph: "LI" },
  { id: "crewai", label: "CrewAI Outputs", glyph: "CR" },
  { id: "langsmith", label: "LangSmith", glyph: "LS" },
  { id: "env", label: "Env Config", glyph: "EN" },
];

let dashboardData = null;
let activeTab = "overview";

const view = document.querySelector("#view");
const nav = document.querySelector("#nav");
const generatedAt = document.querySelector("#generatedAt");

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function badge(status) {
  const text = String(status || "unknown");
  const lower = text.toLowerCase();
  const tone = lower.includes("active") || lower.includes("present") || lower.includes("ok") || lower.includes("tracked") || lower.includes("static") || lower.includes("files") || lower.includes("submitted")
    ? "ok"
    : lower.includes("missing") || lower.includes("not_installed") || lower.includes("not_generated") || lower.includes("awaiting") || lower.includes("configured_not_installed")
      ? "warn"
      : lower.includes("fail") || lower.includes("blocked")
        ? "block"
        : "";
  return `<span class="badge ${tone}">${escapeHtml(text.replaceAll("_", " "))}</span>`;
}

function pathLink(path) {
  const cleanPath = String(path || "");
  const href = cleanPath.startsWith("project/")
    ? `../${cleanPath.replace(/^project\//, "")}`
    : `../../${cleanPath}`;
  return `<a class="code" href="${escapeHtml(href)}">${escapeHtml(cleanPath)}</a>`;
}

function renderNav() {
  nav.innerHTML = tabs
    .map((tab) => `
      <button type="button" class="${tab.id === activeTab ? "active" : ""}" data-tab="${tab.id}">
        <span class="glyph">${tab.glyph}</span>
        <span>${tab.label}</span>
      </button>
    `)
    .join("");

  nav.querySelectorAll("button").forEach((button) => {
    button.addEventListener("click", () => {
      activeTab = button.dataset.tab;
      render();
    });
  });
}

function card({ label, value, note, tone }) {
  return `
    <article class="card">
      <div class="card-label">${escapeHtml(label)}</div>
      <div class="card-value tone-${tone || "ok"}">${escapeHtml(String(value).replaceAll("_", " "))}</div>
      ${note ? `<div class="card-note">${escapeHtml(note)}</div>` : ""}
    </article>
  `;
}

function table(headers, rows) {
  return `
    <table class="table">
      <thead><tr>${headers.map((h) => `<th>${escapeHtml(h)}</th>`).join("")}</tr></thead>
      <tbody>${rows.map((row) => `<tr>${row.map((c) => `<td>${c}</td>`).join("")}</tr>`).join("")}</tbody>
    </table>
  `;
}

function renderOverview(data) {
  const cards = data.status_cards.map((c) => card(c)).join("");
  const recent = data.activity.slice(0, 7);
  view.innerHTML = `
    <div class="grid cols-6">${cards}</div>
    <div class="split" style="margin-top:16px">
      <section class="panel">
        <h2 class="section-title">Current Workflow Spine</h2>
        <p class="muted">Scroll horizontally inside the node strip to inspect the full path.</p>
        <div class="node-flow">
          ${data.langgraph.nodes.map((node) => `
            <div class="node">
              <strong>${escapeHtml(node.id)}</strong>
              <span>${escapeHtml(node.purpose)}</span>
              <span class="owner">${escapeHtml(node.owner)}</span>
            </div>
          `).join("")}
        </div>
        <div class="callout">
          LangGraph is configured as the workflow spine, but runtime packages are not installed in this public project yet. This dashboard tracks contracts and files until the first proof workflow exists.
        </div>
      </section>
      <section class="panel">
        <h2 class="section-title">Phase Decision</h2>
        <div class="list">
          <div class="row"><span class="row-title">Phase 1</span><div class="row-meta">Codex, GitHub, LangSmith, Obsidian, and WikiLLM files remain the primary operating surfaces.</div></div>
          <div class="row"><span class="row-title">Phase 2</span><div class="row-meta">This local dashboard reads public project files and shows status, activity, nodes, agents, and config health.</div></div>
          <div class="row"><span class="row-title">Phase 3</span><div class="row-meta">Full control panel only after one complete LangGraph/LlamaIndex/CrewAI proof run works.</div></div>
        </div>
      </section>
    </div>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Recent Project Activity</h2>
      ${table(["Kind", "Title", "Path"], recent.map((item) => [
        badge(item.kind),
        escapeHtml(item.title),
        pathLink(item.path),
      ]))}
    </section>
  `;
}

function renderWiki(data) {
  view.innerHTML = `
    <div class="grid cols-3">
      ${card({ label: "Wiki files", value: data.wiki.file_count, note: "Public durable memory layer", tone: "ok" })}
      ${card({ label: "Memory", value: data.wiki.memory_path, note: "Current stable project facts", tone: "ok" })}
      ${card({ label: "Insights", value: data.wiki.insights_path, note: "Reusable reasoning layer", tone: "ok" })}
    </div>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">WikiLLM Files</h2>
      <div class="list">
        ${data.wiki.files.map((file) => `
          <article class="row">
            <span class="row-title">${escapeHtml(file.title)}</span>
            <div class="row-meta">${pathLink(file.path)}</div>
            <p>${escapeHtml(file.excerpt)}</p>
          </article>
        `).join("")}
      </div>
    </section>
  `;
}

function renderGraphify(data) {
  const hasGraph = data.graphify.status === "available";
  view.innerHTML = `
    <div class="grid cols-2">
      ${card({ label: "Graphify status", value: data.graphify.status, note: "Generated structure reference", tone: hasGraph ? "ok" : "warn" })}
      ${card({ label: "Recommended next", value: "After runtime code", note: data.graphify.recommended_next, tone: "warn" })}
    </div>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Graphify Links</h2>
      ${hasGraph
        ? `<div class="list">${data.graphify.paths.map((p) => `<div class="row">${pathLink(p)}</div>`).join("")}</div>`
        : `<div class="callout">No Graphify output is present in this public project yet. Generate it after LangGraph dashboard/runtime code exists so the graph reflects the real implementation.</div>`
      }
    </section>
  `;
}

function renderLangGraph(data) {
  view.innerHTML = `
    <div class="grid cols-3">
      ${card({ label: "Status", value: data.langgraph.status, tone: "warn" })}
      ${card({ label: "Runtime", value: data.langgraph.runtime, tone: "warn" })}
      ${card({ label: "Revision loop limit", value: data.langgraph.params.max_revision_loops || "unset", tone: "ok" })}
    </div>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Configured Nodes</h2>
      <p class="muted">These are contract nodes from the YAML config, not completed runtime executions.</p>
      ${table(["Node", "Owner", "Purpose", "Output"], data.langgraph.nodes.map((node) => [
        `<strong>${escapeHtml(node.id)}</strong>`,
        badge(node.owner),
        escapeHtml(node.purpose),
        Array.isArray(node.output) ? node.output.map(escapeHtml).join("<br>") : escapeHtml(node.output),
      ]))}
    </section>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Routing And Stop Logic</h2>
      ${table(["From", "To", "Condition"], data.langgraph.edges.map((edge) => [
        escapeHtml(edge.from),
        escapeHtml(edge.to || ""),
        escapeHtml(edge.condition || "always"),
      ]))}
    </section>
  `;
}

function scoreResult(query, doc) {
  const terms = query.toLowerCase().split(/\s+/).filter(Boolean);
  const text = `${doc.title} ${doc.path} ${doc.text}`.toLowerCase();
  return terms.reduce((sum, term) => sum + (text.includes(term) ? 1 : 0), 0);
}

function renderLlamaIndex(data) {
  view.innerHTML = `
    <div class="grid cols-3">
      ${card({ label: "Status", value: data.llamaindex.status, tone: "warn" })}
      ${card({ label: "Approved corpus", value: data.llamaindex.include.join(", "), tone: "ok" })}
      ${card({ label: "Top K", value: data.llamaindex.similarity_top_k || "5", note: "Contract value", tone: "ok" })}
    </div>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Local Query Test</h2>
      <p class="muted">This is a lexical dashboard test over approved public files. It is not a vector index and does not replace LlamaIndex runtime.</p>
      <div class="query-box">
        <input type="search" id="queryInput" value="LangGraph CrewAI WikiLLM" aria-label="Search approved corpus" />
        <button class="primary" id="queryButton">Search</button>
      </div>
      <div id="queryResults"></div>
    </section>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Corpus Boundary</h2>
      ${table(["Include", "Exclude"], [[
        data.llamaindex.include.map(escapeHtml).join("<br>"),
        data.llamaindex.exclude.map(escapeHtml).join("<br>"),
      ]])}
    </section>
  `;

  const input = document.querySelector("#queryInput");
  const button = document.querySelector("#queryButton");
  const results = document.querySelector("#queryResults");
  const runQuery = () => {
    const query = input.value.trim();
    const scored = data.corpus
      .map((doc) => ({ ...doc, score: scoreResult(query, doc) }))
      .filter((doc) => doc.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, 8);
    results.innerHTML = scored.length
      ? `<div class="list">${scored.map((doc) => `
          <article class="row">
            <span class="row-title">${escapeHtml(doc.title)}</span>
            <div class="row-meta">${pathLink(doc.path)} · score ${doc.score}</div>
            <p>${escapeHtml(doc.text.slice(0, 360))}</p>
          </article>
        `).join("")}</div>`
      : `<div class="callout">No local matches. Try terms like WikiLLM, LangSmith, CrewAI, LangGraph, dashboard, or source.</div>`;
  };
  button.addEventListener("click", runQuery);
  input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") runQuery();
  });
  runQuery();
}

function renderCrew(data) {
  view.innerHTML = `
    <div class="grid cols-3">
      ${card({ label: "Status", value: data.crewai.status, tone: "warn" })}
      ${card({ label: "Process", value: data.crewai.process, tone: "ok" })}
      ${card({ label: "Memory", value: data.crewai.memory, note: "Disabled until boundaries are proven", tone: "warn" })}
    </div>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Agent Roles</h2>
      ${table(["Agent", "Role", "Goal", "Skills"], data.crewai.agents.map((agent) => [
        `<strong>${escapeHtml(agent.id)}</strong>`,
        escapeHtml(agent.role),
        escapeHtml(agent.goal),
        Array.isArray(agent.skills) ? agent.skills.map(escapeHtml).join("<br>") : "",
      ]))}
    </section>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Expected Task Outputs</h2>
      ${table(["Task", "Agent", "Expected output"], data.crewai.tasks.map((task) => [
        escapeHtml(task.id),
        badge(task.agent),
        escapeHtml(task.expected_output),
      ]))}
    </section>
  `;
}

function renderLangSmith(data) {
  const langsmith = data.env.find((item) => item.name === "Local LangSmith env");
  const sdkStatus = data.packages.find((p) => p.module === "langsmith")?.status || "unknown";
  view.innerHTML = `
    <div class="grid cols-3">
      ${card({ label: "Trace status", value: langsmith?.status || "unknown", tone: langsmith?.status === "key_present_ignored" ? "ok" : "warn" })}
      ${card({ label: "SDK", value: sdkStatus, tone: sdkStatus === "installed" ? "ok" : "warn" })}
      ${card({ label: "Mode", value: "observability only", note: "Not a model provider", tone: "ok" })}
    </div>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Trace Rules</h2>
      <div class="list">
        <div class="row"><span class="row-title">Allowed</span><div class="row-meta">Sanitized run metadata, node names, public-safe source packet IDs, approval status, trace links.</div></div>
        <div class="row"><span class="row-title">Blocked</span><div class="row-meta">Raw private dialogue, real secrets, private workspace links, local-only paths, unapproved source text.</div></div>
        <div class="row"><span class="row-title">Next check</span><div class="row-meta">Install LangGraph, LlamaIndex, and CrewAI in the ignored local runtime, then run one full sanitized workflow trace.</div></div>
      </div>
    </section>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Official References</h2>
      <div class="chips">${data.sources.map((s) => `<a class="badge" href="${escapeHtml(s.url)}">${escapeHtml(s.label)}</a>`).join("")}</div>
    </section>
  `;
}

function renderEnv(data) {
  view.innerHTML = `
    <div class="grid cols-2">
      <section class="panel">
        <h2 class="section-title">Env And Config Status</h2>
        ${table(["Name", "Path", "Status"], data.env.map((item) => [
          escapeHtml(item.name),
          `<span class="code">${escapeHtml(item.path)}</span>`,
          badge(item.status),
        ]))}
      </section>
      <section class="panel">
        <h2 class="section-title">Runtime Package Status</h2>
        ${table(["Package", "Module", "Status"], data.packages.map((item) => [
          escapeHtml(item.label),
          `<span class="code">${escapeHtml(item.module)}</span>`,
          badge(item.status),
        ]))}
      </section>
    </div>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Operating Rule</h2>
      <div class="callout">Use Codex direct prompting first, then CLI proof scripts, then this local dashboard. A full control panel should wait until one full proof workflow has real run data and LangSmith traces.</div>
    </section>
  `;
}

function render() {
  renderNav();
  const data = dashboardData;
  generatedAt.textContent = `Generated ${new Date(data.generated_at).toLocaleString()}`;
  if (activeTab === "overview") renderOverview(data);
  if (activeTab === "wikillm") renderWiki(data);
  if (activeTab === "graphify") renderGraphify(data);
  if (activeTab === "langgraph") renderLangGraph(data);
  if (activeTab === "llamaindex") renderLlamaIndex(data);
  if (activeTab === "crewai") renderCrew(data);
  if (activeTab === "langsmith") renderLangSmith(data);
  if (activeTab === "env") renderEnv(data);
}

fetch("./data.json")
  .then((response) => {
    if (!response.ok) throw new Error(`Unable to load data.json: ${response.status}`);
    return response.json();
  })
  .then((data) => {
    dashboardData = data;
    render();
  })
  .catch((error) => {
    view.innerHTML = `<section class="panel"><h2 class="section-title">Dashboard data error</h2><p>${escapeHtml(error.message)}</p></section>`;
  });
