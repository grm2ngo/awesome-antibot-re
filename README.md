![Awesome Anti-Bot Reverse Engineering](assets/banner.svg)

# Awesome Anti-Bot Reverse Engineering [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

An evidence-backed catalogue of tools and references for inspecting browser anti-bot and CAPTCHA implementations: JavaScript AST/IR, deobfuscation, browser-engine hooks, signing and sensor observation, TLS/HTTP fingerprints, detection predicates and computational challenges.

**Study the method and its limits. Historical research and small, substantive contributions are welcome.**

[Tiếng Việt](README.vi.md) · [Policy](CURATION.md) · [Source atlas](SOURCES.md) · [Evidence ledger](data/resources.json) · [Latest review](reports/2026-09-13-dkaptcha-review.md)

**4 current RE tools · 9 current supporting references · 0 runtime-tested claims.**

## RE tools

### AST and intermediate representations

- [webcrack](https://github.com/j4k0xb/webcrack) — AST deobfuscation and webpack/browserify unpacking. **en · living · source-reviewed**. Transform coverage and Node/V8 dependencies bound what it can analyze.
- [JSIR](https://github.com/google/jsir) — MLIR-based JavaScript representation for data-flow analysis and source transformation. **en · living · source-reviewed**. This review did not build its LLVM/Bazel stack.

### Browser-engine and runtime instrumentation

- [Firefox-Reverse](https://github.com/WhiteNightShadow/firefox-reverse) — SpiderMonkey/Gecko hooks for observing signing logic, JSVMP execution and WASM boundaries. **zh-Hans · living · source-reviewed**. Experimental fork; not executed in this review.
- [Camoufox Reverse MCP](https://github.com/WhiteNightShadow/camoufox-reverse-mcp) — Frame/world-aware hooks, source capture and offline signer comparisons. **zh-Hans · updated 2026-09-08 · source-reviewed**. Maintainer-reported validation; raw logs are unavailable and hooks can affect observations.

## Supporting RE workbench

The nine current resources for PoW structure, browser observation, transport comparison and detection predicates are in [SUPPORTING.md](SUPPORTING.md). They are not counted as implementation case studies.

## What qualifies

- Sources may be recent, living projects, or historical snapshots with a bounded artifact/version, continuing methodological value and explicit limitations.
- A core tool names its RE target, method and inspected artifact URLs. A case study also identifies the sample/version actually studied.
- Useful resources score 80–<85; Gold resources score ≥85. Both require all evidence gates, including scope and evidence ≥4/5. A small script, VM handler, trace or original technical post can qualify without a full project or polished README. Unsupported dumps and promotional material still fail.
- `working` requires a runtime test from the last 30 days: exact version, environment, procedure, expected/actual result and public evidence.
- PoW requires the algorithm, difficulty/parameters, verifier and a reproducible vector. A PoW label in a README is insufficient.

## Research loop

Keyword/dork in multiple languages → open the original → inspect code/PoC/trace/protocol → follow related code, datasets and docs breadth-first (depth ≤3, ≤10 children/page) → canonicalize and deduplicate lineage → score skeptically → publish only supported changes.

Discovery prioritizes implementation RE and rotates vendor, method, language and source type. GitHub Following is used only when the connector exposes the actual public list; no account is inferred. See the [roadmap](docs/RE_CATALOG_ROADMAP.md), [watchlist](WATCHLIST.md) and [automation runbook](docs/AUTOMATION.md).

## Maintenance

Run:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

A configured workflow or cron is not proof that validation ran. Check every event type and actual job steps. Link status, stars and recent commits are discovery signals only.

This AI-assisted catalogue does not claim acceptance into the upstream Awesome index. Repository text is [CC0](LICENSE); linked resources retain their own licenses.
