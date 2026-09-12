# Supporting references for anti-bot RE

[Back to the RE case studies and tools](README.md)

These 21 resources support implementation research: protocols, network signals, detection experiments, human verification, accessibility and measurement. They remain in the [curated ledger](data/resources.json) under the same acceptance threshold, with `editorial_role: supporting`; they are not counted as RE case studies.

Descriptions retain their 2026-09-11 source-review evidence. Moving an entry here on 2026-09-12 does not renew its review date or assert runtime success.

## Contents

- [Foundations and measurement](#foundations-and-measurement)
- [CAPTCHA systems and service documentation](#captcha-systems-and-service-documentation)
- [JavaScript analysis and instrumentation](#javascript-analysis-and-instrumentation)
- [TLS and HTTP fingerprinting](#tls-and-http-fingerprinting)
- [Detection and browser behavior](#detection-and-browser-behavior)
- [Papers benchmarks and datasets](#papers-benchmarks-and-datasets)

## Foundations and measurement

- [MDN: Fingerprinting](https://developer.mozilla.org/en-US/docs/Glossary/Fingerprinting) - Introduces browser fingerprint attributes and links to measurement and standards guidance. **en · foundation**. A glossary, not a bot detector or current effectiveness benchmark.
- [W3C fingerprinting guidance](https://w3c.github.io/fingerprinting-guidance/) - Defines fingerprinting surfaces, threat models and mitigation tradeoffs for web specifications. **en · standard**. Living guidance; it does not promise complete prevention of fingerprinting.
- [W3C: Inaccessibility of CAPTCHA](https://www.w3.org/TR/turingtest/) - Examines accessibility barriers and alternatives to visual human-verification challenges. **en · foundation**. A 2021 Group Draft Note; historical examples are not a current vendor ranking.
- [Am I Unique?](https://amiunique.org/) - Research project for studying browser fingerprint diversity and evolution. **en · research**. A research sample does not establish population-wide uniqueness or bot detection accuracy.

## CAPTCHA systems and service documentation

- [Cloudflare Turnstile validation](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/) - Documents server-side token validation, errors and integration boundaries. **en · service-docs**. Vendor documentation; no paid service test or comparative success claim.
- [Yandex SmartCaptcha quickstart](https://yandex.cloud/ru/docs/smartcaptcha/quickstart) - Russian-language first-party guide to widget integration and server-side answer validation. **ru · service-docs**. Documentation review only; account requirements and regional availability must be checked before adoption.
- [hCaptcha developer guide](https://docs.hcaptcha.com/) - Explains widget integration, token verification, configuration and testing boundaries. **en · service-docs**. Vendor claims are not independent comparative evidence; no production integration tested.
- [ALTCHA](https://github.com/altcha-org/altcha) - Source and documentation for a self-hosted proof-of-work challenge widget. **en · software**. Study algorithm/version tradeoffs; compliance and anti-bot efficacy claims were not independently validated.
- [mCaptcha](https://github.com/mCaptcha/mCaptcha) - SHA-256 proof-of-work CAPTCHA system with an explanation of its challenge and validation flow. **en · software**. A computational cost mechanism is not proof of human identity; runtime and capacity not tested.

## JavaScript analysis and instrumentation

- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) - Primary protocol reference for browser debugging, network observation and profiling. **en · standard**. Tip-of-tree can change without compatibility guarantees; match the browser version.
- [WebDriver BiDi](https://www.w3.org/TR/webdriver-bidi/) - Standards-track reference for bidirectional browser automation commands and events. **en · standard**. Specification status and implementation coverage vary; this is not a tested compatibility matrix.
- [nodriver](https://github.com/ultrafunkamsterdam/nodriver) - Asynchronous Python browser driver exposing CDP domains, commands and events. **en · software**. No claim of undetectability; browser-version changes affect behavior.

## TLS and HTTP fingerprinting

- [JA4 / JA4+](https://github.com/FoxIO-LLC/ja4) - Network fingerprint definitions and reference implementations spanning TLS, HTTP and related protocols. **en · software**. Licenses differ by component; do not treat all JA4+ methods as uniformly licensed.
- [uTLS](https://github.com/refraction-networking/utls) - Go TLS fork exposing ClientHello controls and fingerprint-oriented handshake configuration. **en · software**. The README warns parts may lag; ClientHello control is not full browser-stack emulation.
- [curl_cffi](https://github.com/lexiforest/curl_cffi) - Python bindings to a curl-impersonate fork for studying TLS and HTTP/2 client profiles. **en · software**. Profiles and supported Python versions change; embedded sponsor links are outside this listing.
- [TrackMe](https://github.com/pagpeter/TrackMe) - Go HTTP/1 and HTTP/2 server that reports request, header-order and TLS fingerprint details. **en · software**. Demo output is not a general bot-detection verdict; local deployment was not tested.

## Detection and browser behavior

- [CreepJS](https://github.com/abrahamjuliot/creepjs) - Browser fingerprinting research covering prototype tampering, rendering signals and consistency checks. **en · software**. Use the project-linked deployment; a fingerprint or inconsistency does not by itself prove bot traffic.
- [FPScanner](https://github.com/antoinevastel/fpscanner) - Browser fingerprint collection and bot-detection primitives with documented limits and non-goals. **en · software**. Not a complete fraud-prevention system; sponsored by Castle as disclosed by the project.
- [Camoufox](https://github.com/daijro/camoufox) - Firefox-based browser project for studying fingerprint configuration and automation tradeoffs. **en · software**. The project warns it is under development; production stability and present-day effectiveness were not tested.

## Papers benchmarks and datasets

- [Next-Gen CAPTCHAs](https://github.com/MetaAgentX/NextGen-CAPTCHAs) - Research platform with CAPTCHA generation, benchmark data and documented GUI-agent evaluation protocols. **en · research**. Benchmark claims are author-reported; model settings and full/lite subsets must not be conflated.
- [Open CaptchaWorld dataset](https://huggingface.co/datasets/OpenCaptchaWorld/Open_CaptchaWorld) - Dataset card and files connected to the Open CaptchaWorld research platform. **en · research**. Dataset revisions, row counts and licenses must be tracked separately from paper/code; not downloaded or benchmarked.
