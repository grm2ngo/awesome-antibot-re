# Latest-only catalogue reset — 2026-09-13

Base reviewed: `a31b76d84cef713e82dda8ad25e9e1bc13df0df7`. Publication does not renew any source date.

## Decision

Applied the owner's latest-only rule across the ledger and listings.

- Removed 10 version-bounded or old case studies from the current tree.
- Kept 13 records: 4 current RE tools and 9 current supporting references.
- Removed the archive/migration catalogue files, superseded reports and old review files.
- Removed 15 reference edges belonging only to removed records; 21 useful discovery edges remain.
- Replaced the broad unresolved queue with six plausibly active leads having concrete evidence steps.
- No record is labelled `runtime-tested` or `working`.

The removals do not assert that older work lacks educational value. It simply does not satisfy this repository's current-only product decision. Git history preserves the prior evidence and rationale.

## Current acceptance boundary

A source must be within 365 days or a living project with current primary documentation/status evidence. Core records still need target, method and inspected artifact; support records need a concrete RE operation. PoW and working claims retain their stronger reproducibility requirements.

No new candidate was accepted in this cleanup. Source registry observations and checked dates were not rewritten.

Current-status verification on 2026-09-13 covered the 12 retained GitHub projects through repository metadata; none was archived or disabled. Their primary documentation had already been inspected at the ledger's recorded dates, and the status URLs are now evidence fields. This check establishes current project status only, not runtime operation or content quality. The current Chrome DevTools Protocol page was also read directly: it exposes tip-of-tree and stable protocol routes and warns that tip-of-tree can break without compatibility guarantees.

## Validation

Run before publication:

- `python3 scripts/validate.py`
- `python3 -m unittest discover -s tests -v`
- whitespace/diff inspection

## Workflow health

The latest observed run before this change was [push run 34716143317](https://github.com/grm2ngo/awesome-antibot-re/actions/runs/34716143317), created 2026-09-12 20:07:10 UTC. It concluded failure. This catalogue does not call the schedule healthy unless a run reaches and passes actual validation steps.

## Next queue

Kakao DKAPTCHA transcript/slides; exact current Japanese code articles; Kanxue signing artifacts; Vietnamese implementation RE; then current DataDome, Kasada, PerimeterX/HUMAN and hCaptcha leads with public artifacts. GitHub Following remains unused until the connector returns the real public list.

## Deep discovery review — 2026-09-13

This pass used multilingual keyword/dork discovery and followed code relationships to pinned implementation files. English and Simplified Chinese artifacts were read. Japanese, Korean, Russian and Vietnamese searches did not establish a current original article with inspectable anti-bot code; topic pages, blocked pages, generic tutorials and solver storefronts were not treated as evidence. GitHub Following remained unavailable as a real connector result and was not inferred.

### Decisions

- **JSHookMCP — hold, 83/100.** Scope 5, depth 4, evidence 3, distinctiveness 4, documentation 5. At current v0.3.5, inspected source includes a `webcrack` wrapper, Babel-based JSVMP heuristics, `Function`/debugger/timing patches, CDP network capture and pre-load WASM capture. The code is substantive, but it does not by itself prove the README's broad tool count or full devirtualization. Hooking and fetch replacement can change observed behavior, and the project also includes CAPTCHA-solving, anti-detection and sponsor/proxy material. No code was executed in this pass.
- **Scrapfly Antibot Detector — hold, 80/100.** Scope 5, depth 4, evidence 3, distinctiveness 4, documentation 4. Inspected v2.7 MAIN-world hook bridge, Akamai `sensor_data` interceptor, detector rule and changelog. The implementation is useful for instrumentation study, but the Akamai rule still declares `lastUpdated: 2024-01-15`; current repository activity is not current signature evidence. Maintainer-reported fixes were not independently reproduced, and publisher/product interest plus the NPOSL-3.0 license are material limitations.
- **Cap core — active PoW lead, not promoted.** The current repository release is `standalone@3.1.11` (2026-09-04); inspected core v0.1.2 exposes challenge count/size/difficulty, SHA-256 prefix verification, token validation, replay callback and reproducible unit fixtures. This satisfies the artifact shape expected for a PoW review, but the repository's independent-review gate and a public runtime record were not completed. No `working` label was assigned.
- **GeeTest 7.8.1 reverse — freshness rejected.** The source contains concrete image-gap, track, `w` parameter and request reconstruction, but its README explicitly dates the implementation to 2021-06-01. The 2026-08-18 change is an README update; it does not establish a substantive current GeeTest implementation. The lead remains only for one precise current-version evidence check.
- **`bypass-anti-crawler` — rejected, not queued.** The repository is a generic scraping tutorial with toy Base64/DevTools examples, proxy rotation and a simple solver. It has no target sample, trace, protocol reconstruction or meaningful implementation RE.
- **`awesome-web-reversing` — discovery seed only.** Its own verification method is repository activity metadata and its catalogue is seeded from LLM research reports. Neither is independent technical evidence for the downstream claims.

### Artifact inspection

- JSHookMCP: `Deobfuscator.ts`, `JSVMPDeobfuscator.ts`, anti-debug bypass core, `NetworkMonitor.impl.ts`, WASM browser handlers and package metadata at commit `55e22b706d937c3c56f3b48b883b98b524d4166d`.
- Antibot Detector: `content-main-world.js`, Akamai detector JSON/interceptor, changelog and NPOSL-3.0 license at tree `c1ad7486a9cf0f121736bd328796a1499e6ac573`.
- Cap: core README, `src/index.js`, `src/crypto.js`, core/crypto test files and package v0.1.2 at commit `e02138579482c711ee0bb79c7be3486fe0bf3e84`.
- GeeTest reverse: README, `utils.py`, `validate.py` and `test/test.py` at commit `67203ad9bd01a9074b7fd0b43082c47964d7c1a9`.

No candidate was added to README or SUPPORTING.md. The catalogue remains 4 RE tools and 9 supporting resources, with zero `runtime-tested`/`working` records.

### Queue after this pass

1. Reproduce Cap's pinned verifier fixtures and inspect the v2 RSW path without claiming human verification.
2. Build benign pinned fixtures for JSHookMCP's JSVMP and WASM paths; quantify observer effects.
3. Seek current original code from Kakao/LINE, Qiita/Zenn and Vietnamese public security communities, not tag pages.
4. Complete Kanxue signing provenance, then rotate to current DataDome, Kasada and PerimeterX/HUMAN artifacts.

## Vendor implementation rotation — 2026-09-13

This bounded pass used four current searches for DataDome, Kasada, PerimeterX/HUMAN and Chinese-language implementations, then read original pages and pinned code artifacts. Commercial scraping guides, solver services, topic pages and generic bypass advice were excluded.

- **Kasada VM — hold, 88/100 but evidence 3/5.** Scope 5, depth 5, evidence 3, distinctiveness 5, documentation 4. The repository includes a linear-sweep disassembler for `p.js j-1.2.430`, decoded bytecode/string tables, an exploratory SHA-256 `x-kpsdk-cd` search over four private trace directories and a Node sandbox. However, the README says `cd` is still WIP, the committed verifier depends on gitignored `_vm-traces`, and the current head only updates `LICENSE`. No captured `p.js` provenance or public expected output establishes the asserted server-valid `x-kpsdk-ct` result. It remains a strong active lead, not a catalogue entry and not `working`.
- **DataDome encryption — hold, 87/100 but evidence 3/5.** Scope 5, depth 5, evidence 3, distinctiveness 4, documentation 5. v1.1.1 provides extensive analysis, an encrypt/decrypt rewrite, constants for CAPTCHA/interstitial modes and fixture files. The inspected test compares all but the final salt-dependent character and then performs self-roundtrip decryption; it does not independently establish equivalence to a named current DataDome bundle. Original bundle hash/version and capture provenance are missing. The README prominently advertises the author's paid bypass API, so its effectiveness claims are treated as interested-party claims.
- **Kernel Kasada article — rejected under the code gate.** The current original describes a 449 KB VM, 1,515 decoded strings, repeating-XOR telemetry, Blink-level instrumentation and CDP/Playwright differences. It provides neither the generated extractor nor Chromium patch nor trace corpus, so the technical claims cannot be reproduced from the publication alone.
- **PerimeterX Solver v6.7.9 — rejected and not queued.** The code is tied to an unspecified older v6.7.9 snapshot, admits hard-coded dynamic WebGL values, and offers newer versions for purchase via Telegram. A cosmetic 2026 README/contact update does not renew the implementation; the sales path is outside repository scope.
- **DataDome/Kasada commercial guides — rejected.** Recent pages from scraping vendors primarily direct readers to paid APIs or offer generic browser/proxy advice without original artifacts. Publication recency did not compensate for absent code provenance.

The obsolete GeeTest 7.8.1 lead was removed from the active watchlist immediately: no evidence suggests a current-version implementation is forthcoming. No accepted record or `working` claim changed.

### Queue after vendor rotation

1. Resolve Kasada VM's substantive commit date and captured `p.js` provenance; obtain a public offline fixture before executing anything.
2. Trace DataDome fixture lineage to an immutable bundle and independently compare exact encrypt/decrypt output.
3. Continue regional original-code search for Kakao/LINE, Qiita/Zenn, Kanxue and Vietnamese communities.
4. Seek a current PerimeterX/HUMAN analysis with a public bundle/trace and method documentation, excluding storefronts.
