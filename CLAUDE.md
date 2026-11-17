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

Read the three Google Docs with Drive `read_file_content` (`includeComments: true`).
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

## `/apply` — run Casey's 9-step process from the Project Instructions doc
Follow that doc exactly. This file only adds the repo bookkeeping and the Google Docs mechanics.

1. **Role analysis.** Fetch the full posting. Scaffold the repo record:
   `python3 scripts/new_application.py --company "X" --role "Y" --track <track> --url "..."`
   (pick the job-type track in `tracks/`; ask before creating a new one). Save the posting text
   in `posting.md` and write the Role Requirements Profile into `analysis.md`.
2. **Knowledge Base audit.** Coverage map (Strong / Partial / None) against the live Bullet Bank,
   into `analysis.md`. Call out any [STILL OPEN] bullet that maps to a must-have.
3. **Prioritization.** Rank roles and engagements; state the reasoning in `analysis.md`.
4. **Bullet proposal.** Show Casey the proposed Baker Tilly bullets in priority order, with reasons.
5. **Gap-check question.**
6. **STOP.** Do not build any document until Casey confirms the bullets. Commit the repo record
   with status `drafting` so the analysis is saved.
7. **Build the resume as a Google Doc:**
   - Download the template .docx and upload it with Drive `create_file`
     (`contentMimeType` = the .docx MIME type, `parentId` = the company's folder under 2026 Applications) so it converts to a
     Google Doc. Name it `Casey-Hellenbrand-[Job Role]`.
   - `read_doc`, then replace only the Baker Tilly bullets. The template's `Text` paragraphs are
     placeholders: delete the placeholder text and insert the bullets separated by `\n`, which keeps
     the bullet formatting. Replace or remove any pre-filled Baker Tilly bullet that wasn't chosen.
     Edit from the highest index to the lowest, guarded by `requiredRevisionId`.
   - Never touch UW Credit Union, Badger Consulting, Education, or Skills & Certifications.
     The Summary changes only as the Bullet Bank's Summary Bank allows (fixed anchor, tailored
     second sentence).
   - Export to PDF and check it: one page, no leftover `Text` placeholders.
8. **Cover letter (if requested)**, following the Playbook: run its intake questions, use the
   four-paragraph base structure at 300–400 words, then do the accuracy pass. Create it as a Google
   Doc in the company's folder under 2026 Applications, named `Casey Hellenbrand - [Role] - Cover Letter`.
9. **Review round** with Casey, editing the same Google Docs in place (same links).
10. **Record and feed back.**
    - Fill in the decision log in `analysis.md`.
    - Put the Google Doc links in the headers of `resume.md` and `cover-letter.md`, and paste in
      the final text as a snapshot.
    - Update `tracker.csv`, run `python3 scripts/build_index.py`, commit and push.
    - Propose additions to the Bullet Bank (new phrasing, confirmed numbers, the Shipped Versions
      Log entry). **Edit the Bullet Bank only after Casey approves the changes.**
      Its open items (number standardization, healthcare engagement, Badger decision) stay there.

## Where Claude stops and asks (never skipped)
1. **Before analysis:** if the posting is behind a login or unclear, ask for the text.
2. **New job type:** ask before creating a new track.
3. **Must-have mapped to a [STILL OPEN] bullet or an unconfirmed number:** ask for the real value.
4. **Gap check (step 5):** ask what is missing or could be reframed.
5. **Sign-off (step 6):** nothing is built until Casey approves the bullets.
6. **Cover letter intake:** the Playbook's intake questions, including "why this company" in his words.
7. **Bullet Bank changes:** proposed, applied only after approval.
Ask with the question tool (multiple choice + free text) where available, so questions are quick to answer on a phone.

## Learning loop (how it adapts from posting to posting)
- Every run reads the **live** Bullet Bank, Summary Bank, Shipped Versions Log and the track's
  "Notes from past applications", so approved phrasing from earlier runs is reused.
- Every run ends with a decision log and Bullet Bank proposals (step 10).
- When an outcome arrives (`/job-status <company> interviewing|rejected|offer`), add one line to the
  track's "Notes from past applications": what was sent, the framing used, and the result.
- `/job-review` summarizes patterns across applications (which framing and bullets got responses, by job type)
  and proposes changes to the tracks, Bullet Bank or Project Instructions.

## After submission
- Casey runs `/job-status <company> applied`.
- If he edited the Google Docs before submitting, the docs are already the final versions. Refresh
  the text snapshots in `resume.md` / `cover-letter.md` from them.
- Optionally save the submitted PDF in `originals/`.

## Repo layout
- `applications/<YYYY-MM-DD>_<company>_<role>/`: `posting.md`, `analysis.md` (requirements
  profile, coverage map, prioritization, decision log), `resume.md` and `cover-letter.md`
  (Google Doc link plus final-text snapshot), `interviews.md` (dates, interviewers, questions,
  feedback, follow-ups sent), `originals/` (submitted PDFs, optional)
- `tracks/`: job types, used to group applications and to record what worked per type. These are
  not a bullet source; bullets come only from the Bullet Bank.
- `tracker.csv` and the README Applications table (`scripts/build_index.py`)
- `scripts/new_application.py`, `scripts/update_status.py`, `scripts/build_index.py`

## Rules
- Everything in the Project Instructions "Tone and honesty" section and the Playbook rules applies.
  Never fabricate or estimate a metric; flag it as [STILL OPEN].
- Every resume and cover letter is linked to its posting, and every posting links its materials.
- Never trash or overwrite Casey's Drive files without asking. Edits to an existing doc go in place.
- Status values: `drafting`, `applied`, `interviewing`, `offer`, `rejected`, `withdrawn`, `skipped`.
