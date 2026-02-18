# JAXX Operator Playbook

Version: 1.0.0
Last Updated: 2026-02-18
Status: Active
Owner: Repository Governance

## Purpose

This playbook is the fast path for day-to-day work in this repository.
Use it to decide where to edit, what to check, and how to keep changes consistent.

## 10-minute onboarding path

1. Read `README.md` for project purpose and layout.
2. Read `docs/index.md` for canonical navigation.
3. Read `docs/conventions.md` for naming and canonical-source rules.
4. Start work in your target domain (`openclaw/` or `investments/`).

## Where to edit decision table

| If you need to change... | Edit here first |
| --- | --- |
| repository navigation or documentation map | `docs/index.md` |
| naming, archive, canonical-source rules | `docs/conventions.md` |
| high-level repository model and rationale | `docs/jaxx_repository_concept.md` |
| assistant identity or memory behavior | `openclaw/assistant/` |
| OpenClaw runtime config/install notes | `openclaw/system/` |
| investment guides, thesis, templates, ops | `investments/` |
| credential file shape examples | `credentials/examples/` |
| local private secrets guidance | `local_secrets/README.md` |

## Common recipes

### Add a new governance doc

1. Decide whether it is active standard or historical artifact.
2. If active, place under `docs/`.
3. If historical/reporting, place under `docs/history/`.
4. Add link from `docs/index.md`.

### Publish a new guide version

1. Update active file under the correct canonical area.
2. Move prior active version to matching `archive/` folder.
3. Keep filename versioned and date-stamped where applicable.

### Move a file to canonical location

1. Use `git mv` to preserve history.
2. Update references in `docs/index.md`.
3. Run metadata check on changed files.

## Pre-commit checklist

- [ ] File is in canonical location.
- [ ] Naming follows repository conventions.
- [ ] No live secrets were added.
- [ ] `docs/index.md` updated for structural changes.
- [ ] Active versus history/archive placement is correct.

## References

- `README.md`
- `docs/index.md`
- `docs/conventions.md`
- `docs/jaxx_repository_concept.md`
