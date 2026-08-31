#!/usr/bin/env python3
"""Shared URL → local-path mapping for PS5 doc crawlers.

The DevNet site's sidebar (#local_nav) groups every doc under a category
hierarchy (e.g. PlayStation™Network › Trophies › NpTrophy2 Library Overview),
but the URLs themselves are flat — ``SDK/12.000/NpTrophy2-Overview/__toc.html``
carries no "Trophies" segment.  To mirror the *site's organizational structure*
(not its URL structure) in the local tree, we map each section to the
category_path recorded in ``sdk_12_catalog.json`` and build the local path from
that hierarchy.  SDK and WebAPI docs that the sidebar groups together land in
the same folder.

Sections not present in the catalog (e.g. ``SDK/latest/...``) fall back to the
flat URL path — re-run ``extract_sdk_12_catalog.py`` to pick up new sections.
"""

import json
import re
from pathlib import Path
from urllib.parse import urlparse

CATALOG_PATH = Path(__file__).resolve().parent.parent / "spike_output" / "sdk_12_catalog.json"

# Characters Windows forbids in folder names, plus commas (ugly in paths).
_INVALID = re.compile(r'[\\/:*?"<>|,]')

_SECTION_MAP: dict[str, list[str]] | None = None


def _sanitize_category(name: str) -> str:
    """Turn a sidebar category name into a safe folder name.

    'PlayStation™Network' → 'PlayStation_Network'
    'Session Manager (Sessions, Invitations, Matches, Matchmaking)' →
        'Session_Manager_(Sessions_Invitations_Matches_Matchmaking)'
    """
    for ch in "™®":
        name = name.replace(ch, "")
    name = _INVALID.sub("_", name)
    name = name.replace(" ", "_")
    name = re.sub(r"_+", "_", name)
    return name.strip("_")


def _section_path(url: str) -> str:
    """Return the URL's section path (everything after /documents/ minus page).

    '.../SDK/12.000/NpTrophy2-Overview/__toc.html' → 'SDK/12.000/NpTrophy2-Overview'
    '.../WebAPI/1/Trophy2_WebAPI-Overview/__toc.html' → 'WebAPI/1/Trophy2_WebAPI-Overview'
    """
    parsed = urlparse(url)
    parts = parsed.path.split("/")
    # Drop the leading empty segment from the absolute-path leading slash.
    if parts and parts[0] == "":
        parts = parts[1:]
    if len(parts) >= 2 and parts[0] == "resources" and parts[1] == "documents":
        parts = parts[2:]
    return "/".join(parts[:-1])


def _load_section_map() -> dict[str, list[str]]:
    """Build {section_path: category_path}, preferring the deepest grouping."""
    global _SECTION_MAP
    if _SECTION_MAP is not None:
        return _SECTION_MAP
    m: dict[str, list[str]] = {}
    try:
        catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
        for leaf in catalog.get("leafs", []):
            sp = _section_path(leaf.get("url", ""))
            cp = leaf.get("category_path", [])
            if sp and cp and (sp not in m or len(cp) > len(m[sp])):
                m[sp] = cp
    except (OSError, ValueError):
        # Catalog missing/corrupt — fall back to flat layout (faithful to URL).
        pass
    _SECTION_MAP = m
    return m


def _page_to_md(page: str) -> str:
    """'__toc.html' → 'index.md', 'purpose.html' → 'purpose.md'."""
    if not page or page.startswith("__"):
        return "index.md"
    name = page.rsplit(".", 1)[0] if "." in page else page
    return f"{name}.md"


def url_to_relative_path(url: str) -> Path:
    """Map a document URL to a relative output path.

    Catalog-known sections route by sidebar category_path (minus the trailing
    leaf title, which is redundant with the URL section name). SDK and WebAPI
    docs that the sidebar groups together land as siblings under the same
    business-domain folder. Unknown sections fall back to the flat URL path.
    """
    parsed = urlparse(url)
    path_str = parsed.path[1:] if parsed.path.startswith("/") else parsed.path
    parts = path_str.split("/")
    if len(parts) >= 2 and parts[0] == "resources" and parts[1] == "documents":
        parts = parts[2:]

    section = "/".join(parts[:-1])
    cp = _load_section_map().get(section)

    if cp and len(cp) >= 2 and len(parts) >= 2:
        # category_path[:-1] = folder hierarchy; URL section = leaf folder.
        folders = [_sanitize_category(c) for c in cp[:-1]]
        section_seg = parts[-2]
        page_name = _page_to_md(parts[-1])
        return Path(*folders, section_seg, page_name)

    # Fallback: flat URL path (docs not in catalog, e.g. SDK/latest/...).
    if not parts:
        parts = ["index.md"]
    elif parts[-1].startswith("__"):
        parts[-1] = "index.md"
    else:
        parts[-1] = _page_to_md(parts[-1])
    return Path("/".join(parts))
