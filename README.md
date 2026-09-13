![Awesome Anti-Bot Reverse Engineering](assets/banner.svg)

# Awesome Anti-Bot Reverse Engineering [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

An evidence-backed catalogue of tools and references for inspecting browser anti-bot and CAPTCHA implementations: JavaScript AST/IR, deobfuscation, browser-engine hooks, signing and sensor observation, TLS/HTTP fingerprints, detection predicates and computational challenges.

**Study the method and its limits. Historical research and small, substantive contributions are welcome.**

[Tiếng Việt](README.vi.md) · [Policy](CURATION.md) · [Source atlas](SOURCES.md) · [Evidence ledger](data/resources.json) · [Latest review](reports/2026-09-13-dkaptcha-review.md)

**4 current RE tools · 9 current supporting references · 0 runtime-tested claims.**

## Contents

- [Choose a research path](#choose-a-research-path)
- [Browse by product](#browse-by-product)
- [RE tools](#re-tools)
- [Supporting RE workbench](#supporting-re-workbench)
- [Research waiting for evidence](#research-waiting-for-evidence)
- [Read the labels](#read-the-labels)
- [What qualifies](#what-qualifies)
- [Where we look](#where-we-look)
- [Research loop](#research-loop)
- [Maintenance](#maintenance)

## Choose a research path

| Your question | Start here | What to look for |
| --- | --- | --- |
| How can I simplify obfuscated JavaScript? | [AST and IR tools](#ast-and-intermediate-representations) | Transform coverage, intermediate output and unsupported syntax |
| Where does a sensor or signer get its inputs? | [Engine instrumentation](#browser-engine-and-runtime-instrumentation) | Observed calls, frame/world boundaries and effects of the observer |
| Which transport attributes distinguish clients? | [Transport inspection](#transport-fingerprint-inspection) | Captured TLS/HTTP fields and the limits of profile emulation |
| Which browser properties become detection signals? | [Detection predicates](#detection-predicates) | Consistency checks and the conditions behind a verdict |
| How is a computational challenge verified? | [Challenge implementations](#computational-challenge-implementations) | Algorithm, parameters, verifier boundary and test vectors |
| What still needs verification? | [Research queue](#research-waiting-for-evidence) | Missing provenance, artifacts or independent checks |

## Browse by product

[TikTok / Douyin](#tiktok-and-douyin) · [reCAPTCHA / hCaptcha](#recaptcha-and-hcaptcha) · [Kasada](#kasada) · [DataDome](#datadome) · [Akamai / Cloudflare](#akamai-and-cloudflare) · [PoW implementations](#computational-challenge-implementations)

Product navigation includes research gaps. A product heading is not a claim that a current implementation has passed review.

## RE tools

### AST and intermediate representations

Use these to study code transformations and representations. Preserve the original sample and compare outputs before drawing conclusions about behavior.

- [webcrack](https://github.com/j4k0xb/webcrack) — AST deobfuscation and webpack/browserify unpacking. **en · living · source-reviewed**. Transform coverage and Node/V8 dependencies bound what it can analyze.
- [JSIR](https://github.com/google/jsir) — MLIR-based JavaScript representation for data-flow analysis and source transformation. **en · living · source-reviewed**. This review did not build its LLVM/Bazel stack.

### Browser-engine and runtime instrumentation

These entries focus on observing internals. Instrumentation can affect the behavior being observed; the listed evidence does not establish live-target success.

- [Firefox-Reverse](https://github.com/WhiteNightShadow/firefox-reverse) — SpiderMonkey/Gecko hooks for observing signing logic, JSVMP execution and WASM boundaries. **zh-Hans · living · source-reviewed**. Experimental fork; not executed in this review.
- [Camoufox Reverse MCP](https://github.com/WhiteNightShadow/camoufox-reverse-mcp) — Frame/world-aware hooks, source capture and offline signer comparisons. **zh-Hans · updated 2026-09-08 · source-reviewed**. Maintainer-reported validation; raw logs are unavailable and hooks can affect observations.

## Supporting RE workbench

Nine reviewed supporting references are summarized below so you can choose a tool from this page. Their full caveats and canonical links remain in [the workbench](SUPPORTING.md); they are not implementation case studies.

### Computational challenge implementations

| Resource | Research use | Main limitation |
| --- | --- | --- |
| [ALTCHA](SUPPORTING.md#computational-challenge-implementations) | Inspect the challenge and client/verifier boundary | Parameter/vector audit remains pending |
| [mCaptcha](SUPPORTING.md#computational-challenge-implementations) | Trace SHA-256 challenge generation and validation | No reproduced work-factor or capacity result |

### Browser observation

| Resource | Research use | Main limitation |
| --- | --- | --- |
| [Chrome DevTools Protocol](SUPPORTING.md#browser-observation) | Locate debugger, runtime and network observation commands | Match the protocol to the browser version |

### Transport fingerprint inspection

| Resource | Research use | Main limitation |
| --- | --- | --- |
| [JA4 / JA4+](SUPPORTING.md#transport-fingerprint-inspection) | Compare TLS/HTTP attributes and fingerprint definitions with a trace | Licenses differ by component |
| [uTLS](SUPPORTING.md#transport-fingerprint-inspection) | Vary ClientHello configuration in controlled comparisons | ClientHello control is not full browser emulation |
| [curl_cffi](SUPPORTING.md#transport-fingerprint-inspection) | Compare documented TLS/HTTP2 profiles with browser captures | A profile does not establish target success |
| [TrackMe](SUPPORTING.md#transport-fingerprint-inspection) | Observe request, header-order and TLS fields on a controlled server | Output is not a general bot verdict |

### Detection predicates

| Resource | Research use | Main limitation |
| --- | --- | --- |
| [CreepJS](SUPPORTING.md#detection-predicates) | Inspect consistency and prototype-tampering predicates | An inconsistency does not prove bot traffic |
| [FPScanner](SUPPORTING.md#detection-predicates) | Inspect fingerprint collection and detection primitives | Not a complete fraud-prevention system |

[Back to contents](#contents)

## Research waiting for evidence

These are **pending lanes**, not accepted sources. Read the linked review before treating a promising result as established.

### TikTok and Douyin

The [Douyin/MetaSec VMP review](reports/2026-09-13-douyin-metasec-vmp-review.md) records a bounded investigation and its remaining evidence gaps. TikTok and Douyin must be assessed separately; one platform's sample does not establish the other's behavior.

### reCAPTCHA and hCaptcha

No product-specific implementation entry is accepted in the current ledger. The [research roadmap](docs/RE_CATALOG_ROADMAP.md) includes CAPTCHA internals; [the source atlas](SOURCES.md) supplies discovery channels. General browser and challenge tools above should not be read as validated solutions for these products.

### Kasada

The [Kasada VM lead](WATCHLIST.md) has disassembly and decoded artifacts, but capture provenance and stronger result claims need further evidence. Its provisional total does not override the evidence gate.

### DataDome

The [DataDome encryption lead](WATCHLIST.md) needs clearer bundle provenance and exact-vector checks, including the salt-dependent behavior documented in the queue.

### Akamai and Cloudflare

The [Antibot Detector lead](WATCHLIST.md) illustrates why vendor rules need their own dates, fixtures and false-positive checks. See the [roadmap](docs/RE_CATALOG_ROADMAP.md) for additional implementation research lanes; a vendor name in a tool is not evidence of accuracy.

### Other pending work

[The watchlist](WATCHLIST.md) also tracks Cap core, JSHookMCP, regional posts and talks. Each lead records the missing evidence and next step. Nothing is added merely to fill a product category.

## Read the labels

| Label | Meaning |
| --- | --- |
| Useful | Validated score 80–<85, with every mandatory gate passed |
| Gold | Validated score ≥85, with every mandatory gate passed |
| Source-reviewed | Relevant primary material was read; software need not have been executed |
| Code-reviewed | Specific source portions and an immutable revision were inspected |
| Runtime-tested | A dated test record names version, environment, procedure and result |
| Living / recent | Describes source freshness, not guaranteed effectiveness |
| Snapshot | Historical or version-bounded research with an explicit artifact, method value and limitations |
| Pending | Missing evidence or review; not an accepted resource |

Quality tier, evidence level and source age are separate. Scores and detailed evidence are in [the ledger](data/resources.json).

## What qualifies

- Sources may be recent, living projects, or historical snapshots with a bounded artifact/version, continuing methodological value and explicit limitations.
- A core tool names its RE target, method and inspected artifact URLs. A case study also identifies the sample/version actually studied.
- Useful resources score 80–<85; Gold resources score ≥85. Both require all evidence gates, including scope and evidence ≥4/5. A small script, VM handler, trace or original technical post can qualify without a full project or polished README. Unsupported dumps and promotional material still fail.
- `working` requires a runtime test from the last 30 days: exact version, environment, procedure, expected/actual result and public evidence.
- PoW requires the algorithm, difficulty/parameters, verifier and a reproducible vector. A PoW label in a README is insufficient.

## Where we look

| Source type | What can qualify |
| --- | --- |
| Repositories and small code artifacts | A full tool, script, VM handler, trace or fixture that explains a concrete mechanism |
| Blogs and technical posts | Original analysis with inspectable examples and bounded claims |
| X, CSDN and forums | Exact original posts/threads with technical substance; a profile, repost or snippet stays a lead |
| Papers, talks and datasets | Read methods, slides/transcripts, provenance and limitations before inclusion |
| Historical work | A specific version/artifact and a clear explanation of what remains useful |

Discovery covers [16 language lanes and source channels](SOURCES.md). Original authors, citations and substantive forks can lead to further research; copies do not count as independent confirmation.

## Research loop

Keyword/dork in multiple languages → open the original → inspect code/PoC/trace/protocol → follow related code, datasets and docs breadth-first (depth ≤3, ≤10 children/page) → canonicalize and deduplicate lineage → score skeptically → publish only supported changes.

Discovery prioritizes implementation RE and rotates vendor, method, language and source type. See the [roadmap](docs/RE_CATALOG_ROADMAP.md), [watchlist](WATCHLIST.md) and [public maintenance guide](docs/AUTOMATION.md).

## Maintenance

Run:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

A configured workflow or cron is not proof that validation ran. Check every event type and actual job steps. Link status, stars and recent commits are discovery signals only.

This catalogue does not claim acceptance into the upstream Awesome index. Repository text is [CC0](LICENSE); linked resources retain their own licenses.
