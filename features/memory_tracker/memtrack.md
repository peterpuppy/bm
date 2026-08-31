# MemTrack — 进程内内存观察层

Chaos 引擎内建的进程内内存统计基础设施（命名空间 `Chaos::MemTrack`）。提供**游戏内实时的内存总量仪表**，并作为对接 Tracy / HUD / 上报等的统计中枢。与离线的 **WPA/WPR 分析**（独立工具仓库 `E:\code\memory_analyzer`）分工互补。

> ⚠️ 命名空间是 `Chaos::MemTrack`，不要用 `Chaos::MemoryTracker`（被 `datum_manager.h` 的 friend 占了）。

---

## 一、定位

| | MemTrack | WPA / WPR（`memory_analyzer`）|
|---|---|---|
| 角色 | **实时仪表 + 数据中枢**（进程内、常驻、便宜）| **离线显微镜**（内核级、带调用栈）|
| 看什么 | 当前**总量**：各池 / Composition / 子系统 gauge | **按 dll / 函数**归因 |
| 何时用 | 游戏内随时看"涨没涨、哪个池大、覆盖率"，喂 HUD/Tracy | 定位"具体哪个函数分配的" |

一句话：**MemTrack 是仪表盘（实时统计、池维度、对接 Tracy），WPA 是显微镜（出按函数的报告）。**

---

## 二、基本设计

MemTrack 是一个**采集与展示解耦**的统计框架：多个"数据源"把内存数字喂给中心 `Tracker`，再由多个"出口"消费。

```
   数据源（生产者）                 Tracker（中心）              出口（消费者）
 ┌─────────────────┐          ┌──────────────────┐        ┌────────────────┐
 │ PoolBridge      │──┐       │  源注册表         │     ┌─→│ dump 到日志     │
 │ system_gauges   │──┼──记录→│  Counter / Gauge  │──读─┤  │ (周期+Composition)│
 │ 第三方 gauge    │──┤       │  线程安全/lock-free│     └─→│ ISink → Tracy   │
 │ pool_attrib     │──┘       └──────────────────┘        │ / HUD / 上报    │
 └─────────────────┘                                       └────────────────┘
```

### 核心：Tracker（单例）
内存"源"的注册中心。每个源是两类之一：
- **Counter**：事件驱动，`recordAlloc/recordFree` 累加（saturating，free 多了 clamp 0）。
- **Gauge**：周期总量快照，`recordGauge` 覆盖上一次值。

三个核心 API：`registerSource(name, kind)` → 拿 `SourceId`；热路径 `recordAlloc/Free/Gauge(id, ...)`；读出 `getAllSourceStats(...)`。注册表 lock-free 读、源永不释放（进程生命周期）。

### 数据源（生产者）
| 源 | 提供 | 类型 |
|---|---|---|
| **PoolBridge** | 每个 mempool 池的总量（cur/peak/allocs/frees）| Counter |
| **system_gauges** | ProcessCommit / GPU 显存(DXGI) / 全堆 busy(HeapWalk) / AddressSpace(VirtualQueryEx) / 线程栈 | Gauge |
| **第三方 gauge** | Wwise / cohtml ImageCache / Lua heap / Coherent | Gauge |
| **pool_attrib**（opt-in）| DefaultPool 的 top 调用方（net-live，`RtlCaptureStackBackTrace`）| 调用方表 |

### 出口（消费者）
- **dump**：周期（默认 30s）把所有源渲染成多段文本到日志，末尾附 **Composition Summary**（`Total CPU = Image+Mapped+Private`、`Tracked`、`Blind spot`、覆盖率）。
- **ISink**：`onAlloc/onFree/onGauge` 接口 + `Tracker::registerSink()`——挂载点。实现一个 sink 即可把同一份数据接到 Tracy 实时图表 / HUD / 上报系统（一份采集，多个出口）。

### 管理层
`MemoryTrackerManager`（标准 manager pattern，在 `g_common_global_context`）：负责 install 数据源、主循环 tick 触发 dump、对外暴露 Lua API。

### 总开关
运行时开关，`Tracker::setEnabled(bool)`（atomic，**默认 false**），从 Lua 实时切换、**无需重编译**。关闭时数据源不上报、不 dump；生产者（PoolBridge + system gauges）**惰性安装**——首次 `setEnabled(true)` 才装，从不启用的构建零成本。

---

## 三、使用

### 启用
从 Lua 打开（见下），无需改代码重编译：
```lua
global_context.m_memory_tracker_manager:setEnabled(true)
```
> 尽早开启：关闭期间发生的分配不计入，开启后才开始累计。

### Lua 控制
`CommonGlobalContext` 是 Lua 全局 `global_context`，`m_memory_tracker_manager` 字段与方法都注册给了 Lua：

```lua
local mgr = global_context.m_memory_tracker_manager
mgr:setEnabled(true)                  -- 总开关（惰性安装 + 开始 dump）
mgr:dump()                            -- 立即 dump
mgr:setDumpIntervalSeconds(10)        -- 改周期
mgr:setDumpTopN(0)                    -- 每段行数（0=全部）
mgr:setPoolDefaultCallerAttrib(true)  -- 开 DefaultPool 调用方采集
mgr:dumpPoolDefaultCallers()          -- 打印 top 调用方
mgr:getProcessCommitBytes()           -- 取单项总量给 HUD/自动化
mgr:setEnabled(false)                 -- 关闭（停止上报 + dump）
```

### dump 输出形态（30s 周期）
```
======== MemTrack snapshot  frame=N  sources=M ========
  flags: PoolAttrib=off
---- Pool (top all; total X) ----                  各 mempool 池 cur/peak/allocs/frees
---- DefaultPool caller breakdown (top 20) ----     仅 PoolAttrib 开启时
---- CRT Heap: all-heaps busy = X ----              全堆 busy 总量（HeapWalk）
---- Observation / Other ----                       GPU / Coherent / Wwise / Lua / cohtml gauge
---- Address Space (VirtualQueryEx) ----            Image / Mapped / Private / PrivDataLarge
========== Composition Summary ==========           Total CPU / Tracked / Blind spot / 覆盖率
```

---

## 四、与 WPA 的分工

- **MemTrack 的池维度**（PoolDefault/PhysXPool 等逻辑池总量）是引擎领域概念，WPA 看不到——这是 MemTrack 独有。
- **MemTrack 的 Composition Blind spot** ≈ WPA 的 direct VA（D3D12/V8/Coherent 等裸 VirtualAlloc）——MemTrack 知道"有多少看不到"，WPA 能按函数说清是谁。
- **口径互相印证**：同场景 MemTrack 的 Private ≈ WPA 的 net-resident 总量（实测吻合）。
- 闭环：**MemTrack 实时发现"涨了/某池大" → WPA 离线定位"具体哪个函数"**。

---

## 五、代码位置（chaos 引擎）

```
source/core/{public,private}/chaos/core/memory/tracker/
  memory_tracker.{h,cpp}            -- Tracker 核心 + dump + Composition
  memory_tracker_sink.h             -- ISink 接口（Tracy/HUD 挂载点）
  memory_tracker_pool_bridge.*      -- 池总量
  memory_tracker_system_gauges.*    -- ProcessCommit / GPU / 全堆 busy / AddrSpace / 栈
  memory_tracker_pool_attrib.*      -- DefaultPool 调用方（opt-in）+ symbols + ptr_table
  memory_tracker_macros.h           -- CHAOS_MEM_TRACKER_* 便利宏
source/common/.../memory/chaos_memory_tracker_manager.{h,cpp}  -- Manager + Lua API
source/core/private/.../memory/memory.cpp                       -- Tracker::initialize()
```

安装链：`MemoryTrackerManager::initialize()` 起 Tracker（不装生产者）；首次 `setEnabled(true)` 惰性装 PoolBridge + system gauges；client/server 主循环 tick 在开启时触发 dump。`Tracker::isEnabled()` gate 全部上报与 dump。

> 离线分析工具是独立仓库 `E:\code\memory_analyzer`（`wpr.py` + `usage.md`），实测报告见 [`docs/reports/`](docs/reports/)。
