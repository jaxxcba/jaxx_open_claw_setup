# Investment Methodology
Version: 1.1.0
Last Updated: 2026-02-18
Status: Active
Change Note: Added explicit Phase 1 lock and validation checkpoint.

## Purpose

This is the single source of truth for how investment theses are defined, validated, governed, and reviewed.

Use this document for methodology and governance only.
Use `./operator_quickstart.md` for step-by-step execution.

## Scope and authority

Authority order (highest to lowest):

1. `../../thesis/portfolio/portfolio_master_v1_0.json`
2. `../../thesis/constitutions/thesis_*.json`
3. `../../operations/` snapshots, logs, and research outputs
4. This guide and operator quickstart

If this file conflicts with thesis JSON or portfolio JSON, JSON wins.

## Phase 1 lock (implemented)

Until one complete bi-weekly operating cycle is completed and reviewed:

- Keep exactly two active guide documents (`investment_methodology.md`, `operator_quickstart.md`).
- Keep `research_sources_reference.json` as the only active reference data file.
- Keep `operations/` runtime-only.
- Avoid structural folder changes unless a break-fix is required.

Validation command:

- `python3 /workspace/jaxx_open_claw_setup/scripts/check_investments_phase1.py`

## Core operating model

A thesis is executable logic, not a narrative.

Each thesis must define:

- Structural pillars with falsifiable tests.
- Primary KPIs linked to pillars.
- Kill criteria with persistence filters.
- Implementation and expression constraints.
- Allocation band and governance constraints.
- Missing-data policy.

Portfolio-level governance is defined in `../../thesis/portfolio/portfolio_master_v1_0.json`.

## Separation of concerns

- Rules layer (stable, edited rarely): `../../thesis/`
- Runtime layer (append-only, frequent updates): `../../operations/`
- Process layer (human instructions): `../active/`

Do not store current KPI values, active decisions, or weekly status in thesis constitutions.
Do not store governance logic in operations results files.

## Standard workflows

### 1) Create or update a thesis constitution

Inputs:
- Thesis rationale and mechanism.
- Portfolio role and constraints.

Outputs:
- Updated or new thesis JSON in `../../thesis/constitutions/`.
- Version history updated in the JSON.

Quality rules:
- Keep KPI set small and directly linked to pillars.
- Use stable KPI IDs.
- Define canonical data source and fallback.

### 2) Bi-weekly review

Inputs:
- Thesis JSON files.
- Portfolio overlay JSON.
- Latest KPI and macro data.

Outputs (to `../../operations/`):
- Snapshot per thesis.
- Audit log updates.
- Evidence ledger updates.
- Action recommendations constrained by portfolio overlay.

### 3) New research intake

Inputs:
- New report or summary.

Outputs:
- Thesis impact map (supporting, strengthening, challenging, invalidating, neutral).
- Evidence entry with source and confidence.
- If needed, thesis review trigger.

Use templates from `../../templates/`.

Preferred research source universe:
- `./research_sources_reference.json`

## Non-negotiable governance rules

- Constitutions are stable logic; runtime state is append-only.
- Missing primary KPI data freezes adds but does not force sells.
- Kill criteria include persistence to reduce noise reactions.
- Portfolio-level circuit breaker can override thesis-level add risk.
- Cross-thesis overlap rule applies globally.
- Large allocation changes require cool-off and rationale.

## Naming and consistency policy

- Refer to theses by canonical JSON `meta.slug` and `meta.name`.
- Use lowercase folder names and snake_case file names for new markdown outputs.
- Keep one active methodology file and one active quickstart file.
- Move superseded active guidance into `../archive/`.

## Where things live

- Methodology: `./investment_methodology.md`
- Execution steps: `./operator_quickstart.md`
- Runtime results and logs: `../../operations/`
- Thesis rules: `../../thesis/`
- Templates: `../../templates/`
- Historical guidance: `../archive/`

## Change control

When methodology changes:

1. Bump version and date in this file.
2. Add a short change note at top.
3. Confirm no conflicts with thesis and portfolio JSON.
4. Move previous version to `../archive/` only if a separate versioned file is created.
