# Contributing

Read [the policy](CURATION.md). Add a resource because it teaches something concrete, not because it is popular or from an underrepresented country.

1. Check the main catalogue, watchlist and historical/migration files for duplicates.
2. Open the original resource and record exact URLs, dates and what you inspected.
3. Add an entry to `data/resources.json` with all evidence, scores and limitations; mirror its concise description in the appropriate README category.
4. Record related-source edges in `data/references.json` when used. Keep translations under one origin.
5. For old content, provide the freshness route, reason and next review date. For “working”, provide the actual dated test record.
6. Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`.
7. Submit a PR explaining benefit, primary evidence, limitations and checks. Disclose authorship/sponsorship. No marketing slogans or referral links.

Corrections and removals must explain what changed and preserve the previous decision in a dated report. If a link fails, distinguish blocked/rate-limited from dead. There is no minimum star count and no addition quota.
