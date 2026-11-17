#!/usr/bin/env python3
"""Convert an application's resume.md or cover-letter.md into clean HTML for
uploading as a Google Doc (Drive converts the HTML into native Docs formatting).

Strips the repo-only parts (link header, HTML comments, "as sent" notes) so the
Google Doc contains only what goes to the employer.

Usage:
  python3 scripts/to_gdoc_html.py applications/<folder>/resume.md > /tmp/resume.html
"""
import re
import sys
from pathlib import Path

import markdown

STYLE = {
    "body": "font-family:Calibri,Arial,sans-serif;font-size:10.5pt;",
    "h1": "font-family:Calibri,Arial,sans-serif;font-size:18pt;text-align:center;margin:0;",
    "h2": "font-family:Calibri,Arial,sans-serif;font-size:11pt;text-transform:uppercase;"
          "border-bottom:1px solid #000;margin:10pt 0 4pt 0;",
    "h3": "font-family:Calibri,Arial,sans-serif;font-size:10.5pt;margin:6pt 0 2pt 0;",
    "p": "font-family:Calibri,Arial,sans-serif;font-size:10.5pt;margin:0 0 6pt 0;",
    "li": "font-family:Calibri,Arial,sans-serif;font-size:10.5pt;margin:0;",
}


def clean(md: str, kind: str) -> str:
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    lines = md.splitlines()
    out, skipping_title = [], True
    for line in lines:
        # Drop the repo title line ("# Resume: X — Y"), link header, and repo notes
        if skipping_title and line.startswith("# ") and (":" in line):
            skipping_title = False
            continue
        if line.startswith(">"):
            continue
        if re.match(r"^(Original PDF|Addressed to|Sent the general)", line):
            continue
        if line.strip() == "---":
            continue
        out.append(line)
    # Markdown needs a blank line before a list that follows a paragraph line
    fixed = []
    for line in out:
        if line.startswith("- ") and fixed and fixed[-1].strip() and not fixed[-1].startswith("- "):
            fixed.append("")
        fixed.append(line)
    text = "\n".join(fixed).strip()
    if kind == "cover":
        # Cover letters get the same name + contact header as the resume
        master = (Path(__file__).resolve().parent.parent / "profile" / "master-resume.md")
        name, contact = [l for l in master.read_text().splitlines() if l.strip()][1:3]
        text = f"{name}\n{contact}\n\n{text}"
        kind = "resume"
    if kind == "resume":
        # First bold line is the name → title; next line is contact info → centered
        text = re.sub(r"^\*\*(.+?)\*\*\n(.+)$", r"# \1\n\n<p class='contact'>\2</p>", text,
                      count=1, flags=re.M)
    return text


def main() -> None:
    path = Path(sys.argv[1])
    kind = "resume" if "resume" in path.name else "cover"
    html = markdown.markdown(clean(path.read_text(), kind), extensions=["sane_lists"])
    for tag, css in STYLE.items():
        if tag != "body":
            html = re.sub(fr"<{tag}>", f'<{tag} style="{css}">', html)
    html = html.replace("<ul>", '<ul style="margin:0 0 4pt 0;">')
    html = html.replace("<p class='contact'>",
                        f'<p style="{STYLE["p"]}text-align:center;">')
    print(f'<html><body style="{STYLE["body"]}">{html}</body></html>')


if __name__ == "__main__":
    main()
