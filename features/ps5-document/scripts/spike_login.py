#!/usr/bin/env python3
"""Self-contained login + attach spike.

This script starts Chrome with a remote debugging port and a fresh profile,
waits for the user to log in manually, then attaches Playwright to the same
Chrome process to verify access and save storage state.
"""

import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from playwright.sync_api import sync_playwright


def get_chrome_executable() -> Path:
    candidates = [
        Path(os.environ.get("PROGRAMFILES", "C:\\Program Files")) / "Google" / "Chrome" / "Application" / "chrome.exe",
        Path(os.environ.get("PROGRAMFILES(X86)", "C:\\Program Files (x86)")) / "Google" / "Chrome" / "Application" / "chrome.exe",
        Path(os.environ.get("LOCALAPPDATA")) / "Google" / "Chrome" / "Application" / "chrome.exe",
    ]
    for c in candidates:
        if c.exists():
            return c
    raise FileNotFoundError("Could not find chrome.exe")


def is_login_page(url: str) -> bool:
    lowered = url.lower()
    return any(k in lowered for k in ("sign-in", "signin", "login", "authenticate", "saml"))


def wait_for_chrome_debug_port(port: int = 9222, timeout: int = 30) -> bool:
    import socket
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=1):
                return True
        except OSError:
            time.sleep(0.5)
    return False


def main() -> int:
    start_url = "https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_WebAPI-Overview/__toc.html"
    storage_path = Path(__file__).resolve().parent.parent / "spike_output" / "storage_state.json"
    chrome_exe = get_chrome_executable()
    user_data_dir = Path(tempfile.gettempdir()) / "ps5_crawler_profile_attach"
    port = 9222

    if user_data_dir.exists():
        import shutil
        shutil.rmtree(user_data_dir)

    print("Starting Chrome with remote debugging port...")
    cmd = [
        str(chrome_exe),
        f"--remote-debugging-port={port}",
        f"--user-data-dir={user_data_dir}",
        "--no-first-run",
        "--no-default-browser-check",
        "--start-maximized",
        start_url,
    ]
    proc = subprocess.Popen(cmd)

    if not wait_for_chrome_debug_port(port):
        print("ERROR: Chrome did not open debug port.", file=sys.stderr)
        proc.terminate()
        return 1

    print("Chrome started. Please complete login in the browser window.")
    print("Script will auto-detect login completion (up to 10 minutes).")

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{port}")
        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.pages[0] if context.pages else context.new_page()

        # Ensure we are on the target page.
        if page.url == "about:blank":
            page.goto(start_url, timeout=60000)

        timeout_seconds = 600
        poll_interval = 3
        logged_in = False
        for i in range(0, timeout_seconds, poll_interval):
            current_url = page.url
            if i % 15 == 0:
                print(f"[{i}s] Current URL: {current_url}")
            if not is_login_page(current_url):
                logged_in = True
                print(f"Login detected at {i}s. Current URL: {current_url}")
                break
            time.sleep(poll_interval)

        if not logged_in:
            print("ERROR: Login was not completed within 10 minutes.", file=sys.stderr)
            browser.close()
            proc.terminate()
            return 1

        page.wait_for_timeout(3000)

        print("Saving storage state...")
        storage_path.parent.mkdir(exist_ok=True)
        context.storage_state(path=str(storage_path))
        print(f"Storage state saved to: {storage_path}")

        print(f"Page title: {page.title()}")
        print(f"Current URL: {page.url}")

        nav_selectors = ["nav", "aside", "[class*='toc']", "[class*='navigation']", "[class*='menu']"]
        found = False
        for selector in nav_selectors:
            count = page.locator(selector).count()
            if count > 0:
                print(f"Found nav-like element with selector '{selector}': {count} instance(s)")
                found = True

        if not found:
            print("WARNING: No obvious navigation element found.")

        output_dir = Path(__file__).resolve().parent.parent / "spike_output"
        output_dir.mkdir(exist_ok=True)
        page.screenshot(path=str(output_dir / "spike_screenshot.png"), full_page=True)
        (output_dir / "spike_page.html").write_text(page.content(), encoding="utf-8")
        print(f"Screenshot and HTML saved to: {output_dir}")

        browser.close()

    proc.terminate()
    return 0


if __name__ == "__main__":
    sys.exit(main())
