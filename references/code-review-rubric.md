# Bộ Tiêu Chuẩn Code Review & Đánh Giá Năng Lực Chuẩn Senior (Rubric & Assessment)

Trong kỹ thuật C++ và Lập trình nhúng (Embedded Systems), **"code chạy được" không đồng nghĩa với "code đúng" hay "học viên đã hiểu"**. 

Một chương trình chạy trơn tru trong phòng lab hoàn toàn có thể gây treo CPU (HardFault) ngoài hiện trường do:
- Thiếu từ khóa `volatile` bị compiler nuốt mất lệnh đọc thanh ghi khi bật cờ tối ưu `-O2/-O3`.
- Tràn Stack Frame trong ngắt (ISR).
- Race condition giữa ngắt và vòng lặp chính.
- Xóa cờ ngắt muộn khiến CPU liên tục bị ngắt đệ quy lặp vô tận (Interrupt storm).

Tài liệu này chuẩn hóa quy trình **Senior Code Review** và **Bộ Câu Hỏi Đánh Giá Năng Lực (Assessment Battery)**.

---

## 1. Thang Điểm & 4 Trục Đánh Giá (The 4-Pillar Evaluation)

Khi học viên nộp code, Agent bắt buộc phải chấm điểm từ 0 đến 100 theo 4 trục:

| Trục Đánh Giá | Trọng Số | Tiêu Chí Đo Lường |
|---|---|---|
| **1. Understanding (Thấu hiểu bản chất)** | 30% | Học viên có hiểu phần cứng/compiler đang làm gì bên dưới không? Có nắm được Vector Table, context save, thứ tự khởi tạo phần cứng không? |
| **2. Implementation (Kỹ năng hiện thực)** | 30% | Code có sạch không? Đúng chuẩn C++17/20 hoặc Bare-metal không? Có vi phạm Memory Leak, Dangling Pointer, Non-atomic access, Clobbering không? |
| **3. Debugging & Edge Cases (Xử lý lỗi & Biên)** | 20% | Đã xử lý cờ ngắt, timeout, overflow, unaligned access chưa? Có tự bẫy lỗi bằng `assert` hoặc fault handler không? |
| **4. Mental Model (Tư duy kiến trúc hệ thống)** | 20% | Phân định ranh giới giữa ISR và Main rõ ràng không? Có nhồi nhét delay/printf vào ISR không? Có chọn đúng mô hình dữ liệu (SPSC queue, double-buffering) không? |

---

## 2. Quy Trình Xuất Bản Code Review (Output Format)

Mỗi lần review code phải xuất bản theo cấu trúc chặt chẽ sau:

```markdown
# Senior Code Review

## Tổng Điểm Thấu Hiểu: [Score]/100
- Understanding: [xx]/100
- Implementation: [xx]/100
- Debugging: [xx]/100
- Mental Model: [xx]/100

### Điểm Mạnh (Strong Points)
✓ [Những gì học viên đã nắm vững, ví dụ: Hiểu rõ cơ chế ánh xạ thanh ghi qua struct volatile]
✓ [Cấu hình NVIC đúng thứ tự ưu tiên]

### Điểm Yếu & Rủi Ro Tiềm Ẩn (Weak Points & Latent Bugs)
⚠ [Chỉ ra lỗi nghiêm trọng: ví dụ: Biến chia sẻ giữa ISR và main() thiếu volatile / std::atomic]
⚠ [ISR thực hiện phép toán quá nặng gây nghẽn hệ thống]
⚠ [Chưa xóa cờ pending trước khi thoát ISR dẫn đến ngắt lặp vô tận]

### Phân Tích Chuyên Sâu Cấp Độ Hợp Ngữ & Trình Biên Dịch (Assembly & Compiler Impact)
[Giải thích ngắn gọn đoạn code này khi GCC/Clang biên dịch với cờ -O3 sẽ sinh ra mã máy thế nào, có nguy cơ bị reorder instruction hoặc omit read không]

### Gợi Ý Tối Ưu Hóa Chuẩn Senior (Refactored Snippet)
```cpp
// Trích đoạn code sửa lại chuẩn, kèm chú thích giải thích TẠI SAO
```
```

---

## 3. Bộ Câu Hỏi Phản Biện Chuyên Sâu (Deep Assessment Questions)

Để chắc chắn học viên **không học vẹt hay nhờ AI viết hộ**, sau phần Code Review, Agent bắt buộc phải đặt ra **3 đến 5 câu hỏi sát hạch** chia thành 3 tầng:

### Tầng 1: Bản Chất Kiến Trúc (Architecture & Concept)
- *Mục tiêu:* Kiểm tra học viên có hiểu dòng chảy vật lý của phần cứng không.
- *Ví dụ mẫu:*
  - "Ai là người trực tiếp gọi hàm `EXTI0_IRQHandler`? CPU biết địa chỉ hàm này nằm ở đâu trong bộ nhớ Flash?"
  - "Hàm `main()` của bạn được gọi từ đâu? Trước khi `main()` chạy thì thanh ghi `SP` (Stack Pointer) đã được nạp giá trị gì?"
  - "Khi CPU đang thực thi dở một lệnh số học trong `main()` mà có ngắt xảy ra, CPU xử lý lệnh đó ra sao trước khi nhảy vào ISR?"

### Tầng 2: Đột Biến Mã Nguồn (Code Mutation — "Nếu bỏ dòng này...?")
- *Mục tiêu:* Kiểm tra xem từng dòng code có thực sự mang tính chất "sống còn" đối với học viên không.
- *Ví dụ mẫu:*
  - "Nếu bỏ dòng `EXTI->PR = EXTI_PR_PR0;` (xóa cờ pending) ở cuối ISR thì hiện tượng gì sẽ xảy ra trên MCU? CPU có quay về được `main()` không?"
  - "Tại sao biến `flag` chia sẻ giữa ISR và `main()` phải có từ khóa `volatile`? Nếu tôi xóa chữ `volatile` và biên dịch với cờ `-O3`, hãy dự đoán chính xác hành vi của vòng lặp `while(!flag)` trong `main()`?"
  - "Nếu bỏ `volatile` trên con trỏ trỏ tới thanh ghi ngoại vi GPIO, compiler có quyền làm gì với thao tác ghi liên tiếp 2 lần vào thanh ghi?"

### Tầng 3: Kịch Bản Gỡ Lỗi Ngoài Thực Tế (Debugging Scenarios)
- *Mục tiêu:* Kiểm tra phản xạ gỡ lỗi phần cứng.
- *Ví dụ mẫu:*
  - "Sau khi nạp code của bạn vào chip, LED không bao giờ sáng khi bấm nút. Hãy liệt kê quy trình 4 bước kiểm tra lần lượt từ: *Nguồn cấp chân vật lý → Clock RCC → Cấu hình GPIO Mode → Kích hoạt NVIC & Vector Table*."
  - "Hệ thống chạy được 10 phút thì rơi vào `HardFault_Handler`. Bạn sẽ đọc những thanh ghi nào trong Stack Frame để tìm ra địa chỉ câu lệnh (PC) đã gây ra lỗi?"

---

## 4. Báo Cáo Tổng Kết Đánh Giá (Learning Report Standard Format)

Khi kết thúc một bài học hoặc chủ đề, Agent xuất bản `LEARNING REPORT`:

```
╔══════════════════════════════════════════════════════════════╗
║                     LEARNING REPORT                          ║
╚══════════════════════════════════════════════════════════════╝
Chủ đề: [Tên Chủ Đề, ví dụ: Interrupt & Exception trên Cortex-M]
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

## Cần Bổ Sung / Lỗ Hổng Kiến Thức (Gaps & Weaknesses)
⚠ [Khái niệm C: Cần hiểu sâu thêm về exception entry context save]
⚠ [Khái niệm D: Cần nắm chắc Memory Barrier]

## Khuyến Nghị Lộ Trình Tiếp Theo (Next Path Recommendation)
- [ĐƯỢC PHÉP HỌC TIẾP / KHUYÊN ÔN TẬP]
- Nếu học tiếp: Khái niệm [X] (vì đã đủ điều kiện tiên quyết).
- Nếu bị chặn: ❌ CHƯA NÊN HỌC [Y] vì kiến thức [Z] chưa đạt mức 75/100.
```
