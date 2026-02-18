# Step 3 Deduplication Review Queue

Version: 1.0.0
Last Updated: 2026-02-18
Status: Awaiting user decisions

## Purpose

This file tracks Step 3 deduplication decisions in a no-loss workflow.
It follows the agreed rule: when the newest file cannot be determined reliably, present all candidates for user choice.

## Decision methodology

1. If a clear semantic version exists, keep the highest version in `active/` and keep prior versions in `archive/`.
2. If two files are byte-identical and one is a copy suffix variant (`(1)`, `(2)`), keep the canonical non-suffix name.
3. If file role is ambiguous across domains (OpenClaw system vs investments), do not delete; request user decision.

## A) Clear by methodology (proposed automatic cleanup)

### A1. Copy-suffix duplicates with identical content

- Keep: `investments/guides/archive/Investment_Guide_v1.1.0_2026-02-10.md`
  - Duplicate candidate: `investments/guides/archive/Investment_Guide_v1.1.0_2026-02-10 (1).md`
- Keep: `investments/guides/archive/research-summary-template_v1.1.0_2026-02-10.md`
  - Duplicate candidate: `investments/guides/archive/research-summary-template_v1.1.0_2026-02-10 (1).md`

### A2. Same-version duplicate in `active/` and `archive/` with identical content

Proposed rule: keep only one canonical `active` copy for the current active version, keep historical versions in archive.

- `Investment_Guide_v1.2.0_2026-02-10.md`
  - Active: `investments/guides/active/Investment_Guide_v1.2.0_2026-02-10.md`
  - Archive duplicate: `investments/guides/archive/Investment_Guide_v1.2.0_2026-02-10.md`
- `Investment_Guide_v1.3.0_2026-02-10.md`
  - Active: `investments/guides/active/Investment_Guide_v1.3.0_2026-02-10.md`
  - Archive duplicate: `investments/guides/archive/Investment_Guide_v1.3.0_2026-02-10.md`

## B) Ambiguous and needs user decision

### B1. Cross-domain duplicates (same content, different location role)

These files are byte-identical but appear in both OpenClaw legacy and investment active areas. The canonical owner is unclear without product intent.

1. `openclaw/system/installation/legacy/USER_v1.1.0.md`
2. `investments/guides/active/USER_v1.1.0.md`

3. `openclaw/system/installation/legacy/open_claw_architecture_v_1_5_2.md`
4. `investments/guides/active/open_claw_architecture_v_1_5_2.md`

5. `openclaw/system/installation/legacy/openclaw_openrouter_presets_configuration_v_1_1.md`
6. `investments/guides/active/openclaw_openrouter_presets_configuration_v_1_1.md`

7. `openclaw/system/installation/legacy/open_claw_user_guide_v_1_2.md`
8. `investments/guides/active/open_claw_user_guide_v_1_2.md`

Decision requested for each pair:
- Keep both (because each domain keeps its own historical context), or
- Keep one canonical location and replace the other with a pointer note.

### B2. Non-versioned template variants

These files do not have trustworthy version metadata and cannot be ordered by date reliably:

- `investments/guides/archive/research-summary-template.md`
- `investments/guides/archive/research-summary-template (1).md`
- `investments/guides/archive/research-summary-template (2).md`
- `investments/guides/archive/research-summary-template (3).md`
- `investments/guides/archive/research-summary-template (4).md`

Decision requested:
- Keep all variants in archive with normalized names, or
- Select one as canonical and retire the rest.

## C) Placeholder files

These placeholders are identical and likely removable, but deletion is deferred until Step 3 approval:

- `100_All_Guides/txt.txt`
- `workspace_files/2nd_Installation/txt.txt`
- `openclaw/system/installation/legacy/txt.txt`

## Next action after decisions

Once decisions are confirmed, execute Step 3 in one commit with:
- full pre/post file manifests,
- deterministic rename/remove mapping,
- no content loss validation.
