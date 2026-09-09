# Quy Chuẩn Sinh Bài Tập 3 Cấp Độ (3-Level Progressive Exercise Generator)

Một kỹ sư Embedded / C++ Senior không học bằng cách trả lời trắc nghiệm lý thuyết. Phải bắt tay vào viết code từ mức logic mô phỏng cho đến chạm trực tiếp vào thanh ghi trần của phần cứng (Bare-metal). 

Mỗi khi kết thúc bài giảng lý thuyết, Agent bắt buộc phải xuất bộ bài tập gồm 3 cấp độ tăng tiến rõ rệt:

---

## Cấu Trúc 3 Cấp Độ Bài Tập

```
LEVEL 1: LOGIC & HOST SIMULATION (C++ Chuẩn trên PC)
  │
  ▼
LEVEL 2: TARGET & REGISTER MAPPING (Thao tác thanh ghi / CMSIS)
  │
  ▼
LEVEL 3: ZERO-HAL / BARE-METAL MASTER (Không thư viện / Tự viết từ đáy)
```

---

### Cấp Độ 1: Level 1 — Logic & Host Simulation (Mô phỏng kiến trúc trên PC)
- **Mục tiêu:** Giúp học viên nắm vững logic hoạt động, thứ tự thực thi và luồng dữ liệu mà không bị phụ thuộc vào kit mạch phần cứng thật. Chạy được trên GCC/Clang máy tính cá nhân.
- **Yêu cầu kỹ thuật:**
  - Viết bằng C++17/20 chuẩn.
  - Sử dụng thread, atomic, callback function pointer hoặc queue để giả lập hành vi phần cứng.
  - Phải có hàm `main()` mô phỏng kịch bản chạy thử (Test Harness) in ra log trực quan.
- *Ví dụ đề bài (Chủ đề Interrupt):*
  > "Viết một chương trình C++ mô phỏng cơ chế Hardware Interrupt:
  > 1. Luồng chính chạy `main()` thực hiện tác vụ in số liên tục.
  > 2. Luồng thứ hai đóng vai trò ngoại vi phần cứng sinh sự kiện ngẫu nhiên.
  > 3. Triển khai cấu trúc Vector Table giả lập bằng mảng con trỏ hàm.
  > 4. Khi phần cứng kích hoạt ngắt, tạm dừng hoặc ngắt quãng luồng chính để gọi ISR tương ứng trong Vector Table, sau đó quay lại luồng chính."

---

### Cấp Độ 2: Level 2 — Target & Register Mapping (Lập trình cấu hình thanh ghi)
- **Mục tiêu:** Áp dụng vào vi điều khiển mục tiêu (STM32 ARM Cortex-M, ESP32, AVR hoặc x86). Học viên phải làm việc trực tiếp với thanh ghi phần cứng (qua CMSIS hoặc địa chỉ bộ nhớ định sẵn).
- **Yêu cầu kỹ thuật:**
  - Không được dùng thư viện HAL cấp cao đóng gói sẵn toàn bộ (như `HAL_GPIO_Init`, `HAL_UART_Transmit`).
  - Phải dùng thao tác Bitwise (`|=`, `&= ~`, `^=`) trên các thanh ghi ngoại vi (Peripheral Registers).
  - Cấu hình đúng thứ tự: Bật xung Clock (RCC) → Cấu hình chân (GPIO Mode, Pull-up/down) → Kích hoạt bộ điều khiển ngắt (NVIC) → Viết hàm ISR đúng tên định sẵn.
- *Ví dụ đề bài (Chủ đề Interrupt trên STM32):*
  > "Cấu hình ngắt ngoài EXTI trên chân GPIO PA0 (nút nhấn) để toggle LED trên PC13 (STM32F103/F4):
  > 1. Bật Clock cho GPIOA, GPIOC và AFIO/SYSCFG.
  > 2. Cấu hình chân PA0 chế độ Input Pull-up.
  > 3. Cấu hình EXTI Line 0 kích hoạt ngắt cạnh xuống (Falling edge).
  > 4. Kích hoạt ngắt `EXTI0_IRQn` trên bộ điều khiển NVIC với độ ưu tiên xác định.
  > 5. Viết hàm `EXTI0_IRQHandler()`, nhớ xóa cờ ngắt Pending Register sau khi xử lý."

---

### Cấp Độ 3: Level 3 — Zero-HAL / Bare-Metal Master (Lập trình không thư viện hãng)
- **Mục tiêu:** Thấu hiểu tận gốc những gì diễn ra trước `main()`. Viết mã nguồn từ con số 0 mà không include bất kỳ file `.h` nào của hãng (No ST HAL, No CMSIS, No Standard Library nếu cần).
- **Yêu cầu kỹ thuật:**
  - Tự định nghĩa bảng Vector Table và Startup Code (`Reset_Handler`, khởi tạo `.data` và `.bss`).
  - Tự tạo cấu trúc Struct ánh xạ thanh ghi MMIO từ địa chỉ Base Address trong datasheet.
  - Viết Linker Script hoặc giải thích chính xác vùng nhớ Flash/RAM được liên kết như thế nào.
  - Tối ưu hóa assembly / memory footprint, đảm bảo zero-overhead.
- *Ví dụ đề bài (Chủ đề Interrupt & Startup):*
  > "Xây dựng dự án Bare-metal C/C++ từ con số 0 cho STM32F401 (không CMSIS, không thư viện):
  > 1. Viết file `startup.c`: Định nghĩa mảng Vector Table chứa địa chỉ đỉnh Stack và các con trỏ hàm ngoại lệ (`Reset_Handler`, `HardFault_Handler`, `SysTick_Handler`).
  > 2. Trong `Reset_Handler`: Tự viết vòng lặp copy đoạn `.data` từ Flash vào SRAM, xóa trắng đoạn `.bss` về 0, rồi gọi `main()`.
  > 3. Tự định nghĩa base address `0x40023800` (RCC) và `0x40020000` (GPIOA) bằng macro hoặc struct ép kiểu con trỏ `volatile`.
  > 4. Cấu hình Timer SysTick ngắt mỗi 1ms để đếm thời gian hệ thống mà không dùng bất kỳ file header nào từ nhà sản xuất."

---

## Hướng Dẫn Giao Bài Tập Cho Học Viên

1. Khi giao bài tập, Agent luôn xuất bản cả 3 cấp độ để học viên có cái nhìn toàn cảnh về độ sâu kiến thức.
2. Khuyến khích học viên bắt đầu từ Level 1 nếu chưa có kit mạch thật, hoặc nhảy thẳng vào Level 2 và Level 3 nếu đã có nền tảng.
3. Nhắc nhở học viên: *"Khi làm xong, hãy dán toàn bộ code (hoặc link repo Git/commit) để Agent tiến hành Senior Code Review và chất vấn năng lực."*
