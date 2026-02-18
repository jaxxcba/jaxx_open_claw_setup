#!/usr/bin/env python3
"""Validate Phase 1 investment documentation lock constraints."""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
active_dir = REPO / "investments" / "guides" / "active"
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

if errors:
    print("Phase 1 check FAILED")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("Phase 1 check PASSED")
print("- active guide lock is valid")
print("- operations runtime-only guardrails are valid")
