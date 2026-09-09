/**
 * @file main.c
 * @brief Chương trình chính cho Lab 01
 */

#include <stdint.h>

// Biến toàn cục có khởi tạo (Thuộc phân vùng .data)
uint32_t g_initialized_var = 0xDEADBEEF;

// Biến toàn cục không khởi tạo (Thuộc phân vùng .bss)
uint32_t g_uninitialized_var;

int main(void) {
    // TODO: Học viên kiểm tra xem khi vào main(), 
    // g_initialized_var đã có giá trị 0xDEADBEEF chưa?
    // g_uninitialized_var đã được xóa về 0 chưa?
    
    g_uninitialized_var = g_initialized_var + 1;

    while (1) {
        // Vòng lặp chính của MCU
    }

    return 0;
}
