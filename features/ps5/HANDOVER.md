# PS5 平台接入 — 交接文档

> 最后更新：2026-09-16
> 接手所需信息全部在此，不依赖其他文件。

---

## 1. 状态速览

| 能力 | 状态 | 卡点 |
|---|---|---|
| **登录** | 已合 master | — |
| **存档** | 已合 master | 遗留 TRC R5089（prepare 在主线程）未修 |
| **奖杯** | 完成 | — |
| **支付** | 代码完成，**未实测** | **卡在 DevNet 认证，不卡代码** |

**分支**：两仓同名 `feature/CB2N-30579-ps5-payment`（base 为奖杯分支，其 base 为 master）

---

## 2. 分支与 Title / 商品信息

分支上混有**奖杯**和**支付**两个功能的提交：奖杯已完成 DevKit 验证（见 3.3）；
支付代码完成、卡在 DevNet 认证未实测（见 3.4）。

⚠️ 分支上有一个**未解的手柄问题**和两次未验证的修复尝试，见第 4 节。

### NP Title / 商品

```
NP Title ID:        PPSA38951_00
Content ID:         HP3255-PPSA38951_00-0364252386100017
NpCommunicationId:  NPWR62682_00
测试账号 Online ID:  arty-school / pouty_crony

支付商品（PSVC 虚拟货币）：
  Product Group:  CONQ COIN (ID 10090141)
  Product ID:     HP3255-PPSA38951_00-0683974373790429
  Entitlement:    HP3255-PPSA38951_00-CONQCOIN00000000
  SIE Regions:    SIEA / SIEE / SIEJA-Asia / SIEJA-Japan
  Availability:   2026-09-20（四区 WSP/IRP 已填且已 Submitted）
```

---

## 3. 各能力要点

### 3.1 登录（已合 master）

**两种对话框别混：**

| 对话框 | 用途 | 何时弹 |
|---|---|---|
| **SigninDialog** | PSN 网络登录（输密码 / 已登录秒过） | 真实用户启动 |
| **LoginDialog** | 本机用户选择（列出所有本地账号） | guest 启动 |

**分叉点**：`beginPS5AuthForUser()` 里的 `sceNpHasSignedUp()`。

**认证链路**：

```
sceNpAuthGetAuthorizationCodeV3() → auth_code + issuer_id
  → 客户端经 GAC（Go 服务）换 account_id + token
    → RPC 登录服（platform=ps5）→ 进游戏
```

GAC 端点：`/ps5/getUserInfo`、`/login/auth/token`

### 3.2 存档（已合 master）

- PS5 标准 SaveData（`sceSaveDataMount3`），走 **Mount → Prepare → Write → Commit** 事务
- 挂载点 `/savedata0` 不支持 mkdir，设置文件写根目录

### 3.3 奖杯

**SDK12 没有 unlock 函数**（`NpTrophy2` 是只读 + 回调），解锁走 **UDS 事件**：

```
post UDS 事件 "_UnlockTrophy" { "_trophy_id": N }
  → 系统比对奖杯条件（UDS Management Tool / GEMS）
    → 满足则解锁 → sceNpCheckCallback() 触发回调
```

**三层配置**（改触发事件只需动第 1 层）：

| 层 | 位置 | 作用 |
|---|---|---|
| 1. 设计表 | `_content/design/{client,server}/24_achievement/04_activityachievement_cumulate.design_sheet.gpa` | 决定成就何时完成（`relate_event1` 列） |
| 2. 资产 | `_content/preload/game_preload.game_preload.ast` | DID → `ps5_trophy_id` 映射 |
| 3. PS5 后端 | UDS Management Tool / GEMS | **只认 trophy_id，不知触发原因** |

**本项目改过**：触发事件 `create_character` → 复用 `login`。
改时注意：`condition_num = 0`、`achievement_count_type != condition_achievement`，
且**客户端和服务端两份设计表都要改**。

**平台侧配置流程**（奖杯条件 + UDS 数据，非代码）：

1. 在 **UDS Management Tool**（DevNet 在线工具）配置奖杯条件
   （trophy_id、解锁所需的 Stat）
2. 从 **GEMS**（Package/Disc Management Tool）下载 **`npconfig.zip`**，
   内含 trophy 配置 + UDS 配置文件
3. 解压到应用包的 **`sce_sys/`** 目录（得到 `sce_sys/trophy2/` 与 `sce_sys/uds/`）；
   `nptitle.dat`（NP Title 配置，NPWR62682_00）也放在 `sce_sys/`
4. **DevKit 测试**：系统 ★Debug Settings 里把 UDS Development Mode 设为
   **Local Mode** —— 系统直接读本地安装的配置，不连 PSN 也能验证解锁流程
5. 改了奖杯条件后，重新走 2-3 部署，再用第 5 节的命令清 trophy/uds 数据重测

### 3.4 支付

**架构**（与 Steam 相反）：

```
Steam: 服务端建订单 → 弹窗 → 服务端 finalize
PS5:   客户端 CHECKOUT 弹窗（系统直接扣款）→ entitlement 记在 PSN
         → 客户端通知服务端 → 服务端 S2S 调 consumeEntitlement → 发货
```

**红线**：PSVC（虚拟货币）必须由游戏服务器消耗，一次性全部消耗，
**先 consume 成功再发货**，`transactionId` 幂等。

**代码位置**：

- 客户端 `chaos_ps5_commerce_context.{h,cpp}`
- 服务端 `server/charge_server/charge_manager/chaos_charge_server_charge_manager_ps5.lua`
- RPC `CLT2CHARACTERFinalizePS5RechargeOrder`

**当前卡点：DevNet 认证**

Certification Center 的 **GC-119326 一直 On Hold**，两条原因：

```
1. Awaiting submission of base application.
   （认证依赖主程序先提交；主程序 PPSA-38951 在 Submission Manager 里没有记录）

2. 商品未出现在 Regional / title store preview。
   （In-Game Catalog 里该商品 VALID / STATUS 两列为空）
```

**Communication Tracker 里一条沟通记录都没有** —— On Hold 是**人工放行**流程，
原文要求「解决后通过 Communication Tracker 联系 CertOps」，**不主动联系就永远挂着**。

**已排除的项**（避免重复排查）：四区价格、Metadata、Age Rating、Compatibility Notices、
Product Preview、In-Game Catalog 到 Sp-int、MDT 表单 —— **全部已就绪**。

**注意**：Content Pipeline **列表页的状态列不可信**（显示 `-`，详情页才是真状态），
必须点进 `Manage` 看。

**下一步**：Communication Tracker 开沟通问清解除条件 + 确认主程序是否需提交认证
（若只做 DEV 测试，值得争取豁免）。另：Availability 日期未到之前商品仍不可购买。

---

## 4. 切换用户与手柄问题（未解）

> 这一节全部是**未确认**的内容。现象是真实的，原因和修复方向都没验证通过。

### 现象

1. **guest 启动 → LoginDialog 选用户 → 进游戏后手柄无响应**
   UI 渲染正常、游戏进程活着、系统 UI（PS 键等）可用，只有游戏收不到手柄输入。
2. 运行中从系统菜单切换用户，应用被 suspend；测试中观察到切换用户后
   **无法从 PS5 侧 resume 回游戏**（回主界面再返回则正常）。

### 切换用户时系统做了什么

- LoginDialog 里选另一个用户 = **切换本机用户**，原用户登出
- **guest 登出会被系统直接删除**（从 `prospero-ctrl user list` 里消失）
- 系统只上报 LOGIN / LOGOUT 事件，**无法区分「切换用户」与其他登出原因**

### 相关配置：`param.json` 的 `attribute2`

| 值 | 含义 | 换用户时的行为 |
|---|---|---|
| `0` | 启用 `InitialUserAlwaysLoggedIn` —— 不支持初始用户登录/登出 | 系统 suspend，同用户 resume / 不同用户 **restart** |
| `1` | 禁用 —— 应用自行接管用户管理 | 所有用户登出时 suspend，任何用户可 resume。**需要配套实现，否则用户/输入状态错乱** |

⚠️ `param.json` 是**包属性**，只有**打包安装**后系统才读取，VS 直接跑 ELF 时不生效。
本项目一直用 VS 跑 ELF，所以 `attribute2` 改动的实际效果**从未真正验证过** ——
要验证必须先打包安装。

### 已做的尝试（均未验证通过）

| 提交 | 内容 |
|---|---|
| chaos `339553274fc` | LoginService 认领手柄（`sceLoginServiceRequestDevices`）+ 调 `resetInputSystem()` 重建输入系统 |
| PG `75502b79f2` | `message_box` 快捷键映射补手柄确认键 `x`（原本只注册了键盘 `space`） |

两次改动测试后手柄**仍无响应**。既不能确认方向正确，也不能排除是这两次改动
引入的新问题。

### 建议排查方式

1. 先在**干净 master** 上走同一条路径（guest → LoginDialog 选用户 → 进游戏），
   确认是否同样复现 —— 以此判断问题是本分支引入的，还是本来就存在
2. 排查期间注意 **workspace 里的 Lua 必须与所测引擎版本同批**，
   混用会出现「进游戏无法操作」等伪象，容易误判
3. 用第 5 节的 `user list` 和分层截图先排除「用户被删」「系统 UI 占输入」两种情况
ti
## 5. 诊断命令

```bash
# 用户 / 手柄状态（排查输入问题必用）
prospero-ctrl user list

# 分层截图（判断系统 UI 是否占输入）
prospero-ctrl target screenshot x.png /mode:system   # 系统层
prospero-ctrl target screenshot x.png /mode:game     # 游戏层
#   系统层全黑 = 没有系统 UI 拦截输入

# 挂起 / 恢复（测 resume 逻辑）
prospero-ctrl application suspend <app>
prospero-ctrl application resume <app>

# 清奖杯 / UDS 数据（重测解锁前，需先退出游戏）
prospero-ctrl application delete-data trophy all /user:<User>
prospero-ctrl application delete-data uds all /user:<User>

# workspace
prospero-ctrl workspace list
prospero-ctrl workspace explore ymj-ps5-dev "_scripts/client"
prospero-ctrl workspace push ymj-ps5-dev "<host路径>" "<ws内路径>"
#   Git Bash 里跑要加 MSYS_NO_PATHCONV=1，否则 "/" 被路径转换吃掉
```

---

## 6. 待办

| # | 优先级 | 事项 |
|---|---|---|
| 1 | **高** | 查清切换用户后的手柄无响应问题（见第 4 节） |
| 2 | **高** | 支付：Communication Tracker 联系 CertOps 解除 GC-119326 |
| 3 | **高** | 存档：修 TRC R5089（`sceSaveDataPrepare` 在主线程） |
| 4 | 中 | Client Secret 轮换（GAC 侧） |
| 5 | 中 | 「退出游戏」按钮改合规实现（违反 TRC R5093，认证会被抓） |

### 待办 5 补充说明：「退出游戏」按钮违反 TRC R5093

**R5093 禁止应用自行终止**：

> The application does not perform processing to terminate itself...
> implementations that use a button to terminate the application are prohibited.

本项目「退出游戏」按钮走的是
`notifyShutdown() → ClientRoot::shutdown() → 主循环 break → 进程结束`，
三个调用点：

- `client/ui/widgets/chaos_html_ui_widget_login_base.lua:35`
- `client/ui/widgets/chaos_html_ui_widget_scr_sys_login.lua:120`
- `client/game_level/chaos_client_level_manager.lua:750`

**合规改法**：按钮不终止应用，改为弹提示让用户用系统方式退出（按 PS 键关闭），
且**不要解释具体怎么操作**。

`sceSystemServiceReportAbnormalTermination()` 仅限**不可恢复的致命错误**，
禁止用于可恢复错误（明确点名网络断开），且 CertOps 按崩溃处理。
