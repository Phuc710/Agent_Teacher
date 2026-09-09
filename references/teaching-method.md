# Sổ Tay Phương Pháp Giảng Dạy Senior Software & Systems (Universal Playbook)

> **TRIẾT LÝ BẤT DI BẤT DỊCH: BUILD SMALL. UNDERSTAND DEEP.**
> Đừng học lập trình theo kiểu "học vẹt tính năng" hay "lắp ghép thư viện" (chỉ biết gọi library làm app/dashboard hào nhoáng nhưng không hiểu cơ chế bên dưới).
> Dù là C++, Rust, Go, Python hay TypeScript, phải giải thích được **bản chất cơ chế thực thi, quản lý bộ nhớ và runtime bên dưới**:
> - **C/C++ & Nhúng:** CPU execution, registers, stack frame, compiler codegen `-O3`, MMIO, interrupts, context switch.
> - **Rust:** Ownership, borrow checker, lifetimes, zero-cost abstractions, memory layout, unsafe.
> - **Go:** Goroutines, CSP channels, runtime scheduler (GMP model), escape analysis, interface dispatch.
> - **Python:** CPython VM, bytecode, GIL, reference counting, event loop, memory management.
> - **TypeScript/JavaScript:** V8 engine, event loop (microtasks/macrotasks), call stack, prototype.
> - **Systems & Distributed:** Protocol state machines, consensus, network sockets, serialization.

---

## 1. Hợp Đồng 6 Tầng Chuẩn Bản Chất (The 6-Layer Universal Spine)

Mọi bài giảng lý thuyết đều phải tuân thủ nghiêm ngặt 6 tầng dưới đây:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. INTUITION (Bế tắc kỹ thuật cốt lõi mà cơ chế giải quyết) │
├─────────────────────────────────────────────────────────────┤
│ 2. MENTAL MODEL & ARCHITECTURE (Sơ đồ bộ nhớ / Runtime / Luồng)│
├─────────────────────────────────────────────────────────────┤
│ 3. CODE EXAMPLE & RUNTIME MECHANICS (Code chuẩn + Cơ chế dưới)│
├─────────────────────────────────────────────────────────────┤
│ 4. WALKTHROUGH (Bóc tách purpose units & vòng đời tài nguyên)│
├─────────────────────────────────────────────────────────────┤
│ 5. TRAPS & PITFALLS (Cạm bẫy chí mạng & Lỗi ngầm)            │
├─────────────────────────────────────────────────────────────┤
│ 6. POINTERS (Bản đồ tri thức mở rộng - Không lan man)       │
└─────────────────────────────────────────────────────────────┘
```

---

### Tầng 1: Intuition (Trực Giác & Vấn Đề Cốt Lõi)
- **Quy tắc vàng:** Dẫn dắt bằng **bế tắc kỹ thuật** (nút thắt CPU, tắc nghẽn bộ nhớ, xung đột luồng hoặc chi phí cấp phát) nếu không có kỹ thuật này.
- **TUYỆT ĐỐI KHÔNG:** Đọc định nghĩa từ điển ("X là một khái niệm...", "Y là một interface...").
- **VÍ DỤ ĐA NGÔN NGỮ CHUẨN SENIOR:**
  - *Rust (Ownership):* "C/C++ đòi hỏi lập trình viên tự quản lý `malloc/free` nên rất dễ dính Use-After-Free. Các ngôn ngữ có Garbage Collector (Java/Go/Python) giải quyết được nhưng phải trả giá bằng việc dừng chương trình (Stop-The-World) và tốn gấp đôi RAM. Rust sinh ra hệ thống Ownership để compiler tự chèn lệnh giải phóng bộ nhớ ngay lúc biên dịch mà không cần GC và không lo dangling pointer."
  - *Go (Goroutines & Channels):* "Mỗi Thread của hệ điều hành (OS Thread) tốn từ 1MB đến 8MB bộ nhớ stack và việc chuyển ngữ cảnh (Context Switch) tốn hàng ngàn chu kỳ CPU. Một server không thể tạo 1 triệu OS Thread. Go sinh ra Goroutine với stack khởi điểm chỉ 2KB và bộ lập lịch GMP chạy ở user-space để xử lý hàng triệu kết nối đồng thời với chi phí cực thấp."
  - *Python (GIL - Global Interpreter Lock):* "Bộ quản lý bộ nhớ của CPython dùng cơ chế đếm tham chiếu (Reference Counting) không an toàn đa luồng. Để tránh race condition khi nhiều thread cùng tăng/giảm biến đếm, CPython khóa toàn bộ trình thông dịch bằng một chiếc khóa duy nhất là GIL. Hệ quả: chạy đa luồng tính toán CPU trên Python không những không nhanh hơn mà còn chậm đi."
  - *JavaScript (Event Loop & Microtasks):* "JS chỉ có đúng 1 luồng thực thi duy nhất (Single-threaded Call Stack). Nếu một hàm đọc file hay gọi mạng mất 2 giây mà chạy đồng bộ, cả trình duyệt sẽ đơ cứng. Event Loop sinh ra để đẩy các tác vụ nặng cho Web APIs chạy ngầm, rồi nhặt callback từ Task Queue / Microtask Queue đưa lại vào Call Stack khi Call Stack rỗng."

---

### Tầng 2: Mental Model & Architecture (Sơ Đồ Bộ Nhớ & Runtime)
Bắt buộc có sơ đồ trực quan (ASCII Art hoặc Mermaid) mô tả cơ chế hoạt động:
- Bộ nhớ: Stack, Heap, Pointer, Reference, Control Block.
- Runtime Engine: Call Stack, Task Queues, Runqueues, Thread pools, Registers.

*Ví dụ Mental Model cho Event Loop (JS/TS):*
```
[Call Stack] ───────────────► [Web APIs / OS Threads] (Chạy ngầm Network, Timers)
     ▲                                   │
     │ Khi Stack rỗng                    ▼
[Event Loop] ◄─── [Microtask Queue (Promise.then)] ◄─── [Macrotask Queue (setTimeout)]
                  (Ưu tiên làm sạch trước!)
```

---

### Tầng 3: Code Example & Runtime Mechanics (Code Thực Thi & Cơ Chế)
- Viết code ngắn gọn (10–30 dòng), sạch sẽ, đúng chuẩn idiomatic của ngôn ngữ đó (Modern C++, Safe Rust, Idiomatic Go, Pythonic, TypeScript strict).
- Giải thích cơ chế runtime hoặc cách compiler xử lý bên dưới.

---

### Tầng 4: Walkthrough (Bóc Tách Mục Đích)
- Gom code thành 2–3 khối mục đích (*Purpose Units*):
  1. *Khởi tạo & Cấu hình tài nguyên*.
  2. *Xử lý dữ liệu / Đồng bộ luồng*.
  3. *Thu hồi / Khôi phục trạng thái*.
- Trả lời: *Tại sao phải làm bước này trước bước kia? Thứ tự thực thi có sinh ra race condition hay leak không?*

---

### Tầng 5: Traps & Pitfalls (Cạm Bẫy Chí Mạng)
- Phân biệt giữa coder tay mơ và Senior:
  - *Rust:* Bẫy Deadlock do giữ `RefCell` mượn mutable 2 lần; Reference cycle gây rò rỉ bộ nhớ trong `Rc/Arc`.
  - *Go:* Goroutine leak do gửi vào unbuffered channel mà không ai đọc; Data race khi truy cập map mà không có RWMutex.
  - *C/C++:* Thiếu `volatile` bị compiler tối ưu hóa nuốt mất lệnh; Dangling pointer; Data race.
  - *Python:* Mutable default argument trong hàm (`def func(a=[])`); Vòng tròn tham chiếu khiến GC không thu hồi ngay.
  - *JS/TS:* Starvation khi microtask queue sinh thêm microtask liên tục chặn đứng macrotask; Unhandled promise rejection.

---

### Tầng 6: Pointers (Bản Đồ Mở Rộng)
- 2–3 gạch đầu dòng trỏ tới khái niệm nâng cao tiếp theo. Tuyệt đối không giảng bài thứ hai.

---

## 2. Tiêu Chuẩn Bộ Câu Hỏi Phản Biện (Assessment Questions)

Mỗi bài giảng kết thúc bằng 3 câu hỏi tăng tiến:
1. **Câu 1 (Bản chất Runtime / Under-the-hood):** "Bộ phận nào trong runtime quản lý việc này?", "Bộ nhớ được cấp phát ở đâu?"
2. **Câu 2 (Đột biến mã / Mutation):** "Nếu đổi kiểu dữ liệu hoặc xóa dòng này thì hành vi chương trình sẽ thay đổi thế nào?"
3. **Câu 3 (Kịch bản gỡ lỗi thực tế / Debugging):** Đưa ra triệu chứng lỗi ngoài sản xuất và yêu cầu học viên tìm nguyên nhân gốc rễ.
