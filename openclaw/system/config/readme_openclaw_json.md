# OpenClaw System Config Notes

This folder stores the tracked OpenClaw runtime configuration template used for repository documentation and setup reference.

## Security rule

Do not commit real tokens in `openclaw_2026-02-26.json`.

Use placeholders in tracked files and keep real values only in local machine secret storage.

Sensitive fields include:
- `channels.telegram.botToken`
- `gateway.auth.token`
