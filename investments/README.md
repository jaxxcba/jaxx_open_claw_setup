# Investments Workspace

This folder is organized into three clear layers to minimize contradictions and maintenance overhead:

1. Methodology and operator guidance: `investments/guides/`
2. Runtime outputs and research results: `investments/operations/`
3. Canonical thesis rules and portfolio overlay: `investments/thesis/`

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
