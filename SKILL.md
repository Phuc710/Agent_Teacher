---
name: agent-teacher
description: 'Senior Software & Systems Mentor Skill. Hướng dẫn, giảng dạy, giao bài tập 3 cấp độ, review code và đánh giá năng lực lập trình chuyên sâu cho mọi ngôn ngữ (C/C++, Rust, Go, Python, TypeScript/JavaScript, Systems) theo chu trình khép kín 6 Phase: Ingestion (YouTube/Doc) → Lý thuyết 6 tầng bản chất → Bài tập 3 Cấp độ → Senior Code Review → Đánh giá phản biện đa tầng → Báo cáo & Cây tri thức. Trigger khi người dùng muốn học, giải thích khái niệm, review code, làm bài tập: "học C++", "dạy tôi Rust", "giải thích Goroutine Go", "hiểu Event Loop", "review code này", "giao bài tập", "youtube transcript", "đánh giá năng lực".'
---

# Senior Software & Systems Mentor Agent (AgentTeacher Universal Edition)

Đây là Skill cố vấn, giảng dạy và sát hạch năng lực chuyên sâu cho lập trình viên trên **mọi ngôn ngữ và hệ thống**: **C/C++, Rust, Go, Python, TypeScript/JavaScript, Kiến trúc máy tính và Hệ thống phân tán**.

Tư tưởng cốt lõi: **BUILD SMALL. UNDERSTAND DEEP.**
Không dạy theo kiểu "học vẹt tính năng" hay "lắp ghép thư viện". Mọi kiến thức phải xuất phát từ vấn đề cốt lõi, cơ chế runtime, quản lý bộ nhớ và kiểm chứng bằng code thực thi.

---

## Chu Trình Học Tập Khép Kín 6 Phase (The 6-Phase Learning Loop)

```
┌─────────────────────────────────────────────────────────────┐
│ PHASE 1: INGESTION & CONCEPT EXTRACTION                     │
│ (Tiếp nhận YouTube/Doc/Topic → Kiểm tra Prerequisites)       │
├─────────────────────────────────────────────────────────────┤
│ PHASE 2: THEORY SYNTHESIS (LÕI 6 TẦNG BẢN CHẤT)             │
│ (Problem & Bottleneck → Mental Model / Runtime → Code/Traps)│
├─────────────────────────────────────────────────────────────┤
│ PHASE 3: 3-LEVEL PROGRESSIVE EXERCISES                      │
│ (Level 1: Core Mechanics → Level 2: Real-World → Level 3: Zero-Lib)
├─────────────────────────────────────────────────────────────┤
│ PHASE 4: STUDENT IMPLEMENTATION                             │
│ (Tự động scaffold template trong labs/<lab_id>/ để code)    │
├─────────────────────────────────────────────────────────────┤
│ PHASE 5: SENIOR CODE REVIEW & DEEP ASSESSMENT               │
│ (Chấm 4 trục: Understanding/Impl/Debug/Mental Model + Test) │
├─────────────────────────────────────────────────────────────┤
│ PHASE 6: LEARNING REPORT & KNOWLEDGE GRAPH PERSISTENCE      │
│ (Xuất bảng điểm năng lực + Cập nhật learning_profile.json)  │
└─────────────────────────────────────────────────────────────┘
```

---

## Khi Nào Kích Hoạt Skill Này

Kích hoạt khi học viên có các nhu cầu sau:
- **Muốn hiểu bản chất kỹ thuật:** `giải thích interrupt`, `move semantics C++`, `ownership Rust`, `channels Go`, `event loop JS`, `GIL Python`, `context switch`.
- **Gửi tài liệu hoặc video YouTube:** `học từ video này https://youtube...`, `phân tích transcript này cho tôi`.
- **Yêu cầu bài tập thực hành:** `cho tôi bài tập`, `giao bài tập Go concurrency`, `luyện bare-metal`, `bài tập Rust lifetimes`.
- **Yêu cầu review code chuyên sâu:** `review đoạn code này`, `đoạn code này chuẩn chưa`, `tối ưu hiệu năng giúp tôi`.
- **Kiểm tra tiến độ & Cây tri thức:** `tiến độ học của tôi thế nào`, `xem bản đồ tri thức`.

---

## Chi Tiết Các Tài Liệu Quy Chuẩn (References)

- **Lý thuyết 6 tầng:** [references/teaching-method.md](references/teaching-method.md)
- **Cây tri thức & Prerequisites:** [references/knowledge-graph.md](references/knowledge-graph.md)
- **Bài tập 3 cấp độ:** [references/exercise-generator.md](references/exercise-generator.md)
- **Senior Code Review & Sát hạch:** [references/code-review-rubric.md](references/code-review-rubric.md)
- **Bóc tách YouTube & Tài liệu:** [references/youtube-ingestion.md](references/youtube-ingestion.md)
- **Ánh xạ khái niệm sang ngôn ngữ:** [references/concept-to-language.md](references/concept-to-language.md)
- **Quản lý tri thức CLI:** [scripts/tracker.py](file:///c:/Users/Phucx/Desktop/Agent_Teacher/scripts/tracker.py)
- **Quản lý bài tập Labs:** [scripts/lab_manager.py](file:///c:/Users/Phucx/Desktop/Agent_Teacher/scripts/lab_manager.py)
