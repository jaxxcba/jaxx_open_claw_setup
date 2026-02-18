# JAXX Repository Index

Version: 2.0.0
Last Updated: 2026-02-18
Status: Active

## Purpose

This is the canonical navigation map for the repository.
Use this file first to locate active standards and operational content.

## Canonical top-level areas

- `governance_docs/`: governance, navigation, and operator guidance.
- `openclaw/`: OpenClaw runtime and assistant setup.
- `investments/`: investment guides, thesis files, templates, and profiles.
- `scripts/`: utility scripts for maintenance and validation.
- `local_secrets/`: local-only secrets storage (must be gitignored).

## Normative core (default read path)

1. `README.md`
2. `governance_docs/index.md`
3. `governance_docs/conventions.md`
4. `governance_docs/operator_playbook.md`

## Active governance files

- Repository concept: `governance_docs/jaxx_repository_concept.md`
- Naming and operating conventions: `governance_docs/conventions.md`
- Metadata policy (active standard): `governance_docs/metadata_policy.md`
- Metadata classification map: `governance_docs/metadata_reference_classification_map.json`
- Metadata/reference compliance proposal: `governance_docs/metadata_reference_rubric_proposal_v1_0_0_2026-02-18.md`
- Operator playbook: `governance_docs/operator_playbook.md`

## History and completed artifacts (optional)

Historical process artifacts are stored in `governance_docs/history/` and are not required for daily operation.

Archived governance references are stored in `archive/` (for example: `archive/documentation_philosophy_assessment_v1.0.0_2026-02-18.md` and `archive/documentation_simplification_implementation_plan_v1.0.0_2026-02-18.md`).

Start here only if needed:
- `governance_docs/history/README.md`
- `governance_docs/history/phases_summary.md`

## Implemented layout snapshot

```text
jaxx_open_claw_setup/
  README.md

  governance_docs/
    index.md
    conventions.md
    jaxx_repository_concept.md
    metadata_policy.md
    metadata_reference_classification_map.json
    metadata_reference_rubric_proposal_v1_0_0_2026-02-18.md
    operator_playbook.md
    history/

  archive/

  openclaw/
    assistant/
      identity/
      memory_policy/
    system/
      config/
      installation/
        legacy/
          README.md

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
  credentials/
```

## Usage rules

1. Identify the content type first.
2. Edit the canonical area for that content type.
3. Keep one active canonical file and archive or history artifacts separate.
4. Do not store live credentials in tracked files.

## References

- `governance_docs/conventions.md` - naming and canonical source rules.
- `governance_docs/operator_playbook.md` - day-to-day operating guidance.
