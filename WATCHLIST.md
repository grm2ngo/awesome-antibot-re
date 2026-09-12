# Watchlist and unresolved leads

[Back to the main list](README.md). Presence here is not endorsement or a “working” claim.

| Lead | Language | Observation on 2026-09-11 | Required next step |
| --- | --- | --- | --- |
| [Kakao DKAPTCHA talk](https://tech.kakao.com/posts/604) | ko | Title and official landing page visible; substantive talk/transcript not retrieved. | Obtain public slides/transcript and read methods/limitations before scoring. |
| [Kanxue](https://bbs.kanxue.com/) | zh-Hans | Fetch failed; no thread accepted from a snippet. | Resolve an exact public thread and read original evidence. |
| [Qiita CAPTCHA](https://qiita.com/tags/captcha) | ja | Topic directory read; article bodies not surfaced by available retrieval. | Find and inspect an exact original article, date and code. |
| [Zenn CAPTCHA](https://zenn.dev/topics/captcha) | ja | Topic directory read; no complete article accepted. | Find exact article and verify primary links. |
| [Previous catalogue](catalog/LEGACY.md) | mixed | All previous entries preserved; only ledger-backed entries are promoted to the main list. | Prioritize challenge-VM writeups and transport tools; review 8 pending items per daily deepening. |

No useful search results in a lane means an unresolved coverage gap, not absence of useful research. Source-directory checks are tracked separately in [SOURCES.md](SOURCES.md).

## RE review — 2026-09-12

| Resource | Material actually inspected | Decision and next evidence |
| --- | --- | --- |
| [Turnstile reverse implementation](https://github.com/munew/cloudflare-turnstile-solver) | README and the complete `src/disassembler/disassemble.rs` entry point at `ba6cbd2faa8471394ab7e016a12ef52e6ebcc52e`. | Author explicitly says obsolete and nonfunctional. Retain as a historical RE lead; inspect the recursive disassembler and opcode semantics before selecting a bounded study. Sparse explanation is a gap independent of age. |
| [Turnstile fork maintenance guide](https://github.com/imwithyourbitch/cloudflare-turnstile-solver/blob/2be55ddf48e3c9dd191e7c09b58cdeb5fa89c5cc/MAINTENANCE_GUIDE.md) | README, tree and guide introduction/module-map sections. | Guide acknowledges the obsolete implementation. Its vendor-update frequency and repair suggestions lack inspected validation evidence. Compare claimed pipeline/opcode behavior with source before promotion. A fork guide is not independent corroboration of upstream code. |
| [Cloudflare deobfuscator](https://github.com/Ciarands/cloudflare-deobf) | Repository tree and selected string-array recovery code in `src/deobfuscator.py`, at `2f49f674ef79f825c8245efb6a8fbd45bce13297`. | No README exists in the inspected tree. Document sample provenance, dependencies, usage and license limits before promotion; README 404 does not mean the repository is dead. |
| [mixintu/cloudflare-deobfuscator](https://github.com/mixintu/cloudflare-deobfuscator) | README describes dynamic string, control-flow and proxy simplification with a local npm input file, but source files and sample provenance were not established in this pass. | Inspect pinned implementation and input artifact; compare with the accepted rastvl snapshot before deciding whether it adds distinct learning value. |
| [LOBYXLYX/cloudflare-deobfuscator](https://github.com/LOBYXLYX/cloudflare-deobfuscator) | README contains transformation examples for string decoding and switch flattening, but no inspected versioned challenge artifact or independent capture. | Read source files, provenance and license; do not treat README examples as current Cloudflare behavior. |
| [MeowShield](https://github.com/qq185863818/MeowShield) | AST/JSVM protection product README; it protects code rather than documenting anti-bot implementation RE, and the linked service is outside catalogue scope. | Keep as an adjacent obfuscation lead only if a concrete anti-bot RE case and public code artifact are found. |
| [wulu-shumei-bypass](https://github.com/wulu007/shumei-bypass) | Public protocol wrapper documents Shumei registration/encryption, but solver implementations are private extensions and the project is framed as bypass tooling. | Excluded unless a defensive, public implementation-RE artifact is separated from private solver/account-market material. |
| [Nike VM, part 1](https://nullpt.rs/devirtualizing-nike-vm-1/) and [part 2](https://nullpt.rs/devirtualizing-nike-vm-2/) | Both original reads returned server errors; no article content was inferred. | Keep blocked/unreadable, locate a legitimate public author mirror or retry later. Do not label a link permanently dead from one session. |
| [JSC deobfuscator](https://github.com/hasherezade/jsc_deobfuscator) | README and portions of `deobf_all.py` at `6970e4af35c35e77ac8c09ba0887bb79c7b12f97`. | Compiled V8/JSCeal analysis may be a useful transferable method. Establish the specific anti-bot learning use before adding; it is not a JSVMP or general-JavaScript deobfuscator. No code executed. |
| [Cloudflare Turnstile reversed](https://github.com/CircuitSavage/cloudflare-turnstile-reversed) | README, tree, loader excerpts, flow note, fingerprinting index, capture script, observed-build log and capture workflow at `7e1264e4ba82f3a5763fc0afc68c21ac19e5af2e`. | **Defer — 66/100; evidence gate 2/5.** Useful loader excerpts, but no archived bundle/HAR binds them to the claimed capture. Runtime fingerprint sections are reconstructed from general sources, not the captured payload. The tool embeds a paid solver path, excluded from this catalogue. Remove promotional/solver coupling, preserve a hashed raw capture where lawful, and distinguish exact observations from extrapolation before rescoring. |

The rastvl Cloudflare article was promoted as a bounded 2023 snapshot after full methodological review; see the [Cloudflare snapshot report](reports/2026-09-12-cloudflare-habr.md). It remains the same publisher group as the accepted Akamai article and is not independent corroboration.

Seven RE resources from legacy and the historical Russian Akamai article now have individual acceptance records; see the [RE correction report](reports/2026-09-12-re-focus.md). The original legacy text is preserved, including claims that this review corrected rather than repeated.
