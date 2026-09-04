#!/usr/bin/env python3
"""Attach to the running Chrome debug port and save storage state."""

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def main() -> int:
    port = 9222
    storage_path = Path(__file__).resolve().parent.parent / "spike_output" / "storage_state.json"

    print(f"Connecting to Chrome on port {port}...")
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{port}")
        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.pages[0] if context.pages else context.new_page()

        print(f"Current URL: {page.url}")
        print(f"Page title: {page.title()}")

        storage_path.parent.mkdir(exist_ok=True)
        context.storage_state(path=str(storage_path))
        print(f"Storage state saved to: {storage_path}")

        # Also save a screenshot and HTML for inspection.
        output_dir = storage_path.parent
        page.screenshot(path=str(output_dir / "spike_screenshot.png"), full_page=True)
        (output_dir / "spike_page.html").write_text(page.content(), encoding="utf-8")
        print(f"Screenshot and HTML saved to: {output_dir}")

        browser.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
