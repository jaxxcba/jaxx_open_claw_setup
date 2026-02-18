#!/usr/bin/env python3
"""Validate investment documentation lock constraints (Phase 1 + Phase 2)."""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
active_dir = REPO / "investments" / "guides" / "active"
archive_dir = REPO / "investments" / "guides" / "archive"
ops_dir = REPO / "investments" / "operations"

allowed_active = {
    "investment_methodology.md",
    "operator_quickstart.md",
    "research_sources_reference.json",
}

errors = []

if not active_dir.exists():
    errors.append(f"missing active directory: {active_dir}")
else:
    active_files = {p.name for p in active_dir.iterdir() if p.is_file()}
    extra = sorted(active_files - allowed_active)
    missing = sorted(allowed_active - active_files)
    if extra:
        errors.append(f"unexpected active files: {', '.join(extra)}")
    if missing:
        errors.append(f"missing required active files: {', '.join(missing)}")

for forbidden in ["openclaw_thesis_system_v3_3.md", "research_sources.json"]:
    if (ops_dir / forbidden).exists():
        errors.append(f"forbidden operations file present: investments/operations/{forbidden}")

required_ops_dirs = [
    ops_dir / "research_results",
    ops_dir / "logs",
    ops_dir / "logs" / "snapshots",
]
for req in required_ops_dirs:
    if not req.exists():
        errors.append(f"missing operations directory: {req.relative_to(REPO)}")

if not (archive_dir / "README.md").exists():
    errors.append("missing archive index: investments/guides/archive/README.md")

if archive_dir.exists():
    for p in archive_dir.iterdir():
        if not p.is_file():
            continue
        name = p.name
        if " (" in name and name.endswith(").md"):
            errors.append(f"lean-archive violation (duplicate style filename): investments/guides/archive/{name}")
        if name.startswith("research-summary-template") and "_v" not in name and name != "README.md":
            errors.append(f"lean-archive violation (unversioned template file): investments/guides/archive/{name}")

if errors:
    print("Investments documentation check FAILED")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("Investments documentation check PASSED")
print("- active guide lock is valid")
print("- operations runtime-only guardrails are valid")
print("- lean archive policy guardrails are valid")
