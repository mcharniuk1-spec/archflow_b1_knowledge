const clamp = (value, min, max) => Math.min(Math.max(value, min), max);

if (new URLSearchParams(window.location.search).has("figma")) {
  document.documentElement.dataset.captureMode = "full";
}

const packageRecommendations = [
  "Recommended first package: PRD rescue and evidence map.",
  "Recommended first package: ICP evidence review and positioning brief.",
  "Recommended first package: knowledgebase readiness and task matrix.",
  "Recommended first package: governed agent-orchestra setup plan."
];

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
  const score = document.querySelector("[data-calc-score]");
  if (!form || !output || !score) return;

  function update() {
    const formData = new FormData(form);
    const sources = Number(formData.get("sources") || 3);
    const decisions = Number(formData.get("decisions") || 2);
    const pressure = Number(formData.get("pressure") || 4);
    const sourceReadiness = sources * 14;
    const decisionReadiness = decisions * 13;
    const pressurePenalty = (6 - pressure) * 4;
    const readiness = clamp(Math.round(sourceReadiness + decisionReadiness + pressurePenalty), 18, 96);
    const knowledgeGap = 6 - Math.round((sources + decisions) / 2);
    const index = clamp(Math.round((knowledgeGap + pressure - 2) / 2), 0, packageRecommendations.length - 1);

    score.textContent = `Readiness index: ${readiness} / 100`;
    output.value = packageRecommendations[index];
  }

  form.addEventListener("input", update);
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
