# Investment Operator Quickstart
Version: 1.0.0
Last Updated: 2026-02-18
Status: Active

## Purpose

This is the practical runbook for day-to-day operation.
Methodology and governance authority remain in `./investment_methodology.md`.

## 10-minute onboarding

1. Read `../../README.md`.
2. Read `./investment_methodology.md`.
3. Open `../../thesis/portfolio/portfolio_master_v1_0.json`.
4. Open all files in `../../thesis/constitutions/`.
5. Confirm runtime output locations in `../../operations/`.

## Folder map

- Method and policy: `./`
- Runtime outputs: `../../operations/`
- Thesis source of truth: `../../thesis/`
- Templates: `../../templates/`
- Archive: `../archive/`

## Standard operating cadence

### Bi-weekly cycle

1. Collect KPI and macro updates.
2. Review each thesis against constitution logic.
3. Apply portfolio overlay constraints.
4. Record outputs in operations paths.
5. Record decisions and evidence references.

### Research intake cycle

1. Start from template in `../../templates/`.
2. Summarize report facts and inferences distinctly.
3. Map impact to thesis slug(s).
4. Write impact output to `../../operations/research_results/`.
5. Update logs if decision or confidence state changed.

## Operations output conventions

### Research results

Path: `../../operations/research_results/`
File naming:
- `source-YYYY-MM-DD-short-description.md`

### Logs and snapshots

Paths:
- `../../operations/logs/audit_log.jsonl`
- `../../operations/logs/evidence_ledger.jsonl`
- `../../operations/logs/snapshots/`

Rule:
- Treat logs and snapshots as append-only.

## Contradiction prevention checklist

Before finalizing any action:

- Verify thesis name and slug match JSON canon.
- Verify recommendation does not violate portfolio overlay.
- Verify rationale references evidence or KPI changes.
- Verify updates are written to operations, not to constitutions unless logic changed.

## Escalation triggers

Escalate when:

- Two or more theses show red or kill-proximity in the same weekly window.
- A recommendation changes exposure materially beyond portfolio guardrail.
- Required KPI data is unavailable for a primary metric.

## Document hygiene

- Keep only these two active guide files in this folder.
- Move superseded guidance to `../archive/`.
- Add cross-links instead of duplicated paragraphs.
