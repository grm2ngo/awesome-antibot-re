# Douyin 40.2.0 MetaSec VMP review — 2026-09-13

Base reviewed: `c4c0c94263480732245ce325795b8bada4ae371d`. Discovery used four GitHub repository queries, then read the original repository at commit `5acc6fc1b859451314d3a4db941df95c64a27e97`. No resource was accepted and no runtime claim was adopted.

## Findings

The Vietnamese-owned repository is a substantive, current RE lead rather than a title-only result. Its pinned documentation identifies Douyin 40.2.0 and an AArch64 `libmetasec_ml.so` by size and SHA-256; maps a relocation-filled 1,133-slot direct-threaded handler table, 48-byte instruction format, register files and opcode groups; documents native operations for initialization, string decryption and `frameSign`; and publishes a LIEF/Capstone verifier for the static addresses and relocation claims.

The evidence remains one publisher's workset. The target SO is not redistributed, the app-bound license is redacted, and the public verifier has no bundled legal fixture or expected-output test. The reported Unidbg execution and decrypted strings are not independently reproduced here. The author explicitly does not claim full devirtualization or server acceptance, which is a useful limitation but does not close the evidence gap. Three repository-search hits collapse to the same repository and its forks; they are not independent corroboration.

## Decision

Hold on the active watchlist at **87/100**: scope 5, depth 5, evidence 3, distinctiveness 4, documentation 5. It fails the mandatory evidence gate despite its numeric score, so it is not added to README and is not labelled `working`.

The next bounded step is to read the pinned Java harness and credited prior art, then reproduce the static verifier against the exact SHA-256 sample or a legally shareable fixture with public expected/actual output. A structurally plausible `frameSign` value must not be generalized into current server acceptance.

## Other discovery decisions

- `hashcash-captcha` exposes a current SHA-256/WebGPU PoW implementation and tests, but its README says the code was generated from an AI prompt. It is not anti-bot RE, and no independent technical review was established, so it was not queued or listed.
- `caddy-altcha` exposes verifier and challenge-handler source files, but this pass established an integration implementation rather than reverse engineering. It was not promoted from discovery metadata alone.

The catalogue remains 4 RE tools and 9 supporting resources, with zero `runtime-tested`/`working` records.
