# Step 2 Move Plan (Non-Destructive)

Version: 1.2.0
Last Updated: 2026-02-18
Status: Completed

## Purpose

Execute a safe, non-destructive move from the old layout to the approved Option A structure.
Step 2 performs moves only and does not delete files.

## Scope and assumptions

- Keep all historical versions during Step 2.
- Preserve duplicates for Step 3 review.
- Defer credential cleanup to Step 4.

## Folder tree created in Step 2

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

## Move mapping used

### OpenClaw system and assistant

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

### Investments

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

### General and legacy notes

- `workspace_files/read_me_workspace.md`
  -> `governance_docs/archive/readme_workspace_legacy.md`

- `100_All_Guides/txt.txt`
  -> retained for Step 3 cleanup review
- `workspace_files/1st_installation/txt.txt`
  -> retained for Step 3 cleanup review
- `workspace_files/2nd_Installation/txt.txt`
  -> retained for Step 3 cleanup review

## Sensitive files intentionally deferred

Handle in Step 4 with sanitization/replacement:

- `credentials/google_token.json`
- `credentials/google_oauth_client.json`
- `credentials/telegram-allowFrom.json`
- `credentials/telegram-pairing.json`
- `credentials/read_me_jaxx_credentials.md`
- `credentials/google_auth_bootstrap.py`

## Completion checklist

- [x] Create target folder tree
- [x] Move files according to mapping
- [x] Preserve all historical files
- [x] Preserve duplicates for Step 3
- [x] Update `governance_docs/index.md` to match new structure
- [x] Record execution in `governance_docs/step2_execution_report.md`

## Next actions

1. Step 3: deduplicate and normalize filenames.
2. Step 4: remove tracked credentials, add ignore rules, and replace with sanitized examples.
3. Run a path-reference pass and patch any stale links after deduplication.
