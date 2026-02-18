# OpenClaw Architecture
## Version 1.5.2 — Governance-First Investment Intelligence & Continuous Thesis Monitoring

Change Summary (v1.5.2):
- Clarified Portfolio Master overlay (portfolio-level guardrails and precedence)
- Clarified Verification policy: adapters-first; web/online retrieval is fallback only

**Status:** Controlled Deployment  
**Replaces:** v1.5  
**Core Principle:** Separate Reading, Verification, and Judgment  
**New in 1.5.1:** Explicit Bi-Weekly Thesis Reality Reassessment Workflow  

---

# PART I — Plain English Concept

## 1. What OpenClaw Is

OpenClaw is a structured decision system for managing investment theses with discipline.

It is designed to:

- Read research reports  
- Independently verify important facts  
- Compare findings against defined investment theses  
- Monitor stop conditions and risk triggers  
- Continuously reassess reality versus assumptions  

It is not a chat assistant.  
It is a structured investment control system.

---

## 2. Why It Uses Phases

Important investment decisions require different types of thinking:

1. Reading (extracting what is claimed)  
2. Verifying (checking what is true now)  
3. Judging (evaluating against your thesis)  
4. Challenging (adversarial review)  

If a single model does all of this:

- Costs increase  
- Errors compound  
- Hallucinations go unnoticed  
- Auditability suffers  

OpenClaw separates these tasks intentionally.

---

# 3. Core Use Cases

## A. Report Review Against Thesis

You provide a research report.  
OpenClaw:

1. Extracts structured claims  
2. Verifies current data  
3. Compares to thesis  
4. Flags contradictions  
5. Evaluates kill conditions  
6. Runs red-team review  

Output:

- Clear alignment assessment  
- Risk map  
- Trigger status  
- Confidence level  
- Explicit uncertainty statement  

---

## B. Analytical Extraction

You only want structured data from a document.

OpenClaw:

- Extracts numbers, assumptions, risks  
- Returns structured JSON  
- Does not run live verification unless requested  

---

## C. Routine Tasks

Formatting, checklists, drafting, summarization.  
Low-cost models are used.  
No heavy verification layer.

---

## D. Scheduled Thesis Reality Reassessment (Bi-Weekly)

Every two weeks, OpenClaw:

1. Pulls live market data  
2. Pulls relevant macro indicators  
3. Checks predefined thesis assumptions  
4. Evaluates trigger thresholds  
5. Calculates thesis drift  
6. Runs adversarial red-team  
7. Stores snapshot for historical comparison  

This turns OpenClaw into:

- A continuous monitoring system  
- An early warning engine  
- A thesis integrity tracker  

No external report required.

---

## 4. How You Interact

Natural language example:

> Run bi-weekly reality check for all 4 core theses. Include trigger proximity and delta vs last review.

Command style example:

```
/run thesis_monitor --all --delta --redteam on
```

---

## 5. What Makes v1.5.1 Strong

- No synthesis without verified facts  
- Fail-closed design  
- Structured evidence ledger  
- Red-team adversarial challenge  
- Escalation for irreversible decisions  
- Automated thesis monitoring  
- Benchmark-driven model governance  

---

# PART II — Technical Architecture

---

# 1. System Flow (Full Review)

```text
User Prompt
   ↓
Router (OpenRouter Preset)
   ↓
Phase A — Extraction (if report provided)
   ↓
Phase B.1 — Query Planner
   ↓
Phase B.2 — Verification Engine
       ├─ Hard Fact Retrieval
       └─ Optional Sentiment Scout
   ↓
Evidence Ledger + Completeness Index
   ↓
Phase C — Strategic Synthesis
   ↓
Red-Team (Adversarial)
   ↓
Divergence Check
   ↓
Escalation (if needed)
   ↓
Final Structured Output + Audit Log
```

---

# 2. Scheduled Thesis Monitoring Flow (No Report)

```text
Bi-Weekly Trigger
   ↓
For each Thesis:
   ↓
Phase B.1 — Generate verification targets from thesis assumptions
   ↓
Phase B.2 — Retrieve live data
   ↓
Evidence Completeness Index
   ↓
Phase C — Synthesize Reality vs Thesis
   ↓
Red-Team
   ↓
Divergence Check
   ↓
Snapshot Stored (with timestamp)
```

---

# 3. Orchestration Layer

OpenRouter is the sole execution gateway.

Each phase maps to a preset:

| Phase | Preset |
|--------|--------|
| Extraction | openclaw-extraction |
| Planner | openclaw-planner |
| Verification (adapters-first) | openclaw-verification |
| Verification (online fallback) | openclaw-verification-online |
| Synthesis | openclaw-synthesis |
| Red-Team | openclaw-redteam |
| Escalation (rare) | openclaw-escalation |


Benefits:

- Cost-aware routing  
- Provider fallback  
- Central configuration  
- Context caching  


## 3.1 Portfolio Master Overlay

Optional but recommended when decisions can change overall portfolio risk.

**What it is**
A portfolio-level governor file (`portfolio_master.json`) that enforces cross-thesis guardrails (e.g., concentration caps, overlap constraints, and risk-off modes).

**Precedence**
Portfolio Master > Thesis Constitution (thesis_*.json) > Snapshots/Logs.

**How it works**
After Phase C produces a thesis-level recommendation, the Portfolio Master overlay may:
- veto or downsize “add risk” actions during risk-off mode
- block actions that breach portfolio-level caps
- require escalation if multiple theses propose correlated adds

This preserves the core principle: *no hidden authority* and *explicit guardrails*.


---

# 4. Phase A — Extraction

Primary: Gemini Flash  
Fallback: DeepSeek Reasoner  

Purpose: Mechanical parsing only.

Circuit breaker:

- Max cost threshold  
- Retry limit  

---

# 5. Phase B — Verification

## Phase B.1 — Query Planner

Model: Gemini Flash  

Role:

- Translate thesis assumptions into verification targets  
- No factual answering  

Output:

```json
{
  "verification_targets": []
}
```

---

## Phase B.2 — Verification Engine

Policy: Canonical data should come from adapters/primary sources. Web/online retrieval is fallback only when an adapter source is unavailable.

Default:

- Market data adapters  
- Macro data adapters  
- Filing retrieval  

Optional:

- Grok sentiment scout (only when relevant)

All data normalized into Evidence Ledger.

---

# 6. Evidence Ledger & Completeness Index

Each fact stored with:

- Entity  
- Value  
- Timestamp  
- Source  
- Confidence  

Before synthesis:

- Calculate % targets resolved  
- Identify conflicts  
- Check critical gaps  

If below threshold → abort synthesis.

Fail-closed by design.

---

# 7. Phase C — Strategic Synthesis

Primary: Gemini Pro  
Red-Team: DeepSeek-R1  
Escalation: OpenAI o1 (rare)  

Purpose:

- Thesis alignment  
- Downside risk  
- Kill criteria evaluation  
- Trigger proximity analysis  

Structured JSON output mandatory.

---

# 8. Divergence & Escalation

Escalate if:

- Kill decision + ambiguity  
- Significant disagreement between primary and red-team  
- Evidence conflict unresolved  

Escalation logged.

---

# 9. Circuit Breakers

Phase A:

- Max cost  
- Retry limit  

Phase B:

- Max adapter failures  
- Latency threshold  

Phase C:

- Max reasoning tokens  
- Schema failure retries  

---

# 10. Thesis Drift Monitoring

Each bi-weekly run computes:

- Assumption Validity Ratio  
- Trigger Proximity Index  
- Risk Acceleration Flag  
- Drift Score vs previous snapshot  

Snapshots stored with timestamps.

This allows:

- Trend analysis  
- Gradual deterioration detection  
- Early exit signals  

---

# 11. Model Governance

Every 2 months:

- Benchmark all phases  
- Evaluate cost, logical consistency, schema compliance  
- Approve or reject model swaps  

Event-triggered reassessment:

- Major model release  
- Failure spike  
- Cost anomaly  

No model promoted without benchmark.

---

# 12. What v1.5.1 Explicitly Rejects

- Single-model dominance  
- Mixing retrieval and synthesis  
- Sentiment-driven decisions  
- Model swapping without data  
- Silent execution without logging  

---

# Final Position

Version 1.5.1 transforms OpenClaw into:

- A structured research evaluator  
- A capital-protection system  
- A continuous thesis monitoring engine  
- An institution-grade decision framework  

It is stable, disciplined, benchmark-driven, and escalation-aware.

---

Explicit uncertainty statement:  
No material uncertainty regarding structural robustness. Implementation complexity for snapshot storage and drift metrics requires careful engineering but does not alter conceptual