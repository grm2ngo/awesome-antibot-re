# Multilingual source atlas

[Back to the list](README.md). This is a discovery registry, not a list of endorsed articles. Status is from 2026-09-11 unless the ledger records a later check: **content-checked** = at least one relevant primary resource read; **directory-checked** = directory/site inspected only; **blocked** = access failed or relevant text unavailable; **pending** = seed not yet inspected. No status exempts future articles from the curation gates.

## Language and ecosystem lanes

Coverage is driven by technical relevance and information gaps, not a ranking of countries. Russia/Russian-speaking engineering, China/Taiwan, Japan, Korea, Europe, India, Israel, the Americas, Vietnam and Arabic-language research can publish in local languages or English. Record an author's actual affiliation only when explicitly sourced; do not infer it from language. Native posts and their translations are one evidence origin.

| Language | Search ecosystem | Native query seeds | Starting channels |
| --- | --- | --- | --- |
| en | Global; US/UK/Canada/Australia and English-language engineering | browser fingerprinting; CAPTCHA; deobfuscation; instrumentation | GitHub, standards, research labs |
| ru | Russian-speaking engineering | отпечаток браузера; капча; деобфускация; анализ JavaScript | Habr, OpenNet, Yandex docs |
| zh-Hans | Simplified-Chinese engineering | 浏览器指纹; 验证码; JS逆向; 反混淆; 检测 | Kanxue, CSDN, Cnblogs, Gitee |
| zh-Hant | Traditional-Chinese engineering | 瀏覽器指紋; 驗證碼; 反混淆; 機器人偵測 | iT 邦幫忙, author repositories |
| ja | Japanese engineering | ブラウザフィンガープリント; CAPTCHA; 難読化解除; ボット検知 | Qiita, Zenn, LY engineering |
| ko | Korean engineering | 브라우저 지문; 캡차; 난독화 해제; 봇 탐지 | Kakao, LINE, original developer posts |
| de | German-speaking engineering | Browser-Fingerprinting; CAPTCHA; Deobfuskation; Bot-Erkennung | CCC, Heise, research institutions |
| fr | French-speaking engineering | empreinte du navigateur; CAPTCHA; désobfuscation; détection de robots | SSTIC, Developpez, original research |
| vi | Vietnamese engineering | dấu vân tay trình duyệt; mã xác thực; giải mã rối; phát hiện bot | Viblo, original author repositories |
| es | Spanish-speaking engineering | huella del navegador; CAPTCHA; desofuscación; detección de bots | Original researchers, conferences and vendor docs |
| pt | Portuguese-speaking engineering; including Brazil | impressão digital do navegador; CAPTCHA; desofuscação; detecção de bots | Original researchers and engineering blogs |
| hi | Hindi-language discovery; Indian research also searched in English | ब्राउज़र फिंगरप्रिंटिंग; कैप्चा; बॉट पहचान | Original author/lab pages discovered through queries |
| he | Hebrew-language discovery; Israeli research also searched in English | טביעת אצבע של דפדפן; קפצ׳ה; זיהוי בוטים | Original author/lab pages discovered through queries |
| ar | Arabic-language discovery; regional research also searched in English | بصمة المتصفح; كابتشا; كشف الروبوتات | Original author/lab pages discovered through queries |
| pl | Polish-language engineering | odcisk przeglądarki; CAPTCHA; deobfuskacja; wykrywanie botów | Original researchers and technical communities |
| tr | Turkish-language engineering | tarayıcı parmak izi; CAPTCHA; kod çözümleme; bot tespiti | Original researchers and technical communities |

## Source registry

| Source | Languages | Type | Inspection status | Selection rule |
| --- | --- | --- | --- | --- |
| [GitHub](https://github.com/) | en, ru, zh-Hans, zh-Hant, ja, ko, de, fr, es, pt, vi, hi, he, ar, pl, tr | forge | content-checked | Read code/docs, resolve canonical owner, check archive state and license scope; stars are discovery signals only. |
| [Habr](https://habr.com/ru/) | ru, en | community | content-checked | Original author, technical mechanism and dated evidence; distinguish company blogs, translation and repost. |
| [OpenNet](https://www.opennet.ru/) | ru | news-community | directory-checked | Follow news references to original release/code/paper; a headline is not sufficient. |
| [Yandex SmartCaptcha docs](https://yandex.cloud/ru/docs/smartcaptcha/quickstart) | ru, en | vendor-docs | content-checked | Use documented protocol boundaries only as evidence for a concrete RE case; standalone integration guides are excluded. |
| [Kanxue](https://bbs.kanxue.com/) | zh-Hans | forum | content-checked | Exact public thread plus original author/traces required; never substitute a forum home page for a read article. |
| [CSDN](https://blog.csdn.net/) | zh-Hans | community | directory-checked | Require original author/work, date provenance and primary references; reject scraped/repackaged SEO summaries. |
| [Cnblogs](https://www.cnblogs.com/) | zh-Hans | community | directory-checked | Prefer original implementation/experiments; trace reposts to the first publisher. |
| [iT 邦幫忙](https://ithelp.ithome.com.tw/) | zh-Hant | community | pending | Select specific technical posts with primary references; popularity alone is insufficient. |
| [Qiita CAPTCHA topic](https://qiita.com/tags/captcha) | ja | community | directory-checked | Read the complete article and repository/version; do not accept tag pages as articles. |
| [Zenn CAPTCHA topic](https://zenn.dev/topics/captcha) | ja | community | directory-checked | Prefer reproducible technical posts and authored books; preserve Japanese title and translation notes. |
| [LY Corporation engineering](https://techblog.lycorp.co.jp/ja/) | ja, en | engineering-blog | directory-checked | Select relevant first-party engineering work, distinguishing translation from independent corroboration. |
| [LINE Engineering](https://engineering.linecorp.com/ko/) | ko, en | engineering-blog | directory-checked | Require an actual article, mechanism and evidence; treat related corporate publications as one publisher group. |
| [Kakao Tech](https://tech.kakao.com/) | ko | engineering-blog | directory-checked | Read article/slides/transcript; a video landing page alone remains a lead. |
| [Viblo](https://viblo.asia/) | vi, en | community | directory-checked | Prioritize original Vietnamese experiments with exact version and source references. |
| [SSTIC](https://www.sstic.org/) | fr, en | conference | directory-checked | Read selected paper/slides with named authors; require direct topic relevance. |
| [CCC media archive](https://media.ccc.de/) | de, en | conference | directory-checked | Inspect slides/transcript and timestamps; distinguish archival talks from current claims. |
| [Developpez](https://www.developpez.com/) | fr | community | blocked | Require primary code/research behind the article; retry only through allowed public access. |
| [Heise developer](https://www.heise.de/developer/) | de | news-community | blocked | Trace original technical work; do not count reporting and the cited original as independent results. |
| [Information Security Stack Exchange](https://security.stackexchange.com/) | en | forum | directory-checked | Question context, answer evidence and present-day applicability must all be read; votes alone are insufficient. |
| [arXiv](https://arxiv.org/) | en | paper-index | content-checked | Read relevant methods and limitations, pin paper version, follow code/data; label preprint status accurately. |
| [Hugging Face datasets](https://huggingface.co/datasets) | en, zh-Hans | dataset-host | content-checked | Read dataset card, version, provenance and per-asset license; downloads/likes are not quality proof. |
| [W3C](https://www.w3.org/) | en | standards | content-checked | Use exact protocol semantics to resolve a concrete RE observation; general surveys do not become catalogue entries. |
| [MDN](https://developer.mozilla.org/) | en, ru, zh-Hans, zh-Hant, ja, ko, de, fr, es, pt | standards-docs | content-checked | Match feature/version; translations share one evidence origin. |
| [Cloudflare technical material](https://blog.cloudflare.com/) | en, ru, zh-Hans, zh-Hant, ja, ko, de, fr, es, pt, vi, he, ar, pl, tr | vendor-research | content-checked | Use original mechanisms/docs, not marketing outcomes; all translations are one publisher. |
| [hCaptcha docs](https://docs.hcaptcha.com/) | en | vendor-docs | content-checked | Use documented protocol boundaries only as evidence for a concrete RE case; standalone integration guides are excluded. |
| [PortSwigger Research](https://portswigger.net/research) | en | vendor-research | directory-checked | Only browser/protocol/instrumentation work directly relevant to scope; exclude unrelated vulnerability news. |
| [Check Point Research](https://research.checkpoint.com/) | en | vendor-research | pending | Select original JavaScript/VM analysis with sample provenance; exclude generic product pages. |
| [nullpt.rs](https://nullpt.rs/) | en | independent-blog | blocked | Nike-VM article reads failed on 2026-09-12; retry only if a legitimate current author source is available. |
| [GitLab](https://gitlab.com/) | en, ru, de, fr, es, pt | forge | pending | Resolve original project and public source; a mirror is not an independent resource. |
| [Codeberg](https://codeberg.org/) | en, de, fr | forge | pending | Same repository gates as GitHub; avoid platform bias. |
| [Gitee](https://gitee.com/) | zh-Hans | forge | pending | Establish upstream identity and license; distinguish original projects from mirrors. |
| [USENIX](https://www.usenix.org/) | en | conference | pending | Read full browser measurement/security paper and artifact; preserve experimental conditions. |
| [NDSS](https://www.ndss-symposium.org/) | en | conference | pending | Read full relevant paper, version and artifact; no venue-wide endorsement. |

## Coverage discipline

- Core lanes are searched at least every 7 days; all lanes at least every 28 days. A failed search is logged as a gap, not as proof no useful work exists.
- Daily discovery budget: 80% current topical work and 20% new sources/neglected lanes. These are effort allocations, never acceptance quotas.
- Review concentration when one publisher supplies more than 25% of new accepted entries, or GitHub consumes more than 50% of discovery effort. Primary reference necessities can justify an explicit exception. GitHub is a host, not a single author.
- Track topic, language, publisher, resource type, difficulty, browser/OS, stack, deployment model, license model, maturity and perspective. An apparent diversity improvement does not compensate for weak evidence.
- Source promotion requires at least 3 inspected relevant resources from the past year, at least 2 original technical contributions, identifiable authorship, and correction/version practices. A source with too little evidence remains a seed; individual excellent articles can still pass.
- Search local spellings, technical English loanwords, alternative terminology and original authors. For translations, preserve title/terms, quote short original passages only when needed and mark uncertain translation.
- When search is empty, use known public directories and author references through available authorized readers. Never bypass login/access restrictions or equate metadata with full-text inspection.

## Latest regional pass

[Latest-only review](reports/2026-09-13-latest-only.md) records the current catalogue boundary and remaining queue. Kanxue implementation threads were partially read; Viblo remained directory-only; the Russian-language Reverse4You forum and GitHub Following reads failed. Searches aimed at Vietnamese and Polish sources did not establish an eligible original. These are coverage gaps, not claims that a community lacks useful work.

## Approved expansion

[Policy 1.3](CURATION.md) allows bounded historical methods and small substantive artifacts. Source freshness still matters for current compatibility claims. The [approved-change report](reports/2026-09-13-approved-expansion.md) supersedes the old latest-only eligibility rule; earlier search logs remain historical observations.
