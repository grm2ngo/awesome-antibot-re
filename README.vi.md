![Awesome Anti-Bot Reverse Engineering](assets/banner.svg)

# Awesome Anti-Bot Reverse Engineering

Catalogue chọn lọc **dựa trên bằng chứng** để phân tích implementation anti-bot/CAPTCHA: AST/IR JavaScript, deobfuscation, hook browser engine, sensor/signing, fingerprint TLS/HTTP, predicate detection và challenge tính toán.

[English](README.md) · [Policy](CURATION.md) · [Nguồn](SOURCES.md) · [Ledger](data/resources.json) · [Báo cáo mới nhất](reports/2026-09-13-dkaptcha-review.md)

Hiện có **4 công cụ RE và 9 tài nguyên hỗ trợ trực tiếp; 0 mục được gắn `runtime-tested`**.

## Công cụ RE

- [webcrack](https://github.com/j4k0xb/webcrack) — AST deobfuscation và unpack bundle.
- [JSIR](https://github.com/google/jsir) — IR dựa trên MLIR cho data-flow và source transformation.
- [Firefox-Reverse](https://github.com/WhiteNightShadow/firefox-reverse) — hook SpiderMonkey/Gecko để quan sát signer, JSVMP và WASM.
- [Camoufox Reverse MCP](https://github.com/WhiteNightShadow/camoufox-reverse-mcp) — hook theo frame/world, capture source và so sánh signer offline.

Giới hạn, bằng chứng và ngày rà lại nằm trong [ledger](data/resources.json). Chín công cụ hỗ trợ cho PoW, quan sát browser, so sánh transport và đọc predicate detection nằm ở [SUPPORTING.md](SUPPORTING.md).

## Tiêu chí đã mở rộng

Nhận nguồn mới trong 365 ngày, dự án còn hoạt động, và nghiên cứu cũ có giá trị phương pháp. Nguồn cũ phải ghi rõ mẫu/phiên bản hoặc artifact, phần còn đáng học và giới hạn; không suy ra khả năng chạy hiện tại.

Một script nhỏ, handler VM, trace, PoC hoặc bài kỹ thuật X/CSDN cũng có thể đạt chuẩn; không cần dự án hoàn chỉnh hay README đẹp. Vẫn phải đọc nguồn gốc, giải thích cơ chế và kiểm chứng độc lập.

**Useful: 80 đến dưới 85; Gold: từ 85.** Cả hai giữ scope/evidence ≥4/5 và toàn bộ điều kiện bằng chứng. Không tự nâng hạng nguồn chưa kiểm tra. `working` vẫn cần thử nghiệm runtime trong 30 ngày; PoW vẫn cần thuật toán, tham số, verifier và vector tái lập.

Vòng research: keyword/dork đa ngôn ngữ → nguồn gốc → code/PoC/trace/protocol → related links tối đa ba cạnh → chống trùng lineage → chấm điểm hoài nghi → cập nhật đồng bộ. Xem [roadmap](docs/RE_CATALOG_ROADMAP.md), [watchlist](WATCHLIST.md) và [hướng dẫn bảo trì công khai](docs/AUTOMATION.md).
