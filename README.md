# Job Search Workflow

A Claude Code workflow for tailoring a resume and cover letter to each posting,
organized by job type, with a record of why each resume turned out the way it did.

## Quick start
1. In Claude Code, open this repo and run `/apply <posting URL or text>`.
2. Claude follows your 9-step process from the Project Instructions in Google Drive, and stops at step 6 for your sign-off.
3. You get a Google Doc resume, built from your template, in Drive → Position Resumes (and a cover letter in Cover Letters, if you want one).
4. After you apply, run `/job-status <company> applied`.

**Source of truth:** your Google Drive "Claude - Job and Resume 2026" folder (Project Instructions, Bullet Bank, Cover Letter Playbook, resume template). This repo is the record of each application.

## Where things are
| Path | What it is |
|---|---|
| `tracks/` | One file per job type: what to emphasize and what has worked |
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
| Date | Company | Role | Track | Status | Fit | Your edits | Posting | Materials |
|---|---|---|---|---|---|---|---|---|
| 2026-11-17 | Huron | Digital Consulting Sr. Associate, Oracle Cloud Core Financials | erp-consulting | applied |  |  | [Saved copy](applications/2026-11-17_huron_digital-consulting-sr-associate-oracle-cloud-core-financials/posting.md) | [Resume](applications/2026-11-17_huron_digital-consulting-sr-associate-oracle-cloud-core-financials/resume.md) · [Cover letter](applications/2026-11-17_huron_digital-consulting-sr-associate-oracle-cloud-core-financials/cover-letter.md) · [Analysis](applications/2026-11-17_huron_digital-consulting-sr-associate-oracle-cloud-core-financials/analysis.md) · [: .gitkeep](applications/2026-11-17_huron_digital-consulting-sr-associate-oracle-cloud-core-financials/originals/.gitkeep) |
| 2026-11-17 | Huron | Associate-Sr. Associate, Oracle EPM | erp-consulting | applied |  |  | [Saved copy](applications/2026-11-17_huron_associate-sr-associate-oracle-epm/posting.md) | [Resume](applications/2026-11-17_huron_associate-sr-associate-oracle-epm/resume.md) · [Cover letter](applications/2026-11-17_huron_associate-sr-associate-oracle-epm/cover-letter.md) · [Analysis](applications/2026-11-17_huron_associate-sr-associate-oracle-epm/analysis.md) · [: .gitkeep](applications/2026-11-17_huron_associate-sr-associate-oracle-epm/originals/.gitkeep) |
| 2026-10-23 | EY | FSO Business Transformation - WAM Asset Senior Consultant (Req 1721086) | asset-management | interviewing | 6 |  | [Live posting](https://careers.ey.com/job-invite/1721086/) · [Saved copy](applications/2026-10-23_ey_wam-asset-senior-consultant/posting.md) | [Analysis](applications/2026-10-23_ey_wam-asset-senior-consultant/analysis.md) · [: .gitkeep](applications/2026-10-23_ey_wam-asset-senior-consultant/originals/.gitkeep) |
| 2026-10-11 | Morning Consult | Product Manager | product-management | applied | 7 |  | [Live posting](https://jobs.ashbyhq.com/morningconsult/bafd9942-f815-4b8b-83fd-2719e3eb6a4a) · [Saved copy](applications/2026-10-11_morning-consult_product-manager/posting.md) | [Resume](applications/2026-10-11_morning-consult_product-manager/resume.md) · [Cover letter](applications/2026-10-11_morning-consult_product-manager/cover-letter.md) · [Analysis](applications/2026-10-11_morning-consult_product-manager/analysis.md) · [PDF: Casey_Hellenbrand_Product_Manager_Cover_Letter](applications/2026-10-11_morning-consult_product-manager/originals/Casey_Hellenbrand_Product_Manager_Cover_Letter.pdf) · [PDF: Casey_Hellenbrand_Resume_2026](applications/2026-10-11_morning-consult_product-manager/originals/Casey_Hellenbrand_Resume_2026.pdf) |
| 2026-09-28 | EY | Business Transformation Senior - WAM Wealth Management (Req 1726266) | asset-management | withdrawn | 6 |  | [Live posting](https://careers.ey.com/job-invite/1721086/) · [Saved copy](applications/2026-09-28_ey_wam-wealth-senior/posting.md) | [Resume](applications/2026-09-28_ey_wam-wealth-senior/resume.md) · [Cover letter](applications/2026-09-28_ey_wam-wealth-senior/cover-letter.md) · [Analysis](applications/2026-09-28_ey_wam-wealth-senior/analysis.md) · [PDF: Casey_Hellenbrand_Cover_Letter_EY_WAM](applications/2026-09-28_ey_wam-wealth-senior/originals/Casey_Hellenbrand_Cover_Letter_EY_WAM.pdf) · [PDF: Casey_Hellenbrand_Resume_2026_WAM](applications/2026-09-28_ey_wam-wealth-senior/originals/Casey_Hellenbrand_Resume_2026_WAM.pdf) |
<!-- APPLICATIONS:END -->
