# Contributing

Read [the policy](CURATION.md). Add a resource because it exposes an anti-bot/CAPTCHA implementation or directly enables its inspection—not because it is popular.

1. Check README, SUPPORTING, ledger and active watchlist for duplicates.
2. Open the original source and inspect exact code/PoC/trace/protocol; record source date, version and URLs.
3. Add a complete record to `data/resources.json`. Core RE needs target, method and artifact; a case also needs the studied sample/version. Supporting material needs a concrete `re_use`.
4. Record used related-source edges in `data/references.json` and deduplicate forks, translations and reposts.
5. Select recent, living or snapshot eligibility. A snapshot needs historical_scope, snapshot_version, method_value and snapshot_artifact_urls in the evidence list. A small script, handler, trace or original technical post is eligible when it explains a concrete mechanism.
6. Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`.
7. Submit the benefit, evidence, limitations and checks. Disclose authorship/sponsorship.

Do not submit marketing, solver markets, generic integration, title-only links, unsupported “working” claims or code without methodological explanation. Useful requires 80–<85 and Gold ≥85, with scope/evidence ≥4 and all gates passed. Old removals require individual review before restoration; their dates must not be renewed by migration.
