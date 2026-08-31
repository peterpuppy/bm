#!/usr/bin/env python3
"""Run all PlayStation Network doc batches sequentially into a single output tree.

Usage:
    python scripts/run_all_batches.py [batch_size] [--start-batch N] [--end-batch M]

Defaults to batches of 10 toc entries.  Keeps one browser session open across
all batches to avoid repeated CDP connection/login overhead.  Already-crawled
URLs are skipped automatically.
"""

import json
import logging
import math
import subprocess
import sys
from datetime import datetime
from pathlib import Path


LINKS_JSON = Path("spike_output/psn_12_links.json")
BATCHES_DIR = Path("spike_output/batches")
OUTPUT_DIR = Path("output/psn_12")
DEFAULT_BATCH_SIZE = 10


def setup_logging() -> logging.Logger:
    """Configure a master log file for the multi-batch run."""
    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"run_batches_{timestamp}.log"

    logger = logging.getLogger("ps5_batch_runner")
    logger.setLevel(logging.INFO)
    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.info(f"Master log: {log_file}")
    return logger


def split_batches(links: list[dict], batch_size: int) -> list[Path]:
    BATCHES_DIR.mkdir(parents=True, exist_ok=True)
    # Remove old batch files.
    for old in BATCHES_DIR.glob("psn_12_batch_*.json"):
        old.unlink()

    paths = []
    total = len(links)
    num_batches = math.ceil(total / batch_size)
    for i in range(num_batches):
        batch = links[i * batch_size : (i + 1) * batch_size]
        path = BATCHES_DIR / f"psn_12_batch_{i + 1:02d}.json"
        path.write_text(json.dumps(batch, indent=2, ensure_ascii=False), encoding="utf-8")
        paths.append(path)
    return paths


def main() -> int:
    logger = setup_logging()
    args = sys.argv[1:]

    start_batch = 1
    end_batch = None

    if "--start-batch" in args:
        i = args.index("--start-batch")
        start_batch = int(args[i + 1])
        args = args[:i] + args[i + 2:]
    if "--end-batch" in args:
        i = args.index("--end-batch")
        end_batch = int(args[i + 1])
        args = args[:i] + args[i + 2:]

    batch_size = int(args[0]) if args else DEFAULT_BATCH_SIZE

    links = json.loads(LINKS_JSON.read_text(encoding="utf-8"))
    batch_files = split_batches(links, batch_size)
    logger.info(f"Split {len(links)} links into {len(batch_files)} batches of ~{batch_size}.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    end_batch = end_batch or len(batch_files)
    for idx in range(start_batch, end_batch + 1):
        batch_file = batch_files[idx - 1]
        logger.info("=" * 60)
        logger.info(f"Batch {idx}/{len(batch_files)}: {batch_file} -> {OUTPUT_DIR}")
        logger.info("=" * 60)
        result = subprocess.run(
            ["python", "scripts/crawl_toc_list.py", str(batch_file), str(OUTPUT_DIR)],
            check=False,
        )
        if result.returncode != 0:
            logger.warning(f"Batch {idx} exited with code {result.returncode}")

    logger.info("All batches complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
