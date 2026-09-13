![Awesome Anti-Bot Reverse Engineering](assets/banner.svg)

# Awesome Anti-Bot Reverse Engineering

Catalogue chọn lọc **chỉ nội dung hiện hành** để phân tích implementation anti-bot/CAPTCHA: AST/IR JavaScript, deobfuscation, hook browser engine, sensor/signing, fingerprint TLS/HTTP, predicate detection và challenge tính toán.

[English](README.md) · [Policy](CURATION.md) · [Nguồn](SOURCES.md) · [Ledger](data/resources.json) · [Báo cáo mới nhất](reports/2026-09-13-latest-only.md)

Hiện có **4 công cụ RE và 9 tài nguyên hỗ trợ trực tiếp; 0 mục được gắn `runtime-tested`**.

## Công cụ RE

- [webcrack](https://github.com/j4k0xb/webcrack) — AST deobfuscation và unpack bundle.
- [JSIR](https://github.com/google/jsir) — IR dựa trên MLIR cho data-flow và source transformation.
- [Firefox-Reverse](https://github.com/WhiteNightShadow/firefox-reverse) — hook SpiderMonkey/Gecko để quan sát signer, JSVMP và WASM.
- [Camoufox Reverse MCP](https://github.com/WhiteNightShadow/camoufox-reverse-mcp) — hook theo frame/world, capture source và so sánh signer offline.

Giới hạn, bằng chứng và ngày rà lại nằm trong [ledger](data/resources.json). Chín công cụ hỗ trợ cho PoW, quan sát browser, so sánh transport và đọc predicate detection nằm ở [SUPPORTING.md](SUPPORTING.md).

## Nguyên tắc latest-only

Chỉ nhận nguồn có cập nhật nội dung trong 365 ngày hoặc dự án living có tài liệu/trạng thái hiện tại. Không giữ case phiên bản cũ, mục thiếu documentation/artifact, marketing, integration quickstart, repost, solver market hoặc code không giải thích phương pháp.

Ngưỡng nhận là ≥85; scope và evidence đều ≥4/5. `working` cần phép thử runtime trong 30 ngày với version, môi trường, quy trình, expected/actual và bằng chứng công khai. PoW cần thuật toán, difficulty/parameter, verifier và test vector tái lập.

Vòng research: keyword/dork đa ngôn ngữ → nguồn gốc → code/PoC/trace/protocol → related links tối đa ba cạnh → chống trùng lineage → chấm điểm hoài nghi → cập nhật đồng bộ. Xem [roadmap](docs/RE_CATALOG_ROADMAP.md), [watchlist](WATCHLIST.md) và [runbook](docs/AUTOMATION.md).
