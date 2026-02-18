# JAXX Repository Index

Version: 1.9.0
Last Updated: 2026-02-18
Status: Active

## Purpose

This is the canonical navigation map for the repository.
Use this file first to locate active standards and operational content.

## Canonical top-level areas

- `docs/`: governance, navigation, and operator guidance.
- `openclaw/`: OpenClaw runtime and assistant setup.
- `investments/`: investment guides, thesis files, templates, and profiles.
- `scripts/`: utility scripts for maintenance and validation.
- `local_secrets/`: local-only secrets storage (must be gitignored).

## Normative core (default read path)

1. `README.md`
2. `docs/index.md`
3. `docs/conventions.md`
4. `docs/operator_playbook.md`

## Active governance files

- Repository concept: `docs/jaxx_repository_concept.md`
- Naming and operating conventions: `docs/conventions.md`
- Metadata policy (active standard): `docs/metadata_policy.md`
- Metadata classification map: `docs/metadata_reference_classification_map.json`
- Metadata/reference compliance proposal: `docs/metadata_reference_rubric_proposal_v1_0_0_2026-02-18.md`
- Documentation philosophy assessment: `docs/documentation_philosophy_assessment_v1.0.0_2026-02-18.md`
- Documentation simplification implementation plan: `docs/documentation_simplification_implementation_plan_v1.0.0_2026-02-18.md`
- Operator playbook: `docs/operator_playbook.md`

## History and completed artifacts

Historical process artifacts are stored in `docs/history/`.

- `docs/history/README.md`
- `docs/history/step2_move_plan.md`
- `docs/history/step2_execution_report.md`
- `docs/history/step3_dedup_review.md`
- `docs/history/step4_secrets_hardening.md`
- `docs/history/task_a_consistency_audit_2026-02-18.md`
- `docs/history/metadata_compliance_implementation_plan_v1_0_0_2026-02-18.md`

## Implemented layout snapshot

```text
jaxx_open_claw_setup/
  README.md

  docs/
    index.md
    conventions.md
    jaxx_repository_concept.md
    metadata_policy.md
    metadata_reference_classification_map.json
    metadata_reference_rubric_proposal_v1_0_0_2026-02-18.md
    documentation_philosophy_assessment_v1.0.0_2026-02-18.md
    documentation_simplification_implementation_plan_v1.0.0_2026-02-18.md
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

- `docs/conventions.md` - naming and canonical source rules.
- `docs/operator_playbook.md` - day-to-day operating guidance.
