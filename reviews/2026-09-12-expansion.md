# R&D discovery log — 2026-09-12

No new initiative proposed. Existing decisions in [2026-09-09](2026-09-09.md#ideas-awaiting-manual-approval) remain unchanged: gap-map trial pending; separate provenance index and offline reproduction held. No implementation, source admission, or experiment in this R&D pass.

## Next ordinary search lane

Question: which browser inspection mechanisms change observations used in anti-bot research? This connects the existing engine instrumentation and detection sections. Closest existing source is Castle's Error.stack/CDP article. A scout can investigate one trace and its upstream revision, without creating a new index or benchmark. Strongest objection: drifting into generic debugger internals; require an explicit browser anti-bot measurement connection. Debugger detection must not be described as proof of bot identity.

## Queries actually run

All queries used the web search tool on 2026-09-12 with no date/recency filter; older methodological sources were deliberately eligible. Language coverage here is English, Russian and Vietnamese; search-language coverage does not imply an accepted original in that language.

1. `browser anti bot reverse engineering Error stack CDP detection V8 inspector original research`
2. `антибот reverse engineering CDP V8 детект браузера исследование`
3. `dịch ngược antibot fingerprint V8 CDP nghiên cứu`
4. `site.habr.com/ru/articles/ CDP антибот V8 исследование`
5. `"dịch ngược" "antibot"`

## Leads and limits

- [Sveba, How V8 Leaks Your Headless Browser's Identity](https://svebaa.github.io/personal/blog/cdp-fingerprinting/), English, page dated 2026-03-29. Full article read. It traces a prototype-chain Proxy through inspector preview code and reports a March 2026 content_shell build. Its own Implications section credits the existing Castle article; related lineage, not independent confirmation of Castle. Distinct potential value: a different preview path and source-level trace. HOLD: exact tested revision not established, upstream code links not inspected, broad behavior claims unreproduced; do not promote the article's vulnerability terminology or current compatibility. Scout evidence only, no independent gate pass.
- [V8 Inspector Security Framework, commit c195efb1d03b5171c376a02bca885c68792ae0f7](https://chromium.googlesource.com/v8/v8/+/c195efb1d03b5171c376a02bca885c68792ae0f7/src/inspector/SECURITY.md), English, full document read. Security Goals and Boundaries treats inspector detection as a non-goal; Reproductions explains that d8 behavior may differ from production and asks for inspector-test. This is a methodological cross-check, not independent experimental validation and not an assertion that the blog used d8. Publication date not checked. No admission proposed.
- [Habr 1054270](https://habr.com/ru/articles/1054270/) and [Habr 1063180](https://habr.com/ru/articles/1063180/), Russian: search-returned leads only; full articles/provenance not inspected, no factual claims adopted. First article and its AMP URL are one source. Broad anecdotes are not enough to infer vendor internals.
- Vietnamese searches produced no clearly relevant original methodological lead in the returned results. This is a bounded search outcome, not a claim no Vietnamese sources exist.

No access failures occurred for the two deliberately opened originals. Other returned search results were not fully inspected and remain unqualified leads; commercial summaries and generic debugger/security material were not followed.

## Council challenge

Sent to final_gatekeeper: investigate the above lane only under existing discovery scope; distinguish observation effects, bot attribution, and security-policy terminology; preserve all prior manual decisions. Gatekeeper response belongs in the managing editor's final debate packet. No addition is being submitted for gate passage here.
