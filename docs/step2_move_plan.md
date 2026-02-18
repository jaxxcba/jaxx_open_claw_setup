# Step 2 Move Plan (Non-Destructive)

Version: 1.1.0
Last Updated: 2026-02-18
Status: Completed

## Purpose

Prepare and execute a safe, non-destructive move from the old structure to the approved target structure.
No files are deleted in this step.

## Assumptions

- All historical versions are preserved for now.
- Duplicates are moved first and deduplicated in Step 3.
- Secrets removal is handled in Step 4.

## Planned folder creation

Create these folders before moving files:

- `openclaw/system/config/`
- `openclaw/system/installation/current/`
- `openclaw/system/installation/legacy/`
- `openclaw/assistant/identity/`
- `openclaw/assistant/memory_policy/`
- `investments/guides/active/`
- `investments/guides/archive/`
- `investments/thesis/constitutions/`
- `investments/thesis/portfolio/`
- `investments/templates/`
- `investments/profiles/`
- `investments/operations/`

## File mapping plan

### OpenClaw system and assistant files

- `openclaw.JSON Folder/openclaw 2026.02.26.json`
  -> `openclaw/system/config/openclaw_2026-02-26.json`

- `openclaw.JSON Folder/read_me_openclaw_JSON.md`
  -> `openclaw/system/config/readme_openclaw_json.md`

- `workspace_files/2nd_Installation/AGENTS.md`
  -> `openclaw/assistant/memory_policy/agents.md`
- `workspace_files/2nd_Installation/HEARTBEAT.md`
  -> `openclaw/assistant/memory_policy/heartbeat.md`
- `workspace_files/2nd_Installation/BOOTSTRAP.md`
  -> `openclaw/assistant/identity/bootstrap.md`
- `workspace_files/2nd_Installation/IDENTITY.md`
  -> `openclaw/assistant/identity/identity.md`
- `workspace_files/2nd_Installation/SOUL.md`
  -> `openclaw/assistant/identity/soul.md`
- `workspace_files/2nd_Installation/USER.md`
  -> `openclaw/assistant/identity/user.md`
- `workspace_files/2nd_Installation/TOOLS.md`
  -> `openclaw/assistant/identity/tools.md`

- `workspace_files/1st_installation/*`
  -> `openclaw/system/installation/legacy/`

### Investment files

- `Investment_Management_Concept/Guides/*.md`
  -> `investments/guides/active/`

- `Investment_Management_Concept/Archive/*`
  -> `investments/guides/archive/`

- `Investment_Management_Concept/Templates/*`
  -> `investments/templates/`

- `Investment_Management_Concept/Profiles/*`
  -> `investments/profiles/`

- `Investment_Management_Concept/Thesis/thesis_*.json`
  -> `investments/thesis/constitutions/`

- `Investment_Management_Concept/Thesis/portfolio_master_v1_0.json`
  -> `investments/thesis/portfolio/portfolio_master_v1_0.json`

- `Investment_Management_Concept/Thesis/research-sources.json`
  -> `investments/operations/research_sources.json`

- `Investment_Management_Concept/Thesis/OpenClaw_Thesis_System_v3_3.md`
  -> `investments/operations/openclaw_thesis_system_v3_3.md`

### General and temporary files

- `workspace_files/read_me_workspace.md`
  -> `docs/archive/readme_workspace_legacy.md`

- `100_All_Guides/txt.txt`
  -> candidate deletion in Step 3
- `workspace_files/1st_installation/txt.txt`
  -> candidate deletion in Step 3
- `workspace_files/2nd_Installation/txt.txt`
  -> candidate deletion in Step 3

## Sensitive files (do not move as-is)

These should be removed from tracked git content in Step 4 and replaced with sanitized examples:
- `credentials/google_token.json`
- `credentials/google_oauth_client.json`
- `credentials/telegram-allowFrom.json`
- `credentials/telegram-pairing.json`

These can be converted to template/example docs:
- `credentials/read_me_jaxx_credentials.md`
- `credentials/google_auth_bootstrap.py`

## Execution checklist for Step 2

- [x] Create target folder tree
- [x] Move files according to mapping
- [x] Keep all history files during move
- [x] Do not delete duplicates yet
- [x] Update `docs/index.md` after moves
- [x] Commit as a single non-destructive reorganization change

## Risks and mitigations

- Risk: accidental path conflicts due to duplicate names.
  - Mitigation: move in small batches and check `git status` after each batch.

- Risk: breaking references between docs.
  - Mitigation: run a link/path scan after moving and patch references in a follow-up commit.

- Risk: secrets still tracked.
  - Mitigation: complete Step 4 immediately after Step 3 stabilization.
