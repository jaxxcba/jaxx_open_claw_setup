# Step 3 Deduplication Review Queue

Version: 1.2.0
Last Updated: 2026-02-18
Status: In progress (cross-domain decisions applied, template decision pending)

## Purpose

Track Step 3 deduplication in a no-loss workflow.
When canonical ownership cannot be determined reliably, present all candidates for explicit user choice before further deletion.

## Completed deterministic cleanup

The following duplicates/placeholders were removed without ambiguity:

- Removed copy-suffix duplicate:
  - `investments/guides/archive/Investment_Guide_v1.1.0_2026-02-10 (1).md`
- Removed copy-suffix duplicate:
  - `investments/guides/archive/research-summary-template_v1.1.0_2026-02-10 (1).md`
- Removed same-version duplicates from archive where an identical active canonical exists:
  - `investments/guides/archive/Investment_Guide_v1.2.0_2026-02-10.md`
  - `investments/guides/archive/Investment_Guide_v1.3.0_2026-02-10.md`
- Removed placeholder files:
  - `100_All_Guides/txt.txt`
  - `workspace_files/2nd_Installation/txt.txt`
  - `openclaw/system/installation/legacy/txt.txt`

## Explicit user decisions applied

User-selected canonical owner for cross-domain duplicates: keep `openclaw/system/installation/legacy/*` versions and remove corresponding `investments/guides/active/*` copies.

Removed according to decision:
- `investments/guides/active/USER_v1.1.0.md`
- `investments/guides/active/open_claw_architecture_v_1_5_2.md`
- `investments/guides/active/openclaw_openrouter_presets_configuration_v_1_1.md`
- `investments/guides/active/open_claw_user_guide_v_1_2.md`

## Pending explicit user decision

### Non-versioned template variants (archive)

Please choose one policy:
- Keep all variants (rename to normalized archive names), or
- Select one canonical file and retire the others.

Candidates:
- `investments/guides/archive/research-summary-template.md`
- `investments/guides/archive/research-summary-template (1).md`
- `investments/guides/archive/research-summary-template (2).md`
- `investments/guides/archive/research-summary-template (3).md`
- `investments/guides/archive/research-summary-template (4).md`

## Next action

After the template decision above, execute final Step 3 normalization commit and then proceed to Step 4 secrets hardening.
