#!/usr/bin/env python3
"""Build a single master _index.json from all batch index fragments and markdown files.

Usage:
    python scripts/consolidate_index.py [output_dir]
"""
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent / "output" / "psn_12"
SOURCE_RE = re.compile(r"^Source:\s*(.+)$", re.MULTILINE)


def extract_from_md(md_path: Path, rel_path: str):
    text = md_path.read_text(encoding="utf-8")
    title = text.splitlines()[0].lstrip("# ").strip() if text else "Untitled"
    m = SOURCE_RE.search(text)
    url = m.group(1).strip() if m else None
    return {"title": title, "url": url, "path": rel_path}


def consolidate(root: Path) -> list[dict]:
    root.mkdir(parents=True, exist_ok=True)
    manifest_path = root / "_merge_manifest.json"
    entries: dict[str, dict] = {}

    # Seed from merge manifest if present.
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for entry in manifest.get("index_entries", []):
            path = Path(entry.get("path", "")).as_posix()
            if not path:
                continue
            entries.setdefault(path, {
                "title": entry.get("title", "Untitled"),
                "path": path,
                "urls": [],
                "batches": [],
            })
            rec = entries[path]
            url = entry.get("url")
            if url and url not in rec["urls"]:
                rec["urls"].append(url)
            batch = entry.get("batch")
            if batch and batch not in rec["batches"]:
                rec["batches"].append(batch)

    # Reconcile against actual markdown files on disk (skip legacy batch dirs).
    for md in sorted(root.rglob("*.md")):
        rel_parts = md.relative_to(root).parts
        if rel_parts and rel_parts[0].startswith("batch_"):
            continue
        rel = md.relative_to(root).as_posix()
        if rel not in entries:
            meta = extract_from_md(md, rel)
            entries[rel] = {
                "title": meta["title"],
                "path": rel,
                "urls": [meta["url"]] if meta["url"] else [],
                "batches": [],
            }

    # Build canonical index.
    canonical = []
    for rel in sorted(entries):
        rec = entries[rel]
        primary_url = rec["urls"][0] if rec["urls"] else None
        alt_urls = rec["urls"][1:] if len(rec["urls"]) > 1 else []
        item = {
            "title": rec["title"],
            "url": primary_url,
            "path": rel,
        }
        if alt_urls:
            item["alt_urls"] = alt_urls
        if rec["batches"]:
            item["batches"] = rec["batches"]
        canonical.append(item)

    out_path = root / "_index.json"
    out_path.write_text(json.dumps(canonical, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Consolidated {len(canonical)} entries into {out_path}")
    duplicate_urls = sum(1 for item in canonical if "alt_urls" in item)
    if duplicate_urls:
        print(f"Note: {duplicate_urls} entries had multiple source URLs mapping to the same path.")
    return canonical


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
    consolidate(root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
