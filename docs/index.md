# JAXX Repository Index

Version: 1.5.0
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
- Step 4 secrets hardening report: `docs/step4_secrets_hardening.md`
- Metadata/reference compliance proposal: `docs/metadata_reference_rubric_proposal_v1_0_0_2026-02-18.md`
- Metadata policy (active standard): `docs/metadata_policy.md`
- Metadata classification map: `docs/metadata_reference_classification_map.json`

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
    step3_dedup_review.md
    step4_secrets_hardening.md

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

  credentials/      # templates only (live credentials removed)
```

## Usage rules

1. Identify the content type first.
2. Open the canonical area for that content type.
3. Keep one active canonical file and archive prior versions.
4. Do not store live credentials in tracked files.

## Next checkpoint

- Step 2 is complete.
- Step 3 deduplication is complete.
- Step 4 secrets hardening is complete.


## References

- `docs/conventions.md` - naming and canonical source rules.
