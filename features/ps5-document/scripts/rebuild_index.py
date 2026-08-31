#!/usr/bin/env python3
"""重建 output/psn_12/_index.json：扫描所有 .md 文件，按目录结构生成索引。

用法:
    python scripts/rebuild_index.py
"""
import json
import re
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output" / "psn_12"
INDEX_PATH = OUTPUT_DIR / "_index.json"

SOURCE_RE = re.compile(r"^Source:\s*(\S+)", re.MULTILINE)


def extract_title(md_path: Path) -> str:
    try:
        with open(md_path, encoding="utf-8") as f:
            for line in f:
                if line.startswith("# "):
                    return line[2:].strip()
    except Exception:
        pass
    return md_path.stem


def extract_source_url(md_path: Path) -> str | None:
    """Pull the real source URL from the `Source:` header written by the crawler."""
    try:
        with open(md_path, encoding="utf-8") as f:
            m = SOURCE_RE.search(f.read())
            if m:
                return m.group(1).strip()
    except Exception:
        pass
    return None


def main() -> None:
    entries = []
    for md in sorted(OUTPUT_DIR.rglob("*.md")):
        rel = md.relative_to(OUTPUT_DIR).as_posix()  # 正斜杠
        # url 来自文件头 Source: 行（真实原始 URL），不从本地路径反推——
        # 本地树已按 PSN 子域聚拢，路径不再是 URL 的镜像。
        url = extract_source_url(md) or ""
        entries.append({
            "title": extract_title(md),
            "url": url,
            "path": rel,
        })
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    print(f"rebuilt {INDEX_PATH}: {len(entries)} entries")


if __name__ == "__main__":
    main()
