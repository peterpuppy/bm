#!/usr/bin/env python3
"""Generate human-readable catalog docs from sdk_12_catalog.json.

Produces:
    docs/sdk_12_catalog.md        — full hierarchical catalog
    docs/sdk_12_sandbox_analysis.md — sandbox-related sections
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
DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"

SANDBOX_KEYWORDS = [
    "sandbox",
    "devadmin",
    "development account",
    "development accounts",
    "test account",
    "test accounts",
    "sandbox network",
    "np id",
    "account management",
]


def url_to_relative_path(url: str) -> str:
    # Delegate to shared mapper so catalog docs show the real (PSN-grouped) local paths.
    return path_mapping.url_to_relative_path(url).as_posix()


def matches_sandbox(item: dict) -> bool:
    text = f"{item.get('title', '')} {' '.join(item.get('category_path', []))} {item.get('url', '')}".lower()
    return any(kw.lower() in text for kw in SANDBOX_KEYWORDS)


def build_catalog_md(catalog: dict) -> str:
    leafs = catalog["leafs"]

    # Group by full category path.
    tree: dict = {}
    for item in leafs:
        path = item.get("category_path") or ["Uncategorized"]
        node = tree
        for part in path:
            node = node.setdefault(part, {})
        node.setdefault("__leafs__", []).append(item)

    lines = []
    lines.append("# PS5 SDK 12.000 Documentation Catalog")
    lines.append("")
    lines.append(f"- **Source:** `{catalog['source']}`")
    lines.append(f"- **Base page:** {catalog['base_page']}")
    lines.append(f"- **Total leaf links:** {len(leafs)}")
    lines.append("")
    lines.append("This catalog maps every SDK/12.000 documentation section to its source URL and expected local Markdown path.")
    lines.append("")

    def emit(node, depth=0):
        for key in sorted(node.keys()):
            if key == "__leafs__":
                continue
            lines.append(f"{'#' * (depth + 2)} {key}")
            lines.append("")
            if "__leafs__" in node[key]:
                for leaf in sorted(node[key]["__leafs__"], key=lambda x: x["title"]):
                    rel = url_to_relative_path(leaf["url"])
                    title = leaf["title"].replace("|", "\\|")
                    lines.append(f"- [{title}]({leaf['url']}) → `output/psn_12/{rel}`")
                lines.append("")
            emit(node[key], depth + 1)

    emit(tree)
    return "\n".join(lines)


def build_sandbox_md(catalog: dict) -> str:
    matches = [item for item in catalog["leafs"] if matches_sandbox(item)]

    lines = []
    lines.append("# SDK 12.000 Sandbox-Related Documentation Analysis")
    lines.append("")
    lines.append(f"- **Total SDK/12.000 leaf links:** {len(catalog['leafs'])}")
    lines.append(f"- **Sandbox-related matches:** {len(matches)}")
    lines.append("")
    lines.append("## Keywords used")
    lines.append("")
    for kw in SANDBOX_KEYWORDS:
        lines.append(f"- `{kw}`")
    lines.append("")
    lines.append("## Matched sections")
    lines.append("")

    if not matches:
        lines.append("No sandbox-related sections found.")
    else:
        for item in sorted(matches, key=lambda x: x["url"]):
            rel = url_to_relative_path(item["url"])
            cat = " > ".join(item.get("category_path", []))
            title = item["title"].replace("|", "\\|")
            lines.append(f"### {title}")
            lines.append(f"- **Category path:** {cat}")
            lines.append(f"- **URL:** {item['url']}")
            lines.append(f"- **Expected local path:** `output/psn_12/{rel}`")
            lines.append("")

    return "\n".join(lines)


def main() -> int:
    if not CATALOG_JSON.exists():
        print(f"ERROR: {CATALOG_JSON} not found. Run scripts/extract_sdk_12_catalog.py first.", file=sys.stderr)
        return 1

    catalog = json.loads(CATALOG_JSON.read_text(encoding="utf-8"))
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    catalog_md = build_catalog_md(catalog)
    (DOCS_DIR / "sdk_12_catalog.md").write_text(catalog_md, encoding="utf-8")
    print(f"Wrote docs/sdk_12_catalog.md ({len(catalog['leafs'])} entries)")

    sandbox_md = build_sandbox_md(catalog)
    (DOCS_DIR / "sdk_12_sandbox_analysis.md").write_text(sandbox_md, encoding="utf-8")
    print(f"Wrote docs/sdk_12_sandbox_analysis.md ({sum(1 for x in catalog['leafs'] if matches_sandbox(x))} matches)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
