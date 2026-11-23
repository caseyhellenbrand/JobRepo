# Job Search Workflow — instructions for Claude

This repo is Casey's job-search **record**: one folder per application holding the
posting, the analysis, the decision log, and links to the Google Docs that were sent.

**Casey's Google Drive is the source of truth for content and process.** Read these
at the start of every `/apply` run. Never work from chat memory or from copies in this
repo; the Drive versions may have changed.

## Source-of-truth docs (Google Drive)
| What | File | ID |
|---|---|---|
| Process (9 steps) | Project Instructions — Job and Resume Search | `1BhYRO5zRn5LlrhA77Ds-o1w3K-82IkdwtA7-1y2HSxg` |
| Bullets, tags, lessons, shipped log | Baker Tilly Resume Bullet Bank — Master Reference | `1GjSLQmAVfv8uzOobVBdQVlEV6TKCfcbIWWxr2DmaM_0` |
| Cover letter structure and rules | Cover Letter Playbook: Base Template and Process | `1Oj-tHmUJt0rvvy941r9UZY9MYEoxFgSoGcmlKLKOUDY` |
| Resume template (.docx) | Template - Casey Hellenbrand - Resume - 2026.docx | `19YerE0difcOGITi-THIMy9OHQsx_L4pm` |
| Review standard (17 checks, rounds, learning rules) | Resume Quality Rubric | `1JQOWt1ZUWNynvn7oW0HJmMCFbMWDNly6atWncsupi5U` |

Read the four Google Docs with Drive `read_file_content` (`includeComments: true`).
If a file has moved or been renamed, search the Knowledge Base folder by title.

## Drive folders
| Folder | ID | Used for |
|---|---|---|
| Claude - Job and Resume 2026 | `1T87LI-jUTz7B1E12KdLLOGjMjqvH-8ES` | parent |
| Knowledge Base | `18G5CLJnnU6BsPUvCVVRyu--gccfpHJLI` | the source docs above |
| 2026 Applications | `1ejQxfpJFotUXdgqQLBXl7gDDY-KKUjUY` | **one folder per company; finished resume + cover letter go here** |
| 2026 Applications / EY | `1GQyZVeFh4LSvpnYOvCUls2UVE3gV875V` | |
| 2026 Applications / Morning Consult | `10pVXvzc3l4fLEbZ90bSfx583Cw9_m534` | |
| 2026 Applications / Huron | `1arTWQzyw86qjJOOIdFByRyA1gNho5aVd` | |
| Position Resumes / Cover Letters | `1dHldth7olwMZotzF_Ra4whF-yDPdxm6Z` / `1-EoIQmWWyyp-Mkuvi6N6oK4esRC-niLr` | archive of earlier finals only |

New company → create its folder under 2026 Applications and add it to this table.
The resume template in Drive is the only template. If Casey says a newer copy exists elsewhere
(e.g. the old Claude Project files), ask him to upload it over the Drive one first.

## `/apply` — seven phases
Casey's Project Instructions (Drive) define the tailoring logic; the Resume Quality Rubric (Drive)
defines the review standard and the learning rules. This section is the order of work plus the
repo and Google Docs mechanics. Read all four Drive docs fresh at the start of every run.

### A. Intake: ask everything up front, once
Fetch the posting (if it's behind a login, ask for the text). Then ask, in ONE question batch:
- Which job type (suggest one from `tracks/`; a new type needs Casey's OK)
- Why this company and role, in his words, even rough
- Anything to emphasize or avoid; any contact or referral there
- Cover letter needed? Deadline?
Scaffold: `python3 scripts/new_application.py --company "X" --role "Y" --track <track> --url "..."`.
Save the full posting text in `posting.md` and the answers under "Intake" in `analysis.md`.

### B. Analysis (Project Instructions steps 1-3)
Role Requirements Profile → coverage map against the live Bullet Bank → prioritization, plus
the job type's "Notes from past applications" and the Shipped Versions Log for similar roles.
All into `analysis.md`, with a fit score.

### C. Proposal and questions, then STOP
Show Casey, in one message: fit score; the proposed Baker Tilly bullets in order, each with the
requirement it serves; the proposed summary second sentence; terms mirrored and left out; then
the questions: the gap check, any [STILL OPEN] item or unconfirmed number tied to a must-have, and
anything missing. **Build nothing until he approves.** Commit the record as `drafting`.

### D. Build, then Claude's review rounds (before Casey sees a draft)
1. **Round 1, build:** convert the Drive template .docx into a Google Doc in the company's folder
   under 2026 Applications, named `Casey-Hellenbrand-[Job Role]`. Replace only the Baker Tilly
   bullets (the `Text` placeholders and pre-filled bullets) and the summary second sentence.
   Delete-then-insert with `\n` between bullets keeps the formatting. Edit from the highest index
   down, guarded by `requiredRevisionId`.
2. **Round 2, rubric:** export the doc as PDF, score all 17 rubric checks Pass/Fix, revise every Fix
   in the same doc. Repeat until all Pass, or only Fixes that need Casey remain.
3. **Round 3, fresh eyes:** if the Agent tool is available, give a sub-agent ONLY the posting text,
   the exported resume text and the rubric's section D; ask it to review as this role's hiring
   manager. Otherwise reread it yourself as that skeptic. Revise.
4. Save the scorecard per round in `analysis.md`. Export the doc as plain text to
   `resume-claude-final.txt`; this is the baseline Casey's edits are compared against.
Cover letter (if requested): same rounds, following the Playbook (intake, four paragraphs,
300-400 words, accuracy pass), as a Google Doc in the same company folder.

### E. Casey's review
Send: the Google Doc link(s), the final scorecard, the three biggest tailoring choices, and any open
questions. Casey edits the doc directly or tells Claude what to change; Claude edits the SAME doc
(same link). Repeat until he says it's final.

### F. Learn from his edits (when he says final, or runs `/resume-learn`)
1. Export the final doc as plain text to `resume-final.txt`.
2. `python3 scripts/resume_diff.py applications/<folder>` lists every change.
3. Sort each change per the rubric: accuracy fix · phrasing preference · emphasis/selection ·
   rubric gap · one-off. Show the list and ask which are standing rules (one question batch).
4. Apply only what he approves: Bullet Bank (accuracy, preferred phrasing, Lessons, Shipped Versions
   Log entry), the job type's notes in `tracks/`, the rubric (new/changed check), Project Instructions.
5. Record the change count in `tracker.csv` → `casey_edits`, and rounds in `review_rounds`.

### G. Track
Decision log and "What Claude learned" in `analysis.md`; final text in `resume.md` with the Google
Doc link; `python3 scripts/build_index.py`; commit and push. The application is now part of what the
next run reads.

## Where Claude stops and asks (never skipped)
1. Intake (phase A), in one batch.
2. A new job type.
3. A must-have that depends on a [STILL OPEN] bullet or an unconfirmed number.
4. Sign-off on bullets and summary (phase C): nothing is built before it.
5. Rubric Fixes that only Casey can resolve (phase D).
6. Standing rule or one-off, for each non-trivial edit (phase F).
7. Any change to a Drive doc: proposed first, applied only after approval.
Ask with the question tool (multiple choice + free text) where available, so it's quick on a phone.

## Learning loop (how it adapts from posting to posting)
- Every run reads the live Bullet Bank, Summary Bank, Shipped Versions Log, rubric, and the job
  type's notes, so approved wording and lessons from earlier runs are reused.
- Every run ends with phase F: Casey's edits become Bullet Bank wording, job-type notes or rubric
  checks, once he approves them.
- `casey_edits` in the tracker is the scoreboard: if drafts are improving, it falls over time.
- Outcomes (`/job-status ... interviewing|rejected|offer`) add a line to the job type's notes.
- `/job-review` looks across applications for patterns and proposes changes.

## After submission
- Casey runs `/job-status <company> applied`.
- If he edited the Google Docs before submitting, the docs are already the final versions. Refresh
  the text snapshots in `resume.md` / `cover-letter.md` from them.
- Optionally save the submitted PDF in `originals/`.

## Repo layout
- `applications/<YYYY-MM-DD>_<company>_<role>/`: `posting.md`, `analysis.md` (requirements
  profile, coverage map, prioritization, decision log), `resume.md` and `cover-letter.md`
  (Google Doc link plus final-text snapshot), `interviews.md` (dates, interviewers, questions,
  feedback, follow-ups sent), `resume-claude-final.txt` + `resume-final.txt` (Claude's last draft and
  Casey's final, for the edit comparison), `originals/` (submitted PDFs, optional)
- `tracks/`: job types, used to group applications and to record what worked per type. These are
  not a bullet source; bullets come only from the Bullet Bank.
- `tracker.csv` and the README Applications table (`scripts/build_index.py`)
- `scripts/new_application.py`, `scripts/update_status.py`, `scripts/build_index.py`,
  `scripts/resume_diff.py`
- Commands: `/apply`, `/job-triage`, `/job-status`, `/resume-learn`, `/job-review`

## Rules
- Everything in the Project Instructions "Tone and honesty" section and the Playbook rules applies.
  Never fabricate or estimate a metric; flag it as [STILL OPEN].
- Every resume and cover letter is linked to its posting, and every posting links its materials.
- Never trash or overwrite Casey's Drive files without asking. Edits to an existing doc go in place.
- Status values: `drafting`, `applied`, `interviewing`, `offer`, `rejected`, `withdrawn`, `skipped`.
