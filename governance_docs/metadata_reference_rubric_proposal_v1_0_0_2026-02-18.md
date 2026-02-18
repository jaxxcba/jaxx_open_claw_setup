# Metadata and Reference Compliance Proposal

Version: 1.0.0
Last Updated: 2026-02-18
Status: Proposed
Owner: Repository Governance

## 1) Goal

Move from "close" to "fully compliant" with a practical, low-risk standard for metadata and references across `.md`, `.json`, and `.py` files.

This proposal defines:
- one metadata rubric per file type,
- where references are required versus optional,
- what is best practice and fit for purpose for this repository.

## 2) Scope and non-goals

Scope:
- repository content quality and consistency,
- authoring and review standards,
- lightweight validation guidance.

Non-goals:
- large structural refactors,
- retroactive rewrites of archival/historical records,
- introducing strict schemas that break existing valid content.

## 3) Core policy decisions

1. **Single rubric per file type**
   Each file type has one canonical metadata contract.

2. **Reference requirement by content intent**
   References are mandatory only where claims, decisions, or external facts require traceability.

3. **Historical tolerance**
   Archived documents may remain as-is unless materially edited.

4. **Progressive enforcement**
   Start with "warn" checks, then move to "required" for active canonical files.

## 4) Metadata rubric by file type

### 4.1 Markdown (`.md`)

#### Required metadata (active governance/guide/report docs)
At top of file:
- `Version:`
- `Last Updated:` (ISO `YYYY-MM-DD`)
- `Status:` (`Active`, `Proposed`, `Deprecated`, `Archived`)

#### Recommended metadata
- `Owner:` (team or area)
- `Scope:` (optional short phrase)

#### Reference format
- Preferred: bullet list under `## References`.
- Each reference should include enough locator detail to be actionable (path/URL + context).

### 4.2 JSON (`.json`)

#### Required metadata keys
- `schema_version` (string)
- `document_version` (string)
- `last_updated` (ISO date)
- `status` (`active`, `proposed`, `deprecated`, `archived`)
- `source_refs` (array; can be empty if references are optional for that file class)

#### Recommended metadata keys
- `owner`
- `notes`

#### Reference format
- `source_refs` array of objects:
  - `type` (`internal`, `external`)
  - `location` (repo path or URL)
  - `note` (brief purpose)

### 4.3 Python (`.py`)

#### Required metadata
At module top:
- module docstring with purpose sentence,
- `__version__` constant,
- `__updated__` date constant (`YYYY-MM-DD`).

#### Recommended metadata
- `__owner__`
- `__status__` (`active`, `experimental`, `deprecated`)

#### Reference format
- If references are required for the module class, include a `REFERENCES` constant list with strings (paths/URLs).
- Otherwise, no reference list required.

## 5) Required vs optional references matrix

### 5.1 References **required**

Use required references when files contain any of:
- policy or governance decisions,
- operational runbooks and procedures,
- factual assertions influencing investment or system decisions,
- schema/contract definitions consumed by automation,
- migration or validation logic definitions.

### 5.2 References **optional**

References may be optional for:
- templates intended as starting points,
- personal/profile preference files,
- purely descriptive onboarding text without factual claims,
- small utility scripts with self-contained logic.

### 5.3 References **not required**

Not required for:
- generated artifacts,
- obvious boilerplate,
- transient local-only examples where traceability adds no value.

## 6) Fit-for-purpose examples in this repository

- `governance_docs/` governance files: metadata required, references required where claims/decisions are made.
- `investments/guides/active/`: metadata required, references required for analytical/factual content.
- `investments/templates/`: metadata required, references optional unless template encodes policy.
- `investments/thesis/constitutions/*.json`: JSON metadata required, `source_refs` required.
- small helper scripts in `scripts/`: Python metadata required; references optional unless script codifies policy rules.

## 7) Lightweight compliance checks (low risk)

Phase 1 (warn only):
- missing required metadata fields,
- missing `## References` in markdown files classified as "required references",
- missing `source_refs` in JSON files classified as "required references".

Phase 2 (enforce on active canonical files):
- block merges only for newly changed files that fail rubric.

Phase 3 (expand):
- broaden enforcement to all active files, keep archives exempt.

## 8) Implementation plan

1. Approve this rubric and classification matrix.
2. Create a small `governance_docs/metadata_policy.md` from this proposal (active standard).
3. Add a file-class map in `governance_docs/` identifying required-reference classes.
4. Add a non-blocking validation script in `scripts/`.
5. Run once, capture findings, fix only active canonical files.
6. Enable CI warning mode, then gate mode for touched active files.

## 9) Acceptance criteria for "fully compliant"

A repository is "fully compliant" when:
- active `.md`, `.json`, and `.py` files meet required metadata rubric,
- files in required-reference classes include valid references,
- CI reports zero violations for changed active files,
- archive files are either exempt or compliant when edited.

## 10) Open decisions to confirm

1. Exact controlled vocabulary for statuses (`Active` vs `active`) by type.
2. Whether template files should require `Version`.
3. Whether `README.md` should follow full markdown rubric or a minimal variant.
4. Threshold for moving from warning mode to blocking mode.

## 11) Concrete implementation delivered

The following implementation artifacts are now in place:
- Policy standard: `governance_docs/metadata_policy.md`
- File-class and requirement map: `governance_docs/metadata_reference_classification_map.json`
- Automated checker: `scripts/metadata_compliance_check.py`
- Implementation plan: `governance_docs/metadata_compliance_implementation_plan_v1_0_0_2026-02-18.md`

Immediate execution steps:
1. Run warning mode in CI and publish violation summary.
2. Fix high-priority active files first (`governance_docs/`, active investment guides, constitutions).
3. Enable strict mode for changed files.
4. Expand strict mode to full active set once violation count is near zero.


## References

- `governance_docs/conventions.md` - repository conventions used by this proposal.
- `governance_docs/index.md` - canonical navigation map for policy placement.
