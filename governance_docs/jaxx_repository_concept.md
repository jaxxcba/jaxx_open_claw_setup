# JAXX Repository Concept

Version: 1.1.0
Last Updated: 2026-02-18
Status: Active

## Purpose

This document explains the high-level model for how the repository is organized.
It is intentionally short: it defines the why and the shape, not day-to-day rules.

## Repository model

The repository is a system notebook with three primary domains:

1. `governance_docs/`
   - governance, navigation, and operator guidance.
2. `openclaw/`
   - assistant identity and runtime setup.
3. `investments/`
   - investment research guides, thesis files, and operating artifacts.

Supporting domains:
- `credentials/` for safe credential templates only,
- `local_secrets/` for local private data,
- `scripts/` for utility automation.

## Design principles

1. One concern per folder.
2. One canonical home per content type.
3. Keep active guidance easy to find.
4. Keep historical artifacts available but out of default onboarding flow.
5. Never commit live secrets.

## Documentation shape

- Normative core:
  - `README.md`
  - `governance_docs/index.md`
  - `governance_docs/conventions.md`
  - `governance_docs/operator_playbook.md`
- Historical process artifacts:
  - `governance_docs/history/`

## Ownership boundaries

- This file (`jaxx_repository_concept.md`) defines intent and structure.
- `governance_docs/conventions.md` defines operational rules.
- `governance_docs/operator_playbook.md` defines day-to-day operating steps.

## Definition of success

The concept is successful when:
- new contributors can find edit locations quickly,
- governance remains clear without excessive overhead,
- historical context is preserved without cluttering active docs,
- secrets remain outside tracked content.

## References

- `README.md`
- `governance_docs/index.md`
- `governance_docs/conventions.md`
- `governance_docs/operator_playbook.md`
- `governance_docs/history/README.md`
