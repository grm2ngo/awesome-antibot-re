# RE workbench

[Case studies and RE tools](README.md)

These 9 supporting references enable specific anti-bot/CAPTCHA RE operations. They are not case studies. Their prior review dates and evidence levels are unchanged; naming an RE use does not claim a new code audit or a successful runtime test. All retain their existing ledger limitations.

## Computational challenge implementations

- [ALTCHA](https://github.com/altcha-org/altcha) — Inspect a public computational-challenge implementation and its client/verifier boundary; parameter/vector audit remains pending. **en · source-reviewed**. Study algorithm/version tradeoffs; compliance and anti-bot efficacy claims were not independently validated.
- [mCaptcha](https://github.com/mCaptcha/mCaptcha) — Trace the SHA-256 computational-challenge and validation flow; no reproduced work-factor or capacity claim. **en · source-reviewed**. A computational cost mechanism is not proof of human identity; runtime and capacity not tested.

## Browser observation

- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) — Locate browser debugger, runtime and network observation commands when instrumenting a captured challenge. **en · source-reviewed**. Tip-of-tree can change without compatibility guarantees; match the browser version.

## Transport fingerprint inspection

- [JA4 / JA4+](https://github.com/FoxIO-LLC/ja4) — Compare extracted TLS/HTTP attributes and reference fingerprint definitions against a captured client trace. **en · source-reviewed**. Licenses differ by component; do not treat all JA4+ methods as uniformly licensed.
- [uTLS](https://github.com/refraction-networking/utls) — Vary ClientHello configuration in a controlled transport-fingerprint experiment. **en · source-reviewed**. The README warns parts may lag; ClientHello control is not full browser-stack emulation.
- [curl_cffi](https://github.com/lexiforest/curl_cffi) — Compare documented TLS/HTTP2 profiles with browser captures; a profile is not evidence of target success. **en · source-reviewed**. Profiles and supported Python versions change; embedded sponsor links are outside this listing.
- [TrackMe](https://github.com/pagpeter/TrackMe) — Observe request/header-order/TLS fields on a controlled server during fingerprint analysis. **en · source-reviewed**. Demo output is not a general bot-detection verdict; local deployment was not tested.

## Detection predicates

- [CreepJS](https://github.com/abrahamjuliot/creepjs) — Inspect browser consistency and prototype-tampering predicates used as detection signals. **en · source-reviewed**. Use the project-linked deployment; a fingerprint or inconsistency does not by itself prove bot traffic.
- [FPScanner](https://github.com/antoinevastel/fpscanner) — Inspect fingerprint-collection and bot-detection primitives when mapping a detection predicate. **en · source-reviewed**. Not a complete fraud-prevention system; sponsored by Castle as disclosed by the project.

PoW labels require an inspected algorithm, difficulty/parameters, verifier and reproducible vector. A project describing itself as proof-of-work is only a discovery lead for that stronger label. Service quickstarts, broad surveys and general CAPTCHA benchmarks were removed in the [scope review](reports/2026-09-12-scope-and-regional-review.md).
