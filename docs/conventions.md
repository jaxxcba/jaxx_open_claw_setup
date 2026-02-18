# JAXX Repository Conventions

Version: 1.0.0
Last Updated: 2026-02-18
Status: Active

## 1) Scope

These conventions define how files are named, where they live, and how changes are maintained.

## 2) Naming rules

### Folders
- lowercase only
- snake_case only
- no spaces

### Files
- lowercase snake_case preferred
- allow existing external naming only when required
- do not use suffixes such as `(1)`, `(2)`, `(copy)`

### Versioned markdown
- `topic_vX.Y.Z_YYYY-MM-DD.md`
- Example: `investment_guide_v1.4.0_2026-02-10.md`

### Thesis JSON files
- `thesis_<topic>_vX_Y.json`
- Example: `thesis_energy_systems_transition_v1_1.json`

## 3) Canonical-source policy

One document type must have one canonical home.
- Repository governance docs: `docs/`
- OpenClaw runtime docs/config: `openclaw/`
- Investment docs/templates/thesis: `investments/`

If other folders need the same content, add references, not duplicates.

## 4) Active vs archive policy

- Active documents live in `active/` folders.
- Prior versions live in corresponding `archive/` folders.
- Keep all historical versions for now.
- When a new version becomes active, move the previous active version to archive.

## 5) Change workflow

For each documentation change:
1. Edit canonical active file.
2. Bump version/date if semantics changed.
3. Move replaced version to archive.
4. Commit with a scope-first message.

Recommended commit style:
- `docs: ...`
- `repo: ...`
- `chore: ...`

## 6) Secrets policy

- Never commit live secrets, tokens, refresh tokens, or client secrets.
- Keep local secrets in `local_secrets/` only, and gitignore that path.
- Track only sanitized examples, for example `*.example.json`.
- Rotate and revoke any credentials that were previously committed.

## 7) Duplication policy

- Do not keep duplicate active files with identical purpose.
- Keep one active canonical file and archive alternatives if needed.
- Remove placeholder files like `txt.txt` during cleanup unless they serve a clear purpose.

## 8) Definition of done for organization updates

Organization changes are done when:
- every file has one clear canonical home,
- active files are easy to discover,
- archive files are separated from active files,
- no tracked secrets remain,
- `docs/index.md` reflects the real structure.
