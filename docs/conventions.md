# JAXX Repository Conventions

Version: 1.1.0
Last Updated: 2026-02-18
Status: Active

## Scope

This file defines operational rules for naming, placement, and maintenance.
Use `docs/jaxx_repository_concept.md` for high-level rationale.

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

## Canonical-source policy

One document type must have one canonical home.
- repository governance docs: `docs/`
- OpenClaw runtime docs/config: `openclaw/`
- investment docs/templates/thesis: `investments/`

If other folders need the same content, link to the canonical file instead of duplicating it.

## Active vs history vs archive

- active governance standards stay in top-level `docs/`
- completed plans and reports go to `docs/history/`
- versioned content history for domain docs stays in matching `archive/` folders
- when a new version becomes active, move the prior active version to archive

## Change workflow

For each documentation change:
1. edit the canonical active file
2. bump version/date if semantics changed
3. move replaced versions or process artifacts to history/archive as appropriate
4. update `docs/index.md` when structure or canonical links change
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
- `docs/index.md` reflects the real structure

## Ambiguous version resolution

If the newest file cannot be determined from explicit versioning in the filename:
- do not delete or overwrite candidates
- list candidates in a decision queue
- request explicit user selection before cleanup

If semantic versioning is explicit, keep the highest version active and move older versions to archive.

## References

- `docs/jaxx_repository_concept.md`
- `docs/index.md`
- `docs/history/README.md`
