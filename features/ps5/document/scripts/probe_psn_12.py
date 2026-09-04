#!/usr/bin/env python3
"""Probe the SDK/12.000 PlayStation Network landing page structure."""

import sys
from pathlib import Path
from urllib.parse import urljoin

from playwright.sync_api import sync_playwright


def main() -> int:
    url = "https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayStation_Network/PlayStation_Network_Landing.html"
    storage_path = Path(__file__).resolve().parent.parent / "spike_output" / "storage_state.json"
    out_dir = Path(__file__).resolve().parent.parent / "spike_output"

    if not storage_path.exists():
        print(f"ERROR: Storage state not found at {storage_path}", file=sys.stderr)
        return 1

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.new_page()

        print(f"Navigating to {url} ...")
        page.goto(url, timeout=60000)
        page.wait_for_timeout(3000)

        print(f"Page title: {page.title()}")
        print(f"Current URL: {page.url}")

        # Save probe HTML
        out_dir.mkdir(exist_ok=True)
        (out_dir / "psn_12_landing.html").write_text(page.content(), encoding="utf-8")
        page.screenshot(path=str(out_dir / "psn_12_landing.png"), full_page=True)

        # Extract local nav links
        links = page.eval_on_selector_all(
            "#local_nav a[href]",
            "elements => elements.map(a => ({text: a.innerText.trim(), href: a.href}))",
        )

        # Filter to SDK/12.000/PlayStation_Network scope and dedupe.
        seen = set()
        filtered = []
        for link in links:
            href = link.get("href", "")
            text = link.get("text", "")
            if href and href not in seen and "SDK/12.000" in href:
                seen.add(href)
                filtered.append({"text": text, "url": href})

        print(f"Found {len(filtered)} unique SDK/12.000 links under local nav:")
        for link in filtered[:30]:
            print(f"  - {link['text'][:60]:<60}  {link['url']}")

        browser.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
