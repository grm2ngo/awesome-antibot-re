# Curation policy 1.1

Scope revision, 2026-09-12: the owner requested a narrower anti-bot/CAPTCHA RE catalogue and explicitly authorized this cleanup and publication. Policy 1.1's score, evidence and independent-review requirements are retained; organizational playbooks and duplicate navigation are removed. Machine thresholds live in [config/curation.json](config/curation.json).

## Scope and source types

Public analysis of anti-bot/CAPTCHA implementations: JavaScript/VM, sensor and request signing, challenge/verifier logic, anti-debugging, browser-engine instrumentation and protocol/fingerprint reconstruction. Mobile signing belongs only when the request-integrity or anti-abuse mechanism is identified. Generic mobile unpacking, malware, game cheats and unrelated vulnerability research are outside scope.

Require inspected code, disassembly, a concrete trace, or a reproducible experiment tied to the stated mechanism. A code block that only configures an SDK is insufficient. Papers, forums and personal blogs face the same gate; venue, popularity and language earn no exemption.

Vendor specifications can corroborate a case's protocol boundary, but widget quickstarts and product introductions do not receive standalone catalogue entries. Paid solving storefronts, account markets, referral placements, gated-only content and thin SEO compilations remain excluded. Commercial authors may contribute excellent public technical work.

## Editorial priority: implementation RE

The main README is for reverse engineering: studies of concrete anti-bot implementations and tools that expose or transform their internals. Each core entry names `re_target`, `re_method` and the inspected `re_artifact_urls`. A case study additionally records `sample_scope` and `snapshot_version`; a dated original writeup with actual code/trace examples can be its artifact. A general product page, integration tutorial or feature list is insufficient.

- `case-study`: JavaScript/VM deobfuscation, sensor or signing reconstruction, anti-debugging, browser-engine behavior, protocol or fingerprint analysis grounded in a specific implementation.
- `re-tool`: AST/IR transforms, disassemblers, decompilers, trace analysis and browser/engine instrumentation with substantive documentation explaining the RE operation.
- `supporting`: a small [RE workbench](SUPPORTING.md) for debugger operations, transport capture/comparison, detection-predicate inspection and computational challenge analysis. Every record must name its concrete `re_use`. General introductions, standalone integration guides, usability surveys, generic drivers and CAPTCHA benchmarks without an implementation-RE connection are excluded. Supporting items retain the same score threshold and do not count as cases.

Spend a target 70% of discovery effort on actual RE cases/methods/tools, rotating vendors, techniques, languages and source types. This is an effort target, never a required number of accepted entries. Record exceptions and missing vendor/technique coverage. Broader diversity must not displace the repository's subject.

## Mandatory gates

Every new or promoted item must satisfy all gates:

1. Direct scope fit, identifiable resource and a concrete reader benefit.
2. The exact original resource was opened and its relevant content read. Search snippets, repository stars, summaries, home pages and HTTP 200 are not substitutes.
3. The description is supported by primary material. Claims about performance or superiority need a reproducible evaluation or at least two independent primary publishers with compatible methods; otherwise attribute the claim and remove the implied comparison.
4. Show technical substance tied to implementation RE: inspected code/disassembly, a concrete trace or a reproducible experiment. For a supporting protocol reference, identify the debugger/capture operation it enables in `re_use`. Prose, SDK configuration, HTTP 200 and popularity alone earn no acceptance.
5. No unacknowledged duplication. Canonical project and stable ID are known; forks need a concrete difference. Mirrors, translations and articles copying one source count as one origin.
6. Dates are sourced and typed: publication, substantive update, read, verification and test dates are separate. Unknown dates remain null. Do not infer activity from copyright year, title, search crawl, cosmetic commit or a README news mention.
7. Limitations, maturity and commercial affiliation are visible. Source-visible is not automatically open source. Record licensing per code/data/paper asset before asserting an open-source or reuse claim.
8. Freshness route and next review date are recorded. Archived/deprecated tools are not presented as current tooling; their methods may qualify separately as explicitly bounded snapshot research.
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
- Snapshot: a study of a captured implementation may remain in the main RE list regardless of age if it meets the same score and evidence gates. Require a named sample/version or immutable artifact, a concrete method, an explanation of its continuing educational value and explicit limits. Preserve publication/capture dates when known; an immutable source revision can bound an undated case without implying recent publication. Missing original captures or private tools must be disclosed and constrain claims. Snapshot is research, not a recommendation that obsolete software currently runs.
- Historical: retain superseded context, deprecated tools without a qualifying standalone study, old benchmark results and earlier decisions separately. Age alone is not a reason to hide a qualified RE method from the main list.
- Unknown: if a time-sensitive claim lacks a date, defer it. Undated living docs may be accepted for a narrow specification claim; an undated snapshot needs an immutable artifact and cannot make current-compatibility claims. Otherwise keep it in watchlist.

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

Hourly budget is 4 queries/20 pages; the daily deepening budget is 30 queries/120 pages/30 minutes. Stop at the first limit. At most 2 concurrent requests/domain, at least 2 seconds between requests and backoff for throttling. No newly purchased API or subscription. These are upper bounds, not quotas. An explicit owner-requested editorial correction is recorded separately from a scheduled discovery run; do not disguise it as a completed hourly or daily run.

## Lifecycle, retention and autonomy

Discovered → watchlist → source/code-reviewed → curated. Runtime-tested is an additional evidence level. Curated → needs-review → historical/removed only with a documented reason. One blocked fetch/403/429/timeout is inconclusive; confirm ordinary dead-link suspicion over three separate runs spanning at least seven days, considering moves and author archives. A clear shutdown/deprecation notice can establish retirement sooner.

The owner's current session instructions authorize evidence-supported updates and this scope cleanup on main. Use an atomic, non-forced update based on current main; use a ready PR if branch rules require it. Authorization does not waive evidence or independent review. Never overwrite unrelated changes, rewrite history, spend new funds or create empty activity commits.

Audit migrated entries incrementally; the previous catalogue is preserved in [catalog/LEGACY.md](catalog/LEGACY.md) and is not silently certified under this policy. Every accepted entry has an evidence ledger. Reports record accepted/deferred/retired items, gaps, budgets, examined languages, reference traversal and next work. Keep machine link checks separate from editorial decisions.

## Design references

- [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md): concise scope and reasoned selection.
- [Awesome Python](https://github.com/vinta/awesome-python): task-oriented categories and concise entries.
- [Awesome Selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) and [its data repository](https://github.com/awesome-selfhosted/awesome-selfhosted-data): separate navigable list and structured maintenance data.
- [Awesome Node.js](https://github.com/sindresorhus/awesome-nodejs): clear resource categories and the practical cost of low-quality submissions.

These are design references, not endorsements. This owner-authorized, AI-assisted repository does not claim admission to the upstream Awesome index or compliance with its separate prohibition on AI-generated lists. The badge alone is not certification.

## Review and publication

A proposed promotion or materially strengthened claim needs an independent reviewer who opens its original evidence. Record actual identities, objections and responses. A second pass by the same researcher is useful self-critique, not an independent review. Unresolved material contradictions force HOLD regardless of score. If independent review is unavailable, save the candidate and missing checks in the watchlist; do not fabricate approval.

Keep one catalogue and evidence ledger. Reports retain decisions, corrections, reference traversal and pending work; they are not a second acceptance list. Optional ideas must identify the problem, benefit, cost, strongest objection and smallest reversible trial. An idea is not an implemented feature.

The current cleanup is documented in [the scope review](reports/2026-09-12-scope-and-regional-review.md). Historical reports describe their original decisions and counts, not today's catalogue or schedule.
