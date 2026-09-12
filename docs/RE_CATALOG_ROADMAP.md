# RE catalogue roadmap

The target is a deep catalogue, not a quota-driven link dump. Each lane has a **discovery target of about 50 qualified records**. A target is a planning horizon: it never overrides the ≥85 score, evidence gate, license limits, source diversity or the requirement to read original code/content.

## Lanes

| Lane | What belongs in the main list | Working/PoW emphasis |
| --- | --- | --- |
| JavaScript AST and deobfuscation | AST transforms, constant/string recovery, control-flow cleanup tied to an anti-bot implementation | Working requires a recent pinned sample and test; record transform output, not “deobfuscated” as a blanket claim |
| JSVMP, bytecode and VM lifting | Opcode maps, interpreters, IR lifting, register/stack VM traces and devirtualization | Require an immutable sample and explicit unknown opcodes; no “full devirt” without complete evidence |
| Sensor, signing and crypto reconstruction | Sensor payloads, request signers, key derivation, native/WASM crypto and protocol encoding | Working means expected/actual signer or payload comparison in a stated environment; never infer secret recovery from a wrapper |
| Browser engine and instrumentation RE | CDP/BiDi, SpiderMonkey/V8/Gecko hooks, frame/world boundaries, native/API observation and anti-debug surfaces | Record observer side effects and build/version; hook success is not target success |
| Protocol, TLS and HTTP fingerprint RE | ClientHello, HTTP/2/3 ordering, browser headers, transport/session correlations grounded in a target implementation | Working requires a reproducible capture comparison; library support alone is not browser impersonation |
| CAPTCHA and challenge implementation RE | CAPTCHA bytecode, token/challenge flow, accessibility branches, sensor collection and verifier analysis | PoW/interactive claims need algorithm, parameters and verifier; solver services and account markets are excluded |
| Detection, anti-debug and tamper analysis | Native-code checks, `toString`/webdriver probes, timing, integrity and environment consistency logic | Separate observed detection predicates from universal bot verdicts |
| Proof-of-work and computational challenges | Hash puzzles, memory-hard work, rate puzzles and browser-side computational gates with code/spec | PoW entries must expose difficulty, nonce/domain separation, verifier and a reproducible vector |
| Mobile, WebView and embedded browser RE | Android/iOS/WebView SDK sensors, JNI/Frida traces and embedded JS engines | Require lawful public artifact and exact platform/version; no private SDK dumps |
| Datasets, traces and reproducible measurements | Public captures, challenge corpora, schemas and measurement harnesses used to study an implementation | Dataset provenance, schema, license and collection procedure are mandatory; benchmark results stay author-reported |

## Status labels

- `source-reviewed`: original article or documentation was read; no execution claim.
- `code-reviewed`: immutable source file/commit was inspected; this is not a full audit.
- `runtime-tested` / `working`: only with version, environment, procedure, expected/actual result, date and public evidence from the last 30 days.
- `pow`: only when algorithm and verifier details are present. A CAPTCHA that merely uses a hash or a service that advertises “difficulty” is not enough.
- `snapshot`: version-bounded educational value; it is not a current-vendor or bypass claim.

## Filling order

Spend roughly 70% of discovery effort on the first eight implementation lanes, rotate vendor/method/language/source type, and revisit all 16 language lanes within 28 days. Fill the smallest-evidence lanes first rather than padding a lane with duplicate forks, translations, homepages or solver storefronts. Keep rejected/blocked candidates in `WATCHLIST.md` with the exact missing evidence.

The first milestone is not “500 accepted links.” It is one or more defensible entries per lane, followed by breadth expansion only when each new item contributes a distinct artifact, method, version or measurement.
