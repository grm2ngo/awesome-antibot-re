# Curation policy 1.0

Effective 2026-09-11 under the repository owner's authorization to broaden research and publish updates autonomously. Machine thresholds live in [config/curation.json](config/curation.json). This policy supersedes the earlier 8/10 guide and the unactivated v0.1 proposal.

## Scope and source types

Public research on browser anti-bot reverse engineering, challenge design, JavaScript/VM analysis, instrumentation, TLS/HTTP and browser fingerprints, detection, human-verification usability, and reproducible measurement. Include source, docs, defensive service specifications, original blogs, explainers, public forum threads, papers, datasets and talks when they teach this scope. General technology news and geographic representation alone do not qualify.

Public vendor documentation is eligible as first-party documentation; it is not evidence of comparative superiority. Paid solving storefronts, account markets, referral placements, gated-only content and thin SEO compilations remain excluded. Commercial authors may contribute excellent public technical work.

## Mandatory gates

Every new or promoted item must satisfy all gates:

1. Direct scope fit, identifiable resource and a concrete reader benefit.
2. The exact original resource was opened and its relevant content read. Search snippets, repository stars, summaries, home pages and HTTP 200 are not substitutes.
3. The description is supported by primary material. Claims about performance or superiority need a reproducible evaluation or at least two independent primary publishers with compatible methods; otherwise attribute the claim and remove the implied comparison.
4. Explain technical substance: code, trace, mechanism, data, methodology, specification or a precise conceptual explanation. Popularity and volume earn no points.
5. No unacknowledged duplication. Canonical project and stable ID are known; forks need a concrete difference. Mirrors, translations and articles copying one source count as one origin.
6. Dates are sourced and typed: publication, substantive update, read, verification and test dates are separate. Unknown dates remain null. Do not infer activity from copyright year, title, search crawl, cosmetic commit or a README news mention.
7. Limitations, maturity and commercial affiliation are visible. Source-visible is not automatically open source. Record licensing per code/data/paper asset before asserting an open-source or reuse claim.
8. Freshness route and next review date are recorded. Archived/deprecated work is Historical, not presented as current tooling.
9. Evidence ledger and score rationale exist; no fabricated second reviewer or runtime result. Uncertainty is recorded, not averaged away by a high score.
10. The complete diff passes local validation. Publication uses a non-forced update based on the actual current branch; concurrent changes are preserved.

## Selection score

Each dimension is 0–5. 0 = absent/unknown, 1 = weak, 2 = partial, 3 = adequate with meaningful gaps, 4 = strong for the stated purpose, 5 = exceptional/directly established. Add a specific rationale per dimension. Sum dimension × weight/5; decimal scores are audit aids, not statistical precision.

| Dimension | Weight | Strong evidence |
| --- | --- | --- |
| Scope | 25 | Directly addresses a listed mechanism/use case. |
| Technical depth | 20 | Exposes mechanisms, methods, samples or a precise specification. |
| Evidence | 25 | Primary content supports the bounded description; execution claims have actual test records. |
| Distinctiveness | 15 | Adds a meaningful method, artifact or perspective beyond existing entries. |
| Documentation | 15 | Accessible explanation with context and visible limitations. |

Accept ≥85/100, scope ≥4/5 and evidence ≥4/5, only after all gates pass. 70–84 is watchlist; below 70 is reject/defer with reason. Never raise a score to meet a language or volume quota. Compare within a use case, not across code, service, paper and blog. Source-review can support educational selection without supporting operational effectiveness.

## Evidence levels

| Level | Required record | Does not establish |
| --- | --- | --- |
| discovered | Search/directory URL and reason to inspect. | That the article was read. |
| source-reviewed | Exact primary URL, inspected material, claim, limitation, reviewer/date. | That software was executed or the service works. |
| code-reviewed | Source-review plus exact code file and immutable commit/blob and inspection note. | Successful runtime behavior. |
| runtime-tested | Version/commit, supported environment, procedure, expected/actual output and dated evidence. | Universal success on other sites or future versions. |

Use “working” only with runtime-tested evidence within 30 days and name the tested scenario. Never turn a successful link audit into last_verified_at or last_tested_at. The initial migration is source-reviewed, not runtime-tested.

## Freshness and compensating criteria

- Recent: dated articles/benchmarks normally fall within the rolling 365-day window computed at run time. A substantive update must be evidenced; a changed title does not qualify.
- Living: age of a repo/service is not a cutoff. Inspect relevant current docs and status for descriptive inclusion; operational claims require a supported-version test. No visible release is not proof of abandonment.
- Foundation: older concepts can remain if still useful, with explicit boundaries and corroborating current primary context. Do not carry old benchmark results into present rankings.
- Historical: methods from archived/deprecated tools or captured vendor versions live in a separate file with dates, purpose and limitations.
- Unknown: if a time-sensitive claim lacks a date, defer it. Undated living docs may be accepted for a narrow specification claim with the uncertainty recorded.

Review service docs/software within 30 days; research/standards within 90; foundations/history within 180. Major releases, deprecations or contradictory findings trigger earlier review. Review deadlines cause a recheck, not automatic factual conclusions or deletion. Keep old primary references available to discovery even when ineligible for the current list.

## Type-specific checks

| Type | Additional checks |
| --- | --- |
| Code/library/browser | Canonical owner, source/docs, archived status, version/dependencies, license boundaries, limitations; test before claiming operation. |
| Hosted/self-hosted service | Public integration protocol, server/client boundary, documented limits and access model; price/unit/date only if verified; no unapproved paid testing. |
| Blog/explainer | Original authorship, mechanism, examples and references; distinguish sponsored/translated/reposted material. |
| Forum/Q&A | Read exact thread and replies that change the answer; require primary artifacts or a reproducible original explanation. |
| Paper/benchmark | Read methods/limitations, pin version, check dataset/splits/models/metrics and independent versus author-reported claims. |
| Dataset | Card, origin, version, sampling/labeling, license per asset and relationship to code/paper; no inference from row count alone. |
| Talk/video | Read slides or available transcript and relevant timestamps. A title/landing page alone is watchlist. |
| Standard | Record publication status/version; drafts are not final recommendations. |

## Multilingual discovery and reference traversal

Use [SOURCES.md](SOURCES.md) and [config/languages.json](config/languages.json). Diversity spans language, publisher, perspective, medium, use case, difficulty, platform, stack, hosting, licensing and maturity. Do not infer nationality, rank countries or lower quality gates for representation.

1. Read current ledger, last report, queue and policy. Resolve the current main commit.
2. Run language × topic × resource-type × intent queries, including failure/limitation/deprecation terms. Search effort is logged independently from acceptance.
3. Open primary content and extract only relevant references, related work, successors, code, dataset and docs links. Record parent/child/relation/depth/read status.
4. Canonicalize and deduplicate before expansion; retain semantic query parameters and version identifiers. Translation and affiliate mirrors are not independent evidence.
5. Breadth-first traversal: seed depth 0, at most 3 edges, at most 10 relevant children/page. Prefer primary evidence and underserved lanes; never recursively follow every navigation link.
6. Stop when the budget is exhausted, queue is empty, or two successive expansions of a branch produce no new relevant URL. Save the unprocessed queue and visited IDs in the run report; continue next time.
7. Score candidates, then perform a separate skeptical review pass: challenge unsupported details, source dependence, dates, novelty and comparison conditions. Record one actual reviewer honestly; use additional reviewers when available, never invent agreement.
8. Publish only supported entries and corrections. Preserve rejected/deferred reasons and old descriptions in the migration/history files.

Hourly budget is 4 queries/20 pages; the daily deepening budget is 30 queries/120 pages/30 minutes. Stop at the first limit. At most 2 concurrent requests/domain, at least 2 seconds between requests and backoff for throttling. No newly purchased API or subscription. These are upper bounds, not quotas.

## Lifecycle, retention and autonomy

Discovered → watchlist → source/code-reviewed → curated. Runtime-tested is an additional evidence level. Curated → needs-review → historical/removed only with a documented reason. One blocked fetch/403/429/timeout is inconclusive; confirm ordinary dead-link suspicion over three separate runs spanning at least seven days, considering moves and author archives. A clear shutdown/deprecation notice can establish retirement sooner.

The owner authorized direct publication of meaningful policy-compliant updates on 2026-09-11. Do not ask for per-entry reapproval. Never force-push, overwrite unrelated changes, rewrite history, spend new funds, or create empty commits to make the repo appear active. If branch rules require a PR, create a ready PR and report that gate accurately.

Audit migrated entries incrementally; the previous catalogue is preserved in [catalog/LEGACY.md](catalog/LEGACY.md) and is not silently certified under this policy. Every accepted entry has an evidence ledger. Reports record accepted/deferred/retired items, gaps, budgets, examined languages, reference traversal and next work. Keep machine link checks separate from editorial decisions.

## Design references

- [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md): concise scope and reasoned selection.
- [Awesome Python](https://github.com/vinta/awesome-python): task-oriented categories and concise entries.
- [Awesome Selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) and [its data repository](https://github.com/awesome-selfhosted/awesome-selfhosted-data): separate navigable list and structured maintenance data.
- [Awesome Node.js](https://github.com/sindresorhus/awesome-nodejs): clear resource categories and the practical cost of low-quality submissions.

These are design references, not endorsements. This owner-authorized, AI-assisted repository does not claim admission to the upstream Awesome index or compliance with its separate prohibition on AI-generated lists. The badge alone is not certification.
