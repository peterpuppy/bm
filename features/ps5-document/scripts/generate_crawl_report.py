#!/usr/bin/env python3
"""Generate a crawl coverage report for the full SDK/12.000 catalog.

Reads the catalog produced by extract_sdk_12_catalog.py and the master index,
then writes docs/sdk_12_crawl_report.md with:
  - overall coverage percentage
  - per top-level category summary
  - per-section status, file count, and a short synopsis
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

# ponytail: scripts/ is on sys.path when run as a module; add fallback for direct execution.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import path_mapping


CATALOG_JSON = Path(__file__).resolve().parent.parent / "spike_output" / "sdk_12_catalog.json"
INDEX_JSON = Path(__file__).resolve().parent.parent / "output" / "psn_12" / "_index.json"
OUT_MD = Path(__file__).resolve().parent.parent / "docs" / "sdk_12_crawl_report.md"
OUTPUT_ROOT = Path(__file__).resolve().parent.parent / "output" / "psn_12"


def safe_print(message: str) -> None:
    try:
        print(message)
    except UnicodeEncodeError:
        print(message.encode(sys.stdout.encoding or "utf-8", errors="replace").decode(sys.stdout.encoding or "utf-8"))


def url_to_relative_dir(url: str) -> str | None:
    """Map a documentation URL to the output subdirectory that would hold it."""
    # Delegate to the shared path mapper so PSN SDK sections route into
    # PlayStation_Network/ — same logic the crawler uses to write files.
    rel = path_mapping.url_to_relative_path(url)
    rel_dir = rel.parent.as_posix()
    return rel_dir or None


def is_crawled(url: str, crawled_dirs: set[str]) -> bool:
    rel_dir = url_to_relative_dir(url)
    return rel_dir in crawled_dirs


def section_dir(url: str) -> Path | None:
    rel_dir = url_to_relative_dir(url)
    if not rel_dir:
        return None
    return OUTPUT_ROOT / rel_dir.replace("/", "\\")


def count_files(section_path: Path) -> int:
    if not section_path.exists():
        return 0
    return sum(1 for f in section_path.iterdir() if f.is_file() and f.suffix == ".md")


def _first_real_paragraph(text: str) -> str | None:
    """Return the first non-empty, non-TOC paragraph from markdown text."""
    lines = text.splitlines()
    body_lines = []
    in_header = True
    for line in lines:
        stripped = line.strip()
        if in_header:
            if stripped.startswith("#") or stripped.startswith("Source:") or not stripped:
                continue
            in_header = False
        if not stripped:
            if body_lines:
                break
            continue
        # Skip TOC-like lines (numbered lists or bare markdown links).
        if re.match(r"^\d+\.\s+\[", stripped) or re.match(r"^\*\s+\[", stripped):
            if not body_lines:
                continue
            break
        body_lines.append(stripped)
    if body_lines:
        synopsis = " ".join(body_lines)
        synopsis = re.sub(r"\s+", " ", synopsis)
        if len(synopsis) > 280:
            synopsis = synopsis[:277] + "..."
        return synopsis
    return None


def extract_synopsis(section_path: Path) -> str:
    """Pull a short synopsis from the section's best available content page."""
    if not section_path.exists():
        return "Not crawled."

    # 1. Prefer a dedicated overview page if present.
    candidates = sorted(section_path.glob("overview*.md"))
    # 2. Otherwise use the first non-index content page.
    if not candidates:
        candidates = sorted(
            f for f in section_path.iterdir()
            if f.is_file() and f.suffix == ".md" and f.name != "index.md"
        )
    # 3. Fall back to the TOC/index page.
    if not candidates:
        candidates = [section_path / "index.md"]

    for cand in candidates:
        if not cand.exists():
            continue
        try:
            text = cand.read_text(encoding="utf-8")
        except Exception:
            continue
        synopsis = _first_real_paragraph(text)
        if synopsis:
            return synopsis

    return "No synopsis available."


def main() -> int:
    if not CATALOG_JSON.exists():
        safe_print(f"ERROR: {CATALOG_JSON} not found")
        return 1
    if not INDEX_JSON.exists():
        safe_print(f"ERROR: {INDEX_JSON} not found")
        return 1

    catalog = json.loads(CATALOG_JSON.read_text(encoding="utf-8"))
    index = json.loads(INDEX_JSON.read_text(encoding="utf-8"))

    # Build set of directories that actually exist in the output tree.
    # _index.json stores Windows backslash paths; normalize to forward slashes.
    crawled_dirs: set[str] = set()
    for entry in index:
        path = entry.get("path", "").replace("\\", "/")
        if not path:
            continue
        # path is like "SDK/12.000/NpAuth-Overview/index.md"
        dir_part = "/".join(path.split("/")[:-1])
        if dir_part:
            crawled_dirs.add(dir_part)

    # Group leafs by top-level category.
    tree: dict[str, list[dict]] = defaultdict(list)
    for item in catalog["leafs"]:
        top = item.get("category_path", ["Uncategorized"])[0]
        tree[top].append(item)

    total_leafs = len(catalog["leafs"])
    crawled_leafs = sum(1 for item in catalog["leafs"] if is_crawled(item["url"], crawled_dirs))
    overall_pct = (crawled_leafs / total_leafs * 100) if total_leafs else 0.0

    lines = []
    lines.append("# PS5 SDK 12.000 Documentation Crawl Report")
    lines.append("")
    lines.append(f"- **Source catalog:** `{CATALOG_JSON}`")
    lines.append(f"- **Master index:** `{INDEX_JSON}`")
    lines.append(f"- **Total catalog entries:** {total_leafs}")
    lines.append(f"- **Crawled entries:** {crawled_leafs}")
    lines.append(f"- **Coverage:** {overall_pct:.1f}%")
    lines.append("")
    lines.append("This report lists every section from the SDK/12.000 sidebar, marks whether it has been crawled, and includes a short synopsis for each section that has been downloaded.")
    lines.append("")

    # Summary table by top-level category.
    lines.append("## Coverage by Category")
    lines.append("")
    lines.append("| Category | Entries | Crawled | Coverage |")
    lines.append("|---|---:|---:|---:|")
    for cat in sorted(tree.keys()):
        items = tree[cat]
        cat_crawled = sum(1 for item in items if is_crawled(item["url"], crawled_dirs))
        cat_pct = (cat_crawled / len(items) * 100) if items else 0.0
        safe_cat = cat.replace("|", "\\|")
        lines.append(f"| {safe_cat} | {len(items)} | {cat_crawled} | {cat_pct:.1f}% |")
    lines.append("")

    # Detailed section lists per category.
    for cat in sorted(tree.keys()):
        safe_heading = cat.replace("?", "")
        lines.append(f"## {safe_heading}")
        lines.append("")

        for item in sorted(tree[cat], key=lambda x: x["title"]):
            title = item["title"].replace("|", "\\|")
            url = item["url"]
            rel_dir = url_to_relative_dir(url) or ""
            local_path = f"output/psn_12/{rel_dir}/index.md" if rel_dir else ""
            status = "✅ Crawled" if is_crawled(url, crawled_dirs) else "⬜ Not crawled"

            if is_crawled(url, crawled_dirs):
                sec_path = section_dir(url)
                file_count = count_files(sec_path) if sec_path else 0
                synopsis = extract_synopsis(sec_path) if sec_path else ""
                lines.append(f"### {title} — {status} ({file_count} files)")
                lines.append("")
                lines.append(f"- **URL:** {url}")
                lines.append(f"- **Local:** `{local_path}`")
                lines.append(f"- **Synopsis:** {synopsis}")
            else:
                lines.append(f"### {title} — {status}")
                lines.append("")
                lines.append(f"- **URL:** {url}")
                if local_path:
                    lines.append(f"- **Expected local:** `{local_path}`")
            lines.append("")

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    safe_print(f"Wrote {OUT_MD} ({crawled_leafs}/{total_leafs} = {overall_pct:.1f}% coverage)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
