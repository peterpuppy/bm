# PS5 平台接入（登录 / 存档 / 奖杯 / 支付 / DLC）

**目标**：在 Chaos 引擎 + Proven Ground 游戏中接入 PS5（Prospero）平台能力。
各功能共用同一套基础设施（`PlatformDelegate` 分阶段初始化、NpAuth、S2S 凭据、
子线程事务），所以放同一个 feature 分区，各自独立记录进度。

---

## 分区结构

```
features/ps5/
├── CLAUDE.md          本文件，feature 上下文
├── README.md          结构导航
├── 备忘.md            账号 / ID / 密钥 / 常用命令（⚠ 含明文机密）
├── nptitle.dat        NP Title 配置，需拷到 _content/PS5/sce_sys/
├── login/             CB2N-27968  已合入 master
├── savedata/          CB2N-29569  已合入 master
├── trophy/            CB2N-30497  DevKit 验证通过，未推送
├── payment/           CB2N-30579  代码就绪，卡 DevNet
├── dlc/               未分配      调研完成，未开工
├── document/          SDK 文档爬虫 + 离线文档（结构不变）
└── shared/            跨功能的 SDK 索引与探测工具
```

每个功能目录下 `STATUS.md` 是进度与下一步，`PLAN.md` 是原始方案（若有）。

---

## 分支

| 仓库 | 分支 |
|---|---|
| Chaos 引擎 | `feature/CB2N-30497-ps5-trophy`（base: master） |
| Chaos 引擎 | `feature/CB2N-30579-ps5-payment`（base: trophy） |
| Proven Ground | 同上两个分支 |

支付基于奖杯，奖杯基于 master。登录与存档已合入 master。

---

## 源码仓库

```
Chaos 引擎:     H:\cb2\dev\chaos
Proven Ground:  H:\cb2\dev\wolfgang\_games\proven_ground
GAC（Go）:      E:\code\game_account_center
```

---

## 各功能当前状态

| 功能 | 状态 | 卡点 |
|---|---|---|
| 登录 | 已合 master | — |
| 存档 | 已合 master | 遗留 TRC R5089（prepare 主线程）待修 |
| 奖杯 | DevKit 验证通过 | 两仓库各一个提交未推送 |
| 支付 | 代码就绪，未实测 | DevNet：WSP 未提交 + Certification On Hold |
| DLC | 调研完成 | 待选 PSAL / PSAC |

---

## 跨功能的共性坑

- **分阶段初始化**：启动期（`initializePS5`，主线程直调）vs 首帧（deferred，
  调度器就绪后可用子线程）。阻塞型 SDK 调用放启动期会崩
- **CMake GLOB**：新增 cpp 必须重新 reconfigure，否则不进工程
- **meta 生成后必须重编对应 dll**：meta 新 dll 旧 → Lua 调用抛错 → 连锁崩溃
  （`chaos_general_server.dll` 踩过）
- **CRLF 红线**：中文注释文件必须 CRLF，LF 会让 MSVC(GBK) 注释吃掉下一行代码（静默）
- **PS5 客户端日志只有 stdout**：spdlog 文件 sink 被 Prospero 条件编译排除，
  用 VS Output / Neighborhood TTY / `prospero-ctrl tty capture` 看，
  格式 `[Level][file][line][module][msg]`
- **Chaos Lua 类严格类型**：加 `self.m_xxx` 前必须在 ctor 声明，否则 `__index/__newindex` 报错
- **LoggerSystem 占位符是 `{0}` 不是 `{}`**：接的是 `Chaos::StringFormat`，
  空 `{}` 会原样打印且参数被吞
- **全局对象名**：C++ 侧成员用 `g_client_global_context:get_m_xxx()`，
  Lua 侧管理器用 `g_lua_client_global_context.m_xxx`。混用会 `attempt to call
  missing method`（支付充值 widget 曾因此 PS5 分支从未跑通）

---

## 安全约束（必读）

- **Client Secret 已泄漏**（曾出现在聊天与代码中），生产前必须轮换。
  现只应存在于 GAC 服务端，禁止写入客户端 / 提交 git / 明文传播
- `连接配置` 与 `服务器地址配置` 两个 xml 含 Client Secret，**永不提交**
- **PS5 SDK 与 DevNet 文档受 NDA 保护**：禁止上传在线服务 / AI 云 / 公开仓库，
  禁止外传截图。`document/output/` 已 gitignore

---

## 常用操作

```bash
# 切到本 feature 上下文
python scripts/switch_feature.py ps5

# 抓取 / 更新 SDK 文档（注意必须传第二参数）
cd features/ps5/document
python scripts/crawl_subtree.py <__document_toc.html URL> output/psn_12

# 清奖杯 + UDS 数据（重测解锁前，需先退出游戏）
prospero-ctrl application delete-data trophy all /user:<User>
prospero-ctrl application delete-data uds all /user:<User>
```

---

## 找东西去哪

| 想知道 | 看 |
|---|---|
| 某功能进度 / 下一步 | `<功能>/STATUS.md` |
| 某功能原始方案 | `<功能>/PLAN.md` |
| 账号 / ID / 密钥 / 环境地址 | `备忘.md` |
| SDK API 细节 | `document/output/psn_12/...` |
| 爬虫怎么用 | `document/README.md` |
| SDK 在线文档索引 | `shared/ps5_sdk_reference_links.md` |
