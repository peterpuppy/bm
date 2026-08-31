#!/usr/bin/env python3
"""Merge per-batch PSN crawl outputs into a single flat output/psn_12/ tree.

Usage:
    python scripts/merge_psn_batches.py [root_output]
"""
import json
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent / "output" / "psn_12"
DOC_MARKER = "Source: "


def posix_rel(path: Path, base: Path) -> str:
    return path.relative_to(base).as_posix()


def extract_meta_from_md(md_path: Path):
    """Return (title, url) from the markdown header if present."""
    try:
        text = md_path.read_text(encoding="utf-8")
    except Exception:
        return None, None
    lines = text.splitlines()
    title = lines[0].lstrip("# ").strip() if lines else None
    url = None
    for line in lines[1:10]:
        if line.startswith(DOC_MARKER):
            url = line[len(DOC_MARKER):].strip()
            break
    return title, url


def merge_batches(root: Path) -> dict:
    root.mkdir(parents=True, exist_ok=True)
    batch_dirs = sorted(d for d in root.glob("batch_*") if d.is_dir())
    manifest = {
        "batches": [],
        "copied_files": 0,
        "conflicts": [],
        "index_entries": [],
    }

    for batch_dir in batch_dirs:
        batch_name = batch_dir.name
        batch_record = {"name": batch_name, "files": []}

        # Copy markdown files.
        for src in sorted(batch_dir.rglob("*.md")):
            rel = posix_rel(src, batch_dir)
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)

            if dst.exists():
                src_size = src.stat().st_size
                dst_size = dst.stat().st_size
                if src_size != dst_size or src.read_bytes() != dst.read_bytes():
                    resolution = "keep_larger" if src_size > dst_size else "keep_existing"
                    manifest["conflicts"].append({
                        "path": rel,
                        "batch": batch_name,
                        "resolution": resolution,
                    })
                    if src_size > dst_size:
                        shutil.copy2(src, dst)
            else:
                shutil.copy2(src, dst)

            batch_record["files"].append(rel)
            manifest["copied_files"] += 1

        # Collect index entries from batch _index.json or regenerate from markdown.
        batch_index = batch_dir / "_index.json"
        if batch_index.exists():
            try:
                entries = json.loads(batch_index.read_text(encoding="utf-8"))
            except Exception:
                entries = []
            for entry in entries:
                path = Path(entry.get("path", "")).as_posix()
                manifest["index_entries"].append({
                    "title": entry.get("title", "Untitled"),
                    "url": entry.get("url"),
                    "path": path,
                    "batch": batch_name,
                })
        else:
            for md in sorted(batch_dir.rglob("*.md")):
                rel = posix_rel(md, batch_dir)
                title, url = extract_meta_from_md(md)
                if url:
                    manifest["index_entries"].append({
                        "title": title or "Untitled",
                        "url": url,
                        "path": rel,
                        "batch": batch_name,
                        "regenerated": True,
                    })

        manifest["batches"].append(batch_record)

    manifest_path = root / "_merge_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Merged {manifest['copied_files']} files from {len(manifest['batches'])} batches.")
    if manifest["conflicts"]:
        print(f"Resolved {len(manifest['conflicts'])} conflicts; see {manifest_path}")
    return manifest


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
    merge_batches(root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
