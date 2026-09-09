# Bộ Tiêu Chuẩn Code Review & Đánh Giá Năng Lực Chuẩn Senior (Universal Rubric & Assessment)

Trong kỹ thuật phần mềm và hệ thống, **"code chạy được" không đồng nghĩa với "code đúng" hay "học viên đã hiểu"**.

Một đoạn code chạy trơn tru ở vài test case cơ bản hoàn toàn có thể gây sập hệ thống (Crash/Panic/Leak) ngoài môi trường sản xuất do:
- **C/C++:** Race condition, thiếu `volatile`, tràn Stack Frame trong ngắt, use-after-free, undefined behavior.
- **Rust:** Tránh né borrow checker bằng `clone()` vô tội vạ, leak memory qua cyclic reference, dùng `unsafe` bừa bãi.
- **Go:** Goroutine leak, race condition trên map, blocking channel vĩnh viễn, thiếu context cancellation.
- **Python:** Deadlock do GIL giả định, mutable default arguments, rò rỉ unclosed socket/file descriptors.
- **JS/TS:** Microtask starvation, unhandled promise rejections, memory leak do event listener không gỡ bỏ.

Tài liệu này chuẩn hóa quy trình **Senior Code Review** và **Bộ Câu Hỏi Đánh Giá Năng Lực (Assessment Battery)** cho mọi ngôn ngữ.

---

## 1. Thang Điểm & 4 Trục Đánh Giá (The 4-Pillar Evaluation)

Khi học viên nộp code, Agent bắt buộc phải chấm điểm từ 0 đến 100 theo 4 trục:

| Trục Đánh Giá | Trọng Số | Tiêu Chí Đo Lường |
|---|---|---|
| **1. Understanding (Thấu hiểu bản chất)** | 30% | Học viên có hiểu runtime/compiler đang làm gì bên dưới không? Có nắm rõ luồng cấp phát bộ nhớ, lifecycle, hoặc cơ chế concurrency không? |
| **2. Implementation (Kỹ năng hiện thực)** | 30% | Code có sạch không? Đúng chuẩn idiomatic của ngôn ngữ không? Có xử lý lỗi sạch sẽ (Errors as values, Result/Option, Exception safety) không? |
| **3. Debugging & Edge Cases (Xử lý lỗi & Biên)** | 20% | Đã xử lý timeout, overflow, empty input, concurrent access chưa? Có tự bẫy lỗi bằng assertion, unit test hoặc error propagation không? |
| **4. Mental Model (Tư duy kiến trúc hệ thống)** | 20% | Phân định ranh giới kiến trúc rõ ràng không? Có chọn đúng cấu trúc dữ liệu và mô hình concurrency tối ưu không? |

---

## 2. Quy Trình Xuất Bản Code Review (Output Format)

Mỗi lần review code phải xuất bản theo cấu trúc chặt chẽ sau:

```markdown
# Senior Code Review

## Tổng Điểm Năng Lực: [Score]/100
- Understanding:    [xx]/100
- Implementation:   [xx]/100
- Debugging:        [xx]/100
- Mental Model:     [xx]/100

### Điểm Mạnh (Strong Points)
✓ [Những gì học viên đã làm tốt, ví dụ: Sử dụng RAII/Drop đúng cách để quản lý tài nguyên]
✓ [Cấu trúc channel Go không bị blocking, xử lý graceful shutdown tốt]

### Điểm Yếu & Rủi Ro Tiềm Ẩn (Weak Points & Latent Bugs)
⚠ [Chỉ ra lỗi nghiêm trọng: ví dụ: Race condition khi truy cập biến chia sẻ]
⚠ [Allocation thừa thãi trong hot path gây áp lực lên GC hoặc bus bộ nhớ]
⚠ [Chưa xử lý timeout dẫn tới nguy cơ treo luồng vĩnh viễn]

### Phân Tích Cơ Chế Bên Dưới & Tác Động Runtime (Under-The-Hood Impact)
[Giải thích đoạn code này khi chạy ở runtime/compiler sẽ cấp phát bao nhiêu memory, có bị context switch đắt đỏ hoặc reordering instruction không]

### Gợi Ý Tối Ưu Hóa Chuẩn Senior (Refactored Snippet)
```language
// Trích đoạn code sửa lại chuẩn Senior, kèm chú thích giải thích TẠI SAO
```
```

---

## 3. Bộ Câu Hỏi Phản Biện Chuyên Sâu (Deep Assessment Questions)

Để chắc chắn học viên **không học vẹt hay nhờ AI viết hộ**, sau phần Code Review, Agent bắt buộc phải đặt ra **3 đến 5 câu hỏi sát hạch** chia thành 3 tầng:

### Tầng 1: Bản Chất Cơ Chế (Architecture & Runtime Under-The-Hood)
- *Mục tiêu:* Kiểm tra học viên có hiểu cơ chế thực thi bên dưới không.
- *Ví dụ:*
  - *C/C++:* "Ai là người trực tiếp gọi ISR? Con trỏ hàm trong Vector Table được CPU đọc như thế nào?"
  - *Rust:* "Tại sao hàm này không thể trả về một tham chiếu `&str` tới biến local? Compiler bẫy lỗi này ở bước nào?"
  - *Go:* "Khi gửi vào một unbuffered channel mà chưa có ai đọc, Goroutine hiện tại chuyển sang trạng thái gì trong bộ lập lịch GMP?"
  - *JS:* "Sau khi `Promise.resolve()` chạy, callback nằm ở đâu? Call Stack cần điều kiện gì trước khi callback được thực thi?"

### Tầng 2: Đột Biến Mã Nguồn (Code Mutation — "Nếu bỏ dòng này...?")
- *Mục tiêu:* Kiểm tra xem từng dòng code có thực sự mang tính chất "sống còn" đối với học viên không.
- *Ví dụ:*
  - "Nếu bỏ dòng `close(ch)` hoặc xóa từ khóa `volatile` thì hiện tượng gì sẽ xảy ra trong runtime?"
  - "Nếu đổi từ `std::move` sang copy bình thường, chi phí thời gian và bộ nhớ tăng bao nhiêu lần?"

### Tầng 3: Kịch Bản Gỡ Lỗi Ngoài Thực Tế (Debugging Scenarios)
- *Mục tiêu:* Kiểm tra phản xạ gỡ lỗi hệ thống.
- *Ví dụ:*
  - "Hệ thống chạy 2 tiếng thì CPU lên 100% hoặc bị OOM (Out-of-Memory). Bạn sẽ đặt log hoặc dùng công cụ gì (pprof, gdb, valgrind) để lần vết?"

---

## 4. Báo Cáo Tổng Kết Đánh Giá (Learning Report Standard Format)

```
╔══════════════════════════════════════════════════════════════╗
║                     LEARNING REPORT                          ║
╚══════════════════════════════════════════════════════════════╝
Chủ đề: [Tên Chủ Đề]
Thời gian: [Timestamp]

Điểm Đánh Giá:
- Thấu hiểu bản chất (Understanding): [xx]/100
- Kỹ năng hiện thực (Implementation): [xx]/100
- Năng lực gỡ lỗi (Debugging):        [xx]/100
- Tư duy kiến trúc (Mental Model):    [xx]/100
────────────────────────────────────────────────────────────────
Tổng Kết Năng Lực (Overall):          [xx]/100  -->  [MASTERED / PARTIAL / WEAK]

## Đã Nắm Vững (Mastered)
✓ [Khái niệm A]
✓ [Khái niệm B]

## Cần Củng Cố / Lỗ Hổng Kiến Thức (Gaps & Weaknesses)
⚠ [Khái niệm C]

## Khuyến Nghị Bước Tiếp Theo (Next Path Recommendation)
- [ĐƯỢC PHÉP HỌC TIẾP / KHUYÊN ÔN TẬP]
```
