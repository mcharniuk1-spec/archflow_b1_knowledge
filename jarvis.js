(function () {
  "use strict";

  const fallbackModels = [
    { id: "openai/gpt-5.6-luna", name: "GPT-5.6 Luna", provider: "OpenAI", tier: "frontier", context_length: 1050000, allowed: true },
    { id: "anthropic/claude-sonnet-5", name: "Claude Sonnet 5", provider: "Anthropic", tier: "frontier", context_length: 1000000, allowed: true },
    { id: "qwen/qwen3.7-plus", name: "Qwen3.7 Plus", provider: "Qwen", tier: "economy", context_length: 1000000, allowed: true },
    { id: "deepseek/deepseek-v4-flash", name: "DeepSeek V4 Flash", provider: "DeepSeek", tier: "economy", context_length: 1048576, allowed: true }
  ];

  const state = {
    curated: fallbackModels,
    catalog: fallbackModels,
    allowed: new Set(fallbackModels.map((model) => model.id)),
    selectedId: fallbackModels[0].id,
    selectedName: fallbackModels[0].name,
    messages: [],
    apiOnline: false
  };

  const nodes = {
    form: document.querySelector("[data-chat-form]"),
    conversation: document.querySelector("[data-conversation]"),
    ownerToken: document.querySelector("[data-owner-token]"),
    apiBase: document.querySelector("[data-api-base]"),
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
    if (!sameOrigin && !loopback) {
      throw new Error("API base must be this origin or an HTTP loopback address");
    }
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

  function perMillion(value) {
    const number = Number(value);
    if (!Number.isFinite(number)) return null;
    const dollars = number * 1000000;
    return dollars < 1 ? `$${dollars.toFixed(2)}` : `$${dollars.toFixed(1)}`;
  }

  function modelDisplay(model) {
    return model.name || model.label || model.id;
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
    nodes.modelCards.replaceChildren(
      ...state.curated.map((model) => {
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
        detail.textContent = `${formatContext(model.context_length)} · ${state.allowed.has(model.id) ? "allowed" : "server allowlist required"}`;
        button.append(provider, title, detail);
        button.addEventListener("click", () => setSelected(model));
        return button;
      })
    );
  }

  function renderCatalog(query) {
    if (!nodes.catalogResults) return;
    const normalized = query.trim().toLowerCase();
    if (!normalized) {
      nodes.catalogResults.replaceChildren();
      return;
    }

    const results = state.catalog
      .filter((model) => `${model.id} ${modelDisplay(model)} ${model.description || ""}`.toLowerCase().includes(normalized))
      .slice(0, 24);

    nodes.catalogResults.replaceChildren(
      ...results.map((model) => {
        const button = document.createElement("button");
        button.type = "button";
        button.className = "catalog-result";
        button.disabled = !state.allowed.has(model.id);

        const title = document.createElement("strong");
        title.textContent = modelDisplay(model);
        const stateLabel = document.createElement("em");
        stateLabel.textContent = state.allowed.has(model.id) ? "Allowed" : "Search only";
        const detail = document.createElement("span");
        const prompt = perMillion(model.pricing?.prompt);
        const completion = perMillion(model.pricing?.completion);
        detail.textContent = `${model.id} · ${formatContext(model.context_length)}${prompt && completion ? ` · ${prompt}/${completion} per 1M input/output` : ""}`;
        button.append(title, stateLabel, detail);
        button.addEventListener("click", () => setSelected(model));
        return button;
      })
    );

    if (nodes.catalogStatus) {
      nodes.catalogStatus.textContent = results.length
        ? `${results.length} result${results.length === 1 ? "" : "s"}; search-only routes require a server allowlist change.`
        : "No matching route in the loaded catalog.";
    }
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
    updateApiState(false, "Checking API");
    try {
      const health = await fetchJson(apiUrl("/api/health"), {}, 5000);
      const payload = health.payload || {};
      updateApiState(true, payload.provider_enabled ? "API ready / gated" : "API ready / provider off");
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
    let catalogUrl = "https://openrouter.ai/api/v1/models";
    try {
      const response = await fetchJson(apiUrl("/api/models"), {}, 5000);
      const payload = response.payload || {};
      if (Array.isArray(payload.allowed_model_ids)) state.allowed = new Set(payload.allowed_model_ids);
      if (Array.isArray(payload.curated) && payload.curated.length) {
        state.curated = payload.curated.map((model) => ({ ...model, name: model.label || model.id }));
      }
      if (payload.live_catalog_url) catalogUrl = payload.live_catalog_url;
    } catch (_error) {
      // Static preview uses the public-safe curated fallback and still attempts the live public catalog.
    }

    renderCurated();
    try {
      const live = await fetchJson(catalogUrl, {}, 10000);
      if (Array.isArray(live.data) && live.data.length) {
        state.catalog = live.data;
        if (nodes.catalogStatus) nodes.catalogStatus.textContent = `${live.data.length} live routes loaded. Search does not authorize execution.`;
      }
    } catch (_error) {
      state.catalog = state.curated;
      if (nodes.catalogStatus) nodes.catalogStatus.textContent = "Live catalog unavailable; curated 2026-07-13 routes remain available.";
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
    meta.append(source, detail);
    const body = document.createElement("p");
    body.textContent = text;
    article.append(meta, body);
    nodes.conversation.append(article);
    nodes.conversation.scrollTop = nodes.conversation.scrollHeight;
  }

  async function submitChat(event) {
    event.preventDefault();
    if (!nodes.form || !nodes.send) return;
    const data = new FormData(nodes.form);
    const request = String(data.get("request") || "").trim();
    if (!request) return;

    const approved = data.get("provider_approval") === "on";
    const token = nodes.ownerToken?.value || "";
    const conversation = state.messages.slice(-6);
    appendMessage("user", request, `${state.selectedName} · ${data.get("architecture")}`);
    state.messages.push({ role: "user", source: "jarvis-page", text: request, time: new Date().toISOString() });
    nodes.send.disabled = true;
    if (nodes.composerStatus) nodes.composerStatus.textContent = "Waiting for the guarded API; no execution is claimed until its receipt returns.";

    const headers = { "Content-Type": "application/json" };
    if (token) headers.Authorization = `Bearer ${token}`;

    try {
      const result = await fetchJson(
        apiUrl("/api/chat"),
        {
          method: "POST",
          headers,
          body: JSON.stringify({
            request,
            lane: "jarvis_operator",
            architecture: data.get("architecture") || "control",
            model_id: state.selectedId,
            provider_approval: approved,
            conversation
          })
        },
        45000
      );

      const provider = result.payload?.provider_result || {};
      const executed = provider.provider_executed === true;
      const text = executed
        ? String(provider.reply || "Provider returned an empty response.")
        : `Review packet created. Provider execution did not occur. Blocker: ${provider.reason || result.status || "not reported"}.`;
      const model = provider.model || provider.requested_model || state.selectedId;
      appendMessage("assistant", text, executed ? `${model} · execution receipt returned` : `${model} · gated`, !executed);
      state.messages.push({ role: "assistant", source: model, text, time: new Date().toISOString() });
      setRuntime("execution", executed ? `Executed · ${model}` : `Blocked · ${provider.reason || result.status}`);
      if (nodes.composerStatus) {
        const usage = provider.usage || {};
        nodes.composerStatus.textContent = executed
          ? `Executed by ${model}. Usage receipt: ${usage.total_tokens ?? "not reported"} total tokens. Writeback remains disabled.`
          : `No provider call was proven. ${provider.reason || "A runtime gate blocked execution."}`;
      }
      updateApiState(true, executed ? "Provider response received" : "API ready / call gated");
    } catch (error) {
      appendMessage("assistant", `The guarded API could not be reached: ${error.message}. No provider response or writeback occurred.`, "transport failure", true);
      setRuntime("execution", "Transport failed");
      if (nodes.composerStatus) nodes.composerStatus.textContent = "Transport failed. No provider execution is claimed.";
      updateApiState(false, "API unavailable");
    } finally {
      nodes.send.disabled = false;
      nodes.form.elements.request.value = "";
      nodes.form.elements.provider_approval.checked = false;
      nodes.form.elements.request.focus();
    }
  }

  nodes.form?.addEventListener("submit", submitChat);
  nodes.modelSearch?.addEventListener("input", (event) => renderCatalog(event.target.value));
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
    loadModels();
  });
  document.querySelector("[data-check-runtime]")?.addEventListener("click", checkRuntime);
  document.querySelector("[data-clear-chat]")?.addEventListener("click", () => {
    state.messages = [];
    nodes.conversation?.querySelectorAll(".message:not(.message-system)").forEach((message) => message.remove());
    setRuntime("execution", "No call yet");
    if (nodes.composerStatus) nodes.composerStatus.textContent = "Local chat cleared. No remote data was deleted.";
  });
  document.addEventListener("keydown", (event) => {
    const editingTarget = event.target instanceof Element
      && Boolean(event.target.closest("input, textarea, select, [contenteditable='true']"));
    if (event.key === "/" && !editingTarget && document.activeElement !== nodes.modelSearch && !event.metaKey && !event.ctrlKey && !event.altKey) {
      event.preventDefault();
      nodes.modelSearch?.focus();
    }
  });

  renderCurated();
  checkRuntime();
  loadModels();
})();
