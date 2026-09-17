"""Read the WPA VirtualAlloc-Commit CSV and yield one cleaned row per allocation.

Columns are located by header NAME, so column reordering / inserted columns
(e.g. WPA's "Commit Stack (Frame Tags)") don't break parsing.
"""
import csv
from dataclasses import dataclass
from typing import Iterator

# Stacks can be several KB per row; raise the csv field cap to 16 MiB.
csv.field_size_limit(1 << 24)

# Text WPA puts in a frame when symbols aren't loaded.
_NO_SYMBOL_MARKER = "<Symbols disabled>"


@dataclass(frozen=True)
class RawRow:
    stack: str            # "Commit Stack": [Root]/mod!sym/mod!sym/...
    impacting_mb: float   # net-resident at trace end (0 if WPA didn't compute it)
    size_mb: float        # cumulative committed (includes freed allocations)
    decommitted: bool     # has a Decommit Time
    symbolless: bool      # stack has no symbols


def _find_col(header, *names) -> int:
    low = [c.strip().lower() for c in header]
    for n in names:
        if n in low:
            return low.index(n)
    return -1


def _to_float(s: str) -> float:
    # Excel sometimes writes numbers as forced-text formulas: ="123,456.789".
    # csv.reader returns them literally; strip the formula wrapper before parsing.
    if isinstance(s, str):
        s = s.strip()
        if len(s) >= 3 and s.startswith('="') and s.endswith('"'):
            s = s[2:-1]
    try:
        return float(s.replace(",", ""))
    except (ValueError, AttributeError):
        return 0.0


class ColumnError(Exception):
    pass


def iter_rows(path: str) -> Iterator[RawRow]:
    """Stream cleaned rows, skipping the per-process total row (no stack).

    Process isolation must happen BEFORE export (filter-to-process in WPA, or a
    Process condition in the profile): when WPA expands a stack into detail rows
    the Process column lands only on the group header, leaving detail rows blank.
    """
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header is None:
            return
        c_stack = _find_col(header, "commit stack", "commit stack (frame tags)")
        c_size = _find_col(header, "size (mb)")
        c_imp = _find_col(header, "impacting size (mb)")
        c_dec = _find_col(header, "decommit time (s)")
        if c_stack < 0 or c_size < 0:
            raise ColumnError(
                "missing required columns 'Commit Stack' / 'Size (MB)'; "
                f"got header: {header}")

        wide = max(c for c in (c_stack, c_size, c_imp, c_dec) if c >= 0)
        for row in reader:
            if len(row) <= wide:
                continue
            stack = row[c_stack]
            if not stack:               # process-total / aggregate rows
                continue
            yield RawRow(
                stack=stack,
                impacting_mb=_to_float(row[c_imp]) if c_imp >= 0 else 0.0,
                size_mb=_to_float(row[c_size]),
                decommitted=(row[c_dec].strip() != "") if c_dec >= 0 else False,
                symbolless=(_NO_SYMBOL_MARKER in stack),
            )
