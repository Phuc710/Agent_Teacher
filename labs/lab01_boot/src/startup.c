/**
 * @file startup.c
 * @brief Minimal Startup Code & Vector Table
 */

#include <stdint.h>

#define SRAM_START  0x20000000U
#define SRAM_SIZE   (128 * 1024U) // 128KB
#define SRAM_END    ((SRAM_START) + (SRAM_SIZE))

// Khai báo các symbol từ Linker Script
extern uint32_t _sidata; // Bắt đầu .data trong Flash
extern uint32_t _sdata;  // Bắt đầu .data trong RAM
extern uint32_t _edata;  // Kết thúc .data trong RAM
extern uint32_t _sbss;   // Bắt đầu .bss trong RAM
extern uint32_t _ebss;   // Kết thúc .bss trong RAM

// Prototype
int main(void);
void Reset_Handler(void);
void Default_Handler(void);

// 1. Vector Table
__attribute__((section(".isr_vector")))
const uint32_t g_vector_table[] = {
    SRAM_END,                 // 0x00: Initial MSP
    (uint32_t)Reset_Handler,  // 0x04: Reset Handler
    (uint32_t)Default_Handler, // 0x08: NMI
    (uint32_t)Default_Handler, // 0x0C: HardFault
    // TODO: Bổ sung thêm nếu cần
};

void Default_Handler(void) {
    while (1) {}
}

void Reset_Handler(void) {
    // TODO: Bước 1: Copy đoạn .data từ Flash vào SRAM
    uint32_t *src = &_sidata;
    uint32_t *dst = &_sdata;
    while (dst < &_edata) {
        *dst++ = *src++;
    }

    // TODO: Bước 2: Xóa trắng đoạn .bss về 0
    uint32_t *bss = &_sbss;
    while (bss < &_ebss) {
        *bss++ = 0;
    }

    // TODO: Bước 3: Gọi main()
    main();

    // Nếu main trả về, rơi vào vòng lặp vô tận
    while (1) {}
}
