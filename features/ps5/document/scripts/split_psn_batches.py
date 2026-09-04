#!/usr/bin/env python3
"""Split the extracted PSN links into smaller batch files for staged crawling.

Usage:
    python scripts/split_psn_batches.py [links_json] [batches_dir] [batch_size]
"""

import json
import math
import sys
from pathlib import Path


def main() -> int:
    links_json = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("spike_output/psn_12_links.json")
    batches_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("spike_output/batches")
    batch_size = int(sys.argv[3]) if len(sys.argv) > 3 else 25

    links = json.loads(links_json.read_text(encoding="utf-8"))
    batches_dir.mkdir(parents=True, exist_ok=True)

    total = len(links)
    num_batches = math.ceil(total / batch_size)

    for i in range(num_batches):
        start = i * batch_size
        end = min(start + batch_size, total)
        batch = links[start:end]
        out_path = batches_dir / f"psn_12_batch_{i + 1:02d}.json"
        out_path.write_text(json.dumps(batch, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"{out_path}: {len(batch)} entries")

    print(f"\nSplit {total} links into {num_batches} batches (size ~{batch_size}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
