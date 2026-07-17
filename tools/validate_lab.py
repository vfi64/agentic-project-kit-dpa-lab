#!/usr/bin/env python3
"""Deterministic repository gates for the DPA architecture lab."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "README.md",
    "LAB_BOOTSTRAP.md",
    "MAIN_REPOSITORY_CONTEXT.md",
    "LAB_EXECUTION_CONTRACT.md",
    "GOVERNANCE.md",
    "STATUS.md",
    "ROADMAP.md",
    "DECISIONS.md",
    "ASSUMPTIONS.md",
    "specs/dpa/README.md",
    "integration/MAIN_REPO_VALIDATION_CHECKLIST.md",
    "integration/IMPORT_PLAN.md",
)

FORBIDDEN_WORKFLOW_MARKERS = (
    "one-shot",
    "adjudication-sync",
)

STATUS_RE = re.compile(r"^Status:\s*(\S(?:.*\S)?)\s*$", re.MULTILINE)
MAP_ROW_RE = re.compile(
    r"^\|\s*(DPA-\d{3})\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|\s*$",
    re.MULTILINE,
)
CONFLICT_RE = re.compile(r"^(<<<<<<<|=======|>>>>>>>)", re.MULTILINE)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def read_text(path: Path, errors: list[str]) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        fail(errors, f"non-UTF-8 text file: {path.relative_to(ROOT)}")
    except OSError as exc:
        fail(errors, f"cannot read {path.relative_to(ROOT)}: {exc}")
    return None


def check_required(errors: list[str]) -> None:
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            fail(errors, f"missing required file: {relative}")


def check_forbidden_runtime_state(errors: list[str]) -> None:
    if (ROOT / ".agentic").exists():
        fail(errors, "forbidden live .agentic state exists in the architecture lab")


def check_workflows(errors: list[str]) -> None:
    workflow_dir = ROOT / ".github" / "workflows"
    if not workflow_dir.exists():
        fail(errors, "missing .github/workflows directory")
        return
    workflows = sorted(workflow_dir.glob("*.y*ml"))
    if not workflows:
        fail(errors, "no durable GitHub Actions workflow exists")
        return
    for path in workflows:
        lower_name = path.name.lower()
        text = read_text(path, errors)
        if any(marker in lower_name for marker in FORBIDDEN_WORKFLOW_MARKERS):
            fail(errors, f"temporary or self-mutating workflow remains: {path.relative_to(ROOT)}")
        if text is not None and "contents: write" in text:
            fail(errors, f"workflow must be read-only: {path.relative_to(ROOT)}")


def check_text_integrity(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".mmd", ".yml", ".yaml", ".json", ".py"}:
            continue
        text = read_text(path, errors)
        if text is None:
            continue
        if CONFLICT_RE.search(text):
            fail(errors, f"merge-conflict marker in {path.relative_to(ROOT)}")
        if text and not text.endswith("\n"):
            fail(errors, f"missing final newline: {path.relative_to(ROOT)}")


def check_canonical_dpa_map(errors: list[str]) -> None:
    map_path = ROOT / "specs" / "dpa" / "README.md"
    text = read_text(map_path, errors)
    if text is None:
        return
    rows = MAP_ROW_RE.findall(text)
    expected_numbers = [f"DPA-{number:03d}" for number in range(0, 1000, 100)]
    found_numbers = [number for number, _, _ in rows]
    if found_numbers != expected_numbers:
        fail(errors, f"canonical DPA map must list exactly {', '.join(expected_numbers)} in order")
    seen_files: set[str] = set()
    for number, filename, mapped_status in rows:
        if filename in seen_files:
            fail(errors, f"duplicate canonical DPA file: {filename}")
        seen_files.add(filename)
        path = ROOT / "specs" / "dpa" / filename
        if not path.is_file():
            fail(errors, f"canonical map target missing: specs/dpa/{filename}")
            continue
        spec = read_text(path, errors)
        if spec is None:
            continue
        first_line = spec.splitlines()[0] if spec.splitlines() else ""
        if not first_line.startswith(f"# {number}"):
            fail(errors, f"canonical heading mismatch in specs/dpa/{filename}")
        match = STATUS_RE.search(spec)
        if not match:
            fail(errors, f"missing Status field in specs/dpa/{filename}")
            continue
        actual_status = match.group(1).strip().lower()
        if actual_status != mapped_status.strip().lower():
            fail(
                errors,
                f"status drift for {number}: map={mapped_status.strip()!r}, file={match.group(1).strip()!r}",
            )


def main() -> int:
    errors: list[str] = []
    check_required(errors)
    check_forbidden_runtime_state(errors)
    check_workflows(errors)
    check_text_integrity(errors)
    check_canonical_dpa_map(errors)
    if errors:
        print("DPA lab gates: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("DPA lab gates: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
