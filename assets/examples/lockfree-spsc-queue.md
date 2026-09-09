# Bài Giảng Chuẩn Mẫu: Hàng Đợi Không Khóa (Lock-Free SPSC Queue) Trong C++20

Ví dụ bài giảng thực tế cho chủ đề **Tối ưu hóa hiệu năng cao & Bộ nhớ đệm CPU** theo chuẩn 6 tầng.

---

## 1. Intuition (Vấn Đề Phần Cứng & Xung Nhịp Giải Quyết)

Khi truyền dữ liệu tần số cao giữa 2 luồng (ví dụ: luồng nhận gói tin mạng 10Gbps và luồng xử lý), phương án trực quan của người mới là dùng `std::mutex` và `std::queue`:
```cpp
std::mutex mtx;
std::queue<Data> q;
// Mỗi lần push/pop đều gọi: std::lock_guard<std::mutex> lock(mtx);
```
**Bế tắc kỹ thuật:**
1. Mỗi lần tranh chấp Mutex thất bại, Hệ điều hành phải đưa luồng vào trạng thái Sleep, kích hoạt System Call và hoán đổi ngữ cảnh (Context Switch), tiêu tốn hàng ngàn chu kỳ CPU.
2. Trong môi trường nhúng, **ISR không bao giờ được phép dùng Mutex** vì ISR không thể bị block/sleep.

**Lock-Free Single-Producer Single-Consumer (SPSC) Queue** giải quyết vấn đề bằng cách:
Không khóa, không block, chỉ dùng 2 con trỏ chỉ số atomic `head` và `tail` giao tiếp qua quan hệ đồng bộ hóa bộ nhớ **Acquire-Release**, đạt độ trễ sub-microsecond.

---

## 2. Mental Model & Memory Layout (Hiện Tượng False Sharing)

### Kiến trúc bộ đệm vòng (Ring Buffer):
```
Buffer [0] [1] [2] [3] [4] [5] [6] [7]  (Capacity = 8, Mask = 7)
            ▲               ▲
            │               │
          head_           tail_
       (Consumer đọc)   (Producer ghi)
```

### Bẫy False Sharing trên Cache Line:
Kích thước 1 Cache Line của CPU hiện đại thường là **64 byte**.
Nếu `head_` (8 byte) và `tail_` (8 byte) nằm cạnh nhau trong cùng một struct:
```
[ ---------------- 1 Cache Line (64 bytes) ---------------- ]
[ head_ (8B) | tail_ (8B) | unused padding (48B)           ]
```
Mỗi khi Producer cập nhật `tail_`, L1 Cache của CPU lõi 1 gửi tín hiệu vô hiệu hóa (Cache Invalidation) tới toàn bộ Cache Line trên CPU lõi 2 (nơi Consumer đang đọc `head_`), làm tốc độ tụt thê thảm dù logic không hề có lock!

**Giải pháp Senior:** Dùng `alignas(64)` để đẩy `head_` và `tail_` sang 2 Cache Line tách biệt hoàn toàn.

---

## 3. Mã Nguồn Mẫu
Xem chi tiết mã nguồn hoàn chỉnh tại [lockfree-spsc-queue.hpp](file:///c:/Users/Phucx/Desktop/Agent_Teacher/assets/examples/lockfree-spsc-queue.hpp).

---

## 4. Traps & Undefined Behavior

1. **Bẫy Memory Order:** Dùng `memory_order_relaxed` cho `tail_.store()` sẽ cho phép compiler hoặc CPU reorder lệnh ghi dữ liệu ra sau lệnh tăng `tail_`, khiến Consumer đọc phải dữ liệu rác chưa kịp khởi tạo! Bắt buộc phải dùng `memory_order_release` khi ghi và `memory_order_acquire` khi đọc.
2. **Bẫy Wrap-around:** Không cần dùng phép chia lấy dư `% Capacity` (rất chậm trên CPU). Hãy bắt buộc `Capacity` là lũy thừa của 2 (`power of 2`) để thay thế bằng phép toán bitwise `index & (Capacity - 1)` cực nhanh chỉ mất 1 chu kỳ.
