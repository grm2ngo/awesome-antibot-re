# Curation policy 1.1

This draft adds the maintainer-requested research company and manual review process to policy 1.1. Version 1.1 corrects the loss of implementation RE in the 1.0 migration; acceptance scores are unchanged. Machine thresholds live in [config/curation.json](config/curation.json).

## Scope and source types

Public research on browser anti-bot reverse engineering, challenge design, JavaScript/VM analysis, instrumentation, TLS/HTTP and browser fingerprints, detection, human-verification usability, and reproducible measurement. Include source, docs, defensive service specifications, original blogs, explainers, public forum threads, papers, datasets and talks when they teach this scope. General technology news and geographic representation alone do not qualify.

Public vendor documentation is eligible as first-party documentation; it is not evidence of comparative superiority. Paid solving storefronts, account markets, referral placements, gated-only content and thin SEO compilations remain excluded. Commercial authors may contribute excellent public technical work.

## Editorial priority: implementation RE

The main README is for reverse engineering: studies of concrete anti-bot implementations and tools that expose or transform their internals. Each core entry names `re_target`, `re_method` and the inspected `re_artifact_urls`. A case study additionally records `sample_scope` and `snapshot_version`; a dated original writeup with actual code/trace examples can be its artifact. A general product page, integration tutorial or feature list is insufficient.

- `case-study`: JavaScript/VM deobfuscation, sensor or signing reconstruction, anti-debugging, browser-engine behavior, protocol or fingerprint analysis grounded in a specific implementation.
- `re-tool`: AST/IR transforms, disassemblers, decompilers, trace analysis and browser/engine instrumentation with substantive documentation explaining the RE operation.
- `supporting`: related standards, basic concepts, service integration, CAPTCHA design/accessibility, general browser drivers, detection and measurement. These remain useful and curated in [SUPPORTING.md](SUPPORTING.md), with the same score threshold, but do not count as implementation RE.

Spend a target 70% of discovery effort on actual RE cases/methods/tools, rotating vendors, techniques, languages and source types. This is an effort target, never a required number of accepted entries. Record exceptions and missing vendor/technique coverage. Broader diversity must not displace the repository's subject.

## Mandatory gates

Every new or promoted item must satisfy all gates:

1. Direct scope fit, identifiable resource and a concrete reader benefit.
2. The exact original resource was opened and its relevant content read. Search snippets, repository stars, summaries, home pages and HTTP 200 are not substitutes.
3. The description is supported by primary material. Claims about performance or superiority need a reproducible evaluation or at least two independent primary publishers with compatible methods; otherwise attribute the claim and remove the implied comparison.
4. Explain technical substance: code, trace, mechanism, data, methodology, specification or a precise conceptual explanation. Popularity and volume earn no points.
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

For this research company, the maintainer requires approval of each concrete draft revision and optional initiative. Earlier direct-publication wording is superseded by this review workflow. Prepare a draft PR; do not merge or push to the default branch before approval. Never force-push, overwrite unrelated changes, rewrite history, spend new funds, or create empty commits to make the repo appear active. Preserve unresolved objections in the draft; elapsed time, votes and silence are not approval.

Audit migrated entries incrementally; the previous catalogue is preserved in [catalog/LEGACY.md](catalog/LEGACY.md) and is not silently certified under this policy. Every accepted entry has an evidence ledger. Reports record accepted/deferred/retired items, gaps, budgets, examined languages, reference traversal and next work. Keep machine link checks separate from editorial decisions.

## Design references

- [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md): concise scope and reasoned selection.
- [Awesome Python](https://github.com/vinta/awesome-python): task-oriented categories and concise entries.
- [Awesome Selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) and [its data repository](https://github.com/awesome-selfhosted/awesome-selfhosted-data): separate navigable list and structured maintenance data.
- [Awesome Node.js](https://github.com/sindresorhus/awesome-nodejs): clear resource categories and the practical cost of low-quality submissions.

These are design references, not endorsements. This owner-authorized, AI-assisted repository does not claim admission to the upstream Awesome index or compliance with its separate prohibition on AI-generated lists. The badge alone is not certification.

## Research company and manual decisions

Follow [company roles](docs/agents/company.md) and [separate search playbooks](docs/agents/README.md). Every run includes a dedicated Expansion Lead and independent Gatekeeper; staff repository, publication and social/regional researchers in waves. The parent coordinates and edits; the maintainer approves publication and new initiatives.

Run every three days at 09:00 Asia/Saigon. Attempt English plus at least two relevant non-English languages per run, rotating the existing language atlas. Existing query/page/time limits are upper bounds for a run, not scheduled hourly work or acceptance quotas.

The Gatekeeper independently opens the originals for every proposed promotion and materially changed claim. Round one records objections and alternative interpretations; round two records evidence-based responses. An unresolved material contradiction forces HOLD regardless of score. Numeric thresholds remain unchanged and cannot compensate for failed gates.

Approval and independent-review outcome are separate from the existing evidence levels. Use the existing ledger schema; a source-reviewed or code-reviewed label never implies reproduction. Review packets can supplement ledger evidence but must not create a competing acceptance catalogue. See [record template](docs/agents/evidence-template.md).

New ideas require a problem, benefit, cost, strongest objection and a smallest reversible trial. Researching possible directions does not authorize implementing the proposed feature. Keep deferred candidates and optional ideas outside the accepted README until the existing ledger requirements and manual review are complete.
