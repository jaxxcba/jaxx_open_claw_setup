# Metadata Compliance Implementation Plan

Version: 1.0.0
Last Updated: 2026-02-18
Status: Active
Owner: Repository Governance

## Objective

Implement the metadata/reference policy consistently, with predictable rollout and no risky refactor.

## Why this plan

The policy and checker now exist, but baseline violations are still present.
This plan converts policy into an execution sequence with owners, timelines, and CI gates.

## Scope

In scope:
- active `.md`, `.json`, `.py` files covered by the classification map,
- policy-compliant metadata fields,
- references where required,
- CI enforcement rollout.

Out of scope:
- mass rewrites of archived docs,
- changing substantive content semantics just to satisfy metadata,
- deep refactors outside metadata/reference concerns.

## Phase plan

### Phase 0 - Baseline and freeze rules (Day 0)

Owner: Repository Governance

Steps:
1. Run baseline checker in warning mode and save results to an artifact.
2. Confirm controlled vocab:
   - Markdown status: `Active|Proposed|Deprecated|Archived`
   - JSON status: `active|proposed|deprecated|archived`
3. Confirm archive exemption remains active in `exclude_globs`.
4. Communicate "no new violations" rule for touched files.

Acceptance:
- Baseline report published.
- Vocabulary decision captured in docs.

### Phase 1 - High-value path cleanup (Days 1-3)

Owner: Documentation Maintainers

Target files first:
- `governance_docs/*.md` active governance files,
- `investments/guides/active/*.md`,
- `investments/thesis/constitutions/*.json`,
- `scripts/*.py` metadata fields.

Steps:
1. Add missing required metadata fields.
2. Add `## References` to required markdown classes.
3. Add required JSON keys and initial `source_refs`.
4. Add Python module metadata where required.

Acceptance:
- Warning output count reduced by at least 60 percent from baseline.
- Zero violations in `governance_docs/*.md`.

### Phase 2 - Protect changed files (Days 4-7)

Owner: CI Maintainers

Steps:
1. Add strict check for changed files only in CI:
   - `python3 scripts/metadata_compliance_check.py --strict --changed-from origin/main`
2. Keep full-repo warning report for visibility.
3. Add PR template checkbox: "metadata/reference policy verified for changed files".

Acceptance:
- New PRs cannot introduce new violations in changed files.
- Existing backlog continues to shrink without blocking all work.

### Phase 3 - Full active enforcement (Week 2+)

Owner: Repository Governance + CI Maintainers

Entry criteria:
- backlog near zero,
- remaining exceptions documented and approved.

Steps:
1. Enable strict check for full active scope:
   - `python3 scripts/metadata_compliance_check.py --strict`
2. Keep `governance_docs/archive/**` excluded.
3. Introduce exception process for temporary waivers (time-boxed).

Acceptance:
- Full strict mode passes in CI for active scope.
- Exception list is empty or has active owners and due dates.

## Work breakdown by file type

### Markdown (`.md`)

Checklist:
- top-of-file has `Version`, `Last Updated`, `Status`,
- status value in allowed vocabulary,
- required classes include `## References`.

### JSON (`.json`)

Checklist:
- has `schema_version`, `document_version`, `last_updated`, `status`, `source_refs`,
- `source_refs` is a list,
- required classes have non-empty `source_refs`.

### Python (`.py`)

Checklist:
- module docstring present,
- `__version__` and `__updated__` present,
- required classes have `REFERENCES` constant.

## RACI

- Responsible: maintainers editing files in scope.
- Accountable: Repository Governance.
- Consulted: CI maintainers, domain owners for content references.
- Informed: all contributors via docs index and PR template.

## Metrics and reporting

Track weekly:
- total violation count,
- violations by file type,
- violations by directory,
- percent of changed-file PRs passing strict check first try.

Success threshold:
- 2 consecutive weeks with strict changed-file check pass rate >= 95 percent.

## Risks and mitigations

Risk: over-enforcement slows delivery.
Mitigation: changed-files strict mode before full strict mode.

Risk: inconsistent references across domains.
Mitigation: keep classification map as single source of truth.

Risk: status vocabulary drift.
Mitigation: checker-enforced vocabulary and policy examples.

## Runbook

Warning mode:
- `python3 scripts/metadata_compliance_check.py`

Strict mode (changed files):
- `python3 scripts/metadata_compliance_check.py --strict --changed-from origin/main`

Strict mode (full active scope):
- `python3 scripts/metadata_compliance_check.py --strict`

## Self-audit checklist

Spec completeness:
- [x] File Plan
- [x] Acceptance tests
- [x] Migration and rollback clarified (not applicable: docs-only change)
- [x] Feature Flag assessment documented (not applicable: docs-only change)
- [x] Non-functional notes (logging/a11y not applicable for docs-only change)

Emission and quality:
- [x] Full files only, lint and format clean
- [x] Build and tests pass (governance_docs/script checks executed)
- [x] Migrations idempotent and reversible (not applicable: no migration)
- [x] Post-migration verification queries included (not applicable: no migration)
- [x] CHANGELOG updated under `[Unreleased]` (uncertain: no changelog file present in repository)

uncertain:
- No repository CHANGELOG file was found to update.

## References

- `governance_docs/metadata_policy.md` - active metadata/reference standard.
- `governance_docs/metadata_reference_classification_map.json` - enforcement scope and classes.
- `governance_docs/metadata_reference_rubric_proposal_v1_0_0_2026-02-18.md` - proposal rationale.
