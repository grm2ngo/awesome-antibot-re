# CAPTCHA and community-code RE pass — 2026-09-12

## Outcome

[InsideReCaptcha](https://github.com/neuroradiology/InsideReCaptcha) was promoted as a **historical implementation case** at **100/100** under policy 1.1. The score is for the bounded artifact and code evidence, not for current reCAPTCHA behavior or bypass success. The curated ledger now contains 35 entries: 10 implementation case studies, 4 RE tools and 21 supporting references.

## Search and reading method

This pass used keyword/dork searches for `cloudflare deobfuscator`, `jsvmp reverse engineering`, `captcha reverse engineering` and `anti bot sensor reverse engineering`, then opened repository READMEs and followed concrete code/artifact paths. The connector exposes the account's visible repositories but not a Following list; the public Following page was unavailable. No private repository was read.

The strongest new artifact was the English-language `neuroradiology/InsideReCaptcha` repository. Other leads were deliberately deferred: two Cloudflare deobfuscator READMEs lacked inspected pinned source/provenance, MeowShield is an obfuscation product rather than anti-bot RE, and Shumei solver code is private/market-oriented.

## Evidence read

- Pinned commit `5176f31a7dc87654bcf3e9fa98d62bd537bea32b`, with final commit date 2014-12-09.
- README wire-flow and signal analysis: reCAPTCHA `api.js`, anchor/frame requests, bytecode, browser behavior, canvas and interaction signals, XTEA-protected data, and the explicit hardcoded `enc` sample limitation.
- `disasm.py` (9,882 bytes): opcode handlers, key/seed updates and XTEA-based encrypted-byte decoding.
- `decomp.py` (19,089 bytes): pseudo-JavaScript reconstruction, VM object model, opcode handlers and the `enc`/`model.js` input path.
- `model.js` (9,432 bytes): pinned JavaScript model used by the decompiler.

The Python headers state public-domain release for the tools. That does not grant rights to redistribute Google's scripts or captured `enc`/model data.

## Skeptical assessment

The case passes because scope, depth, evidence and documentation are all directly represented in immutable source files. It is intentionally labeled `historical`, with `snapshot_version`, `sample_scope`, exact artifact URLs and no runtime test. The repository's own text says the code is hardcoded to one sample; no current endpoint, token validity or bypass claim was accepted.

## Queue and coverage

- Inspect `mixintu/cloudflare-deobfuscator` and `LOBYXLYX/cloudflare-deobfuscator` source trees for distinct artifacts before promotion; README-only claims remain on watchlist.
- Continue dorks for Japanese/Korean CAPTCHA or browser-VM writeups with full code/transcript and stable samples.
- Seek Cloudflare/Turnstile, DataDome, Kasada and PerimeterX/HUMAN artifacts with bundle hashes or raw traces; do not count solver stores.
- Following repositories remain unresolved because the connected GitHub surface does not expose that list; only public search results and visible repositories were used.

The latest known quality workflow remains the prior startup failure: `validate` has no steps/log and `link-audit` is skipped. This pass does not claim CI health.
