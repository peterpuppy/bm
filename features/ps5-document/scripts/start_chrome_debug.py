#!/usr/bin/env python3
"""Just start Chrome with remote debugging port and keep it alive."""

import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path


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


def main() -> int:
    url = "https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_WebAPI-Overview/__toc.html"
    chrome_exe = get_chrome_executable()
    # Use a persistent profile inside the project so login state survives restarts.
    user_data_dir = Path(__file__).resolve().parent.parent / "chrome_profile"
    user_data_dir.mkdir(parents=True, exist_ok=True)
    port = 9222

    print(f"Starting Chrome on debug port {port}...")
    print("User data dir:", user_data_dir)
    print("Please log in, then run: python scripts/save_storage.py")
    print("Keep this window open while crawling.")

    cmd = [
        str(chrome_exe),
        f"--remote-debugging-port={port}",
        f"--user-data-dir={user_data_dir}",
        "--no-first-run",
        "--no-default-browser-check",
        "--start-maximized",
        url,
    ]
    proc = subprocess.Popen(cmd)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down Chrome...")
    finally:
        proc.terminate()

    return 0


if __name__ == "__main__":
    sys.exit(main())
