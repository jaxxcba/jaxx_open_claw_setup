# JAXX Repository Index

Version: 1.2.0
Last Updated: 2026-02-18
Status: Active

## Purpose

This is the navigation map for the repository.
Use this file first to find canonical locations.

## Canonical top-level areas

- `docs/`: repository governance and navigation.
- `openclaw/`: OpenClaw runtime and assistant setup.
- `investments/`: investment management guides, thesis files, templates, and profiles.
- `scripts/`: utility scripts for maintenance and validation.
- `local_secrets/`: local-only secrets storage (must be gitignored).

## Core governance files

- Repository concept: `docs/jaxx_repository_concept.md`
- Naming and operating conventions: `docs/conventions.md`
- Step 2 plan and mapping: `docs/step2_move_plan.md`
- Step 2 execution tracking: `docs/step2_execution_report.md`
- Step 3 decision queue: `docs/step3_dedup_review.md`

## Implemented layout snapshot

```text
jaxx_open_claw_setup/
  README.md

  docs/
    archive/
    index.md
    conventions.md
    jaxx_repository_concept.md
    step2_move_plan.md
    step2_execution_report.md

  openclaw/
    assistant/
      identity/
      memory_policy/
    system/
      config/
      installation/
        current/
        legacy/

  investments/
    guides/
      active/
      archive/
    operations/
    profiles/
    templates/
    thesis/
      constitutions/
      portfolio/

  scripts/
  local_secrets/

  credentials/      # retained until Step 4 cleanup
  workspace_files/  # residual files pending Step 3 cleanup
  100_All_Guides/   # residual files pending Step 3 cleanup
```

## Usage rules

1. Identify the content type first.
2. Open the canonical area for that content type.
3. Keep one active canonical file and archive prior versions.
4. Do not store live credentials in tracked files.

## Next checkpoint

- Step 2 is complete.
- Next: Step 3 finalization pending only the template-variant decision in `docs/step3_dedup_review.md`.
- Next: Step 3 deduplication and filename normalization (decision queue in `docs/step3_dedup_review.md`).
- Then: Step 4 secrets hardening and credential removal from tracked paths.
