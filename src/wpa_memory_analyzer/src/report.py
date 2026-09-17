"""Render a Result to text and write the report files. No analysis here."""
import csv
import os

from analyze import Result

# argparse defaults reference these, keeping a single source of truth.
DEFAULT_TOP_N = 25       # modules listed per view
DEFAULT_FUNC_TOP = 20    # functions listed per module (views 2/3/4)
DEFAULT_EXPAND_MB = 100.0 # View 4: trace callers up while a bucket exceeds this

_FUNC_NAME_WIDTH = 84    # function-name column; longer is truncated with "..."
_MIN_MB = 0.1            # report floor: rows below this are noise, omitted
_MIN_FUNC_MB = 0.05      # function floor (anything that rounds to 0.0 MB)
_MAX_TREE_DEPTH = 12     # View 4 caller-tree depth guard
_CHAIN_LINES = 5         # caller frames printed (one per line) under a folded chain

SUMMARY_FILENAME = "wpr_summary.txt"     # one-screen summary
REPORT_FILENAME = "wpr_report.txt"       # multi-view top-N human report
BY_FUNCTION_CSV = "wpr_by_function.csv"  # full machine-readable (view,module,function,MB)
BY_MODULE_CSV = "wpr_by_module.csv"      # simple machine-readable (module,MB)


def _pct(mb: float, grand: float) -> float:
    return mb / grand * 100.0


def _func_only(frame: str) -> str:
    return frame.split("!", 1)[1] if "!" in frame else frame


def _short(s: str, width: int = _FUNC_NAME_WIDTH) -> str:
    return s if len(s) <= width else s[:width - 3] + "..."


def _top_modules(by_module, top_n):
    """Modules sorted desc, capped at top_n, dropping the sub-_MIN_MB tail."""
    out = []
    for mod, mb in sorted(by_module.items(), key=lambda x: -x[1]):
        if mb < _MIN_MB or len(out) >= top_n:
            break
        out.append((mod, mb))
    return out


def _emit_module_func_tree(a, by_module, by_func, top_n, func_top, grand):
    """"module total + its top functions"; shared by views 2 and 3. A module
    with a single non-trivial function prints inline instead of as a sub-tree."""
    for mod, mb in _top_modules(by_module, top_n):
        ranked = [(f, v) for f, v in sorted(by_func.get(mod, {}).items(), key=lambda x: -x[1])
                  if v >= _MIN_FUNC_MB]
        head = f"    {mod:40s} {mb:12,.1f} MB  ({_pct(mb, grand):5.1f}%)"
        if len(ranked) <= 1:
            a(head + (f"  {_short(_func_only(ranked[0][0]), 60)}" if ranked else ""))
            continue
        a("")
        a(head)
        for frame, fmb in ranked[:func_top]:
            a(f"        {fmb:12,.1f} MB  {_short(_func_only(frame))}")
        if len(ranked) > func_top:
            rest = sum(v for _, v in ranked[func_top:])
            a(f"        {rest:12,.1f} MB  ... +{len(ranked) - func_top} more")


def _emit_node(a, frame, node, func_top, expand_mb, depth, indent):
    """Render one caller-tree node. Fold a single-child chain into one line; at a
    branch (or once a bucket drops <= expand_mb) stop and list the callers."""
    chain = [frame]
    cur = node
    d = depth
    while cur["mb"] > expand_mb and len(cur["kids"]) == 1 and d < _MAX_TREE_DEPTH:
        (cf, ck), = cur["kids"].items()
        chain.append(cf)
        cur = ck
        d += 1
    a(f"{indent}{node['mb']:12,.1f} MB  {_func_only(chain[0])}")
    tail = chain[1:]
    cont = indent + " " * 14          # align caller lines under the function name
    for f in tail[:_CHAIN_LINES]:
        a(f"{cont}<- {_func_only(f)}")
    if len(tail) > _CHAIN_LINES:
        a(f"{cont}<- ...(+{len(tail) - _CHAIN_LINES} more)")

    if cur["mb"] > expand_mb and len(cur["kids"]) > 1 and d < _MAX_TREE_DEPTH:
        kids = sorted(cur["kids"].items(), key=lambda kv: -kv[1]["mb"])
        kshown = 0.0
        n = 0
        for kf, kn in kids:
            if kn["mb"] < _MIN_MB or n >= func_top:
                break
            n += 1
            kshown += kn["mb"]
            _emit_node(a, kf, kn, func_top, expand_mb, d + 1, indent + "    ")
        resid = cur["mb"] - kshown
        if resid > expand_mb:
            a(f"{indent}    {resid:12,.1f} MB  (other callers / self)")


def _emit_dp_tree(a, forest, top_n, func_top, expand_mb):
    """View 4 forest: caller trees rooted at each deepest business frame."""
    roots = sorted(forest.items(), key=lambda kv: -kv[1]["mb"])
    n = 0
    for frame, node in roots:
        if node["mb"] < _MIN_MB or n >= func_top:
            break
        n += 1
        _emit_node(a, frame, node, func_top, expand_mb, 0, "        ")


def render(res: Result, top_n: int = DEFAULT_TOP_N, func_top: int = DEFAULT_FUNC_TOP,
           expand_mb: float = DEFAULT_EXPAND_MB) -> str:
    g = res.grand_mb or 1.0
    L = []
    a = L.append
    a("==================== WPR VirtualAlloc analysis ====================")
    a(f"  input        : {os.path.abspath(res.path)}")
    a(f"  data rows    : {res.total_rows}")
    a(f"  size metric  : {res.metric_name}")
    a(f"  grand total  : {res.grand_mb:,.1f} MB")
    a(f"  symbols      : {'present' if res.have_symbols else 'DISABLED'} "
      f"({res.symbolless_pct:.0f}% rows symbol-less)")
    if res.is_churn:
        a("  !! WARNING: Impacting=0 and every alloc has a Decommit Time.")
        a("  !! This export is the commit-LIFETIMES view = allocation CHURN,")
        a("  !! NOT the resident footprint. Re-export with Impacting populated")
        a("  !! (select an impact time in WPA) or with symbols loaded. See usage.md.")

    # View 1: allocator-level owning module (no per-function tree).
    a("")
    a("  ==== VIEW 1: by direct-allocator module (deepest non-system frame) ====")
    a("  (where bytes are physically allocated)")
    for mod, mb in _top_modules(res.by_module, top_n):
        a(f"    {mod:40s} {mb:12,.1f} MB  ({_pct(mb, g):5.1f}%)")

    # View 2: business caller module -> function.
    a("")
    a("  ==== VIEW 2: by business caller (allocator/container glue skipped) ====")
    a("  (which engine code asked for the memory)")
    _emit_module_func_tree(a, res.by_biz_module, res.by_biz_func, top_n, func_top, g)

    # View 3: NON-POOL heap by business caller (needs symbols).
    if res.have_symbols:
        a("")
        a("  ==== VIEW 3: NON-POOL heap (direct new/malloc/STL, bypassed mempool) ====")
        a(f"  non-pool heap total: {res.nph_total_mb:,.1f} MB  "
          f"({_pct(res.nph_total_mb, g):.1f}% of grand)")
        _emit_module_func_tree(a, res.by_nph_module, res.by_nph_func, top_n, func_top, g)

    # View 4: DefaultPool (catch-all pool) by business caller (needs symbols).
    if res.have_symbols and res.dp_total_mb > 0:
        a("")
        a("  ==== VIEW 4: DefaultPool (catch-all pool) by business caller ====")
        a(f"  DefaultPool total: {res.dp_total_mb:,.1f} MB  "
          f"({_pct(res.dp_total_mb, g):.1f}% of grand);  "
          f"callers traced up while a bucket > {expand_mb:,.0f} MB  (a <- b: b calls a)")
        for mod, mb in _top_modules(res.by_dp_module, top_n):
            a("")
            a(f"    {mod:40s} {mb:12,.1f} MB  ({_pct(mb, g):5.1f}%)")
            _emit_dp_tree(a, res.by_dp_tree.get(mod, {}), top_n, func_top, expand_mb)

    # alloc-path summary.
    if res.have_symbols:
        named = res.pool_heap_mb - res.dp_total_mb     # pool-backed minus DefaultPool
        a("")
        a("  ---- alloc path (context) ----")
        a(f"    heap segment VA : {res.heap_mb:12,.1f} MB  ({_pct(res.heap_mb, g):5.1f}%)")
        a(f"      - pool-backed : {res.pool_heap_mb:12,.1f} MB  "
          f"(DefaultPool {res.dp_total_mb:,.1f} + named pools {named:,.1f})")
        a(f"      - non-pool    : {res.nph_total_mb:12,.1f} MB")
        a(f"    direct VA       : {res.direct_mb:12,.1f} MB  ({_pct(res.direct_mb, g):5.1f}%)")
    else:
        a("")
        a("  (heap-vs-direct path needs symbols; skipped -- see usage.md)")
    a("===================================================================")
    return "\n".join(L)


def _flatten_funcs(by_func) -> dict:
    """Collapse {module: {frame: mb}} into a global {func: mb} across modules."""
    out = {}
    for fd in by_func.values():
        for frame, mb in fd.items():
            f = _func_only(frame)
            out[f] = out.get(f, 0.0) + mb
    return out


def render_summary(res: Result, top: int = 5) -> str:
    """One-screen summary: total, heap/direct split, and the top-N of each view."""
    g = res.grand_mb or 1.0

    def topline(d, n, maxlen=0):
        items = sorted(d.items(), key=lambda x: -x[1])[:n]
        def short(s):
            return s if (not maxlen or len(s) <= maxlen) else s[:maxlen - 3] + "..."
        return "  ".join(f"{short(k)} {v:,.0f}" for k, v in items) or "(none)"

    L = []
    a = L.append
    a("==================== WPR Memory Summary ====================")
    a(f"  input   : {os.path.abspath(res.path)}")
    a(f"  rows    : {res.total_rows}    metric: {res.metric_name}")
    a(f"  TOTAL   : {res.grand_mb:,.1f} MB")
    if res.is_churn:
        a("  !! CHURN data (not net-resident) -- re-export with Impacting. See usage.md.")
    if res.have_symbols:
        a(f"  heap VA : {res.heap_mb:,.0f} MB ({_pct(res.heap_mb, g):.0f}%)  "
          f"[pool {res.pool_heap_mb:,.0f} (DefaultPool {res.dp_total_mb:,.0f}) "
          f"/ non-pool {res.nph_total_mb:,.0f}]")
        a(f"  direct  : {res.direct_mb:,.0f} MB ({_pct(res.direct_mb, g):.0f}%)")
    a("")
    a(f"  top allocator dll   : {topline(res.by_module, top)}")
    a(f"  top business module : {topline(res.by_biz_module, top)}")
    a(f"  top business funcs  : {topline(_flatten_funcs(res.by_biz_func), top, maxlen=44)}")
    if res.have_symbols:
        a(f"  top non-pool source : {topline(_flatten_funcs(res.by_nph_func), top, maxlen=44)}")
        a(f"  top DefaultPool src : {topline(_flatten_funcs(res.by_dp_func), top, maxlen=44)}")
    a("============================================================")
    return "\n".join(L)


def write_outputs(res: Result, out_dir: str,
                  top_n: int = DEFAULT_TOP_N, func_top: int = DEFAULT_FUNC_TOP,
                  expand_mb: float = DEFAULT_EXPAND_MB) -> None:
    """Write 4 artifacts into out_dir:
       wpr_summary.txt      -- one-screen summary
       wpr_report.txt       -- multi-view top-N human report
       wpr_by_function.csv  -- FULL machine-readable data (view,module,function,MB)
       wpr_by_module.csv    -- simple machine-readable (module,MB)
    """
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, SUMMARY_FILENAME), "w", encoding="utf-8") as f:
        f.write(render_summary(res) + "\n")

    with open(os.path.join(out_dir, REPORT_FILENAME), "w", encoding="utf-8") as f:
        f.write(render(res, top_n, func_top, expand_mb) + "\n")

    # Full, un-truncated data -- every view / module / function. Pivot in Excel.
    with open(os.path.join(out_dir, BY_FUNCTION_CSV), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["view", "module", "function", "MB"])
        for mod, mb in sorted(res.by_module.items(), key=lambda x: -x[1]):
            w.writerow(["allocator", mod, "", f"{mb:.3f}"])
        for mod, fd in res.by_biz_func.items():
            for frame, mb in sorted(fd.items(), key=lambda x: -x[1]):
                w.writerow(["business", mod, _func_only(frame), f"{mb:.3f}"])
        for mod, fd in res.by_nph_func.items():
            for frame, mb in sorted(fd.items(), key=lambda x: -x[1]):
                w.writerow(["nonpool", mod, _func_only(frame), f"{mb:.3f}"])
        for mod, fd in res.by_dp_func.items():
            for frame, mb in sorted(fd.items(), key=lambda x: -x[1]):
                w.writerow(["defaultpool", mod, _func_only(frame), f"{mb:.3f}"])

    with open(os.path.join(out_dir, BY_MODULE_CSV), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["module", "MB"])
        for mod, mb in sorted(res.by_module.items(), key=lambda x: -x[1]):
            w.writerow([mod, f"{mb:.3f}"])
