#!/usr/bin/env python3
"""
Learning Profile & Knowledge Graph Tracker for Senior C++ / Embedded Agent Teacher.
Manages student mastery states, checks prerequisites, and outputs visual progress reports.
"""

import argparse
import json
import os
import sys
from datetime import datetime

# Đảm bảo in UTF-8 không lỗi trên Windows cmd/powershell
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

PROFILE_FILE = "learning_profile.json"

DEFAULT_KNOWLEDGE_GRAPH = {
    "c-memory-layout": {
        "name": "Bố cục bộ nhớ tiến trình (Stack/Heap/BSS/Data/Text)",
        "category": "C & Pointer Mastery",
        "prereqs": [],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "c-pointer-arithmetic": {
        "name": "Con trỏ & Số học con trỏ (Pointer Arithmetic)",
        "category": "C & Pointer Mastery",
        "prereqs": ["c-memory-layout"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "c-function-pointer": {
        "name": "Con trỏ hàm & Callback (Function Pointers)",
        "category": "C & Pointer Mastery",
        "prereqs": ["c-pointer-arithmetic"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "c-volatile": {
        "name": "Từ khóa volatile & Compiler Optimization",
        "category": "C & Pointer Mastery",
        "prereqs": ["c-pointer-arithmetic"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "c-struct-padding-alignment": {
        "name": "Đệm cấu trúc & Canh lề bộ nhớ (Padding & Alignment)",
        "category": "C & Pointer Mastery",
        "prereqs": ["c-pointer-arithmetic"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "cpp-raii": {
        "name": "RAII & Resource Management",
        "category": "Modern C++ Core",
        "prereqs": ["c-memory-layout"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "cpp-move-semantics": {
        "name": "Move Semantics & Rvalue References (&&)",
        "category": "Modern C++ Core",
        "prereqs": ["cpp-raii", "c-pointer-arithmetic"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "cpp-smart-pointers": {
        "name": "Smart Pointers (unique_ptr, shared_ptr)",
        "category": "Modern C++ Core",
        "prereqs": ["cpp-move-semantics", "cpp-raii"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "cpp-vtable-polymorphism": {
        "name": "Đa hình & Cơ chế VTable / _vptr",
        "category": "Modern C++ Core",
        "prereqs": ["c-function-pointer", "c-struct-padding-alignment"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "cpp-memory-model-atomics": {
        "name": "C++ Memory Model & std::atomic (Memory Orders)",
        "category": "Modern C++ Core",
        "prereqs": ["c-volatile", "c-memory-layout"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "arch-registers-abi": {
        "name": "Tập thanh ghi CPU & Calling Conventions",
        "category": "Computer Architecture & Assembly",
        "prereqs": ["c-memory-layout"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "arch-stack-frame": {
        "name": "Cấu trúc Stack Frame & Hardware Context Save",
        "category": "Computer Architecture & Assembly",
        "prereqs": ["arch-registers-abi"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "arch-inline-assembly": {
        "name": "GCC Inline Assembly & Clobber List",
        "category": "Computer Architecture & Assembly",
        "prereqs": ["arch-registers-abi"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "arch-cache-locality": {
        "name": "Cache Line, False Sharing & Memory Hierarchy",
        "category": "Computer Architecture & Assembly",
        "prereqs": ["c-struct-padding-alignment"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "embed-memory-mapped-io": {
        "name": "Memory Mapped I/O (MMIO) & Bitwise Registers",
        "category": "Embedded Systems & Bare-Metal",
        "prereqs": ["c-volatile", "c-pointer-arithmetic"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "embed-startup-code": {
        "name": "Quy trình khởi động MCU & Startup Code",
        "category": "Embedded Systems & Bare-Metal",
        "prereqs": ["c-memory-layout", "arch-registers-abi"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "embed-vector-table": {
        "name": "Bảng Vector Ngắt (Vector Table & VTOR)",
        "category": "Embedded Systems & Bare-Metal",
        "prereqs": ["embed-startup-code", "c-function-pointer"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "embed-nvic-interrupt": {
        "name": "Bộ điều khiển ngắt NVIC & ISR Lifecycle",
        "category": "Embedded Systems & Bare-Metal",
        "prereqs": ["embed-vector-table", "arch-stack-frame", "embed-memory-mapped-io"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "embed-zero-hal-driver": {
        "name": "Viết Driver Bare-Metal không dùng thư viện hãng",
        "category": "Embedded Systems & Bare-Metal",
        "prereqs": ["embed-memory-mapped-io", "embed-nvic-interrupt"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "rtos-context-switch": {
        "name": "Chuyển đổi ngữ cảnh PendSV & Context Switching",
        "category": "RTOS & Real-Time Systems",
        "prereqs": ["arch-stack-frame", "embed-nvic-interrupt", "arch-inline-assembly"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "rtos-scheduler": {
        "name": "Bộ lập lịch Task & Trạng thái Task (Ready/Blocked)",
        "category": "RTOS & Real-Time Systems",
        "prereqs": ["rtos-context-switch"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "rtos-sync-primitives": {
        "name": "Đồng bộ hóa: Semaphore, Mutex & Priority Inversion",
        "category": "RTOS & Real-Time Systems",
        "prereqs": ["rtos-scheduler"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "perf-lockfree-queue": {
        "name": "Lock-Free Ring Buffer / SPSC Queue với std::atomic",
        "category": "High Performance & Concurrency",
        "prereqs": ["cpp-memory-model-atomics", "arch-cache-locality"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    },
    "perf-zero-copy": {
        "name": "Kiến trúc Zero-Copy DMA & Cache Maintenance",
        "category": "High Performance & Concurrency",
        "prereqs": ["embed-memory-mapped-io", "arch-cache-locality"],
        "status": "MISSING",
        "score": 0,
        "last_assessed": None
    }
}


def load_profile(path=PROFILE_FILE):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_profile(data, path=PROFILE_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def init_profile(path=PROFILE_FILE):
    if os.path.exists(path):
        print(f"INFO: {path} đã tồn tại. Đang tải và hợp nhất các node mới...")
        current = load_profile(path)
        for k, v in DEFAULT_KNOWLEDGE_GRAPH.items():
            if k not in current.get("nodes", {}):
                current["nodes"][k] = v
        save_profile(current, path)
        print(f"OK: Đã đồng bộ profile tại {path}")
        return current

    profile = {
        "version": "1.0.0",
        "student_name": "Senior C++ Apprentice",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "nodes": DEFAULT_KNOWLEDGE_GRAPH
    }
    save_profile(profile, path)
    print(f"OK: Đã khởi tạo hồ sơ tri thức thành công tại {path}")
    return profile


def update_node(node_id, status, score, path=PROFILE_FILE):
    profile = load_profile(path) or init_profile(path)
    nodes = profile.get("nodes", {})

    # Tìm kiếm theo ID hoặc chuỗi tên tương đồng
    matched_id = None
    if node_id in nodes:
        matched_id = node_id
    else:
        for k, v in nodes.items():
            if node_id.lower() in k.lower() or node_id.lower() in v["name"].lower():
                matched_id = k
                break

    if not matched_id:
        print(f"ERROR: Không tìm thấy node '{node_id}' trong đồ thị tri thức.", file=sys.stderr)
        return False

    status = status.upper()
    valid_statuses = ["MASTERED", "PARTIAL", "WEAK", "MISSING"]
    if status not in valid_statuses:
        print(f"ERROR: Trạng thái không hợp lệ. Chọn một trong: {valid_statuses}", file=sys.stderr)
        return False

    nodes[matched_id]["status"] = status
    nodes[matched_id]["score"] = int(score)
    nodes[matched_id]["last_assessed"] = datetime.now().isoformat()
    profile["updated_at"] = datetime.now().isoformat()

    save_profile(profile, path)
    print(f"OK: Đã cập nhật node '{matched_id}' -> [{status}] ({score}/100)")
    return True


def check_prereqs(node_id, path=PROFILE_FILE):
    profile = load_profile(path) or init_profile(path)
    nodes = profile.get("nodes", {})

    matched_id = None
    if node_id in nodes:
        matched_id = node_id
    else:
        for k, v in nodes.items():
            if node_id.lower() in k.lower() or node_id.lower() in v["name"].lower():
                matched_id = k
                break

    if not matched_id:
        print(f"ERROR: Không tìm thấy node '{node_id}'", file=sys.stderr)
        return False

    target = nodes[matched_id]
    prereqs = target.get("prereqs", [])

    print(f"\nKiểm tra điều kiện tiên quyết cho: [{matched_id}] - {target['name']}")
    print("-" * 70)

    if not prereqs:
        print("✓ Khái niệm này là nền tảng khởi đầu, không có điều kiện tiên quyết bắt buộc.")
        return True

    all_passed = True
    for p in prereqs:
        p_info = nodes.get(p, {})
        status = p_info.get("status", "MISSING")
        score = p_info.get("score", 0)
        p_name = p_info.get("name", p)

        if status == "MASTERED" or score >= 75:
            print(f"  ✓ [{p}] {p_name}: {status} ({score}/100)")
        elif status == "PARTIAL" or score >= 50:
            print(f"  ⚠ [{p}] {p_name}: {status} ({score}/100) -> Cần củng cố thêm")
        else:
            print(f"  ❌ [{p}] {p_name}: {status} ({score}/100) -> HỔNG KIẾN THỨC NỀN!")
            all_passed = False

    print("-" * 70)
    if all_passed:
        print(">> ĐÁNH GIÁ: Đủ điều kiện để học sâu chủ đề này.")
    else:
        print(">> CẢNH BÁO: Học viên chưa nắm vững các kiến thức nền tảng phía trên!")
        print(">> Khuyến nghị: Ôn tập các node bị đánh dấu [❌] trước khi vào chi tiết phức tạp.")
    return all_passed


def print_status_tree(path=PROFILE_FILE):
    profile = load_profile(path) or init_profile(path)
    nodes = profile.get("nodes", {})

    print("\n" + "=" * 75)
    print("           BẢN ĐỒ TRI THỨC SENIOR C++ & EMBEDDED SYSTEMS")
    print("=" * 75)

    categories = {}
    for k, v in nodes.items():
        cat = v.get("category", "Other")
        categories.setdefault(cat, []).append((k, v))

    total = len(nodes)
    mastered = sum(1 for _, v in nodes.items() if v.get("status") == "MASTERED")
    partial = sum(1 for _, v in nodes.items() if v.get("status") == "PARTIAL")
    weak = sum(1 for _, v in nodes.items() if v.get("status") == "WEAK")
    missing = total - (mastered + partial + weak)

    status_icons = {
        "MASTERED": "✓ [Hoàn tất]",
        "PARTIAL": "⚠ [Đang học]",
        "WEAK": "⚡ [Cần ôn]",
        "MISSING": "· [Chưa học]"
    }

    for cat, items in categories.items():
        print(f"\n📁 {cat.upper()}")
        print("   " + "-" * 65)
        for node_id, data in items:
            st = data.get("status", "MISSING")
            score = data.get("score", 0)
            icon = status_icons.get(st, "·")
            print(f"   {icon:<15} {node_id:<28} {score:>3}/100 | {data['name']}")

    print("\n" + "=" * 75)
    print(f"Tổng kết: {mastered} Mastered | {partial} Partial | {weak} Weak | {missing} Missing / {total} Concepts")
    progress = (mastered * 100 + partial * 50 + weak * 20) / (total * 100) * 100
    print(f"Độ hoàn thiện lộ trình Senior: {progress:.1f}%")
    print("=" * 75 + "\n")


def main():
    parser = argparse.ArgumentParser(description="Quản lý hồ sơ tri thức Senior C++ / Embedded Agent Teacher")
    parser.add_argument("--init", action="store_true", help="Khởi tạo hoặc đồng bộ profile")
    parser.add_argument("--status", action="store_true", help="Hiển thị cây tri thức và tiến độ hiện tại")
    parser.add_argument("--check", metavar="NODE_ID", help="Kiểm tra điều kiện tiên quyết của một chủ đề")
    parser.add_argument("--update", metavar="NODE_ID", help="Cập nhật trạng thái chủ đề")
    parser.add_argument("--state", choices=["MASTERED", "PARTIAL", "WEAK", "MISSING"], default="MASTERED", help="Trạng thái cập nhật")
    parser.add_argument("--score", type=int, default=85, help="Điểm đánh giá (0-100)")

    args = parser.parse_args()

    if args.init:
        init_profile()
    elif args.status:
        print_status_tree()
    elif args.check:
        check_prereqs(args.check)
    elif args.update:
        update_node(args.update, args.state, args.score)
    else:
        print_status_tree()


if __name__ == "__main__":
    main()
