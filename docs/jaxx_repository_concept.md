# JAXX Repository Concept

Version: 1.0.0
Last Updated: 2026-02-18
Status: Approved baseline

## 1) Purpose

This document defines a simple and durable filing concept for the `jaxx_open_claw_setup` repository.

Goals:
- Keep OpenClaw system files separate from investment-management content.
- Keep active files easy to find and maintain.
- Keep history available without cluttering active work areas.
- Reduce risk by removing secrets from version control.

## 2) Guiding principles

1. One concern per folder.
2. One canonical location per document type.
3. Active and archive content are separated.
4. Names are predictable and machine-friendly.
5. Secrets are never committed.

## 3) Repository structure (Option A)

Target structure:

```text
jaxx_open_claw_setup/
  README.md
  docs/
    index.md
    jaxx_repository_concept.md
    conventions.md

  openclaw/
    system/
      config/
        openclaw.json
      installation/
        current/
        legacy/
    assistant/
      identity/
      memory_policy/

  investments/
    guides/
      active/
      archive/
    thesis/
      constitutions/
      portfolio/
    templates/
    profiles/
    operations/

  scripts/

  local_secrets/          # local only, gitignored
  .gitignore
```

## 4) Folder responsibilities

### `docs/`
Repository governance and navigation.
- `index.md`: map of where everything lives.
- `conventions.md`: naming and maintenance rules.
- `jaxx_repository_concept.md`: this concept document.

### `openclaw/`
OpenClaw runtime and assistant setup only.
- `system/config/`: operational config (for example, `openclaw.json`).
- `system/installation/current/`: currently used install baseline.
- `system/installation/legacy/`: previous installs kept only for reference.
- `assistant/identity/`: assistant identity and behavior files.
- `assistant/memory_policy/`: memory and continuity instructions.

### `investments/`
Investment-management system and knowledge base.
- `guides/active/`: one active version per guide.
- `guides/archive/`: prior versions for traceability.
- `thesis/constitutions/`: thesis JSON constitutions.
- `thesis/portfolio/`: portfolio-level overlays and policy objects.
- `templates/`: report and briefing templates.
- `profiles/`: investor/operator profile docs.
- `operations/`: process playbooks and cadence docs.

### `scripts/`
Utility scripts for validation, indexing, and maintenance.

## 5) Naming conventions

General:
- Folders: lowercase `snake_case`, no spaces.
- Files: lowercase `snake_case` preferred, except externally-defined names.
- Never use duplicate suffixes like `(1)`, `(2)`, `(copy)`.

Markdown docs:
- `topic_vX.Y.Z_YYYY-MM-DD.md`
- Examples:
  - `investment_guide_v1.4.0_2026-02-10.md`
  - `research_summary_template_v1.2.0_2026-02-10.md`

JSON constitutions:
- `thesis_<topic>_vX_Y.json`
- Example:
  - `thesis_energy_systems_transition_v1_1.json`

## 6) Active vs archive policy

For now, keep all historical files, but apply strict placement:
- Current working docs go under `active/`.
- Historical versions go under `archive/`.
- If a new version is published, move the prior active file to archive.

Version control policy:
- GitHub is the source of historical versions and diffs.
- Archive folders are for readability and operational clarity, not for duplicating exact copies in multiple locations.

## 7) Canonical-source policy

Each document type has one canonical home:
- OpenClaw architecture docs: `openclaw/` subtree only.
- Investment guides/templates/thesis: `investments/` subtree only.
- Repository policies: `docs/` only.

If a file is needed in another context, link to the canonical file instead of duplicating it.

## 8) Secrets and credentials policy

Required policy:
1. No live credentials in git.
2. Store local secrets in `local_secrets/` (gitignored) or secret manager.
3. Keep only sanitized examples in repo, for example:
   - `google_oauth_client.example.json`
   - `telegram_allow_from.example.json`
4. Rotate/revoke any credentials previously committed.
5. Never include tokens, refresh tokens, or client secrets in Markdown docs.

## 9) Migration approach (safe, staged)

Stage 1 (documentation):
- Approve this concept and publish `docs/index.md` + `docs/conventions.md`.

Stage 2 (non-destructive move):
- Create new folder structure.
- Move files into canonical locations.
- Keep all historical versions.

Stage 3 (dedup and normalize):
- Remove duplicate files and `(1)/(2)` naming.
- Keep one canonical copy per active doc.

Stage 4 (secrets hardening):
- Remove credential files from repo.
- Add `.gitignore` rules and sanitized examples.
- Rotate exposed credentials.

## 10) Day-to-day maintenance workflow

When editing a concept doc:
1. Update the active file in its canonical location.
2. Bump version/date if content meaning changed.
3. If superseding a prior active version, move previous file to archive.
4. Commit with clear scope message.

When adding a new file:
1. Decide whether it is `openclaw`, `investments`, or `docs`.
2. Place it in the canonical subtree.
3. Follow naming conventions.
4. Avoid cross-folder duplicates.

## 11) Definition of done for repository organization

The repository is considered organized when:
- Every file has one clear home.
- Active files are easy to find in less than 2 clicks from root.
- Archive files are preserved but separated from active work.
- No secrets are tracked by git.
- README and docs index make navigation obvious for future sessions.

## 12) Immediate next actions

1. Create `docs/index.md` with a clickable map.
2. Create `docs/conventions.md` with naming and archive rules.
3. Execute staged file moves into `openclaw/` and `investments/`.
4. Remove committed secrets and replace with templates.
5. Add and validate `.gitignore` for secrets and local runtime artifacts.

