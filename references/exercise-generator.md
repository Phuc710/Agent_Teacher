# Quy Chuẩn Sinh Bài Tập 3 Cấp Độ (3-Level Progressive Exercise Generator)

Một kỹ sư Senior không học bằng cách trả lời trắc nghiệm lý thuyết. Phải bắt tay vào viết code từ mức logic ngữ pháp cơ bản cho đến mức đào sâu tận gốc cơ chế bên dưới (Under-the-Hood / Zero-framework).

Mỗi khi kết thúc bài giảng lý thuyết, Agent bắt buộc phải xuất bộ bài tập gồm 3 cấp độ tăng tiến rõ rệt:

---

## Cấu Trúc 3 Cấp Độ Bài Tập Đa Ngôn Ngữ

```
LEVEL 1: CORE MECHANICS (Nắm vững cú pháp chuẩn & Logic cơ bản)
  │
  ▼
LEVEL 2: REAL-WORLD & CONSTRAINTS (Bài toán thực tế, ràng buộc tài nguyên & concurrency)
  │
  ▼
LEVEL 3: UNDER-THE-HOOD / ZERO-FRAMEWORK (Tự viết từ đáy, không thư viện ngoài)
```

---

### Cấp Độ 1: Level 1 — Core Mechanics (Nắm vững cú pháp chuẩn & Logic cơ bản)
- **Mục tiêu:** Học viên nắm vững cú pháp chuẩn (*idiomatic syntax*), luồng dữ liệu và API cốt lõi của ngôn ngữ.
- **Yêu cầu kỹ thuật:**
  - Viết code chuẩn ngữ pháp (Modern C++, Safe Rust, Idiomatic Go, Pythonic, TypeScript strict).
  - Có hàm kiểm thử hoặc test harness chạy thử in log rõ ràng.
- *Ví dụ mẫu:*
  - *C/C++:* Viết chương trình mô phỏng ngắt bằng function pointer và thread.
  - *Rust:* Triển khai một Struct quản lý file descriptor có cài đặt trait `Drop` để tự động giải phóng tài nguyên.
  - *Go:* Viết worker pool 5 worker xử lý 100 task qua channel và `sync.WaitGroup`.
  - *Python:* Viết custom context manager (`__enter__`, `__exit__`) đo thời gian thực thi tác vụ.
  - *JS/TS:* Viết hàm debounce / throttle bằng Promise và async/await.

---

### Cấp Độ 2: Level 2 — Real-World & Constraints (Ràng buộc thực tế & Hiệu năng)
- **Mục tiêu:** Áp dụng vào kịch bản sản xuất có ràng buộc về tài nguyên, độ trễ, đa luồng hoặc xử lý lỗi phức tạp.
- **Yêu cầu kỹ thuật:**
  - Xử lý triệt để các edge cases: timeout, graceful shutdown, memory leak, race condition, data corruption.
  - Áp dụng các mẫu thiết kế chuẩn (*Pattern*) của ngôn ngữ.
- *Ví dụ mẫu:*
  - *C/C++ & Nhúng:* Cấu hình trực tiếp thanh ghi ngoại vi GPIO/UART qua bitwise trên MCU mà không dùng HAL.
  - *Rust:* Triển khai Concurrent Cache có thời hạn (TTL) dùng `Arc<RwLock<HashMap>>` mà không bị deadlock.
  - *Go:* Xây dựng Rate Limiter (Token Bucket algorithm) thread-safe chỉ dùng channel và time.Ticker.
  - *Python:* Xây dựng Async Task Queue xử lý retry có backoff bằng `asyncio.Queue` và Worker coroutines.
  - *JS/TS:* Xây dựng Observable / EventEmitter tự quản lý memory leak và unsubscribe.

---

### Cấp Độ 3: Level 3 — Under-the-Hood / Zero-Framework (Tự viết từ đáy)
- **Mục tiêu:** Chứng minh thấu hiểu bản chất bằng cách **tự tay viết lại cơ chế mà thông thường người ta phải mượn framework hoặc thư viện ngoài**.
- **Yêu cầu kỹ thuật:**
  - Zero third-party dependencies (Không dùng thư viện ngoài).
  - Tối ưu hóa kích thước bộ nhớ, số lần allocation, và chu kỳ xử lý.
- *Ví dụ mẫu:*
  - *C/C++:* Viết startup code và bảng vector ngắt từ con số 0; hoặc viết Lock-Free SPSC Queue dùng `std::atomic` và cacheline alignment.
  - *Rust:* Viết một phiên bản tí hon của `Rc<T>` hoặc `Vec<T>` tự quản lý raw pointer và layout memory an toàn.
  - *Go:* Viết một HTTP/1.1 Server mini chỉ dùng `net.Listen` của socket TCP, tự parse request header và HTTP response stream.
  - *Python:* Tự viết Event Loop mini bằng generator (`yield`) và `select/epoll` mà không dùng thư viện `asyncio`.
  - *JS/TS:* Tự viết lại toàn bộ `Promise` (A+ Specification: `then`, `catch`, trạng thái pending/fulfilled/rejected).

---

## Tự Động Scaffold File Làm Bài

Mỗi khi giao bài tập:
1. Agent tự động gọi `python scripts/lab_manager.py --create <lab_id> --name "<Tên bài tập>"` để tạo thư mục `labs/<lab_id>/`.
2. Tạo sẵn file `README.md` (yêu cầu chi tiết) và file code template rỗng trong `labs/<lab_id>/src/` với các comment `// TODO` rõ ràng.
3. Học viên chỉ cần mở file trong IDE và gõ code nộp bài.
