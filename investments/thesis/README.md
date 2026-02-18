# Thesis

This folder contains the canonical investment logic for the OpenClaw system.

## Basic concept

The thesis layer is split into two levels that work together:

1. **Portfolio Master (umbrella):** `portfolio/portfolio_master_v1_0.json`
   - Defines portfolio-wide governance and constraints across all theses.
   - Sets sleeve target ranges, overlap rules, and circuit-breaker behavior.
   - Acts as the top authority when a thesis-level rule conflicts with portfolio-level risk controls.

2. **Individual thesis constitutions:** `constitutions/thesis_*.json`
   - Define each thesis mechanism, KPI logic, tests, and kill criteria.
   - Govern security selection and thesis-specific decision logic inside that thesis scope.
   - Must remain consistent with (and subordinate to) the Portfolio Master umbrella.

In practice: the Portfolio Master governs *how all theses fit together*, while each constitution governs *how one thesis operates*.

## Subfolders

- `constitutions/`: thesis-level constitutions (one JSON per thesis).
- `portfolio/`: portfolio-level umbrella overlay and constraints.

## Authority and consistency rules

- Canonical read order:
  1. `../guides/active/investment_methodology.md`
  2. `../guides/active/operator_quickstart.md`
  3. `portfolio/portfolio_master_v1_0.json`
  4. `constitutions/thesis_*.json`
- If active guide text conflicts with thesis JSON or portfolio JSON, JSON wins.
- If a constitution conflicts with Portfolio Master governance, Portfolio Master wins.

## Rule

Files here define stable policy and constraints.
Do not store runtime review outcomes here.
Runtime outcomes belong in `../operations/`.

For operating process, use `../guides/active/investment_methodology.md`.
