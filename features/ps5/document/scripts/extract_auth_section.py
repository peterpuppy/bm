#!/usr/bin/env python3
"""Extract the 'Authentication and Authorization' section from local_nav."""

import json
import sys
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup


def main() -> int:
    html_path = Path(__file__).resolve().parent.parent / "spike_output" / "psn_12_landing.html"
    out_path = Path(__file__).resolve().parent.parent / "spike_output" / "auth_section_links.json"
    base_url = "https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayStation_Network/PlayStation_Network_Landing.html"

    html = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    nav = soup.find(id="local_nav")
    if not nav:
        print("ERROR: #local_nav not found", file=sys.stderr)
        return 1

    # Walk the local_nav DOM looking for the "Authentication and Authorization" heading/list.
    items = []
    in_section = False
    section_level = None

    # Heuristic: traverse all list items; when we see the section heading, start collecting until next same-level heading.
    for elem in nav.find_all(["li", "a"]):
        text = elem.get_text(strip=True)
        if not text:
            continue

        if elem.name == "li" and "Authentication and Authorization" in text:
            in_section = True
            section_level = elem.find_parent("ul")
            continue

        if in_section:
            # Stop if we hit another top-level section heading (li with direct ul sibling or parent change).
            a = elem.find("a", href=True) if elem.name == "li" else elem if elem.name == "a" else None
            if a:
                href = urljoin(base_url, a["href"])
                items.append({"text": a.get_text(strip=True), "url": href})

    # Simple filter: links that look auth-related under WebAPI/latest Auth_for_Websites / Auth_for_Websites-Reference.
    auth_links = [item for item in items if "Auth" in item["url"] or "auth" in item["url"].lower()]

    out_path.write_text(json.dumps(auth_links, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Found {len(auth_links)} auth-related links under the section.")
    print(f"Saved to: {out_path}")
    for link in auth_links:
        print(f"  - {link['text']:<50} {link['url']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
