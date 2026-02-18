# Metadata and Reference Policy

Version: 1.0.0
Last Updated: 2026-02-18
Status: Active
Owner: Repository Governance

## Purpose

This policy operationalizes metadata and reference compliance for `.md`, `.json`, and `.py` files.
It is the implementation standard for active files and is designed for low-risk rollout.

## 1) Required metadata by file type

### Markdown (`.md`)

Required fields near top of file:
- `Version:`
- `Last Updated:` (ISO date `YYYY-MM-DD`)
- `Status:` (`Active`, `Proposed`, `Deprecated`, `Archived`)

Required references for classes marked required:
- `## References` heading must exist.

### JSON (`.json`)

Required top-level keys:
- `schema_version` (string)
- `document_version` (string)
- `last_updated` (ISO date `YYYY-MM-DD`)
- `status` (`active`, `proposed`, `deprecated`, `archived`)
- `source_refs` (array)

### Python (`.py`)

Required module metadata:
- module docstring on top of file
- `__version__ = "..."`
- `__updated__ = "YYYY-MM-DD"`

Required references for classes marked required:
- `REFERENCES = [...]` constant must exist.

## 2) Reference requirement classes

Reference requirements are managed by:
- `governance_docs/metadata_reference_classification_map.json`

Rules:
- `reference_required_globs`: references are mandatory.
- `reference_optional_globs`: references are recommended but not mandatory.
- files not matching either list default to optional.

## 3) Rollout plan

Phase 1 (warn mode):
- run checker in warning mode in CI, no merge block.
- fix violations in active canonical files as they are touched.

Phase 2 (strict on changed active files):
- run checker in strict mode only on changed files.
- block merge on violations.

Phase 3 (strict on all active files):
- enforce full active set.
- keep archive paths exempt by configuration.

## 4) Operational commands

Run warning mode:
- `python3 scripts/metadata_compliance_check.py`

Run strict mode:
- `python3 scripts/metadata_compliance_check.py --strict`

Run strict mode on changed files only:
- `python3 scripts/metadata_compliance_check.py --strict --changed-from HEAD~1`

## 5) Ownership

- Policy owner: Repository Governance.
- Classification updates require policy owner review.
- Any new active doc class should be added to the classification map in the same change.

## References

- `governance_docs/metadata_reference_rubric_proposal_v1_0_0_2026-02-18.md` - source proposal and rationale.
- `governance_docs/conventions.md` - canonical location and naming conventions.
