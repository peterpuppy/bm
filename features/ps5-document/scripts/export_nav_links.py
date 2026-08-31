#!/usr/bin/env python3
"""Export the left navigation links from the saved PS5 docs page to a JSON file."""

import json
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup


def main() -> int:
    html_path = Path(__file__).resolve().parent.parent / "spike_output" / "spike_page.html"
    out_path = Path(__file__).resolve().parent.parent / "spike_output" / "local_nav_links.json"
    base_url = "https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_WebAPI-Overview/__toc.html"

    html = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    container = soup.find(id="local_nav")
    if not container:
        print("ERROR: Could not find #local_nav", file=sys.stderr)
        return 1

    links = []
    seen = set()
    for a in container.find_all("a", href=True):
        href = urljoin(base_url, a["href"])
        text = a.get_text(strip=True)
        if not text or href in seen:
            continue
        seen.add(href)
        links.append({"text": text, "url": href})

    out_path.write_text(json.dumps(links, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Exported {len(links)} unique links to: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
