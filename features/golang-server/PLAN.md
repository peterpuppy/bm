# 方案：模块设计 + 迁移

> 现状见 [CURRENT_STATE.md](CURRENT_STATE.md)｜进度见 [STATUS.md](STATUS.md)
>
> **范围**：`chaos` + `proven_ground` 全部服务端进程。**不含 GameServer**
> （`_ServiceType_GAM` / `GAM_LOCAL` 及其专属 C++ 模块 `game_server_common` 11.2 万行）。

---

## 一、任务两块

| 块 | 是什么 | 规模 | 人日 |
|---|---|---|---:|
| **Ⅰ 基础模块** | Go 侧底层能力，分 `gosvc`（通用框架）+ `chaosadapter`（对接层） | 对应 C++ 手写 ≈ 6.6 万行 | **171** |
| **Ⅱ 业务迁移** | 41 个 Lua 服务 + 7 个 C++ 专用服务 + 迁移基建 | Lua 44.4 万行 + C++ 2.9 万行 | **4,918** |

---

## 二、Go 侧模块设计

### 2.1 两层切分：`gosvc` 与 `chaosadapter`

**结论：要分，而且这是本方案最重要的一个结构决定。**

判定规则一句话：**改了会和 Lua/C++ 对不上的，进 `chaosadapter`；其余进 `gosvc`。**

分层的四个理由：

1. **把兼容性风险关进一个包**。整个项目最危险的东西——二进制协议、一致性哈希、etcd
   value 格式、埋点 JSON 字段、ID 格式——全部只在 `chaosadapter` 里。这个包配跨语言黄金测试
   并进 CI；包外就是普通 Go 代码，普通单测即可。
2. **变更半径固定**。IDL 改、协议改、哈希改，只动一个包，不会扩散到 20 个服务。
3. **可退场**。Lua 侧最终收缩时（或只剩 GameServer），adapter 整体瘦身甚至删除，
   `gosvc` 与业务代码不动。反过来若这条路走不通，止损也只丢一个包。
4. **降低上手门槛**。写业务的人只碰 `gosvc` + 生成的 stub，不需要懂 Chaos 二进制协议。

**明确不要做的**：`chaosadapter` **不做成 interface + 多实现**。它只有一个实现，
永远只会有一个。它是个包边界，用具体类型，不要为了"可替换"造抽象。

### 2.2 目录布局

现状是扁平布局（`auth_server/`、`chaos_sdk/`、`rpc/` 平铺），需要一次重排：

```
booming/
├── cmd/<service>/main.go        每服务一个入口，只做装配
├── gosvc/                       通用框架，与 Chaos 无关，可脱离 Chaos 独立测试
│   ├── app/       生命周期：启动编排、优雅退出、panic recover、健康检查
│   ├── log/       slog 封装（字段规范、分级、轮转）
│   ├── conf/      配置加载（XML/JSON）+ 热更监听
│   ├── netx/      TCP 长连接：分帧、重连、心跳、背压、连接池
│   ├── shard/     按 key 分片 worker 池（同实体串行、跨实体并行）
│   ├── task/      本地定时器 + 分布式单次任务（多实例只跑一次）
│   ├── store/     redis / mysql / mongo 连接与事务
│   ├── obs/       metrics + tracing + 运行时指标
│   └── debugx/    pprof / expvar / 在线诊断命令
├── chaosadapter/                ★ 唯一需要跨语言字节兼容的地方
│   ├── codec/     RPCPackage 编解码 + 基础类型（DID / GUID / ItemID / Vector3…）
│   ├── rpcrt/     RPC 运行时：请求-响应关联、超时、错误码、事件 pub/sub
│   ├── registry/  etcd key/value 格式 + ServiceType 表
│   ├── routing/   5 种路由规则 + MurmurHash 一致性哈希环
│   ├── sticky/    粘性会话表 + Running/Stopping/Stopped 状态机
│   ├── design/    设计表 / GPA 资产读取
│   ├── idgen/     global_id / item_id / sn 格式
│   └── gamelog/   埋点 JSON → log_server
├── rpc/                         .nsd 生成物（已有 103 万行，禁止手改）
└── svc/<service>/               各服务业务逻辑
```

### 2.3 模块归属表

**状态**：✅ 已可用｜⚠️ 有但需改造｜❌ 缺失

| # | 模块 | 层 | 包 | 对应现状 | Go 现状 | 人日 | 风险 |
|---|---|:--:|---|---|:--:|---:|:--:|
| M-01 | 底层网络 | gosvc | `netx/` | `common/net/` 11.4k | ⚠️ 无重连无背压 | 10 | ★★ |
| M-02 | 协议 codec | **adapter** | `codec/` | `common/sketum/` 3.3k + `rpc/` 890 | ✅ `rpc_base/` | 5 | ★★★ |
| M-03 | schema 代码生成 | **adapter** | `rpc/`（生成物） | 生成器已存在 | ✅ 48 服务 103 万行 | 8 | ★ |
| M-04 | RPC 运行时 | **adapter** | `rpcrt/` | `backend/rpc/` 3.2k | ⚠️ 7 函数空 + 超时 bug + 双反射 | 12 | ★★★ |
| M-05 | 服务发现 | **adapter** | `registry/` | `backend/service/` + `etcd/` | ✅ `service_discover_v3.go` | 3 | ★ |
| M-06 | **路由与一致性哈希** | **adapter** | `routing/` | `..._service_discovery_manager.cpp:1575` | ❌ `ByHash` 空实现，无 MurmurHash | 10 | **★★★★★** |
| M-07 | 并发调度 | gosvc | `shard/` | Lua 单线程协程 | ❌ 全局单队列 | 8 | ★★★★ |
| M-08 | 粘性会话与弹性 | **adapter** | `sticky/` | `backend/sticky_session/` 679 + Lua scaling | ❌ | 12 | ★★★ |
| M-09 | 缓存 ORM | gosvc + adapter | `store/` + 键格式在 adapter | `backend/cache/` 9.9k + Lua `cache_orm/` | ❌ | 15 | ★★★ |
| M-10 | 持久化 | gosvc | `store/` | `mysql_connection/` 3.4k + `mongodb/` 259 | ❌ | 8 | ★★ |
| M-11 | 埋点日志 | **adapter** | `gamelog/` | `common/log_service/` 412 + Lua `logic_log/` 13.5k | ❌ | 12 | ★★★ |
| M-12 | 运行日志 | gosvc | `log/` | `common/logger/` 68 | ⚠️ 用 gf glog | 4 | ★ |
| M-13 | 配置 | gosvc | `conf/` | `backend/config/` 694 + Lua config_center | ⚠️ 简易读取 | 8 | ★★ |
| M-14 | 追踪与指标 | gosvc | `obs/` | `backend/tracing/` 843（**已接 OTel**）+ `status_reporter/` 194 | ❌ | 8 | ★★ |
| M-15 | 时间服务 | gosvc | `app/`（或独立 `timex/`） | `common/os/` 564 + Lua TimeService（**1575 处**） | ❌ | 6 | ★★★ |
| M-16 | 定时器 | gosvc | `task/` | `common/tick/` 972 + `backend/tick/` 203 | ⚠️ `timer.go` 基础版 | 6 | ★★ |
| M-17 | HTTP | gosvc | `netx/http` | `common/http/` 1.4k + Lua http | ⚠️ 用 gf ghttp | 5 | ★ |
| M-18 | **设计表 / 资产** | **adapter** | `design/` | `common/design/` 5.7k + `asset/` 6.5k + `gpa/` 1k | ❌ | 15 | **★★★★** |
| M-19 | ID 生成 | **adapter** | `idgen/` | `backend/global_id/` 130 + `item_id/` 178 | ⚠️ 只有类型定义 | 6 | ★★ |
| M-20 | 服务框架 | gosvc | `app/` + `debugx/` | `general_server/` 14.2k —— **Go 化后净删除** | ⚠️ `service.go` 仅 28 行 | 10 | ★★ |

**合计 171 人日**：`gosvc` 73 · `chaosadapter` 98。

**依赖顺序**：
```
M-05 ─┬─► M-06 ★ ─────────────────────┐
M-01 ─┴─► M-02 ─► M-04 ─► M-07 ───────┼─► M-20 ─► 业务迁移
M-09 / M-10 / M-11 / M-15 ────────────┤
M-18 ★ ───────────────────────────────┘（阻塞 16 个载资产服务）
```
关键路径 M-05→M-06→M-04→M-07→M-20；**M-06 与 M-18 是两个硬阻塞点**。

### 2.4 Go 库选型表

原则：**标准库优先 → 已在 go.mod 的库 → 才考虑新依赖**。
唯一例外是 `chaosadapter` 里的兼容性代码：**兼容性优先于复用**，宁可自研。

| 领域 | 需求 | 选型 | 状态 | 说明 |
|---|---|---|:--:|---|
| **日志** | 结构化、分级、低开销 | `log/slog` | 标准库 | Go 1.21+ 内置。**替掉 gf glog**（115 处引用，其中 96 处在生成代码里，改模板即可） |
| 日志轮转 | 按大小/天切分 | `gopkg.in/natefinch/lumberjack.v2` | ✅ 已在 go.mod | 作为 slog 的 io.Writer |
| **配置** | XML + JSON（现有格式）+ 热更 | `encoding/xml`、`encoding/json` | 标准库 | 现有配置就是这两种，不需要 viper |
| **Net** | TCP 长连接、分帧 | `net` + `bufio` | 标准库 | 已在用。不引 gnet/netpoll，除非压测证明标准库是瓶颈 |
| HTTP | 出入向 HTTP | `net/http` | 标准库 | **替掉 gf ghttp**（4 处） |
| **并发** | 分片、扇出、编排 | channel + `sync` + `golang.org/x/sync/errgroup` | 标准库 + ✅ 已在（间接） | 分片池自研，就是 N 个 channel + N 个 goroutine，几十行 |
| 并发原语 | 单例、原子、池 | `sync.Once` / `sync/atomic` / `sync.Pool` | 标准库 | `sync.Pool` 用于 RPCPackage 复用，减 GC |
| **Debug** | 在线 profile | `net/http/pprof` | 标准库 | CPU / heap / goroutine / block / mutex |
| Debug | 运行时指标 | `runtime/metrics` + `expvar` | 标准库 | GC、goroutine 数、内存 |
| Debug | 在线诊断命令 | 自研（复用 M-04 的 RPC 通道） | 自研 | 对应 Lua 的 `m_command_manager` + `m_remote_command_router`(336 行)。GM 在用，不能丢 |
| Debug | goroutine 泄漏检测 | `go.uber.org/goleak` | 新增（仅测试） | 只在 `_test.go` 引入，不进生产二进制 |
| 竞态检测 | | `go test -race` | 工具链 | CI 必过 |
| **追踪** | 分布式追踪 | `go.opentelemetry.io/otel` + `otlptracegrpc` | 新增 | ★ C++ 侧已用 OTLP/gRPC exporter（`chaos_open_telemetry.cpp`），**Go 直接对接同一 collector，不需要自研** |
| **指标** | 业务与系统指标 | 待确认，见下 | ⚠️ | C++ `StatusReporter` 是 DogStatsD 格式，但**整个 `send()` 被 `#ifdef CHAOS_DEBUG_ENABLED` 包住且只 `LOG_TRACE` 一行——release 下是空操作**。等于现在没有指标后端。Go 侧需与运维确认走 Prometheus 还是 StatsD 后再定 |
| **Redis** | 缓存 / 粘性 / 分布式锁 | `github.com/redis/go-redis/v9` | ✅ 已在 | 支持 Lua 脚本（现有 `cache_orm` 依赖） |
| **MySQL** | 持久化 | `database/sql` + `go-sql-driver/mysql` | 标准库 + ✅ 已在 | **不加 ORM**。db_server 若不迁，多数服务只调 DBS RPC，用量很小 |
| **MongoDB** | 持久化 | `go.mongodb.org/mongo-driver` | ✅ 已在 | |
| **etcd** | 服务发现 | `go.etcd.io/etcd/client/v3` | ✅ 已在 | |
| 分布式协调 | leader 选举、分布式单次定时 | `go.etcd.io/etcd/client/v3/concurrency` | ✅ 已在（子包） | 解决 42 个 single_service 多实例后定时任务跑 N 次 |
| **哈希** | MurmurHash（须与 C++ 一致） | **自研** | 自研 | 可参考 `spaolacci/murmur3`，但**必须逐位校验变体/seed/字节序**，兼容性优先 |
| UUID | | `github.com/google/uuid` | 建议新增 | 现有 `satori/go.uuid` 已归档停维护，建议换掉 |
| **时间** | 时区、日切周切 | `time` | 标准库 | 判定逻辑必须与 Lua `TimeService` 完全一致 |
| 序列化 | 内部数据 | `encoding/json` / 自研 codec | 标准库 | **不引 protobuf** —— 线上协议不是 pb |
| **测试** | 单测、基准 | `testing` | 标准库 | 断言不引库；黄金测试用 testdata 固定字节 |
| 静态检查 | | `go vet` + `staticcheck` | 工具链 | CI 门禁 |

**新增依赖只有三个**：`otel`（对接已有 collector）、`goleak`（仅测试）、`google/uuid`（替换归档库）。
**移除一个**：`gogf/gf v1.8.3`。

---

## 三、业务迁移表

### 3.1 Lua 业务服务（41 个，44.4 万行）

L0 天然无状态｜L1 缓存型｜L2 会话型｜L3 重状态/全局调度。
"额外依赖"指全体共用的 M-01～07 / 12 / 13 / 20 之外还需要的模块。

| 服务 | Lua 行数 | 级 | 路由 | 额外依赖 | 人日 | 备注 |
|---|---:|:--:|---|---|---:|---|
| mail_server | 48 | L0 | Single | M-10 | 2 | |
| warband_server | 132 | L0 | Single | M-18 | 3 | 载资产 |
| global_transfer_server | 267 | L0 | — | M-09 | 4 | |
| location_server | 328 | L0 | Single | M-09 | 4 | |
| gchat_server | 675 | L0 | Single | M-09 | 6 | |
| data_monitor_server | 734 | L0 | — | M-11 M-14 | 7 | |
| transaction_server | 736 | L0 | Single | M-10 | 7 | |
| **token_server** | 244 | L0 | **Consist_Hash** | — | 10 | **★ 试点**：纯 DBS 透传，零状态 |
| id_allocation_server | 1,039 | L0 | — | M-19 | 10 | |
| trial_realm_server | 703 | L1 | Single | M-09 M-18 | 8 | 载资产 |
| guild_info_server | 808 | L1 | Consist_Hash | M-09 | 9 | |
| content_server | 1,084 | L1 | Single | M-09 M-18 | 12 | 载资产 |
| citem_repo_server | 1,193 | L1 | Single | M-09 | 13 | |
| war_server | 1,218 | L1 | — | M-09 | 13 | |
| queue_server | 1,353 | L1 | — | M-09 M-16 | 15 | |
| transfer_server | 1,894 | L1 | — | M-09 M-10 | 20 | |
| trans_db_server | 2,637 | L1 | — | M-10 | 28 | |
| api_cache_server | 2,658 | L1 | Random | M-09 M-17 | 28 | |
| resource_server | 2,828 | L1 | ByServiceID | M-09 M-18 | 32 | 载资产 |
| replay_server | 2,580 | L2 | ByServiceID | M-09 M-10 | 30 | 另含 C++ 5.9k |
| chat_server | 2,942 | L2 | Single | M-08 M-09 | 34 | **L2 首选**：状态简单、可容忍短暂不一致 |
| robot_server | 2,953 | L2 | Single | M-08 M-16 | 34 | |
| aoi_server | 4,129 | L2 | ByServiceID | M-08 M-09 | 50 | |
| group_server | 4,246 | L2 | — | M-08 M-09 | 50 | |
| auction_house_server | 4,887 | L2 | Single | M-08 M-09 M-18 | 60 | 载资产 |
| general_service_server | 5,022 | L2 | Single | M-08 M-09 | 58 | |
| subline_server | 5,037 | L2 | — | M-08 M-09 | 58 | |
| store_server | 5,487 | L2 | — | M-08 M-09 M-10 | 64 | |
| session_mgr_server | 5,535 | L2 | — | M-08 M-16 | 70 | 与 GameServer 强耦合，需专项评估 |
| charge_server | 5,963 | L2 | Single | M-08 M-10 M-17 M-18 | 80 | **真金白银，需额外对账**；载资产 |
| login_server | 6,031 | L2 | ByServiceID | M-08 M-17 | 70 | 另含 C++ 2.5k |
| account_server | 6,835 | L2 | Consist_Hash | M-08 M-09 M-10 | 75 | |
| match_server | 7,575 | L2 | Single | M-08 M-16 M-18 | 90 | 载资产；实时性强 |
| room_server | 15,731 | L2 | — | M-08 M-09 M-16 | 180 | 实时性最强，**L2 最后做** |
| world_server | 31,546 | L3 | Single | M-08 M-16 M-18 | 420 | 全局单例调度、全服广播、定时任务 |
| guild_server | 29,696 | L3 | Single | M-08 M-09 M-18 | 390 | 按公会 id 哈希 + 租约；载资产 |
| region_server | 38,440 | L3 | ByServiceID | 全套 | 500 | 与 GameServer 强耦合，**D8 待评估** |
| character_server | 170,422 | L3 | Consist_Hash | 全套 | 2,200 | 玩家全量状态在内存，**必须按子系统拆分分批迁** |
| db_server | 60,921 | L3 | Consist_Hash | M-10 | — | **建议排除范围（D2）** |
| backend_common | 7,462 | 库 | — | — | 49 | Lua 公共库，随 Ⅰ 一起移植 |
| `common/` 后端切片 | ~20,000 | 库 | — | — | 并入 Ⅰ | 协程 / 时间 / RPC / 埋点 / std |

只有生成代码无手写逻辑（跟随主服务）：`lobby_server` `res_control_server` `world_lobby_server`
`demo_server` `bot_server` `gmatch_server` `global_lobby_server` `ai_server` `template_*`。

### 3.2 C++ 专用服务（7 个）

| 服务 | C++ 行数 | 处置 | 人日 | 说明 |
|---|---:|---|---:|---|
| `general_server` | 14,209 | **净删除** | 0 | Lua 宿主，Go 服务自己就是宿主 |
| `gm_server` | 10,711 | 迁移 | 60 | 无强实时要求，适合早期迁 |
| `replay_server` | 5,881 | 迁移 | 并入上表 | |
| `db_server`(C++ 壳) | 4,046 | 跟随 D2 | — | |
| `gateway` | 2,773 | **保留 C++（D4）** | 0 | 本身已是无状态转发 |
| `login_server`(C++ 壳) | 2,469 | 迁移 | 并入上表 | |
| `router_server` | 1,957 | 迁移 | 20 | |
| `log_server` | 1,251 | 迁移 | 12 | 埋点落地端，与 M-11 配套 |

### 3.3 迁移基建 + 单服务 SOP

| 任务 | 人日 | 不做的后果 |
|---|---:|---|
| **T-1 影子流量对拍**：同请求打 Lua/Go 两版，比对「返回值 / DB 写集 / Redis 写集 / 下游 RPC 序列」 | 20 | 44 万行代码只能靠人肉点测 |
| T-2 灰度放量：同 type 下混布，按 hash 分段 1%→10%→50%→100%，一键回滚 | 10 | 无法安全上线 |
| T-3 迁移 SOP 文档 + 服务模板 | 3 | 每人一套做法 |

**SOP 七步**：① 划边界（入向 RPC / 出向依赖 / 数据表 / 定时任务 / 事件）→ ② 状态清单（逐 manager
记内存态与权威来源）→ ③ 生成 stub（IDL 不动）→ ④ **等价翻译，禁止顺手优化** → ⑤ 对拍跑满一个
业务周期（含日切周切活动开关）→ ⑥ 灰度四档 → ⑦ 删 Lua、更新 `server_type.xml` 与部署脚本。

---

## 四、工作量与阶段

| 阶段 | 内容 | 人日 | 里程碑 |
|---|---|---:|---|
| P0 | Ⅰ 基础模块（171）+ T-1～T-3（33） | 204 | M-06 跨语言黄金测试通过 |
| P1 | token_server 试点 | 10 | Go 版灰度 100%，Lua 版下线 |
| P2 | L0+L1 18 个（231）+ C++ gm/router/log（92） | 323 | 21 个服务 Go 化 |
| P3 | L2 15 个 | 1,003 | L2 全部 Go 化 |
| P4 | L3 3 个（character/world/guild，排除 db_server 与 region_server） | 3,010 | **单独立项** |

| 承诺粒度 | 人日 | 折算 |
|---|---:|---|
| **走通全链路**（P0+P1） | **214** | 3 人 ≈ 4 个月 |
| 除 L3 外全部 Go 化（P0～P3） | 1,540 | ≈ 7 人年 |
| 全量（排除 db_server 与 region_server） | 4,550 | ≈ 21 人年 |

误差 ±50%。**建议只先承诺到「走通全链路」。**

---

## 五、五个难点

| # | 难点 | 对策 |
|---|---|---|
| 1 | **纯无状态在 L3 不可行** —— character_server 单玩家内存态几百 KB，逐请求 Redis 往返是数量级退化 | 改为「协议无状态 + 缓存可漂移」：进程内只有带 version+租约的缓存，权威在 Redis/DB，写走 CAS，kill -9 不丢已提交写。**D1** |
| 2 | **一致性哈希跨语言必须逐位一致** —— 算错 = 同一玩家被两实例并发写 | M-06 + 黄金测试进 CI |
| 3 | **44 万行 Lua 全部无锁** —— 依赖 Lua VM 单线程的隐式串行假设 | M-07 按 key 分片。**D5** |
| 4 | **16 个服务依赖 cook 资产** | M-18，方案见 **D3** |
| 5 | **无回归测试**（Go 侧现有 **0 个 `_test.go`**） | T-1 影子对拍 + 质量门禁（见 §6.4） |

**迁移期不变量**（每条都是事故来源）：RPC 二进制格式与 RPCID ｜ etcd key/value 格式 ｜
一致性哈希算法 ｜ Redis 键格式与序列化 ｜ 埋点 JSON 字段 ｜ 时间服务日切判定。

---

## 六、如何推进

### 6.1 先做三个 Spike，不等决策（第 1～2 周）

现在 D1 / D3 / D5 都是**在没有数据的情况下讨论**，会开不出结果。
以下三件事不依赖任何决策，做完决策会才有输入：

| Spike | 做什么 | 人日 | 产出什么决策输入 |
|---|---|---:|---|
| **S-1 哈希对齐** | Go 实现 MurmurHash + 虚拟节点环，与 C++/Lua 三方对拍 | 2 | 兼容性风险到底多大；M-06 的真实工作量 |
| **S-2 端到端打通** | token_server 用现有 Go SDK 硬怼通一条 RPC（不求质量，求"能不能通"） | 3 | 现有 SDK 的坑还有多少；P0 估算是否离谱 |
| **S-3 状态量测** | 抓线上一个真实玩家：内存态实际字节数、单次高频请求读写了哪些字段、字段数占比 | 2 | **D1 的决定性数据** —— 纯无状态到底退化多少 |

**S-3 尤其关键**。"纯无状态不可行"目前是推断，不是实测。如果量测发现单次请求只碰
5% 的字段、且可以按子系统分片加载，纯无状态可能是可行的——那 D1 的结论就要改。
**先量，再吵。**

### 6.2 决策会怎么开（第 3 周）

| 决策 | 需要谁 | 输入 | 产出形式 |
|---|---|---|---|
| D1 无状态定义 | 后端负责人 + 架构 + 运维 | S-3 量测数据 | 写进本文，作为 L2/L3 设计前提 |
| D3 设计表方案 | 引擎组 + 工具链组 + 后端 | M-18 三方案对比 + cook 管线改造成本 | 定方案 + 排期（**跨组，最容易拖，最先启动**） |
| D5 并发模型 | 架构 + 后端 | S-2 结果 | 定 `shard/` 的设计 |
| D2 / D4 / D7 / D8 | 后端负责人 | 本文 | 直接拍 |
| D6 | 后端负责人 | 本文 | 写进 SOP 第 4 步 |

**D3 涉及引擎组和工具链组，不是后端能独立决定的，应该第一个启动沟通。**

### 6.3 组织与节奏

```
平台组 2～3 人   ── P0（gosvc + chaosadapter + 迁移基建）── 约 3 个月 ──┐
                                                                        ├─► 业务组接手
业务组 (n 人)    ────────────────── 等 P0 ──────────────────────────────┘   逐服务并行
```

- 平台组先行，**业务组在 P0 期间不要提前开工**（框架未定型，返工成本高）
- P0 后期让 1 名业务组同学参与 token_server 试点，作为 SOP 的第一个使用者兼验收人
- 之后业务组按服务并行，每人 1～2 个服务，平台组转为支持 + 评审

### 6.4 质量门禁（Go 侧现在 0 个测试文件，必须从第一天立规矩）

| 门禁 | 适用 | 要求 |
|---|---|---|
| 跨语言黄金测试 | `chaosadapter/**` | 每个包必须有；testdata 固定字节；C++/Lua/Go 三方输出全等；**进 CI** |
| `go test -race` | 全部 | 必过 |
| `go vet` + `staticcheck` | 全部 | 必过 |
| 单测覆盖 | `gosvc/**` | 新增代码必须带测试，PR 无测试不合入 |
| 影子对拍差异率 | 每个迁移的服务 | **0** 才允许开始灰度 |
| goleak | 长生命周期组件 | 测试中检查 goroutine 泄漏 |

### 6.5 怎么防止半途而废

这类大重写最常见的死法：**迁了 5 个服务，双栈维护成本上来了，人被抽走，停在半路** ——
留下一个既有 Lua 又有 Go、两边都要改的烂摊子，比不迁更糟。四条对策：

1. **每阶段独立收益**。P0 交付的 `gosvc`/`chaosadapter` 本身可用于写新服务；
   P2 每迁完一个服务就删掉对应 Lua，不允许"迁完不删"。
2. **双栈期设硬上限**。任何单个服务的 Lua/Go 并行不超过 **1 个月**，
   到期要么切完要么回滚，不许长期并存。
3. **明确 kill criteria**（提前写下来，避免事后扯皮）：
   - P0 超期 > 50%（基线 204 人日），或
   - S-1 哈希对齐无法做到三方全等，或
   - token_server 试点的对拍差异修不平
   → **停下来重新评估，而不是硬着头皮往下推**。
4. **范围收敛优先于进度**。宁可少迁几个服务、把迁完的做干净，
   也不要 20 个服务各迁一半。D7（是否追求"全部"）建议在 P2 结束后按实际收益重新回答。

### 6.6 下一步 checklist

- [ ] 拿 Jira 号，两仓库建分支 `feature/CB2N-xxxxx-go-server`
- [ ] **启动 D3 的跨组沟通**（引擎组 + 工具链组），这是排期最长的一项
- [ ] 排 S-1 / S-2 / S-3 三个 spike，2 周内出结论
- [ ] 第 3 周开决策会，拍 D1～D8
- [ ] 组建平台组（2～3 人），P0 立项

---

## 七、待拍板决策

| # | 决策 | 建议 | 不定的后果 |
|---|---|---|---|
| D1 | 「无状态」定义 | 协议无状态 + 缓存可漂移（**待 S-3 数据**） | L2/L3 无法设计 |
| D2 | db_server 是否在范围内 | 不在 | ±650 人日 |
| D3 | 设计表方案（M-18） | C++ DesignDataService 过渡 + cook 导出中间格式长期 | 16 个服务卡死 |
| D4 | gateway 是否重写 | 保留 C++ | — |
| D5 | Go 并发模型（M-07） | 按 key 分片 worker 池 | M-07 无法开工 |
| D6 | 是否允许重构业务逻辑 | 只做等价翻译 | 对拍失去意义 |
| D7 | 是否移除 `gogf/gf v1.8.3` | 移除，换 `log/slog` + `net/http` | 背一个 2019 年的老框架 |
| D8 | region_server 是否值得迁 | 待评估（与 GameServer 强耦合，500 人日） | ±500 人日 |
| **D9** | **指标后端走什么** | 待与运维确认（现有 `StatusReporter` 在 release 下是空操作，等于没有指标） | M-14 无法定型 |
