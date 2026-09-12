# Cloudflare / Turnstile review — 2026-09-12

## Outcome

No resource was promoted and the curated ledger remains at 33 entries: 8 implementation case studies, 4 RE tools and 21 supporting references. This normal discovery pass used four queries and focused on the Cloudflare/Turnstile gap after the preceding Japanese/Korean pass.

The search results were dominated by solver storefronts, browser automation and topic directories. Those are outside the catalogue or only discovery leads. One repository exposed enough original text and source to review: [CircuitSavage/cloudflare-turnstile-reversed](https://github.com/CircuitSavage/cloudflare-turnstile-reversed), pinned at `7e1264e4ba82f3a5763fc0afc68c21ac19e5af2e`.

## Evidence read

- README and complete repository tree; GitHub metadata reports the repository unarchived and MIT-licensed.
- `docs/04-loader-internals.md`: short minified excerpts for a `Function.toString` native-code check, `Event.isTrusted` gates, stack/timing collection and an endpoint builder.
- `docs/01-challenge-flow.md`: a four-step request-flow narrative and one named bundle path/size.
- `docs/fingerprinting/README.md`: explicitly says canvas/WebGL/audio material is reconstructed from public technique sources because the test key did not serve the runtime payload.
- `tools/capture.py`: static HTML regex extraction for sitekey/widget fields; its optional `--solve` path calls a paid service.
- `docs/observed-builds.md` and `.github/workflows/capture-check.yml`: scheduled sitekey observations and the procedure that writes them.

The README-to-file traversal produced six depth-1 edges in [data/references.json](../data/references.json). These files share one publisher and are not independent corroboration.

## Skeptical assessment

Score: **66/100** — scope 4/5, depth 3/5, evidence 2/5, distinctiveness 3/5, documentation 4/5. It fails the mandatory evidence score of 4 and therefore cannot enter README regardless of total score.

1. The loader excerpts are concrete, but the repository does not retain the referenced 84 KB bundle, a content hash or raw HAR. The catalogue cannot independently bind the excerpts and request sequence to the claimed capture.
2. The repository explicitly states that the heavier runtime vectors were not captured with its test sitekey. General explanations of canvas, WebGL, audio, TLS and IP scoring do not establish that exact Turnstile payload implementation.
3. `Function.toString` finding a wrapper's JavaScript source is one observation, not proof that every anti-detect wrapper is caught; `Function.prototype.toString` itself can be modified. The catalogue would need the exact tested conditions to retain a universal claim.
4. The scheduled check demonstrates that static extraction returned a sitekey. It does not validate bundle internals, challenge payloads or token behavior. Because the workflow uses `set +e`, capture failure does not fail the job; it can append `sitekey=none` and still commit.
5. The capture tool directly integrates and advertises a paid solver. Paid solving links are outside this repository's scope. Technical content cannot use that integration as evidence of RE quality or operation.

The candidate is recorded in [WATCHLIST.md](../WATCHLIST.md), not the curated ledger. Promotion would require a lawfully shareable hashed raw capture or equivalent provenance, exact version/environment, cleaner separation from paid solving, and claims limited to directly observed code. No runtime test was performed.

## Coverage, workflow and queue

Language/source coverage for this pass: English; GitHub source/documentation plus web discovery. The GitHub-heavy exception is explained by targeting a specific missing implementation case. It does not add an independent publisher or improve multilingual acceptance coverage.

The latest workflow listing contained another failed run, [34684996979](https://github.com/grm2ngo/awesome-antibot-re/actions/runs/34684996979), associated with head `689a99c6c56c8c97290e4f667a1df4ec4944d06d`; a fresh main read still returned `6668025e1b1c9172a69cad91be512a07dd0c60a6`. This pass does not infer that the run belongs to current main or diagnose its cause. The previously documented quality-workflow startup failure remains unresolved.

Next queue:

1. Complete the original Russian Cloudflare article already linked from the Akamai study; do not count the same publisher twice as corroboration.
2. Compare the obsolete Rust Turnstile disassembler with its opcode definitions and fork guide, strictly as snapshot research.
3. Seek a primary captured bundle/trace with provenance and no solver-storefront dependence.
4. Return to underserved Japanese/Korean RE only when an exact article, transcript or artifact can be retrieved.
