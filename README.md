# Job Search Workflow

A Claude Code workflow for tailoring a resume and cover letter to each posting,
organized by job type, with a record of why each resume turned out the way it did.

## Quick start
1. Paste your full resume into `profile/master-resume.md`.
2. In Claude Code, open this repo and run: `/apply <paste posting or URL>`
3. Review the output in `applications/<date>_<company>_<role>/`.
4. After you apply: `/job-status <company> applied`

## Where things are
| Path | What it is |
|---|---|
| `profile/` | Master resume, experience bank, your preferences |
| `tracks/` | One file per job type, with what to emphasize for each |
| `applications/` | One folder per application: posting, analysis + decision log, resume, cover letter, and `originals/` with the exact files sent |
| `tracker.csv` | Index of every application and its status |
| `CLAUDE.md` | The workflow Claude follows |

## Tracks so far
- `product-management`: execution-focused / technical PM roles
- `erp-consulting`: Oracle / ERP implementation and consulting roles
- `accounting`: in-house accounting and finance-systems roles
- `asset-management`: investment operations and fund accounting

Add a new track by copying `tracks/_template.md`.

## Applications
<!-- APPLICATIONS:START -->
| Date | Company | Role | Track | Status | Fit | Posting | Materials |
|---|---|---|---|---|---|---|---|
| 2026-10-11 | Morning Consult | Product Manager | product-management | applied | 7 | [Live posting](https://jobs.ashbyhq.com/morningconsult/bafd9942-f815-4b8b-83fd-2719e3eb6a4a) · [Saved copy](applications/2026-10-11_morning-consult_product-manager/posting.md) | [Resume](applications/2026-10-11_morning-consult_product-manager/resume.md) · [Cover letter](applications/2026-10-11_morning-consult_product-manager/cover-letter.md) · [Analysis](applications/2026-10-11_morning-consult_product-manager/analysis.md) · [PDF: Casey_Hellenbrand_Product_Manager_Cover_Letter](applications/2026-10-11_morning-consult_product-manager/originals/Casey_Hellenbrand_Product_Manager_Cover_Letter.pdf) · [PDF: Casey_Hellenbrand_Resume_2026](applications/2026-10-11_morning-consult_product-manager/originals/Casey_Hellenbrand_Resume_2026.pdf) |
| 2026-09-28 | EY | FSO Business Transformation - WAM Senior Consultant | asset-management | applied | 6 | [Live posting](https://careers.ey.com/job-invite/1721086/) · [Saved copy](applications/2026-09-28_ey_wam-senior-consultant/posting.md) | [Resume](applications/2026-09-28_ey_wam-senior-consultant/resume.md) · [Cover letter](applications/2026-09-28_ey_wam-senior-consultant/cover-letter.md) · [Analysis](applications/2026-09-28_ey_wam-senior-consultant/analysis.md) · [PDF: Casey_Hellenbrand_Cover_Letter_EY_WAM](applications/2026-09-28_ey_wam-senior-consultant/originals/Casey_Hellenbrand_Cover_Letter_EY_WAM.pdf) · [PDF: Casey_Hellenbrand_Resume_2026_WAM](applications/2026-09-28_ey_wam-senior-consultant/originals/Casey_Hellenbrand_Resume_2026_WAM.pdf) |
<!-- APPLICATIONS:END -->
