#!/usr/bin/env python3
"""Verify the integrity of crawled markdown content.

Usage:
    python scripts/verify_crawled_content.py [output_dir]
"""
import json
import re
import statistics
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent / "output" / "psn_12"
TITLE_RE = re.compile(r"^#\s+(.+)$")
SOURCE_RE = re.compile(r"^Source:\s*(https?://.+)$")
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")


class Issue:
    def __init__(self, path: str, category: str, message: str, severity: str = "warning"):
        self.path = path
        self.category = category
        self.message = message
        self.severity = severity  # error | warning | info


def check_file(md_path: Path, rel: str) -> list[Issue]:
    issues = []
    try:
        text = md_path.read_text(encoding="utf-8")
    except Exception as exc:
        return [Issue(rel, "read_error", str(exc), "error")]

    if not text.strip():
        return [Issue(rel, "empty", "File is empty", "error")]

    lines = text.splitlines()

    # Title check.
    title_match = TITLE_RE.match(lines[0]) if lines else None
    if not title_match or not title_match.group(1).strip():
        issues.append(Issue(rel, "missing_title", "First line is not a non-empty H1 title", "error"))

    # Source URL check.
    source_match = None
    for line in lines[1:10]:
        source_match = SOURCE_RE.match(line)
        if source_match:
            break
    if not source_match:
        issues.append(Issue(rel, "missing_source", "No 'Source: <url>' line near top of file", "error"))

    # Navigation-only stub detection.
    body = "\n".join(lines[2:]).strip() if len(lines) > 2 else ""
    body_no_links = LINK_RE.sub(r"\1", body)
    visible_text = re.sub(r"\s+", " ", body_no_links).strip()
    if len(visible_text) < 200:
        issues.append(Issue(rel, "stub", f"Body is only {len(visible_text)} visible chars (likely TOC stub)", "info"))

    return issues


def find_duplicates(index: list[dict]) -> list[Issue]:
    issues = []
    seen_paths: dict[str, list[str]] = {}
    for entry in index:
        path = entry.get("path")
        url = entry.get("url")
        if not path or not url:
            continue
        seen_paths.setdefault(path, []).append(url)

    for path, urls in seen_paths.items():
        if len(urls) > 1:
            issues.append(Issue(path, "duplicate_path", f"{len(urls)} URLs map to this path: {urls}", "warning"))
    return issues


def size_outliers(md_files: list[Path]) -> list[Issue]:
    issues = []
    sizes = [f.stat().st_size for f in md_files if f.exists()]
    if len(sizes) < 4:
        return issues
    qs = statistics.quantiles(sizes, n=4)
    q1 = qs[0]
    q3 = qs[2]
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    for f in md_files:
        s = f.stat().st_size
        rel = f.relative_to(ROOT).as_posix()
        if s < lower:
            issues.append(Issue(rel, "size_outlier", f"Size {s}B is far below lower IQR bound {lower:.0f}B", "warning"))
        elif s > upper:
            issues.append(Issue(rel, "size_outlier", f"Size {s}B is far above upper IQR bound {upper:.0f}B", "warning"))
    return issues


def verify(root: Path) -> dict:
    root.mkdir(parents=True, exist_ok=True)
    index_path = root / "_index.json"
    index = json.loads(index_path.read_text(encoding="utf-8")) if index_path.exists() else []
    # Only verify files in the merged tree, not legacy batch dirs or metadata files.
    md_files = sorted(
        f for f in root.rglob("*.md")
        if f.relative_to(root).parts
        and not f.relative_to(root).parts[0].startswith("batch_")
        and not f.name.startswith("_")
    )

    all_issues: list[Issue] = []
    for md in md_files:
        rel = md.relative_to(root).as_posix()
        all_issues.extend(check_file(md, rel))

    all_issues.extend(find_duplicates(index))
    all_issues.extend(size_outliers(md_files))

    counts = {"error": 0, "warning": 0, "info": 0}
    for issue in all_issues:
        counts[issue.severity] += 1

    report = {
        "total_files": len(md_files),
        "total_index_entries": len(index),
        "issues": [
            {"path": i.path, "category": i.category, "message": i.message, "severity": i.severity}
            for i in all_issues
        ],
        "counts": counts,
    }
    report_path = root / "_verification_report.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Verified {report['total_files']} files against {report['total_index_entries']} index entries.")
    print(f"Errors: {counts['error']}  Warnings: {counts['warning']}  Info: {counts['info']}")
    print(f"Report: {report_path}")
    return report


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
    report = verify(root)
    return 1 if report["counts"]["error"] > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
