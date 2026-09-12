# Awesome Anti-Bot Reverse Engineering — tiếng Việt

[Case RE và công cụ](README.md) · [Tài liệu hỗ trợ](SUPPORTING.md) · [Nguồn đa ngôn ngữ](SOURCES.md) · [Tiêu chí](CURATION.md)

Trọng tâm repo là **bóc tách cách anti-bot được triển khai**: deobfuscation JavaScript, VM/JSVMP, sensor, thuật toán ký, anti-debug, quan sát browser engine và phân tích giao thức. Mục chính phải chỉ ra đối tượng RE, phương pháp và mã/trace/bài phân tích đã đọc.

Danh sách hiện có case Akamai BMP/XP1M/Bot Manager 2.0, một snapshot Cloudflare JS challenge năm 2023, RE implementation của reCAPTCHA 2014, Imperva Reese84, AWS WAF, Trip.com, VM của một marketplace và Douyin. Case Cloudflare kết hợp hook runtime với Babel AST; InsideReCaptcha có disassembler/decompiler bytecode và phân tích XTEA nhưng là historical snapshot, không phải bypass hiện tại. Công cụ được nhóm theo AST/IR và instrumentation. Catalogue còn **10 case RE, 4 công cụ RE và 9 tài liệu hỗ trợ trực tiếp**. Trang hỗ trợ chỉ giữ công cụ quan sát, so sánh transport, đọc predicate detection và phân tích challenge tính toán; mỗi mục ghi rõ công dụng RE. Đã bỏ 12 mục nền tảng/tích hợp/benchmark chưa gắn với implementation RE và 10 file tổ chức, điều hướng trùng lặp.

**Nguồn cũ vẫn có giá trị RE.** Ưu tiên bài trong 365 ngày, nhưng một nghiên cứu phiên bản cụ thể được xét là snapshot nếu phương pháp có bằng chứng, mẫu hoặc phiên bản được xác định và giới hạn được ghi rõ. Không biến nghiên cứu cũ thành hướng dẫn đang chạy được. Ngày đọc, ngày công bố, phiên bản mẫu và ngày test là các trường riêng.

**Kiểm chứng có phạm vi.** Source-reviewed là đã đọc nội dung gốc liên quan; code-reviewed ghi chính xác file/commit và phần mã đã xem, không đồng nghĩa audit toàn repo. Runtime-tested cần môi trường, phiên bản, bước thử, expected/actual và bằng chứng trong 30 ngày. Đợt sửa 2026-09-12 không chạy công cụ RE trên mục tiêu thực và không cấp nhãn runtime-tested.

**Đa dạng có chọn lọc.** Giữ 16 luồng ngôn ngữ và 33 kênh khám phá; en, ru, zh-Hans là ngôn ngữ của các mục hiện được nhận. Đọc một directory không có nghĩa đã đọc bài gốc; tên repo, tên tác giả và ngôn ngữ không chứng minh quốc tịch. Không nâng điểm để đủ số mục hoặc ngôn ngữ.

Vòng cập nhật: tìm theo case/phương pháp RE → đọc nguồn → theo references/related/code → chống trùng → chấm điểm → tự phản biện → cập nhật README, ledger và queue. Mười tuyến RE có mục tiêu khám phá khoảng 50 hồ sơ mỗi tuyến trong [roadmap](docs/RE_CATALOG_ROADMAP.md), nhưng đây không phải quota nhận bài. `working` và PoW cần bằng chứng tái lập riêng. Ngưỡng vẫn ≥85 và phải qua mọi gate. Xem [báo cáo lọc scope và nguồn khu vực](reports/2026-09-12-scope-and-regional-review.md), [báo cáo CAPTCHA/RE](reports/2026-09-12-captcha-research.md), [báo cáo Cloudflare snapshot](reports/2026-09-12-cloudflare-habr.md), [báo cáo sửa trọng tâm](reports/2026-09-12-re-focus.md) và [lịch duy trì](docs/AUTOMATION.md).
