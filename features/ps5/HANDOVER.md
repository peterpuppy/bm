# PS5 平台接入 — 交接文档（自包含）

> 最后更新：2026-09-16
> 本文档**不依赖任何其他文件**，接手所需信息全部在此。

---

## 目录

1. 三十秒速览
2. 代码现状（接手第一件事）
3. 环境与仓库
4. 各能力详解
5. 必须知道的坑（11 条）
6. 诊断命令速查
7. 后台地址与 SDK 文档
8. 待办清单
9. 安全与合规
10. 附录：关键 API 与代码位置

---

## 1. 三十秒速览

| 能力 | 状态 | 卡点 |
|---|---|---|
| **登录** | 已合 master | — |
| **存档** | 已合 master | 遗留 TRC R5089（prepare 在主线程）未修 |
| **奖杯** | 完成 | — |
| **支付** | 代码完成，**未实测** | **卡在 DevNet 认证，不卡代码** |
| **DLC** | 未开工 | 待选 PSAL / PSAC |

**分支**：两仓同名 `feature/CB2N-30579-ps5-payment`（base 为奖杯分支，其 base 为 master）

---

## 2. 代码现状（接手第一件事）

### Chaos 引擎 `H:\cb2\dev\chaos`

分支 `feature/CB2N-30579-ps5-payment`（已 rebase 到 origin/master）：

```
96c45503524  CB2N-30579:支付功能
0fa3977bff6  优化奖杯代码
edebdbc7dda  CB2N-30497: PS5奖杯功能
```

**⚠️ 有未提交改动（暂存区，+76 行，未验证）：**

| 文件 | 改动 |
|---|---|
| `_source/_engine/source/client/CMakeLists.txt` | +1 行：链接 `libSceLoginService_stub_weak.a` |
| `.../client/private/chaos/client/platform/chaos_platform_delegate.cpp` | +70 行 |
| `.../client/public/chaos/client/platform/chaos_platform_delegate.h` | +5 行 |

改动内容（用 `git diff --cached` 看全文）：

1. `initializePS5()` 加载 `SCE_SYSMODULE_LOGIN_SERVICE` PRX + `sceLoginServiceInitialize()`
   （失败只报错，不阻断启动）
2. 新增 `PlatformDelegate::claimPS5PadForUser()`：用 `sceLoginServiceRequestDevices()`
   把手柄认领给当前用户
3. `updatePS5LoginDialog()`：
   - 取消分支 → 只认领
   - **选定用户分支 → 认领 + `resetInputSystem()`**（重建 OIS 输入系统）
4. `finalizePS5()` 清理：`sceLoginServiceTerminate()` + 卸载 PRX

**未验证**：最后一轮编译测试没跑完。审查后 `git commit`，或 `git reset` 丢弃。

**可删的调试分支**：`debug/ps5-pad-baseline`（排查时留的基线快照）

### Proven Ground `H:\cb2\dev\wolfgang\_games\proven_ground`

分支 `feature/CB2N-30579-ps5-payment`（已 rebase）：

```
75502b79f2  CB2N-27968: message_box 快捷键映射补手柄确认键 x
2397af8bb5  CB2N-30579:支付功能
37c7ba824e  CB2N-30497: 奖杯解锁事件复用 login
```

**工作区干净。**

---

## 3. 环境与仓库

| 项 | 路径 / 值 |
|---|---|
| Chaos 引擎源码 | `H:\cb2\dev\chaos` |
| Proven Ground 游戏源码 | `H:\cb2\dev\wolfgang\_games\proven_ground` |
| GAC（Go 账号中心） | `E:\code\game_account_center` |
| 本工作台仓库 | `E:\code\mutli_level` |
| Chaos 构建目录 | `H:\cb2\dev\chaos\build-ps5` |
| 游戏 ELF 产物 | `H:\cb2\dev\chaos\_install\ps5\bin\Engine_Check\client\xenon_client.elf` |
| DevKit workspace | `ymj-ps5-dev`（VS 调试时 `/app0` 指向它） |
| PS5 SDK | `C:\SCE\Prospero SDKs\12.000\` |
| 主机工具日志 | `C:\Users\mengjie.yuan\AppData\Local\SCE\PROSPERO\TMUI\Log` |

### NP Title / 商品信息

```
NP Title ID:        PPSA38951_00
Content ID:         HP3255-PPSA38951_00-0364252386100017
NpCommunicationId:  NPWR62682_00
PSN Online ID:      arty-school / pouty_crony（测试账号）

支付商品（PSVC 虚拟货币）：
  Product Group:   CONQ COIN  (Product Group ID 10090141)
  Product ID:      HP3255-PPSA38951_00-0683974373790429
  Entitlement:     HP3255-PPSA38951_00-CONQCOIN00000000
  Classification:  Virtual Currency / Consumable Limit: 1 Usage
  SIE Regions:     SIEA / SIEE / SIEJA-Asia / SIEJA-Japan
  Availability:    2026-09-20（四区 WSP/IRP 已填且已 Submitted）
```

### 环境映射（PSN 后端）

| 环境 | Issuer ID | Token Endpoint |
|---|---|---|
| sp-int（研发） | 1 | `https://auth.api.sp-int.s2s.playstation.com/oauth/token` |
| prod-qa（认证） | 8 | `https://auth.api.prod-qa.s2s.playstation.com/oauth/token` |
| np（生产） | 256 | `https://auth.api.np.s2s.playstation.com/oauth/token` |

UserInfo 端点同理，把 `oauth/token` 换成 `userinfo`。

---

## 4. 各能力详解

### 4.1 登录（CB2N-27968，已合 master）

**两种对话框，别混：**

| 对话框 | 用途 | 何时弹 |
|---|---|---|
| **SigninDialog** | PSN 网络登录（输密码 / 已登录秒过） | 真实用户启动 |
| **LoginDialog** | 本机用户选择（列出所有本地账号） | guest 启动 |

**入口**：`PlatformDelegate::startPS5Login()` → `beginPS5AuthForUser()`，
用 `sceNpHasSignedUp()` 判定走哪条分支。

**认证链路**：

```
sceNpAuthGetAuthorizationCodeV3() → auth_code + issuer_id
  → 客户端经 GAC（Go 服务）换 account_id + token
    → RPC 登录服（platform=ps5）→ 进游戏
```

**GAC 端点**：`/ps5/getUserInfo`（客户端换 token）、`/login/auth/token`（登录服校验）

Client Secret 现已从游戏侧移除，只存在于 GAC 服务端，但**已泄漏过，生产前必须轮换**。

### 4.2 存档（CB2N-29569，已合 master）

- 用 PS5 标准 SaveData（`sceSaveDataMount3`）存设置项，走 **Mount → Prepare → Write → Commit** 事务
- 挂载点 `/savedata0` **不支持 mkdir**，设置文件直接写挂载点根目录
- **遗留缺陷**：`sceSaveDataPrepare()` 在主线程调用，**违反 TRC R5089**，送认证前必须修

**R5089 要求**：以下 API 不能与 `suspendPoint()` 在同一线程调用 ——
`sceSaveDataPrepare` / `sceSaveDataDelete` / `sceSaveDataDirNameSearch` /
`sceSaveDataSetupSaveDataMemory2` / `sceSaveDataGetSaveDataMemory2` / `sceSaveDataSetSaveDataMemory2`

### 4.3 奖杯（CB2N-30497）

**核心认知**：SDK12 **没有 unlock 函数**（`NpTrophy2` 库是只读 + 回调），解锁走 **UDS 事件**：

```
post UDS 事件 "_UnlockTrophy" { "_trophy_id": N }
  → 系统更新 UDS Stat
    → 系统比对奖杯条件（UDS Management Tool / GEMS 配置）
      → 满足则解锁 → sceNpCheckCallback() 触发 unlock 回调
```

**三层配置**（改触发事件只需动第 1 层）：

| 层 | 位置 | 作用 |
|---|---|---|
| 1. 设计表 | `_content/design/{client,server}/24_achievement/04_activityachievement_cumulate.design_sheet.gpa` | 决定成就何时完成（`relate_event1` 列） |
| 2. 资产 | `_content/preload/game_preload.game_preload.ast` | DID → `ps5_trophy_id` 映射 |
| 3. PS5 后端 | UDS Management Tool / GEMS | **只认 trophy_id，不知道触发原因** |

**改触发事件时**（本项目做过：`create_character` → 复用 `login`）：

- 改第 1 层的 `relate_event1`；同时确保 `condition_num = 0`、
  `achievement_count_type != condition_achievement`（否则代码会跳过事件分支）
- 第 2、3 层**不用动**（DID 未变）
- **客户端和服务端两份设计表都要改**

**用户切换**：`PS5TrophyContext::initializeForUser()` 在用户变化时拆旧 context 重建。

### 4.4 支付（CB2N-30579）— 最需要接手人推的

**架构**（与 Steam 相反）：

```
Steam: 服务端建订单 → 弹窗 → 服务端 finalize
PS5:   客户端 CHECKOUT 弹窗（系统直接扣款）→ entitlement 记在 PSN
         → 客户端通知服务端 → 服务端 S2S 调 consumeEntitlement → 发货
```

**红线**：PSVC（虚拟货币）**必须由游戏服务器消耗**，一次性全部消耗，
**先 consume 成功再发货**，`transactionId` 幂等（重试复用同一 ID）。

**代码位置**：

- 客户端：`chaos_ps5_commerce_context.{h,cpp}`（CHECKOUT 弹窗状态机）
- 服务端：`_source/_scripts/server/charge_server/charge_manager/chaos_charge_server_charge_manager_ps5.lua`
- RPC：`CLT2CHARACTERFinalizePS5RechargeOrder` → `CHARGE.FinalizePS5RechargeOrder`

**当前卡点：DevNet 认证（不是代码）**

Certification Center 的 **GC-119326 一直 On Hold**，两条原因：

```
1. Awaiting submission of base application.
   （DLC 认证依赖主程序先提交；主程序 CONQ / PPSA-38951 在 Submission Manager 里没有记录）

2. This DLC is not appearing on the Regional or title store preview.
   （In-Game Catalog 里该商品的 VALID / STATUS 两列为空）
```

**⚠️ Communication Tracker 里一条沟通记录都没有** —— On Hold 是**人工放行**流程，
原文要求「解决后通过 Communication Tracker 联系 CertOps」，**不主动联系就永远挂着**。

**已确认不是问题的项**（避免重复排查）：

- 四区价格全部 `Submitted`，WSP/IRP 齐全，Availability = 2026-09-20
- Metadata / Age Rating / Compatibility Notices 全部 `Complete`
- Product Preview 已 `Published`；In-Game Catalog 已发到 Sp-int（`INGESTED`）
- MDT 表单状态 `FINAL`
- `DLC` 提交类型是**正确的**（PSVC/PSCONS 这类内购商品在 SIE 认证体系里统一走 DLC 类型）

**教训**：Content Pipeline **列表页的状态列不可信**（显示 `-` 但详情页是 `Submitted`），
必须点进 `Manage` 看详情页。

**建议下一步**：

1. 去 Certification Center 的 Communication Tracker 开一条沟通，问清 On Hold 的解除条件
2. 确认主程序 `PPSA-38951` 是否需要提交认证（若目标只是 DEV 测试，值得争取豁免）
3. 邮件里的 `{0}` 模板变量未渲染，一并问 SIE

**注意**：即使上述全部解决，**Availability 日期（2026-09-20）未到之前商品仍不可购买**。

### 4.5 DLC（未开工）

两条路待选：

| 方案 | 说明 |
|---|---|
| **PSAL**（不带数据） | 内容在主包，只卖权利钥匙。客户端加一次权利查询 + 放行判断。不依赖 AppContent 库 |
| **PSAC**（带数据） | 单独打包上传 GEMS，玩家下载安装。要 AppContent 库挂载 + 资源路径 + 重下载引导。AppContent 文档未爬，需补 |

**已确认的事实**：

- 权利判定用 `NpEntitlementAccess`，**禁止缓存权利状态**（TRC R5116），每次用前必须查
- 权利运行时会变，监听 `SCE_SYSTEM_SERVICE_EVENT_ENTITLEMENT_UPDATE`
- DLC 必须挂 **PSSDC** 服务（挂 Commerce Catalog 会导致游戏内挂载不了）
- PSAC / PSAL 的 label 在 **GEMS** 建，PSVC 在 Content Pipeline 建

---

## 5. 必须知道的坑（11 条）

### ① CRLF 红线

**中文注释文件必须 CRLF。** LF 会让 MSVC(GBK) 把下一行代码当注释吃掉 —— **静默，不报错。**

### ② meta 生成物与 dll 必须同批

**症状**：更新代码后启动崩在 `TypedHandle<T>::TypedHandle` / `DatumTable` / `TransparentPtr`，
地址形如读取 `0x240`。

**原因**：`git checkout` 换了源码 → meta 生成头（含 type ID 表）重新生成 →
但**部分 .o 没重编**，旧 .o 带着旧 type ID 链进同一个 ELF。

**修法（不用全量删 build）**：

```bash
cd H:\cb2\dev\chaos\build-ps5
find . -type d -name "generated_src" -exec rm -rf {} +
# 若仍崩，再清早于生成头重生成时间的 .o/.a
find p -path "*generated_src*" -type f -printf '%TY-%Tm-%Td %TH:%TM:%TS\n' | sort | tail -1   # 看阈值
find Engine ProjectXenon ProjectXenon_precompile \( -name "*.o" -o -name "*.a" \) ! -newermt "<阈值>" -delete
```

### ③ `_content/` 被 gitignore，checkout 不回退它

**症状**：切换代码版本后启动 **SIGSEGV**，崩在 `TypedHandle<...>`。

**原因**：`_content/` 不在版本控制里（`.gitignore` 忽略整个目录）。切到旧代码时，
资产若带了新字段而引擎不认识 → preload 解析中断 → 资产句柄无效 → 解引用崩。

**修法**：在 `_schemas/` 里补对应字段声明（例如
`_schemas/_rsa/common/_assets/preload.rsd` 加
`<ks:element name="ps5_trophy_id" type="Int" default="-1"/>`），或回退资产里的字段。

### ④ workspace 与代码版本必须匹配

DevKit workspace（`ymj-ps5-dev`）里的 Lua 与引擎版本**必须同批**。混合会出现
「进游戏后无法操作任何内容」等伪象 —— 因为 Lua 调用了引擎不存在的接口。

**换基线测试时，必须同步换 workspace 里的 Lua。**

另：workspace 名必须是 **`workspace0`~`workspace7`** 才会出现 ★Workspace 图标。
当前名 `ymj-ps5-dev` 不合规，只能靠 VS 部署启动。

### ⑤ `param.json` 是包属性，VS 跑 ELF 不生效

`param.json` 必须在**打包安装**后才被系统读取。VS 直接跑 ELF 时不会应用它。

**`attribute2` 语义**（`InitialUserAlwaysLoggedIn` 位）：

| 值 | 含义 | 换用户时的行为 |
|---|---|---|
| `0` | 启用 —— 不支持初始用户登录/登出 | 系统 suspend 应用，**同用户 resume / 不同用户 restart** |
| `1` | 禁用 —— 应用自行接管用户管理 | 所有用户登出时 suspend，任何用户可 resume。**需要配套实现，否则用户/输入状态会错乱** |

### ⑥ LoginDialog 的两个专属陷阱（**登录功能时代就存在**）

**(a) 提示框没绑手柄确认键 → 按任何键都没反应**

`_source/_scripts/client/input/chaos_input_system_ui_callbacks.lua`：

```lua
insert_ui_shortcut_map(STRING_ID("html_scr_message_box_ui"), STRING_ID("space"));  -- 只有键盘 space
```

手柄确认键在这个系统里叫 **`"x"`** —— message_box 从未注册它，所以手柄按 X 无响应。
**已在 PG 侧修复**（提交 `75502b79f2`）。

**同类隐患未修**：`reward_box`、`slot_box`、`battle_pass_purchase_exp` 等也只注册了
`space`，建议批量排查。

**(b) 经 LoginDialog 选用户后手柄失效**

选用户 = **切换本机用户**：原用户登出（**guest 会被系统直接删除**）→ 输入层（OIS）
的 pad handle 绑在已删除的用户上 → **输入永久死亡**。

**修法**（见第 2 节未提交改动）：

1. 用 LoginService **认领手柄**给新用户（`sceLoginServiceRequestDevices`）
2. **重建输入系统**：`g_client_global_context.m_input_device_manager->resetInputSystem()`
   —— 该函数一直存在但全引擎无人调用，正是为这种场景准备的

**为什么当年没发现**：登录功能验收走的是**真实用户 happy path**
（SigninDialog 秒过 → 进游戏），本机用户从未切换过，pad handle 从启动活到退出。
guest → LoginDialog 选用户这条路径**从未被手柄验证过**。

### ⑦ PS5 客户端日志只有 stdout

spdlog 的文件 sink 被 Prospero 条件编译排除。

**看日志的方式**：VS Output 窗口 / Target Manager → Console Output / `prospero-ctrl tty capture`
**格式**：`[Level][file][line][module][msg]`

**调试时不要 grep 函数名**：日志里的「函数名」字段是**打日志那行所在的函数**，不是调用者。
比如搜 `startPS5Login` 会漏掉 `updatePS5LoginDialog` 里打的日志 ——
**搜 `PS5` 这种通用前缀更安全。**

### ⑧ meta 改了要重编对应 dll

meta 新、dll 旧 → Lua 调用抛错 → 连锁崩溃（`chaos_general_server.dll` 踩过）。

### ⑨ 全局对象名别混

- C++ 成员：`g_client_global_context:get_m_xxx()`
- Lua 管理器：`g_lua_client_global_context.m_xxx`

混用报 `attempt to call missing method`。

### ⑩ Chaos Lua 类严格类型

加 `self.m_xxx` 前**必须在 ctor 里声明**，否则 `__index/__newindex` 报错。

### ⑪ Logger 占位符是 `{0}` 不是 `{}`

接的是 `Chaos::StringFormat`。空 `{}` 会原样打印且参数被吞。

---

## 6. 诊断命令速查

```bash
# ---- 用户 / 手柄状态（排查输入问题必用）----
prospero-ctrl user list
#   看 Status(LOGGED_IN/NOT_LOGGED_IN)、PSN Status、用户 Id
#   guest 登出会被系统删除，从列表消失

# ---- 分层截图（判断系统 UI 是否占输入）----
prospero-ctrl target screenshot x.png /mode:system   # 系统层
prospero-ctrl target screenshot x.png /mode:game     # 游戏层
prospero-ctrl target screenshot x.png /mode:auto     # 实际显示
#   系统层全黑 = 没有系统 UI 拦截输入

# ---- workspace ----
prospero-ctrl workspace list
prospero-ctrl workspace info ymj-ps5-dev
prospero-ctrl workspace explore ymj-ps5-dev "_scripts/client"
prospero-ctrl workspace files ymj-ps5-dev /filter:<关键词>
prospero-ctrl workspace pull ymj-ps5-dev "<ws内路径>" "<host路径>"
prospero-ctrl workspace push ymj-ps5-dev "<host路径>" "<ws内路径>"
#   ⚠️ 在 Git Bash 里跑要加 MSYS_NO_PATHCONV=1 前缀，否则 "/" 会被路径转换吃掉

# ---- 挂起 / 恢复（测 resume 逻辑）----
prospero-ctrl application suspend <app>
prospero-ctrl application resume <app>

# ---- 清奖杯/UDS 数据（重测解锁前，需先退出游戏）----
prospero-ctrl application delete-data trophy all /user:<User>
prospero-ctrl application delete-data uds all /user:<User>
#   用户名到 PS5 用户简介处查看

# ---- 电源 ----
prospero-ctrl power rest-mode    # 系统挂起
prospero-ctrl power on           # 系统恢复
```

**排查「手柄无响应」的推荐顺序**：

```
1. prospero-ctrl user list            → 用户状态是否正常？guest 是否被删？
2. target screenshot /mode:system     → 系统层是否拦截输入？
3. VS Output 搜 "PS5"                 → 代码走到哪一步了？
4. 卡在网页弹窗                       → 查 chaos_input_system_ui_callbacks.lua 的快捷键映射
5. 卡在进游戏后                       → 查 OIS pad handle 是否孤儿化（用户切换场景）
```

---

## 7. 后台地址与 SDK 文档

### 后台工具

| 工具 | 地址 |
|---|---|
| DevNet 门户 | `https://game.develop.playstation.net/` |
| Titles and products | `https://game.develop.playstation.net/titles` |
| **Content Pipeline** | `https://publish.playstation.net/concepts/10020266`（**注意不在 DevNet 域下**） |
| CONQ COIN Product Group | `https://publish.playstation.net/concepts/10020266/products/10090141` |
| In-Game Catalog | `https://publish.playstation.net/concepts/10020266/ingamestructures/10008112` |
| **Certification Center** | `https://certify.playstation.net/fqaweb/index.cfm` |
| Submission Manager | `https://certify.playstation.net/fqaweb/index.cfm?event=submission_manager.main` |
| 认证文档（可访问） | `https://learn.playstation.net/category/certify` |
| Add-On MDT 指南 | `https://learn.playstation.net/bundle/certops-guide/page/mdt_add-on.html` |

### SDK 文档（本地已爬取）

```bash
cd E:\code\mutli_level\features\ps5\document
python scripts/start_chrome_debug.py          # 启动 Chrome 调试端口 9222
python scripts/save_storage.py                # 保存登录态（登录过期时重跑）
python scripts/crawl_subtree.py <TOC_URL> output/psn_12   # ⚠️ 第二参数必传
```

已爬内容在 `document/output/psn_12/`，关键路径：

```
System/User_Management/          ← UserService / LoginDialog / LoginService
System/System_Service/           ← SystemService（ON_RESUME 等事件）
System/Kernel/Kernel-Overview/   ← 进程终止（TRC R5093 的另一处表述）
Getting_Started/Programming_Basics/Programming-Startup_Guide/   ← 应用状态/挂起恢复
Getting_Started/Development_Environment/Target_Manager_CLI-Users_Guide/  ← prospero-ctrl 命令全集
PlayStationNetwork/PlayStationStore/   ← NpCommerceDialog / In-Game Catalog
TRC/2026.07/TRC/                 ← TRC 条文（R5093 / R5089 等）
```

### ⚠️ 尚未爬取的重要文档

- **`CommonDialog-*`** 未爬
- **`AppContent-*`**（DLC 需要）未爬
- **Content Pipeline 在线帮助** `https://learn.playstation.net/bundle/content-pipeline` ——
  **不在 SDK 文档树里，爬虫取不到**，PAR / entitlement 的填写步骤只能看界面提示或问 SIE

### 账号

```
PSN 开发者账号:    mengjie.yuan@boomingtech.com
DevNet / PSN 网站: 同账号
GAC 域名:          accounts-cbx.boomingtech.com
GAC 日志面板:      https://g-ofc.booming-inc.com/
                   (project: cb-frontier, app: game-account-center-cbx)
```

完整密钥与环境地址见 `E:\code\mutli_level\features\ps5\备忘.md`（含明文机密）。

---

## 8. 待办清单

| # | 优先级 | 事项 | 位置 |
|---|---|---|---|
| 1 | **高** | 审查并验证未提交的 LoginService / 输入重建改动 | chaos 暂存区（见第 2 节） |
| 2 | **高** | **支付：联系 CertOps 解除 GC-119326** + 确认主程序认证状态 | 见 4.4 节 |
| 3 | **高** | 存档：修 TRC R5089（`sceSaveDataPrepare` 在主线程） | 见 4.2 节 |
| 4 | 中 | 补全其他弹窗的手柄确认键（`reward_box` / `slot_box` 等） | PG `chaos_input_system_ui_callbacks.lua` |
| 5 | 中 | 「退出游戏」按钮违反 TRC R5093 | 见下方说明 |
| 6 | 中 | Client Secret 轮换（GAC 侧） | 见第 9 节 |
| 7 | 低 | DLC 选型（PSAL / PSAC）+ 补爬 AppContent 文档 | 见 4.5 节 |

### 关于待办 5（TRC R5093）

**TRC R5093 禁止应用自行终止**。原文：

> The application does not perform processing to terminate itself...
> implementations that use a button to terminate the application are prohibited.

而本项目的「退出游戏」按钮走的是：

```
点击退出 → notifyShutdown() → ClientRoot::shutdown() → 主循环 break → 进程结束
```

**三个调用点**：

- `client/ui/widgets/chaos_html_ui_widget_login_base.lua:35`
- `client/ui/widgets/chaos_html_ui_widget_scr_sys_login.lua:120`
- `client/game_level/chaos_client_level_manager.lua:750`

**合规改法**：按钮不终止应用，改为**弹提示让用户用系统方式退出**（按 PS 键选关闭），
文案不要解释具体怎么操作（文档允许 *"display a message asking the user to terminate
the application (without explaining how to do so)"*）。

**唯一可用终止 API 及边界**：`sceSystemServiceReportAbnormalTermination()` **仅限不可恢复的
致命错误**（必需文件缺失 / 关键库内部错误），**禁止用于可恢复错误（明确点名网络断开）**，
且 CertOps 按崩溃处理。

---

## 9. 安全与合规

### 必守项

- **Client Secret 已泄漏**（曾出现在聊天记录与代码中）→ **生产前必须轮换**，
  现只应存在于 GAC 服务端（客户端侧已清理）
- **Client Secret 只能存在于服务端**：禁止写入客户端、禁止提交 git、禁止明文传播
- **`连接配置`、`服务器地址配置` 两个 xml 含 Secret，永不提交**

### NDA

**PS5 SDK / DevNet / TRC 文档受 NDA 保护**：

- 禁止上传在线服务、AI 云、公开仓库
- 禁止外传截图
- ⚠️ **`E:\code\mutli_level\features\ps5\document\output\` 实际未加入 gitignore**
  （`document/.gitignore` 里那行被注释掉了）—— **本工作台仓库请勿推送或分享**

---

## 10. 附录：关键 API 与代码位置

### Chaos 引擎（C++）

```
_source/_engine/source/client/
├── private/chaos/client/platform/
│   ├── chaos_platform_delegate.cpp          # PS5 SDK 调用总入口（登录/奖杯/存档/商店）
│   ├── chaos_ps5_trophy_context.{h,cpp}     # 奖杯：NpTrophy2 + UDS
│   ├── chaos_ps5_data_archive.{h,cpp}       # 存档：SaveData 挂载/事务
│   ├── chaos_ps5_commerce_context.{h,cpp}   # 商店：CHECKOUT 弹窗
│   └── chaos_ps5_subthread.{h,cpp}          # 子线程封装（阻塞型 SDK 调用）
├── private/chaos/client/input/
│   ├── chaos_input_device_manager.cpp       # 输入系统（含 resetInputSystem）
│   └── input_device/chaos_input_device_gamepad.cpp
└── public/chaos/client/platform/
    └── chaos_platform_delegate.h            # 声明 + Meta 注册（Lua 可见）
```

### Proven Ground（Lua）

```
_source/_scripts/
├── client/game_level/chaos_client_login_level.lua       # 登录页流程
├── client/input/chaos_input_system_ui_callbacks.lua     # ★ UI 快捷键映射（手柄键位）
├── client/ui/chaos_ui_info_box_manager.lua              # 消息框 / 加载框
├── client/ui/widgets/chaos_html_ui_widget_scr_message_box.lua
├── client/ui/widgets/chaos_html_ui_widget_recharge_steam.lua   # 充值 UI（含 PS5 分支）
└── server/
    ├── login_server/login_user/chaos_login_user_game_account_center.lua
    └── charge_server/charge_manager/chaos_charge_server_charge_manager_ps5.lua
```

### 关键 SDK API

| API | 用途 |
|---|---|
| `sceUserServiceGetInitialUser` | 取启动时用户（OIS 用它开 pad） |
| `sceUserServiceGetEvent` | 取 LOGIN / LOGOUT 事件 |
| `sceUserServiceGetLoginUserIdList` | 当前登录用户列表 |
| `sceNpHasSignedUp` | 判定用户是否有 PSN 账号（SigninDialog / LoginDialog 分叉点） |
| `sceLoginDialog*` | 本机用户选择框 |
| `sceSigninDialog*` | PSN 登录框 |
| `sceLoginServiceRequestDevices` | **认领手柄**（LoginDialog 后必需） |
| `sceCommonDialogInitialize` | CommonDialog 前置（NpCommerceDialog 等需要） |
| `sceNpCommerceDialog*` | CHECKOUT 购买弹窗 |
| `sceNpAuthGetAuthorizationCodeV3` | 取 auth code |
| `sceNpTrophy2*` | 奖杯（只读 + 回调，**无 unlock**） |
| `sceNpUniversalDataSystemPostEvent` | 发 UDS 事件（奖杯解锁实际走这里） |
| `sceSaveData*` | 存档事务 |
| `sceSystemServiceReceiveEvent` | 取系统事件（**ON_RESUME = 0x10000000**） |
| `sceSystemServiceGetStatus` | 取状态（**isSystemUiOverlaid** 判断系统 UI 是否占输入） |

### TRC 相关条文

| 条文 | 内容 |
|---|---|
| **R5093** | 应用不得自行终止（禁止「退出游戏」按钮、禁止 return from main） |
| **R5089** | Suspend/Resume 实现要求（SaveData API 不能与 `suspendPoint` 同线程） |
| **R5116** | 禁止缓存权利状态，每次用前必须查（DLC 相关） |

在线地址格式：
`https://game.develop.playstation.net/resources/documents/TRC/latest/TRC/<条文号>.html`
（如 `R5093.html`）
