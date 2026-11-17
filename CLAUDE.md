# Job Search Workflow — instructions for Claude

This repo is Casey's job-search system. Every application is a folder with a
record of **what** was sent and **why** it came out that way.

## Layout
- `profile/master-resume.md` — the full, untailored resume. Source of truth.
- `profile/experience-bank.md` — every bullet Casey could use, tagged by skill/track. Tailored resumes pull from here; never invent experience that isn't in the bank or master resume.
- `profile/preferences.md` — tone, formatting, things to always/never do.
- `tracks/<track>.md` — one file per job type (e.g. ERP consulting, accounting, asset management). Each says which titles it targets, what to lead with, keywords, and which bullets to favor.
- `applications/<YYYY-MM-DD>_<company>_<role>/` — one folder per application:
  - `posting.md` — the job posting (full text) plus the live URL, and links to the materials sent
  - `analysis.md` — fit score, keyword match, gaps, and the **decision log**
  - `resume.md` — the tailored resume (header links back to the posting)
  - `cover-letter.md` — the tailored cover letter (header links back to the posting)
  - `originals/` — the exact files submitted (PDF/DOCX), named `Casey_Hellenbrand_<Resume|Cover_Letter>_<Company>.<ext>`
- `tracker.csv` — one row per application (the index of everything).
- `templates/` — starting points for analysis, resume, and cover letter.
- `scripts/new_application.py` — creates the folder + tracker row.
- `scripts/update_status.py` — changes an application's status in the tracker.
- `scripts/build_index.py` — rebuilds the Applications table in `README.md` (runs automatically from the two scripts above).

## The workflow (run when Casey gives a posting)
1. **Classify** the posting into an existing track in `tracks/`. If none fits, propose a new track (copy `tracks/_template.md`) and ask Casey before creating it.
2. **Scaffold**: `python3 scripts/new_application.py --company "X" --role "Y" --track <track> --url "..."`. Save the posting text into `posting.md`.
3. **Analyze** (`analysis.md`, from `templates/analysis.md`):
   - Fit score 1–10 with a one-line justification
   - Must-have requirements → matched / partial / missing, citing the bullet that matches
   - Keywords from the posting to mirror, and gaps to address honestly (or leave out)
4. **Tailor the resume** (`resume.md`): start from the master resume, apply the track's emphasis, reorder and reword bullets from the experience bank. Mirror the posting's language only where it's true.
5. **Write the cover letter** (`cover-letter.md`): 3–4 short paragraphs, specific to the company and role, using the 2–3 strongest matches.
6. **Fill in the decision log** in `analysis.md` — the core of this system. Record:
   - which track was used and why
   - what was moved up, cut, or reworded, and the reason for each
   - which gaps were left unaddressed and why
7. **Save the sendable files**: export the final resume and cover letter to PDF (and DOCX if Casey wants) into `originals/`, and fill in the "File sent" links in both headers. If Casey sends back an edited final version, save that one instead; `originals/` must always match what was actually submitted.
8. Update `fit_score` in `tracker.csv`, run `python3 scripts/build_index.py`, commit and push, then give Casey a short summary: fit score, the top 3 changes, and any open questions.

## Rules
- **Everything is linked.** Every resume and cover letter links to its posting (live URL + saved copy), and every posting lists the materials sent for it. The README table links all of it. Never leave a resume or cover letter outside an application folder.
- When Casey shares materials he already sent (PDFs/DOCX) for a past application, log them the same way: originals in `originals/`, markdown copies in `resume.md` / `cover-letter.md`, and a reconstructed decision log marked as reconstructed.
- Never fabricate skills, titles, dates, numbers, or employers. If a posting wants something Casey doesn't have, say so in the analysis rather than stretching.
- Keep resumes to one page of content unless the track file says otherwise.
- When Casey corrects a draft, ask whether the correction should be saved to `profile/preferences.md` or the track file so it carries forward.
- Status values: `drafting`, `applied`, `interviewing`, `offer`, `rejected`, `withdrawn`, `skipped`.
