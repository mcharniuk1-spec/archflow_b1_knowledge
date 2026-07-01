const QUIZ_PACKAGES = {
  "source-prd": {
    title: "Source-to-PRD Packet",
    bottlenecks: ["prd-rework", "task-ambiguity", "context-loss"],
    goals: ["prd", "tasks"],
    inputs: ["Calls", "Chats", "Docs", "Tickets", "Research", "Decisions"],
    gates: ["Source scope approved", "Product lead approves PRD claims", "Engineering reviews task readiness"],
    action: "Start with one project source inventory, then produce a source-backed PRD and task matrix."
  },
  "icp-evidence": {
    title: "ICP Evidence Review",
    bottlenecks: ["weak-evidence", "icp-unclear"],
    goals: ["icp"],
    inputs: ["Customer notes", "Sales signals", "Competitor notes", "Market research", "Account evidence"],
    gates: ["No demand claim without evidence", "Owner approves target segment", "Gaps remain visible"],
    action: "Start with the current ICP assumptions and build evidence cards, source grades, and disqualifiers."
  },
  "agent-orchestra": {
    title: "Agent Orchestra Setup",
    bottlenecks: ["agent-control", "task-ambiguity"],
    goals: ["agents"],
    inputs: ["Node contracts", "Prompts", "Run notes", "Approval rules", "Provider boundaries"],
    gates: ["Provider activation requires approval", "External writes require approval", "Reviewer pass before integration"],
    action: "Start with dashboard node contracts and approval gates before enabling provider-backed execution."
  },
  "knowledgebase-loop": {
    title: "Knowledgebase And Execution Loop",
    bottlenecks: ["context-loss", "weak-evidence", "agent-control"],
    goals: ["tasks", "agents"],
    inputs: ["Memory rules", "Source registry", "Issues", "Decisions", "Run notes"],
    gates: ["Secrets are masked", "Private raw sources stay out of public artifacts", "Durable choices become decisions"],
    action: "Start with a memory contract and source registry so future PRDs and agent runs do not repeat context loss."
  }
};

if (new URLSearchParams(window.location.search).has("figma")) {
  document.documentElement.dataset.captureMode = "full";
}

const SOURCE_LABELS = {
  calls: "customer calls or meeting notes",
  chats: "team chats",
  docs: "product or research docs",
  tickets: "ticket systems",
  analytics: "product analytics",
  sales: "sales or success notes",
  github: "GitHub or technical docs"
};

const BOTTLENECK_LABELS = {
  "prd-rework": "PRD rework",
  "weak-evidence": "weak evidence",
  "task-ambiguity": "ambiguous tasks",
  "icp-unclear": "unclear ICP",
  "context-loss": "discovery-to-delivery context loss",
  "agent-control": "unclear agent approval gates"
};

const QUIZ_STORAGE_KEY = "archflow-prd-icp-quiz-v1";
const QUIZ_SUBMISSION_SOURCE = "archflow-prd-icp-diagnostic";
const OTHER_VALUE = "other";
const quizEuro = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "EUR",
  maximumFractionDigits: 0
});
const quizNumber = new Intl.NumberFormat("en-US", { maximumFractionDigits: 0 });

function qClamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

function checkedValues(form, name) {
  return [...form.querySelectorAll(`[name="${name}"]:checked`)].map((input) => input.value);
}

function radioValue(form, name) {
  return form.querySelector(`[name="${name}"]:checked`)?.value || "";
}

function otherValue(form, name) {
  return form.elements[`${name}Other`]?.value.trim() || "";
}

function displayChoice(value, customText, labels = {}) {
  if (value === OTHER_VALUE) return customText ? `Other: ${customText}` : "Other";
  return labels[value] || value;
}

function displayChoices(values, customText, labels = {}) {
  return values.map((item) => displayChoice(item, item === OTHER_VALUE ? customText : "", labels));
}

function parseBudgetAmount(text) {
  const match = String(text || "").match(/(\d[\d\s,.]*)(\s*k)?/i);
  if (!match) return 0;
  const numeric = Number(match[1].replace(/[^\d.]/g, ""));
  if (!Number.isFinite(numeric)) return 0;
  return match[2] ? numeric * 1000 : numeric;
}

function budgetDisplay(value, customText) {
  const labels = {
    "5000": "Under EUR 7,500",
    "12500": "EUR 7,500-17,500",
    "25000": "EUR 17,500-35,000",
    "45000": "EUR 35,000+",
    "14500": "Not sure yet"
  };
  if (value === "custom") return customText ? `Other: ${customText}` : "Other";
  return labels[value] || "";
}

function collectState(form) {
  const budgetBand = form.elements.budget.value;
  const budgetOther = form.elements.budgetOther?.value.trim() || "";
  const sources = checkedValues(form, "sources");
  const bottlenecks = checkedValues(form, "bottlenecks");
  const ownerRole = radioValue(form, "ownerRole");
  const sourceStructure = radioValue(form, "sourceStructure");
  const firstGoal = radioValue(form, "firstGoal");

  return {
    productPeople: Number(form.elements.productPeople.value),
    ownerRole,
    ownerRoleOther: otherValue(form, "ownerRole"),
    ownerRoleDisplay: displayChoice(ownerRole, otherValue(form, "ownerRole")),
    sources,
    sourcesOther: otherValue(form, "sources"),
    sourcesDisplay: displayChoices(sources, otherValue(form, "sources"), SOURCE_LABELS),
    sourceStructure,
    sourceStructureOther: otherValue(form, "sourceStructure"),
    sourceStructureDisplay: displayChoice(sourceStructure, otherValue(form, "sourceStructure")),
    bottlenecks,
    bottlenecksOther: otherValue(form, "bottlenecks"),
    bottlenecksDisplay: displayChoices(bottlenecks, otherValue(form, "bottlenecks"), BOTTLENECK_LABELS),
    firstGoal,
    firstGoalOther: otherValue(form, "firstGoal"),
    firstGoalDisplay: displayChoice(firstGoal, otherValue(form, "firstGoal")),
    weeklyHours: Number(form.elements.weeklyHours.value),
    hourlyCost: Number(form.elements.hourlyCost.value),
    wasteShare: Number(form.elements.wasteShare.value),
    recoverableShare: Number(form.elements.recoverableShare.value),
    evidenceQuality: Number(form.elements.evidenceQuality.value),
    approvalMaturity: Number(form.elements.approvalMaturity.value),
    budget: budgetBand === "custom" ? parseBudgetAmount(budgetOther) || 14500 : Number(budgetBand || 0),
    budgetBand,
    budgetOther,
    budgetDisplay: budgetDisplay(budgetBand, budgetOther),
    success30: form.elements.success30.value.trim(),
    contactName: form.elements.contactName.value.trim(),
    contactEmail: form.elements.contactEmail.value.trim(),
    contactCompany: form.elements.contactCompany.value.trim(),
    consent: Boolean(form.elements.consent?.checked),
    website: form.elements.website?.value.trim() || ""
  };
}

function saveState(form) {
  localStorage.setItem(QUIZ_STORAGE_KEY, JSON.stringify(collectState(form)));
}

function restoreState(form) {
  const raw = localStorage.getItem(QUIZ_STORAGE_KEY);
  if (!raw) return;
  try {
    const state = JSON.parse(raw);
    Object.entries(state).forEach(([key, value]) => {
      if (Array.isArray(value)) {
        value.forEach((item) => {
          const input = form.querySelector(`[name="${key}"][value="${CSS.escape(item)}"]`);
          if (input) input.checked = true;
        });
        return;
      }
      const controls = [...form.querySelectorAll(`[name="${CSS.escape(key)}"]`)];
      if (!controls.length) return;
      if (controls.length > 1 && controls[0].type === "radio") {
        const radio = form.querySelector(`[name="${CSS.escape(key)}"][value="${CSS.escape(String(value))}"]`);
        if (radio) radio.checked = true;
        return;
      }
      const control = controls[0];
      if (control.type === "checkbox") {
        control.checked = Boolean(value);
      } else {
        control.value = value;
      }
    });
  } catch (error) {
    localStorage.removeItem(QUIZ_STORAGE_KEY);
  }
}

function scorePackages(state) {
  const scores = Object.fromEntries(Object.keys(QUIZ_PACKAGES).map((id) => [id, 0]));
  Object.entries(QUIZ_PACKAGES).forEach(([id, pack]) => {
    state.bottlenecks.forEach((bottleneck, index) => {
      if (pack.bottlenecks.includes(bottleneck)) scores[id] += 42 - index * 5;
    });
    if (pack.goals.includes(state.firstGoal)) scores[id] += 28;
  });
  if (state.sourceStructure === "low") scores["knowledgebase-loop"] += 24;
  if (state.sources.includes("analytics") || state.sources.includes("sales")) scores["icp-evidence"] += 12;
  if (state.bottlenecks.includes("agent-control")) scores["agent-orchestra"] += 20;
  return Object.entries(scores).sort((a, b) => b[1] - a[1])[0][0];
}

function readinessScores(state) {
  const sourceScore = state.sourceStructure === "high" ? 90 : state.sourceStructure === "medium" ? 64 : 35;
  const sourceCoverage = qClamp(state.sources.length * 12, 25, 100);
  const evidence = state.evidenceQuality * 10;
  const prdStructure = state.bottlenecks.includes("prd-rework") ? 45 : 70;
  const approval = state.approvalMaturity * 10;
  const taskReadiness = state.bottlenecks.includes("task-ambiguity") ? 48 : 72;

  const kb = Math.round(sourceScore * 0.28 + sourceCoverage * 0.22 + evidence * 0.25 + prdStructure * 0.25);
  const agent = Math.round(sourceScore * 0.18 + approval * 0.32 + taskReadiness * 0.25 + prdStructure * 0.25);
  return { kb, agent };
}

function calculateResult(state) {
  const packageId = scorePackages(state);
  const pack = QUIZ_PACKAGES[packageId];
  const readiness = readinessScores(state);
  const monthlyLostValue = state.weeklyHours * 4.33 * state.hourlyCost * (state.wasteShare / 100);
  const monthlyRecoveredValue = monthlyLostValue * (state.recoverableShare / 100);
  const payback = monthlyRecoveredValue > 0 ? state.budget / monthlyRecoveredValue : null;
  const primaryBottleneck = state.bottlenecks.find((item) => item !== OTHER_VALUE) || pack.bottlenecks[0];

  return {
    packageId,
    pack,
    kbReadiness: readiness.kb,
    agentReadiness: readiness.agent,
    monthlyRecoveredValue,
    payback,
    primaryBottleneck
  };
}

function updateRangeOutputs(form) {
  form.querySelector('[data-quiz-output="productPeople"]').textContent = `${form.elements.productPeople.value} people`;
  form.querySelector('[data-quiz-output="weeklyHours"]').textContent = `${form.elements.weeklyHours.value} hours`;
  form.querySelector('[data-quiz-output="hourlyCost"]').textContent = quizEuro.format(Number(form.elements.hourlyCost.value));
  form.querySelector('[data-quiz-output="wasteShare"]').textContent = `${form.elements.wasteShare.value}%`;
  form.querySelector('[data-quiz-output="recoverableShare"]').textContent = `${form.elements.recoverableShare.value}%`;
  form.querySelector('[data-quiz-output="evidenceQuality"]').textContent = `${form.elements.evidenceQuality.value} / 10`;
  form.querySelector('[data-quiz-output="approvalMaturity"]').textContent = `${form.elements.approvalMaturity.value} / 10`;
}

function renderResult(form) {
  const state = collectState(form);
  const result = calculateResult(state);
  const pack = result.pack;
  const sourceState = state.sourceStructureDisplay ? `${state.sourceStructureDisplay.toLowerCase()} source structure` : "a source structure that still needs scoping";
  const explanation = `Based on your answers, ArchFlow should start with ${pack.title} because your strongest pressure is ${BOTTLENECK_LABELS[result.primaryBottleneck] || "product workflow readiness"} and your current knowledgebase state suggests ${sourceState}.`;

  document.querySelector("[data-sidebar-service]").textContent = pack.title;
  document.querySelector("[data-result-headline]").textContent = `Your strongest first package: ${pack.title}`;
  document.querySelector("[data-result-explanation]").textContent = explanation;
  document.querySelector("[data-result-kb]").textContent = `${result.kbReadiness} / 100`;
  document.querySelector("[data-result-agent]").textContent = `${result.agentReadiness} / 100`;
  document.querySelector("[data-result-value]").textContent = quizEuro.format(result.monthlyRecoveredValue);
  document.querySelector("[data-result-payback]").textContent = result.payback ? `${Math.max(1, Math.round(result.payback))} mo` : "Needs scoping";
  document.querySelector("[data-result-tools]").innerHTML = pack.inputs.map((tool) => `<span class="tool-chip">${tool}</span>`).join("");
  document.querySelector("[data-result-gates]").innerHTML = pack.gates.map((gate) => `<li>${gate}</li>`).join("");
  document.querySelector("[data-result-next-action]").textContent = pack.action;

  const mailBody = [
    "ArchFlow PRD/ICP workflow diagnostic",
    "",
    `Recommended package: ${pack.title}`,
    `Knowledgebase readiness: ${result.kbReadiness}/100`,
    `Agent execution readiness: ${result.agentReadiness}/100`,
    `Monthly value estimate: ${quizEuro.format(result.monthlyRecoveredValue)}`,
    `Payback estimate: ${result.payback ? `${Math.max(1, Math.round(result.payback))} months` : "Needs scoping"}`,
    `Bottlenecks: ${state.bottlenecksDisplay.join(", ")}`,
    `Sources: ${state.sourcesDisplay.join(", ")}`,
    `Budget: ${state.budgetDisplay || "Not provided"}`,
    `30-day success: ${state.success30 || "Not provided"}`,
    "",
    `Name: ${state.contactName || ""}`,
    `Email: ${state.contactEmail || ""}`,
    `Company: ${state.contactCompany || ""}`
  ].join("\n");

  document.querySelector("[data-mailto-link]").href =
    `mailto:hello@archflow.ai?subject=${encodeURIComponent("ArchFlow PRD/ICP diagnostic")}&body=${encodeURIComponent(mailBody)}`;
}

function buildSubmission(form) {
  const state = collectState(form);
  const result = calculateResult(state);
  return {
    source: QUIZ_SUBMISSION_SOURCE,
    timestamp: new Date().toISOString(),
    pageUrl: window.location.href,
    website: state.website,
    answers: state,
    result: {
      recommendedPackage: result.pack.title,
      packageId: result.packageId,
      knowledgebaseReadiness: result.kbReadiness,
      agentReadiness: result.agentReadiness,
      monthlyValueEstimate: Math.round(result.monthlyRecoveredValue),
      estimatedPayback: result.payback ? `${Math.max(1, Math.round(result.payback))} mo` : "Needs scoping",
      primaryBottleneck: result.primaryBottleneck
    },
    client: {
      userAgent: navigator.userAgent,
      language: navigator.language,
      screen: `${window.screen.width}x${window.screen.height}`
    }
  };
}

function validateStep(form, stepIndex) {
  const step = form.querySelector(`[data-step="${stepIndex}"]`);
  const error = document.querySelector("[data-form-error]");
  error.textContent = "";

  const requiredGroups = [...step.querySelectorAll("[data-required-group]")];
  for (const group of requiredGroups) {
    const name = group.dataset.requiredGroup;
    const checked = form.querySelectorAll(`[name="${name}"]:checked`).length;
    if (!checked) {
      error.textContent = "Please answer the required question before continuing.";
      group.classList.add("has-error");
      return false;
    }

    const checkedOther = group.querySelector(`[name="${name}"][value="${OTHER_VALUE}"]:checked`);
    const otherInput = form.elements[`${name}Other`];
    if (checkedOther && otherInput && !otherInput.value.trim()) {
      error.textContent = "Please describe the Other option before continuing.";
      group.classList.add("has-error");
      otherInput.focus();
      return false;
    }
    group.classList.remove("has-error");
  }

  if (stepIndex === 3 && !form.elements.budget.value) {
    error.textContent = "Please select a budget band before continuing.";
    form.elements.budget.focus();
    return false;
  }

  if (stepIndex === 3 && form.elements.budget.value === "custom" && !form.elements.budgetOther.value.trim()) {
    error.textContent = "Please describe the Other budget detail before continuing.";
    form.elements.budgetOther.focus();
    return false;
  }

  return true;
}

function setupMaxSelect(form) {
  form.querySelectorAll("[data-max-select]").forEach((group) => {
    const max = Number(group.dataset.maxSelect);
    group.addEventListener("change", (event) => {
      const checked = [...group.querySelectorAll("input:checked")];
      if (checked.length > max) {
        event.target.checked = false;
      }
    });
  });
}

function setupOtherInputs(form) {
  const budgetOther = document.querySelector("[data-budget-other]");

  function syncOtherField(input) {
    const groupName = input.dataset.otherFor;
    const active = Boolean(form.querySelector(`[name="${groupName}"][value="${OTHER_VALUE}"]:checked`));
    input.disabled = !active;
    input.required = active;
    if (!active) input.value = "";
  }

  form.querySelectorAll("[data-other-for]").forEach((input) => {
    syncOtherField(input);
    input.closest(".choice-field")?.addEventListener("change", () => syncOtherField(input));
  });

  function syncBudgetOther() {
    const active = form.elements.budget.value === "custom";
    if (budgetOther) budgetOther.hidden = !active;
    form.elements.budgetOther.disabled = !active;
    form.elements.budgetOther.required = active;
    if (!active) form.elements.budgetOther.value = "";
  }

  form.elements.budget.addEventListener("change", syncBudgetOther);
  syncBudgetOther();
}

function setupQuizDepthMotion() {
  const fields = [...document.querySelectorAll("[data-arch-field]")];
  let ticking = false;

  function update() {
    const pageMax = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    const pageProgress = qClamp(window.scrollY / pageMax, 0, 1);
    document.body.style.setProperty("--light-x", `${Math.round(10 + pageProgress * 22)}%`);
    document.body.style.setProperty("--light-y", `${Math.round(16 + pageProgress * 48)}%`);

    fields.forEach((field) => {
      const host = field.closest(".quiz-shell") || field;
      const rect = host.getBoundingClientRect();
      const viewport = window.innerHeight || document.documentElement.clientHeight || 1;
      const progress = qClamp((viewport - rect.top) / (viewport + rect.height), 0, 1);
      const phase = (progress - 0.5) * 2;
      field.querySelectorAll("[data-arch-layer]").forEach((arc, index) => {
        const speed = Number(arc.dataset.speed || 0.5);
        const drift = Number(arc.dataset.drift || 0);
        const rotate = Number(arc.dataset.rotate || 0);
        const x = phase * 120 * speed + drift * progress;
        const y = Math.sin(progress * Math.PI * 2 + index) * 16 * speed;
        arc.style.setProperty("--scroll-x", `${x.toFixed(1)}px`);
        arc.style.setProperty("--scroll-y", `${y.toFixed(1)}px`);
        arc.style.setProperty("--arc-rotate", `${(rotate * phase).toFixed(2)}deg`);
      });
    });
    ticking = false;
  }

  function requestUpdate() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(update);
  }

  window.addEventListener("scroll", requestUpdate, { passive: true });
  window.addEventListener("resize", requestUpdate);
  update();
}

function setupQuiz() {
  const form = document.querySelector("[data-quiz-form]");
  if (!form) return;

  restoreState(form);
  setupMaxSelect(form);
  setupOtherInputs(form);

  const steps = [...form.querySelectorAll("[data-step]")];
  const next = document.querySelector("[data-next-step]");
  const prev = document.querySelector("[data-prev-step]");
  const progress = document.querySelector("[data-quiz-progress]");
  const label = document.querySelector("[data-step-label]");
  const title = document.querySelector("[data-step-title]");
  const submitButton = document.querySelector("[data-submit-assessment]");
  const submitStatus = document.querySelector("[data-submit-status]");
  const requestedStep = Number(new URLSearchParams(window.location.search).get("step"));
  let activeStep = 0;

  function showStep(index) {
    activeStep = qClamp(index, 0, steps.length - 1);
    steps.forEach((step, stepIndex) => {
      const active = stepIndex === activeStep;
      step.classList.toggle("is-active", active);
      step.hidden = !active;
    });
    progress.style.width = `${((activeStep + 1) / steps.length) * 100}%`;
    label.textContent = `Step ${activeStep + 1} of ${steps.length}`;
    title.textContent = steps[activeStep].dataset.title;
    prev.disabled = activeStep === 0;
    next.textContent = activeStep === steps.length - 1 ? "Update result" : "Next";
    if (activeStep === steps.length - 1) renderResult(form);
  }

  form.addEventListener("input", () => {
    updateRangeOutputs(form);
    saveState(form);
    if (activeStep === steps.length - 1) renderResult(form);
  });
  form.addEventListener("change", () => {
    saveState(form);
    if (activeStep === steps.length - 1) renderResult(form);
  });

  next.addEventListener("click", () => {
    if (activeStep < steps.length - 1) {
      if (!validateStep(form, activeStep)) return;
      showStep(activeStep + 1);
      return;
    }
    renderResult(form);
    saveState(form);
  });

  prev.addEventListener("click", () => showStep(activeStep - 1));

  submitButton?.addEventListener("click", async () => {
    renderResult(form);
    saveState(form);
    submitStatus.textContent = "";
    submitButton.disabled = true;
    submitButton.textContent = "Saving...";

    try {
      const response = await fetch("/api/quiz-submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(buildSubmission(form))
      });
      const data = await response.json();
      if (!response.ok || !data.ok) throw new Error(data.code || "SUBMISSION_FAILED");
      submitStatus.textContent = "Saved to ArchFlow. We will review the assessment and follow up if contact details were provided.";
    } catch (error) {
      submitStatus.textContent =
        error.message === "SHEETS_NOT_CONFIGURED"
          ? "The backend save path is ready in code but not configured yet. Use the email fallback for now."
          : "Could not save automatically. Use the email fallback or try again later.";
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = "Save assessment to ArchFlow";
    }
  });

  updateRangeOutputs(form);
  showStep(Number.isInteger(requestedStep) ? requestedStep : 0);
}

document.addEventListener("DOMContentLoaded", setupQuiz);
document.addEventListener("DOMContentLoaded", setupQuizDepthMotion);
