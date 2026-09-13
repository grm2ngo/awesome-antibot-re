# Contributing

Read [the policy](CURATION.md). Add a resource because it exposes a current anti-bot/CAPTCHA implementation or directly enables its inspection—not because it is popular.

1. Check README, SUPPORTING, ledger and active watchlist for duplicates.
2. Open the original source and inspect exact code/PoC/trace/protocol; record source date, version and URLs.
3. Add a complete record to `data/resources.json`. Core RE needs target, method and artifact; a case also needs current sample/version. Supporting material needs a concrete `re_use`.
4. Record used related-source edges in `data/references.json` and deduplicate forks, translations and reposts.
5. Confirm current eligibility: update within 365 days or living project with current primary docs/status.
6. Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`.
7. Submit the benefit, evidence, limitations and checks. Disclose authorship/sponsorship.

Do not submit marketing, solver markets, generic integration, title-only links, unsupported “working” claims or code without methodological explanation. Removed material stays in Git history; the live tree contains only current accepted records and active leads.
