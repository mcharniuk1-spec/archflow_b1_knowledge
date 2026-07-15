(function () {
  "use strict";

  const SHARED_SESSION_KEY = "archflow.sharedSession";
  const VIEWER_MODE_KEY = "archflow.jarvis.viewerMode";
  const fallbackModels = [
    { id: "openai/gpt-5.6-luna", name: "GPT-5.6 Luna", provider: "OpenAI", tier: "frontier", context_length: 1050000, allowed: true },
    { id: "anthropic/claude-sonnet-5", name: "Claude Sonnet 5", provider: "Anthropic", tier: "frontier", context_length: 1000000, allowed: true },
    { id: "qwen/qwen3.7-plus", name: "Qwen3.7 Plus", provider: "Qwen", tier: "economy", context_length: 1000000, allowed: true },
    { id: "deepseek/deepseek-v4-flash", name: "DeepSeek V4 Flash", provider: "DeepSeek", tier: "economy", context_length: 1048576, allowed: true }
  ];

  function loadJson(key, fallback) {
    try {
      return JSON.parse(localStorage.getItem(key) || "null") || fallback;
    } catch (_error) {
      return fallback;
    }
  }

  const defaultSharedSession = {
    knowledge: { status: "not_started", report_id: null, updated_at: null },
    agent_control: { status: "locked_pending_knowledge", report_id: null, updated_at: null },
    last_report: null
  };

  const state = {
    curated: fallbackModels,
    catalog: fallbackModels,
    allowed: new Set(fallbackModels.map((model) => model.id)),
    selectedId: fallbackModels[0].id,
    selectedName: fallbackModels[0].name,
    messages: [],
    apiOnline: false,
    viewerMode: localStorage.getItem(VIEWER_MODE_KEY) === "guest" ? "guest" : "admin",
    shared: loadJson(SHARED_SESSION_KEY, defaultSharedSession)
  };

  const nodes = {
    form: document.querySelector("[data-chat-form]"),
    conversation: document.querySelector("[data-conversation]"),
    ownerToken: document.querySelector("[data-owner-token]"),
    apiBase: document.querySelector("[data-api-base]"),
    viewerMode: document.querySelector("[data-viewer-mode]"),
    modelCards: document.querySelector("[data-model-cards]"),
    modelSearch: document.querySelector("[data-model-search]"),
    catalogStatus: document.querySelector("[data-catalog-status]"),
    catalogResults: document.querySelector("[data-catalog-results]"),
    selectedModel: document.querySelector("[data-selected-model]"),
    composerStatus: document.querySelector("[data-composer-status]"),
    send: document.querySelector("[data-send]"),
    statusDot: document.querySelector("[data-status-dot]"),
    runtimeLabel: document.querySelector("[data-runtime-label]")
  };

  const configuredApi = new URLSearchParams(window.location.search).get("api");
  if (configuredApi && /^http:\/\/(127\.0\.0\.1|localhost):\d+$/.test(configuredApi) && nodes.apiBase) {
    nodes.apiBase.value = configuredApi;
  }

  function nowIso() {
    return new Date().toISOString();
  }

  function packetId(prefix) {
    const random = globalThis.crypto?.randomUUID?.() || Math.random().toString(16).slice(2);
    return `${prefix}-${new Date().toISOString().slice(0, 10)}-${random.slice(0, 8)}`;
  }

  function saveShared() {
    localStorage.setItem(SHARED_SESSION_KEY, JSON.stringify(state.shared));
  }

  function trustedApiBase() {
    const raw = (nodes.apiBase?.value || "").trim();
    if (!raw) return window.location.origin;
    let parsed;
    try {
      parsed = new URL(raw, window.location.origin);
    } catch (_error) {
      throw new Error("API base is not a valid URL");
    }
    const sameOrigin = parsed.origin === window.location.origin;
    const loopback = parsed.protocol === "http:" && ["127.0.0.1", "localhost"].includes(parsed.hostname);
    if (!sameOrigin && !loopback) throw new Error("API base must be this origin or an HTTP loopback address");
    return parsed.origin;
  }

  function apiUrl(path) {
    return `${trustedApiBase()}${path}`;
  }

  function formatContext(value) {
    const number = Number(value);
    if (!Number.isFinite(number)) return "Context not listed";
    return number >= 1000000 ? `${(number / 1000000).toFixed(number % 1000000 ? 1 : 0)}M context` : `${Math.round(number / 1000)}K context`;
  }

  function modelDisplay(model) {
    return model.name || model.label || model.id;
  }

  function setRuntime(name, value) {
    const node = document.querySelector(`[data-runtime="${name}"]`);
    if (node) node.textContent = value;
  }

  function updateApiState(online, label) {
    state.apiOnline = online;
    nodes.statusDot?.classList.toggle("is-ready", online);
    nodes.statusDot?.classList.toggle("is-offline", !online);
    if (nodes.runtimeLabel) nodes.runtimeLabel.textContent = label;
    setRuntime("api", online ? "Reachable" : "Offline / static");
  }

  function renderActivityState() {
    const knowledge = state.shared.knowledge || {};
    const control = state.shared.agent_control || {};
    const label = control.status === "prepared_local"
      ? `Agent handoff ${control.report_id || "prepared"}`
      : knowledge.report_id
        ? `Knowledge report ${knowledge.report_id}`
        : "No report prepared";
    setRuntime("activity", label);
  }

  function setViewerMode(mode) {
    state.viewerMode = mode === "guest" ? "guest" : "admin";
    localStorage.setItem(VIEWER_MODE_KEY, state.viewerMode);
    document.body.dataset.viewerMode = state.viewerMode;
    if (nodes.viewerMode) nodes.viewerMode.value = state.viewerMode;
    document.querySelectorAll("[data-admin-only]").forEach((element) => {
      element.hidden = state.viewerMode === "guest";
    });
    if (nodes.send) nodes.send.querySelector("span").textContent = state.viewerMode === "guest" ? "Prepare local report" : "Prepare report / optional guarded review";
    if (state.viewerMode === "guest") {
      setRuntime("auth", "Hidden in guest preview");
      setRuntime("provider", "Not requested");
      updateApiState(false, "Guest local preview");
    } else {
      checkRuntime();
    }
    renderActivityState();
  }

  function setSelected(model) {
    if (!model || !state.allowed.has(model.id)) return;
    state.selectedId = model.id;
    state.selectedName = modelDisplay(model);
    if (nodes.selectedModel) nodes.selectedModel.textContent = state.selectedName;
    renderCurated();
    renderCatalog(nodes.modelSearch?.value || "");
  }

  function renderCurated() {
    if (!nodes.modelCards) return;
    nodes.modelCards.replaceChildren(...state.curated.map((model) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "model-card";
      button.setAttribute("aria-pressed", String(model.id === state.selectedId));
      button.disabled = !state.allowed.has(model.id);
      const provider = document.createElement("small");
      provider.textContent = `${model.provider || model.id.split("/")[0]} · ${model.tier || "route"}`;
      const title = document.createElement("strong");
      title.textContent = modelDisplay(model);
      const detail = document.createElement("span");
      detail.textContent = `${formatContext(model.context_length)} · ${state.allowed.has(model.id) ? "allowed route candidate" : "server allowlist required"}`;
      button.append(provider, title, detail);
      button.addEventListener("click", () => setSelected(model));
      return button;
    }));
  }

  function renderCatalog(query) {
    if (!nodes.catalogResults) return;
    const normalized = String(query || "").trim().toLowerCase();
    if (!normalized) {
      nodes.catalogResults.replaceChildren();
      return;
    }
    const results = state.catalog
      .filter((model) => `${model.id} ${modelDisplay(model)} ${model.description || ""}`.toLowerCase().includes(normalized))
      .slice(0, 24);
    nodes.catalogResults.replaceChildren(...results.map((model) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "catalog-result";
      button.disabled = !state.allowed.has(model.id);
      const title = document.createElement("strong");
      title.textContent = modelDisplay(model);
      const stateLabel = document.createElement("em");
      stateLabel.textContent = state.allowed.has(model.id) ? "Route candidate" : "Search only";
      const detail = document.createElement("span");
      detail.textContent = `${model.id} · ${formatContext(model.context_length)}`;
      button.append(title, stateLabel, detail);
      button.addEventListener("click", () => setSelected(model));
      return button;
    }));
    if (nodes.catalogStatus) nodes.catalogStatus.textContent = results.length
      ? `${results.length} loaded catalog result(s). Search does not authorize execution.`
      : "No matching route in the loaded catalog.";
  }

  async function fetchJson(url, options = {}, timeoutMs = 8000) {
    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), timeoutMs);
    try {
      const response = await fetch(url, { cache: "no-store", ...options, signal: controller.signal });
      const type = response.headers.get("content-type") || "";
      if (!response.ok || !type.includes("application/json")) throw new Error(`HTTP ${response.status}`);
      return await response.json();
    } finally {
      window.clearTimeout(timeout);
    }
  }

  async function checkRuntime() {
    if (state.viewerMode === "guest") return;
    updateApiState(false, "Checking API");
    try {
      const health = await fetchJson(apiUrl("/api/health"), {}, 5000);
      const payload = health.payload || {};
      updateApiState(true, payload.provider_enabled ? "API ready / provider gated" : "API ready / provider off");
      setRuntime("provider", payload.provider_enabled && payload.provider_key_configured ? "Configured + gated" : "Execution disabled");
      setRuntime("auth", payload.owner_auth_configured ? "Server token set" : "Not configured");
      if (Array.isArray(payload.allowed_models)) state.allowed = new Set(payload.allowed_models);
      renderCurated();
    } catch (_error) {
      updateApiState(false, "Static UI / API unavailable");
      setRuntime("provider", "Not verified");
      setRuntime("auth", "Not verified");
    }
  }

  async function loadModels() {
    if (state.viewerMode === "guest") return;
    if (nodes.catalogStatus) nodes.catalogStatus.textContent = "Loading public catalog on explicit request…";
    let catalogUrl = "https://openrouter.ai/api/v1/models";
    try {
      const response = await fetchJson(apiUrl("/api/models"), {}, 5000);
      const payload = response.payload || {};
      if (Array.isArray(payload.allowed_model_ids)) state.allowed = new Set(payload.allowed_model_ids);
      if (Array.isArray(payload.curated) && payload.curated.length) state.curated = payload.curated.map((model) => ({ ...model, name: model.label || model.id }));
      if (payload.live_catalog_url) catalogUrl = payload.live_catalog_url;
    } catch (_error) {
      // Keep only public-safe curated routes if the guarded endpoint is absent.
    }
    renderCurated();
    try {
      const live = await fetchJson(catalogUrl, {}, 10000);
      if (Array.isArray(live.data) && live.data.length) {
        state.catalog = live.data;
        if (nodes.catalogStatus) nodes.catalogStatus.textContent = `${live.data.length} public routes loaded. Discovery does not enable a route.`;
      }
    } catch (_error) {
      state.catalog = state.curated;
      if (nodes.catalogStatus) nodes.catalogStatus.textContent = "Catalog unavailable; curated route candidates remain visible.";
    }
  }

  function appendMessage(role, text, metadata, blocked = false) {
    if (!nodes.conversation) return;
    const article = document.createElement("article");
    article.className = `message message-${role}${blocked ? " is-blocked" : ""}`;
    const meta = document.createElement("div");
    meta.className = "message-meta";
    const source = document.createElement("span");
    source.textContent = role === "user" ? "Operator" : "Jarvis";
    const detail = document.createElement("time");
    detail.textContent = metadata;
    const body = document.createElement("p");
    body.textContent = text;
    meta.append(source, detail);
    article.append(meta, body);
    nodes.conversation.append(article);
    nodes.conversation.scrollTop = nodes.conversation.scrollHeight;
  }

  function reportMarkdown(report) {
    const lines = [
      "# ArchFlow Local Architecture Report",
      "",
      `- Report ID: ${report.activity_id}`,
      `- Stage: ${report.stage}`,
      `- Status: ${report.status}`,
      `- Viewer mode: ${report.mode}`,
      `- Created: ${report.created_at}`,
      "",
      "## Goal",
      report.goal,
      "",
      "## Repository / project reference",
      report.repository.reference || "Not supplied",
      "",
      "## Source boundary",
      report.knowledge_service.source_boundary,
      "",
      "## Requested output and review",
      `- Output: ${report.knowledge_service.requested_output}`,
      `- Reviewer: ${report.knowledge_service.reviewer}`,
      `- Constraints: ${report.knowledge_service.constraints}`,
      "",
      "## Classification",
      `- FACT: ${(report.knowledge_service.facts || []).join(" ")}`,
      `- INTERPRETATION: ${(report.knowledge_service.interpretations || []).join(" ")}`,
      `- HYPOTHESIS: ${(report.knowledge_service.hypotheses || []).join(" ")}`,
      `- GAP: ${(report.knowledge_service.gaps || []).join(" ")}`,
      "",
      "## Runtime boundary",
      "This report was prepared locally. It did not fetch or clone a repository, ingest a corpus, launch an agent, call a provider, create files, write a database, push Git, deploy, or write to an external system."
    ];
    if (report.agent_control) {
      lines.push("", "## Agent Control proposal", `- Uses report: ${report.agent_control.source_activity_id}`, `- Roles: ${report.agent_control.roles.join(", ")}`, `- Review gate: ${report.agent_control.review_gate}`, "- Proposed files are suggestions only:");
      report.agent_control.proposed_files.forEach((file) => lines.push(`  - ${file.suggested_path}: ${file.purpose} (created: false; operator review required)`));
    }
    return lines.join("\n");
  }

  function isUnsafeInput(value) {
    return /(?:file:\/\/|\/Users\/|C:\\Users\\|BEGIN (?:RSA |OPENSSH )?PRIVATE KEY|(?:api[_-]?key|token|password|secret)\s*[:=]\s*\S+)/i.test(String(value || ""));
  }

  function formValues() {
    const data = new FormData(nodes.form);
    return {
      goal: String(data.get("request") || "").trim(),
      stage: data.get("architecture") === "control" ? "agent_control" : "knowledge_service",
      projectReference: String(data.get("project_reference") || "").trim(),
      sourceBoundary: String(data.get("source_boundary") || "").trim(),
      requestedOutput: String(data.get("requested_output") || "").trim(),
      reviewer: String(data.get("reviewer") || "").trim(),
      constraints: String(data.get("constraints") || "").trim(),
      providerApproval: data.get("provider_approval") === "on"
    };
  }

  function buildLocalReport(values) {
    const combined = [values.goal, values.projectReference, values.sourceBoundary, values.requestedOutput, values.reviewer, values.constraints].join("\n");
    if (isUnsafeInput(combined)) throw new Error("Remove local paths, credentials, tokens, private keys, or raw private material before preparing a public-safe report.");
    if (!values.goal || !values.sourceBoundary || !values.requestedOutput || !values.reviewer || !values.constraints) throw new Error("Complete goal, source boundary, requested output, reviewer, and stop conditions first.");
    const hasKnowledgeReport = Boolean(state.shared.knowledge?.report_id);
    if (values.stage === "agent_control" && !hasKnowledgeReport) {
      throw new Error("Prepare a Knowledge Service report first. Agent Control needs a report ID and its documented source boundary.");
    }
    const activityId = packetId(values.stage === "knowledge_service" ? "knowledge" : "agent-control");
    const base = {
      schema_version: "1.0",
      kind: "archflow_local_architecture_report",
      created_at: nowIso(),
      activity_id: activityId,
      mode: state.viewerMode,
      stage: values.stage,
      status: "review_required_not_executed",
      goal: values.goal,
      repository: { reference: values.projectReference || "Not supplied", access: "not_fetched_or_cloned" },
      knowledge_service: {
        source_boundary: values.sourceBoundary,
        requested_output: values.requestedOutput,
        reviewer: values.reviewer,
        constraints: values.constraints,
        facts: ["The operator supplied a browser-local request and source boundary."],
        interpretations: ["The requested output needs review before it can become a durable knowledge or implementation action."],
        hypotheses: ["The bounded source set can support the requested output after an approved operator reviews it."],
        gaps: ["No repository or external source was fetched, inspected, indexed, or verified by this static page."],
        review_owner: values.reviewer
      },
      runtime_boundary: {
        state_source: "browser_local",
        provider_calls: 0,
        agent_launches: 0,
        repository_writes: 0,
        database_writes: 0,
        external_writeback: "disabled",
        authentication: "not_implemented"
      }
    };
    if (values.stage === "agent_control") {
      base.agent_control = {
        enabled_after: "reviewed Knowledge Service report",
        source_activity_id: state.shared.knowledge.report_id,
        goal: values.goal,
        roles: ["Goal Architect", "Bounded Worker", "Independent Reviewer", "Integrator"],
        allowed_skills: ["archflow-knowledge-service", "archflow-agent-control", "archflow-task-breakdown", "task-handout"],
        review_gate: values.reviewer,
        stop_conditions: values.constraints,
        proposed_files: [
          { suggested_path: "docs/architecture-report.md", purpose: "Reviewed architecture and source-boundary report", created: false, requires_operator_review: true },
          { suggested_path: "project/agents/agent-roster.yaml", purpose: "Role-contract proposal after independent review", created: false, requires_operator_review: true },
          { suggested_path: "project/runs/<run-id>/agent-handout.md", purpose: "Execution handoff and validation record", created: false, requires_operator_review: true }
        ]
      };
    }
    return base;
  }

  function prepareLocalReport(values, announce = true) {
    const report = buildLocalReport(values);
    if (report.stage === "knowledge_service") {
      state.shared = {
        ...state.shared,
        knowledge: { status: "prepared_local", report_id: report.activity_id, updated_at: report.created_at, source: "Jarvis browser-local report" },
        agent_control: { ...state.shared.agent_control, status: "available_from_knowledge" },
        last_report: report
      };
    } else {
      state.shared = {
        ...state.shared,
        agent_control: { status: "prepared_local", report_id: report.activity_id, updated_at: report.created_at, source: "Jarvis browser-local handoff" },
        last_report: report
      };
    }
    saveShared();
    renderActivityState();
    if (announce) appendMessage("assistant", `${report.stage === "knowledge_service" ? "Knowledge report" : "Agent-control handoff"} prepared locally: ${report.activity_id}. It is review-required and downloadable. ${report.stage === "knowledge_service" ? "Next: review/download it, then select Agent Control." : "Next: download it and ask an approved operator to apply only reviewed changes."}`, "local architecture report", true);
    return report;
  }

  function downloadBlob(filename, type, text) {
    const blob = new Blob([text], { type });
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.download = filename;
    anchor.click();
    URL.revokeObjectURL(url);
  }

  function downloadReport() {
    const report = state.shared.last_report;
    if (!report) {
      if (nodes.composerStatus) nodes.composerStatus.textContent = "Prepare a local report before downloading it.";
      return;
    }
    downloadBlob(`archflow-${report.stage}-${report.activity_id}.md`, "text/markdown", reportMarkdown(report));
    if (nodes.composerStatus) nodes.composerStatus.textContent = "Downloaded a browser-local report. It is not a repository patch or runtime receipt.";
  }

  function downloadPackage() {
    const report = state.shared.last_report;
    if (!report) {
      if (nodes.composerStatus) nodes.composerStatus.textContent = "Prepare a local report before downloading its handoff package.";
      return;
    }
    const bundle = { ...report, markdown_report: reportMarkdown(report), download_boundary: "Local proposal only; no file was created or changed." };
    downloadBlob(`archflow-${report.stage}-${report.activity_id}.json`, "application/json", JSON.stringify(bundle, null, 2));
    if (nodes.composerStatus) nodes.composerStatus.textContent = "Downloaded a local handoff JSON. Review it before any repository action.";
  }

  async function submitGuardedReview(values, report) {
    if (state.viewerMode === "guest" || !values.providerApproval) return;
    const token = nodes.ownerToken?.value || "";
    const headers = { "Content-Type": "application/json" };
    if (token) headers.Authorization = `Bearer ${token}`;
    try {
      const result = await fetchJson(apiUrl("/api/chat"), {
        method: "POST",
        headers,
        body: JSON.stringify({
          request: `Review the guarded contract status for local ${report.stage} report ${report.activity_id}. The browser did not send the report body, project reference, source boundary, or chat history to this API route.`,
          lane: "jarvis_operator",
          architecture: values.stage === "agent_control" ? "control" : "service",
          model_id: state.selectedId,
          provider_approval: true,
          conversation: []
        })
      }, 45000);
      const provider = result.payload?.provider_result || {};
      const executed = provider.provider_executed === true;
      const detail = executed
        ? "A provider receipt returned. Check the server receipt separately; local downloads remain proposals."
        : `Guarded review returned without provider execution. Blocker: ${provider.reason || result.status || "not reported"}.`;
      appendMessage("assistant", detail, executed ? "guarded API receipt" : "guarded API blocked", !executed);
      setRuntime("execution", executed ? "Receipt returned" : "Guarded review blocked");
      if (nodes.composerStatus) nodes.composerStatus.textContent = detail;
    } catch (error) {
      appendMessage("assistant", `The optional guarded API review could not be reached: ${error.message}. The local report remains available; no provider response or writeback is claimed.`, "transport failure", true);
      setRuntime("execution", "Guarded API unavailable");
    }
  }

  async function submitChat(event) {
    event.preventDefault();
    if (!nodes.form || !nodes.send) return;
    let values;
    let report;
    try {
      values = formValues();
      appendMessage("user", values.goal, `${values.stage} · ${state.viewerMode}`);
      state.messages.push({ role: "user", source: "jarvis-page", text: values.goal, time: nowIso() });
      report = prepareLocalReport(values, true);
    } catch (error) {
      appendMessage("assistant", error.message, "input held", true);
      if (nodes.composerStatus) nodes.composerStatus.textContent = `Held locally: ${error.message}`;
      return;
    }
    if (nodes.composerStatus) nodes.composerStatus.textContent = values.providerApproval && state.viewerMode === "admin"
      ? "Local report prepared. Sending an optional guarded API review; provider execution is still separately gated."
      : "Local report prepared. Download it or move to the next reviewed stage; no API or provider call was requested.";
    nodes.send.disabled = true;
    try {
      await submitGuardedReview(values, report);
    } finally {
      nodes.send.disabled = false;
      nodes.form.elements.request.value = "";
      nodes.form.elements.provider_approval.checked = false;
      nodes.form.elements.request.focus();
    }
  }

  nodes.form?.addEventListener("submit", submitChat);
  nodes.modelSearch?.addEventListener("input", (event) => renderCatalog(event.target.value));
  nodes.viewerMode?.addEventListener("change", (event) => setViewerMode(event.target.value));
  nodes.apiBase?.addEventListener("change", () => {
    try {
      trustedApiBase();
      nodes.apiBase.setCustomValidity("");
    } catch (error) {
      nodes.apiBase.setCustomValidity(error.message);
      nodes.apiBase.reportValidity();
      updateApiState(false, "Untrusted API base blocked");
      setRuntime("auth", "Token not sent");
      return;
    }
    checkRuntime();
  });
  document.querySelector("[data-check-runtime]")?.addEventListener("click", checkRuntime);
  document.querySelector("[data-load-model-catalog]")?.addEventListener("click", loadModels);
  document.querySelector("[data-download-report]")?.addEventListener("click", downloadReport);
  document.querySelector("[data-download-package]")?.addEventListener("click", downloadPackage);
  document.querySelector("[data-clear-chat]")?.addEventListener("click", () => {
    state.messages = [];
    nodes.conversation?.querySelectorAll(".message:not(.message-system)").forEach((message) => message.remove());
    setRuntime("execution", "No guarded review requested");
    if (nodes.composerStatus) nodes.composerStatus.textContent = "Local chat cleared. The browser-local activity report was kept.";
  });
  document.querySelector("[data-clear-activity]")?.addEventListener("click", () => {
    state.shared = structuredClone(defaultSharedSession);
    saveShared();
    renderActivityState();
    if (nodes.composerStatus) nodes.composerStatus.textContent = "Local activity cleared from this browser. No remote data was deleted.";
  });
  document.addEventListener("keydown", (event) => {
    const editingTarget = event.target instanceof Element && Boolean(event.target.closest("input, textarea, select, [contenteditable='true']"));
    if (event.key === "/" && !editingTarget && state.viewerMode === "admin" && !event.metaKey && !event.ctrlKey && !event.altKey) {
      event.preventDefault();
      nodes.modelSearch?.focus();
    }
  });

  renderCurated();
  setViewerMode(state.viewerMode);
  renderActivityState();
})();
