const tabs = [
  { id: "jarvis", label: "Jarvis", glyph: "JV" },
  { id: "history", label: "Chat History", glyph: "CH" },
  { id: "service", label: "(1) PRD/ICP Flow", glyph: "P1" },
  { id: "schema", label: "(2) Agent Orchestra", glyph: "A2" },
  { id: "config", label: "Config", glyph: "CF" },
  { id: "plan", label: "Project Plan", glyph: "PL" },
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
  voiceOutput: "archflow.jarvis.voiceOutput",
  promptConfig: "archflow.jarvis.promptConfig",
  chatHistory: "archflow.jarvis.chatHistory",
  blockSchema: "archflow.jarvis.blockSchema",
  serviceBlockSchema: "archflow.jarvis.serviceBlockSchema",
  schemaZoom: "archflow.jarvis.schemaZoom",
  roleConfig: "archflow.jarvis.roleConfig",
  prdComposer: "archflow.jarvis.prdComposer",
  voiceTranscriptPreview: "archflow.jarvis.voiceTranscriptPreview",
  autoSpeak: "archflow.jarvis.autoSpeak",
  packets: "archflow.jarvis.localPackets",
  events: "archflow.jarvis.events",
  architectureMode: "archflow.jarvis.architectureMode",
  interviewState: "archflow.jarvis.interviewState",
  apiBase: "archflow.jarvis.apiBase",
};

const blockSchemaVersion = "0.5";

let dashboardData = null;
let activeTab = window.location.hash?.replace(/^#/, "") || "jarvis";
let jarvisMode = localStorage.getItem(storageKeys.mode) || "normal";
let architectureMode = localStorage.getItem(storageKeys.architectureMode) || "service";
const voiceModeDisabled = true;
localStorage.removeItem(storageKeys.voiceAuthorized);
localStorage.removeItem(storageKeys.voiceOutput);
localStorage.removeItem(storageKeys.autoSpeak);
localStorage.removeItem(storageKeys.voiceTranscriptPreview);
let voiceAuthorized = false;
let voiceOutputEnabled = false;
let autoSpeakEnabled = false;
let dataSignature = "";
let refreshTimer = null;
let localPackets = loadJson(storageKeys.packets, []);
let roleConfigs = loadJson(storageKeys.roleConfig, defaultRoleConfigs());
let prdComposerDraft = localStorage.getItem(storageKeys.prdComposer) || "";
let blockSchemas = {
  service: loadBlockSchemaFromStorage(storageKeys.serviceBlockSchema, defaultServiceBlockSchema(), "service"),
  control: loadBlockSchemaFromStorage(storageKeys.blockSchema, defaultBlockSchema(), "control"),
};
let blockSchema = blockSchemas.control;
let schemaZoom = clamp(Number(localStorage.getItem(storageKeys.schemaZoom) || 1), 0.55, 1.35);
let blockSchemaConnectSource = null;
let blockSchemaDrag = null;
let blockSchemaDragMoved = false;
let nodeControlPanelId = null;
let initialPanelDeepLinkApplied = false;
const initialPanelDeepLinkId = new URLSearchParams(window.location.search).get("panel");
let voiceFallbackDraft = "";
let voiceTranscriptPreview = "";
let interviewState = loadJson(storageKeys.interviewState, defaultInterviewState());
let activeRecognition = null;
let voiceTimerId = null;
let voiceStartedAt = null;
let voiceElapsedSeconds = 0;
let jarvisApiBase = (localStorage.getItem(storageKeys.apiBase) || defaultJarvisApiBase()).replace(/\/+$/, "");
let apiHealthTimer = null;
let jarvisApiState = {
  status: "checking",
  label: "Jarvis API checking",
  detail: "Local Jarvis API has not been checked yet.",
  tone: "warn",
};
let pendingAttachments = [];
migratePersistentChatHistory();
let chatHistory = loadJson(storageKeys.chatHistory, [
  {
    id: "welcome",
    role: "assistant",
    source: "system",
    time: new Date().toISOString(),
    text: "Jarvis is ready in text chat mode. Ask for status, PRD/ICP work, agent orchestration, file review packets, or API checks. Writes stay approval-gated.",
  },
]);
let liveEvents = loadJson(storageKeys.events, [
  {
    id: "boot",
    time: new Date().toISOString(),
    title: "Dashboard opened",
    detail: "Static Vercel-ready shell. API and Railway writeback are staged.",
    tone: "ok",
  },
]);

const view = document.querySelector("#view");
const nav = document.querySelector("#nav");
const generatedAt = document.querySelector("#generatedAt");
const liveStatus = document.querySelector("#liveStatus");
const apiStatus = document.querySelector("#apiStatus");
const refreshDataButton = document.querySelector("#refreshData");
const globalComposer = document.querySelector("#globalComposer");
const globalInput = document.querySelector("#globalInput");

if (!tabs.some((tab) => tab.id === activeTab)) activeTab = "jarvis";
if (activeTab === "service") architectureMode = "service";
if (activeTab === "schema") architectureMode = "control";
localStorage.setItem(storageKeys.architectureMode, architectureMode);

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

function migratePersistentChatHistory() {
  if (localStorage.getItem(storageKeys.chatHistory)) return;
  const legacy = sessionStorage.getItem(storageKeys.chatHistory);
  if (legacy) localStorage.setItem(storageKeys.chatHistory, legacy);
}

function clamp(value, min, max) {
  const numeric = Number.isFinite(value) ? value : min;
  return Math.min(max, Math.max(min, numeric));
}

function defaultJarvisApiBase() {
  const localHostnames = new Set(["127.0.0.1", "localhost", "0.0.0.0"]);
  if (localHostnames.has(window.location.hostname)) return "http://127.0.0.1:8787";
  return window.location.origin;
}

function defaultPromptConfig() {
  return {
    chain_name: "PRD-to-ICP dashboard chain",
    model_policy: "MODEL_PROVIDER=none by default. OpenAI, OpenRouter, or Mistral keys may exist only in ignored local/service env files; static browser code must not read or call provider keys.",
    memory_policy: "Summaries and candidates only; no raw transcript, raw recording, or private document persistence by default.",
    normal_prompt: "Answer from verified dashboard state, explain blockers, prepare approval packets, and avoid scope expansion.",
    interview_prompt: "Ask one question at a time, classify answers as fact, preference, hypothesis, gap, decision, or task candidate.",
    review_prompt: "Check public/private boundary, source links, owner approval, and whether claims are backed by current files.",
  };
}

let promptConfig = loadJson(storageKeys.promptConfig, defaultPromptConfig());

function defaultInterviewState() {
  return {
    active: false,
    questionIndex: 0,
    lane: "service",
    answers: [],
    lastSummary: "",
  };
}

function architectureMeta(mode = architectureMode) {
  return mode === "control"
    ? {
        id: "control",
        short: "Architecture 2",
        label: "Architecture 2 - Agent Control",
        tab: "schema",
        schemaKind: "control",
        commandBias: "agent orchestra, architecture change, logs, WikiLLM, Graphify, LlamaIndex, LangGraph, approvals, and durable output control",
        firstInterviewQuestion: "Architecture 2 selected. What system-level change, agent workflow, memory/logging decision, or dashboard-control outcome should Jarvis help structure first?",
      }
    : {
        id: "service",
        short: "Architecture 1",
        label: "Architecture 1 - PRD Service",
        tab: "service",
        schemaKind: "service",
        commandBias: "source-to-PRD service output, discovery synthesis, ICP evidence, backlog, and buyer-ready reporting",
        firstInterviewQuestion: "Architecture 1 selected. What source material should become the next PRD/ICP packet, and what buyer or product-team decision should it support?",
      };
}

function setArchitectureMode(mode, options = {}) {
  architectureMode = mode === "control" ? "control" : "service";
  localStorage.setItem(storageKeys.architectureMode, architectureMode);
  const meta = architectureMeta();
  if (options.switchTab) activeTab = meta.tab;
  appendEvent("Architecture selected", `${meta.label}. Commands now bias toward ${meta.commandBias}.`, "ok");
}

const interviewQuestions = {
  service: [
    "What source material should become the next PRD/ICP packet, and what buyer or product-team decision should it support?",
    "Who is the intended reviewer or buyer for this output, and what decision should they be able to make after reading it?",
    "What evidence is approved for use, and what raw source material must stay excluded from public or provider-backed processing?",
    "What final outputs are expected: PRD, task matrix, ICP card, evidence map, report, PDF, or backlog?",
    "What would make the output ready for review rather than still needing owner approval?",
  ],
  control: [
    "What system-level change, agent workflow, memory/logging decision, or dashboard-control outcome should Jarvis help structure first?",
    "Which architecture layer is affected: Codex operator, LangGraph route, LlamaIndex retrieval, Graphify map, WikiLLM memory, dashboard UI, backend API, or Railway?",
    "Which durable writes or external actions require approval before execution?",
    "What logs, run notes, decisions, or proof artifacts must be created so the change is auditable?",
    "What validation proves the architecture change is controlled and reversible?",
  ],
};

function currentInterviewQuestion() {
  const lane = interviewState.lane === "control" ? "control" : "service";
  const questions = interviewQuestions[lane];
  return questions[Math.min(interviewState.questionIndex, questions.length - 1)];
}

const schemaScreenMeta = {
  service: {
    title: "(1) PRD/ICP Service Product Flow",
    subtitle: "Externally showable product path: source context into PRD, market evidence, ICP profile, demo package, and approval-ready client output.",
    resetEvent: "Local schema reset to the PRD/ICP service product graph.",
    packetInput: "Export current PRD/ICP service product graph for Codex review.",
  },
  control: {
    title: "(2) Reliable Agent Orchestra",
    subtitle: "Local control system: Codex, LangGraph-style routing, WikiLLM, Graphify, safety review, run logs, approvals, and gated backend/provider actions.",
    resetEvent: "Local schema reset to the reliable agent orchestra graph.",
    packetInput: "Export current reliable agent orchestra graph for Codex review.",
  },
};

function schemaKindForActiveTab() {
  return architectureMeta().schemaKind;
}

function setActiveSchema() {
  const kind = schemaKindForActiveTab();
  blockSchema = blockSchemas[kind];
  if (!blockSchema.nodes.some((node) => node.id === nodeControlPanelId)) nodeControlPanelId = null;
  if (!blockSchema.nodes.some((node) => node.id === blockSchemaConnectSource)) blockSchemaConnectSource = null;
  return kind;
}

function applyInitialPanelDeepLink() {
  if (initialPanelDeepLinkApplied || !initialPanelDeepLinkId) return;
  initialPanelDeepLinkApplied = true;
  const node = getSchemaNode(initialPanelDeepLinkId);
  if (!node) return;
  blockSchema.selectedNodeId = node.id;
  nodeControlPanelId = node.id;
}

function storedSchemaMatchesCurrentDefault(schema, kind) {
  if (!schema || schema.version !== blockSchemaVersion || !Array.isArray(schema.nodes)) return false;
  const ids = new Set(schema.nodes.map((node) => node.id));
  const requiredIds = kind === "service"
    ? ["svc-intake", "svc-output"]
    : ["intake", "architecture-review", "output"];
  return requiredIds.every((id) => ids.has(id));
}

function loadBlockSchemaFromStorage(key, fallback, kind) {
  const stored = loadJson(key, null);
  if (!storedSchemaMatchesCurrentDefault(stored, kind)) return normalizeBlockSchema(fallback, kind);
  return normalizeBlockSchema(stored, kind);
}

function configOptions() {
  return {
    workflowLayer: ["service product", "control system", "safety review", "knowledge/RAG", "approval gate", "publishing"],
    modelProvider: ["none", "Codex local operator", "OpenRouter gated", "Mistral gated", "OpenAI disabled", "Ollama local gated", "NVIDIA safety gated"],
    providerMode: ["disabled", "configured locally", "approval required", "sandbox test only", "blocked"],
    executionMode: ["manual review", "queued for Codex", "LangGraph planned", "browser local only", "backend required"],
    approvalGate: ["required before durable write", "required before provider call", "required before external send", "not applicable"],
    memoryTarget: ["none", "download packet", "run note candidate", "WikiLLM candidate", "Obsidian candidate", "Notion candidate"],
    retrievalScope: ["approved public files", "project run notes", "dashboard data JSON", "manual user packet", "blocked private raw data"],
    traceTarget: ["dashboard packet", "LangGraph metadata", "LangSmith trace URL placeholder", "CrewAI handoff", "not traced"],
    safetyReview: ["public safety scan", "manual source review", "NVIDIA garak planned", "NeMo Guardrails planned", "blocked until approved"],
    persistence: ["session storage", "localStorage", "download only", "Git after Codex review", "backend database gated"],
    inputConnector: ["manual command packet", "browser chat", "file metadata only", "approved corpus", "agent handoff", "none"],
    outputConnector: ["downloadable review packet", "dashboard run note", "PRD artifact", "ICP evidence card", "approval request", "blocked issue"],
    runRecorder: ["browser session log", "public-safe run note", "LangSmith URL placeholder", "agent handoff", "not recorded"],
  };
}

function defaultNodeConfig(type, workflowLayer) {
  return {
    workflowLayer,
    modelProvider: "none",
    providerMode: "disabled",
    executionMode: type === "output" ? "queued for Codex" : "manual review",
    approvalGate: ["approval", "output"].includes(type) ? "required before durable write" : "not applicable",
    memoryTarget: type === "output" ? "run note candidate" : "download packet",
    retrievalScope: "approved public files",
    traceTarget: ["router", "parallel", "merge"].includes(type) ? "LangGraph metadata" : "dashboard packet",
    safetyReview: "public safety scan",
    persistence: "download only",
    inputConnector: "manual command packet",
    outputConnector: type === "output" ? "dashboard run note" : "downloadable review packet",
    runRecorder: "browser session log",
  };
}

function defaultBlockSchema() {
  return defaultControlBlockSchema();
}

function defaultServiceBlockSchema() {
  return {
    version: blockSchemaVersion,
    title: "PRD/ICP Service Product Graph",
    selectedNodeId: "svc-intake",
    connectSourceId: null,
    queue: [],
    nodes: [
      schemaNode("svc-intake", "start", "Client source intake", 60, 120, "Jarvis intake", "Capture dialogue, meeting summary, file metadata, product context, and explicit constraints.", "Sanitized source packet for PRD creation.", {
        workflowLayer: "service product",
        job: "Turn unstructured product-team context into usable source material.",
        pain: "Product teams lose decisions and context across meetings, chats, and docs.",
        evidence: "Current Block 1 proof and E1.3 readback show the source-to-KB path is the first reliable wedge.",
        businessObjective: "Create an externally showable PRD/ICP service path without exposing private raw material.",
        inputs: ["typed brief", "meeting summary", "file metadata only", "approved public examples"],
        outputs: ["sanitized source packet", "missing-context questions"],
        systemPrompt: "Classify every input as fact, assumption, hypothesis, gap, decision, or task candidate. Do not store raw private transcripts."
      }),
      schemaNode("svc-prd", "agent", "PRD builder", 350, 72, "Manager/PRD agent", "Convert accepted context into PRD sections, responsibilities, acceptance criteria, and open questions.", "Draft PRD with source labels and gaps.", {
        workflowLayer: "service product",
        job: "Produce a decision-ready PRD faster than a product team can assemble by hand.",
        pain: "PRDs become inconsistent when product, engineering, and leadership context are scattered.",
        evidence: "June 24 reset defines dialogue/chat/meeting material into PRD and agent-ready KB as Block 1.",
        businessObjective: "Prove paid value through a Product Discovery-to-Production PRD Pack.",
        inputs: ["sanitized source packet", "product constraints", "acceptance criteria"],
        outputs: ["PRD draft", "task/responsibility matrix", "gap list"]
      }),
      schemaNode("svc-research-fork", "parallel", "Market evidence fork", 650, 100, "Research lead", "Split research into ICP evidence, competitor signals, customer pain, and offer-risk checks.", "Parallel evidence packets with weak claims marked as gaps.", {
        workflowLayer: "service product",
        job: "Ground the PRD in market and customer evidence before external positioning.",
        pain: "Teams often mistake internal enthusiasm or social signals for validated demand.",
        evidence: "E2 is defined as bounded evidence engine after E1.3 KB/readback.",
        businessObjective: "Reduce false-positive ICP claims before outreach.",
        inputs: ["PRD draft", "current ICP lane", "approved research sources"],
        outputs: ["ICP evidence cards", "competitor notes", "risk flags"]
      }),
      schemaNode("svc-evidence", "agent", "ICP evidence cards", 950, 30, "Research/ICP agent", "Create source-labeled account, role, pain, trigger, and disqualifier evidence cards for the one current ICP lane.", "Source-labeled evidence cards.", {
        workflowLayer: "service product",
        job: "Prove whether the target buyer and account shape are credible.",
        pain: "ICP choices become weak when they rely on generic market claims.",
        evidence: "E2 requires source grades, account evidence cards, and role verification.",
        businessObjective: "Give the service product a defensible ICP basis.",
        inputs: ["PRD draft", "approved research sources", "source-grade rules"],
        outputs: ["evidence cards", "source grades", "disqualifiers"]
      }),
      schemaNode("svc-pain", "agent", "Customer pain review", 950, 260, "Product marketing agent", "Translate PRD and market evidence into buyer jobs, pains, objections, proof needs, and demo-message requirements.", "Buyer pain and messaging packet.", {
        workflowLayer: "service product",
        job: "Connect the service output to what the buyer needs to decide.",
        pain: "A technically good PRD pack may still fail if it does not map to buyer urgency.",
        evidence: "Reviewer instructions require feature recommendations tied to user job, pain, evidence, and business objective.",
        businessObjective: "Improve conversion readiness before E3/E4/E6.",
        inputs: ["PRD draft", "evidence cards", "offer-risk checks"],
        outputs: ["JTBD notes", "objections", "demo requirements"]
      }),
      schemaNode("svc-research-merge", "merge", "Evidence merge", 1260, 140, "Lead integrator", "Merge ICP evidence and customer-pain packets, preserving contradictions as gaps.", "Merged market evidence packet.", {
        workflowLayer: "service product",
        job: "Make research usable for a decision rather than scattered branch reports.",
        pain: "Parallel research can produce contradictory claims if no integrator resolves them.",
        evidence: "The block-schema contract requires merge rules after parallel execution.",
        businessObjective: "Move only reviewed evidence into ICP synthesis.",
        inputs: ["evidence cards", "buyer pain packet"],
        outputs: ["merged evidence packet", "contradiction list"]
      }),
      schemaNode("svc-icp", "agent", "ICP synthesis", 1570, 52, "Research/ICP agent", "Turn evidence packets into one current ICP profile, buying job, pains, triggers, and disqualifiers.", "Single ICP profile with confidence and blockers.", {
        workflowLayer: "service product",
        job: "Help the marketing/sales path know exactly who the offer is for.",
        pain: "Multiple ICP lanes dilute the first commercial test.",
        evidence: "Current strategy keeps one primary ICP unless explicitly widened.",
        businessObjective: "Focus E3/E4/E6 around a single first lane.",
        inputs: ["evidence cards", "PRD gaps", "source grades"],
        outputs: ["ICP profile", "audience language", "open evidence gaps"]
      }),
      schemaNode("svc-demo", "agent", "Landing/demo package", 1870, 86, "Product marketing agent", "Create demo flow, landing structure, offer language, proof cards, and content angles from accepted ICP/PRD evidence.", "Externally showable demo package for review.", {
        workflowLayer: "service product",
        job: "Show the product-team buyer the outcome, not the internal machinery.",
        pain: "Early buyers need clear output examples and proof, not architecture diagrams.",
        evidence: "E3/E4 depend on accepted PRD/ICP evidence before content and positioning.",
        businessObjective: "Move from internal proof to a firm paid-start conversation.",
        inputs: ["ICP profile", "PRD draft", "proof cards"],
        outputs: ["landing outline", "demo script", "content angles"]
      }),
      schemaNode("svc-crewai-proof", "agent", "CrewAI Level 3 proof", 2180, 286, "AF Manager + AF Review", "Run one tiny public-safe PRD/ICP fixture through direct CrewAI deterministic local runtime with no provider calls and no writeback.", "Proof packet: proof_passed_not_default_runtime.", {
        workflowLayer: "runtime proof",
        job: "Show that direct CrewAI can execute the PRD/ICP fixture without becoming the default runtime.",
        pain: "Level 3 was blocked by missing proof, not by rejection of CrewAI.",
        evidence: "project/runs/2026-07-02-crewai-level-3-proof/runtime-proof.json",
        businessObjective: "Make the runtime readiness path visible while keeping provider/default promotion gated.",
        inputs: ["tiny public-safe PRD/ICP fixture", "budget guard", "model-call ledger schema", "CrewAI config"],
        outputs: ["crew output", "model-call ledger", "budget guard", "AF Review report", "runtime proof"],
        config: {
          modelProvider: "local deterministic",
          providerMode: "OpenRouter disabled",
          executionMode: "direct CrewAI proof only",
          persistence: "run artifact only",
          approvalGate: "proof passed; default/provider runtime still requires owner approval",
          outputConnector: "project/runs/2026-07-02-crewai-level-3-proof/runtime-proof.json"
        },
        lastRuns: [{
          time: "2026-07-02",
          status: "proof_passed_not_default_runtime",
          summary: "Direct CrewAI fixture run completed with zero provider calls, zero writeback, and 0.00 USD spend."
        }]
      }),
      schemaNode("svc-approval", "approval", "Client-output approval", 2490, 120, "Owner approval", "Approve what can be shown externally and what must remain internal or blocked.", "Approved service output or blocked issue.", {
        workflowLayer: "approval gate",
        job: "Prevent unverified claims and private context from reaching external surfaces.",
        pain: "Public-facing assets can overclaim if generated from partial internal notes.",
        evidence: "Public-safety gate requires source labels and approved claims.",
        businessObjective: "Keep demo-ready output credible and safe.",
        inputs: ["demo package", "CrewAI proof state", "safety review", "source labels"],
        outputs: ["approval packet", "blocked issue", "revision request"]
      }),
      schemaNode("svc-output", "output", "Service output packet", 2800, 120, "Publisher", "Package PRD, ICP, demo, next tasks, and confidence level for review or buyer-facing use.", "Linked service packet with confidence level.", {
        workflowLayer: "publishing",
        job: "Create the final artifact the buyer or internal reviewer can inspect.",
        pain: "Work is not done when it exists only in chat.",
        evidence: "Run notes and dashboard data make proof retrievable.",
        businessObjective: "Turn execution into reusable sales and delivery proof.",
        inputs: ["approved output", "run note", "evidence links"],
        outputs: ["PRD/ICP packet", "task list", "confidence rating"]
      })
    ],
    edges: [
      schemaEdge("svc-e1", "svc-intake", "svc-prd", "source packet", "Source context is sanitized and classified.", "normal"),
      schemaEdge("svc-e2", "svc-prd", "svc-research-fork", "PRD ready", "PRD has enough detail for evidence checks.", "parallel"),
      schemaEdge("svc-e3", "svc-research-fork", "svc-evidence", "ICP evidence branch", "Research branch checks source-labeled ICP/account evidence.", "parallel"),
      schemaEdge("svc-e4", "svc-research-fork", "svc-pain", "buyer pain branch", "Research branch checks jobs, pains, objections, and demo proof needs.", "parallel"),
      schemaEdge("svc-e5", "svc-evidence", "svc-research-merge", "evidence cards", "Evidence branch returns source grades and disqualifiers.", "merge"),
      schemaEdge("svc-e6", "svc-pain", "svc-research-merge", "pain packet", "Pain branch returns buyer language and objections.", "merge"),
      schemaEdge("svc-e7", "svc-research-merge", "svc-icp", "merged evidence", "Contradictions are marked as gaps before synthesis.", "normal"),
      schemaEdge("svc-e8", "svc-icp", "svc-demo", "ICP accepted", "One ICP lane is coherent enough for positioning.", "normal"),
      schemaEdge("svc-e9", "svc-demo", "svc-crewai-proof", "runtime proof", "Direct CrewAI may prove the fixture but cannot promote itself to default runtime.", "conditional"),
      schemaEdge("svc-e10", "svc-crewai-proof", "svc-approval", "proof reviewed", "AF Review verifies proof artifacts before owner approval.", "approval"),
      schemaEdge("svc-e11", "svc-approval", "svc-output", "approved", "Owner approves external-safe output.", "normal")
    ]
  };
}

function defaultControlBlockSchema() {
  return {
    version: blockSchemaVersion,
    title: "Reliable Agent Orchestra Graph",
    selectedNodeId: "intake",
    connectSourceId: null,
    queue: [],
    nodes: [
      schemaNode("intake", "start", "Operator command intake", 60, 80, "Owner + Jarvis", "Capture typed command, file attachment summary, correction, or approval.", "One sanitized command packet; audio and raw transcript paths stay off.", {
        workflowLayer: "control system",
        job: "Let the owner direct local execution without losing state.",
        pain: "Agent work becomes unreliable when commands, approvals, and blockers stay only in chat.",
        evidence: "June 30 dashboard branch proved session-local Jarvis packets and block-schema editing.",
        businessObjective: "Make the local agentic operating system observable and controllable.",
        inputs: ["typed command", "file attachment summary", "file metadata", "approval state"],
        outputs: ["sanitized command packet", "local event log"]
      }),
      schemaNode("classify", "router", "Classify request", 350, 80, "Jarvis router", "Separate status, interview, research, config, block-schema, and approval requests.", "Route key plus fact/interpretation/hypothesis/gap label.", {
        workflowLayer: "control system",
        job: "Route work to the right local execution lane.",
        pain: "Dashboards become confusing when product work, code work, memory, and publishing share one screen.",
        evidence: "Reviewer instructions require an explicit split between PRD/ICP service product and reliable control system.",
        businessObjective: "Reduce wrong-lane execution and overclaiming.",
        inputs: ["command packet", "current dashboard state"],
        outputs: ["route key", "evidence label", "stop condition"]
      }),
      schemaNode("codex", "agent", "Codex development response", 650, 54, "Codex operator", "Read current files, edit review branch only, run checks, and report evidence.", "Reviewed branch diff and local run note.", {
        workflowLayer: "control system",
        job: "Implement and verify local changes under approval boundaries.",
        pain: "A web dashboard cannot safely mutate Git, Notion, or memory by itself.",
        evidence: "Codex remains local operator/editor/reviewer; static Vercel remains read-only.",
        businessObjective: "Keep code changes reliable without enabling unsafe browser writeback.",
        inputs: ["route key", "repo files", "agent chat findings"],
        outputs: ["diff", "checks", "run note"]
      }),
      schemaNode("monitor", "agent", "Graph monitor", 650, 270, "LangGraph monitor", "Track state, blockers, approvals, attempts, and branch outputs.", "Trace packet for LangGraph/CrewAI/LangSmith surfaces.", {
        workflowLayer: "control system",
        job: "Show what is running, blocked, or waiting for approval.",
        pain: "Parallel agents are hard to trust when their state is not visible.",
        evidence: "The coordination contract requires chat files, registry state, run notes, and verifier status.",
        businessObjective: "Make future LangGraph execution explainable before it is live.",
        inputs: ["event log", "active route", "validation state"],
        outputs: ["state packet", "trace placeholder", "blocker list"]
      }),
      schemaNode("parallel", "parallel", "Parallel agent fork", 960, 80, "Lead integrator", "Split work across architecture review, safety, stack, product, and delivery lanes.", "Branch reports with contradictions marked as gaps.", {
        workflowLayer: "control system",
        job: "Use focused reviewers without losing merge order.",
        pain: "Uncoordinated agents edit the same surface or approve unsupported claims.",
        evidence: "Parallel-agent protocol requires one integrator and focused sidecar reviewers.",
        businessObjective: "Raise reliability before merge, deploy, or memory promotion.",
        inputs: ["implementation packet", "monitor state"],
        outputs: ["review branches", "findings", "approval blockers"]
      }),
      schemaNode("architecture-review", "agent", "Architecture review", 1260, 40, "Architecture reviewer", "Verify the two-screen architecture, node panel usability, local/offline clarity, and gated provider/writeback boundaries.", "Checker verdict with passed checks and gaps.", {
        workflowLayer: "control system",
        job: "Protect dashboard comprehensibility before final integration.",
        pain: "A powerful graph editor is useless if the operator cannot understand the current layer.",
        evidence: "Delegated review requirements call for two paradigms and node configuration panels.",
        businessObjective: "Get reviewer approval before final handoff.",
        inputs: ["local dashboard route", "diff summary", "safety notes"],
        outputs: ["approval verdict", "required fixes", "final word when satisfied"]
      }),
      schemaNode("safety-review", "agent", "Safety and source review", 1260, 280, "Safety reviewer", "Check public/private boundary, unsupported claims, secrets, third-party repo risk, and source links.", "Safety verdict and required corrections.", {
        workflowLayer: "safety review",
        job: "Prevent unsafe tool installation, secret exposure, and unsupported public claims.",
        pain: "Agent tools can introduce hooks, workers, memory capture, or provider calls.",
        evidence: "Claude-Mem and Impeccable both add hooks/processes; NVIDIA garak/NeMo are evaluation tools, not installed gates here.",
        businessObjective: "Use third-party tools only after scoped onboarding and approval.",
        inputs: ["external repo review", "changed files", "public-safety scan"],
        outputs: ["risk rating", "blocked items", "safe next step"]
      }),
      schemaNode("crewai-proof", "agent", "CrewAI Level 3 direct proof", 1560, 392, "AF Manager + AF Review", "Run or display the direct CrewAI deterministic proof branch; preserve the proof as a runtime-readiness artifact only.", "Reviewed proof packet; not default runtime.", {
        workflowLayer: "runtime proof",
        job: "Represent direct CrewAI readiness inside the operator graph without enabling autonomous/provider execution.",
        pain: "Runtime claims become unsafe when proof, ledger, budget, and review are hidden.",
        evidence: "project/runs/2026-07-02-crewai-level-3-proof/runtime-proof.json",
        businessObjective: "Let the operator see the Level 3 path and remaining gates before promotion.",
        inputs: ["operator task", "public-safe fixture", "budget guard", "ledger path"],
        outputs: ["runtime proof", "review report", "dashboard state"],
        config: {
          modelProvider: "local deterministic",
          providerMode: "provider disabled",
          executionMode: "direct CrewAI proof passed; not default runtime",
          persistence: "repo run artifact",
          approvalGate: "owner approval required for provider/default runtime",
          outputConnector: "project/runs/2026-07-02-crewai-level-3-proof/dashboard-state.md"
        },
        lastRuns: [{
          time: "2026-07-02",
          status: "proof_passed_not_default_runtime",
          summary: "Tiny PRD/ICP fixture produced deterministic CrewAI output, ledger, budget guard, and AF Review packet."
        }]
      }),
      schemaNode("merge", "merge", "Integrator merge", 1860, 160, "Lead integrator", "Merge branch outputs, preserve source links, and reject unsupported claims.", "Single accepted handoff with checks.", {
        workflowLayer: "control system",
        job: "Turn parallel findings into one coherent result.",
        pain: "Separate agent reports can contradict each other or bury blockers.",
        evidence: "The integrator owns merge order, final review, and durable records.",
        businessObjective: "Finish with a verified dashboard state, not scattered chat output.",
        inputs: ["review findings", "safety verdict", "CrewAI proof state", "checks"],
        outputs: ["accepted changes", "remaining gaps", "handoff"]
      }),
      schemaNode("approval", "approval", "Writeback approval", 2160, 160, "Owner approval", "Approve or reject Notion, GitHub, WikiLLM, Telegram, model, capture, or backend writeback.", "Approved packet or blocked issue.", {
        workflowLayer: "approval gate",
        job: "Keep high-impact actions explicit.",
        pain: "Static dashboard actions can look executable even when no safe backend exists.",
        evidence: "Provider calls, raw capture, memory writes, and deploys remain gated.",
        businessObjective: "Prevent unauthorized external or durable state changes.",
        inputs: ["handoff packet", "approval request"],
        outputs: ["approved action", "blocked issue", "revision request"]
      }),
      schemaNode("output", "output", "Durable output", 2460, 160, "Publisher", "Create run note, decision, issue, dashboard data update, or review branch.", "Linked artifact and dashboard status.", {
        workflowLayer: "publishing",
        job: "Make completed work retrievable for the next run.",
        pain: "Work is not complete if the result exists only in chat.",
        evidence: "Public run notes, WikiLLM logs, dashboard data, and handouts are the reliable source layers.",
        businessObjective: "Reduce repeated discovery and failed handoffs.",
        inputs: ["approved packet", "check results"],
        outputs: ["run note", "agent handout", "dashboard data refresh"]
      })
    ],
    edges: [
      schemaEdge("e1", "intake", "classify", "input", "Always after explicit user action.", "normal"),
      schemaEdge("e2", "classify", "codex", "development", "Code or dashboard implementation is requested.", "conditional"),
      schemaEdge("e3", "classify", "monitor", "trace", "Every task emits safe state and blocker metadata.", "conditional"),
      schemaEdge("e4", "codex", "parallel", "review fork", "Implementation needs checker/safety/product review.", "parallel"),
      schemaEdge("e5", "monitor", "parallel", "status fork", "State should be visible to each reviewer.", "parallel"),
      schemaEdge("e6", "parallel", "architecture-review", "architecture branch", "Architecture reviewer validates architecture and UX proof.", "parallel"),
      schemaEdge("e7", "parallel", "safety-review", "safety branch", "Safety reviewer checks public/private and source boundaries.", "parallel"),
      schemaEdge("e12", "parallel", "crewai-proof", "runtime proof branch", "CrewAI proof runs only as deterministic local fixture evidence.", "parallel"),
      schemaEdge("e8", "architecture-review", "merge", "checker verdict", "Architecture reviewer returns facts, gaps, checks, and status.", "merge"),
      schemaEdge("e9", "safety-review", "merge", "safety verdict", "Safety reviewer returns public-safe corrections.", "merge"),
      schemaEdge("e13", "crewai-proof", "merge", "proof state", "Integrator receives proof status and remaining provider/default-runtime gates.", "merge"),
      schemaEdge("e10", "merge", "approval", "needs writeback", "Any durable write, provider, capture, or external send needs approval.", "approval"),
      schemaEdge("e11", "approval", "output", "approved output", "Approved output is recorded and linked.", "normal")
    ]
  };
}

function schemaNode(id, type, title, x, y, owner, prompt, output, options = {}) {
  const workflowLayer = options.workflowLayer || "control system";
  const typeDefaults = schemaNodeTypeDefaults(type, title, output);
  return {
    id,
    type,
    title,
    x,
    y,
    w: options.w || typeDefaults.w,
    h: options.h || typeDefaults.h,
    owner: owner || typeDefaults.owner,
    status: options.status || typeDefaults.status,
    workflowLayer,
    description: options.description || prompt,
    job: options.job || "Define the job this node helps the operator complete.",
    pain: options.pain || "Define the pain or failure this node reduces.",
    evidence: options.evidence || "pending: source evidence assigned during execution",
    businessObjective: options.businessObjective || "Keep execution reliable, explainable, and approval-gated.",
    inputs: options.inputs || typeDefaults.inputs,
    outputs: options.outputs || typeDefaults.outputs,
    prompt,
    systemPrompt: options.systemPrompt || prompt,
    comments: options.comments || typeDefaults.comments,
    requirements: options.requirements || typeDefaults.requirements,
    files: options.files || typeDefaults.files,
    questions: options.questions || typeDefaults.questions,
    possibleOutputs: options.possibleOutputs || typeDefaults.possibleOutputs,
    outputLinks: options.outputLinks || ["pending: created after execution"],
    finalOutput: output,
    lastRuns: options.lastRuns || [
      {
        time: "pending",
        status: "not run",
        summary: "This static dashboard records configuration only until a Codex or backend run writes a public-safe result."
      }
    ],
    config: {
      ...defaultNodeConfig(type, workflowLayer),
      ...typeDefaults.config,
      ...(options.config || {})
    }
  };
}

function schemaNodeTypeDefaults(type, title, output) {
  const base = {
    w: type === "parallel" || type === "router" ? 300 : 260,
    h: type === "parallel" || type === "approval" ? 188 : 168,
    owner: "Unassigned",
    status: "planned",
    inputs: ["manual command packet"],
    outputs: [output || "pending output"],
    comments: "Draft node. Replace with reviewer/operator notes during execution.",
    requirements: "No secrets, raw recordings, raw transcripts, private document bodies, or unapproved provider calls.",
    files: ["pending: assign during execution"],
    questions: [`What does ${title} need to prove?`, "Which source file or artifact supports it?"],
    possibleOutputs: ["run_note", "decision", "issue", "review_branch", "dashboard_packet"],
    config: {},
  };
  if (type === "parallel") {
    return {
      ...base,
      owner: "Lead integrator",
      status: "draft unconnected",
      inputs: ["accepted source packet", "route key", "review criteria"],
      outputs: ["architecture branch brief", "safety branch brief", "product/output branch brief", "merge packet"],
      comments: "Parallel nodes fan out bounded sidecar work. Each branch must return facts, gaps, changed files if any, and a merge recommendation.",
      requirements: "Every branch needs an owner, a disjoint file scope if editing, a stop condition, and a merge target.",
      questions: ["Which branches are needed?", "Which files are reserved by each branch?", "Where does the merge happen?"],
      possibleOutputs: ["branch report", "review finding", "blocked issue", "merge packet"],
      config: {
        traceTarget: "LangGraph metadata",
        approvalGate: "required before durable write",
        outputConnector: "approval request",
      },
    };
  }
  if (type === "approval") {
    return {
      ...base,
      owner: "Owner approval",
      status: "approval gate",
      inputs: ["handoff packet", "evidence links", "risk list", "requested action"],
      outputs: ["approved action", "revision request", "blocked issue"],
      comments: "Approval nodes prevent provider calls, external sends, writeback, deployment, raw capture, or public claims from happening implicitly.",
      requirements: "Define allowed action, forbidden action, evidence required, rollback path, and expiry of approval.",
      questions: ["What exact action is being approved?", "What evidence supports it?", "What remains forbidden?"],
      possibleOutputs: ["approval record", "blocked issue", "revision note", "owner decision"],
      config: {
        approvalGate: "required before provider call",
        persistence: "Git after Codex review",
        outputConnector: "approval request",
      },
    };
  }
  if (type === "router") {
    return {
      ...base,
      owner: "Jarvis router",
      inputs: ["command packet", "current architecture mode", "current task state"],
      outputs: ["route key", "architecture 1 path", "architecture 2 path", "stop condition"],
      comments: "Router nodes classify work before Codex, LangGraph, or review branches act.",
      possibleOutputs: ["route key", "classification", "stop condition"],
      config: {
        traceTarget: "LangGraph metadata",
        outputConnector: "downloadable review packet",
      },
    };
  }
  return base;
}

function schemaEdge(id, from, to, label, condition, mode) {
  return { id, from, to, label, condition, mode };
}

function normalizeBlockSchema(schema, kind = "control") {
  const fallback = kind === "service" ? defaultServiceBlockSchema() : defaultBlockSchema();
  const source = schema && Array.isArray(schema.nodes) && Array.isArray(schema.edges) ? schema : fallback;
  return {
    version: source.version || blockSchemaVersion,
    title: source.title || fallback.title,
    selectedNodeId: source.selectedNodeId || source.nodes?.[0]?.id || null,
    connectSourceId: null,
    queue: Array.isArray(source.queue) ? source.queue : [],
    nodes: source.nodes.map((node) => {
      const normalized = {
        ...schemaNode(node.id || makeId("node"), node.type || "agent", node.title || "Untitled node", Number(node.x) || 80, Number(node.y) || 80, node.owner || "Unassigned", node.prompt || "", node.finalOutput || "Pending output", { workflowLayer: kind === "service" ? "service product" : "control system" }),
        ...node,
      };
      normalized.files = Array.isArray(node.files) ? node.files : String(node.files || "pending: assign during execution").split(/\n+/).filter(Boolean);
      normalized.questions = Array.isArray(node.questions) ? node.questions : String(node.questions || "").split(/\n+/).filter(Boolean);
      normalized.inputs = Array.isArray(node.inputs) ? node.inputs : String(node.inputs || "manual command packet").split(/\n+/).filter(Boolean);
      normalized.outputs = Array.isArray(node.outputs) ? node.outputs : String(node.outputs || normalized.finalOutput || "pending output").split(/\n+/).filter(Boolean);
      normalized.possibleOutputs = Array.isArray(node.possibleOutputs) ? node.possibleOutputs : String(node.possibleOutputs || "").split(/\n+/).filter(Boolean);
      normalized.outputLinks = Array.isArray(node.outputLinks) ? node.outputLinks : String(node.outputLinks || "").split(/\n+/).filter(Boolean);
      normalized.lastRuns = Array.isArray(node.lastRuns) ? node.lastRuns : [{ time: "pending", status: "not run", summary: String(node.lastRuns || "No run history recorded.") }];
      normalized.config = {
        ...defaultNodeConfig(normalized.type, normalized.workflowLayer || (kind === "service" ? "service product" : "control system")),
        ...(typeof node.config === "object" && node.config ? node.config : {})
      };
      normalized.description = normalized.description || normalized.prompt || "No description configured.";
      normalized.systemPrompt = normalized.systemPrompt || normalized.prompt || "";
      return normalized;
    }),
    edges: source.edges.map((edge) => ({ ...schemaEdge(edge.id || makeId("edge"), edge.from, edge.to, edge.label || "next", edge.condition || "", edge.mode || "normal"), ...edge }))
  };
}

function saveBlockSchema() {
  const kind = schemaKindForActiveTab();
  blockSchemas[kind] = blockSchema;
  saveJson(kind === "service" ? storageKeys.serviceBlockSchema : storageKeys.blockSchema, blockSchema);
}

function getSchemaNode(id) {
  return blockSchema.nodes.find((node) => node.id === id);
}

function getSchemaEdge(id) {
  return blockSchema.edges.find((edge) => edge.id === id);
}

function outgoingSchemaEdges(id) {
  return blockSchema.edges.filter((edge) => edge.from === id);
}

function incomingSchemaEdges(id) {
  return blockSchema.edges.filter((edge) => edge.to === id);
}

function listFromTextarea(value) {
  return String(value || "").split(/\r?\n/).map((line) => line.trim()).filter(Boolean);
}

function textareaFromList(value) {
  return Array.isArray(value) ? value.join("\n") : "";
}

function schemaCenter(node) {
  return { x: node.x + node.w / 2, y: node.y + node.h / 2 };
}

function schemaTypeLabel(type) {
  const labels = {
    start: "Start",
    agent: "Agent",
    router: "Router",
    parallel: "Parallel",
    merge: "Merge",
    approval: "Approval",
    output: "Output"
  };
  return labels[type] || type;
}

function schemaStageIndex(node) {
  const typeOrder = {
    start: 0,
    router: 1,
    agent: 2,
    parallel: 3,
    merge: 4,
    approval: 5,
    output: 6,
  };
  return typeOrder[node.type] ?? 2;
}

function layoutBlockSchemaByStage() {
  const grouped = new Map();
  blockSchema.nodes.forEach((node) => {
    const stage = schemaStageIndex(node);
    grouped.set(stage, [...(grouped.get(stage) || []), node]);
  });
  [...grouped.entries()].forEach(([stage, nodes]) => {
    nodes.forEach((node, row) => {
      node.x = 60 + stage * 360;
      node.y = 80 + row * 240;
      node.w = Math.max(node.w || 260, node.type === "parallel" || node.type === "router" ? 300 : 260);
      node.h = Math.max(node.h || 168, node.type === "parallel" || node.type === "approval" ? 188 : 168);
    });
  });
}

function draftSchemaNode(type) {
  const index = blockSchema.nodes.length + 1;
  const stage = schemaStageIndex({ type });
  const sameStage = blockSchema.nodes.filter((node) => schemaStageIndex(node) === stage).length;
  const title = `${schemaTypeLabel(type)} ${index}`;
  const defaults = schemaNodeTypeDefaults(type, title, "Pending review output.");
  return schemaNode(
    makeId(`schema-${type}`),
    type,
    title,
    60 + stage * 360,
    80 + sameStage * 240,
    defaults.owner,
    `Define the ${schemaTypeLabel(type).toLowerCase()} prompt, evidence, owner, inputs, outputs, and approval boundary.`,
    defaults.outputs[0] || "Pending review output.",
    {
      workflowLayer: architectureMode === "service" ? "service product" : "control system",
      status: defaults.status,
      comments: defaults.comments,
      requirements: defaults.requirements,
      inputs: defaults.inputs,
      outputs: defaults.outputs,
      questions: defaults.questions,
      possibleOutputs: defaults.possibleOutputs,
      config: defaults.config,
      w: defaults.w,
      h: defaults.h,
    }
  );
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

function setApiStatus(text, tone = "warn", detail = "") {
  jarvisApiState = {
    ...jarvisApiState,
    label: text,
    tone,
    detail: detail || jarvisApiState.detail,
  };
  if (apiStatus) {
    apiStatus.textContent = text;
    apiStatus.className = `pill live-pill ${tone}`;
    apiStatus.title = detail || text;
  }
}

function apiEndpoint(path) {
  const normalized = path.startsWith("/") ? path : `/${path}`;
  return `${jarvisApiBase}${normalized}`;
}

function cloudApprovalRequested(input) {
  void input;
  // Static dashboard text is never enough to approve provider execution.
  return false;
}

function attachmentRequestPayload() {
  return pendingAttachments.slice(0, 6).map((attachment) => ({
    id: attachment.id,
    name: attachment.name,
    mime_type: attachment.mime_type,
    size: attachment.size,
    transfer_mode: attachment.transfer_mode,
    text_excerpt: attachment.text_excerpt || "",
  }));
}

function conversationRequestPayload() {
  return chatHistory.slice(-8).map((message) => ({
    role: message.role,
    source: message.source,
    time: message.time,
    text: String(message.text || "").slice(0, 1400),
  }));
}

function providerRequestPayload(input, source = "typed command") {
  const useProvider = cloudApprovalRequested(input);
  return {
    request: String(input || "").slice(0, 12000),
    lane: "jarvis_chat",
    architecture: architectureMode,
    approved_test_input: false,
    owner_approval: useProvider,
    provider_approval: useProvider,
    source_refs: [source, "dashboard chat"],
    conversation: conversationRequestPayload(),
    attachments: attachmentRequestPayload(),
  };
}

async function sendJarvisCloudCommand(input, source = "typed command") {
  const endpoint = "/api/chat";
  await checkJarvisApi("Jarvis command submit", { silent: true, timeoutMs: 4000 });
  const response = await fetch(apiEndpoint(endpoint), {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(providerRequestPayload(input, source)),
  });
  if (!response.ok) throw new Error(`backend returned ${response.status}`);
  return response.json();
}

function cloudResultText(result) {
  const provider = result?.payload?.provider_result;
  const runtime = result?.payload?.architecture_runtime;
  if (provider?.provider_executed && provider.reply) {
    return `${runtime?.architecture || "Cloud Jarvis"} returned via ${result.runtime?.model || "OpenRouter"}:\n\n${provider.reply}`;
  }
  const fallbackReply = result?.payload?.reply;
  const attachmentCount = Number(result?.payload?.attachment_count || 0);
  const attachmentText = attachmentCount ? ` Attachments received: ${attachmentCount}.` : "";
  const reason = provider?.reason ? ` Provider route: ${provider.reason}.` : "";
  return `${fallbackReply || `${runtime?.architecture || "Cloud Jarvis"} returned ${result?.status || "a review packet"}.`}${attachmentText}${reason} Writeback remains disabled until review.`;
}

async function checkJarvisApi(reason = "health check", options = {}) {
  const controller = new AbortController();
  const timeoutId = window.setTimeout(() => controller.abort(), options.timeoutMs || 2400);
  try {
    const response = await fetch(`${apiEndpoint("/health")}?ts=${Date.now()}`, {
      cache: "no-store",
      signal: controller.signal,
    });
    if (!response.ok) throw new Error(`health returned ${response.status}`);
    const result = await response.json();
    jarvisApiState = {
      status: "connected",
      label: "Jarvis API connected",
      detail: `${result.payload?.service || "jarvis-api"} ${result.payload?.version || ""}`.trim(),
      tone: "ok",
      payload: result,
    };
    setApiStatus(jarvisApiState.label, "ok", jarvisApiState.detail);
    if (!options.silent) appendEvent("Jarvis API connected", `Health check passed after ${reason}.`, "ok");
    return jarvisApiState;
  } catch (error) {
    const message = error?.name === "AbortError"
      ? "Local Jarvis API health check timed out."
      : `Local Jarvis API unavailable: ${error.message || error}.`;
    jarvisApiState = {
      status: "disconnected",
      label: "Jarvis API disconnected",
      detail: `${message} Start services/jarvis-api on port 8787 or set ${storageKeys.apiBase}.`,
      tone: "warn",
      payload: null,
    };
    setApiStatus(jarvisApiState.label, "warn", jarvisApiState.detail);
    if (!options.silent) appendEvent("Jarvis API disconnected", jarvisApiState.detail, "warn");
    return jarvisApiState;
  } finally {
    window.clearTimeout(timeoutId);
  }
}

function isEditingControlActive() {
  const element = document.activeElement;
  if (!element) return false;
  return ["INPUT", "TEXTAREA", "SELECT"].includes(element.tagName) || element.isContentEditable;
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

function appendChat(role, text, source = "typed command") {
  chatHistory = [
    ...chatHistory,
    {
      id: makeId(`chat-${role}`),
      role,
      source,
      time: nowIso(),
      text: String(text || "").slice(0, 1600),
    },
  ];
  saveJson(storageKeys.chatHistory, chatHistory);
}

function clearChatHistory() {
  const confirmed = window.confirm("Clear persistent Jarvis chat history in this browser?");
  if (!confirmed) return;
  chatHistory = [];
  saveJson(storageKeys.chatHistory, chatHistory);
  appendEvent("Chat history cleared", "Persistent Jarvis chat history was cleared locally by explicit action.", "warn");
  render();
}

function exportChatHistory() {
  const packet = createLocalPacket("jarvis-chat-history-export", "current browser session", "Export current Jarvis chat history for Codex review.", {
    extra: {
      chat_history: chatHistory,
      persistence: "local browser storage until explicit clear; download packet requires Codex review before durable write",
    },
  });
  downloadPacket(packet.id);
}

function enterInterviewMode(lane = architectureMode, source = "mode selector") {
  setArchitectureMode(lane);
  jarvisMode = "interview";
  localStorage.setItem(storageKeys.mode, jarvisMode);
  interviewState = {
    ...defaultInterviewState(),
    active: true,
    lane: architectureMode,
  };
  saveJson(storageKeys.interviewState, interviewState);
  const question = architectureMeta().firstInterviewQuestion;
  appendChat("assistant", question, `Jarvis interview kickoff - ${architectureMeta().short}`);
  appendEvent("Interview started", `${architectureMeta().label}. Jarvis asked the first question proactively from ${source}.`, "ok");
  return question;
}

function advanceInterview(answer, source = "interview answer") {
  const lane = interviewState.lane === "control" ? "control" : "service";
  interviewState = {
    ...interviewState,
    active: true,
    lane,
    answers: [
      ...(interviewState.answers || []),
      {
        time: nowIso(),
        source,
        architecture: lane,
        summary: String(answer || "").slice(0, 900),
      },
    ].slice(-30),
    questionIndex: Math.min((interviewState.questionIndex || 0) + 1, interviewQuestions[lane].length - 1),
    lastSummary: String(answer || "").slice(0, 900),
  };
  saveJson(storageKeys.interviewState, interviewState);
  const packet = createLocalPacket(`${lane}-interview-memory-candidate`, source, answer, {
    extra: {
      architecture: architectureMeta(lane).label,
      next_question: currentInterviewQuestion(),
      memory_policy: "summary candidates only; raw transcript storage is off by default",
    },
  });
  return `Captured for ${architectureMeta(lane).label}: ${packet.id}. Next question: ${currentInterviewQuestion()}`;
}

function architectureSelectorMarkup(context = "jarvis") {
  return `
    <div class="architecture-selector" data-context="${escapeHtml(context)}" aria-label="Jarvis architecture selector">
      <button class="${architectureMode === "service" ? "active" : ""}" data-architecture="service" type="button">
        <strong>1</strong>
        <span>Architecture 1 - PRD/ICP service output</span>
      </button>
      <button class="${architectureMode === "control" ? "active" : ""}" data-architecture="control" type="button">
        <strong>2</strong>
        <span>Architecture 2 - agent control system</span>
      </button>
    </div>
  `;
}

function bindArchitectureSelectors(root = document) {
  root.querySelectorAll("[data-architecture]").forEach((button) => {
    button.addEventListener("click", () => {
      setArchitectureMode(button.dataset.architecture, { switchTab: button.closest(".schema-shell") != null });
      if (jarvisMode === "interview") enterInterviewMode(architectureMode, "architecture selector");
      render();
    });
  });
}

function speechSynthesisAvailable() {
  return "speechSynthesis" in window && "SpeechSynthesisUtterance" in window;
}

function speakText(text, options = {}) {
  if ((!voiceOutputEnabled && !options.force) || !speechSynthesisAvailable()) return;
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(String(text || "").slice(0, 900));
  utterance.rate = 0.96;
  utterance.pitch = 1;
  utterance.volume = 1;
  const voices = window.speechSynthesis.getVoices?.() || [];
  const preferred = voices.find((voice) => /en/i.test(voice.lang) && /samantha|ava|alloy|natural|premium|enhanced/i.test(voice.name))
    || voices.find((voice) => /en/i.test(voice.lang))
    || voices[0];
  if (preferred) utterance.voice = preferred;
  utterance.onstart = () => setLiveStatus("Jarvis speaking", "ok");
  utterance.onend = () => setLiveStatus("Static polling active", "warn");
  window.speechSynthesis.speak(utterance);
}

function stopSpeechPlayback() {
  if (speechSynthesisAvailable()) window.speechSynthesis.cancel();
  setLiveStatus("Speech stopped", "warn");
  appendEvent("Speech playback stopped", "Browser speech synthesis was stopped by the operator.", "warn");
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
  setLiveStatus(changed ? "Static data updated" : "Static polling active", changed ? "ok" : "warn");
  render();
}

function startLiveRefresh() {
  if (refreshTimer) window.clearInterval(refreshTimer);
  refreshTimer = window.setInterval(() => {
    if (isEditingControlActive()) {
      setLiveStatus("Static polling paused while editing", "warn");
      return;
    }
    loadDashboardData("scheduled static poll", true).catch(() => {
      setLiveStatus("Static data only", "warn");
    });
  }, 15000);
  if (apiHealthTimer) window.clearInterval(apiHealthTimer);
  apiHealthTimer = window.setInterval(() => {
    checkJarvisApi("scheduled health check", { silent: true }).catch(() => {});
  }, 30000);
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
      <button type="button" class="${tab.id === activeTab ? "active" : ""}" data-tab="${tab.id}" aria-current="${tab.id === activeTab ? "page" : "false"}">
        <span class="glyph">${tab.glyph}</span>
        <span>${tab.label}</span>
      </button>
    `)
    .join("");

  nav.querySelectorAll("button").forEach((button) => {
    button.addEventListener("click", () => {
      activeTab = button.dataset.tab;
      if (activeTab === "service") setArchitectureMode("service");
      if (activeTab === "schema") setArchitectureMode("control");
      window.history.replaceState(null, "", `#${activeTab}`);
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
    { label: "Refresh", value: "static polling", note: "Manual, focus, command, and 15s data checks", tone: "ok" },
    { label: "Jarvis", value: jarvisMode, note: "Normal or interview command mode", tone: "ok" },
    { label: "Jarvis API", value: jarvisApiState.status, note: jarvisApiState.detail, tone: jarvisApiState.tone },
    { label: "Voice", value: "disabled", note: "Text chat and file transfer only on this dashboard", tone: "warn" },
    { label: "File transfer", value: pendingAttachments.length ? "pending" : "ready", note: pendingAttachments.length ? `${pendingAttachments.length} attachment(s) staged for next chat message` : "Bounded text excerpts or metadata-only packets", tone: pendingAttachments.length ? "ok" : "warn" },
    { label: "Provider keys", value: "server env only", note: "Provider keys are never exposed to static JS; provider calls require API/budget gates", tone: "warn" },
    { label: "E1.3", value: e13?.derived_status || "unknown", note: e13 ? `${e13.passed_count}/${e13.assertion_count} readback` : "No gate data", tone: e13?.readback_status === "passed" ? "ok" : "warn" },
    { label: "Railway", value: "deferred", note: "Use for backend, SSE, auth, workers, durable writes", tone: "warn" },
  ];
}

function operatingStatusCards(data) {
  const latestSource = data.activity?.[0]?.title || data.sources?.[0]?.title || "latest public-safe source";
  return [
    {
      label: "Start Here",
      value: "Jarvis command",
      note: "Ask, refresh, stage packet, or open interview mode.",
      tone: "ok",
    },
    {
      label: "Lane 1",
      value: "PRD/ICP service product",
      note: "Buyer-facing PRD, ICP, evidence, report, and task outputs.",
      tone: "ok",
    },
    {
      label: "Lane 2",
      value: "Reliable agent orchestra",
      note: "Internal Codex, review, provider gate, memory, and writeback control.",
      tone: "ok",
    },
    {
      label: "Current Proof",
      value: "static route smoke",
      note: `Latest source: ${latestSource}`.slice(0, 82),
      tone: "warn",
    },
    {
      label: "Blocked Gates",
      value: "runtime gates",
      note: "Provider, backend, and writeback stay gated.",
      tone: "warn",
    },
  ];
}

function proofBacklogItems() {
  return [
    {
      id: "D-1",
      title: "Jarvis first-screen operating area",
      status: "proved",
      proof: "Jarvis text chat, file transfer, packet queue, and operating states render on #jarvis.",
      next: "Keep voice mode disabled unless a new owner-approved audio lane is opened.",
    },
    {
      id: "D-2",
      title: "Two-orchestra operating modes",
      status: "proved",
      proof: "Operating Switchboard and schema screens separate PRD/ICP service product from reliable agent orchestra.",
      next: "Keep website copy buyer-facing while dashboard remains internal control proof.",
    },
    {
      id: "D-3",
      title: "Static/local/provider/writeback clarity",
      status: "proved",
      proof: "State badges, runtime gates, and smoke markers show provider disabled and writeback gated.",
      next: "Do not claim backend/provider runtime until approved bridge exists.",
    },
    {
      id: "D-4",
      title: "Node control panel hierarchy",
      status: "proved",
      proof: "Node panel includes Overview, Inputs, Outputs, Connections, Config, Logs, Prompts, Comments, and Safety.",
      next: "Add real run artifacts only after Codex/backend writes reviewed outputs.",
    },
    {
      id: "D-5",
      title: "Long graph and mobile review",
      status: "partial",
      proof: "Stage rail and node strip exist; mobile screenshot was inspected temporarily, not retained.",
      next: "Add durable sanitized screenshot or mobile stage-card acceptance record before merge/deploy claim.",
    },
    {
      id: "D-6",
      title: "Proof and blocker visibility",
      status: "proved",
      proof: "This panel surfaces checks, blockers, backlog IDs, accepted static-scope state, and next commands inside the dashboard.",
      next: "Keep it aligned with issue/run notes after each dashboard pass and do not merge gated runtime work into static acceptance.",
    },
    {
      id: "D-8",
      title: "Public-safe sample outputs",
      status: "proved",
      proof: "Sanitized source packet, PRD excerpt, evidence card, task matrix, agent node config, and approval log examples now render on the Jarvis first screen.",
      next: "Replace examples with reviewed E2.0A artifacts only after source-safe proof exists.",
    },
  ];
}

function validationCommandItems() {
  return [
    ["JavaScript syntax", "`node --check project/dashboard/app.js`", "passed"],
    ["Dashboard JSON", "parse `project/dashboard/data.json`", "passed"],
    ["Rendered route smoke", "`python3 project/scripts/dashboard-static-smoke.py`", "passed"],
    ["Public safety", "`python3 scripts/public_safety_scan.py`", "passed"],
    ["Diff hygiene", "`git diff --check`", "passed"],
    ["Runtime guard", "`python3 project/scripts/pre-push-runtime-guard.py`", "required before branch closeout"],
    ["Workflow validation", "`project/local/venv/bin/python project/scripts/validate-workflows.py`", "required before branch closeout"],
  ];
}

function publicSafeSampleOutputs() {
  return [
    {
      label: "Source packet",
      title: "Sanitized product-context packet",
      body: "Situation, goals, known facts, assumptions, open gaps, constraints, and approved source labels. Raw calls, transcripts, documents, customer names, and private links are excluded.",
      output: "Input for PRD builder and evidence fork.",
    },
    {
      label: "PRD excerpt",
      title: "Sanitized PRD excerpt",
      body: "Problem, target user, acceptance criteria, non-goals, dependencies, risks, and reviewer questions. Each claim is tagged as FACT, INTERPRETATION, HYPOTHESIS, or GAP.",
      output: "Draft section for owner review, not an auto-approved PRD.",
    },
    {
      label: "Evidence card",
      title: "ICP signal card",
      body: "Account shape, role hypothesis, pain type, source grade, confidence, contradiction, and next verification action. Public social signals remain hypotheses until triangulated.",
      output: "E2.0A research packet candidate.",
    },
    {
      label: "Task matrix",
      title: "Delivery responsibility grid",
      body: "Task, owner, input artifact, expected output, acceptance criteria, blocker, approval gate, and durable destination. No task is marked done without linked evidence.",
      output: "Implementation handoff for Codex/reviewer lanes.",
    },
    {
      label: "Agent node config",
      title: "Approval-gated node contract",
      body: "Allowed inputs, forbidden inputs, model provider state, persistence mode, retrieval scope, safety review, run recorder, prompt, system prompt, and comments.",
      output: "Browser-local node packet for Codex review.",
    },
    {
      label: "Approval log",
      title: "Human review checkpoint",
      body: "Decision, evidence used, explicit gaps, blocked actions, approved destination, next owner, and confidence level. Provider/backend/writeback claims remain gated.",
      output: "Public-safe run note or issue update.",
    },
  ];
}

function prdIcpOutputBlocks() {
  return [
    ["Meeting Summary", "Decision-ready summary of approved meeting or interview input, with raw transcript storage off by default."],
    ["Product Context", "Problem, product area, user workflow, constraints, non-goals, and source boundary."],
    ["Stakeholders", "Decision owner, product owner, engineering partner, reviewer, and follow-up owners."],
    ["ICP", "Current B2B SaaS product-team lane, account shape, buyer role, triggers, disqualifiers, and confidence."],
    ["Pains/JTBD", "Buyer pains, jobs to be done, current friction, desired outcome, and evidence grade."],
    ["Existing Workflow", "Current steps, tools, handoffs, duplicate work, blockers, and decision-memory loss."],
    ["Proposed Workflow", "Target state, human gates, agent roles, source labels, and review checkpoints."],
    ["Requirements", "Functional, non-functional, safety, reporting, retrieval, and integration requirements."],
    ["Decisions", "Accepted decisions, owner, evidence used, confidence, and later review trigger."],
    ["Questions", "Missing context, contradictions, buyer validation questions, and approval questions."],
    ["Risks", "Unsupported claims, raw-source risk, provider/runtime risk, cost risk, and delivery risk."],
    ["Next Tasks", "Role-owned next actions with artifact target, blocker, review gate, and due condition."],
    ["Backlog", "Suggested Jira/GitLab-ready epics, stories, acceptance criteria, and dependencies."],
    ["Success Metrics", "Cycle-time, rework, handoff quality, evidence completeness, review latency, and buyer signal metrics."],
  ];
}

function taskStages() {
  return ["Intake", "Role Assignment", "Active Work", "QA Gate", "Docs/Reports", "Git/Deploy", "Notion/Memory", "Final Decision"];
}

function defaultRoleConfigs() {
  const makeRole = (id, title, objective, responsibility, tools, modelRoute, budgetMode, outputArtifact, reviewGate, status, handoffTarget) => ({
    id,
    title,
    objective,
    responsibility,
    tools,
    modelRoute,
    budgetMode,
    outputArtifact,
    reviewGate,
    status,
    handoffTarget,
  });
  return [
    makeRole("jesus", "Jesus", "Lead integration and final acceptance.", "Merge order, final validation, Git push packet, and handout.", "Codex, Git, validation scripts", "Codex operator", "local only", "agent-handout.md", "AF Review plus owner gate", "active", "Owner approval"),
    makeRole("messi", "Messi", "Close out PM evidence without overclaiming.", "Notion/GitHub/project closeout, E1/E1.3.9 status, report links, task evidence.", "Notion package, wiki log, Git status", "Codex operator", "local only", "notion-update-package.md", "Evidence exists first", "review", "Jesus"),
    makeRole("lol", "LOL", "Own dashboard UX and block schema surface.", "Screen 1, Screen 2, role panels, composer, voice states, schema controls.", "Dashboard JS/CSS, static smoke", "Codex operator", "local only", "dashboard UI diff", "Browser/static proof", "active", "Jesus"),
    makeRole("ronaldinho", "Ronaldinho", "Review runtime and backend claims.", "Backend/API, LangGraph, CrewAI, OpenRouter, env, Railway, voice, runtime boundaries.", "FastAPI, YAML, runtime guards", "Codex operator", "no provider spend", "technical review", "Provider disabled check", "review", "Jesus"),
    makeRole("ronaldo", "Ronaldo", "Protect product and ICP consistency.", "PRD/ICP offer, buyer value, current single ICP lane, demo/report consistency.", "Reports, ICP docs, PRD template", "Codex operator", "local only", "ICP review", "Source support", "review", "Jesus"),
    makeRole("yushchenko", "Yushchenko", "Keep model budget and ledger discipline.", "OpenRouter ledger, token/cost discipline, 5.00 USD daily cap, 1.99 USD hard stop.", "model-routing.yaml, ledger schema", "OpenRouter gated", "stop before 1.99 USD", "budget verdict", "Ledger required", "gated", "Jesus"),
    makeRole("theory", "Theory Subagent", "Ground PRD and discovery structure.", "FreePRD, PRD theory, ICP theory, discovery-call theory, missing-info questions.", "PRD/report templates", "Codex operator", "local only", "theory notes", "Source review", "review", "Ronaldo"),
    makeRole("security", "Security Subagent", "Protect secrets and unsafe write paths.", "Env variables, Telegram migration, secret scan, browser key ban, raw transcript policy.", "public safety scan, env examples", "Codex operator", "local only", "security checklist", "Secret scan", "active", "Ronaldinho"),
    makeRole("actor", "Actor", "Execute one bounded task slice.", "Implement assigned scope without reverting unrelated changes.", "Scoped editor tools", "Codex operator", "local only", "bounded patch", "Reviewer required", "available", "Jesus"),
    makeRole("af_tools", "AF Tools", "Verify sources, providers, and tools.", "Readiness checks, source inventory, provider status, runtime boundaries.", "runtime guard, config check", "Codex operator", "local only", "tool readiness", "AF Review", "active", "Jesus"),
    makeRole("af_knowledge", "AF Knowledge", "Prepare reviewed memory packets.", "WikiLLM, run notes, insights, and public-safe memory candidates.", "wiki files, run notes", "Codex operator", "local only", "KB update packet", "Memory approval", "review", "Messi"),
    makeRole("af_publisher", "AF Publisher", "Prepare publication only after gates pass.", "Git/deploy/report packet, release notes, blocked send reasons.", "Git, Vercel gated, reports", "Codex operator", "local only", "publication packet", "Owner approval", "gated", "Jesus"),
    makeRole("af_review", "AF Review", "Approve, revise, or block final output.", "Public safety, claim support, runtime boundary, docs/check evidence.", "safety scan, diff check, smoke", "Codex operator", "local only", "review verdict", "Required before push", "active", "Jesus"),
    makeRole("crewai_workers", "CrewAI Role Workers", "Represent CrewAI roles without default runtime promotion.", "Configured role/task workers; Level 3 deterministic proof is evidence only.", "crewai-crew.yaml, proof artifacts", "proof_passed_not_default_runtime", "0.00 USD proof spend", "CrewAI proof packet", "Provider/default approval required", "eligible", "LangGraph"),
  ];
}

function ensureRoleConfigs() {
  const defaults = defaultRoleConfigs();
  const byId = new Map((Array.isArray(roleConfigs) ? roleConfigs : []).map((role) => [role.id, role]));
  roleConfigs = defaults.map((role) => ({ ...role, ...(byId.get(role.id) || {}) }));
  saveJson(storageKeys.roleConfig, roleConfigs);
}

function renderPrdIcpRequestSurface() {
  return `
    <section class="panel prd-request-panel" style="margin-top:16px">
      <div class="section-header">
        <div>
          <h2 class="section-title">Direct Jarvis PRD/ICP Request</h2>
          <p class="muted">Attempts the local backend lane when available; otherwise it stages a browser-local packet for Codex review. OpenRouter stays server-side and disabled until approval and budget guard proof exist.</p>
        </div>
        <div class="row-actions">
          <button class="primary" id="prdSendBackend" type="button">Send to local backend</button>
          <button class="button" id="prdStagePacket" type="button">Stage packet</button>
        </div>
      </div>
      <label class="full-width-label">Request
        <textarea id="prdComposerInput" rows="5" placeholder="Turn the approved meeting/interview/research input into a PRD/ICP packet with backlog and missing-info questions.">${escapeHtml(prdComposerDraft)}</textarea>
      </label>
      <div class="schema-runtime-gates compact">
        <span>Test fixture: docs/testmeeting.md after owner approval</span>
        <span>Discovery source links: approval-gated inputs</span>
        <span>Output includes Jira/GitLab backlog</span>
        <span>Missing-info questions required</span>
      </div>
      <div id="prdBackendStatus" class="callout compact">Backend status unknown. Static mode will preserve the request as text if the backend is unavailable.</div>
    </section>
  `;
}

function renderPrdIcpOutputBlocks() {
  return `
    <section class="panel prd-blocks-panel" style="margin-top:16px">
      <div class="section-header">
        <div>
          <h2 class="section-title">PRD/ICP Output Blocks</h2>
          <p class="muted">The service output follows a product-doc structure: source summary first, then workflow, requirements, decisions, backlog, metrics, and gaps.</p>
        </div>
        <div class="row-actions">
          <a class="button" href="../../docs/prd-icp-output-template.md">PRD template</a>
          <a class="button" href="../../docs/testmeeting-prd-runbook.md">Test runbook</a>
        </div>
      </div>
      <div class="output-block-grid">
        ${prdIcpOutputBlocks().map(([title, body]) => `
          <article class="output-block">
            <strong>${escapeHtml(title)}</strong>
            <p>${escapeHtml(body)}</p>
          </article>
        `).join("")}
      </div>
    </section>
  `;
}

function renderTaskStages() {
  return `
    <section class="panel" style="margin-top:16px">
      <div class="section-header">
        <div>
          <h2 class="section-title">Agent Orchestra Stages</h2>
          <p class="muted">Operator-facing execution path from intake through final decision, with Git/deploy and Notion/memory as explicit gates.</p>
        </div>
      </div>
      <div class="stage-grid">
        ${taskStages().map((stage, index) => `
          <article class="stage-card">
            <span>${index + 1}</span>
            <strong>${escapeHtml(stage)}</strong>
          </article>
        `).join("")}
      </div>
    </section>
  `;
}

function renderRoleConfigPanels() {
  ensureRoleConfigs();
  return `
    <section class="panel role-config-panel" style="margin-top:16px">
      <div class="section-header">
        <div>
          <h2 class="section-title">Role Configuration</h2>
          <p class="muted">Editable safe fields are stored in browser localStorage and can be exported as a review packet. The browser does not write source YAML.</p>
        </div>
        <div class="row-actions">
          <button class="primary" id="saveRoleConfig" type="button">Save local role config</button>
          <button class="button" id="exportRoleConfig" type="button">Export role packet</button>
        </div>
      </div>
      <div class="role-card-grid">
        ${roleConfigs.map((role) => `
          <article class="role-config-card" data-role-id="${escapeHtml(role.id)}">
            <header>
              <strong>${escapeHtml(role.title)}</strong>
              <span>${escapeHtml(role.status)}</span>
            </header>
            <label>Objective<input data-field="objective" value="${escapeHtml(role.objective)}" /></label>
            <label>Responsibility<textarea data-field="responsibility" rows="2">${escapeHtml(role.responsibility)}</textarea></label>
            <label>Tools<input data-field="tools" value="${escapeHtml(role.tools)}" /></label>
            <div class="control-grid compact">
              <label>Model route<input data-field="modelRoute" value="${escapeHtml(role.modelRoute)}" /></label>
              <label>Budget mode<input data-field="budgetMode" value="${escapeHtml(role.budgetMode)}" /></label>
              <label>Output artifact<input data-field="outputArtifact" value="${escapeHtml(role.outputArtifact)}" /></label>
              <label>Review gate<input data-field="reviewGate" value="${escapeHtml(role.reviewGate)}" /></label>
              <label>Status<select data-field="status">
                ${["available", "active", "review", "blocked", "gated", "eligible", "done"].map((status) => `<option value="${status}" ${role.status === status ? "selected" : ""}>${status}</option>`).join("")}
              </select></label>
              <label>Handoff target<input data-field="handoffTarget" value="${escapeHtml(role.handoffTarget)}" /></label>
            </div>
          </article>
        `).join("")}
      </div>
    </section>
  `;
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
  const architecture = architectureMeta();

  if (!text) {
    return `Jarvis is ready in ${architecture.label}. Ask for status, refresh, a PRD/ICP packet, an architecture-control task, or interview mode.`;
  }

  if (lower === "1" || lower.includes("architecture 1") || lower.includes("arch 1") || lower.includes("prd architecture") || lower.includes("service architecture")) {
    setArchitectureMode("service", { switchTab: true });
    return `Architecture 1 is active. Normal commands now bias toward ${architectureMeta().commandBias}.`;
  }

  if (lower === "2" || lower.includes("architecture 2") || lower.includes("arch 2") || lower.includes("control architecture") || lower.includes("agent architecture")) {
    setArchitectureMode("control", { switchTab: true });
    return `Architecture 2 is active. Normal commands now bias toward ${architectureMeta().commandBias}.`;
  }

  if (lower.includes("refresh") || lower.includes("reload") || lower.includes("update dashboard")) {
    loadDashboardData("Jarvis refresh command").catch((error) => {
      appendEvent("Refresh failed", error.message, "block");
      render();
    });
    return "I am refreshing the dashboard data in place. The page will not reload.";
  }

  if (lower.includes("interview")) {
    return enterInterviewMode(architectureMode, source);
  }

  if (lower.includes("normal mode") || lower.includes("status mode")) {
    jarvisMode = "normal";
    localStorage.setItem(storageKeys.mode, jarvisMode);
    interviewState = { ...defaultInterviewState(), lane: architectureMode };
    saveJson(storageKeys.interviewState, interviewState);
    appendEvent("Jarvis mode changed", "Normal mode answers status and waits for instructions.", "ok");
    return `Normal mode is active in ${architectureMeta().label}. I will answer under the selected architecture and ask before durable writes.`;
  }

  if (lower.includes("research") || lower.includes("check") || lower.includes("file") || lower.includes("analyze")) {
    const packet = createLocalPacket("research-check", source, text, {
      extra: {
        architecture: architecture.label,
        recommended_agent: "AF Research + AF Review",
        next_step: "Use Codex or Railway writeback to save the packet and update WikiLLM after review.",
      },
    });
    return `I created a local research/check packet: ${packet.id}. It is staged for ${packet.target_file}; static Vercel cannot write it to the repo without Codex or Railway authority.`;
  }

  if (lower.includes("content") || lower.includes("carousel") || lower.includes("post")) {
    const packet = createLocalPacket("content-template-request", source, text, {
      extra: {
        architecture: architecture.label,
        recommended_agent: "AF Copy + Visual Reporting + AF Review",
        proof_required: "approved artifact, evidence label, no demand claim, AF Review, owner approval",
      },
    });
    return `I staged a content-template packet: ${packet.id}. It should become implementation-focused content only after the proof and review gates pass.`;
  }

  if (lower.includes("status") || lower.includes("what works") || lower.includes("done")) {
    const e13 = dashboardData?.gates?.e1_3;
    return `Current status in ${architecture.label}: E1.3 is ${e13?.derived_status || "unknown"} with ${e13?.passed_count || 0}/${e13?.assertion_count || 0} readback checks. Dashboard keeps local browser packets, while Jarvis API is ${jarvisApiState.status}; OpenRouter execution is server-side only and requires explicit owner/provider approval plus budget guards. Voice is disabled; durable file writes and writeback remain gated.`;
  }

  if (lower.includes("voice") || lower.includes("speak") || lower.includes("sound")) {
    activeTab = "jarvis";
    return "Voice mode is disabled on this dashboard. Use Jarvis text chat and file attachments; raw audio capture, browser speech recognition, speaker playback, and voice API routes stay off.";
  }

  if (lower.includes("schema") || lower.includes("block") || lower.includes("graph")) {
    activeTab = "schema";
    return "Opening the block-schema page. It separates direct operator-to-Codex interaction from the downstream graph, reviewer, memory, and dashboard-monitor structure.";
  }

  if (lower.includes("icp") || lower.includes("service product") || lower.includes("prd flow")) {
    activeTab = "service";
    return "Opening the PRD/ICP service product flow. This screen shows the externally showable path from source intake to PRD, evidence, ICP, demo, approval, and output packet.";
  }

  if (lower.includes("config") || lower.includes("subprompt") || lower.includes("prompt")) {
    activeTab = "config";
    return "Opening the configuration page. Edits are browser-local and can be exported as a packet for Codex review; they do not change GitHub, Notion, or runtime prompts directly.";
  }

  if (lower.includes("project plan") || lower.includes("plan structure") || lower.includes("prd")) {
    activeTab = "plan";
    return "Opening the project plan view. It shows the E1-E7 spine, PRD-to-ICP flow, and source links from the committed dashboard data.";
  }

  if (jarvisMode === "interview") {
    return advanceInterview(text, source);
  }

  if (architectureMode === "control") {
    const packet = createLocalPacket("architecture-control-command", source, text, {
      extra: {
        architecture: architecture.label,
        allowed_scope: "prepare architecture change packet, logs, memory update candidates, and approval gates",
        forbidden_without_approval: ["provider call", "Railway deploy", "live writeback", "raw transcript storage"],
      },
    });
    return `Architecture 2 command staged: ${packet.id}. I will treat this as a controlled architecture/workflow request with logs, KB/Graphify/LlamaIndex/WikiLLM implications, and approval gates.`;
  }

  const packet = createLocalPacket("prd-service-command", source, text, {
    extra: {
      architecture: architecture.label,
      expected_outputs: ["PRD section", "task matrix", "evidence gaps", "review packet"],
    },
  });
  return `Architecture 1 command staged: ${packet.id}. I will treat this as a PRD/ICP service-output request and preserve missing information as questions or gaps.`;
}

async function handleGlobalSubmit(value, source = "typed command") {
  const input = String(value || "").trim();
  if (!input) return;
  const previousTab = activeTab;
  appendChat("user", input, source);
  const reply = jarvisReply(input, source);
  let finalReply = reply;
  let finalSource = "Jarvis local packet";
  appendEvent("Jarvis command", input.slice(0, 160), "ok");
  if (!["refresh", "reload", "update dashboard"].some((phrase) => input.toLowerCase().includes(phrase))) {
    try {
      appendEvent("Jarvis cloud route", `Sending ${architectureMeta().label} request to ${jarvisApiBase}.`, "ok");
      const result = await sendJarvisCloudCommand(input, source);
      const cloudReply = cloudResultText(result);
      finalReply = `${reply}\n\nAPI: ${cloudReply}`;
      finalSource = "Jarvis API + local packet";
      appendEvent("Jarvis cloud response", `${result.status || "ok"} from ${architectureMeta().label}.`, result.status === "provider_response_created" ? "ok" : "warn");
      pendingAttachments = [];
    } catch (error) {
      appendEvent("Jarvis cloud fallback", `Cloud request unavailable: ${error.message || error}. Local packet preserved.`, "warn");
    }
  }
  appendChat("assistant", finalReply, finalSource);
  if (activeTab === previousTab && activeTab !== "jarvis") activeTab = "jarvis";
  window.history.replaceState(null, "", `#${activeTab}`);
  render();
}

function renderJarvis(data) {
  const latestPacket = localPackets[0];
  const recentMessages = chatHistory.slice(-24);
  view.innerHTML = `
    <div class="jarvis-chat-layout">
      <section class="panel jarvis-chat-panel" aria-label="Jarvis chat">
        <div class="jarvis-chat-header">
          <div>
            <div class="jarvis-title-row">
              <div class="jarvis-avatar" aria-hidden="true">JV</div>
              <div>
                <h2>Jarvis Chat</h2>
                <p>${escapeHtml(architectureMeta().label)} - ${escapeHtml(jarvisApiState.label)} - text only</p>
              </div>
            </div>
          </div>
          <div class="jarvis-header-actions">
            <button class="button" id="jarvisRefresh" type="button">Refresh data</button>
            <button class="button" id="exportChat" type="button">Export chat packet</button>
            <button class="button" id="clearChat" type="button">Clear history</button>
          </div>
        </div>
        ${architectureSelectorMarkup("jarvis")}
        <div class="mode-bar inline" aria-label="Jarvis mode">
          <button class="${jarvisMode === "normal" ? "active" : ""}" data-mode="normal" type="button">Normal</button>
          <button class="${jarvisMode === "interview" ? "active" : ""}" data-mode="interview" type="button">Interview</button>
        </div>
        <div class="operator-strip chat-strip" aria-label="Dashboard operating states">
          <span>${escapeHtml(architectureMeta().short)}</span>
          <span>/api/chat</span>
          <span>File transfer</span>
          <span>Voice disabled</span>
          <span>Provider gated</span>
          <span>Writeback gated</span>
        </div>
        <div class="chat-thread main-chat" id="chatThread" aria-live="polite">
          ${recentMessages.length ? recentMessages.map((message) => `
            <article class="chat-message ${escapeHtml(message.role)}">
              <div class="chat-meta">${escapeHtml(message.role)} - ${escapeHtml(message.source)} - ${new Date(message.time).toLocaleTimeString()}</div>
              <p>${escapeHtml(message.text)}</p>
            </article>
          `).join("") : `<div class="callout">No local chat history in this browser.</div>`}
        </div>
        <div class="attachment-tray" id="attachmentTray">
          ${pendingAttachments.length ? pendingAttachments.map((attachment) => `
            <span class="attachment-chip">
              ${escapeHtml(attachment.name)} <small>${escapeHtml(formatFileSize(attachment.size))}</small>
              <button type="button" data-remove-attachment="${escapeHtml(attachment.id)}" aria-label="Remove ${escapeHtml(attachment.name)}">x</button>
            </span>
          `).join("") : `<span class="muted">No files attached.</span>`}
        </div>
        <form class="jarvis-chat-form" id="jarvisChatForm" aria-label="Send message to Jarvis">
          <label class="button icon-file-button" title="Attach files for this Jarvis message">
            Attach
            <input id="jarvisFileInput" type="file" multiple />
          </label>
          <textarea id="jarvisMessageInput" rows="3" placeholder="Message Jarvis about PRD/ICP work, agent orchestration, API checks, attached files, or current blockers."></textarea>
          <button class="primary" type="submit">Send</button>
        </form>
        <div class="callout compact">API: ${escapeHtml(jarvisApiState.detail)} Base: ${escapeHtml(jarvisApiBase)}.</div>
      </section>

      <aside class="panel jarvis-side-panel">
        <h2 class="section-title">Context</h2>
        <div class="list">
          <div class="row"><span class="row-title">Dashboard</span><div class="row-meta">Static Vercel view with API-backed review packets when available.</div></div>
          <div class="row"><span class="row-title">Jarvis actions</span><div class="row-meta">Chat can stage packets, use /api/chat, and include file excerpts without durable writeback.</div></div>
          <div class="row"><span class="row-title">Voice</span><div class="row-meta">Disabled on this dashboard. Use text chat and attachments only.</div></div>
          <div class="row"><span class="row-title">ICP</span><div class="row-meta">Primary lane remains B2B SaaS product-team PRD workflow quality.</div></div>
        </div>
        <div class="row-actions compact-actions">
          <a class="button active-soft" href="#service">PRD/ICP Flow</a>
          <a class="button active-soft" href="#schema">Agent Orchestra</a>
          <a class="button" href="#gates">Gates</a>
          <a class="button" href="#history">History</a>
        </div>
      </aside>
    </div>

    <section class="panel operating-switchboard" style="margin-top:16px">
      <div class="section-header">
        <div>
          <h2 class="section-title">Operating Switchboard</h2>
          <p class="muted">Choose the buyer-output flow or the internal control flow. The dashboard shows proof and blockers before any durable action.</p>
        </div>
        <div class="row-actions">
          <a class="button active-soft" href="#service">Open PRD/ICP Flow</a>
          <a class="button active-soft" href="#schema">Open Agent Orchestra</a>
          <a class="button" href="#gates">Review Gates</a>
        </div>
      </div>
      <div class="grid cols-3">
        <article class="row">
          <span class="row-title">PRD/ICP service product</span>
          <div class="row-meta">Source packet -> PRD -> evidence -> ICP -> demo package -> approval -> service output.</div>
        </article>
        <article class="row">
          <span class="row-title">Reliable agent orchestra</span>
          <div class="row-meta">Command -> route -> Codex work -> parallel review -> merge -> owner approval -> durable output.</div>
        </article>
        <article class="row">
          <span class="row-title">Proof and issue queue</span>
          <div class="row-meta">Static route smoke, public-safety checks, local packets, and blocked gates stay visible before any writeback.</div>
        </article>
      </div>
    </section>

    <div class="grid cols-6" style="margin-top:16px">${operatingStatusCards(data).map((item) => card(item)).join("")}</div>

    <section class="panel proof-backlog" style="margin-top:16px" id="proofBacklog">
      <div class="section-header">
        <div>
          <h2 class="section-title">Proof And Backlog Drawer</h2>
          <p class="muted">Current dashboard acceptance state from the project plan, issue backlog, communication history, and latest run checks.</p>
        </div>
        <div class="row-actions">
          <a class="button" href="../issues/2026-07-01-dashboard-website-improvement-issues.md">Issue backlog</a>
          <a class="button" href="#plan">Project plan</a>
        </div>
      </div>
      <div class="grid cols-3">
        <article class="row proof-command">
          <span class="row-title">Jesus command state</span>
          <div class="row-meta">Jesus accepted JDB-10 as review-ready for the static dashboard scope. Continue preserving provider, backend, writeback, voice, Nexus, deploy, and website-source gates.</div>
        </article>
        <article class="row proof-command">
          <span class="row-title">Next product step</span>
          <div class="row-meta">E2.0A dry run should produce evidence-card schema, source grades, ICP profile outline, executive decision, and next tasks.</div>
        </article>
        <article class="row proof-command">
          <span class="row-title">Next control step</span>
          <div class="row-meta">Run final validation, preserve the accepted static dashboard boundary, and keep Ronaldo's website closeout separate from dashboard acceptance.</div>
        </article>
      </div>
      <div class="proof-grid">
        <div>
          <h3>Dashboard Issue State</h3>
          <div class="list">
            ${proofBacklogItems().map((item) => `
              <article class="proof-item ${escapeHtml(item.status)}">
                <div>
                  <strong>${escapeHtml(item.id)} ${escapeHtml(item.title)}</strong>
                  <p>${escapeHtml(item.proof)}</p>
                  <span>${escapeHtml(item.next)}</span>
                </div>
                ${badge(item.status)}
              </article>
            `).join("")}
          </div>
        </div>
        <div>
          <h3>Validation Commands</h3>
          <div class="list">
            ${validationCommandItems().map(([label, command, status]) => `
              <article class="proof-check">
                <strong>${escapeHtml(label)}</strong>
                <code>${escapeHtml(command)}</code>
                <span>${escapeHtml(status)}</span>
              </article>
            `).join("")}
          </div>
        </div>
      </div>
    </section>

    <section class="panel sample-output-gallery" style="margin-top:16px">
      <div class="section-header">
        <div>
          <h2 class="section-title">Public-Safe Sample Outputs</h2>
          <p class="muted">Sanitized examples show what the service and agent orchestra produce without private screenshots, raw transcripts, customer data, or validated-demand claims.</p>
        </div>
        <div class="row-actions">
          <a class="button" href="#service">Service flow</a>
          <a class="button" href="#schema">Agent config</a>
        </div>
      </div>
      <div class="sample-grid">
        ${publicSafeSampleOutputs().map((item) => `
          <article class="sample-card">
            <span>${escapeHtml(item.label)}</span>
            <strong>${escapeHtml(item.title)}</strong>
            <p>${escapeHtml(item.body)}</p>
            <em>${escapeHtml(item.output)}</em>
          </article>
        `).join("")}
      </div>
    </section>

    <div class="grid cols-6" style="margin-top:16px">${systemCards(data).map((item) => card(item)).join("")}</div>

    <div class="split" style="margin-top:16px">
      <section class="panel">
        <h2 class="section-title">Session Event Stream</h2>
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
      if (button.dataset.mode === "interview") {
        enterInterviewMode(architectureMode, "mode button");
      } else {
        jarvisMode = "normal";
        localStorage.setItem(storageKeys.mode, jarvisMode);
        interviewState = { ...defaultInterviewState(), lane: architectureMode };
        saveJson(storageKeys.interviewState, interviewState);
        appendEvent("Jarvis mode changed", "Normal mode selected.", "ok");
      }
      render();
    });
  });
  bindArchitectureSelectors(view);

  document.querySelector("#jarvisRefresh")?.addEventListener("click", () => {
    loadDashboardData("manual Jarvis button").catch((error) => {
      appendEvent("Refresh failed", error.message, "block");
      render();
    });
  });
  const chatForm = view.querySelector("#jarvisChatForm");
  const chatInput = view.querySelector("#jarvisMessageInput");
  chatForm?.addEventListener("submit", (event) => {
    event.preventDefault();
    const value = chatInput?.value || "";
    chatInput.value = "";
    handleGlobalSubmit(value, pendingAttachments.length ? "Jarvis chat with file transfer" : "Jarvis chat");
  });
  chatInput?.addEventListener("keydown", (event) => {
    if ((event.metaKey || event.ctrlKey) && event.key === "Enter") {
      event.preventDefault();
      chatForm?.requestSubmit();
    }
  });
  view.querySelector("#jarvisFileInput")?.addEventListener("change", handleFiles);
  view.querySelectorAll("[data-remove-attachment]").forEach((button) => {
    button.addEventListener("click", () => {
      pendingAttachments = pendingAttachments.filter((attachment) => attachment.id !== button.dataset.removeAttachment);
      appendEvent("Attachment removed", "Pending Jarvis attachment was removed before send.", "warn");
      render();
    });
  });
  document.querySelector("#exportChat")?.addEventListener("click", exportChatHistory);
  document.querySelector("#clearChat")?.addEventListener("click", clearChatHistory);
  view.querySelectorAll(".packet-download").forEach((button) => {
    button.addEventListener("click", () => downloadPacket(button.dataset.packet));
  });
}

function submitVoiceFallback() {
  const input = view.querySelector("#voiceTranscriptPreview");
  const transcript = (input?.value || voiceTranscriptPreview || voiceFallbackDraft).trim();
  if (!transcript) return;
  appendEvent("Manual transcript submitted", "Manual fallback used the Jarvis chat processing path.", "ok");
  handleGlobalSubmit(transcript, "manual transcript fallback");
  voiceFallbackDraft = "";
  voiceTranscriptPreview = "";
  localStorage.removeItem(storageKeys.voiceTranscriptPreview);
  if (input) input.value = "";
}

function startVoice() {
  if (voiceModeDisabled) {
    appendEvent("Voice disabled", "Voice mode is disabled for this dashboard. Use text chat and file attachments.", "warn");
    return;
  }
  const state = document.querySelector("#voiceState");
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    state.textContent = "Speech recognition is not available in this browser. Use the manual transcript fallback or the bottom input field.";
    appendEvent("Voice unavailable", "Browser speech recognition API is not available.", "warn");
    return;
  }

  const recognition = new SpeechRecognition();
  recognition.lang = "en-US";
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;
  activeRecognition = recognition;
  state.textContent = "Requesting browser microphone permission. If blocked, use manual transcript fallback.";
  recognition.onstart = () => {
    voiceAuthorized = true;
    localStorage.setItem(storageKeys.voiceAuthorized, "true");
    setLiveStatus("Jarvis listening", "ok");
    startVoiceTimer();
    state.textContent = "Transcribing. Speak one command or one interview answer, then review the editable preview.";
    appendEvent("Voice listening started", "Browser speech recognition started. This proves the browser accepted the listening request for this session.", "ok");
  };
  recognition.onresult = (event) => {
    const transcript = event.results?.[0]?.[0]?.transcript || "";
    voiceTranscriptPreview = transcript;
    voiceFallbackDraft = transcript;
    localStorage.setItem(storageKeys.voiceTranscriptPreview, transcript);
    const preview = document.querySelector("#voiceTranscriptPreview");
    if (preview) preview.value = transcript;
    state.textContent = "Transcript captured. Edit the preview, then send transcript.";
    appendEvent("Voice transcript captured", "Authorized browser transcript is waiting for review in the editable preview.", "ok");
  };
  recognition.onnomatch = () => {
    state.textContent = "No clear speech was detected. Use manual transcript fallback or try again.";
    appendEvent("Voice no match", "Speech recognition ended without a confident transcript.", "warn");
  };
  recognition.onerror = (event) => {
    const message = voiceErrorMessage(event.error);
    activeRecognition = null;
    stopVoiceTimer();
    if (event.error === "not-allowed" || event.error === "service-not-allowed") {
      voiceAuthorized = false;
      localStorage.removeItem(storageKeys.voiceAuthorized);
    }
    state.textContent = message;
    setLiveStatus("Voice fallback ready", "warn");
    appendEvent("Voice fallback ready", message, "warn");
  };
  recognition.onend = () => {
    stopVoiceTimer();
    activeRecognition = null;
    if (state.textContent === "Transcribing. Speak one command or one interview answer, then review the editable preview.") {
      state.textContent = "Voice stopped without a transcript. Use manual transcript fallback or try again.";
    }
    setLiveStatus("Static polling active", "warn");
  };
  try {
    recognition.start();
  } catch (error) {
    const message = voiceErrorMessage(error?.message || "start failed");
    state.textContent = message;
    setLiveStatus("Voice fallback ready", "warn");
    appendEvent("Voice start failed", message, "warn");
  }
}

function voiceErrorMessage(errorCode) {
  const code = String(errorCode || "unknown");
  const messages = {
    network: "Voice recognition network service is unavailable in this browser. Use manual transcript fallback now; no audio was stored.",
    "not-allowed": "Microphone permission was denied. Enable browser microphone access or use manual transcript fallback.",
    "service-not-allowed": "The browser blocked the speech recognition service. Use manual transcript fallback or an approved local/provider voice runtime later.",
    "audio-capture": "No microphone input was captured. Check the selected device or use manual transcript fallback.",
    "no-speech": "No speech was detected. Try again or type the transcript manually.",
    aborted: "Voice recognition was stopped. Use manual transcript fallback if this was unintended."
  };
  return messages[code] || `Voice recognition failed (${code}). Use manual transcript fallback or text input; no raw audio is stored.`;
}

function formatVoiceTimer(seconds = voiceElapsedSeconds) {
  const mins = String(Math.floor(seconds / 60)).padStart(2, "0");
  const secs = String(seconds % 60).padStart(2, "0");
  return `${mins}:${secs}`;
}

function startVoiceTimer() {
  stopVoiceTimer(false);
  voiceStartedAt = Date.now();
  voiceElapsedSeconds = 0;
  const update = () => {
    voiceElapsedSeconds = Math.floor((Date.now() - voiceStartedAt) / 1000);
    const timer = document.querySelector("#voiceTimer");
    if (timer) timer.textContent = formatVoiceTimer();
  };
  update();
  voiceTimerId = window.setInterval(update, 1000);
}

function stopVoiceTimer(reset = false) {
  if (voiceTimerId) window.clearInterval(voiceTimerId);
  voiceTimerId = null;
  if (reset) {
    voiceStartedAt = null;
    voiceElapsedSeconds = 0;
  }
  const timer = document.querySelector("#voiceTimer");
  if (timer) timer.textContent = formatVoiceTimer();
}

function stopVoiceRecognition(reason = "Voice recognition stopped") {
  if (activeRecognition) {
    try {
      activeRecognition.stop();
    } catch {
      // Browser recognition can throw after it has already ended.
    }
  }
  activeRecognition = null;
  stopVoiceTimer();
  setLiveStatus("Voice stopped", "warn");
  appendEvent("Voice stopped", reason, "warn");
  const state = document.querySelector("#voiceState");
  if (state) state.textContent = reason;
}

function cancelVoiceTranscript() {
  stopVoiceRecognition("Voice capture canceled. Transcript preview cleared.");
  voiceTranscriptPreview = "";
  voiceFallbackDraft = "";
  localStorage.removeItem(storageKeys.voiceTranscriptPreview);
  const input = document.querySelector("#voiceTranscriptPreview");
  if (input) input.value = "";
}

function fileLooksText(file) {
  const name = String(file.name || "").toLowerCase();
  return Boolean(
    (file.type || "").startsWith("text/")
    || [
      ".md", ".txt", ".csv", ".json", ".yaml", ".yml", ".xml", ".html", ".css", ".js", ".ts", ".tsx", ".jsx", ".py", ".toml", ".log"
    ].some((extension) => name.endsWith(extension))
  );
}

function readFileTextExcerpt(file, maxChars = 6000) {
  if (!fileLooksText(file)) {
    return Promise.resolve("");
  }
  return new Promise((resolve) => {
    const reader = new FileReader();
    const blob = file.slice(0, Math.min(file.size, maxChars * 4));
    reader.onload = () => resolve(String(reader.result || "").slice(0, maxChars));
    reader.onerror = () => resolve("");
    reader.readAsText(blob);
  });
}

function formatFileSize(size) {
  const bytes = Number(size || 0);
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
}

async function handleFiles(event) {
  const files = Array.from(event.target.files || []);
  for (const file of files.slice(0, 6)) {
    const textExcerpt = await readFileTextExcerpt(file);
    const attachment = {
      id: makeId("attachment"),
      name: file.name || "unnamed file",
      mime_type: file.type || "unknown",
      size: file.size,
      transfer_mode: textExcerpt ? "text_excerpt" : "metadata_only",
      text_excerpt: textExcerpt,
    };
    pendingAttachments = [attachment, ...pendingAttachments].slice(0, 6);
    const packet = createLocalPacket(
      "file-transfer-check",
      "local browser file transfer",
      textExcerpt
        ? "File selected for Jarvis chat. The dashboard prepared a bounded text excerpt for the next API message and did not write it durably."
        : "File selected for Jarvis chat. The dashboard prepared metadata only for the next API message.",
      {
        extra: {
          file_name: attachment.name,
          file_type: attachment.mime_type,
          file_size: attachment.size,
          transfer_mode: attachment.transfer_mode,
          privacy: "session attachment only; no durable dashboard writeback",
        },
      },
    );
    appendEvent("File transfer prepared", `${attachment.name} staged as ${packet.id}.`, "ok");
  }
  render();
  event.target.value = "";
}

function renderHistory() {
  view.innerHTML = `
    <section class="panel">
      <div class="section-header">
        <div>
          <h2 class="section-title">Chat History</h2>
          <p class="muted">Full persistent browser-local conversation with Jarvis. Export before turning it into a Codex-reviewed packet. Clear only removes the local browser copy.</p>
        </div>
        <div class="row-actions">
          <button class="primary" id="historyExport" type="button">Export chat packet</button>
          <button class="button" id="historyClear" type="button">Clear persistent history</button>
        </div>
      </div>
      <div class="chat-thread expanded">
        ${chatHistory.length ? chatHistory.map((message) => `
          <article class="chat-message ${escapeHtml(message.role)}">
            <div class="chat-meta">${escapeHtml(message.role)} - ${escapeHtml(message.source)} - ${new Date(message.time).toLocaleString()}</div>
            <p>${escapeHtml(message.text)}</p>
          </article>
        `).join("") : `<div class="callout">No persistent chat history in this browser.</div>`}
      </div>
    </section>
  `;
  document.querySelector("#historyExport")?.addEventListener("click", exportChatHistory);
  document.querySelector("#historyClear")?.addEventListener("click", clearChatHistory);
}

function renderSchema(data) {
  const kind = setActiveSchema();
  applyInitialPanelDeepLink();
  const meta = schemaScreenMeta[kind];
  const selected = getSchemaNode(blockSchema.selectedNodeId) || blockSchema.nodes[0];
  if (selected && blockSchema.selectedNodeId !== selected.id) blockSchema.selectedNodeId = selected.id;
  const validation = validateBlockSchema();
  const canvasWidth = Math.max(2160, ...blockSchema.nodes.map((node) => node.x + node.w + 80));
  const canvasHeight = Math.max(780, ...blockSchema.nodes.map((node) => node.y + node.h + 80));
  const edgeSvg = renderBlockSchemaEdges(canvasWidth, canvasHeight);

  view.innerHTML = `
    <section class="panel schema-shell">
      <div class="section-header">
        <div>
          <h2 class="section-title">${escapeHtml(meta.title)}</h2>
          <p class="muted">${escapeHtml(meta.subtitle)} Click a node to open its full control panel; drag blocks, connect routes, validate the graph, and export a review packet.</p>
          ${architectureSelectorMarkup("schema")}
        </div>
        <div class="row-actions">
          <button class="button ${kind === "service" ? "active-soft" : ""}" data-architecture="service" type="button">Screen 1</button>
          <button class="button ${kind === "control" ? "active-soft" : ""}" data-architecture="control" type="button">Screen 2</button>
          <button class="button schema-add" data-type="agent" type="button">Local agent</button>
          <button class="button schema-add" data-type="router" type="button">Local router</button>
          <button class="button schema-add" data-type="parallel" type="button">Local parallel</button>
          <button class="button schema-add" data-type="approval" type="button">Local approval</button>
          <button class="button" id="schemaConnect" type="button">${blockSchemaConnectSource ? "Cancel local connect" : "Local connect"}</button>
          <button class="button" id="schemaLayout" type="button">Local layout</button>
          <button class="button" id="schemaZoomOut" type="button">Zoom out</button>
          <button class="button" id="schemaZoomIn" type="button">Zoom in</button>
          <button class="button" id="schemaZoomReset" type="button">Reset zoom</button>
          <button class="button" id="schemaZoomFit" type="button">Fit</button>
          <button class="button" id="schemaBackendSend" type="button">Send to backend</button>
          <button class="primary" id="schemaExport" type="button">Export review packet</button>
        </div>
      </div>

      <div class="callout" id="schemaBackendStatus">Backend send is provider-disabled and creates a review packet only. Durable writes still require Codex/operator approval.</div>

      <div class="schema-stage-rail" aria-label="Workflow stage rail">
        ${(kind === "service"
          ? ["Intake", "PRD", "Evidence", "ICP", "Demo", "CrewAI Proof", "Approval", "Output"]
          : ["Command", "Route", "Develop", "Review", "CrewAI Proof", "Merge", "Approval", "Record"]
        ).map((stage, index) => `<span><strong>${index + 1}</strong>${escapeHtml(stage)}</span>`).join("")}
      </div>

      <div class="schema-status">
        <span>${badge(validation.errors.length ? "blocked" : validation.warnings.length ? "needs review" : "valid")}</span>
        <span>${badge("static browser local")}</span>
        <span>${badge("browser-local edits only")}</span>
        <span>${badge("MODEL_PROVIDER none")}</span>
        <span>${badge(`zoom ${Math.round(schemaZoom * 100)}%`)}</span>
        <span>${escapeHtml(blockSchemaConnectSource ? `Connect mode: source is ${getSchemaNode(blockSchemaConnectSource)?.title || "unknown"}. Choose target.` : "Click a block to open its control panel. Drag selected blocks to reposition.")}</span>
      </div>

      <div class="schema-layer-brief">
        ${[
          ["Job", kind === "service" ? "Make PRD/ICP output understandable and buyer-reviewable." : "Make local agent work observable, configurable, and approval-gated."],
          ["Pain", kind === "service" ? "Product evidence and ICP decisions get mixed with internal agent machinery." : "Parallel agents, providers, memory, and writes become unsafe when hidden behind one vague action."],
          ["Boundary", "Static UI creates local review packets only. No secrets, raw transcripts, provider calls, backend writes, or deployment actions run here."],
          ["Confidence", validation.errors.length ? "Medium: schema still has blocking validation errors." : validation.warnings.length ? "Medium-high: warnings need reviewer attention." : "High for static review UI; runtime execution remains gated."]
        ].map(([label, value]) => `<div><strong>${escapeHtml(label)}</strong><span>${escapeHtml(value)}</span></div>`).join("")}
      </div>

      <div class="schema-runtime-gates">
        <span>Runtime gate: provider disabled</span>
        <span>Runtime gate: backend absent</span>
        <span>Runtime gate: CrewAI Level 3 proof passed, not default runtime</span>
        <span>Runtime gate: writeback approval required</span>
        <span>Runtime gate: public-safe sources only</span>
      </div>

      <div class="schema-node-strip" aria-label="Node index">
        ${blockSchema.nodes.map((node) => `
          <button class="schema-node-jump ${node.id === blockSchema.selectedNodeId ? "active" : ""}" type="button" data-node-jump="${escapeHtml(node.id)}">
            <strong>${escapeHtml(node.title)}</strong>
            <span>${escapeHtml(schemaTypeLabel(node.type))} - ${escapeHtml(node.config?.modelProvider || "none")}</span>
          </button>
        `).join("")}
      </div>

      <div class="schema-workspace">
        <div class="schema-canvas-wrap">
          <div class="schema-canvas" id="schemaCanvas" style="width:${canvasWidth}px;height:${canvasHeight}px;transform:scale(${schemaZoom});transform-origin:top left;">
            <svg class="schema-edge-layer" width="${canvasWidth}" height="${canvasHeight}" viewBox="0 0 ${canvasWidth} ${canvasHeight}" aria-hidden="true">${edgeSvg}</svg>
            ${blockSchema.nodes.map((node) => renderSchemaNode(node)).join("")}
          </div>
        </div>

        <aside class="schema-inspector">
          <div class="schema-tabs">
            <button class="active" type="button">Node</button>
            <button type="button" id="schemaValidateFocus">Validation</button>
            <button type="button" id="schemaLangSmithFocus">Tracing</button>
          </div>
          ${selected ? renderSchemaInspector(selected) : `<div class="callout">Select or add a block to edit it.</div>`}
        </aside>
      </div>
    </section>

    <div class="grid cols-2" style="margin-top:16px">
      <section class="panel">
        <h2 class="section-title">Validation And Review Queue</h2>
        <ul class="schema-validation" id="schemaValidation">
          ${validation.errors.map((item) => `<li class="blocker">ERROR: ${escapeHtml(item)}</li>`).join("")}
          ${validation.warnings.map((item) => `<li>WARNING: ${escapeHtml(item)}</li>`).join("")}
          ${!validation.errors.length && !validation.warnings.length ? `<li class="ok">OK: graph is ready for review export.</li>` : ""}
        </ul>
        <div class="row-actions">
          <button class="button" id="schemaQueueSelected" type="button">Queue local node</button>
          <button class="button" id="schemaReset" type="button">Reset local schema</button>
        </div>
      </section>
      <section class="panel">
        <h2 class="section-title">LangGraph / CrewAI / LangSmith Trace Prep</h2>
        ${table(["Layer", "Traceable state", "Boundary"], [
          ["LangGraph", "node id, route key, approval state, blocker, output link", "No raw private prompts or recordings"],
          ["CrewAI", "agent role, task, proof status, ledger path, handoff file, reviewer verdict", "Level 3 proof passed; not default/provider runtime; no autonomous writeback"],
          ["LangSmith", "sanitized run metadata, node names, trace URL placeholder", "LANGSMITH_API_KEY not exposed or activated here"],
          ["Codex", "review branch, changed files, checks, run note", "Local operator/editor only"],
        ].map((row) => row.map(escapeHtml)))}
      </section>
    </div>
    ${kind === "service" ? renderPrdIcpRequestSurface() + renderPrdIcpOutputBlocks() : renderTaskStages() + renderRoleConfigPanels()}
    ${nodeControlPanelId ? renderNodeControlPanel(getSchemaNode(nodeControlPanelId)) : ""}
  `;

  bindSchemaEditor();
  bindArchitectureSelectors(view);
}

function renderBlockSchemaEdges(width, height) {
  const defs = `
    <defs>
      <marker id="schemaArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#5b6673"></path>
      </marker>
    </defs>
  `;
  const paths = blockSchema.edges.map((edge) => {
    const from = getSchemaNode(edge.from);
    const to = getSchemaNode(edge.to);
    if (!from || !to) return "";
    const a = schemaCenter(from);
    const b = schemaCenter(to);
    const mid = (a.x + b.x) / 2;
    const d = `M ${a.x} ${a.y} C ${mid} ${a.y}, ${mid} ${b.y}, ${b.x} ${b.y}`;
    const labelX = mid;
    const labelY = (a.y + b.y) / 2 - 8;
    return `
      <path d="${d}" fill="none" stroke="#5b6673" stroke-width="2.2" marker-end="url(#schemaArrow)"></path>
      <text x="${labelX}" y="${labelY}" text-anchor="middle" class="schema-edge-label">${escapeHtml(edge.label || edge.mode || "route")}</text>
    `;
  }).join("");
  return `${defs}<rect width="${width}" height="${height}" fill="transparent"></rect>${paths}`;
}

function renderSchemaNode(node) {
  const selected = node.id === blockSchema.selectedNodeId;
  const inCount = incomingSchemaEdges(node.id).length;
  const outCount = outgoingSchemaEdges(node.id).length;
  const config = node.config || {};
  return `
    <article class="schema-node ${escapeHtml(node.type)} ${selected ? "selected" : ""}" role="button" tabindex="0" aria-label="Open ${escapeHtml(node.title)} control panel" data-node-id="${escapeHtml(node.id)}" style="transform:translate(${node.x}px, ${node.y}px);width:${node.w}px;height:${node.h}px">
      <div class="schema-node-head">
        <strong>${escapeHtml(node.title)}</strong>
        <span>${escapeHtml(schemaTypeLabel(node.type))}</span>
      </div>
      <p>${escapeHtml(node.prompt || "No prompt configured.").slice(0, 150)}</p>
      <div class="schema-node-meta">
        <span>${escapeHtml(node.owner || "Unassigned")}</span>
        <span>routes ${inCount} in / ${outCount} out</span>
      </div>
      <div class="schema-node-meta">
        <span>ports ${(node.inputs || []).length} in / ${(node.outputs || []).length} out</span>
        <span>${escapeHtml(node.status || "planned")}</span>
      </div>
      <div class="schema-node-output">${escapeHtml(node.finalOutput || "Pending output").slice(0, 110)}</div>
    </article>
  `;
}

function renderSchemaInspector(node) {
  const incoming = incomingSchemaEdges(node.id);
  const outgoing = outgoingSchemaEdges(node.id);
  return `
    <div class="schema-summary">
      <h3>${escapeHtml(node.title)}</h3>
      <p>${escapeHtml(node.description || node.prompt || "No description configured.")}</p>
      <dl>
        <div><dt>Layer</dt><dd>${escapeHtml(node.workflowLayer || "not set")}</dd></div>
        <div><dt>Owner</dt><dd>${escapeHtml(node.owner || "Unassigned")}</dd></div>
        <div><dt>Status</dt><dd>${escapeHtml(node.status || "planned")}</dd></div>
        <div><dt>Provider</dt><dd>${escapeHtml(node.config?.modelProvider || "none")}</dd></div>
        <div><dt>Inputs</dt><dd>${incoming.length} connections, ${(node.inputs || []).length} ports</dd></div>
        <div><dt>Outputs</dt><dd>${outgoing.length} connections, ${(node.outputs || []).length} ports</dd></div>
      </dl>
      <div class="schema-move-controls" aria-label="Move selected node">
        <button class="button schema-move" type="button" data-dx="0" data-dy="-40">Up</button>
        <button class="button schema-move" type="button" data-dx="-40" data-dy="0">Left</button>
        <button class="button schema-move" type="button" data-dx="40" data-dy="0">Right</button>
        <button class="button schema-move" type="button" data-dx="0" data-dy="40">Down</button>
      </div>
      <div class="row-actions">
        <button class="primary" id="nodePanelOpen" type="button">Open control panel</button>
        <button class="button" id="schemaDuplicateNode" type="button">Duplicate local</button>
        <button class="button" id="schemaDeleteNode" type="button">Delete local draft</button>
      </div>
    </div>
  `;
}

function renderNodeControlPanel(node) {
  const incoming = incomingSchemaEdges(node.id);
  const outgoing = outgoingSchemaEdges(node.id);
  const tabs = ["Overview", "Inputs", "Outputs", "Connections", "Config", "Logs", "Prompts", "Comments", "Safety"];
  return `
    <div class="node-panel-backdrop" role="presentation">
      <section class="node-panel" role="dialog" aria-modal="true" aria-labelledby="nodePanelTitle">
        <form id="nodeControlPanelForm">
          <header class="node-panel-header">
            <div>
              <div class="panel-eyebrow">${escapeHtml(blockSchema.title)}</div>
              <h2 id="nodePanelTitle">${escapeHtml(node.title)}</h2>
              <p>${escapeHtml(node.job || "Configure this node for the selected workflow layer.")}</p>
              <div class="node-panel-quick-facts" aria-label="Node operating facts">
                <span>${escapeHtml(node.workflowLayer || "workflow layer unset")}</span>
                <span>${escapeHtml(incoming.length)} inputs</span>
                <span>${escapeHtml(outgoing.length)} outputs</span>
                <span>MODEL PROVIDER ${escapeHtml(node.config?.modelProvider || "none")}</span>
                <span>${escapeHtml(node.config?.approvalGate || "approval gate unset")}</span>
              </div>
            </div>
            <div class="row-actions">
              <button class="primary" type="submit">Save local node</button>
              <button class="button" id="nodePanelQueue" type="button">Queue local node</button>
              <button class="button" id="nodePanelClose" type="button">Close</button>
            </div>
          </header>
          <nav class="node-panel-tabs" aria-label="Node control panel sections">
            ${tabs.map((tab) => `<button class="node-panel-tab" type="button" data-panel-target="nodePanel${tab}">${tab}</button>`).join("")}
          </nav>
          <div class="node-panel-body">
            <section class="node-panel-section node-panel-overview" id="nodePanelOverview">
              <h3>Overview</h3>
              <div class="grid cols-3">
                <div class="row"><span class="row-title">Job</span><div class="row-meta">${escapeHtml(node.job || "No job defined.")}</div></div>
                <div class="row"><span class="row-title">Pain Reduced</span><div class="row-meta">${escapeHtml(node.pain || "No risk defined.")}</div></div>
                <div class="row"><span class="row-title">Evidence</span><div class="row-meta">${escapeHtml(node.evidence || "Evidence pending.")}</div></div>
              </div>
              <div class="schema-runtime-gates compact">
                <span>Provider calls require approval</span>
                <span>Raw capture blocked</span>
                <span>Writeback requires approval</span>
                <span>Export creates local packet</span>
              </div>
            </section>

            <section class="node-panel-section" id="nodePanelInputs">
              <h3>Inputs</h3>
              <div class="control-grid">
                <label>Title<input id="nodeTitleInput" value="${escapeHtml(node.title)}" /></label>
                <label>Type<select id="nodeTypeInput">
                  ${["start", "agent", "router", "parallel", "merge", "approval", "output"].map((type) => `<option value="${type}" ${node.type === type ? "selected" : ""}>${schemaTypeLabel(type)}</option>`).join("")}
                </select></label>
                <label>Owner / agent<input id="nodeOwnerInput" value="${escapeHtml(node.owner || "")}" /></label>
                <label>Status<select id="nodeStatusInput">
                  ${["planned", "active", "waiting", "blocked", "done"].map((status) => `<option value="${status}" ${node.status === status ? "selected" : ""}>${status}</option>`).join("")}
                </select></label>
              </div>
              <label>Input ports<textarea id="nodeInputsInput" rows="5">${escapeHtml(textareaFromList(node.inputs))}</textarea></label>
              <div class="connection-list">
                ${incoming.length ? incoming.map((edge) => `<div><strong>${escapeHtml(getSchemaNode(edge.from)?.title || edge.from)}</strong><span>${escapeHtml(edge.label || "input")} - ${escapeHtml(edge.condition || "no condition")}</span></div>`).join("") : `<div><span>No incoming connections yet.</span></div>`}
              </div>
            </section>

            <section class="node-panel-section" id="nodePanelOutputs">
              <h3>Outputs</h3>
              <label>Final output<textarea id="nodeFinalOutputInput" rows="3">${escapeHtml(node.finalOutput || "")}</textarea></label>
              <label>Output ports<textarea id="nodeOutputsInput" rows="5">${escapeHtml(textareaFromList(node.outputs))}</textarea></label>
              <label>Possible outputs<textarea id="nodePossibleOutputsInput" rows="4">${escapeHtml(textareaFromList(node.possibleOutputs))}</textarea></label>
              <label>Output links<textarea id="nodeOutputLinksInput" rows="3">${escapeHtml(textareaFromList(node.outputLinks))}</textarea></label>
            </section>

            <section class="node-panel-section" id="nodePanelConnections">
              <h3>Connections</h3>
              <p class="muted">Connection settings stay browser-local until exported. Use Connect blocks on the canvas to add routes.</p>
              <div class="edge-editor-list">
                ${[...incoming, ...outgoing].length ? [...incoming, ...outgoing].map((edge) => renderEdgeEditor(edge, edge.to === node.id ? "input" : "output")).join("") : `<div class="callout">No route connected to this node yet.</div>`}
              </div>
            </section>

            <section class="node-panel-section" id="nodePanelConfig">
              <h3>Configuration</h3>
              <div class="control-grid">
                ${renderConfigDropdowns(node)}
              </div>
            </section>

            <section class="node-panel-section" id="nodePanelLogs">
              <h3>Last Runs</h3>
              <label>Interpreted run log<textarea id="nodeLastRunsInput" rows="7">${escapeHtml((node.lastRuns || []).map((run) => `${run.time} | ${run.status} | ${run.summary}`).join("\n"))}</textarea></label>
              <div class="callout compact">Static mode records interpreted summaries only. Raw transcripts, recordings, private document bodies, and provider traces are not persisted here.</div>
            </section>

            <section class="node-panel-section" id="nodePanelPrompts">
              <h3>Prompts</h3>
              <label>Operating prompt<textarea id="nodePromptInput" rows="5">${escapeHtml(node.prompt || "")}</textarea></label>
              <label>System prompt<textarea id="nodeSystemPromptInput" rows="6">${escapeHtml(node.systemPrompt || "")}</textarea></label>
              <label>Requirements<textarea id="nodeRequirementsInput" rows="4">${escapeHtml(node.requirements || "")}</textarea></label>
            </section>

            <section class="node-panel-section" id="nodePanelComments">
              <h3>Comments</h3>
              <label>Description<textarea id="nodeDescriptionInput" rows="4">${escapeHtml(node.description || "")}</textarea></label>
              <label>Developer comments<textarea id="nodeCommentsInput" rows="5">${escapeHtml(node.comments || "")}</textarea></label>
              <label>Files owned/touched<textarea id="nodeFilesInput" rows="4">${escapeHtml(textareaFromList(node.files))}</textarea></label>
              <label>Questions covered<textarea id="nodeQuestionsInput" rows="4">${escapeHtml(textareaFromList(node.questions))}</textarea></label>
            </section>

            <section class="node-panel-section" id="nodePanelSafety">
              <h3>Safety And Business Fit</h3>
              <label>Job to be done<textarea id="nodeJobInput" rows="3">${escapeHtml(node.job || "")}</textarea></label>
              <label>Pain / risk reduced<textarea id="nodePainInput" rows="3">${escapeHtml(node.pain || "")}</textarea></label>
              <label>Evidence<textarea id="nodeEvidenceInput" rows="4">${escapeHtml(node.evidence || "")}</textarea></label>
              <label>Business objective<textarea id="nodeBusinessObjectiveInput" rows="3">${escapeHtml(node.businessObjective || "")}</textarea></label>
              <div class="callout compact">Provider calls, writeback, deployment, raw capture, and third-party tool installation require explicit approval and verification before execution.</div>
            </section>
          </div>
        </form>
      </section>
    </div>
  `;
}

function renderConfigDropdowns(node) {
  const options = configOptions();
  return Object.entries(options).map(([key, values]) => {
    const current = node.config?.[key] || defaultNodeConfig(node.type, node.workflowLayer)[key] || values[0];
    return `
      <label>${escapeHtml(key.replace(/([A-Z])/g, " $1").toLowerCase())}
        <select class="node-config-select" data-config-key="${escapeHtml(key)}">
          ${values.map((value) => `<option value="${escapeHtml(value)}" ${current === value ? "selected" : ""}>${escapeHtml(value)}</option>`).join("")}
        </select>
      </label>
    `;
  }).join("");
}

function renderEdgeEditor(edge, direction) {
  const from = getSchemaNode(edge.from);
  const to = getSchemaNode(edge.to);
  return `
    <fieldset class="edge-editor" data-edge-id="${escapeHtml(edge.id)}">
      <legend>${escapeHtml(direction)}: ${escapeHtml(from?.title || edge.from)} -> ${escapeHtml(to?.title || edge.to)}</legend>
      <label>Label<input class="edge-label-input" value="${escapeHtml(edge.label || "")}" /></label>
      <label>Mode<select class="edge-mode-input">
        ${["normal", "conditional", "parallel", "merge", "approval"].map((mode) => `<option value="${mode}" ${edge.mode === mode ? "selected" : ""}>${mode}</option>`).join("")}
      </select></label>
      <label>Condition<textarea class="edge-condition-input" rows="2">${escapeHtml(edge.condition || "")}</textarea></label>
    </fieldset>
  `;
}

function bindSchemaEditor() {
  const activateSchemaNode = (nodeId) => {
    const node = getSchemaNode(nodeId);
    if (!node) return;
    if (blockSchemaConnectSource && blockSchemaConnectSource !== node.id) {
      blockSchema.edges.push(schemaEdge(makeId("schema-edge"), blockSchemaConnectSource, node.id, "next", "Selected in dashboard editor.", "normal"));
      blockSchemaConnectSource = null;
      appendEvent("Schema blocks connected", "A local block-schema connection was added.", "ok");
    } else if (blockSchemaConnectSource === node.id) {
      blockSchemaConnectSource = null;
    } else {
      blockSchema.selectedNodeId = node.id;
      nodeControlPanelId = node.id;
    }
    saveBlockSchema();
    render();
  };

  view.querySelectorAll(".schema-node").forEach((element) => {
    element.addEventListener("pointerdown", (event) => {
      const node = getSchemaNode(element.dataset.nodeId);
      if (!node) return;
      blockSchema.selectedNodeId = node.id;
      blockSchemaDrag = {
        id: node.id,
        startX: event.clientX,
        startY: event.clientY,
        nodeX: node.x,
        nodeY: node.y,
        moved: false
      };
      element.setPointerCapture?.(event.pointerId);
    });
    element.addEventListener("click", () => {
      if (blockSchemaDragMoved) {
        blockSchemaDragMoved = false;
        return;
      }
      activateSchemaNode(element.dataset.nodeId);
    });
    element.addEventListener("keydown", (event) => {
      if (event.key !== "Enter" && event.key !== " ") return;
      event.preventDefault();
      activateSchemaNode(element.dataset.nodeId);
    });
  });

  window.onpointermove = (event) => {
    if (!blockSchemaDrag) return;
    const node = getSchemaNode(blockSchemaDrag.id);
    if (!node) return;
    const dx = event.clientX - blockSchemaDrag.startX;
    const dy = event.clientY - blockSchemaDrag.startY;
    blockSchemaDrag.moved = Math.abs(dx) + Math.abs(dy) > 2;
    if (blockSchemaDrag.moved) blockSchemaDragMoved = true;
    node.x = Math.max(0, blockSchemaDrag.nodeX + dx);
    node.y = Math.max(0, blockSchemaDrag.nodeY + dy);
    const block = view.querySelector(`[data-node-id="${CSS.escape(node.id)}"]`);
    if (block) block.style.transform = `translate(${node.x}px, ${node.y}px)`;
  };

  window.onpointerup = () => {
    if (!blockSchemaDrag) return;
    if (blockSchemaDrag.moved) blockSchemaDragMoved = true;
    saveBlockSchema();
    blockSchemaDrag = null;
    render();
  };

  view.querySelectorAll(".schema-add").forEach((button) => {
    button.addEventListener("click", () => {
      const type = button.dataset.type || "agent";
      const node = draftSchemaNode(type);
      blockSchema.nodes.push(node);
      blockSchema.selectedNodeId = node.id;
      saveBlockSchema();
      render();
    });
  });

  view.querySelectorAll(".schema-node-jump").forEach((button) => {
    button.addEventListener("click", () => {
      const node = getSchemaNode(button.dataset.nodeJump);
      if (!node) return;
      blockSchema.selectedNodeId = node.id;
      nodeControlPanelId = node.id;
      saveBlockSchema();
      render();
    });
  });

  view.querySelector("#schemaConnect")?.addEventListener("click", () => {
    blockSchemaConnectSource = blockSchemaConnectSource ? null : blockSchema.selectedNodeId;
    render();
  });

  view.querySelector("#schemaLayout")?.addEventListener("click", () => {
    layoutBlockSchemaByStage();
    saveBlockSchema();
    render();
  });
  view.querySelector("#schemaZoomOut")?.addEventListener("click", () => setSchemaZoom(schemaZoom - 0.1));
  view.querySelector("#schemaZoomIn")?.addEventListener("click", () => setSchemaZoom(schemaZoom + 0.1));
  view.querySelector("#schemaZoomReset")?.addEventListener("click", () => setSchemaZoom(1));
  view.querySelector("#schemaZoomFit")?.addEventListener("click", () => setSchemaZoom(0.72));

  view.querySelector("#schemaExport")?.addEventListener("click", exportBlockSchemaPacket);
  view.querySelector("#schemaBackendSend")?.addEventListener("click", sendBlockSchemaToBackend);
  view.querySelector("#schemaQueueSelected")?.addEventListener("click", queueSelectedSchemaNode);
  view.querySelector("#schemaReset")?.addEventListener("click", () => {
    const kind = schemaKindForActiveTab();
    blockSchema = normalizeBlockSchema(kind === "service" ? defaultServiceBlockSchema() : defaultBlockSchema(), kind);
    blockSchemas[kind] = blockSchema;
    nodeControlPanelId = null;
    saveBlockSchema();
    appendEvent("Block schema reset", schemaScreenMeta[kind].resetEvent, "warn");
    render();
  });

  view.querySelectorAll(".schema-move").forEach((button) => {
    button.addEventListener("click", () => {
      moveSelectedSchemaNode(Number(button.dataset.dx || 0), Number(button.dataset.dy || 0));
    });
  });
  view.querySelector("#nodePanelOpen")?.addEventListener("click", () => {
    nodeControlPanelId = blockSchema.selectedNodeId;
    render();
  });
  view.querySelector("#schemaDuplicateNode")?.addEventListener("click", duplicateSchemaNode);
  view.querySelector("#schemaDeleteNode")?.addEventListener("click", deleteSchemaNode);
  view.querySelector("#schemaValidateFocus")?.addEventListener("click", () => view.querySelector("#schemaValidation")?.scrollIntoView({ behavior: "smooth", block: "center" }));
  view.querySelector("#schemaLangSmithFocus")?.addEventListener("click", () => handleGlobalSubmit("Explain LangSmith trace setup for this block schema", "schema trace button"));
  bindPrdIcpRequestSurface();
  bindRoleConfigPanels();
  bindNodeControlPanel();
}

function setSchemaZoom(value) {
  schemaZoom = clamp(value, 0.55, 1.35);
  localStorage.setItem(storageKeys.schemaZoom, String(schemaZoom));
  appendEvent("Schema zoom changed", `Block schema zoom is now ${Math.round(schemaZoom * 100)}%.`, "ok");
  render();
}

function bindPrdIcpRequestSurface() {
  const input = view.querySelector("#prdComposerInput");
  const status = view.querySelector("#prdBackendStatus");
  if (!input) return;
  input.addEventListener("input", () => {
    prdComposerDraft = input.value;
    localStorage.setItem(storageKeys.prdComposer, prdComposerDraft);
  });
  view.querySelector("#prdStagePacket")?.addEventListener("click", () => {
    const packet = createLocalPacket("prd-icp-request", "Screen 1 PRD/ICP composer", input.value, {
      extra: {
        lane: "prd_icp_flow",
        required_blocks: prdIcpOutputBlocks().map(([title]) => title),
        backlog_required: true,
        missing_questions_required: true,
        test_fixture: "docs/testmeeting.md after owner approval",
      },
    });
    if (status) status.textContent = `Local packet staged: ${packet.id}.`;
    render();
  });
  view.querySelector("#prdSendBackend")?.addEventListener("click", async () => {
    const payload = {
      request: input.value,
      lane: "prd_icp_flow",
      architecture: architectureMode,
      approved_test_input: false,
      owner_approval: cloudApprovalRequested(input.value),
      provider_approval: cloudApprovalRequested(input.value),
      source_refs: ["sanitized E1.2.8 source packet", "approved discovery summary labels"],
    };
    if (status) status.textContent = "Sending to local backend if available...";
    try {
      await checkJarvisApi("PRD/ICP backend send", { silent: true });
      const response = await fetch(apiEndpoint("/api/lanes/prd-icp"), {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      if (!response.ok) throw new Error(`backend returned ${response.status}`);
      const result = await response.json();
      appendEvent("PRD/ICP backend response", result.status || "Backend returned a lane packet.", "ok");
      if (status) status.textContent = `Backend response: ${result.status || "ok"}.`;
    } catch (error) {
      const packet = createLocalPacket("prd-icp-request-backend-unavailable", "Screen 1 PRD/ICP composer", input.value, {
        extra: {
          backend_error: String(error.message || error),
          fallback: "preserved as browser-local review packet",
          provider_state: "disabled_until_owner_approval_and_budget_guard",
        },
      });
      if (status) status.textContent = `Backend unavailable; local packet staged: ${packet.id}.`;
      appendEvent("PRD/ICP backend unavailable", "Request preserved as a local review packet.", "warn");
      render();
    }
  });
}

function bindRoleConfigPanels() {
  if (!view.querySelector(".role-config-panel")) return;
  view.querySelector("#saveRoleConfig")?.addEventListener("click", () => {
    roleConfigs = Array.from(view.querySelectorAll(".role-config-card")).map((card) => {
      const existing = roleConfigs.find((role) => role.id === card.dataset.roleId) || {};
      const next = { ...existing };
      card.querySelectorAll("[data-field]").forEach((input) => {
        next[input.dataset.field] = input.value;
      });
      return next;
    });
    saveJson(storageKeys.roleConfig, roleConfigs);
    appendEvent("Role config saved locally", "Agent Orchestra role configuration was saved in browser localStorage only.", "ok");
    render();
  });
  view.querySelector("#exportRoleConfig")?.addEventListener("click", () => {
    const packet = createLocalPacket("agent-orchestra-role-config", "Screen 2 role configuration", "Export browser-local role config for Codex review.", {
      extra: {
        roles: roleConfigs,
        editable_fields: ["role objective", "responsibility", "tools", "model route", "budget mode", "output artifact", "review gate", "status", "handoff target"],
        write_policy: "browser cannot write raw files; backend or Codex review required",
      },
    });
    downloadPacket(packet.id);
  });
}

function bindNodeControlPanel() {
  const panel = view.querySelector("#nodeControlPanelForm");
  const closePanel = () => {
    nodeControlPanelId = null;
    render();
  };
  view.querySelector("#nodePanelClose")?.addEventListener("click", closePanel);
  view.querySelector(".node-panel-backdrop")?.addEventListener("click", (event) => {
    if (event.target === event.currentTarget) closePanel();
  });
  view.querySelector(".node-panel")?.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;
    event.preventDefault();
    closePanel();
  });
  view.querySelector("#nodePanelClose")?.focus();
  view.querySelector("#nodePanelQueue")?.addEventListener("click", () => {
    saveNodeControlPanel({ renderAfter: false });
    queueSelectedSchemaNode();
  });
  view.querySelectorAll(".node-panel-tab").forEach((button) => {
    button.addEventListener("click", () => {
      const target = view.querySelector(`#${CSS.escape(button.dataset.panelTarget || "")}`);
      target?.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
  panel?.addEventListener("submit", (event) => {
    event.preventDefault();
    saveNodeControlPanel();
  });
}

function parseLastRuns(value) {
  return listFromTextarea(value).map((line) => {
    const [time = "manual", status = "noted", ...rest] = line.split("|").map((part) => part.trim());
    return { time, status, summary: rest.join(" | ") || line };
  });
}

function saveNodeControlPanel({ renderAfter = true } = {}) {
  const node = getSchemaNode(nodeControlPanelId || blockSchema.selectedNodeId);
  if (!node) return null;
  node.title = view.querySelector("#nodeTitleInput")?.value.trim() || node.title;
  node.type = view.querySelector("#nodeTypeInput")?.value || node.type;
  node.owner = view.querySelector("#nodeOwnerInput")?.value.trim() || "Unassigned";
  node.status = view.querySelector("#nodeStatusInput")?.value || "planned";
  node.inputs = listFromTextarea(view.querySelector("#nodeInputsInput")?.value);
  node.finalOutput = view.querySelector("#nodeFinalOutputInput")?.value.trim() || "";
  node.outputs = listFromTextarea(view.querySelector("#nodeOutputsInput")?.value);
  node.possibleOutputs = listFromTextarea(view.querySelector("#nodePossibleOutputsInput")?.value);
  node.outputLinks = listFromTextarea(view.querySelector("#nodeOutputLinksInput")?.value);
  node.lastRuns = parseLastRuns(view.querySelector("#nodeLastRunsInput")?.value);
  node.prompt = view.querySelector("#nodePromptInput")?.value.trim() || "";
  node.systemPrompt = view.querySelector("#nodeSystemPromptInput")?.value.trim() || "";
  node.requirements = view.querySelector("#nodeRequirementsInput")?.value.trim() || "";
  node.description = view.querySelector("#nodeDescriptionInput")?.value.trim() || "";
  node.comments = view.querySelector("#nodeCommentsInput")?.value.trim() || "";
  node.files = listFromTextarea(view.querySelector("#nodeFilesInput")?.value);
  node.questions = listFromTextarea(view.querySelector("#nodeQuestionsInput")?.value);
  node.job = view.querySelector("#nodeJobInput")?.value.trim() || "";
  node.pain = view.querySelector("#nodePainInput")?.value.trim() || "";
  node.evidence = view.querySelector("#nodeEvidenceInput")?.value.trim() || "";
  node.businessObjective = view.querySelector("#nodeBusinessObjectiveInput")?.value.trim() || "";
  node.config = { ...(node.config || {}) };
  view.querySelectorAll(".node-config-select").forEach((select) => {
    node.config[select.dataset.configKey] = select.value;
  });
  node.workflowLayer = node.config.workflowLayer || node.workflowLayer;
  view.querySelectorAll(".edge-editor").forEach((editor) => {
    const edge = getSchemaEdge(editor.dataset.edgeId);
    if (!edge) return;
    edge.label = editor.querySelector(".edge-label-input")?.value.trim() || edge.label;
    edge.mode = editor.querySelector(".edge-mode-input")?.value || edge.mode;
    edge.condition = editor.querySelector(".edge-condition-input")?.value.trim() || "";
  });
  saveBlockSchema();
  appendEvent("Node control panel saved", `${node.title} configuration was saved in browser storage.`, "ok");
  if (renderAfter) render();
  return node;
}

function moveSelectedSchemaNode(dx, dy) {
  const node = getSchemaNode(blockSchema.selectedNodeId);
  if (!node) return;
  node.x = Math.max(0, node.x + dx);
  node.y = Math.max(0, node.y + dy);
  saveBlockSchema();
  appendEvent("Schema node moved", `${node.title} moved to x=${node.x}, y=${node.y}.`, "ok");
  render();
}

function duplicateSchemaNode() {
  const node = getSchemaNode(blockSchema.selectedNodeId);
  if (!node) return;
  const copy = JSON.parse(JSON.stringify(node));
  copy.id = makeId("schema-copy");
  copy.title = `${node.title} copy`;
  copy.x += 40;
  copy.y += 40;
  blockSchema.nodes.push(copy);
  blockSchema.selectedNodeId = copy.id;
  saveBlockSchema();
  render();
}

function deleteSchemaNode() {
  const node = getSchemaNode(blockSchema.selectedNodeId);
  if (!node) return;
  blockSchema.nodes = blockSchema.nodes.filter((item) => item.id !== node.id);
  blockSchema.edges = blockSchema.edges.filter((edge) => edge.from !== node.id && edge.to !== node.id);
  blockSchema.selectedNodeId = blockSchema.nodes[0]?.id || null;
  saveBlockSchema();
  render();
}

function validateBlockSchema() {
  const errors = [];
  const warnings = [];
  const ids = new Set(blockSchema.nodes.map((node) => node.id));
  if (!blockSchema.nodes.some((node) => node.type === "start")) errors.push("At least one Start block is required.");
  if (!blockSchema.nodes.some((node) => node.type === "approval")) warnings.push("Add an Approval block before writeback or provider actions.");
  blockSchema.edges.forEach((edge) => {
    if (!ids.has(edge.from)) errors.push(`Edge ${edge.label || edge.id} has missing source.`);
    if (!ids.has(edge.to)) errors.push(`Edge ${edge.label || edge.id} has missing target.`);
  });
  blockSchema.nodes.forEach((node) => {
    if (!node.title?.trim()) errors.push(`${node.id} needs a title.`);
    if (!node.owner?.trim()) warnings.push(`${node.title} needs an owner/agent.`);
    if (!node.description?.trim()) warnings.push(`${node.title} needs a description.`);
    if (!node.job?.trim()) warnings.push(`${node.title} needs a user job.`);
    if (!node.pain?.trim()) warnings.push(`${node.title} needs a pain/risk statement.`);
    if (!node.evidence?.trim()) warnings.push(`${node.title} needs evidence or an explicit pending marker.`);
    if (!node.businessObjective?.trim()) warnings.push(`${node.title} needs a business objective.`);
    if (!node.prompt?.trim()) errors.push(`${node.title} needs a prompt.`);
    if (!node.systemPrompt?.trim()) warnings.push(`${node.title} needs a system prompt.`);
    if (!node.comments?.trim()) warnings.push(`${node.title} has no reviewer/operator comments yet.`);
    if (!node.finalOutput?.trim()) errors.push(`${node.title} needs a final output contract.`);
    if (!node.inputs?.length) warnings.push(`${node.title} needs input ports.`);
    if (!node.outputs?.length) warnings.push(`${node.title} needs output ports.`);
    if (!node.files?.length) warnings.push(`${node.title} needs owned/touched files or an explicit pending marker.`);
    if (!node.questions?.length) warnings.push(`${node.title} needs questions covered.`);
    if (!node.possibleOutputs?.length) warnings.push(`${node.title} needs possible outputs.`);
    if (!node.config?.modelProvider) warnings.push(`${node.title} needs model/provider dropdown config.`);
    if (!node.config?.approvalGate) warnings.push(`${node.title} needs approval-gate dropdown config.`);
    if (node.type !== "start" && incomingSchemaEdges(node.id).length === 0) warnings.push(`${node.title} has no incoming route.`);
    if (!["output", "approval"].includes(node.type) && outgoingSchemaEdges(node.id).length === 0) warnings.push(`${node.title} has no outgoing route.`);
    if (node.type === "parallel" && outgoingSchemaEdges(node.id).length < 2) errors.push(`${node.title} needs at least two outgoing branch routes.`);
    if (node.type === "merge" && incomingSchemaEdges(node.id).length < 2) errors.push(`${node.title} should merge at least two incoming routes.`);
  });
  return { errors, warnings };
}

function queueSelectedSchemaNode() {
  const node = getSchemaNode(blockSchema.selectedNodeId);
  if (!node) return;
  blockSchema.queue = [
    {
      id: makeId("schema-queue"),
      created_at: nowIso(),
      node_id: node.id,
      node_title: node.title,
      owner: node.owner,
      workflow_layer: node.workflowLayer,
      description: node.description,
      job: node.job,
      pain: node.pain,
      evidence: node.evidence,
      business_objective: node.businessObjective,
      inputs: node.inputs,
      outputs: node.outputs,
      prompt: node.prompt,
      system_prompt: node.systemPrompt,
      comments: node.comments,
      files: node.files,
      requirements: node.requirements,
      final_output: node.finalOutput,
      possible_outputs: node.possibleOutputs,
      output_links: node.outputLinks,
      last_runs: node.lastRuns,
      incoming_connections: incomingSchemaEdges(node.id),
      outgoing_connections: outgoingSchemaEdges(node.id),
      config: node.config,
      write_gate: "Codex review required before any durable writeback."
    },
    ...(blockSchema.queue || [])
  ].slice(0, 20);
  saveBlockSchema();
  appendEvent("Schema node queued", `${node.title} queued for Codex review packet export.`, "ok");
  render();
}

function exportBlockSchemaPacket() {
  const validation = validateBlockSchema();
  const meta = schemaScreenMeta[schemaKindForActiveTab()];
  const packet = createLocalPacket("block-schema-review-packet", "dashboard block-schema editor", meta.packetInput, {
    extra: {
      block_schema: blockSchema,
      validation,
      langsmith_preparation: {
        enabled_now: false,
        next_step: "Add sanitized LangGraph run metadata and trace URLs after LANGSMITH_TRACING/LANGSMITH_API_KEY policy is approved.",
        blocked_data: ["raw transcripts", "raw recordings", "secrets", "private document bodies"]
      }
    }
  });
  downloadPacket(packet.id);
}

async function sendBlockSchemaToBackend() {
  const kind = schemaKindForActiveTab();
  const meta = schemaScreenMeta[kind];
  const status = view.querySelector("#schemaBackendStatus");
  const endpoint = kind === "service" ? "/api/lanes/prd-icp" : "/api/lanes/agent-orchestra";
  const payload = {
    request: `${meta.packetInput}\n\n${blockSchema.title}`,
    lane: kind === "service" ? "prd_icp_flow" : "agent_orchestra",
    architecture: kind,
    approved_test_input: false,
    owner_approval: false,
    provider_approval: false,
    source_refs: ["dashboard block-schema editor", "browser-local schema candidate"],
  };
  if (status) status.textContent = "Sending provider-disabled schema packet to backend if available...";
  try {
    await checkJarvisApi("block schema backend send", { silent: true });
    const response = await fetch(apiEndpoint(endpoint), {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    if (!response.ok) throw new Error(`backend returned ${response.status}`);
    const result = await response.json();
    appendEvent("Schema backend response", `${kind} backend returned ${result.status || "ok"}.`, "ok");
    if (status) status.textContent = `Backend response: ${result.status || "ok"}. Provider calls and writeback remain disabled.`;
  } catch (error) {
    const packet = createLocalPacket(`${kind}-schema-backend-unavailable`, "dashboard block-schema editor", meta.packetInput, {
      extra: {
        architecture: kind,
        backend_error: String(error.message || error),
        block_schema: blockSchema,
        fallback: "preserved as browser-local review packet",
      },
    });
    appendEvent("Schema backend unavailable", `${packet.id} staged locally for Codex review.`, "warn");
    if (status) status.textContent = `Backend unavailable; local packet staged: ${packet.id}.`;
  }
}

function savePromptConfigFromForm() {
  promptConfig = {
    chain_name: document.querySelector("#cfgChain")?.value || "",
    model_policy: document.querySelector("#cfgModel")?.value || "",
    memory_policy: document.querySelector("#cfgMemory")?.value || "",
    normal_prompt: document.querySelector("#cfgNormal")?.value || "",
    interview_prompt: document.querySelector("#cfgInterview")?.value || "",
    review_prompt: document.querySelector("#cfgReview")?.value || "",
  };
  saveJson(storageKeys.promptConfig, promptConfig);
  appendEvent("Config saved locally", "Prompt/subprompt configuration was saved in browser localStorage only.", "ok");
  render();
}

function exportPromptConfig() {
  const packet = createLocalPacket("jarvis-subprompt-config-candidate", "dashboard config page", "Export browser-local Jarvis chain and subprompt config for Codex review.", {
    extra: {
      prompt_config: promptConfig,
      jarvis_api_base: jarvisApiBase,
      persistence: "localStorage only until exported and reviewed",
    },
  });
  downloadPacket(packet.id);
}

function saveJarvisApiBaseFromForm() {
  const value = (document.querySelector("#cfgApiBase")?.value || "").trim().replace(/\/+$/, "");
  jarvisApiBase = value || defaultJarvisApiBase();
  localStorage.setItem(storageKeys.apiBase, jarvisApiBase);
  appendEvent("Jarvis API base saved", `API base saved in browser localStorage: ${jarvisApiBase}`, "ok");
  checkJarvisApi("config save", { silent: false });
  render();
}

function renderConfig() {
  view.innerHTML = `
    <section class="panel">
      <div class="section-header">
        <div>
          <h2 class="section-title">Chain Configuration And Subprompting</h2>
          <p class="muted">Edit browser-local prompt and API candidates. Export creates a review packet; it does not mutate GitHub, Notion, WikiLLM, or runtime services.</p>
        </div>
        <div class="row-actions">
          <button class="button" id="cfgApiCheck" type="button">Check API</button>
          <button class="button" id="cfgApiSave" type="button">Save API base</button>
          <button class="primary" id="cfgSave" type="button">Save locally</button>
          <button class="button" id="cfgExport" type="button">Export config packet</button>
        </div>
      </div>
      <div class="callout">
        <strong>Jarvis API base</strong>
        <p>Use the deployed Railway or Vercel API origin here. This value is saved only in this browser and lets the dashboard check hosted <span class="code">/health</span> and submit guarded review/provider packets.</p>
        <label>API base URL<input id="cfgApiBase" value="${escapeHtml(jarvisApiBase)}" placeholder="https://example.up.railway.app" /></label>
        <p class="muted">Current API state: ${escapeHtml(jarvisApiState.label)} - ${escapeHtml(jarvisApiState.detail)}</p>
      </div>
      <div class="config-grid">
        <label>Chain name<input id="cfgChain" value="${escapeHtml(promptConfig.chain_name)}" /></label>
        <label>Model policy<textarea id="cfgModel">${escapeHtml(promptConfig.model_policy)}</textarea></label>
        <label>Memory policy<textarea id="cfgMemory">${escapeHtml(promptConfig.memory_policy)}</textarea></label>
        <label>Normal mode subprompt<textarea id="cfgNormal">${escapeHtml(promptConfig.normal_prompt)}</textarea></label>
        <label>Interview mode subprompt<textarea id="cfgInterview">${escapeHtml(promptConfig.interview_prompt)}</textarea></label>
        <label>Reviewer subprompt<textarea id="cfgReview">${escapeHtml(promptConfig.review_prompt)}</textarea></label>
      </div>
    </section>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Agent Chain Links</h2>
      ${table(["Chain link", "Role", "Persistence"], [
        ["Jarvis intake", "Collect text, file transfer metadata/excerpts, and explicit approval.", "session/local packet"],
        ["Context analyzer", "Summarize and classify fact, interpretation, hypothesis, gap, decision, task.", "review packet"],
        ["Research/ICP agent", "Create source-backed evidence cards and market questions.", "run note after review"],
        ["Manager/PRD agent", "Convert accepted context into tasks, owners, PRD deltas, deadlines.", "Notion candidates"],
        ["Knowledge/RAG agent", "Promote reviewed summaries into Project Desire, WikiLLM, Obsidian.", "approval-gated"],
        ["Reviewer/integrator", "Verify safety, source links, status claims, and merge order.", "decision/run/issue"],
      ].map((row) => row.map(escapeHtml)))}
    </section>
  `;
  document.querySelector("#cfgApiSave")?.addEventListener("click", saveJarvisApiBaseFromForm);
  document.querySelector("#cfgApiCheck")?.addEventListener("click", () => checkJarvisApi("manual config check", { silent: false }));
  document.querySelector("#cfgSave")?.addEventListener("click", savePromptConfigFromForm);
  document.querySelector("#cfgExport")?.addEventListener("click", exportPromptConfig);
}

function renderPlan(data) {
  const eCards = [
    ["E1", "Knowledge base on ourselves", "Partly complete; E1.3 readback passed and review gate is active."],
    ["E2", "Evidence engine and PRD-to-ICP", "Readiness/source visibility only; production evidence cards still missing."],
    ["E3", "Positioning", "Depends on E2 evidence; do not claim ready."],
    ["E4", "Content direction", "Planning/reporting gate only; publishing needs proof and approval."],
    ["E5", "Analytics and ROI", "Dashboard visibility shell exists; ROI methodology and metrics remain future work."],
    ["E6", "Outreach", "Not started; blocked until E2-E4 proof."],
    ["E7", "Payment verdict", "Not started; needs demand/conversion evidence."],
  ];
  view.innerHTML = `
    <div class="grid cols-3">
      ${card({ label: "Current lane", value: "B2B SaaS product teams", note: "One ICP lane unless the owner expands scope", tone: "ok" })}
      ${card({ label: "Dashboard mode", value: "protected static preview", note: "Not a live control plane", tone: "warn" })}
      ${card({ label: "Next safe step", value: "E2.0 dry run", note: "No model/provider calls by default", tone: "ok" })}
    </div>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">E1-E7 Project Plan</h2>
      ${table(["Epic", "Scope", "Current status"], eCards.map((row) => row.map(escapeHtml)))}
    </section>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Recent Source Links</h2>
      <div class="list">
        ${(data.activity || []).slice(0, 10).map((item) => `
          <article class="row">
            ${badge(item.kind)}
            <span class="row-title">${escapeHtml(item.title)}</span>
            <div class="row-meta">${pathLink(item.path)}</div>
          </article>
        `).join("")}
      </div>
    </section>
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
      ${card({ label: "Mode", value: data.llamaindex.query_mode || "hybrid", note: data.llamaindex.query_engine || "approved corpus", tone: "ok" })}
      ${card({ label: "Vector top K", value: data.llamaindex.vector_top_k || "5", note: "Semantic candidates when local embedder is available", tone: "ok" })}
      ${card({ label: "Lexical top K", value: data.llamaindex.lexical_top_k || "5", note: "Deterministic fallback and traceability path", tone: "ok" })}
      ${card({ label: "Rerank top K", value: data.llamaindex.rerank_top_k || "5", note: `Fallback to lexical: ${data.llamaindex.fallback_to_lexical || "true"}`, tone: "ok" })}
    </div>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Local Query Test</h2>
      <p class="muted">This browser preview is lexical over generated dashboard data. The repo LlamaIndex script owns bounded hybrid retrieval, stable source/chunk provenance, and lexical fallback.</p>
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
    <div class="grid cols-3" style="margin-top:16px">
      ${card({ label: "Level 3", value: data.crewai.level_3_status || "unknown", note: "Direct CrewAI deterministic proof; not default/provider runtime", tone: data.crewai.level_3_status === "proof_passed_not_default_runtime" ? "ok" : "warn" })}
      ${card({ label: "Proof ledger", value: data.crewai.level_3_ledger || "not recorded", note: "Public-safe proof ledger for deterministic fixture", tone: data.crewai.level_3_ledger ? "ok" : "warn" })}
      ${card({ label: "Proof cost", value: data.crewai.level_3_cost || "unknown", note: "OpenRouter remains disabled", tone: data.crewai.level_3_cost === "0.00 USD" ? "ok" : "warn" })}
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
        <div class="row"><span class="row-title">Next check</span><div class="row-meta">Use the existing local runtime for sanitized traces only. Hosted provider calls require approval and budget proof.</div></div>
      </div>
    </section>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Official References</h2>
      <div class="chips">${data.sources.map((s) => `<a class="badge" href="${escapeHtml(s.url)}">${escapeHtml(s.label)}</a>`).join("")}</div>
    </section>
  `;
}

function renderEnv(data) {
  const jarvisStatus = data.jarvis_api?.status || "unknown";
  const jarvisTone = jarvisStatus.includes("provider_disabled") || jarvisStatus.includes("guarded_openrouter") ? "ok" : "warn";
  view.innerHTML = `
    <div class="grid cols-3">
      ${card({ label: "Jarvis API", value: jarvisStatus, note: data.jarvis_api?.path || "services/jarvis-api", tone: jarvisTone })}
      ${card({ label: "Provider runtime", value: data.jarvis_api?.provider_runtime || "disabled", note: "OpenRouter server-side only after approval", tone: "warn" })}
      ${card({ label: "Run hard stop", value: `${data.jarvis_api?.openrouter_budget?.run_hard_stop_usd || "1.99"} USD`, note: "Stop and ask approval above cap", tone: "ok" })}
    </div>
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
      <h2 class="section-title">Jarvis API Required Endpoints</h2>
      <div class="chips">${(data.jarvis_api?.endpoints || []).map((endpoint) => `<span class="badge">${escapeHtml(endpoint)}</span>`).join("")}</div>
    </section>
    <section class="panel" style="margin-top:16px">
      <h2 class="section-title">Operating Rule</h2>
      <div class="callout">Use Codex direct prompting first, then CLI proof scripts, then this dashboard. Write actions wait for Railway/auth/writeback gates.</div>
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
  document.body.dataset.activeTab = activeTab;
  renderNav();
  const data = dashboardData;
  generatedAt.textContent = `Generated ${new Date(data.generated_at).toLocaleString()}`;
  globalInput.placeholder = `${architectureMeta().short}: ask Jarvis, run a check, or type refresh`;
  if (activeTab === "jarvis") renderJarvis(data);
  if (activeTab === "history") renderHistory(data);
  if (activeTab === "service") renderSchema(data);
  if (activeTab === "schema") renderSchema(data);
  if (activeTab === "config") renderConfig(data);
  if (activeTab === "plan") renderPlan(data);
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
  window.setTimeout(() => {
    if (isEditingControlActive()) {
      setLiveStatus("Static polling paused while editing", "warn");
      return;
    }
    loadDashboardData("window focus").catch(() => {
      setLiveStatus("Static data only", "warn");
    });
  }, 250);
});

document.addEventListener("visibilitychange", () => {
  if (!document.hidden) {
    window.setTimeout(() => {
      if (isEditingControlActive()) {
        setLiveStatus("Static polling paused while editing", "warn");
        return;
      }
      loadDashboardData("tab visible").catch(() => {
        setLiveStatus("Static data only", "warn");
      });
    }, 250);
  }
});

window.addEventListener("hashchange", () => {
  const nextTab = window.location.hash?.replace(/^#/, "") || "jarvis";
  if (!tabs.some((tab) => tab.id === nextTab)) return;
  activeTab = nextTab;
  render();
});

loadDashboardData("initial load")
  .then(() => checkJarvisApi("initial load", { silent: true }))
  .then(startLiveRefresh)
  .catch((error) => {
    setLiveStatus("Data error", "block");
    view.innerHTML = `<section class="panel"><h2 class="section-title">Dashboard data error</h2><p>${escapeHtml(error.message)}</p></section>`;
  });
