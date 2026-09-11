# 现状（实测 2026-09-10）

> 仓库 `H:\cb2\dev\chaos` / `H:\cb2\dev\wolfgang\_games\proven_ground`，分支 `feature/CB2N-30579-ps5-payment`
> 只写"现在是什么样"。方案见 [PLAN.md](PLAN.md)。
> **GameServer 不在迁移范围，本文不分析**（其专属 C++ 模块 `game_server_common` 11.2 万行、
> Lua 23.7 万行均不统计在内）。

---

## 1. 进程形态

一个后端服务 = **一个 Chaos C++ 宿主进程 + 内嵌 Lua VM**。C++ 提供基础设施，Lua 写全部业务。

```
进程
├── Lua 业务层    _scripts/server/<svc>/ + _scripts/common/ + _scripts/server/backend_common/
│      ↕ g_*_global_context / lua_accessor
└── C++ 引擎层    engine/source/server/backend/     后端基础设施
                  engine/source/server/general_server/  Lua 宿主
                  engine/source/common/            通用（后端只用切片）
     ↕ TCP(自定义 RPC) / Redis / MySQL·Mongo / etcd
```

宿主 exe 分两类：`general_server`（通用 Lua 宿主，多数服务）与 7 个专用 exe。

---

## 2. 引擎能力面

Lua 里 `g_*_global_context:get_m_xxx()` 拿到的即 C++ 能力。以下为全量清点（grep 统计调用点）。

### 2.1 `g_common_global_context`

| 能力 | 调用点 | C++ 位置 `common/private/chaos/common/` | 行数 | 后端需要 |
|---|---:|---|---:|:---:|
| `m_design_table_manager` | 66 | `design/` | 5,674 | ✅ ★ |
| `m_general_table_accessor` | 23 | `design/` | — | ✅ |
| `m_tick_manager` | 20 | `tick/` | 972 | ✅ |
| `m_os_utility` | 20（Lua 侧 901） | `os/` | 564 | ✅ |
| `m_transcoder` | 18 | `transcoder/` | 1,820 | ✅ |
| `m_command_manager` | 10 | `command/` | — | ✅ GM 命令 |
| `m_res_table_manager` | 4 | `res_table/` | 352 | ✅ |
| `m_net_session_manager` | 3 | `net/` | 11,370 | ✅ ★ |
| `m_lua_accessor` | 3（Lua 侧 **1821**） | 各 server 的 `script/` | — | ✅ ★★ 见下 |
| `m_asset_manager` | 2 | `asset/` | 6,527 | ✅（16 服务） |
| `m_status_reporter` | 1 | `status_reporter/` | 194 | ⚠️ **release 下是空操作**：`send()` 全体被 `#ifdef CHAOS_DEBUG_ENABLED` 包住，且只 `LOG_TRACE` 一行，未真正发出 |
| `m_remote_command_router` | 1 | `remote_command/` | 336 | ✅ |
| `m_words_filtering_manager` | 29 | `words_filtering/` | 150 | 少量（room_server 1 处） |
| `m_lua_runtime_profiler` | 18 | `lua_profile/` | — | ❌ Go 无 Lua |
| `m_world_manager` | 97 | `world/` | 1,771 | ❌ **仅 GameServer 使用**（实测 21 个引用文件全在 game_server） |
| 其余各 1 次 | — | `design/` `script/` `http/` … | — | 部分 |

**`m_lua_accessor` 是最大的口子**：Lua 侧 1821 次调用，是各 server 自己的 C++→Lua 绑定门面
（`general_server/private/.../script/chaos_general_server_lua_accessor.cpp`），
ID 生成、设计表快捷查询、引擎工具函数都塞在里面。Go 化必须**逐方法盘点**。

### 2.2 `g_backend_global_context`

| 能力 | 调用点 | C++ 位置 `server/backend/` | 行数 |
|---|---:|---|---:|
| `m_server_group_id` / `m_terminal_id` / `m_server_group_name` / `m_inner_addr` / `m_server_public_ip` | 165 | `global_context/` | 339 |
| `m_service_discovery_manager` | 55（Lua 侧 154） | `service/` | 3,255 ★ |
| `m_server_publisher` | 50 | `global_context/` | — （只是个渠道名字符串，非 Kafka 连接） |
| `m_open_monitor` / `m_tracing_manager` | 43（Lua 侧 32） | `tracing/` | 843（**已接 OpenTelemetry OTLP/gRPC exporter**，见 `chaos_open_telemetry.cpp`） |
| `m_config_manager` / `m_config_center` | 15 | `config/` | 694 |
| `m_http_req_mgr` | 5 | `common/http/` | 1,413 |
| `m_rpc_router` | 4 | `rpc/` | 3,224 ★ |
| `m_cache_manager` | 3 | `cache/` | 9,890 ★ Redis |
| `m_sigterm_manager` | 2 | `sigterm/` | 69 |
| `m_sticky_service_manager` | 1（Lua 侧 5） | `sticky_session/` | 679 ★ |
| `m_hash_generator` | 1（Lua 侧 4） | `service/` | — ★ |
| `m_kafka_connection_manager` | 1 | `kafka/` | 965（**producer 代码整段被注释，死代码**） |
| `generateSnStr` | 1 | `global_id/` | 130 |
| 无 Lua 直接调用但服务依赖 | — | `mysql_connection/` 3,361、`mongodb/` 259、`etcd/` 56,651、`item_id/` 178、`tick/` 203 | |

### 2.3 C++ 服务端模块规模（不含 GameServer 相关）

| 模块 | 行数 | 文件 | 说明 |
|---|---:|---:|---|
| `server/backend/` | 82,756 | 136 | 其中 `etcd/proto/` **54,814 行是生成的 protobuf** → Go 用库，直接消失；手写仅 **27,942** |
| `server/general_server/` | 14,209 | 50 | Lua 宿主，Go 化后**净删除** |
| `server/gm_server/` | 10,711 | 43 | |
| `server/replay_server/` | 5,881 | 39 | |
| `server/db_server/` | 4,046 | 30 | C++ 壳 |
| `server/gateway/` | 2,773 | 35 | |
| `server/login_server/` | 2,469 | 24 | C++ 壳 |
| `server/router_server/` | 1,957 | 22 | |
| `server/log_server/` | 1,251 | 19 | 埋点落地端 |
| `common/` 后端相关切片 | ≈ 38,000 | — | design 5.7k / asset 6.5k / net 11.4k / sketum 3.3k / data_set 2.2k / transcoder 1.8k / http 1.4k / gpa 1k / tick 1k / rpc 890 / 其余 ≈ 3k（不含 `script/` 23k 的 Lua 绑定层） |

**关键**：backend 手写 2.8 万行里，etcd / MySQL / Mongo / Kafka / Redis 驱动占大头，
在 Go 里都是现成库。真正要重写的 Chaos 自有语义只有 RPC 路由、一致性哈希、
粘性会话、设计表、追踪几块。

---

## 3. Lua 公共库层

`XXX:new()` 构造的是 Lua 对象，属业务侧共享库，Go 化是**移植**不是**绑定**。

| 对象 | 调用点 | 位置 | 行数 |
|---|---:|---|---:|
| `CoroutineManager` | **2,466** | `common/thread/` | 483 |
| `TimeService` | 1,575 | `common/time/` | 939 |
| `LogicLogGenerator` | 919 | `common/logic_log/` | 13,519 |
| `CacheManager`(Lua) + `LuaRedisScriptManager` | 58 | `backend_common/cache_orm/` | ~1,500 |
| `RPCRequestInfoManager` | 41 | `common/rpc/` | 3,232 |
| `HttpService` / `HttpServer` / `ProxyManager` | 21 | `backend_common/http/` | ~800 |
| `Scheduler` / `ServiceDiscovery` / `ScalingManager` / `SigtermHandler` / 其余 | ~50 | `common/utility/`、`backend_common/` | ~1,000 |
| std / type / serializer / event 基础库 | — | `common/std,type,serializer,event/` | 3,758 |

规模：`backend_common/` 7,462 行 + `common/` 后端切片 ≈ 2 万行。
（`common/` 共 110,341 行，但 robot 39,805 / game_scene 17,992 / gp_logic 10,303 /
behavior 6,563 等属 GameServer 与客户端，不在范围内。）

---

## 4. 服务清单

`_server_configs/booming_linux/server_type.xml` 定义 51 个 Service Type，
其中 42 个 `is_single_service=true`、16 个 `is_load_global_asset=true`。

**待迁移的 41 个 Lua 业务服务规模见 [PLAN.md §3.1](PLAN.md)**（含等级、路由、依赖模块、工作量）。

合计手写 Lua **444,019 行**；排除 db_server 后 **383,098 行**。
最大的四个：character_server 170,422 / db_server 60,921 / region_server 38,440 / world_server 31,546。

### 路由规则映射（`backend_common/chaos_backend_rpc.lua:11-25`）

| 规则 | 服务 |
|---|---|
| Consist_Hash | CHARACTER、DBS、TOKEN、GLD_INFO、CHARACTER_CACHE |
| ByServiceID | RGN、RESOURCE、CLT、LGN、RPL |
| Random | RDBS、CRI、ACS |
| Single | 其余多数 |

---

## 5. 状态模型（现状不是无状态）

现架构 = **粘性有状态 + 优雅缩容**：

1. **粘性** —— `chaos_sticky_session.cpp`(679) + Redis 记录 entity→实例归属；一致性哈希把同一玩家恒定路由到同一实例
2. **内存权威** —— character_server 把玩家全量数据加载进内存对象图
   （`chaos_character_data_manager.lua` 1.4 MB、`chaos_character_inventory_manager.lua` 1 MB），定期/下线回写
3. **优雅缩容** —— `chaos_scaling_manager.lua`：实例进 Stopping 后等本地 entity 清空 → 置 Stopped
4. **单线程** —— Lua VM 单线程 + 协程 yield，**全部业务代码无锁**

结论：**扩缩容能力已有**，缺的是"实例 kill -9 不丢数据"。

---

## 6. RPC / 服务发现 / 数据

**IDL**：XML `.nsd`，49 个，`_schemas/_rpc/_rpc/`。`ks:RPCCoroutineDef` 定义 param/return_value，
分 Public/Private 接口。最大三个：`rpc_common_struct.nsd` 566 KB、`client_rpc.nsd` 523 KB、
`character_server_rpc.nsd` 332 KB。

**协议**：自定义二进制 `RPCPackage`（非 protobuf）。

**服务发现**：etcd。key `<prefix>/ServiceRegistry/<type>At<id>`，
value `<type>@0@<id>@<addr>@<rule>@1`，lease TTL 16s + keepalive。

**一致性哈希**（`chaos_backend_service_discovery_manager.cpp:1575-1598, 1848-1853`）：
```
虚拟节点  node_name = "{i}#{service_type}#{service_id}#{i}"，i ∈ [0, k_consist_hash_virtual_node_count)
          ring[MurmurHash(node_name)] = service_id
路由      service_id = ring.lookup(MurmurHash(decimal_string(user_data)))
```

**埋点日志出口**：Lua `LogicLogGenerator` → `LuaGameLogService.logJsonValue` →
C++ `common/log_service/`(412 行) → rapidjson 拼 JSON → `net_session_manager->sendData` → **log_server**。
**不是 Kafka**（C++ Kafka producer 已整段注释）。

| 中间件 | 用途 | 接入位置 |
|---|---|---|
| MySQL | 主要持久化 | `backend/mysql_connection/` 3.4k、`db_server/db_orm/` |
| MongoDB | 部分持久化 | `backend/mongodb/` 259 |
| Redis | 缓存 / 粘性 / 分布式 ID | `backend/cache/` 9.9k、`backend_common/cache_orm/`（map/set/zset/list/table/query 已齐全） |
| etcd | 服务发现 | `backend/etcd/` 1.8k 手写 + 54.8k 生成 proto |

---

## 7. Go 侧存量资产

```
proven_ground/_source/go_dev/src/booming/          go.mod: go 1.26
├── chaos_sdk/           Go 服务框架
│   ├── service.go(28行) server.go  handler.go  rpc_manager.go
│   ├── net_connection.go / net_connection_mgr.go / net_data_package.go / net_package_mgr.go
│   ├── service_discover.go / _v2 / _v3      timer.go  concurrent.go
│   ├── common/hash_generator.go             rpc_base/  (RPCPackage + DID/GUID/Vector3/ItemID…)
├── rpc/<SVC>/{private,public}/rpc_struct.go  ★ 48 服务 / 1,032,185 行，已生成
├── rpc_code_generator/  生成器（Go 写的）+ Go/Lua 模板
├── auth_server/         已上线（OAuth / AWS Cognito）
├── charge_status_server/ 已上线
└── db_model_generator/ dynamic_config/ dynamicDB_sync/ stream_persistor_server/ csd_code_generator/
```

生成的 stub 是**完整双向 stub**：每个 RPC 带 `Invoke()` / `Deserialize()` /
`SerializeReturnValues()` + `ByHash()` `ByServiceID()` `ByRandom()` `BySesstionID()` `ByBroadcast()`。
最后改动 2026-08-19（`CB2N-29558: 接入新生成器（v1 模式）`），活跃维护中。

**依赖现状**：`etcd/client/v3`、`redis/go-redis/v9`、`go-sql-driver/mysql`、`mongo-driver`
均已在 go.mod；`gogf/gf v1.8.3`（2019 年老框架）被 116 个文件引用，其中 **96 个是生成代码**，
只用了 glog/ghttp/gconv/gmap 四个包。

---

## 8. Go SDK 已知缺陷

| # | 缺陷 | 位置 | 影响 |
|---|---|---|---|
| 1 | **`ByHash` 空实现** —— 打一行 warning 后丢包 | `net_connection_mgr.go:63` | Go 无法参与一致性哈希路由；CHARACTER/DBS/TOKEN/GLD_INFO/CHARACTER_CACHE 全走这条路 |
| 2 | **哈希函数全是桩** —— `GetStringHash`/`BKDRHash`/`FNVHash` 等 `return 0`，无 MurmurHash | `common/hash_generator.go` | 同上 |
| 3 | **RPC 超时单位错** —— `k_default_yield_timeout_miliseconds = 6000` 用作 `time.Second * 6000` = 100 分钟 | `rpc_manager.go:19,109` | 超时形同虚设 |
| 4 | **7 个函数体为空** —— 错误回包、成功回包、事件订阅/发布/取消 | `rpc_manager.go` | 收不到错误码，不能参与事件 pub/sub（Lua 侧大量使用） |
| 5 | **全局单队列分发** —— 单 goroutine 顺序处理全部 RPC | `handler.go` | 吃不满多核 |
| 6 | **双反射分发** —— `runtime.FuncForPC` 解析函数名 + `reflect.MethodByName` | `rpc_manager.go:60-77,242` | 高频路径开销；对闭包/内联脆弱 |
| 7 | 无优雅退出、无健康检查、无 panic recover | `service.go` | 生产不可用 |
| 8 | 两套并存的连接实现 | `chaos_sdk/` 与 `auth_server/library/communicate/` | 重复代码，语义可能已分叉 |
