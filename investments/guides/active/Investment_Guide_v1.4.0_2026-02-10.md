# Investment Management Guide
Version: 1.4.0
Last Updated: 2026-02-10

## Core Investment Theses (2026-02-09)
1. **Bitcoin and dedicated L1 crypto protocols**
2. **Energy for AI and electrification**
3. **Scarcity with AI incoming**
4. **AI Data Center and Infrastructure**

Guiding principles:
- Always reference each thesis by its exact name.
- Map new research/investments to the relevant thesis and note percent allocation where available.
- Await detailed thesis narratives and current holdings; update this guide accordingly when provided.
- Incorporate research received from 22VResearch analysts (Dennis DeBusschere, Mark Whaling, Jordi Visser) into the thesis framework as soon as it arrives.

## Research Report Archiving (versioned 2026-02-10)
- Draft summaries locally only as a temporary staging step. As soon as the Markdown (`.md`) and Google Doc versions are uploaded to Drive (`Investments/Reports/<YYYY>/<MM>/`), delete the local copies to prevent duplication between the workspace and Drive.
- Naming: `<source>-YYYY-MM-DD-<short-description>.md` for Markdown, and `Source – YYYY-MM-DD – Short Description (Doc)` for Google Docs. The short description should be a 3–6 word slug, ideally derived from the research subject line (e.g., `ai-users-ex-software`).
- Conversion flow: Markdown → HTML (for formatting) → Google Doc upload via Drive API to ensure presentation-quality output. PDFs remain optional.
- The Gmail monitor evaluates every inbox email for research relevance (trusted forwarders, subject/keyword scan, attachments). When uncertain, leave the message untouched and ping the user for guidance before discarding anything.
- Treat Drive as the canonical repository. Local files should only exist while editing; confirm removal at the end of each session.
- Log and resolve any Drive or Doc upload failures immediately; do not consider a report complete until both artifacts are present in Drive.


## Versioning & Archives (versioned 2026-02-10)
- Every instruction/template must declare `Version` and `Last Updated` at the top. Bump the version and date with each modification.
- Maintain active instruction files in `Investments/Guides/`. When a new version is published, move the previous version into `Investments/Archive/` with a filename that encodes the version and date (e.g., `Investment_Guide_v1.0.0_2026-02-09.md`).
- Keep only the latest instruction in the working directory for reference; the canonical copy lives in Drive.

## Reliability & Monitoring (versioned 2026-02-10)
- Monitor all automation jobs (cron, background loops, scripts). If any job fails, hangs, or skips a scheduled run, notify the user immediately with a concise status note and remediation plan.
- “No news” is not acceptable when a job misfires: log the failure details, surface them proactively, and track resolution until the job resumes normal operation.
- Maintain health logs (`logs/research_monitor.log`, others as added) and review them daily; treat repeated errors as incidents requiring escalation.