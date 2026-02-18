# Documentation Simplification Implementation Plan

Version: 1.0.0
Last Updated: 2026-02-18
Status: Active
Owner: Repository Governance

## Purpose

This plan converts the documentation philosophy assessment into immediate, executable implementation steps with low migration risk.

## Why now

The repository is well structured, but governance documentation has become heavy for routine operator workflows. This plan simplifies access paths while preserving compliance and traceability.

## Scope

In scope:
- simplify default documentation entry path,
- separate normative versus historical/process artifacts,
- reduce onboarding reading burden,
- preserve existing safety and governance controls.

Out of scope:
- changing investment or assistant content semantics,
- deleting historical documents,
- modifying secrets policy.

## Assumptions

- Existing canonical-source and naming rules remain authoritative.
- Historical documents must remain available and linkable.
- Simplification should be non-destructive and reversible.

## Execution status

- 2026-02-18: Phase 1 executed. Historical process artifacts moved to `governance_docs/history/`, and navigation was updated in `governance_docs/index.md`.
- 2026-02-18: Phase 2 executed. `governance_docs/operator_playbook.md` was added and linked in onboarding paths.
- 2026-02-18: Phase 3 executed. `governance_docs/jaxx_repository_concept.md` and `governance_docs/conventions.md` were consolidated to reduce overlap (concept = model, conventions = rules).

## Target operating model

Normative core (default path):
1. `README.md`
2. `governance_docs/index.md`
3. `governance_docs/conventions.md`
4. `governance_docs/operator_playbook.md` (new)

Historical/process layer (non-default path):
- `governance_docs/history/` for completed plans, reports, and one-off audits.

Policy layer (reference path):
- `governance_docs/metadata_policy.md` remains active and authoritative, referenced from conventions and index.

## Phase plan

### Phase 1: Create new layout and move non-normative artifacts

Objective:
- establish `governance_docs/history/` and move process/history files out of top-level `governance_docs/`.

Candidate files to move:
- `governance_docs/history/step2_move_plan.md`
- `governance_docs/history/step2_execution_report.md`
- `governance_docs/history/step3_dedup_review.md`
- `governance_docs/history/step4_secrets_hardening.md`
- `governance_docs/history/task_a_consistency_audit_2026-02-18.md`
- `governance_docs/history/metadata_compliance_implementation_plan_v1_0_0_2026-02-18.md`

Execution checklist:
- create `governance_docs/history/`.
- move files with `git mv` to preserve history.
- update links in `governance_docs/index.md`.
- add a `governance_docs/history/README.md` describing what belongs there.

Acceptance criteria:
- top-level `governance_docs/` contains only active canonical navigation/rules plus policy files.
- all moved files remain reachable from `governance_docs/index.md`.

### Phase 2: Add operator playbook and reduce entry friction

Objective:
- create one practical onboarding and operations file for day-to-day use.

Create:
- `governance_docs/operator_playbook.md` including:
  - 10-minute onboarding sequence,
  - common change recipes,
  - "where to edit" decision table,
  - pre-commit safety checklist.

Execution checklist:
- define default read order in `README.md` and `governance_docs/index.md`.
- keep playbook short, task-oriented, and linked to canonical rules.

Acceptance criteria:
- new contributor can find edit destination in under 3 minutes.
- default onboarding list is four files or fewer.

### Phase 3: Consolidate duplicated governance guidance

Objective:
- reduce overlap between `governance_docs/jaxx_repository_concept.md` and `governance_docs/conventions.md`.

Execution checklist:
- keep concept as "why and high-level model".
- keep conventions as "operational rules".
- remove duplicate rule text from concept where conventions already define behavior.

Acceptance criteria:
- no conflicting guidance across core governance documents.
- concept and conventions each have clearly distinct responsibility.

## Implementation commands (exact)

```zsh
#!/usr/bin/env zsh -f
set -euo pipefail

cd "/workspace/jaxx_open_claw_setup"

mkdir -p "/workspace/jaxx_open_claw_setup/governance_docs/history"

git mv "/workspace/jaxx_open_claw_setup/governance_docs/step2_move_plan.md" \
  "/workspace/jaxx_open_claw_setup/governance_docs/history/step2_move_plan.md"

git mv "/workspace/jaxx_open_claw_setup/governance_docs/step2_execution_report.md" \
  "/workspace/jaxx_open_claw_setup/governance_docs/history/step2_execution_report.md"

git mv "/workspace/jaxx_open_claw_setup/governance_docs/step3_dedup_review.md" \
  "/workspace/jaxx_open_claw_setup/governance_docs/history/step3_dedup_review.md"

git mv "/workspace/jaxx_open_claw_setup/governance_docs/step4_secrets_hardening.md" \
  "/workspace/jaxx_open_claw_setup/governance_docs/history/step4_secrets_hardening.md"

git mv "/workspace/jaxx_open_claw_setup/governance_docs/task_a_consistency_audit_2026-02-18.md" \
  "/workspace/jaxx_open_claw_setup/governance_docs/history/task_a_consistency_audit_2026-02-18.md"

git mv "/workspace/jaxx_open_claw_setup/governance_docs/metadata_compliance_implementation_plan_v1_0_0_2026-02-18.md" \
  "/workspace/jaxx_open_claw_setup/governance_docs/history/metadata_compliance_implementation_plan_v1_0_0_2026-02-18.md"

python3 "/workspace/jaxx_open_claw_setup/scripts/metadata_compliance_check.py" --strict --changed-from HEAD~1
```

## Risks and mitigations

1. Broken links after file moves.
   - Mitigation: update `governance_docs/index.md` in same commit and run link/reference checks if added later.
2. Confusion during transition.
   - Mitigation: keep transition notes in index and add `governance_docs/history/README.md`.
3. Over-consolidation that hides useful history.
   - Mitigation: never delete history in this initiative; move only.

## Verification checklist

- [x] `governance_docs/history/` exists and is linked from `governance_docs/index.md`.
- [x] Core governance files in top-level `governance_docs/` are reduced to normative set.
- [x] `governance_docs/operator_playbook.md` exists and is linked.
- [x] Metadata checker passes for changed files.
- [x] No secrets policy regressions.

## Decision log

- 2026-02-18: Adopt two-tier documentation model (normative core + history layer).

## References

- `governance_docs/documentation_philosophy_assessment_v1.0.0_2026-02-18.md`
- `README.md`
- `governance_docs/index.md`
- `governance_docs/conventions.md`
- `governance_docs/metadata_policy.md`
