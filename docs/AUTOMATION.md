# Catalogue maintenance

[Policy](../CURATION.md) · [Source atlas](../SOURCES.md)

## Research passes

Read current main, policy, ledger, watchlist and latest report before discovery. Follow original code, articles and relevant references with the configured depth/page/query limits. Prefer underserved mechanisms and language lanes; preserve unresolved work. The owner has authorized supported updates. Promotions still require the policy's evidence and independent-review gates. Publish atomically on current main without force; use a ready PR if branch rules require one.

The repository is the durable research state. A configured interval does not establish a successful research run. Earlier documents describe different external schedules; do not infer which one is active from repository text. Inspect the task manager when schedule changes are requested. This scope cleanup changes no scheduler or workflow.

## GitHub quality checks

`.github/workflows/quality.yml` validates the catalogue on changes and schedules an external-link audit at `43 1 * * *` UTC. Link responses do not refresh source reviews or establish that RE tools run successfully.

Check **all workflow event types**, including push and schedule. A helper limited to pull-request events cannot establish that a push run is absent. Inspect the run and job steps; a configured cron or an empty filtered result is not a health signal. See the [latest observed failure](../reports/2026-09-12-scope-and-regional-review.md#workflow-health).

## Failure and recovery

Record blocked, throttled, missing or unreadable sources accurately; use public originals and backoff. Do not bypass access controls, retry writes repeatedly, buy services or create empty commits. Preserve partial evidence and the queue. A continuous maintenance task does not finish after one successful publication.

A workflow that fails before any step starts has not validated the catalogue. Do not infer a billing, permission or YAML cause without evidence. Local validation and GitHub execution are reported separately.
