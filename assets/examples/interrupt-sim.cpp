/**
 * @file interrupt-sim.cpp
 * @brief Level 1 Host Simulation: Hardware Interrupt & NVIC Vector Table in C++20
 * Demonstrates CPU execution flow interrupted by an asynchronous hardware event.
 */

#include <iostream>
#include <vector>
#include <functional>
#include <thread>
#include <chrono>
#include <atomic>

using ISR_Func = void (*)();

// Giả lập Vector Table của ARM Cortex-M
constexpr size_t VECTOR_TABLE_SIZE = 16;
ISR_Func g_vector_table[VECTOR_TABLE_SIZE] = { nullptr };

// Cờ ngắt chia sẻ giữa luồng phần cứng và luồng CPU
std::atomic<bool> g_exti0_pending{ false };
std::atomic<bool> g_system_running{ true };

// Biến trạng thái chia sẻ (Ví dụ: đếm xung nút nhấn)
// Cần volatile hoặc atomic để chống compiler optimize caching vào register
volatile uint32_t g_button_press_count = 0;

// ISR: Interrupt Service Routine cho EXTI0
void EXTI0_IRQHandler() {
    std::cout << "\n[CPU EXCEPTION ENTRY] Đang ngắt main loop để vào EXTI0_IRQHandler!\n";
    std::cout << " -> Đọc thanh ghi ngoại vi EXTI->PR\n";
    
    g_button_press_count++;
    std::cout << " -> Đã tăng g_button_press_count = " << g_button_press_count << "\n";

    // Xóa cờ ngắt Pending (giả lập ghi 1 để xóa trên STM32)
    std::cout << " -> Xóa cờ pending: EXTI->PR = (1 << 0);\n";
    g_exti0_pending.store(false, std::memory_order_release);
    
    std::cout << "[CPU EXCEPTION RETURN] Phục hồi thanh ghi context, quay lại main loop.\n\n";
}

// Giả lập ngoại vi phần cứng (ví dụ: Nút nhấn vật lý)
void Hardware_Peripheral_Thread() {
    std::this_thread::sleep_for(std::chrono::milliseconds(250));
    std::cout << "[HARDWARE EVENT] Chân GPIO PA0 đổi trạng thái (Falling Edge)!\n";
    g_exti0_pending.store(true, std::memory_order_release);

    std::this_thread::sleep_for(std::chrono::milliseconds(500));
    std::cout << "[HARDWARE EVENT] Chân GPIO PA0 đổi trạng thái lần 2!\n";
    g_exti0_pending.store(true, std::memory_order_release);

    std::this_thread::sleep_for(std::chrono::milliseconds(500));
    g_system_running.store(false, std::memory_order_release);
}

int main() {
    std::cout << "=== MÔ PHỎNG KIẾN TRÚC INTERRUPT & VECTOR TABLE (C++20) ===\n";

    // 1. Cấu hình Vector Table: Gán địa chỉ ISR vào slot 6
    g_vector_table[6] = EXTI0_IRQHandler;
    std::cout << "1. Đã đăng ký EXTI0_IRQHandler tại Vector Table offset 6.\n";

    // 2. Khởi chạy luồng phần cứng
    std::thread hardware_thread(Hardware_Peripheral_Thread);

    // 3. CPU Main Loop (Tác vụ nền liên tục)
    int cycle = 0;
    while (g_system_running.load(std::memory_order_relaxed)) {
        // Kiểm tra ngắt phần cứng (Hardware Interrupt Controller logic)
        if (g_exti0_pending.load(std::memory_order_acquire)) {
            // CPU tự động tra cứu Vector Table và nhảy vào ISR
            ISR_Func isr = g_vector_table[6];
            if (isr != nullptr) {
                isr();
            }
        }

        std::cout << "." << std::flush;
        std::this_thread::sleep_for(std::chrono::milliseconds(50));
        cycle++;
    }

    hardware_thread.join();
    std::cout << "\n=== KẾT THÚC MÔ PHỎNG. Tổng số lần ngắt xử lý: " 
              << g_button_press_count << " ===\n";
    return 0;
}
