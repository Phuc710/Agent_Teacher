# Lab 01: The Genesis of main()

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
