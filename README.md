# JAXX Open Claw Setup

This repository is the home for a personal research and operating setup.

The goal is simple:
- keep important knowledge in clear files,
- separate sensitive data from normal project data,
- make daily work repeatable,
- make it easy for a new person to understand where everything lives.

If you are new, read this page first, then open `governance_docs/index.md`.

## Project philosophy

This project follows a few practical ideas:

1. Write things down in files, not in memory.
2. Keep secret data out of version control.
3. Group files by purpose so nothing is hidden.
4. Keep old versions in archive folders so active folders stay clean.
5. Prefer plain text and simple markdown so the setup stays readable for years.

In short: this repo is a "system notebook" for operating, research, and assistant behavior.

## Big picture

```text
+---------------------------------------------------+
|                  jaxx_open_claw_setup             |
|---------------------------------------------------|
| governance_docs/         -> map, standards, playbook, history |
| openclaw/     -> assistant identity and system    |
| investments/  -> investing thesis, guides, ops    |
| credentials/  -> examples of credential files     |
| local_secrets/-> local-only secret storage area   |
| scripts/      -> helper scripts                   |
+---------------------------------------------------+
```

## Directory structure

```text
jaxx_open_claw_setup/
|-- README.md
|-- governance_docs/
|   |-- index.md
|   |-- jaxx_repository_concept.md
|   |-- conventions.md
|   |-- operator_playbook.md
|   `-- history/
|       `-- (completed plans and reports)
|
|-- archive/
|   `-- (legacy repository artifacts)
|
|-- openclaw/
|   |-- assistant/
|   |   |-- identity/
|   |   |   |-- bootstrap.md
|   |   |   |-- identity.md
|   |   |   |-- soul.md
|   |   |   |-- tools.md
|   |   |   `-- user.md
|   |   `-- memory_policy/
|   |       |-- agents.md
|   |       `-- heartbeat.md
|   `-- system/
|       |-- config/
|       |   |-- openclaw_2026-02-26.json
|       |   `-- readme_openclaw_json.md
|       `-- installation/
|           `-- legacy/
|               |-- README.md
|               `-- # JAXX -- Operating Constitution (v1.0).md
|
|-- investments/
|   |-- guides/
|   |   |-- active/   (current guides)
|   |   `-- archive/  (created when superseded guide versions exist)
|   |-- operations/
|   |   |-- research_results/
|   |   `-- logs/
|   |-- profiles/
|   |   `-- trader_profile_*.md
|   |-- templates/
|   |   `-- research and briefing templates
|   `-- thesis/
|       |-- constitutions/
|       `-- portfolio/
|
|-- credentials/
|   |-- README.md
|   `-- examples/
|       `-- *.example.json
|
|-- local_secrets/
|   |-- README.md
|   `-- .gitkeep
|
`-- scripts/
    `-- google_auth_bootstrap.py
```

## How the parts work together

```text
                 +----------------------+
                 |      governance_docs/           |
                 | rules, playbook, map |
                 +----------+-----------+
                            |
                            v
+----------------+   +------+-------+   +----------------------+
|  openclaw/     |<->| operator use |<->| investments/         |
| assistant role |   | and workflow |   | research content     |
+--------+-------+   +------+-------+   +----------+-----------+
         |                  |                      |
         v                  v                      v
+----------------+   +----------------+   +---------------------+
| credentials/   |   | local_secrets/ |   | scripts/            |
| file formats   |   | real secrets   |   | helper automation   |
+----------------+   +----------------+   +---------------------+
```

- `governance_docs/` explains the rules and changes.
- `openclaw/` defines how the assistant should behave.
- `investments/` contains the actual research framework and outputs.
- `credentials/` holds safe examples of expected secret file formats.
- `local_secrets/` is the place for real private values on your machine.
- `scripts/` provides practical setup helpers.

## What to read first (new contributor path)

1. `README.md` (this file)
2. `governance_docs/index.md`
3. `governance_docs/conventions.md`
4. `governance_docs/operator_playbook.md`
5. Then enter the area you need (`openclaw/` or `investments/`).
6. Use `credentials/README.md` and `local_secrets/README.md` when handling secret-related setup.

## Safety model for sensitive data

Use this simple rule:

- `credentials/examples/` = fake or template values that are safe to commit.
- `local_secrets/` = real local values that should stay private.

Never put live keys, tokens, or account secrets into normal tracked files.

## Change strategy

When you update this repository:

- keep active files in active folders,
- move old versions into archive folders,
- keep filenames clear and date or version tagged,
- update `governance_docs/index.md` when the structure changes,
- keep this README in sync with major structure changes.

## Quick maintenance checklist

- [ ] New files placed in the correct area.
- [ ] No real secrets added to tracked files.
- [ ] Active vs archive split still clear.
- [ ] Docs updated when structure changes.
- [ ] New person can find what they need in under 5 minutes.

## Plain-language summary

This repository is a structured home for:
- operating instructions,
- assistant behavior definitions,
- investment research system files,
- and safe handling of sensitive data.

It is designed to be understandable, stable, and easy to continue over time.
