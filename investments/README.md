# Investments Workspace

This folder is organized into three clear layers to minimize contradictions and maintenance overhead.

1. Methodology and operator guidance: `investments/guides/`
2. Runtime outputs and research results: `investments/operations/`
3. Canonical thesis rules and portfolio overlay: `investments/thesis/`

## Phase 1 status

Phase 1 is active and locked.

Phase 1 lock means:
- keep exactly two active guide files,
- keep the current authority order,
- keep operations runtime-only,
- avoid further structural moves until one full bi-weekly cycle is run.

## Folder responsibilities

- `guides/active/`: only current, normative guidance.
- `guides/archive/`: superseded guidance kept for traceability.
- `operations/`: append-only runtime artifacts, research outputs, and logs.
- `thesis/constitutions/`: active thesis constitution JSON files.
- `thesis/portfolio/`: portfolio-level overlay JSON.
- `templates/`: reusable report templates.

## Canonical read order

1. `guides/active/investment_methodology.md`
2. `guides/active/operator_quickstart.md`
3. `thesis/portfolio/portfolio_master_v1_0.json`
4. `thesis/constitutions/*.json`

## Cross-reference rules

- If guidance conflicts with thesis JSON or portfolio JSON, JSON wins.
- Runtime status, decisions, and evidence belong in `operations/`, not in guides.
- Active guides should link to thesis and operations paths rather than duplicate their content.

## Validation command

Run this check after any documentation update:

- `python3 /workspace/jaxx_open_claw_setup/scripts/check_investments_phase1.py`
