# JAXX OpenClaw Setup Repository

This repository is the control center for a personal OpenClaw setup.

It has two goals:
1. Keep OpenClaw system setup clean and stable.
2. Keep investment-management content organized, versioned, and easy to use.

If you are new to this repo, read this file first, then open `docs/index.md`.

## What this repository is for

This repo stores:
- OpenClaw runtime and assistant identity files.
- Investment guides, templates, thesis definitions, and profiles.
- Governance documents that explain how files should be named and where they belong.

This repo does **not** store live credentials.

## Repository structure (simple map)

```text
jaxx_open_claw_setup/
  README.md

  docs/
    index.md
    conventions.md
    jaxx_repository_concept.md
    step2_move_plan.md
    step2_execution_report.md
    step3_dedup_review.md
    step4_secrets_hardening.md
    task_a_consistency_audit_2026-02-18.md

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
    operations/
    profiles/
    templates/
    thesis/
      constitutions/
      portfolio/

  credentials/
    README.md
    examples/

  local_secrets/
    README.md

  scripts/
```

## Why there are both `credentials/` and `local_secrets/`

They are related, but they serve different purposes:

- `credentials/` (tracked in git)
  - Contains only safe templates and documentation.
  - Helps you and future contributors know required file shapes.

- `local_secrets/` (ignored by git)
  - Contains real keys/tokens only on your local machine.
  - Prevents accidental secret leaks into repository history.

Short version:
- `credentials/` = examples and instructions.
- `local_secrets/` = real secret material.

## Why archive folders exist in more than one area

Current policy uses **domain-local archives** (for example, `investments/guides/archive/`) instead of one global archive folder.

Reason:
- It keeps old versions next to the content family they belong to.
- It is easier to find history without cross-domain mixing.
- It reduces accidental confusion between OpenClaw system docs and investment docs.

Could we use one global `archive/` at repository root? Yes, but it usually becomes harder to navigate as content grows.

## Working rules (plain language)

- Keep one active canonical file per topic.
- Move replaced versions into the matching archive location.
- Use clear filenames with versions/dates when relevant.
- Never commit live credentials.
- Keep structure updates reflected in `docs/index.md`.

## Where to go next

- Repository map: `docs/index.md`
- Naming and maintenance rules: `docs/conventions.md`
- Full structure rationale: `docs/jaxx_repository_concept.md`
- Recent audit report: `docs/task_a_consistency_audit_2026-02-18.md`

## Current status snapshot

- Step 2 (restructure): completed.
- Step 3 (deduplication): completed.
- Step 4 (secrets hardening): completed.

Next practical step is optional Task B: documentation wording cleanup for historical path references in migration reports.
