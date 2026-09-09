<div align="center">
  <h1>AgentTeacher — Senior C++ & Systems Edition</h1>
  <p><b>Hệ Thống Cố Vấn, Giảng Dạy & Sát Hạch Năng Lực Lập Trình Nhúng & C++ Chuẩn Senior</b></p>
  <p><a href="README.vi.md"><b>Tiếng Việt (Khuyên Dùng)</b></a> · <a href="README.md"><b>English</b></a></p>
  <p>
    <img src="https://img.shields.io/badge/Ngôn%20ngữ-Modern%20C%2B%2B20%20%7C%20C-00599C?style=flat-square&logo=c%2B%2B" alt="C++">
    <img src="https://img.shields.io/badge/Kiến%20trúc-ARM%20Cortex--M%20%7C%20STM32-0091BD?style=flat-square&logo=arm" alt="ARM">
    <img src="https://img.shields.io/badge/Chuyên%20sâu-Bare--Metal%20%7C%20RTOS-E95420?style=flat-square" alt="Domain">
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">
    <img src="https://img.shields.io/badge/Skill-AgentTeacher-blueviolet?style=flat-square" alt="Skill">
  </p>
</div>

---

## Triết Lý Giảng Dạy: Bản Chất Phần Cứng & Mã Máy

Khác biệt hoàn toàn với các chatbot đọc định nghĩa từ điển hoặc tóm tắt lý thuyết suông:
- **Không học vẹt:** Không bắt đầu bằng *"Interrupt là cơ chế...", "RAII là một mẫu thiết kế..."*.
- **Xuất phát từ vật lý & phần cứng:** Bắt đầu từ bế tắc kỹ thuật của CPU, bus dữ liệu, hoặc tối ưu hóa của trình biên dịch: *"CPU bị nghẽn 100% khi polling UART", "Move semantics biến thao tác cấp phát Heap $O(N)$ thành hoán đổi con trỏ $O(1)$"*.
- **Soi tận thanh ghi & Assembly:** Kiểm tra ánh xạ mã máy sinh ra bởi GCC/Clang (`-O2/-O3`), cảnh báo bẫy mất lệnh do thiếu `volatile`, lỗi tràn Stack Frame trong ngắt, và race condition.
- **Code chạy chưa phải là đúng:** Code chạy trong phòng lab vẫn có thể gây HardFault trên chip thật. Agent chỉ công nhận khi học viên vượt qua bộ câu hỏi phản biện chuyên sâu.

---

## Chu Trình Học Tập 6 Phase Khép Kín (The 6-Phase Engineering Loop)

```
┌─────────────────────────────────────────────────────────────┐
│ 1. INGESTION & CONCEPT EXTRACTION                           │
│    Học viên gửi: Video YouTube, Transcript, Datasheet, Topic│
│    Agent: Bóc tách khái niệm + Kiểm tra Prerequisites        │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. THEORY SYNTHESIS (LÕI 6 TẦNG BẢN CHẤT PHẦN CỨNG)         │
│    Intuition → Mental Model / Sơ đồ bộ nhớ → Code & ASM     │
│    → Walkthrough → Bẫy hệ thống / UB → Pointers             │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. 3-LEVEL PROGRESSIVE EXERCISES                            │
│    Level 1: Logic & Host Simulation trên PC (C++20)         │
│    Level 2: Target & Register Mapping (Thanh ghi ngoại vi)  │
│    Level 3: Zero-HAL / Bare-Metal Master (Không thư viện)   │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. HỌC VIÊN CODE & NỘP BÀI                                  │
│    Dán mã nguồn hoặc gửi link Git repo                      │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. SENIOR CODE REVIEW & BỘ CÂU HỎI PHẢN BIỆN CHUYÊN SÂU     │
│    Chấm 4 trục (Understanding / Impl / Debug / Mental Model)│
│    Hỏi 3 tầng: Concept → Code Mutation ("Nếu bỏ dòng này..")│
│    → Debug Scenarios ("Hệ thống rơi vào HardFault..")       │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. LEARNING REPORT & CẬP NHẬT KNOWLEDGE GRAPH               │
│    Xuất báo cáo năng lực + Cập nhật learning_profile.json   │
│    Đề xuất học tiếp hoặc khóa cổng nếu hổng nền tảng        │
└─────────────────────────────────────────────────────────────┘
```

---

## Cấu Trúc Repository

| Tệp / Thư Mục | Vai Trò Kỹ Thuật |
|---|---|
| [SKILL.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/SKILL.md) | Điểm kích hoạt skill: Định nghĩa chu trình 6 Phase, trigger phrases và hợp đồng output |
| [AGENTS.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/AGENTS.md) | Chỉ dẫn vận hành cho Agent: Quy tắc chấm điểm, phong cách Mentor, hard stops |
| [CLAUDE.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/CLAUDE.md) | Hướng dẫn tóm tắt cho Claude Code |
| `references/` | **Kho Cẩm Nang Kỹ Thuật & Sổ Tay Giảng Dạy**: |
| ├── [knowledge-graph.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/knowledge-graph.md) | Cây tri thức 24 Node cốt lõi (C, C++, Arch/ASM, Embedded, RTOS, Lock-free) & Ma trận phụ thuộc |
| ├── [teaching-method.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/teaching-method.md) | Sổ tay phương pháp giảng dạy 6 tầng chuẩn Phần cứng/Bộ nhớ |
| ├── [exercise-generator.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/exercise-generator.md) | Tiêu chuẩn xuất đề bài tập 3 Cấp độ tăng tiến |
| ├── [code-review-rubric.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/code-review-rubric.md) | Bảng tiêu chí Code Review 4 trục và Bộ câu hỏi phản biện 3 tầng |
| ├── [youtube-ingestion.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/youtube-ingestion.md) | Quy trình bóc tách video YouTube và tài liệu kỹ thuật |
| └── [concept-to-language.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/references/concept-to-language.md) | Bảng ánh xạ khái niệm ra ngôn ngữ hiển thị tối ưu nhất |
| `scripts/` | **Bộ Công Cụ Tự Động Hóa**: |
| ├── [tracker.py](file:///c:/Users/Phucx/Desktop/Agent_Teacher/scripts/tracker.py) | Engine CLI quản lý hồ sơ học tập và kiểm tra điều kiện tiên quyết |
| ├── [lab_manager.py](file:///c:/Users/Phucx/Desktop/Agent_Teacher/scripts/lab_manager.py) | Tự động tạo bài tập rỗng (scaffolding) và lưu snapshot phiên học |
| └── [package_skill.py](file:///c:/Users/Phucx/Desktop/Agent_Teacher/scripts/package_skill.py) | Đóng gói artifact phân phối skill |
| `labs/` | **Không Gian Làm Bài Tập**: Thư mục bài tập thực hành độc lập (`lab01_boot`, `lab02_mmio`...) |
| `sessions/` | **Nhật Ký Phiên Học**: Snapshot JSON lưu trữ kết quả đánh giá từng bài |
| [learning_profile.json](file:///c:/Users/Phucx/Desktop/Agent_Teacher/learning_profile.json) | Hồ sơ lưu vết tiến độ tri thức thực tế của học viên |
| [evals/evals.json](file:///c:/Users/Phucx/Desktop/Agent_Teacher/evals/evals.json) | Bộ đề kiểm thử đánh giá kỹ năng |

---

## Hướng Dẫn Sử Dụng CLI Quản Lý Học Tập

### 1. Xem Cây Tri Thức & Tiến Độ Hiện Tại
```bash
python scripts/tracker.py --status
```
Lệnh này sẽ in ra toàn bộ cây tri thức chia theo 6 phân ngành (C & Pointer, Modern C++, Assembly/Arch, Embedded, RTOS, Lock-free) kèm trạng thái `[Hoàn tất]`, `[Đang học]`, `[Cần ôn]`, hoặc `[Chưa học]`.

### 2. Kiểm Tra Điều Kiện Tiên Quyết Trước Khi Học Chủ Đề Mới
```bash
python scripts/tracker.py --check rtos-context-switch
```
Nếu bạn chưa nắm vững `Stack Frame` hoặc `NVIC Interrupt`, hệ thống sẽ cảnh báo ngay lập tức và ngăn bạn nhảy cóc.

### 3. Cập Nhật Kết Quả Đánh Giá
```bash
python scripts/tracker.py --update "embed-nvic-interrupt" --state MASTERED --score 88
```

### 4. Quản Lý Bài Tập Labs
```bash
# Xem danh sách labs
python scripts/lab_manager.py --list

# Tạo bài tập mới và sinh sẵn template file
python scripts/lab_manager.py --create lab02_mmio --name "Lab 02: Peripheral MMIO"
```

---

## Các Câu Lệnh Kích Hoạt Mẫu (Prompt Trò Chuyện)

- **Học từ YouTube:**
  > "Tôi muốn học về Interrupt và NVIC trên ARM Cortex-M từ video này: https://youtube.com/watch?v=... Hãy phân tích và dạy tôi."
- **Giải thích bản chất C++:**
  > "Giải thích cho tôi Move Semantics và Rvalue Reference trong Modern C++. Tại sao std::move không thực sự move dữ liệu gì cả?"
- **Yêu cầu bài tập:**
  > "Giao cho tôi bài tập thiết kế SPSC Queue Lock-free bằng C++20 atomic."
- **Review code:**
  > "Đây là đoạn code ngắt ngoài GPIO trên STM32F4 của tôi: [dán code]. Hãy review chuẩn Senior và đặt câu hỏi sát hạch."

---

## Từ Khóa Tìm Kiếm & Khám Phá (SEO & Bot Discovery)

`c++` · `modern-cpp` · `embedded-systems` · `lap-trinh-nhung` · `bare-metal` · `arm-cortex-m` · `stm32` · `rtos` · `freertos` · `firmware` · `systems-programming` · `interrupt-handling` · `nvic` · `vector-table` · `systick` · `pendsv` · `context-switch` · `memory-mapped-io` · `code-review` · `assembly` · `lock-free`

