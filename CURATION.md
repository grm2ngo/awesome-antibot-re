# Curation policy 1.2 — latest-only implementation RE

Effective 2026-09-13. Machine-enforced settings live in [config/curation.json](config/curation.json).

## Scope

The main [README](README.md) contains current reverse-engineering tools and current implementation studies for browser anti-bot/CAPTCHA systems: JavaScript AST/IR/VM, deobfuscation, sensor/signing reconstruction, anti-debugging, browser-engine instrumentation, TLS/HTTP/browser fingerprint analysis and challenge/PoW verification.

[SUPPORTING.md](SUPPORTING.md) is limited to current resources that directly enable those inspection tasks. Product integration, broad surveys, generic automation, unrelated security, solver/account markets and promotional lists are outside scope.

## Mandatory gates

Every accepted record must:

1. Link the original public source and concrete evidence URLs actually read.
2. Record source date separately from `checked_at`; a read or commit date never renews content.
3. Be published or substantively updated within 365 days, or be a living project with current primary documentation and status evidence.
4. Score at least 85/100, with scope and evidence each at least 4/5.
5. State learning value, limitations, language, publisher group, review due date and listing file.
6. For a core RE tool/case, state `editorial_role`, `re_target`, `re_method` and `re_artifact_urls`; a case also states current `sample_scope` and `snapshot_version`.
7. For a supporting record, state a concrete `re_use`.
8. Avoid unsupported operational claims. `working` requires a runtime test within 30 days with version, environment, procedure, expected/actual output, date and public evidence.
9. For PoW, expose the algorithm, difficulty/parameters, verifier/reference implementation and a reproducible test vector.
10. Pass independent review before a materially strengthened claim or promotion. A second pass by the same researcher is self-critique, not independent approval.

Unknown-age, version-only, obsolete, undocumented or artifact-free material is removed from the current tree. Keep only a plausibly active lead with a precise next step in [WATCHLIST.md](WATCHLIST.md).

## Score

Each dimension is 0–5:

| Dimension | Weight |
| --- | ---: |
| Scope fit | 25% |
| Technical depth | 20% |
| Evidence | 25% |
| Distinctiveness | 15% |
| Documentation | 15% |

Popularity, stars, HTTP 200, search rank and a cosmetic commit do not improve the score. “Top/best” comparisons require equivalent conditions and at least two independent publisher groups.

## Research and provenance

Use the loop defined in [docs/AUTOMATION.md](docs/AUTOMATION.md). Follow references breadth-first to depth three with no more than ten children per page. Canonicalize URLs and publisher lineage; translations, forks and reposts are not independent evidence. Read articles, code, PoCs, traces, protocols, datasets and exact versioned documentation—not snippets or homepages.

Discovery diversity is an effort target, never an acceptance quota. Spend about 70% of discovery on implementation RE and rotate vendor, technique, language and source type. Apply one quality threshold across all 16 language lanes.

## Publication and removal

Update README/SUPPORTING, data ledgers, watchlist and the latest evidence report together. Run local validation and tests, inspect the diff, then publish one atomic non-force fast-forward commit on current `main`. If `main` changed, rebuild on the new head. Do not create date-only commits.

Removal is immediate when a record no longer satisfies current scope/freshness/evidence. Git history is the audit trail; the repository does not maintain archive sections.

## Review cadence

Recheck software every 30 days and research/standards every 90 days, or sooner after material releases, deprecations or contradictory evidence. A deadline triggers inspection, not automatic renewal.

Link checks are triage only. Record 403/429/timeouts as blocked or rate-limited; do not infer content. Workflow health requires an actual run with job steps, across push, schedule and pull-request events.
