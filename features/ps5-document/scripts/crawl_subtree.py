#!/usr/bin/env python3
"""Batch crawler for PS5 docs: crawl a subtree and convert pages to Markdown.

Usage:
    python scripts/crawl_subtree.py <start_url> [output_dir]

Example:
    python scripts/crawl_subtree.py https://game.develop.playstation.net/resources/documents/WebAPI/latest/Auth_for_Websites-Overview/__document_toc.html
"""

import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from markdownify import markdownify as md
from playwright.sync_api import sync_playwright

from path_mapping import url_to_relative_path


# Force line-buffered output so progress is visible when redirected to a log file.
sys.stdout.reconfigure(line_buffering=True)


STORAGE_STATE = Path(__file__).resolve().parent.parent / "spike_output" / "storage_state.json"
CDP_URL = "http://127.0.0.1:9222"
SLEEP_SECONDS = 1.0


def safe_print(message: str) -> None:
    """Print a message, replacing characters the terminal cannot encode."""
    try:
        print(message)
    except UnicodeEncodeError:
        print(message.encode(sys.stdout.encoding or "utf-8", errors="replace").decode(sys.stdout.encoding or "utf-8"))


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    # Drop fragment.
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"


# url_to_relative_path lives in path_mapping.py (shared with crawl_toc_list.py)
# so both crawlers route PSN SDK sections into PlayStation_Network/.


def extract_title(soup: BeautifulSoup) -> str:
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    h1 = soup.find("h1")
    if h1:
        return h1.get_text(strip=True)
    return "Untitled"


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


def document_root_for(url: str) -> str | None:
    """Return the document root URL if `url` lives under /resources/documents/."""
    parsed = urlparse(url)
    parts = parsed.path.split("/")
    try:
        idx = parts.index("resources")
    except ValueError:
        return None
    if idx + 1 >= len(parts) or parts[idx + 1] != "documents":
        return None
    root_path = "/".join(parts[: idx + 2])  # /resources/documents
    return f"{parsed.scheme}://{parsed.netloc}{root_path}/"


def resolve_href(raw_href: str, base_url: str) -> str:
    """Resolve a raw href, handling PSN docs' document-root-relative links.

    The site uses hrefs like ``SDK/12.000/NpAuth-Overview/page.html`` or
    ``WebAPI/1/Auth_WebAPI-Overview/page.html`` that are relative to
    ``/resources/documents/`` even when the current page is deep in that tree.
    Detect these top-level document directories and resolve them against the
    document root instead of the current page.
    """
    # Skip non-HTTP schemes and anchors.
    if ":" in raw_href and not raw_href.startswith(("http://", "https://")):
        return ""

    doc_root_dirs = ("SDK/", "WebAPI/")
    root = document_root_for(base_url)
    if root and raw_href.startswith(doc_root_dirs):
        return normalize_url(urljoin(root, raw_href))

    return normalize_url(urljoin(base_url, raw_href))


def collect_links(page_html: str, base_url: str, prefix: str) -> list[str]:
    soup = BeautifulSoup(page_html, "html.parser")
    links = []
    seen = set()
    for a in soup.find_all("a", href=True):
        href = resolve_href(a["href"], base_url)
        if not href:
            continue
        # Skip non-document anchors (feedback "undo", bare fragments, etc.).
        if not href.endswith(".html"):
            continue
        if not href.startswith(prefix):
            continue
        if href in seen:
            continue
        seen.add(href)
        links.append(href)
    return links


def crawl(start_url: str, output_dir: Path) -> None:
    if not STORAGE_STATE.exists():
        print(f"ERROR: Storage state not found at {STORAGE_STATE}", file=sys.stderr)
        sys.exit(1)

    start_url = normalize_url(start_url)
    # Determine scope: same directory prefix as the start URL (up to the last slash).
    scope_prefix = start_url.rsplit("/", 1)[0] + "/"

    output_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(CDP_URL)
        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.new_page()

        queue = [start_url]
        visited = set()
        index = []

        while queue:
            url = queue.pop(0)
            if url in visited:
                continue
            visited.add(url)

            safe_print(f"[{len(visited)}] Fetching {url} ...")
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=60000)
                page.wait_for_timeout(1500)
            except Exception as exc:
                print(f"  ERROR loading {url}: {exc}", file=sys.stderr)
                continue

            html = page.content()
            soup = BeautifulSoup(html, "html.parser")
            title = extract_title(soup)
            current_url = page.url

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
            # Cleanup excessive blank lines and unicode replacement chars.
            markdown = re.sub(r"\n{3,}", "\n\n", markdown)
            markdown = markdown.replace("�", "")

            md_path.write_text(f"# {title}\n\nSource: {url}\n\n{markdown}", encoding="utf-8")
            safe_print(f"  Saved: {md_path}")

            index.append({"title": title, "url": url, "path": str(rel_path)})

            # Discover child links within scope.
            child_links = collect_links(html, current_url, scope_prefix)
            for child in child_links:
                if child not in visited and child not in queue:
                    queue.append(child)

            time.sleep(SLEEP_SECONDS)

        # Save index: merge with existing _index.json (dedup by url) instead of overwriting.
        index_path = output_dir / "_index.json"
        existing = []
        if index_path.exists():
            try:
                existing = json.loads(index_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                existing = []
        seen = {e.get("url") for e in existing if isinstance(e, dict)}
        merged = existing + [e for e in index if e.get("url") not in seen]
        index_path.write_text(json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nDone. Crawled {len(index)} pages. Index: {index_path} (total {len(merged)})")

        browser.close()


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    start_url = sys.argv[1]
    output_dir = Path(sys.argv[2]) if len(sys.argv) >= 3 else Path("output")
    crawl(start_url, output_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
