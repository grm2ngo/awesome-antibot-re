# Automation runbook

[Policy](../CURATION.md) · [Source atlas](../SOURCES.md)

## Research scheduler

This draft aligns the research company with the maintainer's request: every three days at 09:00 Asia/Saigon, with concrete changes and optional ideas awaiting manual approval. The Codex heartbeat for this task has been updated. An older external hourly schedule described in repository history may be a separate scheduler; it has not been inspected or disabled by this task.

- Read the current repository, evidence ledger, reports, watchlist and pending PRs before discovery; preserve concurrent changes.
- Follow [the company roles](agents/company.md). Expansion Lead and Gatekeeper are mandatory; separate scouts use their own multilingual search playbooks.
- Keep the policy's implementation-RE focus, language atlas and bounded traversal. Search English plus at least two relevant other languages each run; log actual attempts and gaps.
- Independently verify proposed claims, debate objections, and prepare a draft PR. No default-branch push or merge before approval of the specific revision.
- Keep optional ideas separate. No-change runs stay quiet; notify for meaningful review material or actionable conflicts.
- The repository and reports hold durable evidence; the local checkout can be reconstructed. Do not overwrite pending changes.

Activation status is recorded in the dated implementation report only after the scheduler confirms creation. The existence of this runbook alone does not activate a schedule.

The initial 2026-09-11 attempt was blocked by GitHub integration access, and a later attempt by the platform usage limit. Publication succeeded on 2026-09-12 at commit `3738915bda9abba9fe94c2b49cb049b60ae091de`, and the research task was confirmed enabled again. The policy, ledger and workflow now exist on main. The task reads current repository state on every run; the inline policy is only a fallback. See the [deployment report](../reports/2026-09-12.md) for the separate GitHub Actions startup issue.

## GitHub quality cron

`.github/workflows/quality.yml` validates metadata/local links on changes and runs an external-link audit on main updates and daily at `43 1 * * *` UTC (08:43 Vietnam). The audit records HTTP observations as a downloadable Actions artifact and job summary; it neither rewrites review dates nor automatically removes resources. No API/model key is needed for this quality workflow.

GitHub schedule can be delayed/dropped and public-repo schedules can be disabled after 60 days of inactivity. The external research task checks workflow health during its daily run; a failed workflow cannot be its own reliable watchdog. See [GitHub schedule documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

## Failure and recovery

Retain successful partial findings and pending URLs. Report which source failed and whether it was blocked, throttled, missing or unreadable; retry with backoff in later runs. Never treat network success as content verification. Temporary rate/usage limits need backoff, not repeated write attempts or permanent task cancellation. An ongoing maintenance task does not finish after one successful update. If the research scheduler stops, resume it through the task manager; if the GitHub workflow is disabled, explicitly re-enable it. Do not create empty commits to keep either system alive.

The quality workflow is read-only. Research publication re-reads the current head and never force-pushes; if another author has moved main, rebuild the change on the new head. This preserves edits without requiring a synthetic global lock.
