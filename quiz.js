const form = document.querySelector("#diagnosticForm");
const steps = Array.from(document.querySelectorAll(".diagnostic-step"));
const nextButton = document.querySelector("#nextStep");
const prevButton = document.querySelector("#prevStep");
const stepLabel = document.querySelector("#stepLabel");
const progressFill = document.querySelector("#progressFill");
const result = document.querySelector("#diagnosticResult");
const resultTitle = document.querySelector("#resultTitle");
const resultCopy = document.querySelector("#resultCopy");
const resultStack = document.querySelector("#resultStack");

let currentStep = 0;

const recommendationCopy = {
  prd: {
    title: "PRD Rescue And Evidence Map",
    copy: "Start with a source-backed PRD, explicit assumptions, acceptance criteria, and unresolved gaps before expanding automation."
  },
  icp: {
    title: "ICP Evidence Review",
    copy: "Focus first on buyer roles, pains, triggers, current alternatives, and confidence level so public positioning is not built on guesses."
  },
  system: {
    title: "Knowledgebase And Agent-Control Setup",
    copy: "Build the reusable memory, task matrix, decision wall, and approval gates before provider-backed agent execution."
  },
  team: {
    title: "Task Matrix And Delivery Sequence",
    copy: "Translate context into owners, dependencies, review gates, and acceptance criteria that engineering can execute."
  }
};

function formValue(name) {
  return new FormData(form).get(name);
}

function numeric(name) {
  return Number(formValue(name) || 0);
}

function scoreSources() {
  return form.querySelectorAll("input[name='sources']:checked").length;
}

function recommendation() {
  const outcome = formValue("outcome") || "prd";
  const breakage = formValue("breakage") || "prd";
  const agentScope = formValue("agentScope") || "draft";
  const knowledge = numeric("sourceLabels") + numeric("decisionTrace") + numeric("taskReadiness");
  if (agentScope === "provider" || agentScope === "writeback") return "system";
  if (knowledge < 9) return "system";
  if (breakage === "icp") return "icp";
  if (breakage === "handoff" || outcome === "team") return "team";
  return outcome;
}

function updateSteps() {
  steps.forEach((step, index) => step.classList.toggle("is-active", index === currentStep));
  prevButton.disabled = currentStep === 0;
  nextButton.textContent = currentStep === steps.length - 1 ? "Show Result" : "Next";
  stepLabel.textContent = `Step ${currentStep + 1} of ${steps.length}`;
  progressFill.style.width = `${((currentStep + 1) / steps.length) * 100}%`;
  result.hidden = true;
}

function renderResult() {
  const key = recommendation();
  const item = recommendationCopy[key] || recommendationCopy.prd;
  const sourceCount = scoreSources();
  const knowledge = numeric("sourceLabels") + numeric("decisionTrace") + numeric("taskReadiness");
  const providerGate = formValue("agentScope") === "provider" || formValue("agentScope") === "writeback";
  resultTitle.textContent = item.title;
  resultCopy.textContent = item.copy;
  resultStack.innerHTML = [
    ["Source coverage", `${sourceCount}/4 areas selected`],
    ["Knowledge readiness", `${knowledge}/15`],
    ["Automation boundary", providerGate ? "Approval and server-side bridge required" : "Safe for draft/review workflow"],
    ["Next artifact", key === "system" ? "Control-system map" : "Source-backed delivery packet"]
  ]
    .map(([label, value]) => `<div><span>${label}</span><strong>${value}</strong></div>`)
    .join("");
  result.hidden = false;
  result.scrollIntoView({ behavior: "smooth", block: "start" });
}

nextButton.addEventListener("click", () => {
  if (currentStep < steps.length - 1) {
    currentStep += 1;
    updateSteps();
    return;
  }
  renderResult();
});

prevButton.addEventListener("click", () => {
  currentStep = Math.max(0, currentStep - 1);
  updateSteps();
});

const params = new URLSearchParams(window.location.search);
const requestedStep = Number(params.get("step"));
if (Number.isFinite(requestedStep) && requestedStep >= 1 && requestedStep <= steps.length) {
  currentStep = requestedStep - 1;
}

updateSteps();
