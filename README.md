![Awesome Anti-Bot Reverse Engineering](assets/banner.svg)

# Awesome Anti-Bot Reverse Engineering

A curated list of public research, tools, and writeups on reversing browser anti-bot systems: challenge VMs, sensor payloads, TLS and HTTP fingerprinting, and the detection techniques behind them.

Scope: reverse engineering and security research only. No paid solving services, no bypass-as-a-service, no account-market links. Projects move fast in this niche, so every entry notes its last known activity date. Historical tools may remain when their methods are useful, with limitations noted. See the [curation guide](CURATION.md) for selection criteria.

> **Public research · Evidence over hype · Quality over quantity**

## Start here

| Explore | Start with |
| --- | --- |
| Understand challenge logic | [Protocol research](#challenge-protocol-research) and [VM devirtualization](#vm-devirtualization-and-deobfuscation) |
| Observe browser internals | [Engine instrumentation](#engine-level-instrumentation) |
| Study identifying signals | [TLS and HTTP](#tls-and-http-fingerprinting) and [Detection side](#detection-side) |
| Read deeper analysis | [Writeups and talks](#writeups-and-talks) and [Datasets](#datasets) |

## Contents

- [Challenge protocol research](#challenge-protocol-research)
- [VM devirtualization and deobfuscation](#vm-devirtualization-and-deobfuscation)
- [Engine-level instrumentation](#engine-level-instrumentation)
- [TLS and HTTP fingerprinting](#tls-and-http-fingerprinting)
- [Stealth browsers and automation](#stealth-browsers-and-automation)
- [Detection side](#detection-side)
- [Identity and behavior realism](#identity-and-behavior-realism)
- [Writeups and talks](#writeups-and-talks)
- [Datasets](#datasets)

## Challenge protocol research

Teardowns and reimplementations of specific vendors' client-side protections.

- [munew/cloudflare-turnstile-solver](https://github.com/munew/cloudflare-turnstile-solver) - Rust reimplementation of the Cloudflare Turnstile request pipeline: VM parser, fingerprint entry generators, LZ/XTEA/RSA payload crypto. The author states the constants are out of date; the architecture map still holds. 2025-10.
- [B00H0O/cloudflare-jsd-solver](https://github.com/B00H0O/cloudflare-jsd-solver) - Native Go solver for the Cloudflare JSD (JavaScript Detections) oneshot challenge, served as an HTTP API. 2026-08.
- [xKiian/cloudflare-jsd](https://github.com/xKiian/cloudflare-jsd) - Go reverse of the JSD challenge: runtime AST deobfuscation of main.js, inverted property-type fingerprint table, LZ-string with the script's own alphabet. 2026-05.
- [Ciarands/cloudflare-deobf](https://github.com/Ciarands/cloudflare-deobf) - Tree-sitter based string-array reconstructor for Cloudflare's challenge-platform script, with a real jsd sample embedded. 2025-04.
- [hanzheng1954/douyin-abogus-analysis](https://github.com/hanzheng1954/douyin-abogus-analysis) - Full devirtualization of Douyin's a_bogus JSVMP: disassembler, 796 captured VM programs, SM3 pipeline, and a deterministic replay harness with byte-level baselines. 2026-08.
- [armxe/tiktok-api](https://github.com/armxe/tiktok-api) - Pure-Python reimplementation of TikTok mobile and web signatures: X-Argus (protobuf, SM3, SIMON), X-Gnarly (ChaCha20, LZW), X-Bogus, TTEncrypt. 2026-07.
- [arisune1337/akamai-bmp-research](https://github.com/arisune1337/akamai-bmp-research) - Static teardown of a 570KB Akamai BMP sensor: five obfuscation layers, a working TLV bytecode disassembler, decoded string catalog, and the sensor_data wire format. 2026-06.
- [OneWinged-ShunKaido/akamai-xp1m-teardown](https://github.com/OneWinged-ShunKaido/akamai-xp1m-teardown) - Long-form teardown of Akamai XP1M: backward provenance slicing from a divergent output byte to the root probe, sensor reproduced to zero byte difference across daily builds. 2026-06.
- [recurism/decapsula](https://github.com/recurism/decapsula) - Rust devirtualizer for the Imperva Reese84 interrogator: bytecode to triplets, abstract interpretation, constant folding, flat JS output. 2026-06.
- [juanfrilla/FamousRussianMarketplace](https://github.com/juanfrilla/FamousRussianMarketplace) - Writeup plus pipeline for a register-based JSVMP: PC-anchored tracing, function substitution at known PCs, recovered AES with challenge-derived round counts. 2026-09.
- [juanfrilla/trip_vm_reversed](https://github.com/juanfrilla/trip_vm_reversed) - Trip.com phantom-token stack VM reversed, with a Goja sandbox reimplementation as the follow-up repo. 2026-05.
- [juanfrilla/awswaf_ast](https://github.com/juanfrilla/awswaf_ast) - Eleven-plugin Babel fixed-point pipeline for AWS WAF challenge scripts. 2026-06.
- [voidstar0/akamai-deobfuscator](https://github.com/voidstar0/akamai-deobfuscator) - Single-file Babel pipeline for Akamai scripts: sequence-expression unrolling and string-array recovery. **Historical:** archived; useful as a pipeline template. 2023.
- [Probabilities/Stripe-Reverse](https://github.com/Probabilities/Stripe-Reverse) - Decoded field map of the Stripe m.stripe.com/6 init payload, the closest public analog to a vendor sensor dump. 2024-11.
- [Ciarands/jscrambler-deobfuscator](https://github.com/Ciarands/jscrambler-deobfuscator) - Deobfuscator for JScrambler Enterprise with a samples corpus of real obfuscated targets. 2025-10.
- [imwithyourbitch/cloudflare-turnstile-solver](https://github.com/imwithyourbitch/cloudflare-turnstile-solver) - Fork of munew's solver carrying a 29KB maintenance guide: module map, transformer order, and a change-detection playbook for Turnstile format rotations. 2026-09.

## VM devirtualization and deobfuscation

General tooling that survives vendor rotation.

- [hasherezade/jsc_deobfuscator](https://github.com/hasherezade/jsc_deobfuscator) - Static pipeline for compiled V8 bytecode (JSCeal): patched-V8 disassembly, string decryption with bounded brute force, control-flow unflattening, optional LLM renaming with CSV caching. From the Check Point "Breaking the Seal" research. 2026-08.
- [suleram/View8](https://github.com/suleram/View8) and [hasherezade/View8](https://github.com/hasherezade/View8) - Decompiler for serialized V8 code caches; the fork adds deterministic address normalization and jump-target metadata. 2026-08.
- [google/jsir](https://github.com/google/jsir) - MLIR-based IR for JavaScript, designed to lift back to source losslessly while still supporting dataflow passes. The open core of Google's CASCADE deobfuscator. 2026-09.
- [j4k0xb/webcrack](https://github.com/j4k0xb/webcrack) - Unpacks and deobfuscates bundler and obfuscator.io output. 2026-04.
- [ctrl-escp/restringer](https://github.com/ctrl-escp/restringer) - The npm package (2.3.0) now points here; adds control-flow-flattening and js-confuser processors on top of the original REstringer. 2026-08.
- [relative/synchrony](https://github.com/relative/synchrony) - Python deobfuscator for obfuscator.io class output, revived in 2026. 2026-07.
- [youdie323323/js-confuser-deobfuscator](https://github.com/youdie323323/js-confuser-deobfuscator) - Per-transform deobfuscation of js-confuser output; the transform list doubles as a spec of the obfuscator's protection matrix. 2025-12.
- [T14Raptor/go-fAST](https://github.com/T14Raptor/go-fAST) - Go parser, traverser, and generator for JavaScript ASTs; a common foundation for custom deobfuscators. 2026-08.

## Engine-level instrumentation

Tracing code inside the browser engine to study behavior below page-level hooks.

- [WhiteNightShadow/firefox-reverse](https://github.com/WhiteNightShadow/firefox-reverse) - Firefox 153 fork with SpiderMonkey C++ trace points: per-instruction JSVMP tracing, signer-argument capture, WASM import boundaries, engine-level branch diffing. 2026-09.
- [WhiteNightShadow/camoufox-reverse-mcp](https://github.com/WhiteNightShadow/camoufox-reverse-mcp) - MCP server exposing 35 RE tools over the patched browser, with a JSVMP playbook mapping anti-bot class to safe instrumentation mode. 2026-09.
- [WhiteNightShadow/hello_js_reverse_skill](https://github.com/WhiteNightShadow/hello_js_reverse_skill) - Agent skill packaging the same methodology: 18 reference docs, hook generators, sandbox runner, case library. 2026-09.

## TLS and HTTP fingerprinting

- [FoxIO-LLC/ja4](https://github.com/FoxIO-LLC/ja4) - JA4/JA4+ network fingerprint specifications and reference tooling for TLS, HTTP, and related protocols; component licenses vary. 2026-09.
- [refraction-networking/utls](https://github.com/refraction-networking/utls) - Go crypto/tls fork with low-level ClientHello control and captured-hello parsing; browser mimicry is limited to ClientHello, not the full HTTP stack. 2026-08.
- [lexiforest/curl_cffi](https://github.com/lexiforest/curl_cffi) - Python HTTP client with browser TLS impersonation built on curl-impersonate. 2026-09.
- [bogdanfinn/tls-client](https://github.com/bogdanfinn/tls-client) - Go TLS client with browser profiles and HTTP/2 fingerprint control. 2026-09.
- [0x676e67/wreq](https://github.com/0x676e67/wreq) - Rust HTTP client with browser emulation, successor to rnet. 2026-08.
- [deedy5/primp](https://github.com/deedy5/primp) - Python bindings over a Rust core with chrome_144 through chrome_152 profiles. 2026-08.
- [zhkl0228/impersonator](https://github.com/zhkl0228/impersonator) - Pure-Java TLS fingerprint impersonation on a BouncyCastle fork, including ECH per profile. 2026-09.
- [danikishin/SharpTls](https://github.com/danikishin/SharpTls) - Managed C# TLS stack with byte-exact ClientHello control, no native calls. 2026-08.
- [pagpeter/TrackMe](https://github.com/pagpeter/TrackMe) - Passive request fingerprinting demo (tls.peet.ws) for TLS 1.2/1.3 and HTTP/2. 2026-08.
- [pagpeter/charly](https://github.com/pagpeter/charly) - Go parser for Charles Proxy .chlz captures, including TLS details and timing per transaction. 2026-07.

## Stealth browsers and automation

Listed for capture and instrumentation work; each entry notes its own tradeoffs.

- [daijro/camoufox](https://github.com/daijro/camoufox) - Firefox-based anti-detect browser with a Python API, source public. 2026-09.
- [Kaliiiiiiiiii-Vinyzu/patchright](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright) - Drop-in Playwright fork tracking upstream releases within days. 2026-09.
- [ultrafunkamsterdam/nodriver](https://github.com/ultrafunkamsterdam/nodriver) - Raw CDP driver over system Chrome for browser automation and instrumentation. 2026-05.
- [CloakHQ/cloakbrowser](https://github.com/CloakHQ/cloakbrowser) - Chromium fork with a humanize pipeline; free Chromium 146 Windows build, drop-in Playwright API plus CDP endpoint. 2026-09.
- [arman-bd/chromiumfish](https://github.com/arman-bd/chromiumfish) - Chromium fork spoofing fingerprints inside the C++ engine; macOS and Linux builds so far. 2026-08.

## Detection side

Detection techniques and implementations, from the people who study them.

- [abrahamjuliot/creepjs](https://github.com/abrahamjuliot/creepjs) - Browser fingerprinting research suite with prototype-tampering checks and headless, canvas, WebGL, and worker probes; useful for studying inconsistent spoofing. 2026-06.
- [antoinevastel/fpscanner](https://github.com/antoinevastel/fpscanner) - Headless-browser and driver detection heuristics. 2026-08.
- [antoinevastel/fp-collect](https://github.com/antoinevastel/fp-collect) - Collects only attributes that detect bots, with each attribute's detection meaning documented. 2025-03.
- [antoinevastel/bots-zoo](https://github.com/antoinevastel/bots-zoo) - Working configs for about twenty bot stacks plus UA and API-value pools. 2025.
- [antoinevastel/picasso-like-canvas-fingerprinting](https://github.com/antoinevastel/picasso-like-canvas-fingerprinting) - Faithful implementation of the Picasso canvas proof-of-work challenge. 2025.
- [antoinevastel/avastel-bot-ips-lists](https://github.com/antoinevastel/avastel-bot-ips-lists) - Daily proxy and botnet IP samples; the reputation view from the detector's side. Updated daily.

## Identity and behavior realism

- [Vinyzu/chrome-fingerprints](https://github.com/Vinyzu/chrome-fingerprints) - Ten thousand real collected Windows Chrome fingerprints, packaged, covering navigator, WebGL, WebRTC codecs, and speech voices. 2024-12.
- [Vinyzu/cursory](https://github.com/Vinyzu/cursory) - Mouse trajectory generation by retrieval from recorded human trajectories, morphing to targets, and timing regeneration. 2026-04.
- [Vinyzu/recognizer](https://github.com/Vinyzu/recognizer) - reCAPTCHA solver combining YOLO with CLIP and CLIPSeg for segmentation and click ordering. 2026-03.
- [Vinyzu/Botright](https://github.com/Vinyzu/Botright) - Testing framework bundling the above pieces over Patchright. 2026-09.

## Writeups and talks

- [Why a classic CDP bot detection signal suddenly stopped working](https://blog.castle.io/why-a-classic-cdp-bot-detection-signal-suddenly-stopped-working-and-nobody-noticed/) - Castle; traces the failure of Error.stack getter-based automation detection to V8 inspector changes, with code excerpts and upstream commit links. 2025-08.
- [FP-Inconsistent: Measurement and Analysis of Fingerprint Inconsistencies in Evasive Bot Traffic](https://arxiv.org/abs/2406.07647) - Honey-site study of 20 bot services, deriving detection rules from spatial and temporal browser fingerprint inconsistencies. 2025-09 (v3).
- [Breaking the Seal: Static Deobfuscation of JSCeal's Compiled V8 Bytecode](https://research.checkpoint.com/2026/breaking-the-seal-static-deobfuscation-of-jsceals-compiled-v8-bytecode/) - Check Point Research, 2026-08. Black Hat USA 2025 slides on [SpeakerDeck](https://speakerdeck.com/hshrzd/breaking-the-seal-static-deobfuscation-of-compiled-v8-javascript-bytecode-malware).
- [CASCADE: LLM-Powered JavaScript Deobfuscator at Google](https://arxiv.org/abs/2507.17691) - arXiv 2507.17691, accepted at ICSE-SEIP 2026.
- [nullpt.rs](https://nullpt.rs/) - Long-running reverse engineering blog: devirtualizing Nike's bot protection (two parts), TikTok VM obfuscation, Vercel BotID, anti-debugging taxonomy. 2018-2026.
- [Devirtualizing Nike.com's Bot Protection, part 1](https://nullpt.rs/devirtualizing-nike-vm-1/) and [part 2](https://nullpt.rs/devirtualizing-nike-vm-2/) - Two-part walkthrough of a client-side challenge VM.
- [Anti-detect browser benchmark 2026](https://ianlpaterson.com/blog/anti-detect-browser-benchmark-patchright-nodriver-curl-cffi/) - Independent benchmark, 31 Cloudflare-family targets, 651 verdicts, updated through 2026-08.
- [browsers-benchmark](https://github.com/techinz/browsers-benchmark) - Second independent benchmark of the same category. 2026-09.
- [Kanxue JSVMP threads](https://bbs.kanxue.com/) - Chinese-language forum with JSVMP devirtualization writeups; search the Web Security board for "jsvmp" or "纯算还原".
- [habr: Akamai Bot Manager deobfuscation via a custom AST interpreter](https://habr.com/ru/articles/720588/) - Russian; sandboxed execution defeating self-integrity checks. 2023.
- [habr: Bypassing toString-based native checks with a V8 patch](https://habr.com/ru/articles/940092/) - Russian; C++ patch to BytecodeGenerator so the "in" operator lies about prototype. 2025-08.

## Datasets

- [hasherezade/jsceal_datasets](https://github.com/hasherezade/jsceal_datasets) - 23 JSCeal payloads with extracted strings and labeled LLM renaming sessions across 21,000 functions. 2026-09.
- [Vinyzu/chrome-fingerprints](https://github.com/Vinyzu/chrome-fingerprints) - See above; also usable as an evaluation corpus.
- [antoinevastel/bots-zoo](https://github.com/antoinevastel/bots-zoo) - See above; bot stack configs and value pools.

## Freshness

Daily discovery is scheduled for 09:00 Asia/Saigon, with rotating freshness checks and a full audit due quarterly. An unchanged review need not produce a commit. Entry dates reflect last observed activity or publication, not verification dates or a claim that a tool currently passes a specific vendor. Historical research may remain with a caveat; inaccessible links are investigated before removal. See [the review process](CURATION.md#review-process).

## Contributing

Public research and tools only: repos with readable code or writeups, articles, talks, datasets. No paid solving services, no API storefronts, no Telegram-gated content. Read the [selection criteria](CURATION.md#selection), then send a PR with the same one-line description style, a date, and evidence supporting the entry.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
