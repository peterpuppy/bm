# 后端服务 Golang 无状态重写

**Jira**: CB2N-xxxxx（待分配）｜**阶段**: 方案阶段，未开工

**目标**：`chaos` + `proven_ground` 的全部服务端进程用 Golang 重写，要求无状态。
**不含 GameServer**（`_ServiceType_GAM` / `GAM_LOCAL` 及其专属 C++ 模块 `game_server_common`）。

---

## 文档

| 文档 | 内容 |
|---|---|
| [CURRENT_STATE.md](CURRENT_STATE.md) | **现状**：进程形态、引擎能力面清点、C++/Lua 规模、状态模型、RPC 与服务发现、Go 侧存量、SDK 8 条缺陷 |
| [PLAN.md](PLAN.md) | **方案**：① `gosvc`/`chaosadapter` 两层设计 + 目录布局 + 20 项模块归属表 + Go 库选型表 ② 41 个 Lua 服务 + 7 个 C++ 服务迁移表 ③ 5 难点 ④ 阶段 ⑤ **如何推进**（spike/决策会/组织/门禁/防烂尾）⑥ 9 项决策 |
| [STATUS.md](STATUS.md) | 进度与下一步 |

---

## 任务两块

| 块 | 是什么 | 规模 | 人日 |
|---|---|---|---:|
| **Ⅰ 基础模块** | 分两层：`gosvc`（通用框架：app/log/conf/netx/shard/task/store/obs/debugx，73 人日）+ `chaosadapter`（对接层：codec/rpcrt/registry/routing/sticky/design/idgen/gamelog，98 人日） | 对应 C++ 手写 ≈ 6.6 万行 | **171** |
| **Ⅱ 业务迁移** | 41 个 Lua 业务服务（44.4 万行，4,793）+ 7 个 C++ 专用服务（2.9 万行，92）+ 迁移基建（33） | — | **4,918** |

Ⅰ 不完成，Ⅱ 无法开工。

**Ⅰ 内部的切分规则（本方案最重要的结构决定）**：
**改了会和 Lua/C++ 对不上的，进 `chaosadapter`；其余进 `gosvc`。**
这样把全部跨语言兼容性风险（二进制协议、一致性哈希、etcd value 格式、埋点 JSON、ID 格式）
关进一个包，配黄金测试进 CI；包外就是普通 Go 代码。Lua 侧最终收缩时 adapter 可整体删除。
注意：adapter **不做 interface + 多实现**，它只有一个实现，就是个包边界。

Ⅰ / Ⅱ 判定：Lua 里 `g_*_global_context:get_m_xxx()` 拿到的属 Ⅰ；`XXX:new()` 构造的是
Lua 公共库（随 Ⅰ 一起移植）；`_scripts/server/<服务>/` 下的属 Ⅱ。

---

## 规模速查

| 项 | 数值 |
|---|---|
| Service Type | 51（42 single_service，16 载资产） |
| 待迁移手写 Lua | 444,019 行（排除 db_server 后 383,098） |
| 待迁移 C++ 专用服务 | 29,088 行（另 `general_server` 14,209 行 Go 化后净删除） |
| 后端 C++ 基础设施手写 | 27,942 行（另 54,814 行生成的 etcd proto，Go 用库直接消失） |
| 已生成 Go RPC stub | 48 服务 / 1,032,185 行 |
| **走通全链路**（P0+P1） | **214 人日**（3 人 ≈ 4 个月） |
| **除 L3 外全部 Go 化**（P0～P3） | **1,540 人日 ≈ 7 人年** |
| **全量**（排除 db_server 与 region_server） | **4,550 人日 ≈ 21 人年** |

---

## 三条关键判断

1. **地基已存在** —— `go_dev/src/booming/` 有 Go SDK、`.nsd → Go` 生成器、48 服务 103 万行已生成 stub、
   2 个已上线 Go 服务。etcd/Redis/MySQL/Mongo 客户端都在 go.mod 里。不需要从零造框架。
2. **一致性哈希是最高危单点** —— Go 侧 `ByHash` 是空实现（`net_connection_mgr.go:63` 打 warning 就丢包），
   MurmurHash 缺失。算错 = 同一玩家被两实例并发写。
3. **纯无状态对 L3 大概率不可行** —— character_server 单玩家内存态几百 KB，逐请求 Redis 往返是
   数量级退化。建议改为「协议无状态 + 缓存可漂移」，但**这是推断，需 spike S-3 实测确认**。

## 怎么开始（不等决策）

D1/D3/D5 目前是在没有数据的情况下讨论。先做三个 spike，2 周出结论，再开决策会：
**S-1 哈希对齐**（2 人日，三方对拍）｜**S-2 端到端打通**（3 人日，token_server 硬怼通一条 RPC）｜
**S-3 状态量测**（2 人日，真实玩家内存态字节数与单请求字段占比 → D1 的决定性数据）。
同时立刻启动 **D3 的跨组沟通**（引擎组 + 工具链组），那是排期最长的一项。详见 [PLAN.md §6](PLAN.md)。

---

## 待拍板决策（阻塞开工）

| # | 决策 | 建议 |
|---|---|---|
| D1 | 「无状态」定义 | 协议无状态 + 缓存可漂移 |
| D2 | db_server 是否在范围内 | 不在（60,921 行 Lua，约 ±650 人日） |
| D3 | 设计表方案 | C++ DesignDataService 过渡 + cook 导出中间格式长期 |
| D4 | gateway 是否重写 | 保留 C++ |
| D5 | Go 并发模型 | 按 key 分片 worker 池 |
| D6 | 是否允许重构业务逻辑 | 只做等价翻译 |
| D7 | 是否移除 `gogf/gf v1.8.3` | 移除，换 `log/slog` + `net/http` |
| D8 | region_server 是否值得迁 | 待评估（与 GameServer 强耦合，500 人日） |
| D9 | 指标后端走什么 | 待与运维确认（`StatusReporter` 在 release 下是空操作，等于现在没有指标） |

---

## 分支与常用操作

| 仓库 | 分支 |
|---|---|
| Chaos 引擎 | 待建 `feature/CB2N-xxxxx-go-server` |
| Proven Ground | 待建 `feature/CB2N-xxxxx-go-server` |

Go 代码在 proven_ground 仓库内 `_source/go_dev/src/booming/`；
引擎侧改动预计集中在一致性哈希导出与（可选的）DesignDataService。

```bash
python scripts/switch_feature.py golang-server          # 切本 feature 上下文

cd H:/cb2/dev/wolfgang/_games/proven_ground/_source/go_dev/src/booming && go build ./...

# 查某个引擎能力被谁用了
cd H:/cb2/dev/wolfgang/_games/proven_ground/_source/_scripts
grep -rhoE "g_backend_global_context:[a-zA-Z_]+" --include=*.lua server/ | sort | uniq -c | sort -rn
```
