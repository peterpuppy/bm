#!/usr/bin/env python3
"""Probe the left navigation of the saved PS5 docs HTML."""

import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup


def main() -> int:
    html_path = Path(__file__).resolve().parent.parent / "spike_output" / "spike_page.html"
    base_url = "https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_WebAPI-Overview/__toc.html"

    html = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    # Try a few common selectors for the left navigation.
    nav_selectors = [
        ("id", "local_nav"),
        ("class", "local_nav"),
        ("class", "toc"),
        ("class", "sidebar"),
        ("class", "navigation"),
        ("class", "nav"),
    ]

    for attr, value in nav_selectors:
        if attr == "id":
            container = soup.find(id=value)
        else:
            container = soup.find(class_=value)
        if container:
            print(f"Found nav container by {attr}='{value}'")
            links = container.find_all("a", href=True)
            print(f"  {len(links)} link(s) found:")
            for a in links[:30]:
                href = urljoin(base_url, a["href"])
                text = a.get_text(strip=True).encode("utf-8", errors="ignore").decode("utf-8")
                print(f"    - {text[:60]:<60}  {href}")
            return 0

    # Fallback: print all internal links.
    print("No obvious nav container found. Listing all internal links:")
    seen = set()
    for a in soup.find_all("a", href=True):
        href = urljoin(base_url, a["href"])
        if urlparse(href).netloc == urlparse(base_url).netloc and href not in seen:
            seen.add(href)
            text = a.get_text(strip=True)
            print(f"  - {text[:60]:<60}  {href}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
