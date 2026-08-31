#!/usr/bin/env python3
"""Fetch a single PS5 doc page and convert it to Markdown for review.

Usage:
    python scripts/fetch_single.py <url> [output_dir]
"""

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from markdownify import markdownify as md
from playwright.sync_api import sync_playwright


CDP_URL = "http://127.0.0.1:9222"


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"


def url_to_relative_path(url: str) -> Path:
    parsed = urlparse(url)
    path_str = parsed.path[1:] if parsed.path.startswith("/") else parsed.path
    parts = path_str.split("/")
    if len(parts) >= 2 and parts[0] == "resources" and parts[1] == "documents":
        parts = parts[2:]

    if not parts:
        parts = ["index.md"]
    elif parts[-1].startswith("__"):
        parts[-1] = "index.md"
    else:
        name = parts[-1].rsplit(".", 1)[0] if "." in parts[-1] else parts[-1]
        parts[-1] = f"{name}.md"

    return Path("/".join(parts))


def extract_title(soup: BeautifulSoup) -> str:
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    h1 = soup.find("h1")
    return h1.get_text(strip=True) if h1 else "Untitled"


def extract_main_content(soup: BeautifulSoup) -> str:
    """Return the real document text, excluding the site/global navigation.

    PSN docs render one or more chapter bodies inside #document_view.  The
    sidebar (#local_nav) lives in there too, so we extract #document_view and
    strip the sidebar, then fall back to .chapter_body and other containers.
    """
    document_view = soup.find("div", id="document_view")
    if document_view:
        for nav in document_view.find_all(["nav", "div"], id="local_nav"):
            nav.decompose()
        for feedback in document_view.find_all("div", class_="chapter_feedback"):
            feedback.decompose()
        return str(document_view)

    chapter_body = soup.find("div", class_="chapter_body")
    if chapter_body:
        for feedback in chapter_body.find_all("div", class_="chapter_feedback"):
            feedback.decompose()
        return str(chapter_body)

    content = soup.find(id="content") or soup.find("main") or soup.find("article")
    if content:
        return str(content)

    body = soup.find("body")
    if body:
        for tag in body.find_all(["nav", "header", "footer", "script", "style"]):
            tag.decompose()
        return str(body)
    return str(soup)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    url = sys.argv[1]
    output_dir = Path(sys.argv[2]) if len(sys.argv) >= 3 else Path("output/single_review")

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(CDP_URL)
        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.new_page()

        print(f"Fetching {url} ...")
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(1500)

        html = page.content()
        soup = BeautifulSoup(html, "html.parser")
        title = extract_title(soup)

        rel_path = url_to_relative_path(url)
        md_path = output_dir / rel_path
        md_path.parent.mkdir(parents=True, exist_ok=True)

        content_html = extract_main_content(soup)
        markdown = md(
            content_html,
            heading_style="ATX",
            strip=["img", "script", "style"],
            escape_misc=False,
        )
        markdown = re.sub(r"\n{3,}", "\n\n", markdown)
        markdown = markdown.replace("�", "")

        md_path.write_text(f"# {title}\n\nSource: {url}\n\n{markdown}", encoding="utf-8")
        print(f"Saved: {md_path}")
        print(f"Length: {len(markdown)} chars")

        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
