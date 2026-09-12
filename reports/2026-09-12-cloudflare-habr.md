# Cloudflare JS challenge snapshot review — 2026-09-12

## Outcome

[Chrome Headless против cloudflare JS challenge](https://habr.com/ru/articles/716434/) was promoted as a **snapshot case study** at **92/100**: scope 5/5, depth 5/5, evidence 4/5, distinctiveness 4/5 and documentation 5/5. It passes policy 1.1 for the method demonstrated on the stated 2023 artifact; it does not establish a current Cloudflare or Turnstile bypass.

The curated ledger now has 34 entries: 9 implementation case studies, 4 RE tools and 21 supporting references. This normal pass used four queries, prioritizing an original Russian source outside GitHub; repository files were only followed as related artifacts.

## Evidence read

- Original Habr article, published 2023-02-12: Playwright `addInitScript` interception of `JSON.stringify`, the observed fingerprint object, Babel parsing/traversal, numeric constant folding, sequence simplification, main and scope-local string arrays, proxy/object/logical rewrites, control-flow recovery and browser-environment reconstruction.
- The article's final example names Chrome `109.0.5414.120` and the documented target site. Its screenshots/results remain author-reported; no live target was tested in this review.
- The article explicitly warns that the provided property overrides should not be reused seriously against other anti-bots because each line is easy to detect.
- Same-author repository `rastvl/cloudflare-main-challenge-deobfuscator`, pinned at `c653ec47a10fef4def0a762ff5852decb8e31974`: README, complete 355-byte `index.js`, and selected routines in `deobfuscator/Deobfuscator.js` for evaluation, string recovery, proxy/object/logical transforms and the commented control-flow path.

The same-author repository was found independently by search; the retrieved article text did not visibly link it. It supports only the existence and shape of related transformations, not independent reproduction. Its MIT repository license is not treated as permission to redistribute captured Cloudflare input/output.

## Skeptical assessment

The case earns evidence 4 rather than 5 because the original article contains substantial code and observed structures, but the exact challenge bundle/version/hash is absent and no independent run was performed. The repository is same-publisher evidence. The final screenshots cannot prove present-day effectiveness.

`verification` remains `source-reviewed`, not `runtime-tested`. The item records `sample_scope`, `snapshot_version`, method and artifact URL separately. It was not classified as recent or living, and no `working`, full-devirtualization or current-vendor claim was added.

## Coverage, workflow and queue

Language/source coverage for this pass: Russian original blog plus a related English-code repository. `rastvl` now publishes two accepted cases, still below the 25% publisher soft cap; the pair is never counted as independent corroboration.

For workflow run [34685829073](https://github.com/grm2ngo/awesome-antibot-re/actions/runs/34685829073), `validate` completed with failure but exposes no steps or log URL; `link-audit` was skipped. Local validation is reported separately and cannot turn that startup failure green.

Next queue:

1. Inspect the obsolete Rust Turnstile disassembler and opcode definitions as a bounded snapshot; do not infer current operation.
2. Seek an attributable Cloudflare/Turnstile bundle or trace with a stable hash and no solver-storefront dependency.
3. Resume exact Japanese/Korean implementation-RE sources when full article, slides/transcript or code can be read.
4. Rotate to DataDome, Kasada or PerimeterX/HUMAN with the same artifact and evidence gates.
