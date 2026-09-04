#!/usr/bin/env python3
"""Convert the saved PS5 docs HTML page to Markdown for inspection."""

import sys
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as md


def main() -> int:
    html_path = Path(__file__).resolve().parent.parent / "spike_output" / "spike_page.html"
    html = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    # PSN docs render chapter bodies inside #document_view.  The sidebar
    # (#local_nav) lives in there too, so prefer #document_view with the sidebar
    # removed, then fall back to other containers.
    content = soup.find("div", id="document_view")
    if content:
        for nav in content.find_all(["nav", "div"], id="local_nav"):
            nav.decompose()
        for feedback in content.find_all("div", class_="chapter_feedback"):
            feedback.decompose()
    if not content:
        content = soup.find("div", class_="chapter_body")
        if content:
            for feedback in content.find_all("div", class_="chapter_feedback"):
                feedback.decompose()
    if not content:
        content = soup.find(id="content") or soup.find("main") or soup.find("article")
    if not content:
        # Fall back to body minus nav/header/footer.
        body = soup.find("body")
        if body:
            for tag in body.find_all(["nav", "header", "footer"]):
                tag.decompose()
        content = body

    if not content:
        print("ERROR: Could not find main content.", file=sys.stderr)
        return 1

    markdown = md(str(content), heading_style="ATX", strip=["img", "script", "style"])

    out_path = Path(__file__).resolve().parent.parent / "spike_output" / "spike_page.md"
    out_path.write_text(markdown, encoding="utf-8")
    print(f"Markdown saved to: {out_path}")
    print(f"Length: {len(markdown)} characters")
    print("\n--- First 1500 chars preview ---\n")
    print(markdown[:1500])

    return 0


if __name__ == "__main__":
    sys.exit(main())
