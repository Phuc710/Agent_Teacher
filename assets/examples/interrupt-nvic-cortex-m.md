# Bài Giảng Chuẩn Mẫu: Cơ Chế Ngắt (Interrupt) & NVIC Trên ARM Cortex-M

Đây là ví dụ bài giảng thực tế được sinh ra bởi **AgentTeacher C++ Edition** tuân thủ trọn vẹn hợp đồng 6 tầng bản chất phần cứng và 3 cấp độ bài tập thực hành.

---

## 1. Intuition (Vấn Đề Phần Cứng Giải Quyết)

CPU đang bận rộn chạy vòng lặp tính toán chính trong `main()`. Nhưng các thiết bị ngoại vi bên ngoài (như nút bấm người dùng, UART nhận ký tự từ máy tính, hay cảm biến quá nhiệt) xuất hiện sự kiện bất định bất cứ lúc nào. 

Nếu dùng phương pháp thăm dò liên tục (**Polling**):
```c
while (1) {
    if (UART->SR & UART_SR_RXNE) { handle_uart(); }
    do_heavy_calculation();
}
```
CPU bị lãng phí 100% công suất vào vòng lặp chờ vô nghĩa, hoặc nếu phép toán `do_heavy_calculation()` chạy mất 50ms, byte dữ liệu UART gửi tới sẽ bị tràn bộ đệm (Overrun Error) và biến mất vĩnh viễn trước khi CPU kịp quay lại kiểm tra.

**Interrupt** sinh ra để giải phóng CPU: CPU cứ việc tính toán hoặc ngủ tiết kiệm năng lượng (`WFI` - Wait For Interrupt). Khi chân pin vật lý đổi điện áp, bộ điều khiển ngắt phần cứng (NVIC) sẽ lập tức ra lệnh ép CPU tạm dừng đúng 1 chu kỳ lệnh, tự động cất ngữ cảnh hiện tại và nhảy tới xử lý sự kiện trong vòng vài nano-giây.

---

## 2. Mental Model & Memory Layout (Sơ Đồ Ngữ Cảnh & Vector Table)

Khi có ngắt xảy ra, phần cứng CPU Cortex-M tự động thực hiện **Hardware Context Save** đẩy 8 thanh ghi vào vùng nhớ Stack của Task bị ngắt mà không cần 1 dòng code phần mềm nào:

```
Địa chỉ cao
  │  [Stack Frame của hàm main()]
  │  ┌─────────────────────────┐
  │  │ xPSR (Trạng thái cờ CPU)│
  │  │ PC   (Địa chỉ quay về)  │
  │  │ LR   (Link Register)    │
  │  │ R12                    │
  │  │ R3, R2, R1, R0 (Args)   │
  ▼  └─────────────────────────┘ ◄── Con trỏ SP mới (giảm 32 bytes)
Địa chỉ thấp
```

Ngay sau đó, CPU đọc địa chỉ hàm ISR từ bảng **Vector Table** được ánh xạ tại đầu vùng nhớ Flash (hoặc thanh ghi VTOR):

```
Địa chỉ bộ nhớ Flash       Giá trị ô nhớ
0x08000000                 0x20020000   (Initial MSP - Đỉnh Stack ban đầu)
0x08000004                 0x08000109   (Reset_Handler)
0x08000008                 0x08000185   (NMI_Handler)
0x0800000C                 0x08000191   (HardFault_Handler)
...
0x08000058                 0x08000421   (EXTI0_IRQHandler) ◄── CPU nhảy vào đây!
```

---

## 3. Code Example & Assembly Mapping

### Cấu hình ngắt ngoài nút nhấn trên STM32 (Không dùng HAL):
```c
#include <stdint.h>

// Địa chỉ Base của ngoại vi trên STM32F4
#define RCC_AHB1ENR   (*(volatile uint32_t*)(0x40023830))
#define RCC_APB2ENR   (*(volatile uint32_t*)(0x40023844))
#define GPIOA_MODER   (*(volatile uint32_t*)(0x40020000))
#define SYSCFG_EXTICR1 (*(volatile uint32_t*)(0x40013808))
#define EXTI_IMR      (*(volatile uint32_t*)(0x40013C00))
#define EXTI_FTSR     (*(volatile uint32_t*)(0x40013C0C))
#define EXTI_PR       (*(volatile uint32_t*)(0x40013C14))
#define NVIC_ISER0    (*(volatile uint32_t*)(0xE000E100))

// Biến cờ chia sẻ giữa ISR và Main Loop
volatile uint32_t g_event_flag = 0;

void EXTI0_IRQHandler(void) {
    // 1. Kiểm tra cờ pending của line 0
    if (EXTI_PR & (1 << 0)) {
        g_event_flag = 1;
        
        // 2. BẮT BUỘC: Xóa cờ Pending bằng cách ghi 1 (Write-1-to-Clear)
        EXTI_PR = (1 << 0);
    }
}
```

### Ánh xạ Assembly cho biến `volatile`:
```asm
// Khi trong main() kiểm tra: while (!g_event_flag) {}
// Compiler GCC -O3 sinh ra:
.L_wait:
    ldr     r3, [r2]       // Đọc địa chỉ biến g_event_flag từ RAM
    cmp     r3, #0         // So sánh với 0
    beq     .L_wait        // Nếu bằng 0 lặp lại việc ĐỌC TỪ RAM

// NẾU BỎ TỪ KHÓA volatile (Lỗi tối ưu tai hại):
    ldr     r3, [r2]       // Đọc 1 lần duy nhất vào thanh ghi r3
.L_infinite_loop:
    cmp     r3, #0
    beq     .L_infinite_loop // Lặp trên thanh ghi r3, CPU bị treo vĩnh viễn!
```

---

## 4. Walkthrough (Bóc Tách Luồng Dữ Liệu)

1. **Khởi tạo và Đăng ký:**
   - Bật clock cho bus ngoại vi (RCC).
   - Chọn đường dẫn tín hiệu từ chân PA0 tới ngắt ngoài EXTI0 qua thanh ghi `SYSCFG_EXTICR1`.
   - Bật mặt nạ ngắt trong `EXTI_IMR` và chọn kích hoạt cạnh xuống (falling edge) trong `EXTI_FTSR`.
   - Bật cổng ngắt số 6 (EXTI0) trên bộ điều khiển NVIC qua thanh ghi `NVIC_ISER0`.
2. **Kích hoạt phần cứng:**
   - Nút bấm được nhấn: điện áp PA0 rơi từ 3.3V xuống 0V.
   - Phần cứng EXTI dựng bit 0 trong thanh ghi `EXTI_PR` lên 1.
   - NVIC so sánh mức ưu tiên; nếu được phép, phát tín hiệu ngắt tới lõi Cortex-M.
3. **Thực thi ISR & Xóa cờ:**
   - CPU tự động push context vào Stack, nhảy vào `EXTI0_IRQHandler`.
   - Phải ghi bit 1 vào `EXTI_PR` để reset cờ phần cứng. Nếu quên, khi vừa thoát ISR, NVIC lại thấy cờ còn bật và lập tức gọi lại ISR lần nữa (Interrupt Storm).

---

## 5. Traps & Undefined Behavior (Bẫy Chí Mạng)

1. **Bẫy quên xóa cờ Pending:** Cơ chế của STM32 là **rc_w1** (*read-clear, write 1 to clear*). Phải ghi `(1 << 0)` chứ không phải `&= ~(1 << 0)`.
2. **Bẫy delay/printf trong ISR:** Làm việc quá lâu trong ngắt sẽ chặn toàn bộ các ngắt có mức ưu tiên thấp hơn, làm trễ nhịp điều khiển thời gian thực và dễ gây Watchdog Timer reset hệ thống.
3. **Bẫy thiếu `volatile`:** Mọi biến được đọc trong `main()` và sửa đổi trong ISR đều bắt buộc phải là `volatile` hoặc `std::atomic`.

---

## 6. Pointers (Định Hướng Mở Rộng)

- Muốn truyền dữ liệu byte stream từ ISR sang `main()` mà không cần khóa ngắt? Nghiên cứu **Lock-free Ring Buffer / SPSC Queue**.
- Muốn quản lý nhiều tác vụ với độ ưu tiên ngắt khác nhau? Tìm hiểu cơ chế **NVIC Preemption Priority vs Sub-priority** và **PendSV Handler**.

---

## 7. Bài Tập 3 Cấp Độ Thực Hành

- **Level 1 (Host Simulation):** Chạy và giải thích file mô phỏng [interrupt-sim.cpp](file:///c:/Users/Phucx/Desktop/Agent_Teacher/assets/examples/interrupt-sim.cpp) trên máy tính.
- **Level 2 (Target Registers):** Cấu hình Timer ngắt mỗi 1ms để đếm thời gian hệ thống trên STM32 (sử dụng SysTick hoặc TIM2) qua thanh ghi.
- **Level 3 (Zero-HAL Bare-metal):** Viết từ startup code, tự khai báo vector table chứa hàm ISR ngắt ngoài nút nhấn, nạp trực tiếp vào chip không qua CMSIS.
