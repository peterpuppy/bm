# Memory Tracker — Feature Anchor

**目标**：Chaos 引擎内统一内存观察层（`Chaos::MemTrack`），覆盖 mempool + 第三方（Coherent/Wwise/Lua）+ OS 级（ProcessCommit/AddrSpace/CRT heap/GPU）。进程内只做"总量仪表"；per-dll/per-function 归因转离线 WPR 工具。

**当前形态**：实时层（进程内、便宜、无 Tracy）+ 离线层（WPR 内核级，独立仓库 `E:\code\memory_analyzer`）。heap/vmem hook 已删（源码归档 `archive/deleted_hooks/`），Tracy 路线已废弃。

> 权威细节在 [memtrack.md](memtrack.md)（设计/使用/与 WPA 互补）。Phase 历史、dump 输出样例、完整接线/探针清单都在 memtrack.md，本锚点只留高频要点。

## 文档导航
| 文档 | 用途 |
|---|---|
| [memtrack.md](memtrack.md) | MemTrack 总文档：设计 / 使用 / 能力边界 / 与 WPA 互补 |
| `E:\code\memory_analyzer\usage.md` | 离线分析工具（独立仓库） |
| [docs/reports/](docs/reports/) | 三场景成果报告 + 对比建议 |

`raw/`（被 .gitignore）按场景存原始数据 + 分析产物；`features/memory_tracker/reexport.bat` 一键重出。

## 命名空间防坑
⚠️ 不要用 `Chaos::MemoryTracker`——`datum_manager.h:21` 的 `friend class MemoryTracker;` 占了这个名字。本 feature 用 `Chaos::MemTrack`。

## 关键代码位置（chaos 引擎）
```
source/core/{public,private}/chaos/core/memory/tracker/
  memory_tracker.{h,cpp}          Tracker 核心 + dump + Composition
  memory_tracker_pool_bridge.*    池总量
  memory_tracker_system_gauges.*  ProcessCommit / GPU / 全堆busy(HeapWalk) / AddrSpace / 栈
  memory_tracker_pool_attrib.*    DefaultPool 调用方归因(opt-in) + symbols + ptr_table
  memory_tracker_macros.h 便利宏；memory_tracker_sink.h ISink(未用)
source/common/.../memory/chaos_memory_tracker_manager.{h,cpp}  Manager + Lua API
```
接线点 + 第三方 gauge 探针清单见 memtrack.md「代码位置」段。

## 三个核心 API
```cpp
SourceId id = Tracker::instance().registerSource("Name", SourceKind::Counter); // or Gauge
Tracker::instance().recordAlloc(id, bytes, ptr);
Tracker::instance().recordFree (id, bytes, ptr);   // saturating: cur<bytes 时 clamp 0
Tracker::instance().recordGauge(id, totalBytes);
// 或便利宏（memory_tracker_macros.h）：CHAOS_MEM_TRACKER_REGISTER_COUNTER / _RECORD_ALLOC
```

## 总开关 / dump
运行时开关 `Tracker::setEnabled`（atomic，默认 false；生产者惰性安装 → 从不启用即零成本）。Lua 实时开，无需重编译：
```lua
global_context.m_memory_tracker_manager:setEnabled(true)
```
`MemoryTrackerManager`（在 `g_common_global_context`）由 client 主循环 tick，默认 30s dump（`m_dump_interval_sec`）。dump 输出形态见 memtrack.md。
