#!/usr/bin/env python3
"""Extract all SDK/12.000 PlayStation Network doc links from the landing page nav.

Saves a JSON list of {text, url} entries for every leaf/landing page under the
PlayStation Network section, excluding the PlayStation(R)4 Cross-Generation SDK
supplement section.
"""

import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup


LANDING_HTML = Path(__file__).resolve().parent.parent / "spike_output" / "psn_12_landing.html"
OUT_PATH = Path(__file__).resolve().parent.parent / "spike_output" / "psn_12_links.json"
BASE_URL = "https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayStation_Network/PlayStation_Network_Landing.html"


def normalize_url(url: str) -> str:
    return url.split("#")[0]


def main() -> int:
    html = LANDING_HTML.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    nav = soup.find(id="local_nav")
    if not nav:
        print("ERROR: #local_nav not found", file=sys.stderr)
        return 1

    # Find the top-level PlayStation Network li in the nav.
    psn_li = None
    for li in nav.find_all("li"):
        span = li.find("span")
        if span and "PlayStation" in span.get_text() and "Network" in span.get_text():
            # Make sure it's a top-level section (direct child of nav's root ul).
            if li.find_parent("ul") is nav.find("ul"):
                psn_li = li
                break

    if not psn_li:
        print("ERROR: PlayStation Network section not found", file=sys.stderr)
        return 1

    links = []
    seen = set()

    # Walk all anchors inside the PlayStation Network section.
    for a in psn_li.find_all("a", href=True):
        text = a.get_text(strip=True)
        href = normalize_url(urljoin(BASE_URL, a["href"]))

        # Skip external / non-doc links.
        if not href.startswith("https://game.develop.playstation.net/resources/documents/"):
            continue
        # Skip cross-generation supplement links.
        if "Cross-Generation" in text or "Cross-Generation" in href:
            continue
        # Skip SDK version switchers or purely navigational anchors.
        if href in seen:
            continue
        seen.add(href)
        links.append({"text": text, "url": href})

    OUT_PATH.write_text(json.dumps(links, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Extracted {len(links)} PlayStation Network links -> {OUT_PATH}")
    for link in links:
        print(f"  - {link['text'].encode('utf-8', errors='replace').decode('utf-8'):<60} {link['url']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
