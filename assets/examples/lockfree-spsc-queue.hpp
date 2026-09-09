/**
 * @file lockfree-spsc-queue.hpp
 * @brief Senior Modern C++ (C++20): Single-Producer Single-Consumer Lock-Free Ring Buffer.
 * Eliminates False Sharing via cacheline alignment and enforces correct memory ordering.
 */

#pragma once

#include <atomic>
#include <cstddef>
#include <new>
#include <optional>
#include <utility>

#ifndef __cpp_lib_hardware_interference_size
namespace std {
    constexpr size_t hardware_destructive_interference_size = 64;
}
#endif

template <typename T, size_t Capacity>
class LockFreeSPSCQueue {
    static_assert((Capacity & (Capacity - 1)) == 0, "Capacity must be a power of 2 for fast modulo!");
    static_assert(Capacity >= 2, "Capacity must be at least 2");

public:
    LockFreeSPSCQueue() : head_(0), tail_(0) {}

    ~LockFreeSPSCQueue() {
        T dummy;
        while (pop(dummy)) {}
    }

    // Cấm copy và gán để bảo toàn quyền sở hữu con trỏ/atomic
    LockFreeSPSCQueue(const LockFreeSPSCQueue&) = delete;
    LockFreeSPSCQueue& operator=(const LockFreeSPSCQueue&) = delete;

    /**
     * @brief Đẩy một phần tử vào hàng đợi (Chỉ được gọi bởi Producer thread).
     */
    template <typename... Args>
    bool emplace(Args&&... args) {
        const size_t current_tail = tail_.load(std::memory_order_relaxed);
        const size_t current_head = head_.load(std::memory_order_acquire);

        // Hàng đợi đầy khi tail đuổi kịp head từ phía sau
        if ((current_tail - current_head) >= Capacity) {
            return false; // Queue Full
        }

        // Khởi tạo đối tượng in-place tại slot buffer
        new (&buffer_[current_tail & BufferMask].storage) T(std::forward<Args>(args)...);

        // Xuất bản chỉ số tail mới với quan hệ Release
        tail_.store(current_tail + 1, std::memory_order_release);
        return true;
    }

    /**
     * @brief Lấy một phần tử ra khỏi hàng đợi (Chỉ được gọi bởi Consumer thread).
     */
    bool pop(T& val) {
        const size_t current_head = head_.load(std::memory_order_relaxed);
        const size_t current_tail = tail_.load(std::memory_order_acquire);

        // Hàng đợi rỗng khi head bắt kịp tail
        if (current_head == current_tail) {
            return false; // Queue Empty
        }

        auto* item_ptr = reinterpret_cast<T*>(&buffer_[current_head & BufferMask].storage);
        val = std::move(*item_ptr);
        item_ptr->~T();

        // Xuất bản chỉ số head mới với quan hệ Release
        head_.store(current_head + 1, std::memory_order_release);
        return true;
    }

private:
    static constexpr size_t BufferMask = Capacity - 1;

    struct Node {
        alignas(alignof(T)) std::byte storage[sizeof(T)];
    };

    Node buffer_[Capacity];

    // Chống hiện tượng False Sharing: Đặt head_ và tail_ trên 2 Cache Line khác nhau
    alignas(std::hardware_destructive_interference_size) std::atomic<size_t> head_;
    alignas(std::hardware_destructive_interference_size) std::atomic<size_t> tail_;
};
