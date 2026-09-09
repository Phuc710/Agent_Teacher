<div align="center">
  <h1>AgentTeacher — Senior Software & Systems Edition</h1>
  <p><b>Hệ Thống Cố Vấn, Giảng Dạy & Sát Hạch Năng Lực Lập Trình & Hệ Thống Chuẩn Senior</b></p>
  <p><a href="README.vi.md"><b>Tiếng Việt (Khuyên Dùng)</b></a> · <a href="README.md"><b>English</b></a></p>
  <p>
    <img src="https://img.shields.io/badge/Ngôn%20ngữ-C%2B%2B%20%7C%20Rust%20%7C%20Go%20%7C%20Python%20%7C%20TS-00599C?style=flat-square" alt="Ngôn ngữ">
    <img src="https://img.shields.io/badge/Trọng%20tâm-Bản%20chất%20Hệ%20thống%20%7C%20Runtime-0091BD?style=flat-square" alt="Trọng tâm">
    <img src="https://img.shields.io/badge/Triết%20lý-Build%20Small.%20Understand%20Deep.-E95420?style=flat-square" alt="Triết lý">
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">
    <img src="https://img.shields.io/badge/Skill-AgentTeacher-blueviolet?style=flat-square" alt="Skill">
  </p>
</div>

---

## Triết Lý Giảng Dạy: Bản Chất Hệ Thống & Cơ Chế Thực Thi (Under-The-Hood)

Khác biệt hoàn toàn với các chatbot đọc định nghĩa từ điển hoặc tóm tắt lý thuyết suông:
- **Không học vẹt:** Không bắt đầu bằng *"Interrupt là cơ chế...", "Goroutine là luồng nhẹ...", "Move semantics là..."*.
- **Xuất phát từ bế tắc kỹ thuật cốt lõi:** Bắt đầu từ giới hạn vật lý của CPU, chi phí cấp phát bộ nhớ, race condition hay tối ưu hóa của compiler/runtime: *"CPU bị nghẽn 100% khi polling I/O", "Move semantics biến thao tác cấp phát Heap $O(N)$ thành hoán đổi con trỏ $O(1)$", "Tại sao GMP model trong Go lại scale tốt hơn thread của OS?"*.
- **Soi tận cơ chế thực thi bên dưới:** Kiểm tra mã máy GCC/Clang (`-O3`), cơ chế mượn bộ nhớ (Borrow checker) của Rust, Event Loop trong Node.js/V8, Bytecode & GIL trong Python, cảnh báo bẫy mất lệnh, rò rỉ bộ nhớ và race condition.
- **Code chạy chưa phải là đúng:** Code chạy pass test cục bộ vẫn có thể sập production khi tải cao hoặc rò rỉ tài nguyên. Agent chỉ công nhận khi học viên vượt qua bộ câu hỏi phản biện chuyên sâu.

---

## Chu Trình Học Tập 6 Phase Khép Kín (The 6-Phase Engineering Loop)

```
┌─────────────────────────────────────────────────────────────┐
│ 1. INGESTION & CONCEPT EXTRACTION                           │
│    Học viên gửi: Video YouTube, Transcript, Docs, Topic     │
│    Agent: Bóc tách khái niệm + Kiểm tra Prerequisites        │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. THEORY SYNTHESIS (LÕI 6 TẦNG BẢN CHẤT HỆ THỐNG)          │
│    Intuition → Mental Model / Cơ chế bên dưới → Code        │
│    → Walkthrough → Bẫy hệ thống / Lỗi kinh điển → Pointers  │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. 3-LEVEL PROGRESSIVE EXERCISES                            │
│    Level 1: Core Mechanics (Nắm vững cú pháp & logic)       │
│    Level 2: Real-World & Constraints (Ràng buộc hiệu năng)  │
│    Level 3: Under-the-Hood / Zero-Framework (Tự build đáy)  │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. HỌC VIÊN CODE & NỘP BÀI                                  │
│    Code trực tiếp trong labs/<lab_id>/ hoặc gửi link repo   │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. SENIOR CODE REVIEW & BỘ CÂU HỎI PHẢN BIỆN CHUYÊN SÂU     │
│    Chấm 4 trục (Understanding / Impl / Debug / Mental Model)│
│    Hỏi 3 tầng: Concept → Code Mutation ("Nếu bỏ dòng này..")│
│    → Debug Scenarios ("Ứng dụng gặp deadlock/leak..")       │
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
| [GUIDE.md](file:///c:/Users/Phucx/Desktop/Agent_Teacher/GUIDE.md) | **Cẩm nang hướng dẫn sử dụng toàn tập**: Lệnh tắt, quy trình 6 phase, CLI và ví dụ |
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

---

## Hướng Dẫn Sử Dụng CLI Quản Lý Học Tập

### 1. Xem Cây Tri Thức & Tiến Độ Hiện Tại
```bash
python scripts/tracker.py --status
```
Lệnh này sẽ in ra toàn bộ cây tri thức kèm trạng thái `[Hoàn tất]`, `[Đang học]`, `[Cần ôn]`, hoặc `[Chưa học]`.

### 2. Kiểm Tra Điều Kiện Tiên Quyết Trước Khi Học Chủ Đề Mới
```bash
python scripts/tracker.py --check rtos-context-switch
```
Nếu bạn chưa nắm vững kiến thức nền tảng, hệ thống sẽ cảnh báo ngay lập tức và ngăn bạn nhảy cóc.

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

## Các Câu Lệnh Kích Hoạt Mẫu (Prompt Trò Chuyện Đa Ngôn Ngữ)

- **Học từ YouTube / Docs:**
  > "Tôi muốn học về cơ chế GMP Scheduler trong Go từ video này: https://youtube.com/watch?v=... Hãy phân tích và dạy tôi."
- **Giải thích bản chất dưới đáy (Under-the-hood):**
  > "Giải thích cho tôi Borrow Checker và Lifetimes trong Rust. Tại sao Rust đảm bảo Memory Safety mà không cần Garbage Collector?"
  > "Tại sao GIL trong Python lại ngăn cản true multi-threading cho CPU-bound tasks? Cơ chế hoạt động của bytecode eval loop ra sao?"
- **Yêu cầu bài tập & Code:**
  > "Giao cho tôi bài tập thiết kế SPSC Queue Lock-free hoặc Custom Promise/Async Engine."
- **Review code đa ngôn ngữ:**
  > "Đây là đoạn code Rust/Go/C++/Python của tôi: [dán code]. Hãy review chuẩn Senior và đặt câu hỏi sát hạch."

---

## Từ Khóa Tìm Kiếm & Khám Phá (SEO & Bot Discovery)

`programming` · `software-engineering` · `systems-programming` · `c++` · `rust` · `golang` · `python` · `typescript` · `embedded-systems` · `bare-metal` · `concurrency` · `memory-management` · `compilers` · `code-review` · `architecture` · `under-the-hood` · `learning-mentor`


