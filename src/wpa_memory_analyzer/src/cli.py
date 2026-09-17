"""CLI, invoked via wpr.py at the repo root.

    wpr.py <csv> [--out DIR] [--top N] [--func-top K]

Analyze a WPA VirtualAlloc CSV; print the report and write the report files
into DIR (default '.').
"""
import argparse
import os
import sys

import analyze as _analyze
import report as _report
from loader import ColumnError


def main(argv=None):
    p = argparse.ArgumentParser(prog="wpr_analyzer", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv", help="WPA VirtualAlloc CSV export")
    p.add_argument("--out", default=".", help="output directory for report files")
    p.add_argument("--top", type=int, default=_report.DEFAULT_TOP_N,
                   help="modules listed per view")
    p.add_argument("--func-top", type=int, default=_report.DEFAULT_FUNC_TOP,
                   help="functions listed under each business module (views 2/3)")
    p.add_argument("--expand-threshold", type=float, default=_report.DEFAULT_EXPAND_MB,
                   help="View 4: trace callers up while a bucket exceeds this many MB")
    args = p.parse_args(argv)

    if not os.path.isfile(args.csv):
        sys.exit(f"ERROR: CSV not found: {args.csv}")
    try:
        res = _analyze.analyze(args.csv)
    except ColumnError as e:
        sys.exit(f"ERROR: {e}")

    print(_report.render(res, args.top, args.func_top, args.expand_threshold))
    _report.write_outputs(res, args.out, args.top, args.func_top, args.expand_threshold)
    for fn in (_report.SUMMARY_FILENAME, _report.REPORT_FILENAME,
               _report.BY_FUNCTION_CSV, _report.BY_MODULE_CSV):
        print(f"[written] {os.path.join(args.out, fn)}")


if __name__ == "__main__":
    main()
