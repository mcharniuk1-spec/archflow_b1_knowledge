(function () {
  "use strict";

  const HANDOFF_KEY = "archflow.public.v3.handoff";
  const SCHEMA_VERSION = "3.0";
  const HOSTED_ORIGIN = "https://www.arch-flow.dev";
  const STRING_RULES = Object.freeze({
    objective: { required: true, max: 1200 },
    decision: { required: false, max: 1200 },
    public_reference: { required: false, max: 500 },
    allowed_evidence: { required: false, max: 1800 },
    exclusions: { required: false, max: 1800 },
    requested_output: { required: true, max: 1000 },
    reviewer: { required: false, max: 300 },
    constraints: { required: false, max: 1800 }
  });

  const form = document.querySelector("[data-packet-form]");
  const submitButton = document.querySelector("[data-submit-packet]");
  const statusNode = document.querySelector("[data-form-status]");

  function isFileMode() {
    return window.location.protocol === "file:";
  }

  function dashboardDestination() {
    return isFileMode()
      ? "project/dashboard/index.html#communication"
      : "/project/dashboard/#communication";
  }

  function authDestination() {
    return window.location.origin === HOSTED_ORIGIN
      ? "/api/auth/google/start?return=jarvis"
      : `${HOSTED_ORIGIN}/api/auth/google/start?return=jarvis`;
  }

  function configureRoutes() {
    document.querySelectorAll("[data-dashboard-link]").forEach((link) => {
      link.setAttribute("href", dashboardDestination());
    });
    document.querySelector("[data-admin-action]")?.setAttribute("href", authDestination());
  }

  function normalizeText(value) {
    return String(value || "")
      .replace(/\r\n?/g, "\n")
      .split("\n")
      .map((line) => line.replace(/[\t ]+/g, " ").trim())
      .join("\n")
      .replace(/\n{3,}/g, "\n\n")
      .trim();
  }

  function unsafeReason(value) {
    const text = String(value || "");
    const checks = [
      { pattern: /file:\/\//i, message: "Remove file URLs." },
      { pattern: /(?:^|[\s"'(])(?:\/Users\/|\/home\/[^\s/]+\/|\/private\/|\/var\/|\/tmp\/|\/Volumes\/|~\/|[A-Za-z]:\\Users\\)/im, message: "Remove local device paths." },
      { pattern: /-----BEGIN [A-Z ]*(?:PRIVATE KEY|CERTIFICATE)-----/i, message: "Remove key or certificate material." },
      { pattern: /(?:^|[\s"'(])(?:sk-[A-Za-z0-9_-]{16,}|github_pat_[A-Za-z0-9_]{16,}|gh[pousr]_[A-Za-z0-9]{16,}|AKIA[A-Z0-9]{16})(?:$|[\s"'),.;])/m, message: "Remove credential-like values." },
      { pattern: /\bBearer\s+[A-Za-z0-9._~-]{12,}/i, message: "Remove bearer credentials." },
      { pattern: /\b(?:api[_ -]?key|access[_ -]?token|refresh[_ -]?token|password|client[_ -]?secret)\s*[:=]\s*["']?[^\s"',;]{6,}/i, message: "Remove assigned secret values." },
      { pattern: /\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b/i, message: "Remove personal identifiers such as email addresses." }
    ];
    return checks.find((check) => check.pattern.test(text))?.message || "";
  }

  function privateHostname(hostname) {
    const host = hostname.toLowerCase().replace(/^\[|\]$/g, "");
    if (host === "localhost" || host.endsWith(".local") || host === "::1") return true;
    if (/^127\./.test(host) || /^10\./.test(host) || /^192\.168\./.test(host)) return true;
    const match = host.match(/^172\.(\d{1,3})\./);
    return Boolean(match && Number(match[1]) >= 16 && Number(match[1]) <= 31);
  }

  function publicReferenceReason(value) {
    const text = normalizeText(value);
    if (!text || !/^[a-z][a-z0-9+.-]*:\/\//i.test(text)) return "";
    let url;
    try {
      url = new URL(text);
    } catch (_error) {
      return "Use a valid public HTTPS URL or a generic label.";
    }
    if (url.protocol !== "https:") return "Public references must use HTTPS.";
    if (url.username || url.password) return "Remove credentials from the public reference.";
    if (privateHostname(url.hostname)) return "Local and private-network references are not allowed.";
    for (const name of url.searchParams.keys()) {
      if (/(?:token|key|secret|auth|password|signature)/i.test(name)) {
        return "Remove credential-like query parameters from the public reference.";
      }
    }
    return "";
  }

  function setStatus(message, state) {
    if (!statusNode) return;
    statusNode.textContent = message;
    statusNode.dataset.state = state;
  }

  function setFieldError(field, message) {
    field.setCustomValidity(message);
    field.setAttribute("aria-invalid", message ? "true" : "false");
  }

  function clearFieldError(field) {
    setFieldError(field, "");
  }

  function collectValues() {
    const data = new FormData(form);
    const values = {};
    Object.keys(STRING_RULES).forEach((name) => {
      values[name] = normalizeText(data.get(name));
    });
    return values;
  }

  function validateFormValues(values) {
    let firstInvalid = null;

    Object.entries(STRING_RULES).forEach(([name, rule]) => {
      const field = form.elements.namedItem(name);
      if (!(field instanceof HTMLElement)) return;
      clearFieldError(field);
      let message = "";
      if (rule.required && !values[name]) message = "Complete this field.";
      else if (values[name].length > rule.max) message = `Use ${rule.max} characters or fewer.`;
      else message = unsafeReason(values[name]);
      if (!message && name === "public_reference") message = publicReferenceReason(values[name]);
      if (message) {
        setFieldError(field, message);
        firstInvalid ||= field;
      }
    });

    const confirmation = form.elements.namedItem("public_safe_confirmation");
    if (confirmation instanceof HTMLInputElement) {
      clearFieldError(confirmation);
      if (!confirmation.checked) {
        setFieldError(confirmation, "Confirm the public-safety boundary before transfer.");
        firstInvalid ||= confirmation;
      }
    }

    if (!form.checkValidity() || firstInvalid) {
      setStatus("Held locally. Complete the required fields and remove private or identifying material.", "error");
      form.reportValidity();
      firstInvalid?.focus();
      return false;
    }
    return true;
  }

  function buildPacket(values) {
    return {
      schema_version: SCHEMA_VERSION,
      kind: "archflow_public_handoff",
      objective: values.objective,
      decision: values.decision,
      public_reference: values.public_reference,
      allowed_evidence: values.allowed_evidence,
      exclusions: values.exclusions,
      requested_output: values.requested_output,
      reviewer: values.reviewer,
      constraints: values.constraints,
      created_at: new Date().toISOString(),
      state: "review_required"
    };
  }

  function validatePacket(packet) {
    if (!packet || typeof packet !== "object" || Array.isArray(packet)) return false;
    if (packet.schema_version !== SCHEMA_VERSION) return false;
    if (packet.kind !== "archflow_public_handoff") return false;
    if (!Number.isFinite(Date.parse(packet.created_at))) return false;
    if (packet.state !== "review_required") return false;

    for (const [name, rule] of Object.entries(STRING_RULES)) {
      const value = packet[name];
      if (typeof value !== "string") return false;
      if (rule.required && !value) return false;
      if (value.length > rule.max || unsafeReason(value)) return false;
    }
    if (publicReferenceReason(packet.public_reference)) return false;
    const allowedKeys = new Set(["schema_version", "kind", ...Object.keys(STRING_RULES), "created_at", "state"]);
    return Object.keys(packet).every((name) => allowedKeys.has(name));
  }

  function storePacket(packet) {
    if (!validatePacket(packet)) throw new Error("The packet failed its version-3 contract.");
    const encoded = JSON.stringify(packet);
    window.sessionStorage.setItem(HANDOFF_KEY, encoded);
    if (window.sessionStorage.getItem(HANDOFF_KEY) !== encoded) {
      throw new Error("The browser could not verify the tab-local handoff.");
    }
  }

  function submitPacket(event) {
    event.preventDefault();
    if (!form || !submitButton) return;
    const values = collectValues();
    if (!validateFormValues(values)) return;

    submitButton.disabled = true;
    try {
      const packet = buildPacket(values);
      storePacket(packet);
      setStatus("Packet validated. Opening the Communication Center in this tab.", "ready");
      window.setTimeout(() => window.location.assign(dashboardDestination()), 40);
    } catch (_error) {
      submitButton.disabled = false;
      setStatus("The browser could not create the tab-local handoff. No packet was sent.", "error");
    }
  }

  function updateCount(input) {
    if (!input.id) return;
    const counter = document.querySelector(`[data-count-for="${input.id}"]`);
    if (counter) counter.textContent = `${input.value.length} / ${input.maxLength}`;
  }

  function bindFields() {
    form?.querySelectorAll("input, textarea, select").forEach((field) => {
      updateCount(field);
      field.addEventListener("input", () => {
        clearFieldError(field);
        updateCount(field);
        if (statusNode?.dataset.state === "error") setStatus("Nothing has been stored or sent.", "idle");
      });
      field.addEventListener("change", () => clearFieldError(field));
    });
  }

  configureRoutes();
  bindFields();
  form?.addEventListener("submit", submitPacket);

  window.__ARCHFLOW_JARVIS_CONTRACT__ = Object.freeze({
    schemaVersion: SCHEMA_VERSION,
    handoffKey: HANDOFF_KEY,
    dashboardDestination: dashboardDestination()
  });
})();
