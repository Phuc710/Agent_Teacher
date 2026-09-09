# Quy Trình Bóc Tách YouTube & Tài Liệu Kỹ Thuật (Ingestion & Concept Extraction)

Tài liệu này quy định cách Agent xử lý khi học viên gửi vào:
- Một đường dẫn video YouTube hoặc transcript của video.
- Tài liệu kỹ thuật, Datasheet, Reference Manual, hoặc bài báo chuyên ngành (PDF/Markdown).

Mục tiêu: **Biến nội dung thô (raw transcript / doc) thành một chuỗi khái niệm có cấu trúc chặt chẽ, liên kết với Cây Tri Thức (Knowledge Graph) để phục vụ giảng dạy.**

---

## 1. Các Tình Huống Đầu Vào & Cách Xử Lý

### Tình huống A: Học viên dán Transcript trực tiếp hoặc dán văn bản trích xuất từ YouTube
- Agent trực tiếp bóc tách nội dung văn bản.

### Tình huống B: Học viên gửi URL YouTube (`https://youtube.com/watch?v=...`)
- Nếu Agent có công cụ truy cập web/fetch nội dung hoặc học viên cung cấp transcript kèm theo: tiến hành phân tích ngay.
- Nếu không thể tự động lấy transcript tự động do giới hạn mạng/công cụ: Agent yêu cầu học viên xuất transcript nhanh (bằng công cụ YouTube hoặc tiện ích) hoặc dán tóm tắt nội dung chính của video để Agent bắt đầu pipeline.

---

## 2. Quy Trình Bóc Tách 4 Bước (The 4-Step Extraction Pipeline)

```
[Raw Input: Transcript / Video / Doc]
              │
              ▼
   1. Bóc Tách Râu Ria (Denoise & Filter)
      (Bỏ intro, quảng cáo, câu chào, lời bông đùa)
              │
              ▼
   2. Trích Xuất Khái Niệm Cốt Lõi (Core Concepts)
      (Hardware target, Registers, Algorithms, Idioms)
              │
              ▼
   3. Tra Cứu Cây Tri Thức & Prerequisites
      (Đối chiếu knowledge-graph.md)
              │
              ▼
   4. Xác Định Mục Tiêu Học Tập & Đẩy Vào Phase 2
      (Xuất cấu trúc bài học 6 tầng tương ứng)
```

---

## 3. Định Dạng Chuẩn Hóa Sau Khi Phân Tích (Extraction Output Spec)

Sau khi xử lý nội dung từ YouTube/Tài liệu, Agent luôn tổng hợp ngắn gọn theo định dạng sau trước khi bắt đầu bài giảng:

```markdown
### Phân Tích Nguồn Học Tập (Source Analysis)
- **Chủ đề chính:** [Ví dụ: Cơ chế ngắt và ngoại lệ trên ARM Cortex-M]
- **Target Hardware / Architecture:** [Ví dụ: STM32F4 / ARM Cortex-M4]
- **Khái niệm then chốt trong video:**
  1. Interrupt vs Polling
  2. NVIC (Nested Vectored Interrupt Controller)
  3. Vector Table & Exception Entry Context Save
  4. ISR (Interrupt Service Routine) & Pending Bit Clearing
- **Kiểm tra Điều kiện tiên quyết (Prerequisites Check):**
  - C Pointer & Struct alignment: [✓ Đã nắm / ⚠ Cần lưu ý]
  - Volatile keyword: [✓ Đã nắm]
  - CPU Registers (SP, LR, PC): [⚠ Chưa vững -> Cần giải thích ngắn trong bài]
- **Mục tiêu đầu ra sau buổi học:** Tự cấu hình ngắt bare-metal không qua thư viện HAL, hiểu rõ luồng phần cứng từ lúc chân pin đổi mức đến khi CPU nhảy vào ISR.
```

Sau khi xuất bảng phân tích này, Agent lập tức chuyển sang **Phase 2: Tổng Hợp Lý Thuyết 6 Tầng Chuẩn Phần Cứng**.
