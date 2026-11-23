---
description: Casey's resume is final — compare his version with Claude's last draft and turn his edits into improvements (pass the company)
---

Run phase F of `/apply` in `CLAUDE.md` for this application: $ARGUMENTS

1. Find the application folder and its Google Doc (link in `resume.md`). Export the doc as plain text
   to `resume-final.txt`.
2. Run `python3 scripts/resume_diff.py applications/<folder>`.
3. Sort every change by the Resume Quality Rubric's learning rules, show the list, and ask Casey (one
   question batch) which are standing rules.
4. Apply only what he approves; fill "What Claude learned" in `analysis.md`; set `casey_edits` and
   `review_rounds` in `tracker.csv`; paste the final text into `resume.md`; build the index; commit; push.
