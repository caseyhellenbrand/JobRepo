#!/usr/bin/env python3
"""Compare Claude's last draft with Casey's final version, line by line.

Usage:
  python3 scripts/resume_diff.py applications/<folder>
    (reads resume-claude-final.txt and resume-final.txt in that folder)
  python3 scripts/resume_diff.py <claude_version.txt> <casey_version.txt>

Prints every change as CHANGED / ADDED / REMOVED with both wordings, then a count.
The count is what goes in tracker.csv `casey_edits`: fewer edits over time = the system is learning.
"""
import difflib
import sys
from pathlib import Path


def lines(path: Path) -> list[str]:
    out = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip().lstrip("•*-●◦ ").strip()
        if line:
            out.append(line)
    return out


def main() -> None:
    args = sys.argv[1:]
    if len(args) == 1:
        folder = Path(args[0])
        a, b = folder / "resume-claude-final.txt", folder / "resume-final.txt"
    elif len(args) == 2:
        a, b = Path(args[0]), Path(args[1])
    else:
        raise SystemExit(__doc__)

    old, new = lines(a), lines(b)
    sm = difflib.SequenceMatcher(a=old, b=new, autojunk=False)
    changes = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        olds, news = old[i1:i2], new[j1:j2]
        # Pair lines inside a replaced block by best similarity so rewordings show side by side
        used = set()
        for o in olds:
            best, score = None, 0.0
            for k, n in enumerate(news):
                if k in used:
                    continue
                r = difflib.SequenceMatcher(a=o, b=n).ratio()
                if r > score:
                    best, score = k, r
            if best is not None and score >= 0.5:
                used.add(best)
                changes += 1
                print(f"CHANGED ({score:.0%} similar)\n  Claude: {o}\n  Casey:  {news[best]}\n")
            else:
                changes += 1
                print(f"REMOVED\n  Claude: {o}\n")
        for k, n in enumerate(news):
            if k not in used:
                changes += 1
                print(f"ADDED\n  Casey:  {n}\n")
    print(f"TOTAL CHANGES: {changes}")


if __name__ == "__main__":
    main()
