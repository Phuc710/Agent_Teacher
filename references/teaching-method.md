# Sổ Tay Phương Pháp Giảng Dạy C++ & Hệ Thống (Senior C++ & Systems Playbook)

> **TRIẾT LÝ BẤT DI BẤT DỊCH: BUILD SMALL. UNDERSTAND DEEP.**
> Đừng học Embedded theo kiểu "làm được tính năng" (ESP32 đọc sensor -> gửi MQTT -> dashboard IoT 20 màn hình chỉ toàn gọi library).
> Phải học theo kiểu **"giải thích được tại sao nó chạy tận mức thanh ghi và chu kỳ CPU"**:
>
> ```
> Power ON / Reset
>       ↓
> CPU nạp Initial MSP & Reset_Handler từ Vector Table (Offset 0x0 & 0x4)
>       ↓
> Reset_Handler (Assembly / Startup code)
>       ↓
> SystemInit() (Clock Tree, Flash Latency, FPU)
>       ↓
> C Runtime Init: Copy đoạn .data từ Flash vào RAM, Zero-fill đoạn .bss
>       ↓
> __libc_init_array (Gọi Constructors của static C++ objects)
>       ↓
> main()
>       ↓
> Init Peripherals (MMIO, Bus Clock Gating)
>       ↓
> Enable Interrupt (NVIC Configuration & Priority)
>       ↓
> Peripheral Event → Hardware Auto-Stacking (xPSR, PC, LR, R12, R3-R0)
>       ↓
> ISR Execution → Write-1-to-Clear Pending Bit
>       ↓
> RTOS Scheduler (SysTick Exception triggers PendSV)
>       ↓
> Context Switch (Software Stacking R4-R11, Hoán đổi PSP, EXC_RETURN)
>       ↓
> Task tiếp theo được thực thi
> ```

---

## 1. Hợp Đồng 6 Tầng (The 6-Layer Teaching Spine for C++ & Systems)

Mọi bài giảng lý thuyết đều phải tuân thủ nghiêm ngặt 6 tầng dưới đây:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. INTUITION (Vấn đề phần cứng/CPU giải quyết)              │
├─────────────────────────────────────────────────────────────┤
│ 2. MENTAL MODEL & MEMORY LAYOUT (Sơ đồ bộ nhớ / Thanh ghi)   │
├─────────────────────────────────────────────────────────────┤
│ 3. CODE EXAMPLE & ASSEMBLY MAPPING (Code chuẩn + Mã máy)    │
├─────────────────────────────────────────────────────────────┤
│ 4. WALKTHROUGH (Bóc tách luồng dữ liệu & Vòng đời bộ nhớ)   │
├─────────────────────────────────────────────────────────────┤
│ 5. TRAPS & UNDEFINED BEHAVIOR (Cạm bẫy & Lỗi biên dịch/CPU) │
├─────────────────────────────────────────────────────────────┤
│ 6. POINTERS (Bản đồ tri thức mở rộng - Không lan man)       │
└─────────────────────────────────────────────────────────────┘
```

---

### Tầng 1: Intuition (Trực Giác & Vấn Đề Cốt Lõi)
- **Quy tắc vàng:** Dẫn dắt bằng **bế tắc kỹ thuật** mà CPU, bus dữ liệu hoặc kiến trúc bộ nhớ đang gặp phải nếu không có kỹ thuật này.
- **TUYỆT ĐỐI KHÔNG:** "Interrupt là một cơ chế cho phép...", "RAII là một idiom trong C++..."
- **CHUẨN SENIOR:**
  - *Ví dụ về Interrupt:* "CPU đang miệt mài chạy vòng lặp tính toán `main()`. Nhưng UART bên ngoài có thể nhận 1 byte bất kỳ lúc nào. Nếu dùng polling `while(!UART_READY)`, CPU bị trói chặt 100% xung nhịp chỉ để ngóng chờ. Interrupt sinh ra để phần cứng tự ngắt ngang dòng chảy lệnh của CPU đúng 1 chu kỳ khi có sự kiện thực sự, giải phóng CPU làm việc khác."
  - *Ví dụ về Move Semantics:* "Một mảng động nắm 1 triệu phần tử trên Heap. Nếu muốn trả nó về từ một hàm theo kiểu C++98, CPU buộc phải cấp phát một vùng Heap mới, copy 1 triệu phần tử qua bus bộ nhớ, rồi giải phóng vùng cũ. Move semantics sinh ra để hoán đổi vỏn vẹn một con trỏ 8 byte trên Stack, biến thao tác $O(N)$ tốn kém thành $O(1)$ zero-cost."

---

### Tầng 2: Mental Model & Memory Layout (Sơ Đồ Bộ Nhớ / Thanh Ghi)
- Bắt buộc phải có sơ đồ trực quan (ASCII Art hoặc Mermaid) mô tả sự biến chuyển của bộ nhớ:
  - Vị trí trên Stack / Heap / Flash / RAM.
  - Con trỏ, địa chỉ và giá trị trong ô nhớ.
  - Thanh ghi phần cứng liên quan (PC, SP, LR, R0-R12, hoặc thanh ghi cấu hình NVIC/GPIO).

*Ví dụ Mental Model cho Interrupt Exception Entry (ARM Cortex-M):*
```
[Hardware Event: Chân GPIO đổi mức]
              │
              ▼
   [NVIC kiểm tra Priority & Mask]
              │
              ▼
   [CPU Hardware Auto-Push Context vào Stack]:
   ┌───────────────────────────┐
   │ xPSR                      │
   │ PC (Return Address)       │
   │ LR                        │
   │ R12                       │
   │ R3, R2, R1, R0            │
   └───────────────────────────┘ ◄── SP giảm 32 byte tự động
              │
              ▼
   [Đọc Vector Table tại offset ngắt] ──► Lấy địa chỉ hàm ISR
              │
              ▼
   [Nhảy vào thực thi ISR]
```

---

### Tầng 3: Code Example & Assembly Mapping (Mã Nguồn Thực Thi & Ánh Xạ Mã Máy)
- Dùng **Modern C++ (C++17/C++20)** hoặc **C Bare-metal** chuẩn chỉ:
  - Tên biến có ngữ nghĩa kỹ thuật (`nvic_iser`, `uart_rx_buffer`, `head_index`).
  - Không viết code pseudocode chung chung kiểu "gọi hàm xử lý". Phải viết đúng thanh ghi, đúng kiểu dữ liệu (`uint32_t`, `volatile`, `reinterpret_cast`).
- **Ánh xạ Assembly / Compiler Codegen:** Với các khái niệm nhạy cảm về hiệu năng (Move semantics, Volatile, Virtual function, Inlined function), phải trích đoạn ngắn hợp ngữ GCC/Clang để chứng minh zero-cost abstraction hoặc hành vi sinh mã của compiler.

*Ví dụ ánh xạ `volatile`:*
```cpp
// C Code:
volatile uint32_t* status_reg = (uint32_t*)0x40001000;
while (*status_reg == 0) {}

// Assembly sinh ra (vòng lặp đọc lại bộ nhớ liên tục):
.L2:
    ldr     r3, [r2]       // Đọc giá trị từ địa chỉ 0x40001000 vào thanh ghi r3
    cmp     r3, #0         // So sánh với 0
    beq     .L2            // Nếu bằng 0 nhảy lại L2

// NẾU BỎ volatile (Compiler tối ưu hóa tai hại):
    ldr     r3, [r2]       // Đọc 1 lần duy nhất trước vòng lặp
.L2:
    cmp     r3, #0
    beq     .L2            // Nhảy lặp vô tận trên thanh ghi r3, CPU treo cứng!
```

---

### Tầng 4: Walkthrough (Bóc Tách Luồng Dữ Liệu & Vòng Đời)
- Gom code thành 2–3 khối mục đích (*Purpose Units*):
  1. *Khối thiết lập / Khởi tạo tài nguyên (Initialization & Register config)*.
  2. *Khối kích hoạt / Chuyển giao dữ liệu (Trigger & Dataflow)*.
  3. *Khối dọn dẹp / Khôi phục ngữ cảnh (Cleanup & Context restore)*.
- Trả lời cho học viên: *Tại sao dòng này phải nằm trước dòng kia? Nếu đảo thứ tự thanh ghi có bị lỗi bus hoặc race condition không?*

---

### Tầng 5: Traps & Undefined Behavior (Cạm Bẫy Hệ Thống & Phản Trực Giác)
- Đây là tầng phân hóa giữa thợ code và Kỹ sư Senior. Phải chỉ ra ít nhất một trong các bẫy:
  - **Memory/Hardware race:** Biến dùng chung giữa ISR và `main()` không khai báo `volatile` hoặc thao tác không nguyên tử (non-atomic read-modify-write).
  - **Dangling pointer / Use-After-Free:** Trả về tham chiếu của biến local trên Stack.
  - **Stack Overflow trong ISR:** Cấp phát mảng cục bộ quá lớn hoặc gọi hàm lồng nhau trong ngắt khiến ngắt làm tràn Stack Pointer.
  - **Interrupt Latency & Blocking:** Viết vòng lặp delay hoặc gọi printf/I2C chờ lâu trong ISR khiến hệ thống tê liệt các ngắt ưu tiên thấp hơn.
  - **Compiler Undefined Behavior:** Tràn số nguyên có dấu (signed overflow), vi phạm Strict Aliasing Rule qua `reinterpret_cast`.

---

### Tầng 6: Pointers & Next Steps (Bản Đồ Mở Rộng)
- Đưa ra 2–3 gạch đầu dòng trỏ tới các chủ đề chuyên sâu tiếp theo. **Tuyệt đối không giải thích dài dòng.**
  - *Ví dụ:*
    - "Muốn truyền dữ liệu an toàn từ ISR sang Main Loop mà không cần tắt ngắt? Tìm hiểu **Lock-free Single-Producer Single-Consumer (SPSC) Ring Buffer**."
    - "Cần quản lý hàng chục task chạy song song với độ ưu tiên ngắt phức tạp? Khái niệm tiếp theo là **PendSV & RTOS Context Switching**."

---

## 2. Tiêu Chuẩn Bộ Câu Hỏi Đánh Giá (Test Questions)

Sau bài giảng, đưa ra 2–3 câu hỏi với độ khó tăng dần theo thang:
1. **Câu 1 (Bản chất phần cứng / Recall & Contrast):** Kiểm tra mental model ("Ai gọi ISR?", "CPU biết địa chỉ của hàm ngắt từ đâu?").
2. **Câu 2 (Đột biến mã / Read & Mutate Code):** Thay đổi một chi tiết nhỏ trong code và hỏi hậu quả ("Nếu bỏ từ khóa `volatile` ở đây, hành vi trên chip thực tế với cờ tối ưu `-O3` sẽ ra sao?").
3. **Câu 3 (Thiết kế / Kịch bản gỡ lỗi sâu / Debugging Scenario):** Đưa ra triệu chứng lỗi thực tế ("LED không sáng dù đã bật ngắt; hãy lần vết từ Clock Peripheral → GPIO Mode → NVIC Enable → Vector Table").
