#!/usr/bin/env python3
"""Create an application folder from templates and add a row to tracker.csv.

Usage:
  python3 scripts/new_application.py --company "Acme" --role "ERP Consultant" \
      --track erp-consulting --url "https://..."
"""
import argparse
import csv
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRACKER = ROOT / "tracker.csv"
FIELDS = ["date", "company", "role", "track", "status", "fit_score",
          "url", "folder", "last_updated", "notes"]


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--company", required=True)
    p.add_argument("--role", required=True)
    p.add_argument("--track", required=True)
    p.add_argument("--url", default="")
    a = p.parse_args()

    tracks = {t.stem for t in (ROOT / "tracks").glob("*.md") if not t.stem.startswith("_")}
    if a.track not in tracks:
        raise SystemExit(f"Unknown track '{a.track}'. Existing: {', '.join(sorted(tracks))}")

    today = dt.date.today().isoformat()
    folder = ROOT / "applications" / f"{today}_{slug(a.company)}_{slug(a.role)}"
    if folder.exists():
        raise SystemExit(f"Already exists: {folder}")
    folder.mkdir(parents=True)

    values = {"role": a.role, "company": a.company, "track": a.track,
              "url": a.url, "date": today}
    for name in ("posting.md", "analysis.md", "resume.md", "cover-letter.md"):
        text = (ROOT / "templates" / name).read_text()
        (folder / name).write_text(text.format_map(values))
    (folder / "originals").mkdir()
    (folder / "originals" / ".gitkeep").touch()

    with TRACKER.open("a", newline="") as f:
        csv.DictWriter(f, fieldnames=FIELDS).writerow({
            "date": today, "company": a.company, "role": a.role, "track": a.track,
            "status": "drafting", "fit_score": "", "url": a.url,
            "folder": folder.relative_to(ROOT).as_posix(),
            "last_updated": today, "notes": ""})

    subprocess.run([sys.executable, str(ROOT / "scripts" / "build_index.py")], check=True)
    print(folder)


if __name__ == "__main__":
    main()
