# Hướng Dẫn Sử Dụng Toàn Tập — AgentTeacher (Universal Edition)

> **Cẩm nang vận hành, danh mục lệnh tắt, quy trình học tập 6 Phase và bộ công cụ CLI dành cho học viên.**

---

## I. Tổng Quan & Triết Lý Vận Hành

**AgentTeacher** là hệ thống Cố vấn Kỹ thuật & Sát hạch Năng lực lập trình chuẩn Senior (hỗ trợ mọi ngôn ngữ: **C/C++, Rust, Go, Python, TypeScript/JavaScript, Systems & Distributed**).

### Triết lý bất biến: **BUILD SMALL. UNDERSTAND DEEP.**
- Không học vẹt tính năng, không lắp ghép library hào nhoáng khi chưa hiểu cơ chế bên dưới.
- Luôn đào sâu đến tận đáy cơ chế thực thi: *CPU Registers, Stack Frame, Compiler Codegen (`-O3`), Memory Layout, Borrow Checker, Goroutine Scheduler (GMP), Event Loop, Bytecode & GIL*.

---

## II. Bảng Lệnh Tắt Trong Chat (Slash Commands & Shortcuts)

Học viên có thể gõ các lệnh tắt bắt đầu bằng dấu `/` hoặc sử dụng các câu lệnh tự nhiên tương đương:

| Lệnh tắt (`/`) | Câu lệnh tự nhiên mẫu | Chức năng chi tiết |
|---|---|---|
| **`/teach <chủ đề hoặc URL>`** | `Dạy tôi Move Semantics C++`<br>`Học từ video: https://youtube...`<br>`Giải thích cơ chế GMP của Go` | **Phase 1 & 2 (Lý thuyết)**: Bóc tách tài liệu/video, kiểm tra điều kiện tiên quyết (Prerequisites), giảng giải lý thuyết 6 tầng bản chất. |
| **`/exercise [chủ đề]`** | `Giao bài tập Rust Lifetimes`<br>`Tạo lab SPSC Lock-free Queue` | **Phase 3 (Giao bài)**: Sinh bài tập 3 cấp độ (Level 1, 2, 3) và **tự động tạo sẵn thư mục + file template code** trong `labs/<lab_id>/`. |
| **`/review [lab_id]`** | `Review code này cho tôi: [dán code]`<br>`Chấm bài lab01_boot` | **Phase 5 (Chấm bài & Sát hạch)**: Senior Code Review 4 trục (0–100 điểm) + đặt bộ câu hỏi phản biện chuyên sâu 3 tầng. |
| **`/status`** | `Xem tiến độ học`<br>`Cây tri thức của tôi` | **Phase 6 (Tiến độ)**: Hiển thị trạng thái cây tri thức, các kỹ năng đã mở khóa và điểm số tích lũy từ file `learning_profile.json`. |
| **`/labs`** | `Xem danh sách labs`<br>`Tôi đang có những bài tập nào` | Liệt kê toàn bộ các bài tập thực hành hiện có trong thư mục `labs/`. |
| **`/reset`** | `Bắt đầu bài học mới`<br>`Dọn sạch context làm bài khác` | Lưu snapshot phiên học vào `sessions/`, đóng bài tập cũ và làm mới ngữ cảnh để bắt đầu bài mới. |

---

## III. Chu Trình 6 Phase Chi Tiết (End-to-End Workflow)

```
┌─────────────────────────────────────────────────────────────┐
│ 1. INGESTION & PREREQUISITES                                │
│    Nhập link YouTube / Docs / Chủ đề → Kiểm tra điều kiện    │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. LÝ THUYẾT 6 TẦNG BẢN CHẤT HỆ THỐNG                       │
│    Intuition → Mental Model / Runtime → Code & Codegen      │
│    → Walkthrough → Bẫy hệ thống / Lỗi kinh điển → Pointers  │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. BÀI TẬP 3 CẤP ĐỘ & TỰ ĐỘNG SCAFFOLD TEMPLATE             │
│    Level 1: Core Mechanics (Cú pháp & Logic nền tảng)       │
│    Level 2: Real-World Constraints (Hiệu năng & Ràng buộc)  │
│    Level 3: Under-the-Hood / Zero-Lib (Tự viết từ số 0)     │
│    ==> Tự động sinh file code trong labs/<lab_id>/          │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. HỌC VIÊN CODE TRỰC TIẾP TRONG LABS                       │
│    Mở file trong labs/<lab_id>/ lên viết mã                 │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. SENIOR CODE REVIEW & SÁT HẠCH BẢO VỆ 3 TẦNG              │
│    Chấm điểm 4 trục (0-100) + 3 câu hỏi phản biện:          │
│    1. Concept Under-the-hood  2. Code Mutation  3. Debug    │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. BÁO CÁO NĂNG LỰC & CẬP NHẬT CÂY TRI THỨC                 │
│    Xuất Learning Report + Lưu snapshot vào sessions/        │
│    + Cập nhật learning_profile.json                         │
└─────────────────────────────────────────────────────────────┘
```

---

## IV. Hướng Dẫn Bộ Công Cụ CLI Dòng Lệnh (Terminal Tools)

Học viên có thể mở terminal (PowerShell hoặc Bash) ngay trong thư mục dự án và chạy các lệnh tiện ích sau:

### 1. Quản lý Cây Tri Thức & Tiến Độ Học Tập (`scripts/tracker.py`)

```bash
# Xem toàn bộ cây tri thức và trạng thái từng môn học
python scripts/tracker.py --status

# Kiểm tra điều kiện tiên quyết trước khi nhảy vào một chủ đề
python scripts/tracker.py --check rtos-context-switch

# Cập nhật kết quả bài làm vào hồ sơ cá nhân
python scripts/tracker.py --update "embed-nvic-interrupt" --state MASTERED --score 90
```

*Các trạng thái bài học:* `LOCKED` (Chưa mở khóa), `AVAILABLE` (Sẵn sàng học), `IN_PROGRESS` (Đang học), `WEAK` (Cần củng cố), `MASTERED` (Đã thành thạo).

### 2. Quản lý Không Gian Bài Tập Labs (`scripts/lab_manager.py`)

```bash
# Xem danh sách các labs đang có trong workspace
python scripts/lab_manager.py --list

# Tự tạo một lab bài tập mới kèm cấu trúc file mẫu
python scripts/lab_manager.py --create lab02_mmio --name "Lab 02: Peripheral MMIO"
```

### 3. Đóng Gói Phân Phối Skill (`scripts/package_skill.py`)

```bash
# Đóng gói và kiểm tra dung lượng artifact phân phối
python scripts/package_skill.py
```
*(File zip phân phối sẽ được lưu tự động tại `dist/agent-teacher.zip`)*

---

## V. Tiêu Chuẩn Đánh Giá & Bộ Câu Hỏi Phản Biện

Trong **Phase 5**, Agent không bao giờ công nhận bài chỉ vì "chạy không báo lỗi". Mã nguồn sẽ được soi xét qua 4 trục:

1. **Understanding (30%):** Học viên có hiểu đúng vấn đề cốt lõi và cơ chế của ngôn ngữ hay không.
2. **Implementation (30%):** Quản lý tài nguyên, chi phí bộ nhớ, độ phức tạp $O$, xử lý lỗi, thread-safety.
3. **Debugging (20%):** Khả năng dự đoán lỗi, corner cases, memory leak, race condition.
4. **Mental Model (20%):** Khả năng giải thích chính xác mô hình thực thi runtime bên dưới.

### Bộ 3 Câu Hỏi Phản Biện Bắt Buộc:
- **Câu 1 (Concept/Under-the-hood):** *"Dữ liệu/biến này được cấp phát ở Stack hay Heap? Ai là người thu hồi nó và vào thời điểm nào?"*
- **Câu 2 (Code Mutation):** *"Nếu tôi xóa bỏ dòng lệnh X hoặc đổi kiểu dữ liệu từ Y sang Z, hành vi của chương trình sẽ thay đổi thế nào?"*
- **Câu 3 (Debug Scenario):** *"Khi hệ thống chạy với tải cao bị rò rỉ bộ nhớ hoặc rơi vào deadlock/HardFault, bạn dùng công cụ gì và lần theo dấu vết ra sao để tìm nguyên nhân?"*

---

## VI. Một Ví Dụ Thực Chiến Từng Bước

1. **Gõ:** `/teach Move Semantics trong Modern C++`
   - Agent phân tích bế tắc kỹ thuật: Cấp phát sâu (Deep Copy) gây tốn kém $O(N)$ bộ nhớ và chu kỳ CPU.
   - Giảng giải 6 tầng: Rvalue reference `&&`, hoán đổi con trỏ $O(1)$, sơ đồ ô nhớ trước và sau khi `std::move`.
2. **Gõ:** `/exercise`
   - Agent sinh 3 cấp độ bài tập và tự động tạo file `labs/lab02_move_semantics/src/buffer.hpp`.
3. **Mở file code:**
   - Bạn mở `labs/lab02_move_semantics/src/buffer.hpp` lên viết class quản lý dynamic buffer với Move Constructor và Move Assignment Operator `noexcept`.
4. **Gõ:** `/review lab02_move_semantics`
   - Agent review mã nguồn, chỉ ra các điểm tối ưu và đặt 3 câu hỏi sát hạch.
5. **Trả lời câu hỏi:**
   - Bạn trả lời các câu hỏi phản biện trực tiếp trong chat.
6. **Nhận kết quả:**
   - Agent cấp bảng điểm, ghi snapshot vào `sessions/lab02_move_semantics_<timestamp>.json` và cập nhật điểm số vào `learning_profile.json`.
7. **Gõ:** `/reset`
   - Sẵn sàng cho bài học tiếp theo!
