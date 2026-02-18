#!/usr/bin/env python3
"""Check repository documentation for stale backtick path references.

This checker complements markdown link validation by validating common
root-relative path references written in backticks.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
from typing import Iterable

__version__ = "1.0.0"
__updated__ = "2026-02-18"
__owner__ = "Repository Governance"
__status__ = "active"

REFERENCES = [
    "governance_docs/conventions.md",
    "governance_docs/index.md",
]

EXCLUDED_DIRS = {".git", "archive", "history"}
PATH_PATTERN = re.compile(r"`([^`]+)`")

OPTIONAL_REFERENCE_PREFIXES = [
    "memory/",
    "../../operations/logs/audit_log.jsonl",
    "../../operations/logs/evidence_ledger.jsonl",
]


def is_optional_reference(token: str) -> bool:
    return any(token.startswith(prefix) for prefix in OPTIONAL_REFERENCE_PREFIXES)

def iter_markdown_files(root: pathlib.Path) -> Iterable[pathlib.Path]:
    for path in root.rglob("*.md"):
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        yield path


def looks_like_repo_path(token: str) -> bool:
    token = token.strip().rstrip(".,:;").strip("<>")
    if not token:
        return False
    if token.startswith(("http://", "https://", "mailto:", "#")):
        return False
    if "*" in token or "YYYY" in token:
        return False
    if token.startswith("<") or token.endswith(">"):
        return False
    if " " in token:
        return False
    if "->" in token or "|" in token:
        return False
    if token in {"README.md", "LICENSE"}:
        return True
    if token.endswith("/"):
        return True
    return "/" in token and "." in pathlib.Path(token).name


def exists_in_repo(root: pathlib.Path, ref: str, source: pathlib.Path) -> bool:
    token = ref.strip().rstrip(".,:;").strip("<>")
    if token.startswith("/"):
        token = token.lstrip("/")

    candidates = [
        root / token,
        source.parent / token,
    ]

    if token.endswith("/"):
        candidates.append(root / token.rstrip("/"))
        candidates.append(source.parent / token.rstrip("/"))

    return any(candidate.exists() for candidate in candidates)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate backtick path references.")
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root path (default: current directory).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return non-zero if stale references are found.",
    )
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    failures: list[str] = []

    for md_file in iter_markdown_files(root):
        content = md_file.read_text(encoding="utf-8", errors="ignore")
        for match in PATH_PATTERN.finditer(content):
            token = match.group(1)
            if not looks_like_repo_path(token):
                continue
            if is_optional_reference(token):
                continue
            if not exists_in_repo(root, token, md_file):
                failures.append(f"{md_file.relative_to(root)}: `{token}`")

    if failures:
        print("REFERENCE_DRIFT_FOUND")
        for failure in failures:
            print(f"- {failure}")
        return 1 if args.strict else 0

    print("REFERENCE_DRIFT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
