#!/usr/bin/env python3
"""Rebuild the Applications table in README.md from tracker.csv.

Each row links the job posting, the application folder, and every resume and
cover letter saved for it (markdown versions plus the files actually sent in
originals/). Run after adding or updating an application:
  python3 scripts/build_index.py
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
START, END = "<!-- APPLICATIONS:START -->", "<!-- APPLICATIONS:END -->"


def links_for(folder: Path) -> str:
    out = []
    for name, label in (("resume.md", "Resume"), ("cover-letter.md", "Cover letter"),
                        ("analysis.md", "Analysis")):
        if (folder / name).exists():
            out.append(f"[{label}]({(folder / name).relative_to(ROOT).as_posix()})")
    originals = folder / "originals"
    if originals.exists():
        for f in sorted(originals.iterdir()):
            if f.is_file():
                out.append(f"[{f.suffix.lstrip('.').upper()}: {f.stem}]"
                           f"({f.relative_to(ROOT).as_posix().replace(' ', '%20')})")
    return " · ".join(out)


def main() -> None:
    with (ROOT / "tracker.csv").open(newline="") as f:
        rows = sorted(csv.DictReader(f), key=lambda r: r["date"], reverse=True)

    lines = ["| Date | Company | Role | Track | Status | Fit | Posting | Materials |",
             "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        folder = ROOT / r["folder"]
        posting = f"[Live posting]({r['url']})" if r["url"] else ""
        if (folder / "posting.md").exists():
            posting += f"{' · ' if posting else ''}[Saved copy]({r['folder']}/posting.md)"
        lines.append(f"| {r['date']} | {r['company']} | {r['role']} | {r['track']} | "
                     f"{r['status']} | {r['fit_score']} | {posting} | {links_for(folder)} |")
    table = "\n".join(lines)

    text = README.read_text()
    if START not in text:
        text += f"\n## Applications\n{START}\n{END}\n"
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    README.write_text(f"{head}{START}\n{table}\n{END}{tail}")
    print(f"Indexed {len(rows)} application(s)")


if __name__ == "__main__":
    main()
