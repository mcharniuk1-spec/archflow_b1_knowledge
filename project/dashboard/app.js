const tabs = [
  { id: "jarvis", label: "Jarvis", glyph: "JV" },
  { id: "overview", label: "Overview", glyph: "OV" },
  { id: "wikillm", label: "WikiLLM Memory", glyph: "WK" },
  { id: "graphify", label: "Graphify", glyph: "GF" },
  { id: "langgraph", label: "LangGraph Runs", glyph: "LG" },
  { id: "llamaindex", label: "LlamaIndex Query", glyph: "LI" },
  { id: "crewai", label: "CrewAI Outputs", glyph: "CR" },
  { id: "langsmith", label: "LangSmith", glyph: "LS" },
  { id: "env", label: "Env Config", glyph: "EN" },
  { id: "gates", label: "Gates", glyph: "GT" },
];

const storageKeys = {
  mode: "archflow.jarvis.mode",
  voiceAuthorized: "archflow.jarvis.voiceAuthorized",
  packets: "archflow.jarvis.localPackets",
  events: "archflow.jarvis.events",
};

let dashboardData = null;
let activeTab = "jarvis";
let jarvisMode = localStorage.getItem(storageKeys.mode) || "normal";
let voiceAuthorized = localStorage.getItem(storageKeys.voiceAuthorized) === "true";
let dataSignature = "";
let refreshTimer = null;
let localPackets = loadJson(storageKeys.packets, []);
let liveEvents = loadJson(storageKeys.events, [
  {
    id: "boot",
    time: new Date().toISOString(),
    title: "Dashboard opened",
    detail: "Static Vercel-ready shell. Live API and Railway writeback are staged.",
    tone: "ok",
  },
]);

const view = document.querySelector("#view");
const nav = document.querySelector("#nav");
const generatedAt = document.querySelector("#generatedAt");
const liveStatus = document.querySelector("#liveStatus");
const refreshDataButton = document.querySelector("#refreshData");
const globalComposer = document.querySelector("#globalComposer");
const globalInput = document.querySelector("#globalInput");

function storageForKey(key) {
  return key === storageKeys.packets || key === storageKeys.events ? sessionStorage : localStorage;
}

function loadJson(key, fallback) {
  try {
    return JSON.parse(storageForKey(key).getItem(key) || "null") || fallback;
  } catch {
    return fallback;
  }
}

function saveJson(key, value) {
  storageForKey(key).setItem(key, JSON.stringify(value));
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function nowIso() {
  return new Date().toISOString();
}

function makeId(prefix) {
  const stamp = new Date().toISOString().replace(/[-:.TZ]/g, "").slice(0, 14);
  const suffix = Math.random().toString(36).slice(2, 7);
  return `${prefix}-${stamp}-${suffix}`;
}

function setLiveStatus(text, tone = "ok") {
  liveStatus.textContent = text;
  liveStatus.className = `pill live-pill ${tone}`;
}

function appendEvent(title, detail, tone = "ok") {
  liveEvents = [
    {
      id: makeId("event"),
      time: nowIso(),
      title,
      detail,
      tone,
    },
    ...liveEvents,
  ].slice(0, 30);
  saveJson(storageKeys.events, liveEvents);
}

function addPacket(packet) {
  localPackets = [packet, ...localPackets].slice(0, 20);
  saveJson(storageKeys.packets, localPackets);
}

function dashboardSignature(data) {
  return JSON.stringify({
    generated_at: data.generated_at,
    status_cards: data.status_cards,
    gates: data.gates,
    activity: (data.activity || []).slice(0, 10).map((item) => [item.path, item.modified, item.title]),
  });
}

async function loadDashboardData(reason = "initial load", silent = false) {
  const response = await fetch(`./data.json?ts=${Date.now()}`, { cache: "no-store" });
  if (!response.ok) throw new Error(`Unable to load data.json: ${response.status}`);
  const data = await response.json();
  const nextSignature = dashboardSignature(data);
  const changed = nextSignature !== dataSignature;
  dashboardData = data;
  dataSignature = nextSignature;
  if (!silent || changed) {
    appendEvent(
      changed ? "Dashboard data refreshed" : "Dashboard data checked",
      changed ? `Source snapshot changed after ${reason}.` : `No source snapshot change after ${reason}.`,
      changed ? "ok" : "warn",
    );
  }
  setLiveStatus(changed ? "Live data updated" : "Live polling active", changed ? "ok" : "warn");
  render();
}

function startLiveRefresh() {
  if (refreshTimer) window.clearInterval(refreshTimer);
  refreshTimer = window.setInterval(() => {
    loadDashboardData("scheduled live poll", true).catch(() => {
      setLiveStatus("Static data only", "warn");
    });
  }, 15000);
}

function badge(status) {
  const text = String(status || "unknown");
  const lower = text.toLowerCase();
  const tone = lower.includes("active") || lower.includes("present") || lower.includes("ok") || lower.includes("tracked") || lower.includes("static") || lower.includes("files") || lower.includes("submitted") || lower.includes("installed") || lower.includes("passed") || lower.includes("available") || lower.includes("approved")
    ? "ok"
    : lower.includes("missing") || lower.includes("not_installed") || lower.includes("not_generated") || lower.includes("awaiting") || lower.includes("configured_not_installed") || lower.includes("deferred")
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

function systemCards(data) {
  const e13 = data.gates?.e1_3;
  return [
    { label: "Access", value: "hidden link", note: "Google auth planned after Vercel v1", tone: "warn" },
    { label: "Refresh", value: "live polling", note: "Manual, focus, command, and 15s checks", tone: "ok" },
    { label: "Jarvis", value: jarvisMode, note: "Normal or interview command mode", tone: "ok" },
    { label: "Voice", value: voiceAuthorized ? "authorized" : "requires approval", note: "Browser speech API, no raw audio storage", tone: voiceAuthorized ? "ok" : "warn" },
    { label: "E1.3", value: e13?.derived_status || "unknown", note: e13 ? `${e13.passed_count}/${e13.assertion_count} readback` : "No gate data", tone: e13?.readback_status === "passed" ? "ok" : "warn" },
    { label: "Railway", value: "deferred", note: "Use for backend, SSE, auth, workers, durable writes", tone: "warn" },
  ];
}

function createLocalPacket(kind, source, input, extra = {}) {
  const id = makeId(kind);
  const packet = {
    id,
    kind,
    mode: jarvisMode,
    status: "session_packet_created",
    created_at: nowIso(),
    source,
    input_excerpt: String(input || "").slice(0, 900),
    target_file: `project/runs/inbox/${id}.md`,
    kb_update: "requires Codex or future Railway writeback approval",
    evidence_label: kind.includes("research") ? "HYPOTHESIS" : "INTERPRETATION",
    one_icp_lane: "B2B SaaS product leaders for Product Discovery-to-Production PRD Pack",
    write_gate: "No GitHub, Notion, WikiLLM, or file write occurs from static browser JavaScript. Browser packets are session-only until downloaded by the user.",
    ...extra,
  };
  addPacket(packet);
  appendEvent("Jarvis packet created", `${packet.kind} packet staged for ${packet.target_file}.`, "ok");
  return packet;
}

function markdownPacket(packet) {
  return `# Jarvis Packet: ${packet.kind}

Created: ${packet.created_at}
Status: ${packet.status}
Mode: ${packet.mode}
Evidence label: ${packet.evidence_label}
Target file: ${packet.target_file}

## Source

${packet.source}

## Input Excerpt

${packet.input_excerpt}

## Current ICP Lane

${packet.one_icp_lane}

## Write Gate

${packet.write_gate}

## KB Update

${packet.kb_update}

## Extra

${JSON.stringify(packet.extra || {}, null, 2)}
`;
}

function downloadPacket(packetId) {
  const packet = localPackets.find((item) => item.id === packetId);
  if (!packet) return;
  const blob = new Blob([markdownPacket(packet)], { type: "text/markdown" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = `${packet.id}.md`;
  anchor.click();
  URL.revokeObjectURL(url);
}

function jarvisReply(input, source = "typed command") {
  const text = String(input || "").trim();
  const lower = text.toLowerCase();

  if (!text) {
    return "Jarvis is ready. Ask for status, refresh, research/check, content template, or interview mode.";
  }

  if (lower.includes("refresh") || lower.includes("reload") || lower.includes("update dashboard")) {
    loadDashboardData("Jarvis refresh command").catch((error) => {
      appendEvent("Refresh failed", error.message, "block");
      render();
    });
    return "I am refreshing the dashboard data in place. The page will not reload.";
  }

  if (lower.includes("interview")) {
    jarvisMode = "interview";
    localStorage.setItem(storageKeys.mode, jarvisMode);
    appendEvent("Jarvis mode changed", "Interview mode asks one question at a time and produces candidates for review.", "ok");
    return "Interview mode is active. First question: what source material should become the next PRD or ICP evidence packet?";
  }

  if (lower.includes("normal mode") || lower.includes("status mode")) {
    jarvisMode = "normal";
    localStorage.setItem(storageKeys.mode, jarvisMode);
    appendEvent("Jarvis mode changed", "Normal mode answers status and waits for instructions.", "ok");
    return "Normal mode is active. I will answer, prepare tasks, and ask before durable writes.";
  }

  if (lower.includes("research") || lower.includes("check") || lower.includes("file") || lower.includes("analyze")) {
    const packet = createLocalPacket("research-check", source, text, {
      extra: {
        recommended_agent: "AF Research + AF Review",
        next_step: "Use Codex or Railway writeback to save the packet and update WikiLLM after review.",
      },
    });
    return `I created a local research/check packet: ${packet.id}. It is staged for ${packet.target_file}; static Vercel cannot write it to the repo without Codex or Railway authority.`;
  }

  if (lower.includes("content") || lower.includes("carousel") || lower.includes("post")) {
    const packet = createLocalPacket("content-template-request", source, text, {
      extra: {
        recommended_agent: "AF Copy + GloomyLord + AF Review",
        proof_required: "approved artifact, evidence label, no demand claim, AF Review, owner approval",
      },
    });
    return `I staged a content-template packet: ${packet.id}. It should become implementation-focused content only after the proof and review gates pass.`;
  }

  if (lower.includes("status") || lower.includes("what works") || lower.includes("done")) {
    const e13 = dashboardData?.gates?.e1_3;
    return `Current status: E1.3 is ${e13?.derived_status || "unknown"} with ${e13?.passed_count || 0}/${e13?.assertion_count || 0} readback checks. Dashboard is static/read-only with live polling. Hidden-link Vercel comes first; Railway, Google auth, durable voice/file writes, and model-provider calls are later gates.`;
  }

  if (jarvisMode === "interview") {
    const packet = createLocalPacket("interview-memory-candidate", source, text, {
      extra: {
        question_next: "Which decision, task, or proof should this update?",
        memory_policy: "summary candidates only; raw transcript storage is off by default",
      },
    });
    return `Captured as an interview memory candidate: ${packet.id}. Next question: should this become a task, a decision, an ICP evidence card, or a content angle?`;
  }

  return "I can answer from the dashboard state, refresh data, stage a research/check packet, or switch to interview mode. Durable writes still go through Codex or a later Railway backend.";
}

function handleGlobalSubmit(value, source = "typed command") {
  const input = String(value || "").trim();
  if (!input) return;
  const reply = jarvisReply(input, source);
  appendEvent("Jarvis command", `${input.slice(0, 120)} -> ${reply.slice(0, 160)}`, "ok");
  if (activeTab !== "jarvis") activeTab = "jarvis";
  render();
}

function renderJarvis(data) {
  const latestPacket = localPackets[0];
  view.innerHTML = `
    <div class="jarvis-layout">
      <section class="panel jarvis-main">
        <div class="mode-bar" aria-label="Jarvis mode">
          <button class="${jarvisMode === "normal" ? "active" : ""}" data-mode="normal" type="button">Normal</button>
          <button class="${jarvisMode === "interview" ? "active" : ""}" data-mode="interview" type="button">Interview</button>
        </div>
        <div class="jarvis-orb" aria-hidden="true">JV</div>
        <h2>Jarvis Command Center</h2>
        <p class="muted">Ask for status, refresh, checks, content packets, or interview mode. Voice and file checks stay local until backend writeback exists.</p>
        <div class="jarvis-actions">
          <button class="primary" id="jarvisRefresh" type="button">Refresh data</button>
          <button class="button" id="voiceToggle" type="button">${voiceAuthorized ? "Start voice" : "Authorize voice"}</button>
          <label class="button file-button">
            Attach file
            <input id="fileInput" type="file" multiple />
          </label>
        </div>
        <div id="voiceState" class="callout compact">${voiceAuthorized ? "Voice is authorized in this browser. Raw audio is not stored." : "Voice requires explicit browser-level authorization before use."}</div>
      </section>

      <aside class="panel">
        <h2 class="section-title">Execution Contract</h2>
        <div class="list">
          <div class="row"><span class="row-title">Dashboard</span><div class="row-meta">Hidden-link Vercel static view first. Google auth and server-side access come next.</div></div>
          <div class="row"><span class="row-title">Jarvis actions</span><div class="row-meta">Research/check packets can be created locally; durable writes require Codex or Railway authority.</div></div>
          <div class="row"><span class="row-title">Voice</span><div class="row-meta">Authorized browser transcript only. No raw audio or raw transcript storage by default.</div></div>
          <div class="row"><span class="row-title">ICP</span><div class="row-meta">One lane: B2B SaaS product leaders and PRD workflow quality.</div></div>
        </div>
      </aside>
    </div>

    <div class="grid cols-6" style="margin-top:16px">${systemCards(data).map((item) => card(item)).join("")}</div>

    <div class="split" style="margin-top:16px">
      <section class="panel">
        <h2 class="section-title">Live Stream</h2>
        <div class="list">
          ${liveEvents.slice(0, 8).map((event) => `
            <article class="row event-row">
              ${badge(event.tone)}
              <span class="row-title">${escapeHtml(event.title)}</span>
              <div class="row-meta">${new Date(event.time).toLocaleString()}</div>
              <p>${escapeHtml(event.detail)}</p>
            </article>
          `).join("")}
        </div>
      </section>
      <section class="panel">
        <h2 class="section-title">Local Packets</h2>
        ${latestPacket ? `
          <div class="list">
            ${localPackets.slice(0, 5).map((packet) => `
              <article class="row">
                <span class="row-title">${escapeHtml(packet.kind)} - ${escapeHtml(packet.id)}</span>
                <div class="row-meta">${escapeHtml(packet.status)} - ${escapeHtml(packet.target_file)}</div>
                <p>${escapeHtml(packet.input_excerpt || "No excerpt").slice(0, 220)}</p>
                <div class="row-actions">
                  <button class="button packet-download" type="button" data-packet="${escapeHtml(packet.id)}">Download packet</button>
                </div>
              </article>
            `).join("")}
          </div>
        ` : `<div class="callout">No local packets yet. Ask Jarvis to run a research/check or content task.</div>`}
      </section>
    </div>
  `;

  view.querySelectorAll("[data-mode]").forEach((button) => {
    button.addEventListener("click", () => {
      jarvisMode = button.dataset.mode;
      localStorage.setItem(storageKeys.mode, jarvisMode);
      appendEvent("Jarvis mode changed", `${jarvisMode} mode selected.`, "ok");
      render();
    });
  });

  document.querySelector("#jarvisRefresh")?.addEventListener("click", () => {
    loadDashboardData("manual Jarvis button").catch((error) => {
      appendEvent("Refresh failed", error.message, "block");
      render();
    });
  });

  document.querySelector("#voiceToggle")?.addEventListener("click", startVoice);
  document.querySelector("#fileInput")?.addEventListener("change", handleFiles);
  view.querySelectorAll(".packet-download").forEach((button) => {
    button.addEventListener("click", () => downloadPacket(button.dataset.packet));
  });
}

function startVoice() {
  const state = document.querySelector("#voiceState");
  if (!voiceAuthorized) {
    voiceAuthorized = true;
    localStorage.setItem(storageKeys.voiceAuthorized, "true");
    appendEvent("Voice authorized", "Browser-level voice command permission enabled. Start voice again to listen.", "ok");
    render();
    return;
  }

  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    state.textContent = "Speech recognition is not available in this browser. Use the bottom input field.";
    appendEvent("Voice unavailable", "Browser speech recognition API is not available.", "warn");
    return;
  }

  const recognition = new SpeechRecognition();
  recognition.lang = "en-US";
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;
  state.textContent = "Listening. Speak one command or one interview answer.";
  recognition.onresult = (event) => {
    const transcript = event.results?.[0]?.[0]?.transcript || "";
    state.textContent = `Heard: ${transcript}`;
    handleGlobalSubmit(transcript, "authorized browser voice transcript");
  };
  recognition.onerror = (event) => {
    state.textContent = `Voice error: ${event.error || "unknown"}`;
    appendEvent("Voice error", event.error || "unknown", "warn");
  };
  recognition.onend = () => {
    if (state.textContent === "Listening. Speak one command or one interview answer.") {
      state.textContent = "Voice stopped without a transcript.";
    }
  };
  recognition.start();
}

function handleFiles(event) {
  const files = Array.from(event.target.files || []);
  files.forEach((file) => {
    const packet = createLocalPacket(
      "file-metadata-check",
      "local browser file metadata",
      "File selected for future review. The static dashboard captured metadata only and did not read or store document text.",
      {
        extra: {
          file_name: file.name,
          file_type: file.type || "unknown",
          file_size: file.size,
          privacy: "metadata only; use Codex or a future approved backend to process document contents",
        },
      },
    );
    appendEvent("File metadata prepared", `${file.name} staged as ${packet.id}.`, "ok");
  });
  render();
  event.target.value = "";
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
          E1.3 readback status: ${escapeHtml(data.gates.e1_3.derived_status.replaceAll("_", " "))}. The dashboard derives this from run and wiki artifacts; it does not store decisions or become memory.
        </div>
      </section>
      <section class="panel">
        <h2 class="section-title">Phase Decision</h2>
        <div class="list">
          <div class="row"><span class="row-title">Phase 1</span><div class="row-meta">Codex, GitHub, LangSmith, Obsidian, and WikiLLM files remain the primary operating surfaces.</div></div>
          <div class="row"><span class="row-title">Phase 2</span><div class="row-meta">This dashboard is now the Jarvis-facing command shell with static data refresh and local packets.</div></div>
          <div class="row"><span class="row-title">Phase 3</span><div class="row-meta">Railway/API/SSE, Google auth, durable writes, and provider models after access and storage gates.</div></div>
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
      ${card({ label: "Recommended next", value: "After code changes", note: data.graphify.recommended_next, tone: hasGraph ? "ok" : "warn" })}
    </div>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Graphify Links</h2>
      ${hasGraph
        ? `<div class="list">${data.graphify.paths.map((p) => `<div class="row">${pathLink(p)}</div>`).join("")}</div>`
        : `<div class="callout">No Graphify output is present in this public project yet. Generate it after runtime code exists so the graph reflects the real implementation.</div>`
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
            <div class="row-meta">${pathLink(doc.path)} - score ${doc.score}</div>
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
        <div class="row"><span class="row-title">Next check</span><div class="row-meta">Use the existing local runtime for sanitized traces only. Hosted provider calls stay gated.</div></div>
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
      <div class="callout">Use Codex direct prompting first, then CLI proof scripts, then this dashboard. Live write actions wait for Railway/auth/writeback gates.</div>
    </section>
  `;
}

function renderGates(data) {
  const gate = data.gates.e1_3;
  view.innerHTML = `
    <div class="grid cols-3">
      ${card({ label: "E1.3 derived status", value: gate.derived_status, note: "Read-only status from artifacts", tone: gate.derived_status === "readback_passed" ? "ok" : "warn" })}
      ${card({ label: "Readback", value: `${gate.passed_count}/${gate.assertion_count}`, note: gate.readback_status, tone: gate.readback_status === "passed" ? "ok" : "warn" })}
      ${card({ label: "Source", value: gate.source, note: "Authority remains in project files", tone: "ok" })}
    </div>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Required Evidence</h2>
      ${table(["Path", "Status"], gate.required_evidence.map((item) => [
        pathLink(item.path),
        badge(item.status),
      ]))}
    </section>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Readback Assertions</h2>
      <div class="chips">${gate.readback_assertions.map((item) => `<span class="badge ok">${escapeHtml(item)}</span>`).join("")}</div>
      <div class="callout" style="margin-top:14px">This gate is display-only. Update source files and rerun the dashboard generator or use the future Railway live bridge to change status.</div>
    </section>
  `;
}

function render() {
  if (!dashboardData) return;
  renderNav();
  const data = dashboardData;
  generatedAt.textContent = `Generated ${new Date(data.generated_at).toLocaleString()}`;
  if (activeTab === "jarvis") renderJarvis(data);
  if (activeTab === "overview") renderOverview(data);
  if (activeTab === "wikillm") renderWiki(data);
  if (activeTab === "graphify") renderGraphify(data);
  if (activeTab === "langgraph") renderLangGraph(data);
  if (activeTab === "llamaindex") renderLlamaIndex(data);
  if (activeTab === "crewai") renderCrew(data);
  if (activeTab === "langsmith") renderLangSmith(data);
  if (activeTab === "env") renderEnv(data);
  if (activeTab === "gates") renderGates(data);
}

refreshDataButton.addEventListener("click", () => {
  loadDashboardData("manual refresh button").catch((error) => {
    appendEvent("Refresh failed", error.message, "block");
    render();
  });
});

globalComposer.addEventListener("submit", (event) => {
  event.preventDefault();
  handleGlobalSubmit(globalInput.value, "bottom command input");
  globalInput.value = "";
});

window.addEventListener("focus", () => {
  loadDashboardData("window focus").catch(() => {
    setLiveStatus("Static data only", "warn");
  });
});

document.addEventListener("visibilitychange", () => {
  if (!document.hidden) {
    loadDashboardData("tab visible").catch(() => {
      setLiveStatus("Static data only", "warn");
    });
  }
});

loadDashboardData("initial load")
  .then(startLiveRefresh)
  .catch((error) => {
    setLiveStatus("Data error", "block");
    view.innerHTML = `<section class="panel"><h2 class="section-title">Dashboard data error</h2><p>${escapeHtml(error.message)}</p></section>`;
  });
