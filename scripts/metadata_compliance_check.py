#!/usr/bin/env python3
"""Validate metadata and references against governance_docs/metadata_policy.md."""

from __future__ import annotations

__version__ = "1.0.0"
__updated__ = "2026-02-18"

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "governance_docs" / "metadata_reference_classification_map.json"

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
STATUS_MD = {"Active", "Proposed", "Deprecated", "Archived"}
STATUS_JSON = {"active", "proposed", "deprecated", "archived"}


def load_map() -> dict:
    return json.loads(MAP_PATH.read_text(encoding="utf-8"))


def git_changed_files(changed_from: str) -> set[Path]:
    cmd = ["git", "diff", "--name-only", f"{changed_from}...HEAD"]
    out = subprocess.check_output(cmd, cwd=ROOT, text=True)
    return {ROOT / line.strip() for line in out.splitlines() if line.strip()}


def match_any(rel: str, globs: Iterable[str]) -> bool:
    p = Path(rel)
    return any(p.match(g) for g in globs)


def contains_top_field(text: str, field: str) -> bool:
    first_lines = "\n".join(text.splitlines()[:40])
    return f"{field}:" in first_lines


def check_md(path: Path, require_refs: bool) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    for field in ("Version", "Last Updated", "Status"):
        if not contains_top_field(text, field):
            errors.append(f"missing '{field}:' near top of file")

    status_line = next((ln for ln in text.splitlines()[:40] if ln.startswith("Status:")), None)
    if status_line:
        value = status_line.split(":", 1)[1].strip()
        if value not in STATUS_MD:
            errors.append(f"invalid markdown status '{value}'")

    updated_line = next((ln for ln in text.splitlines()[:40] if ln.startswith("Last Updated:")), None)
    if updated_line:
        value = updated_line.split(":", 1)[1].strip()
        if not DATE_RE.match(value):
            errors.append(f"invalid Last Updated date '{value}'")

    if require_refs and "\n## References" not in text:
        errors.append("missing '## References' section")

    return errors


def check_json(path: Path, require_refs: bool) -> list[str]:
    errors: list[str] = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"invalid json: {exc}"]

    required = ["schema_version", "document_version", "last_updated", "status", "source_refs"]
    for key in required:
        if key not in payload:
            errors.append(f"missing key '{key}'")

    if "status" in payload and payload["status"] not in STATUS_JSON:
        errors.append(f"invalid json status '{payload['status']}'")

    if "last_updated" in payload and not DATE_RE.match(str(payload["last_updated"])):
        errors.append(f"invalid last_updated date '{payload['last_updated']}'")

    if "source_refs" in payload and not isinstance(payload["source_refs"], list):
        errors.append("source_refs must be an array")

    if require_refs and isinstance(payload.get("source_refs"), list) and len(payload["source_refs"]) == 0:
        errors.append("source_refs must be non-empty for required-reference file")

    return errors


def check_py(path: Path, require_refs: bool) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines:
        return ["empty python file"]

    first_nonempty = next((ln.strip() for ln in lines if ln.strip() and not ln.startswith("#!") and not ln.strip().startswith("#")), "")
    if not (first_nonempty.startswith('"""') or first_nonempty.startswith("'''")):
        errors.append("missing module docstring at top of file")

    if "__version__" not in text:
        errors.append("missing __version__ constant")

    updated_match = re.search(r"^__updated__\s*=\s*['\"]([^'\"]+)['\"]", text, re.MULTILINE)
    if not updated_match:
        errors.append("missing __updated__ constant")
    elif not DATE_RE.match(updated_match.group(1)):
        errors.append(f"invalid __updated__ date '{updated_match.group(1)}'")

    if require_refs and not re.search(r"^REFERENCES\s*=\s*\[", text, re.MULTILINE):
        errors.append("missing REFERENCES constant for required-reference file")

    return errors


def iter_files(config: dict, changed: set[Path] | None) -> list[Path]:
    include_globs = set()
    for glist in config["metadata_required_globs"].values():
        include_globs.update(glist)
    include_globs.update(config["reference_required_globs"])
    include_globs.update(config["reference_optional_globs"])

    files: set[Path] = set()
    for pattern in include_globs:
        files.update(ROOT.glob(pattern))

    final = []
    for path in sorted(files):
        if not path.is_file():
            continue
        rel = str(path.relative_to(ROOT))
        if match_any(rel, config.get("exclude_globs", [])):
            continue
        if changed is not None and path not in changed:
            continue
        final.append(path)
    return final


def main() -> int:
    parser = argparse.ArgumentParser(description="Check metadata and references")
    parser.add_argument("--strict", action="store_true", help="exit non-zero on violations")
    parser.add_argument("--changed-from", help="only check files changed since this git ref")
    args = parser.parse_args()

    config = load_map()
    changed = git_changed_files(args.changed_from) if args.changed_from else None

    violations: list[tuple[str, str]] = []

    for path in iter_files(config, changed):
        rel = str(path.relative_to(ROOT))
        require_refs = match_any(rel, config["reference_required_globs"])

        if path.suffix == ".md":
            required_metadata = match_any(rel, config["metadata_required_globs"]["md"])
            errors = check_md(path, require_refs) if required_metadata or require_refs else []
        elif path.suffix == ".json":
            required_metadata = match_any(rel, config["metadata_required_globs"]["json"])
            errors = check_json(path, require_refs) if required_metadata or require_refs else []
        elif path.suffix == ".py":
            required_metadata = match_any(rel, config["metadata_required_globs"]["py"])
            errors = check_py(path, require_refs) if required_metadata or require_refs else []
        else:
            errors = []

        for err in errors:
            violations.append((rel, err))

    if violations:
        print("metadata/reference violations found:")
        for rel, err in violations:
            print(f"- {rel}: {err}")
    else:
        print("metadata/reference checks passed")

    if violations and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
