"""Aggregate parsed rows into the three views the report renders.

One pass over the loader rows: parse each stack, pick the best size metric
(_choose_metric), and sum into per-module / per-function tables. No I/O here.
"""
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Callable, Dict, List, NamedTuple, Tuple

import loader
import parse

# Symbol-less rate below this counts as "have symbols" (views 2/3 and the
# heap/direct split only mean something with symbols).
_SYMBOL_THRESHOLD_PCT = 50.0


class Rec(NamedTuple):
    impacting: float
    size: float
    decommitted: bool
    alloc_mod: str
    biz_mod: str
    biz_frame: str
    is_heap: bool
    is_mempool: bool
    is_default_pool: bool
    dp_chain: tuple          # business-frame chain (leaf->root), only for DefaultPool rows


def _f() -> Dict[str, float]:
    return defaultdict(float)


def _ff() -> Dict[str, Dict[str, float]]:
    return defaultdict(lambda: defaultdict(float))


def _tree_insert(forest: dict, chain: tuple, mb: float) -> None:
    """Add mb along a caller chain into a forest of {frame: {"mb", "kids"}} nodes."""
    level = forest
    for frame in chain:
        node = level.get(frame)
        if node is None:
            node = {"mb": 0.0, "kids": {}}
            level[frame] = node
        node["mb"] += mb
        level = node["kids"]


@dataclass
class Result:
    path: str
    total_rows: int
    symbolless_pct: float
    have_symbols: bool
    metric_name: str
    is_churn: bool
    grand_mb: float
    # View 1 -- allocator module (deepest non-system frame).
    by_module: Dict[str, float] = field(default_factory=_f)
    # View 2 -- business caller: module total + per-module {frame: mb}.
    by_biz_module: Dict[str, float] = field(default_factory=_f)
    by_biz_func: Dict[str, Dict[str, float]] = field(default_factory=_ff)
    # View 3 -- non-pool heap (heap path without a mempool frame).
    nph_total_mb: float = 0.0
    by_nph_module: Dict[str, float] = field(default_factory=_f)
    by_nph_func: Dict[str, Dict[str, float]] = field(default_factory=_ff)
    # View 4 -- DefaultPool (catch-all pool), a subset of pool-backed heap.
    dp_total_mb: float = 0.0
    by_dp_module: Dict[str, float] = field(default_factory=_f)
    by_dp_func: Dict[str, Dict[str, float]] = field(default_factory=_ff)
    by_dp_tree: Dict[str, dict] = field(default_factory=dict)  # module -> caller-tree forest
    # alloc-path split (needs symbols).
    heap_mb: float = 0.0
    direct_mb: float = 0.0
    pool_heap_mb: float = 0.0


def _choose_metric(recs: List[Rec]) -> Tuple[str, Callable[[Rec], float], List[Rec], bool]:
    if sum(r.impacting for r in recs) > 0:
        return "Impacting (net-resident)", (lambda r: r.impacting), recs, False
    resident = [r for r in recs if not r.decommitted]
    if sum(r.size for r in resident) > 0:
        return "Size of never-freed allocs (net-resident)", (lambda r: r.size), resident, False
    return "Size CUMULATIVE (CHURN -- NOT resident!)", (lambda r: r.size), recs, True


def analyze(path: str) -> Result:
    recs: List[Rec] = []
    nosym = 0
    for row in loader.iter_rows(path):
        if row.symbolless:
            nosym += 1
        alloc_mod, biz_mod, biz_frame = parse.attribute(row.stack)
        isdp = parse.is_default_pool(row.stack)
        recs.append(Rec(row.impacting_mb, row.size_mb, row.decommitted,
                        alloc_mod, biz_mod, biz_frame,
                        parse.is_heap_path(row.stack), parse.is_mempool_path(row.stack),
                        isdp, parse.business_chain(row.stack) if isdp else ()))

    total = len(recs)
    sym_pct = (100.0 * nosym / total) if total else 0.0
    metric_name, pick, use, is_churn = _choose_metric(recs)

    res = Result(path=path, total_rows=total, symbolless_pct=sym_pct,
                 have_symbols=(sym_pct < _SYMBOL_THRESHOLD_PCT),
                 metric_name=metric_name, is_churn=is_churn, grand_mb=0.0)
    for r in use:
        mb = pick(r)
        if mb <= 0:
            continue
        res.grand_mb += mb
        res.by_module[r.alloc_mod] += mb
        res.by_biz_module[r.biz_mod] += mb
        res.by_biz_func[r.biz_mod][r.biz_frame] += mb
        if not res.have_symbols:
            continue
        if not r.is_heap:
            res.direct_mb += mb
            continue
        res.heap_mb += mb
        if r.is_mempool:
            res.pool_heap_mb += mb
            if r.is_default_pool:                 # DefaultPool subset of pool-backed
                res.dp_total_mb += mb
                res.by_dp_module[r.biz_mod] += mb
                res.by_dp_func[r.biz_mod][r.biz_frame] += mb
                if r.dp_chain:
                    _tree_insert(res.by_dp_tree.setdefault(r.biz_mod, {}), r.dp_chain, mb)
        else:
            res.nph_total_mb += mb
            res.by_nph_module[r.biz_mod] += mb
            res.by_nph_func[r.biz_mod][r.biz_frame] += mb
    return res
