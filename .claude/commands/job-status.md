---
description: Show or update job application statuses (e.g. "/job-status acme applied", or no args for a summary)
---

Work with `tracker.csv`.

- If arguments were given ($ARGUMENTS), match the application by company/role/folder
  and run `python3 scripts/update_status.py` to set the new status.
- With no arguments, summarize the tracker: counts by status and by track, plus
  anything in `applied` for more than 14 days with no update (suggest a follow-up).
