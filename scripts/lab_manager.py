#!/usr/bin/env python3
"""
Lab & Session Manager for Senior C++ / Embedded Agent Teacher.
Automates lab scaffolding (empty/starter files), session context snapshots, and lab resets.
"""

import argparse
import json
import os
import shutil
import sys
from datetime import datetime

# Đảm bảo in UTF-8 trên Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LABS_DIR = os.path.join(ROOT, "labs")
SESSIONS_DIR = os.path.join(ROOT, "sessions")


LAB_TEMPLATES = {
    "lab01_boot": {
        "title": "Lab 01: The Genesis of main() — Vector Table & Startup Assembly",
        "concept_id": "embed-startup-code",
        "description": "Tự viết startup code, khởi tạo vector table, khởi tạo .data/.bss và nhảy vào main().",
        "files": {
            "README.md": """# Lab 01: The Genesis of main()

## Mục Tiêu
1. Hiểu và tự viết bảng Vector Table tối thiểu chứa Initial MSP và Reset_Handler.
2. Tự viết hàm `Reset_Handler` khởi tạo vùng nhớ:
   - Copy đoạn `.data` từ Flash (LMA) vào SRAM (VMA).
   - Zero-fill toàn bộ đoạn `.bss`.
3. Nhảy vào gọi `main()`.

## Cấu Trúc File
- `src/main.c`: Chương trình chính
- `src/startup.c`: Startup code & Vector Table
- `Makefile`: Lệnh biên dịch và kiểm tra map/disassembly

## Tiêu Chí Đánh Giá (Checklist)
- [ ] Khai báo con trỏ Stack Pointer đỉnh SRAM đúng.
- [ ] Vòng lặp copy `.data` không bị lệch byte hoặc tràn bộ nhớ.
- [ ] Vòng lặp xóa `.bss` chạy đúng kích thước.
- [ ] Giải thích được cờ Thumb-bit trong địa chỉ Reset_Handler.
""",
            "src/main.c": """/**
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
""",
            "src/startup.c": """/**
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
""",
            "Makefile": """CC = arm-none-eabi-gcc
CFLAGS = -mcpu=cortex-m4 -mthumb -O0 -Wall -g
SRCS = src/main.c src/startup.c
OBJS = $(SRCS:.c=.o)

all: firmware.elf

%.o: %.c
	@echo "CC $<"
	$(CC) $(CFLAGS) -c $< -o $@

firmware.elf: $(OBJS)
	@echo "LINK $@"
	$(CC) $(CFLAGS) -T linker.ld -nostdlib $(OBJS) -o $@
	arm-none-eabi-objdump -d firmware.elf > firmware.asm

clean:
	rm -f src/*.o firmware.elf firmware.asm
"""
        }
    }
}


def scaffold_lab(lab_id, custom_name=None):
    os.makedirs(LABS_DIR, exist_ok=True)
    target_dir = os.path.join(LABS_DIR, lab_id)

    if os.path.exists(target_dir):
        print(f"INFO: Thư mục {target_dir} đã tồn tại.")
        return target_dir

    os.makedirs(target_dir, exist_ok=True)

    template = LAB_TEMPLATES.get(lab_id)
    if template:
        for rel_path, content in template["files"].items():
            full_path = os.path.join(target_dir, rel_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)
        print(f"OK: Đã tạo sẵn template cho [{lab_id}] tại: {target_dir}")
    else:
        # Tạo khung sườn cơ bản cho bài mới
        name = custom_name or lab_id
        readme_content = f"# {name}\n\n## Mục tiêu\n\n## TODO\n"
        main_c_content = """#include <stdint.h>\n\nint main(void) {\n    // TODO: Viết code tại đây\n    while (1) {}\n    return 0;\n}\n"""
        
        src_dir = os.path.join(target_dir, "src")
        os.makedirs(src_dir, exist_ok=True)
        with open(os.path.join(target_dir, "README.md"), "w", encoding="utf-8") as f:
            f.write(readme_content)
        with open(os.path.join(src_dir, "main.c"), "w", encoding="utf-8") as f:
            f.write(main_c_content)
        print(f"OK: Đã tạo không gian bài tập mới tại: {target_dir}")

    return target_dir


def list_labs():
    os.makedirs(LABS_DIR, exist_ok=True)
    labs = [d for d in os.listdir(LABS_DIR) if os.path.isdir(os.path.join(LABS_DIR, d))]
    
    print("\n" + "=" * 60)
    print("           DANH SÁCH BÀI TẬP THỰC HÀNH (LABS)")
    print("=" * 60)
    if not labs:
        print("  (Chưa có bài tập nào được tạo trong labs/)")
    else:
        for idx, lab in enumerate(sorted(labs), 1):
            path = os.path.join(LABS_DIR, lab)
            files = []
            for root, _, filenames in os.walk(path):
                for fn in filenames:
                    files.append(os.path.relpath(os.path.join(root, fn), path))
            print(f"  {idx}. [{lab}]")
            print(f"     Đường dẫn: labs/{lab}")
            print(f"     Tệp có sẵn: {', '.join(files[:5])}")
    print("=" * 60 + "\n")


def save_session_snapshot(lab_id, topic, score, passed=True, notes=""):
    os.makedirs(SESSIONS_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    snapshot_filename = f"{lab_id}_{timestamp}.json"
    snapshot_path = os.path.join(SESSIONS_DIR, snapshot_filename)

    data = {
        "session_id": snapshot_filename.replace(".json", ""),
        "timestamp": datetime.now().isoformat(),
        "lab_id": lab_id,
        "topic": topic,
        "score": score,
        "passed": passed,
        "notes": notes
    }

    with open(snapshot_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"OK: Đã lưu snapshot session context tại: {snapshot_path}")
    return snapshot_path


def main():
    parser = argparse.ArgumentParser(description="Quản lý bài tập (Labs) và Session Context cho Agent Teacher")
    parser.add_argument("--create", metavar="LAB_ID", help="Tạo bài tập mới và xuất sẵn file template rỗng")
    parser.add_argument("--name", metavar="NAME", help="Tên hiển thị của bài tập")
    parser.add_argument("--list", action="store_true", help="Liệt kê các lab hiện có")
    parser.add_argument("--snapshot", nargs=3, metavar=("LAB_ID", "TOPIC", "SCORE"), help="Lưu session context JSON")

    args = parser.parse_args()

    if args.create:
        scaffold_lab(args.create, args.name)
    elif args.list:
        list_labs()
    elif args.snapshot:
        save_session_snapshot(args.snapshot[0], args.snapshot[1], int(args.snapshot[2]))
    else:
        list_labs()


if __name__ == "__main__":
    main()
