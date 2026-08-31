#!/usr/bin/env python3
"""Produce a human-readable status report of the PSN documentation crawl.

Usage:
    python scripts/report_crawl_status.py [output_dir]
"""
import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent.parent / "output" / "psn_12"
LINKS_JSON = Path(__file__).resolve().parent.parent / "spike_output" / "psn_12_links.json"


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"


def url_to_relative_path(url: str) -> str:
    parsed = urlparse(url)
    path_str = parsed.path[1:] if parsed.path.startswith("/") else parsed.path
    parts = path_str.split("/")
    if len(parts) >= 2 and parts[0] == "resources" and parts[1] == "documents":
        parts = parts[2:]
    if not parts:
        return "index.md"
    if parts[-1].startswith("__"):
        parts[-1] = "index.md"
    else:
        name = parts[-1].rsplit(".", 1)[0] if "." in parts[-1] else parts[-1]
        parts[-1] = f"{name}.md"
    return "/".join(parts)


def safe_print(message: str) -> None:
    """Print a message, replacing characters the terminal cannot encode."""
    try:
        print(message)
    except UnicodeEncodeError:
        print(message.encode(sys.stdout.encoding or "utf-8", errors="replace").decode(sys.stdout.encoding or "utf-8"))


def build_report(root: Path, links_json: Path) -> str:
    index = json.loads((root / "_index.json").read_text(encoding="utf-8")) if (root / "_index.json").exists() else []
    links = json.loads(links_json.read_text(encoding="utf-8")) if links_json.exists() else []

    # Map TOC URLs to expected index.md paths.
    expected_paths = {url_to_relative_path(link["url"]): link for link in links}
    crawled_paths = {entry["path"]: entry for entry in index if entry.get("path")}

    # Group covered entries by top-level section.
    sections: dict[str, list[dict]] = defaultdict(list)
    for entry in index:
        path = entry.get("path", "")
        parts = path.split("/")
        if len(parts) >= 3 and parts[0] in ("SDK", "WebAPI"):
            section = "/".join(parts[:3])
            sections[section].append(entry)

    lines = []
    lines.append("# PSN Documentation Crawl Status Report")
    lines.append("")
    lines.append(f"- **Report date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"- **Total TOC entries:** {len(links)}")
    lines.append(f"- **Crawled markdown files:** {len(crawled_paths)}")
    lines.append(f"- **Top-level sections covered:** {len(sections)}")
    lines.append("")

    lines.append("## Coverage by Top-Level Section")
    lines.append("")
    sdk_sections = [s for s in sections if s.startswith("SDK/")]
    webapi_sections = [s for s in sections if s.startswith("WebAPI/")]

    for section in sorted(sdk_sections) + sorted(webapi_sections):
        entries = sections[section]
        lines.append(f"### {section}")
        lines.append(f"- Pages: {len(entries)}")
        toc_path = f"{section}/index.md"
        title = expected_paths.get(toc_path, {}).get("text", "Unknown")
        lines.append(f"- TOC title: {title}")
        lines.append("")

    lines.append("## Remaining Gaps (uncrawled TOC entries)")
    lines.append("")
    missing = []
    for link in links:
        expected = url_to_relative_path(link["url"])
        if expected not in crawled_paths:
            missing.append(link)
    if not missing:
        lines.append("All TOC entries are represented in the crawl.")
    else:
        lines.append(f"**{len(missing)} TOC entries not yet crawled:**")
        lines.append("")
        for link in missing:
            lines.append(f"- [{link['text']}]({link['url']}) -> `{url_to_relative_path(link['url'])}`")
    lines.append("")

    lines.append("## Duplicate Path Warnings")
    lines.append("")
    dupes = defaultdict(list)
    for entry in index:
        if entry.get("url"):
            dupes[entry.get("path")].append(entry.get("url"))
    shown = False
    for path, urls in sorted(dupes.items()):
        if len(urls) > 1:
            shown = True
            lines.append(f"- `{path}`: {len(urls)} URLs")
            for u in urls:
                lines.append(f"  - {u}")
    if not shown:
        lines.append("No duplicate paths detected.")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
    report = build_report(root, LINKS_JSON)
    out_path = root / "_crawl_status.md"
    out_path.write_text(report, encoding="utf-8")
    safe_print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
