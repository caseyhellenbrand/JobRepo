#!/usr/bin/env python3
"""Update an application's status (and optionally fit score / notes) in tracker.csv.

Usage:
  python3 scripts/update_status.py <match> <status> [--fit 7] [--note "..."]
  <match> is matched case-insensitively against company, role, or folder.
"""
import argparse
import csv
import datetime as dt
import subprocess
import sys
from pathlib import Path

TRACKER = Path(__file__).resolve().parent.parent / "tracker.csv"
STATUSES = {"drafting", "applied", "interviewing", "offer",
            "rejected", "withdrawn", "skipped"}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("match")
    p.add_argument("status")
    p.add_argument("--fit")
    p.add_argument("--note")
    a = p.parse_args()
    if a.status not in STATUSES:
        raise SystemExit(f"Status must be one of: {', '.join(sorted(STATUSES))}")

    with TRACKER.open(newline="") as f:
        reader = csv.DictReader(f)
        fields, rows = reader.fieldnames, list(reader)

    needle = a.match.lower()
    hits = [r for r in rows
            if needle in f"{r['company']} {r['role']} {r['folder']}".lower()]
    if len(hits) != 1:
        found = "; ".join(r["folder"] for r in hits) or "none"
        raise SystemExit(f"Need exactly one match for '{a.match}', found: {found}")

    row = hits[0]
    row["status"] = a.status
    row["last_updated"] = dt.date.today().isoformat()
    if a.fit:
        row["fit_score"] = a.fit
    if a.note:
        row["notes"] = (row["notes"] + " | " if row["notes"] else "") + a.note

    with TRACKER.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    subprocess.run([sys.executable, str(TRACKER.parent / "scripts" / "build_index.py")], check=True)
    print(f"{row['company']} — {row['role']}: {a.status}")


if __name__ == "__main__":
    main()
