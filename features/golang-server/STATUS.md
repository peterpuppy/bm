# STATUS —— Golang 无状态重写

**更新**: 2026-09-10｜**阶段**: 方案阶段，未开工

---

## 已完成

- [x] 现状测绘 → [CURRENT_STATE.md](CURRENT_STATE.md)
- [x] Go 侧模块设计 → [PLAN.md §2](PLAN.md)：`gosvc`（通用框架）/ `chaosadapter`（对接层）
      两层切分、目录布局、20 项模块归属表、Go 库选型表
- [x] 业务迁移表 → [PLAN.md §3](PLAN.md)：41 个 Lua 服务 + 7 个 C++ 服务
- [x] 推进方案 → [PLAN.md §6](PLAN.md)：3 个 spike、决策会安排、组织节奏、质量门禁、防半途而废
- [x] 工作量（逐表验算过）：Ⅰ=171｜Ⅱ=4,918｜走通全链路 214｜除 L3 外 1,540｜全量 4,550

---

## 关键发现

| # | 发现 | 影响 |
|---|---|---|
| 1 | Go 地基已存在：SDK + 生成器 + 48 服务 103 万行 stub + 2 个已上线服务；etcd/Redis/MySQL/Mongo 已在 go.mod | 不必从零造框架 |
| 2 | `ByHash` 是空实现（`net_connection_mgr.go:63` 打 warning 就丢包），MurmurHash 缺失 | **最高危单点**，M-06 第一优先 |
| 3 | 后端 C++ 手写仅 2.8 万行（`etcd/proto/` 5.5 万行是生成的），大头是各种驱动 —— Go 里都是现成库 | 基础模块 171 人日 |
| 4 | `general_server` 14,209 行是 Lua 宿主，Go 化后**净删除** | 少一块工作量 |
| 5 | C++ Kafka producer **整段被注释**，埋点真实出口是 `common/log_service/` → JSON → net → log_server | **不要引入 Kafka 客户端** |
| 6 | **tracing 已接 OpenTelemetry OTLP/gRPC**（`chaos_open_telemetry.cpp`） | Go 直接用官方 SDK 对接同一 collector，**不需自研**（推翻上一版判断） |
| 7 | `StatusReporter` 在 release 下是**空操作**（`#ifdef CHAOS_DEBUG_ENABLED` + 只 `LOG_TRACE` 一行） | 等于现在没有指标后端，需与运维确认 → **新增 D9** |
| 8 | `m_world_manager`（97 处）**仅 GameServer 使用** | 排掉一个看似很大的依赖 |
| 9 | `gogf/gf v1.8.3` 被 116 文件引用，96 个是生成代码，只用了 glog/ghttp/gconv/gmap | 改一次生成器模板即可摘干净（D7） |
| 10 | RPC 超时常量单位错：`= 6000` 被当秒用 = 100 分钟 | 现有 Go 服务超时形同虚设 |
| 11 | **Go 侧现有 0 个 `_test.go`**；目录扁平无 `cmd/` `internal/` | 质量门禁与目录重排都要从第一天立规矩 |
| 12 | character_server 单文件 1.4 MB / 1 MB，玩家全量状态在内存 | 纯无状态大概率不可行，但**需 S-3 实测确认**，不能只靠推断 |

---

## 下一步（不等决策，先做 spike）

| 顺序 | 事项 | 人日 | 备注 |
|---|---|---:|---|
| 1 | 拿 Jira 号，两仓库建分支 `feature/CB2N-xxxxx-go-server` | — | |
| 2 | **启动 D3 跨组沟通**（引擎组 + 工具链组，设计表方案） | — | 排期最长，最先启动 |
| 3 | **S-1 哈希对齐** —— Go MurmurHash + 虚拟节点环，C++/Lua/Go 三方对拍 | 2 | 出兼容性风险的真实量级 |
| 4 | **S-2 端到端打通** —— token_server 硬怼通一条 RPC | 3 | 摸现有 SDK 还有多少坑 |
| 5 | **S-3 状态量测** —— 真实玩家内存态字节数 + 单请求读写字段占比 | 2 | **D1 的决定性数据** |
| 6 | 第 3 周决策会，拍 D1～D9 | — | |
| 7 | 组建平台组 2～3 人，P0 立项 | — | |

**S-3 特别说明**："纯无状态不可行"目前是推断而非实测。若量测发现单请求只碰少量字段、
且能按子系统分片加载，D1 的结论要改。**先量，再吵。**

---

## 阻塞

- Jira 编号未分配
- D1 / D3 / D5 未决策（D1 待 S-3 数据；D3 跨组）
- D9（指标后端）需与运维确认

---

## 记录

| 日期 | 事项 |
|---|---|
| 2026-09-10 | 建分区，完成现状测绘 |
| 2026-09-10 | 重组为「基础模块表 + 业务迁移表」，剔除 GameServer 分析，合并 TASKS.md 进 PLAN.md |
| 2026-09-10 | 加入 `gosvc`/`chaosadapter` 两层设计、Go 库选型表、推进方案；修正 tracing 选型（OTel 已在用），新增 D9 |
