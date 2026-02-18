# JAXX Repository Index

Version: 1.0.0
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

## Current baseline docs

- Repository concept: `docs/jaxx_repository_concept.md`
- Naming and operating conventions: `docs/conventions.md`
- Step 2 move plan: `docs/step2_move_plan.md`

## Planned target layout

```text
jaxx_open_claw_setup/
  README.md
  docs/
    index.md
    conventions.md
    jaxx_repository_concept.md
    step2_move_plan.md

  openclaw/
    system/
      config/
      installation/
        current/
        legacy/
    assistant/
      identity/
      memory_policy/

  investments/
    guides/
      active/
      archive/
    thesis/
      constitutions/
      portfolio/
    templates/
    profiles/
    operations/

  scripts/
  local_secrets/
```

## How to use this index

1. Identify the content type (system, investments, governance, scripts, secrets).
2. Open the canonical area for that content type.
3. If the file exists in multiple places, keep only one canonical copy in active locations and archive the rest.
4. Never place live credentials in tracked paths.

## Next action checkpoint

This index is Step 1 output.
Next, execute the Step 2 move plan in `docs/step2_move_plan.md`.
