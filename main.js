const clamp = (value, min, max) => Math.min(Math.max(value, min), max);

if (new URLSearchParams(window.location.search).has("figma")) {
  document.documentElement.dataset.captureMode = "full";
}

const euro = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "EUR",
  maximumFractionDigits: 0
});

const packageRecommendations = {
  prd: "Recommended first package: source-backed PRD and task matrix.",
  icp: "Recommended first package: ICP evidence review and buyer logic brief.",
  kb: "Recommended first package: knowledgebase readiness and source-boundary cleanup.",
  agent: "Recommended first package: governed agent-orchestra setup plan."
};

function setupHeader() {
  const header = document.querySelector("[data-site-header]");
  const navToggle = document.querySelector(".nav-toggle");
  const mobileNav = document.querySelector("#mobileNav");
  if (header) {
    const update = () => header.classList.toggle("is-scrolled", window.scrollY > 12);
    window.addEventListener("scroll", update, { passive: true });
    update();
  }

  navToggle?.addEventListener("click", () => {
    const open = navToggle.getAttribute("aria-expanded") === "true";
    navToggle.setAttribute("aria-expanded", String(!open));
    mobileNav?.classList.toggle("is-open", !open);
  });

  mobileNav?.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      navToggle?.setAttribute("aria-expanded", "false");
      mobileNav.classList.remove("is-open");
    });
  });
}

function setupMapMotion() {
  const map = document.querySelector("[data-system-map]");
  if (!map || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  map.addEventListener("pointermove", (event) => {
    const rect = map.getBoundingClientRect();
    const x = (event.clientX - rect.left) / Math.max(rect.width, 1) - 0.5;
    const y = (event.clientY - rect.top) / Math.max(rect.height, 1) - 0.5;
    map.style.setProperty("--map-x", `${(x * 12).toFixed(2)}px`);
    map.style.setProperty("--map-y", `${(y * 8).toFixed(2)}px`);
  });

  map.addEventListener("pointerleave", () => {
    map.style.setProperty("--map-x", "0px");
    map.style.setProperty("--map-y", "0px");
  });
}

function setupMiniCalculator() {
  const form = document.querySelector("[data-mini-calc]");
  const output = document.querySelector("[data-calc-output]");
  const modeLabel = document.querySelector("[data-calc-mode-label]");
  const monthly = document.querySelector("[data-calc-monthly]");
  const yearly = document.querySelector("[data-calc-yearly]");
  const payback = document.querySelector("[data-calc-payback]");
  const readinessOutput = document.querySelector("[data-calc-readiness]");
  if (!form || !output || !modeLabel || !monthly || !yearly || !payback || !readinessOutput) return;

  const rangeOutputs = {
    productPeople: (value) => `${value} people`,
    weeklyHours: (value) => `${value} hours`,
    hourlyCost: (value) => euro.format(value),
    wasteShare: (value) => `${value}%`,
    recoverableShare: (value) => `${value}%`,
    setupCost: (value) => euro.format(value),
    sourceCentralization: (value) => `${value} / 10`,
    approvalMaturity: (value) => `${value} / 10`
  };

  function update() {
    const formData = new FormData(form);
    const mode = String(formData.get("mode") || "roi");
    const productPeople = Number(formData.get("productPeople") || 7);
    const weeklyHours = Number(formData.get("weeklyHours") || 48);
    const hourlyCost = Number(formData.get("hourlyCost") || 95);
    const wasteShare = Number(formData.get("wasteShare") || 28);
    const recoverableShare = Number(formData.get("recoverableShare") || 35);
    const setupCost = Number(formData.get("setupCost") || 15000);
    const sourceCentralization = Number(formData.get("sourceCentralization") || 5);
    const approvalMaturity = Number(formData.get("approvalMaturity") || 6);

    Object.entries(rangeOutputs).forEach(([name, formatter]) => {
      const field = form.elements[name];
      const target = form.querySelector(`[data-range-output="${name}"]`);
      if (field && target) target.textContent = formatter(Number(field.value));
    });

    const monthlyLost = weeklyHours * 4.33 * hourlyCost * (wasteShare / 100);
    const monthlyRecovered = monthlyLost * (recoverableShare / 100);
    const yearlyRecovered = monthlyRecovered * 12;
    const paybackMonths = monthlyRecovered > 0 ? setupCost / monthlyRecovered : 0;
    const scalePenalty = productPeople > 14 ? 4 : productPeople > 8 ? 1 : 0;
    const kbReadiness = clamp(
      Math.round(sourceCentralization * 4.2 + approvalMaturity * 3.4 + (100 - wasteShare) * 0.16 + recoverableShare * 0.12 - scalePenalty),
      18,
      96
    );

    let packageKey = "prd";
    if (sourceCentralization <= 4 || kbReadiness < 50) packageKey = "kb";
    else if (approvalMaturity <= 4 || productPeople >= 14) packageKey = "agent";
    else if (wasteShare < 22 && recoverableShare < 28) packageKey = "icp";

    monthly.textContent = euro.format(monthlyRecovered);
    yearly.textContent = euro.format(yearlyRecovered);
    payback.textContent = paybackMonths > 0 ? `${Math.max(1, Math.round(paybackMonths))} mo` : "Needs scoping";
    readinessOutput.textContent = `${kbReadiness} / 100`;
    modeLabel.textContent = mode === "readiness" ? "Knowledgebase readiness estimate" : "PRD/ICP ROI planning estimate";
    output.value =
      mode === "readiness"
        ? `${packageRecommendations[packageKey]} KB readiness is ${kbReadiness}/100; raise source centralization and approval maturity before provider-backed automation.`
        : `${packageRecommendations[packageKey]} Estimated recoverable product-work value is ${euro.format(monthlyRecovered)} per month before implementation proof.`;
  }

  form.addEventListener("input", update);
  form.addEventListener("change", update);
  update();
}

function setupReveal() {
  const items = [...document.querySelectorAll(".hero-copy, .hero-system, .output-card, .lane-card, .timeline li")];
  if (!items.length || !("IntersectionObserver" in window) || document.documentElement.dataset.captureMode === "full") {
    items.forEach((item) => item.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
  );

  items.forEach((item) => observer.observe(item));
}

document.addEventListener("DOMContentLoaded", () => {
  setupHeader();
  setupMapMotion();
  setupMiniCalculator();
  setupReveal();
});
