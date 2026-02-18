# OpenClaw – OpenRouter Preset Configuration
Version: 1.1
Aligned with: OpenClaw Architecture v1.5.2

---

## Purpose
This document defines the exact OpenRouter preset configuration for all OpenClaw phases. 
Presets must be referenced by slug from the application layer. Model IDs must never be hard-coded in application logic.

Each preset specifies:
- Model selection + fallbacks
- Provider routing constraints
- Deterministic parameter configuration
- Reasoning configuration
- Strict JSON-only output enforcement

---

# Global Configuration Rules (Apply to All Presets)

## Provider Routing
- Include Provider Preferences: ON
- data_collection: deny
- Allow fallbacks: true
- Require parameters: true
- sort/order/only/ignore/quantizations: unset unless explicitly required
- max_price: unset (avoid accidental blocking)
- ZDR: unset unless required and supported

## Parameter Inclusion
For every preset:
- "Include" must be checked for each parameter used
- Otherwise OpenRouter defaults may override configuration

## Verification policy
- Phase B.2 is adapters-first: prefer canonical adapter/primary-source outputs.
- Use online/web retrieval only as a fallback when no adapter source exists (separate preset: openclaw-verification-online).

## JSON Enforcement
All presets enforce JSON-only output through the System Prompt.
No Markdown. No prose. No explanations.

---

# 1. openclaw-extraction (Phase A)

## Purpose
Schema-bound claim extraction only. No verification. No inference.

## Model Selection
Primary: google/gemini-2.0-flash
Fallback: deepseek/deepseek-r1

## Provider Routing
preferred_min_throughput:
- p50: 120
- p90: 60

preferred_max_latency:
- p50: 5
- p90: 12

## Parameters
Temperature: 0.10
Top P: 0.90
Frequency Penalty: 0.00
Presence Penalty: 0.00
Repetition Penalty: 1.05
Max Tokens: 1200
Seed: unset

## Reasoning
Disabled

---

# 2. openclaw-planner (Phase B.1)

## Purpose
Translate assumptions into verification targets and tool plans.
No factual answering.

## Model Selection
Primary: google/gemini-2.0-flash
Fallback: google/gemini-2.0-pro

## Provider Routing
preferred_min_throughput:
- p50: 100
- p90: 50

preferred_max_latency:
- p50: 6
- p90: 15

## Parameters
Temperature: 0.20
Top P: 0.90
Frequency Penalty: 0.00
Presence Penalty: 0.00
Repetition Penalty: 1.05
Max Tokens: 1600
Seed: unset

## Reasoning
Disabled

---

# 3. openclaw-verification (Phase B.2)

## Purpose
Normalize retrieved data into Evidence Ledger.
Record conflicts. Fail closed if incomplete.

## Model Selection
Primary: google/gemini-2.0-flash
Fallback: google/gemini-2.0-pro

Note: This preset assumes canonical data is supplied via adapters/primary sources. Use openclaw-verification-online only when required.

## Provider Routing
preferred_min_throughput:
- p50: 60
- p90: 30

preferred_max_latency:
- p50: 12
- p90: 30

## Parameters
Temperature: 0.10
Top P: 0.90
Frequency Penalty: 0.00
Presence Penalty: 0.00
Repetition Penalty: 1.03
Max Tokens: 2800
Seed: unset

## Reasoning
Enabled
Reasoning Effort: Medium
Exclude reasoning from response: ON

---

# 4. openclaw-synthesis (Phase C)

## Purpose
Strategic judgement using Evidence Ledger only.
Evaluate alignment, triggers, kill criteria.

## Model Selection
Primary: google/gemini-2.0-pro
Fallback 1: google/gemini-2.0-flash
Fallback 2: deepseek/deepseek-r1

## Provider Routing
preferred_min_throughput:
- p50: 40
- p90: 20

preferred_max_latency:
- p50: 10
- p90: 25

## Parameters
Temperature: 0.40
Top P: 0.95
Frequency Penalty: 0.00
Presence Penalty: 0.00
Repetition Penalty: 1.02
Max Tokens: 3500
Seed: unset

## Reasoning
Enabled
Reasoning Effort: High
Exclude reasoning from response: ON

---

# 5. openclaw-redteam

## Purpose
Adversarial critique. Identify missing evidence, logical gaps, unsafe assumptions.

## Model Selection
Primary: deepseek/deepseek-r1
Fallback: google/gemini-2.0-pro

## Provider Routing
preferred_min_throughput:
- p50: 25
- p90: 12

preferred_max_latency:
- p50: 15
- p90: 35

## Parameters
Temperature: 0.70
Top P: 0.95
Frequency Penalty: 0.00
Presence Penalty: 0.00
Repetition Penalty: 1.01
Max Tokens: 3000
Seed: unset

## Reasoning
Disabled (model already performs internal reasoning)

---

# 6. openclaw-escalation (Rare)

## Purpose
High-stakes tie-breaker when synthesis and red-team diverge.
Used rarely and logged.

## Model Selection
Primary: openai/o1
Fallback: google/gemini-2.0-pro

## Provider Routing
preferred_min_throughput:
- p50: 15
- p90: 8

preferred_max_latency:
- p50: 20
- p90: 45

## Parameters
Temperature: 0.10
Top P: 0.90
Frequency Penalty: 0.00
Presence Penalty: 0.00
Repetition Penalty: 1.00
Max Tokens: 4000
Seed: unset

## Reasoning
Enabled
Reasoning Effort: High
Exclude reasoning from response: ON

---

# Governance Notes

1. Escalation usage should remain <5% of total calls.
2. Verification must fail-closed if evidence is incomplete.
3. JSON-only outputs are mandatory across all phases.
4. No model ID should appear in application code.
5. Preset slugs are the stable integration interface.

---

End of configuration document.