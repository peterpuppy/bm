#!/usr/bin/env python3
"""Extract the full hierarchical catalog of SDK/12.000 docs from #local_nav.

Reads the saved landing page (whose sidebar contains the whole SDK/12.000 directory
index) and writes spike_output/sdk_12_catalog.json.  The catalog preserves the
category hierarchy so later AI retrieval / human browsing can see which section
lives under which top-level category.
"""

import json
import sys
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup


def safe_print(message: str) -> None:
    """Print a message, replacing characters the terminal cannot encode."""
    try:
        print(message)
    except UnicodeEncodeError:
        print(message.encode(sys.stdout.encoding or "utf-8", errors="replace").decode(sys.stdout.encoding or "utf-8"))


LANDING_HTML = Path(__file__).resolve().parent.parent / "spike_output" / "psn_12_landing.html"
OUT_PATH = Path(__file__).resolve().parent.parent / "spike_output" / "sdk_12_catalog.json"
BASE_URL = "https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayStation_Network/PlayStation_Network_Landing.html"


def normalize_url(url: str) -> str:
    return url.split("#")[0]


def is_listed_doc(url: str) -> bool:
    """Accept both SDK and WebAPI docs — the SDK/12.000 sidebar references both."""
    return "/SDK/12.000/" in url or "/WebAPI/" in url


def heading_text(li) -> str:
    """Return the heading text of a sidebar <li> (the text before any nested <ul>)."""
    parts = []
    for child in li.children:
        if child.name and child.name != "ul":
            text = child.get_text(strip=True)
            if text:
                parts.append(text)
    return " ".join(parts)


def walk(node, path: list[str], leafs: list[dict]) -> None:
    """Recursively walk #local_nav <ul>/<li> tree and collect SDK/12.000 leaves.

    Collects only DIRECT <a> children of each <li> (recursive=False) so a leaf
    is recorded at its true depth — the parent <li>'s recursive find_all would
    otherwise pre-flatten the whole subtree into the parent's category_path.
    """
    for child in node.children:
        if child.name == "li":
            h = heading_text(child)
            cur_path = path + [h] if h else path

            # Collect only direct anchors (the li's own link), not descendants.
            for a in child.find_all("a", href=True, recursive=False):
                full = normalize_url(urljoin(BASE_URL, a["href"]))
                if is_listed_doc(full) and full.endswith(".html"):
                    leafs.append({
                        "category_path": list(cur_path),
                        "title": a.get_text(strip=True),
                        "url": full,
                    })

            # Descend into direct child <ul> only.
            nested = child.find("ul", recursive=False)
            if nested:
                walk(nested, cur_path, leafs)
        elif child.name == "ul":
            walk(child, path, leafs)


def dedupe(leafs: list[dict]) -> list[dict]:
    """Keep one entry per URL, preferring the DEEPEST category path.

    The sidebar can list the same page under multiple headings; the deepest
    path is the most specific grouping and is what we mirror locally.
    """
    best: dict[str, dict] = {}
    for item in leafs:
        url = item["url"]
        cur = best.get(url)
        if cur is None or len(item["category_path"]) > len(cur["category_path"]):
            best[url] = item
    return sorted(best.values(), key=lambda x: x["url"])


def main() -> int:
    if not LANDING_HTML.exists():
        print(f"ERROR: {LANDING_HTML} not found", file=sys.stderr)
        return 1

    html = LANDING_HTML.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    nav = soup.find(id="local_nav")
    if not nav:
        print("ERROR: #local_nav not found", file=sys.stderr)
        return 1

    pane = nav.find("div", class_="jspPane")
    if not pane:
        print("ERROR: .jspPane not found inside #local_nav", file=sys.stderr)
        return 1

    leafs: list[dict] = []
    walk(pane, [], leafs)
    unique_leafs = dedupe(leafs)

    catalog = {
        "source": str(LANDING_HTML),
        "base_page": BASE_URL,
        "total_unique_leafs": len(unique_leafs),
        "leafs": unique_leafs,
    }

    OUT_PATH.write_text(json.dumps(catalog, indent=2, ensure_ascii=False), encoding="utf-8")
    safe_print(f"Extracted {len(unique_leafs)} unique SDK/12.000 leaf links -> {OUT_PATH}")

    # Print top-level distribution.
    from collections import Counter
    top_counts = Counter(item["category_path"][0] if item["category_path"] else "Uncategorized" for item in unique_leafs)
    safe_print("\nTop-level categories:")
    for cat, count in sorted(top_counts.items(), key=lambda x: x[1], reverse=True):
        safe_print(f"  {cat}: {count}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
