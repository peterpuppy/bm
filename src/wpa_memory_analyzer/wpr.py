#!/usr/bin/env python3
"""Entry point. Adds src/ to the path and runs the CLI, so it works from any cwd:

    python wpr.py <csv> --out <dir> --top 20 --func-top 20

See usage.md.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from cli import main  # noqa: E402

if __name__ == "__main__":
    main()
