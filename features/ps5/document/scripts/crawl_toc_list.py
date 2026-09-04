#!/usr/bin/env python3
"""Crawl a list of toc URLs and their child pages, converting each to Markdown.

Usage:
    python scripts/crawl_toc_list.py <links_json> [output_dir] [--force]
"""

import json
import logging
import math
import random
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from markdownify import markdownify as md

from path_mapping import url_to_relative_path
from playwright.sync_api import sync_playwright


# Force line-buffered output so progress is visible when redirected to a log file.
sys.stdout.reconfigure(line_buffering=True)


STORAGE_STATE = Path(__file__).resolve().parent.parent / "spike_output" / "storage_state.json"
CDP_URL = "http://127.0.0.1:9222"
WAIT_AFTER_LOAD_MS = 800
SLEEP_MIN = 0.2
SLEEP_MAX = 0.5
BACKOFF_BASE_SECONDS = 2.0

# Track consecutive fetch errors for adaptive backoff.
_error_state = {"consecutive_errors": 0}

MASTER_INDEX_FILE = "_index.json"


def load_existing_index(output_dir: Path) -> list[dict]:
    """Load the existing master index if present."""
    index_path = output_dir / MASTER_INDEX_FILE
    if not index_path.exists():
        return []
    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except Exception:
        return []


def setup_logging(log_dir: Path | None = None) -> logging.Logger:
    """Configure file + console logging for the crawl run."""
    log_dir = log_dir or Path(__file__).resolve().parent.parent / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"crawl_{timestamp}.log"

    logger = logging.getLogger("ps5_crawler")
    logger.setLevel(logging.INFO)
    # Avoid duplicate handlers if the function is called more than once.
    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.info(f"Logging to {log_file}")
    return logger


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"


# url_to_relative_path lives in path_mapping.py (shared with crawl_subtree.py)
# so both crawlers route PSN SDK sections into PlayStation_Network/.


_logger: logging.Logger | None = None


def safe_print(message: str, level: int = logging.INFO) -> None:
    """Log and print a message, handling terminals that cannot encode Unicode."""
    if _logger:
        _logger.log(level, message)
    try:
        print(message)
    except UnicodeEncodeError:
        print(message.encode(sys.stdout.encoding or "utf-8", errors="replace").decode(sys.stdout.encoding or "utf-8"))


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
    root_path = "/".join(parts[: idx + 2])
    return f"{parsed.scheme}://{parsed.netloc}{root_path}/"


def resolve_href(raw_href: str, base_url: str) -> str:
    """Resolve a raw href, handling PSN docs' document-root-relative links.

    The site uses hrefs like ``SDK/12.000/NpAuth-Overview/page.html`` or
    ``WebAPI/1/Auth_WebAPI-Overview/page.html`` that are relative to
    ``/resources/documents/`` even when the current page is deep in that tree.
    Detect these top-level document directories and resolve them against the
    document root instead of the current page.
    """
    if ":" in raw_href and not raw_href.startswith(("http://", "https://")):
        return ""

    # Links that start with a top-level document directory are root-relative
    # to /resources/documents/.
    doc_root_dirs = ("SDK/", "WebAPI/")
    root = document_root_for(base_url)
    if root and raw_href.startswith(doc_root_dirs):
        return normalize_url(urljoin(root, raw_href))

    return normalize_url(urljoin(base_url, raw_href))


def collect_child_links(page_html: str, base_url: str) -> list[str]:
    """Collect links that belong to the same directory as base_url.

    The site also uses document-root-relative hrefs (e.g. ``SDK/12.000/...``)
    from pages deep under ``/resources/documents/``; we detect these and resolve
    them against the document root.
    """
    scope_prefix = base_url.rsplit("/", 1)[0] + "/"
    soup = BeautifulSoup(page_html, "html.parser")

    links = []
    seen = set()
    for a in soup.find_all("a", href=True):
        raw_href = a["href"]
        href = resolve_href(raw_href, base_url)
        if not href:
            continue
        # Skip non-document anchors (feedback "undo", bare fragments, etc.).
        if not href.endswith(".html"):
            continue
        if not href.startswith(scope_prefix):
            continue
        if href in seen:
            continue
        seen.add(href)
        links.append(href)
    return links


def fetch_and_save(page, url: str, output_dir: Path, index: list, force: bool = False) -> None:
    url = normalize_url(url)
    rel_path = url_to_relative_path(url)
    md_path = output_dir / rel_path

    if not force and md_path.exists() and any(entry.get("url") == url for entry in index):
        safe_print(f"  SKIP (already crawled): {url}")
        return

    try:
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        # Wait for the actual content container instead of a fixed delay.
        try:
            page.wait_for_selector(".chapter_body, #document_view", timeout=5000)
        except Exception:
            # Fall back to a short fixed wait if the selector is not found.
            page.wait_for_timeout(WAIT_AFTER_LOAD_MS)
    except Exception as exc:
        _error_state["consecutive_errors"] += 1
        backoff = BACKOFF_BASE_SECONDS * (2 ** (_error_state["consecutive_errors"] - 1))
        safe_print(f"  ERROR loading {url}: {exc}", level=logging.ERROR)
        safe_print(f"  Backing off {backoff:.1f}s (consecutive errors: {_error_state['consecutive_errors']})", level=logging.WARNING)
        time.sleep(backoff)
        return

    html = page.content()
    soup = BeautifulSoup(html, "html.parser")
    title = extract_title(soup)

    rel_path = url_to_relative_path(url)
    md_path = output_dir / rel_path
    md_path.parent.mkdir(parents=True, exist_ok=True)

    content_html = extract_main_content(soup)
    markdown = md(content_html, heading_style="ATX", strip=["img", "script", "style"], escape_misc=False)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    markdown = markdown.replace("�", "")

    md_path.write_text(f"# {title}\n\nSource: {url}\n\n{markdown}", encoding="utf-8")
    safe_print(f"  Saved: {md_path}")
    index.append({"title": title, "url": url, "path": str(rel_path)})
    _error_state["consecutive_errors"] = 0


def crawl_toc(start_url: str, output_dir: Path, page, index: list, force: bool = False) -> None:
    start_url = normalize_url(start_url)
    queue = [start_url]
    visited = set()

    while queue:
        url = queue.pop(0)
        if url in visited:
            continue
        visited.add(url)

        safe_print(f"  Fetching {url}")
        fetch_and_save(page, url, output_dir, index, force=force)

        html = page.content()
        for child in collect_child_links(html, url):
            if child not in visited and child not in queue:
                queue.append(child)

        # Small random delay to be polite and avoid steady-rate detection.
        time.sleep(random.uniform(SLEEP_MIN, SLEEP_MAX))


def main() -> int:
    args = sys.argv[1:]
    if not args or "--help" in args or "-h" in args:
        print(__doc__)
        return 0 if not args else 0

    force = "--force" in args
    args = [a for a in args if a != "--force"]

    if len(args) < 1:
        print(__doc__)
        return 1

    global _logger
    _logger = setup_logging()

    links_json = Path(args[0])
    output_dir = Path(args[1]) if len(args) >= 2 else Path("output")

    if not links_json.exists():
        safe_print(f"ERROR: {links_json} not found", level=logging.ERROR)
        return 1

    links = json.loads(links_json.read_text(encoding="utf-8"))

    output_dir.mkdir(parents=True, exist_ok=True)
    index = load_existing_index(output_dir)
    existing_urls = {entry.get("url") for entry in index}

    # Deduplicate by URL and skip already-crawled TOC entries unless forcing.
    seen_urls = set()
    unique_links = []
    for link in links:
        url = normalize_url(link["url"])
        if url in seen_urls:
            continue
        seen_urls.add(url)
        if not force and url in existing_urls:
            safe_print(f"SKIP TOC (already crawled): [{link.get('text', '')}] {url}")
            continue
        unique_links.append({"text": link.get("text", ""), "url": url})

    safe_print(f"Crawling {len(unique_links)} unique toc entries...")

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(CDP_URL)
        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.new_page()

        for entry in unique_links:
            safe_print(f"\n[{entry['text']}] {entry['url']}")
            crawl_toc(entry["url"], output_dir, page, index, force=force)

        # Merge and dedupe before writing.
        seen = set()
        deduped = []
        for entry in index:
            key = (entry.get("url"), entry.get("path"))
            if key in seen:
                continue
            seen.add(key)
            deduped.append(entry)

        index_path = output_dir / MASTER_INDEX_FILE
        index_path.write_text(json.dumps(deduped, indent=2, ensure_ascii=False), encoding="utf-8")
        safe_print(f"\nDone. Total pages: {len(deduped)}. Index: {index_path}")

        browser.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
