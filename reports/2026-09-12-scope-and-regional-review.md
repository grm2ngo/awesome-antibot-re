# Scope cleanup and regional discovery — 2026-09-12

Owner-requested editorial pass, based on main `21a63efe6821970f82941e9dd94352f136d5b3c0`. Source-read date is 2026-09-12 UTC; publication does not renew older checks. This is not a claimed completion of an hourly/deep scheduled run.

## Catalogue decision

Removed 12 supporting entries whose recorded benefit did not meet the owner's narrower implementation-RE scope. Retained **23 entries: 10 case studies, 4 RE tools and 9 supporting references**. There are no new promotions and no runtime-tested/working claims. Scores, source dates, verification levels and review deadlines of retained resources are unchanged.

| Removed ID | Reason under the narrowed scope |
| --- | --- |
| mdn-fingerprinting | General glossary; no inspected implementation case. |
| w3c-fingerprinting | Broad specification-design guidance. |
| captcha-accessibility | Accessibility survey, not implementation RE. |
| amiunique | General fingerprint-diversity research landing page. |
| turnstile-docs | Standalone widget/token-validation integration guide. |
| yandex-smartcaptcha | Standalone service quickstart. |
| hcaptcha-docs | Standalone service integration guide. |
| webdriver-bidi | General automation specification without an inspected RE use in the record. |
| nodriver | General browser driver; no distinct RE instrumentation case recorded. |
| camoufox | General fingerprint-configurable browser; dedicated RE forks already cover instrumentation. |
| nextgen-captchas | General CAPTCHA/agent benchmark, not implementation reconstruction. |
| opencaptchaworld-data | General challenge dataset without an inspected implementation-RE use. |

These are scope removals, not findings that the sources are poor, broken or too old. Their earlier records remain in Git history. The nine retained workbench entries explicitly state their inspection use in `re_use`; this is an editorial mapping from existing evidence, not a new source/code review. The validator checks that field and rejects standalone service-doc entries.

Removed ten redundant organizational/navigation files: eight `docs/agents/*.md` playbooks plus `docs/products.md` and `docs/discovery.md`. README now navigates directly to actual case sections. Evidence reports, legacy records, the source atlas, roadmap and quality workflow remain. Essential independent-review rules stay in CURATION.md; no review gate was waived. Current owner authorization supersedes the older manual-publication text. Scheduler settings were not changed or certified.

## Original-source decisions

- [Kanxue 292935](https://bbs.kanxue.com/thread-292935.htm), zh-Hans, author handle `mb_hbqdmtuz`: partially read version 45.5.3, hashes, native-path and caveat sections. The article itself distinguishes a located signing API from an established HTTP-signing path. Publicly inspectable artifacts and an absolute publication date remain unresolved; private local file paths are not retrievable evidence. HOLD, no final score or current signature claim.
- [Kanxue 292866](https://bbs.kanxue.com/thread-292866.htm), zh-Hans, author handle 星野安全: displayed date 2026-09-04 19:12, timezone unspecified. Read unpacking and signing/serialization sections; the remainder, replies and embedded code require completion. Sample version/provenance and the anti-abuse use need checking. HOLD, unscored; neither app signing nor generic unpacking automatically qualifies as anti-bot RE.
- [Habr 1063180](https://habr.com/ru/articles/1063180/), ru, `sayasufi`: read transport comparisons, configuration examples, caveats and PoW discussion. Several variables change together; no inspected public verifier/vector supports a reproduced PoW claim. Header shows July 27 without year; body describes summer 2026, which is not a publication timestamp. Not accepted; no recent/working label. Referenced projects lead to more substantive material below.
- [HTTP/2 fingerprinting](https://lwthiker.com/networks/2022/06/17/http2-fingerprinting.html), en, `lwthiker`: published 2022-06-17; original read completely. Proposed snapshot case: client HTTP/2 behavior observed through nghttpd logs. Chrome trace: 101.0.4951.64; Firefox version unspecified. Scope/depth/evidence/distinctiveness/documentation = **5/5/4/4/5 → 92**, provisionally: direct mechanism, detailed traces, bounded observations, new frame-order analysis, clear procedure. Mutable article; raw captures unreviewed; no modern-client inference. HOLD pending independent review; self-critique does not qualify.

The related [TLS article](https://lwthiker.com/networks/2022/06/17/tls-fingerprinting.html) was read as dated background, not added as another general reference. The [curl-impersonate README](https://github.com/lwthiker/curl-impersonate) was read for mechanisms and listed versions; patch source and complete license/status review were not performed. [TS1](https://github.com/lwthiker/ts1) and [curl_cffi](https://github.com/lexiforest/curl_cffi) landing pages were opened without a new substantive source-code review.

## Discovery and coverage

Eight queries were attempted across original-blog/forum searches. Many results ignored the intended host/topic or returned directories; none was counted as a read article from a snippet. No popularity ranking or geographic authorship was inferred.

```text
site:securitydaily.net javascript reverse engineering captcha
site:forum.reverse4you.org javascript deobfuscation OR cloudflare
site:habr.com/ru/articles proof of work antibot код
site:cnblogs.com 验证码 逆向 AST 源码
"Cloudflare" "逆向" site:cnblogs.com
"captcha" "dịch ngược" [domain: viblo.asia]
"captcha" site:viblo.asia/p/
"cloudflare" "reverse" site:sekurak.pl
```

Relevant content read: ru, zh-Hans, en. Vietnamese discovery reached the [Viblo RE directory](https://viblo.asia/tags/reverse-engineering), not an eligible original. The [Reverse4You forum](https://forum.reverse4you.org/) read failed. Polish-targeted search produced no eligible original. These attempts do not establish Eastern European or Vietnamese article coverage. [Habr 1054270](https://habr.com/ru/articles/1054270/) was screened only in part and was not scored or accepted.

The owner's [public Following page](https://github.com/grm2ngo?tab=following) returned an access error; the public Following API read also failed. The available repository connector does not expose user/following APIs. No followed account or recommendation was inferred, and no candidate is attributed to Following.

Seven new edges in [the reference ledger](../data/references.json) record the actual traversal: Kanxue directory → exact threads; Habr → projects → original articles → TS1. Maximum depth 3; no parent had more than 10 selected children. Landing-page-only opens are marked `child_read: false`. Related works from the same author are not independent corroboration. New discovery is predominantly outside GitHub, but no diversity quota is claimed complete. The 16-language registry remains a rotation plan, not evidence of 16-language coverage.

## Queue

1. Finish the two Kanxue originals and replies; require a bounded anti-abuse target and public evidence before scoring.
2. Independently review the HTTP/2 snapshot; start TS1 as a new seed in a later pass to inspect code, license, revision and capture provenance without exceeding this traversal's depth.
3. Continue unresolved GitHub Following access through an available supported public reader; never substitute stars or an unrelated account's following list.
4. Seek exact Vietnamese and Polish/Russian-language forum threads with challenge/signing traces. Keep the existing Nike VM, Rust Turnstile, Japanese/Korean, DataDome/Kasada/HUMAN queue.

## Workflow health

The actual push run for base commit 21a63ef is [34714918788](https://github.com/grm2ngo/awesome-antibot-re/actions/runs/34714918788): completed, failure. Job `validate` (103610337167) failed with an empty steps array; `link-audit` was skipped. No successful validation step was observed and the startup cause remains unknown.

Correction to the prior report: the commit-workflow helper filters pull-request events. Its empty result did not establish that a push run was absent. This pass used the repository's all-event workflow-run list. No rerun loop or workflow edit was made.

## Validation and publication

Local catalogue validation and all 12 tests passed, including the new supporting-scope gate. Local Markdown targets were checked after removing duplicate navigation. New research links were opened with read status recorded above; failed opens remain unresolved. This is not a whole-catalogue external link audit or runtime test. Publication re-reads main and uses a single non-forced fast-forward. Retained source review dates and the quality workflow file are unchanged.

## Ideas for the owner

- **Small offline fixtures for selected cases:** pin input hash, environment and expected/actual trace or decoded output. Benefit: meaningful reproduction claims. Cost/objection: capture licensing, secrets and version drift. Smallest trial: one redistributable synthetic or author-licensed fixture; no live service dependency.
- **Marginal-value check per new entry:** require the new mechanism, artifact or failure mode it adds versus the closest existing case. Benefit: a 50-item lane stays useful. Cost/objection: overly aggressive deduplication can hide useful variants. Smallest trial: one comparison sentence in the existing evidence record, without another navigation document.
