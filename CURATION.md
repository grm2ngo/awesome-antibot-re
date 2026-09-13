# Curation policy 1.3 — evidence-backed implementation RE

Effective 2026-09-13, incorporating the maintainer-approved historical-method, small-contribution and quality-tier changes. Machine-enforced settings live in [config/curation.json](config/curation.json).

## Scope

The main [README](README.md) contains reverse-engineering tools and bounded implementation studies for browser anti-bot/CAPTCHA systems: JavaScript AST/IR/VM, deobfuscation, sensor/signing reconstruction, anti-debugging, browser-engine instrumentation, TLS/HTTP/browser fingerprint analysis and challenge/PoW verification.

[SUPPORTING.md](SUPPORTING.md) is limited to resources that directly enable those inspection tasks. Product integration, broad surveys, generic automation, unrelated security, solver/account markets and promotional lists are outside scope.

## Mandatory gates

Every accepted record must:

1. Link the original public source and concrete evidence URLs actually read.
2. Record source date separately from `checked_at`; a read or commit date never renews content.
3. Use one freshness route: recent (published/substantively updated within 365 days), living (current primary documentation/status), or snapshot (historical/undated study bounded to a named version or immutable artifact, with continuing methodological value and limitations). Age alone does not reject a snapshot.
4. Score at least 80/100, with scope and evidence each at least 4/5.
5. State learning value, limitations, language, publisher group, review due date and listing file.
6. For a core RE tool/case, state `editorial_role`, `re_target`, `re_method` and `re_artifact_urls`; a case also states `sample_scope` and `snapshot_version` for the implementation actually studied.
7. For a supporting record, state a concrete `re_use`.
8. Avoid unsupported operational claims. `working` requires a runtime test within 30 days with version, environment, procedure, expected/actual output, date and public evidence.
9. For PoW, expose the algorithm, difficulty/parameters, verifier/reference implementation and a reproducible test vector.
10. Pass independent review before a materially strengthened claim or promotion. A second pass by the same researcher is self-critique, not independent approval.

A snapshot must record `historical_scope`, `snapshot_version`, `method_value`, and `snapshot_artifact_urls` drawn from its inspected evidence URLs. Unknown publication dates remain null; record a version, capture scope or immutable artifact rather than guessing a date. Mark the listing as historical/snapshot and explain what remains useful. An obsolete runnable tool is not automatically a useful study, and a snapshot is not evidence of current compatibility.

A single script, VM handler, trace, PoC or short original X/CSDN/blog post can qualify. Judge the concrete technical contribution, not repository size, a complete product, polished README or platform. An exact code fragment plus a clear explanation may be the artifact. Keep target/method, provenance, claim support, limitations and independent review requirements unchanged. A code dump without interpretable evidence still fails.

Uninspected or unsupported sources remain leads with a precise next step in [WATCHLIST.md](WATCHLIST.md); do not auto-promote old removals.

## Score

All hard gates apply to both accepted tiers. Total scores rank evidence-backed resources, not operational reliability:

- **Gold: 85–100.**
- **Useful: 80–<85.** This includes fractional totals such as 84.5.
- **Watchlist: 70–<80.** Not an accepted listing.
- **Below 70:** defer/reject with a reason.

Scope and evidence must each remain at least 4/5. A high total cannot compensate for a failed gate. Tier is derived from the validated score; it is not a new verification level. Existing records retain their previous evidence/review dates when migrating schema version.

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

Remove a record when it fails scope/evidence after review. First assess whether outdated content qualifies as a bounded snapshot; age alone is not a removal reason. Snapshot studies may stay in the relevant topic section with visible limitations. Git history retains prior decisions.

## Review cadence

Recheck software every 30 days and research/standards every 90 days, or sooner after material releases, deprecations or contradictory evidence. A deadline triggers inspection, not automatic renewal.

Link checks are triage only. Record 403/429/timeouts as blocked or rate-limited; do not infer content. Workflow health requires an actual run with job steps, across push, schedule and pull-request events.
