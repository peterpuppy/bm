# 已删除功能归档：heap hook + vmem hook（进程内 Detours 内存 hook）

> **状态：已于 2026-06-22 从引擎删除。** 本目录是恢复依据（完整源码 + 恢复步骤）。
> 本目录归档了从 Chaos 引擎 MemTrack 中**删除**的两个进程内 Detours hook 的**完整源码 + 原理 + 删除原因 + 恢复步骤**。
> 删除原因一句话：**功能与 WPR 离线分析重复，且进程内 hook 有结构性数据盲区**——细粒度归因改由 WPR（`wpr_analyzer` 视图1/2/3）承担，更全更准。
> 若以后仍需进程内实时归因，可据本目录的代码 + 下文恢复步骤重新填充。

## 归档的源码副本

| 文件 | 行 | 作用 |
|---|--:|---|
| `memory_tracker_heap_hook.{h,cpp}` | 59 + 310 | Detours hook `HeapAlloc/HeapFree/HeapReAlloc`，按返回地址把 CRT 堆分配归因到 dll |
| `memory_tracker_vmem_hook.{h,cpp}` | 72 + 638 | Detours hook `VirtualAlloc/Ex/Free/Alloc2 + NtAllocate/NtFreeVirtualMemory`，per-dll reserve/commit 双维度 |
| `memory_tracker_hook_utils.h` | 62 | 两个 hook 共用的 TLS 再入守卫（`InHookGuard`）|

原位置：`H:\cb2\dev\chaos\_source\_engine\source\core\{public,private}\chaos\core\memory\tracker\`。

---

## 一、原理

### heap hook（`memory_tracker_heap_hook.cpp`）
- 用 **Microsoft Detours** 在进程启动早期 patch `kernel32!HeapAlloc / HeapFree / HeapReAlloc` 的入口（trampoline）。
- 每次分配进入 hook：
  1. 调真函数 `Real_HeapAlloc(...)` 拿到指针；
  2. `_ReturnAddress()` 取调用方返回地址；
  3. `resolveModule(ra)`：`GetModuleHandleExA(FROM_ADDRESS)` + `GetModuleInformation` 找返回地址落在哪个 dll，缓存进固定数组（`s_modules`，线性扫描，避免每次分配都查表）；
  4. `recordAlloc(sid, size, p)` 记到 `HeapAllocFrom_<dll>` 这个 Counter source。
- free 路径：先 `HeapSize` 拿块大小再 `Real_HeapFree`，按 freer 的 dll 扣减。
- **TLS 再入守卫**（`hook_utils.h::InHookGuard`）：hook 内部自己的分配（首次注册 source 等）会再入 HeapAlloc，用线程本地标志位短路掉，避免无限递归 / 记重。

### vmem hook（`memory_tracker_vmem_hook.cpp`）
- 同样用 Detours patch 6 个入口：`VirtualAlloc / VirtualAllocEx / VirtualFree / VirtualAlloc2 / NtAllocateVirtualMemory / NtFreeVirtualMemory`。
- **reserve / commit 双维度**：`MEM_RESERVE` 记到 `VirtualAllocReserveFrom_<dll>`，`MEM_COMMIT` 记到 `VirtualAllocCommitFrom_<dll>`（同一次调用可能两者都有）。
- 维护 ptr→size 表（`s_reserveTable` / `s_commitTable`），free 时按指针扣减对应维度。
- `NtAllocateVirtualMemory` 与 `VirtualAlloc` 会重复计同一次提交（VirtualAlloc 内部调 Nt），dump 里把 Nt 那条标为 "NT-level, overlaps CRT, ref only" 避免重复求和。

> 详细逐行见同目录 `.cpp`。

---

## 二、为何数据不全（删除的核心理由）

### ① heap hook：多线程服务器崩溃 0xC0000374
全局 patch 堆函数入口 + trampoline，在高并发多线程进程（游戏服务器）下，hook 与 NT 堆管理器竞争、trampoline 再入踩坏堆元数据，启动即崩 `0xC0000374`（STATUS_HEAP_CORRUPTION），栈停在 `Hook_HeapAlloc`。因此它后来被 `kHeapHookEnabled` 默认关掉——等于功能不可用。

### ② vmem hook：抓不到最大头（D3D12 GPU 资源）
实测最大的 CPU 内存块是 **GPU 资源在系统 RAM 的 backing（~5–8.5 GB）**，它走 `d3d12core.dll!…D3DKMT_CREATEALLOCATION` → **内核**分配。进程内 hook 拦的是用户态 `VirtualAlloc`，这条路径根本不经过；即便经过，返回地址也归 `ntdll`，**看不到真正的业务调用方**。所以 vmem hook 的 per-dll 数据严重残缺。

### ③ 进程内 hook 的结构性盲区（通病）
- **pre-hook 提交**：hook 在 `Memory::initialize()` 才装，之前（静态初始化 / CRT 引导 / 早期驱动 / V8 初始化）的分配全看不到。
- **非覆盖 API**：`MapViewOfFile*` / 直接 syscall / `NtAllocateVirtualMemoryEx` 等绕过。
- **堆内部 malloc 不可分**：VA hook 只看到堆段整体向 OS 要内存（归 `RtlAllocateHeap`），看不到堆内部是谁 malloc 的。

> 对比：WPR 走**内核 ETW**（`VirtualAllocation` 事件 + 完整调用栈），在系统调用边界捕获**所有**提交，带 root→leaf 符号栈，上述盲区全部覆盖。这就是"改用 WPR"的根本原因。

---

## 三、在引擎里的接线（恢复时要还原这些点）

| 接线点 | 文件 | 内容 |
|---|---|---|
| 安装 | `core/private/.../memory/memory.cpp` | `installHeapHook()` + `installVMemHook()`（在 `Tracker::instance().initialize()` 后） |
| 编译开关 | `memory_tracker.h` | `kHeapHookEnabled`（heap hook 专用，默认 false）；受 `kMemTrackEnabled` 总开关 gate |
| 运行期 flag | `memory_tracker.h` `FeatureFlag` 枚举 | `HeapHookActive` / `VirtualAllocHookActive`（hook 内读它决定是否记录）|
| Lua API | `chaos_memory_tracker_manager.{h,cpp}` | `setHeapHookActive(bool)` / `setVirtualAllocHookActive(bool)` |
| dump 段 | `memory_tracker.cpp` dumpSnapshotToLogger | 「CRT Heap per-dll」段（heap hook 数据）+「VirtualAlloc Commit per-dll」段（vmem 数据）+ helper `isHeapAllocFromModule`/`isVMemCommitFromModule`/`isVMemAllocFromModule`/`isNtHookDuplicate` |
| include（仅引用未调用）| `chaos_client_root.cpp` | 两个 hook 头文件的 include |
| 第三方依赖 | `core/CMakeLists.txt` | **Detours**（仅这两个 hook 用；pool_attrib 用 `RtlCaptureStackBackTrace` 非 Detours）|

---

## 四、恢复步骤

1. 把本目录 5 个文件拷回 `tracker/`（.h 回 `public/`，.cpp 回 `private/`）。
2. `memory.cpp`：恢复 `#include` + `installHeapHook()` / `installVMemHook()` 调用。
3. `memory_tracker.h`：恢复 `kHeapHookEnabled` 编译开关；`FeatureFlag` 枚举加回 `HeapHookActive` / `VirtualAllocHookActive`。
4. `memory_tracker.cpp`：`featureFlags` 默认数组加回两项；dump 恢复 CRT per-dll / VA per-dll 两段 + 相关 helper；头 `flags:` 行加回显示。
5. `chaos_memory_tracker_manager.{h,cpp}`：恢复 `setHeapHookActive` / `setVirtualAllocHookActive`。
6. `core/CMakeLists.txt`：恢复 detours conan 链接 —— 在 `chaos_link_custom_libraries("chaos::mempool")` 之后加回：
   ```cmake
   chaos_link_conan_packages(${PROJECT_NAME} PUBLIC
       "detours"
   )
   ```
7. `chaos_client_root.cpp`：恢复两个 include（如需）。
8. heap hook 若上服务器，务必先解决 0xC0000374（见 §二①）——或只在 client 启用。

---

## 五、替代方案（现状）

这两个 hook 的归因能力现由 **WPR 离线分析**承担，见 `features/memory_tracker/wpr_analyzer`：
- **视图1**（直接分配器 dll）替代 vmem/heap 的 per-dll。
- **视图2**（业务调用方 module→函数）给出 hook 给不了的"哪段业务代码触发"。
- **视图3**（非池 heap 按函数）替代 heap hook 的 CRT per-dll，且精确到函数、区分池/非池。

进程内 MemTrack 删除两 hook 后只保留 WPR 给不了的部分：池总量（PoolBridge）、Composition（system gauges）、第三方 gauge、DefaultPool 调用方（opt-in）。

---

## 六、补充问答（随讨论追加）

> 下面记录关于这两个 hook 的进一步问题与解答，作为恢复/复用时的参考。

_(待补充)_
