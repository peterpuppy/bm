#!/usr/bin/env python3
"""Attempt to copy locked Chrome Cookies file using shared read access."""

import os
import shutil
import sys
import tempfile
from pathlib import Path


def copy_file_shared(src: Path, dst: Path) -> None:
    """Copy a file using FILE_SHARE_READ to bypass locks held by other processes."""
    import msvcrt
    import ctypes
    from ctypes import wintypes

    GENERIC_READ = 0x80000000
    FILE_SHARE_READ = 0x00000001
    OPEN_EXISTING = 3
    FILE_ATTRIBUTE_NORMAL = 0x80

    kernel32 = ctypes.windll.kernel32
    h_src = kernel32.CreateFileW(
        str(src),
        GENERIC_READ,
        FILE_SHARE_READ,
        None,
        OPEN_EXISTING,
        FILE_ATTRIBUTE_NORMAL,
        None,
    )
    if h_src == -1:
        raise OSError(f"Cannot open {src}: {ctypes.get_last_error()}")

    dst.parent.mkdir(parents=True, exist_ok=True)
    with open(dst, "wb") as f_out:
        buffer_size = 64 * 1024
        while True:
            buf = ctypes.create_string_buffer(buffer_size)
            read = wintypes.DWORD()
            ok = kernel32.ReadFile(h_src, buf, buffer_size, ctypes.byref(read), None)
            if not ok:
                kernel32.CloseHandle(h_src)
                raise OSError(f"ReadFile failed: {ctypes.get_last_error()}")
            if read.value == 0:
                break
            f_out.write(buf[: read.value])

    kernel32.CloseHandle(h_src)


def main() -> int:
    src = Path(os.environ["LOCALAPPDATA"]) / "Google" / "Chrome" / "User Data" / "Profile 1" / "Network" / "Cookies"
    dst = Path(tempfile.gettempdir()) / "ps5_cookies_copy.sqlite"

    print(f"Trying to copy locked file: {src}")
    try:
        copy_file_shared(src, dst)
        print(f"Success: copied to {dst}, size {dst.stat().st_size} bytes")
        return 0
    except Exception as exc:
        print(f"Failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
