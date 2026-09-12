# Automation runbook

[Policy](../CURATION.md) · [Source atlas](../SOURCES.md)

## Research scheduler

The owner authorized recurring research and direct evidence-supported publication. The scheduler is a ChatGPT automation using the connected GitHub account and public-source readers, not a background process in an ephemeral workspace.

- Hourly check at minute 17, Asia/Ho_Chi_Minh (the repository previously used the equivalent Asia/Saigon timezone).
- The first local 09:17 run each day performs deeper discovery and a rotating audit. Monday's deeper run also reviews coverage, overdue entries and scheduler/quality health.
- Read the current repository policy, ledger, last report and queue at every run. Normal budget: 4 queries/20 pages; daily deeper budget: 30 queries/120 pages/30 minutes. An unchanged source needs no cosmetic commit.
- Rotate a language lane by local day/hour and prioritize neglected lanes. Core lanes must be attempted every 7 days, all 16 every 28; record gaps rather than inventing accepted results.
- Follow primary references at most 3 edges/10 children per page. Store remaining queue, parent-child evidence, dates and decisions in a dated report.
- Revalidate every new/promoted entry; update README plus ledger coherently. Publish supported changes to main with a non-forced atomic commit. If branch rules prevent this, use a ready PR and report the blocker.
- Do not use a previous workspace as persistent state. The GitHub repository and dated reports are authoritative. Do not read private source accounts or Library files for this task.

Activation status is recorded in the dated implementation report only after the scheduler confirms creation. The existence of this runbook alone does not activate a schedule.

At preparation on 2026-09-11, GitHub read access worked but publication returned HTTP 403 `Resource not accessible by integration`, including a content-only attempt. The task therefore also contains the selection policy inline. Until write access is restored, it reads available repository files and public sources, returns findings marked pending publication, and does not assume these new files exist on main. It does not repeatedly attempt blocked writes. The prepared update still needs publication before the repository can hold the research ledger and quality workflow.

## GitHub quality cron

`.github/workflows/quality.yml` validates metadata/local links on changes and runs an external-link audit on main updates and daily at `43 1 * * *` UTC (08:43 Vietnam). The audit records HTTP observations as a downloadable Actions artifact and job summary; it neither rewrites review dates nor automatically removes resources. No API/model key is needed for this quality workflow.

GitHub schedule can be delayed/dropped and public-repo schedules can be disabled after 60 days of inactivity. The external research task checks workflow health during its daily run; a failed workflow cannot be its own reliable watchdog. See [GitHub schedule documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

## Failure and recovery

Retain successful partial findings and pending URLs. Report which source failed and whether it was blocked, throttled, missing or unreadable; retry with backoff in later runs. Never treat network success as content verification. If the research scheduler stops, resume it through the task manager; if the GitHub workflow is disabled, explicitly re-enable it. Do not create empty commits to keep either system alive.

The quality workflow is read-only. Research publication re-reads the current head and never force-pushes; if another author has moved main, rebuild the change on the new head. This preserves edits without requiring a synthetic global lock.
