# JAXX Repository Conventions

Version: 1.2.0
Last Updated: 2026-02-18
Status: Active

## Scope

This file defines operational rules for naming, placement, and maintenance.
Use `governance_docs/jaxx_repository_concept.md` for high-level rationale.

## Naming rules

### Folders
- lowercase only
- snake_case only
- no spaces

### Files
- lowercase snake_case preferred
- allow external naming only when required
- do not use suffixes such as `(1)`, `(2)`, `(copy)`

### Versioned markdown
- `topic_vX.Y.Z_YYYY-MM-DD.md`
- example: `investment_guide_v1.4.0_2026-02-10.md`

### Thesis JSON files
- `thesis_<topic>_vX_Y.json`
- example: `thesis_energy_systems_transition_v1_1.json`

### Version token style for new files
- for new versioned markdown files, use `vX.Y.Z` token style in filenames
- example: `investment_guide_v1.4.0_2026-02-10.md`
- existing legacy files using underscore tokens (for example `v1_0_0`) are grandfathered and should not be renamed only for style

## Canonical-source policy

One document type must have one canonical home.
- repository governance docs: `governance_docs/`
- OpenClaw runtime config and docs: `openclaw/`
- investment templates and thesis docs: `investments/`

If other folders need the same content, link to the canonical file instead of duplicating it.

## Active vs history vs archive

- active governance standards stay in top-level `governance_docs/`
- completed plans and reports go to `governance_docs/history/`
- versioned content history for domain docs stays in matching `archive/` folders
- when a new version becomes active, move the prior active version to archive

## Change workflow

For each documentation change:
1. edit the canonical active file
2. bump version/date if semantics changed
3. move replaced versions or process artifacts to history/archive as appropriate
4. update `governance_docs/index.md` when structure or canonical links change
5. commit with a scope-first message

Recommended commit prefixes:
- `docs: ...`
- `repo: ...`
- `chore: ...`

## Secrets policy

- never commit live secrets, tokens, refresh tokens, or client secrets
- keep local secrets in `local_secrets/` only, and gitignore that path
- track only sanitized examples, such as `*.example.json`
- rotate and revoke credentials that were previously committed

## Definition of done for organization updates

Organization changes are done when:
- every file has one clear canonical home
- active files are easy to discover
- historical and archived files are separated from active files
- no tracked secrets remain
- `governance_docs/index.md` reflects the real structure

## Ambiguous version resolution

If the newest file cannot be determined from explicit versioning in the filename:
- do not delete or overwrite candidates
- list candidates in a decision queue
- request explicit user selection before cleanup

If semantic versioning is explicit, keep the highest version active and move older versions to archive.

## Documentation hygiene checkpoint

When a change affects repository structure, required checkpoint files are:
- `README.md`
- `governance_docs/index.md`
- domain-level README files under `investments/`, `credentials/`, and `local_secrets/` as applicable

These files must be reviewed and updated in the same change set when references or layout snapshots drift.

## References

- `governance_docs/jaxx_repository_concept.md`
- `governance_docs/index.md`
- `governance_docs/history/README.md`
