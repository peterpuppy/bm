#!/usr/bin/env python3
"""Inspect Chrome cookies for the PS5 docs domain, focusing on session tokens."""

import os
import shutil
import sqlite3
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def chrome_epoch_to_utc(microseconds: int) -> datetime:
    # Chrome cookies use microseconds since 1601-01-01 UTC.
    return datetime(1601, 1, 1, tzinfo=timezone.utc) + __import__("datetime").timedelta(microseconds=microseconds)


def main() -> None:
    db = Path(os.environ["LOCALAPPDATA"]) / "Google" / "Chrome" / "User Data" / "Profile 1" / "Network" / "Cookies"
    temp = Path(tempfile.gettempdir()) / "ps5_cookies_inspect.sqlite"
    shutil.copy2(db, temp)

    conn = sqlite3.connect(temp)
    cursor = conn.cursor()
    cols = {row[1] for row in cursor.execute("PRAGMA table_info(cookies)")}
    has_same_site = "same_site" in cols

    select_cols = "host_key, name, value, path, expires_utc, is_secure, is_httponly"
    if has_same_site:
        select_cols += ", same_site"

    rows = cursor.execute(
        f"SELECT {select_cols} FROM cookies WHERE host_key LIKE ?",
        ("%playstation.net%",),
    ).fetchall()
    conn.close()
    temp.unlink(missing_ok=True)

    now = datetime.now(timezone.utc)
    print(f"{'Name':<50} {'Domain':<40} {'Expires (UTC)':<30} {'Status'}")
    print("-" * 130)
    for row in rows:
        name = row[1]
        domain = row[0]
        expires_utc = row[4]
        expires = chrome_epoch_to_utc(expires_utc) if expires_utc else None
        status = "EXPIRED" if expires and expires < now else "valid"
        expires_str = expires.strftime("%Y-%m-%d %H:%M:%S") if expires else "session"
        print(f"{name:<50} {domain:<40} {expires_str:<30} {status}")


if __name__ == "__main__":
    main()
