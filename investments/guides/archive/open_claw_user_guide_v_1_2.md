# OpenClaw User Guide for Investment Mgmt Use Cases
Version: 1.2
Status: Active

Change Summary (v1.2):
- Added Portfolio Master guardrails (portfolio-level risk overlay)
- Clarified that portfolio guardrails can override per-thesis adds

Previous Change Summary (v1.1):
- Added Bi-Weekly Strategy Reassessment (Reality Check Mode)
- Clarified delta-based reassessment logic
- Updated cost & stability section accordingly

---

## How to Work with JAXX (Practical Guide with Real Examples)

This guide explains how to use OpenClaw in everyday language. No technical knowledge required.

OpenClaw works in structured steps behind the scenes. You only need to describe what you want clearly.

---

# 1. What OpenClaw Can Do For You

OpenClaw supports three types of work:

## A. Important Decisions (High Impact)

Use this when:

- You are reviewing a research report
- You want to check if something still fits your investment idea
- You are considering changing or stopping a strategy
- You are preparing a board-level summary

In these cases, OpenClaw:

1. Reads the document
2. Checks important facts (prices, latest data, updates)
3. Compares everything to your defined idea
4. Gives a structured conclusion

---

## B. Analytical Work (Medium Impact)

Use this when:

- You just want key points from a document
- You want numbers extracted
- You want risks listed
- You want structured summaries

OpenClaw reads and extracts clean data.
It does not perform deep market checks unless you ask for them.

---

## C. Routine Tasks (Low Impact)

Use this when:

- You need a checklist
- You need formatting help
- You need a draft
- You need meeting notes structured

This is fast and inexpensive.

---

# 2. How to Ask JAXX

You can speak naturally.

You do not need technical commands.

Below are practical examples.

---

# Example 1 — Review a Report Against Your Strategy

What You Say:

Please review this report against my BTC-CORE strategy.
Verify today’s price and latest inflation number.
Tell me if anything contradicts the strategy.

What Happens Behind the Scenes:

1. The report is read and broken into structured points.
2. Important numbers are independently checked.
3. Everything is compared to your strategy.
4. You receive a structured result.

---

# 3. Bi-Weekly Strategy Reassessment (Reality Check Mode)

Every two weeks, you can run a structured reassessment of your main investment theses.

This is not a document review.
This is a structured reality alignment check.

Use this when:

- Markets moved materially
- Macro data changed
- Sentiment shifted
- You want discipline against drift
- You want to prevent thesis inertia

What This Does:

For each selected thesis, OpenClaw will:

1. Refresh relevant live market data
2. Check KPIs and trigger thresholds
3. Re-evaluate assumptions
4. Re-run kill criteria
5. Highlight deviations
6. Run Red-Team by default

What You Say:

Run bi-weekly reassessment on my 4 core strategies.
Verify live data.
Highlight deviations and kill-criteria proximity.
Run red-team.

Optional Command:

/run thesis_reassessment --strategies ALL --verify live_data --redteam on

Output Includes:

- Current status (Stable / At Risk / Triggered)
- What changed since last review
- KPI deltas
- Kill-criteria distance
- Suggested action
- Confidence level
- Explicit uncertainty statement

This protects against confirmation bias and thesis decay.

---

# 4. What Happens If Something Goes Wrong

OpenClaw is designed to fail safely.

It will:

- Stop if data cannot be verified
- Flag conflicting sources
- Refuse to continue if key information is missing
- Escalate if major disagreement appears

It will not:

- Guess
- Fill gaps silently
- Make irreversible decisions without clarity

---

# 5. Cost and Stability Protection

The system automatically:

- Uses lightweight models for extraction and planning
- Uses stronger models only for final reasoning
- Stops if token usage spikes abnormally
- Reviews model performance every two months

Bi-weekly reassessments are optimized for delta-only checks.
Full report reprocessing is not triggered unless explicitly requested.

---

# 6. When to Use Which Type of Request

| Situation                   | What to Ask                                    |
|----------------------------|-----------------------------------------------|
| Reviewing new research     | Review this report against my strategy.       |
| Checking if something broke| Check if stop conditions are triggered.       |
| Extracting structured data | Extract key numbers and risks.                |
| Preparing board material   | Summarize findings in board-ready format.     |
| Quick fact check           | Verify today’s price and compare to threshold.|
| Updating decision          | Re-evaluate strategy given latest data.       |
| Regular discipline         | Run bi-weekly thesis reassessment.            |
| Portfolio-wide guardrails | Run portfolio guardrail check; respect risk-off and caps. |

---

# 7. What You Will Always See

For important decisions, responses follow a consistent structure:

- Clear answer
- Key facts
- Edge cases
- Next steps
- Explicit uncertainty statement

---

OpenClaw is built to protect capital, prevent hallucinated data, and keep decisions structured and reviewable.