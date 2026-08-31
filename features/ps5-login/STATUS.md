# PS5 登录 — 当前进度与下一步

> **最后更新**：2026-08-31
> **Jira**：CB2N-27968
> **分支**：`feature/CB2N-27968-ps5-login`（Chaos + Proven Ground）
> **状态**：DevKit 实机走通登录（SigninDialog/LoginDialog → auth code → GAC 换 account_id → 进游戏）。

---

## ✅ 已完成

### 客户端（Chaos C++ `PlatformDelegate`）

- [x] `initializePS5()` 只做初始化：加载 `SigninDialog` / `LoginDialog` / `NpAuth` PRX + `sceUserServiceGetInitialUser()`，**不弹任何框**。
- [x] 登录入口原语化为 `startPS5Login()`：重置凭证 + `beginPS5AuthForUser()`（内部判 guest→选用户框 / 真实用户→登录框）。
- [x] `tick()` 状态机轮询 `sceLoginDialogUpdateStatus()` / `sceSigninDialogUpdateStatus()`，OK 后 `sceNpAuthGetAuthorizationCodeV3()` 拿 auth code + issuer_id 存入 `ClientRoot`。
- [x] NpAuth scope 用文档要求的 `"psn:s2s openid id_token:psn.basic_claims"`；nptitle.dat + param.json titleId 对齐后 `sceNpHasSignedUp` 正常（guest 检测有效）。
- [x] Lua 绑定：`startPS5Login()` / `getPS5SigninState()`（反射）+ `getPS5AuthToken()` / `getPS5IssuerID()` / `isPS5Platform()`（accessor）。
- [x] Prospero CMake 链接 `libSceNpAuth_stub_weak.a` + `libSceSigninDialog_stub_weak.a`。

### 客户端（Proven Ground Lua）

- [x] `login_ui_model` PS5 分支：显示服务器选择框 + 调 `startPS5AutoLogin()`。
- [x] `login_level`：**去掉轮询协程**，改由 `tick()` 每帧调 `tickPS5Login()` 读状态统一判断（成功→`loginAndGetAccountAccessToken()`；失败→提示框→重试）。
- [x] `loginAndGetAccountAccessToken()` 走 GAC：`GET GAC/ps5/getUserInfo?issuer=&code=` 拿 account_id + token，再 RPC 登录服（platform=ps5）。

### 登录服（Proven Ground Lua）

- [x] **PS5 统一走 GAC**：`LoginUserManager` 对 `AccountPlatform.ps5` 派发 `LoginUserGameAccountCenter`，经 `GET GAC/login/auth/token` 校验换 account_id。
- [x] **删除废弃的 `chaos_login_user_ps5.lua`**（直连 S2S + 硬编码 secret 的旧实现，改走 GAC 后成死代码）。

### GAC（`E:\code\game_account_center`，独立 Go 仓库）

- [x] 新增 `/ps5/getUserInfo`（拿 PSN token）+ `/login/auth/token`（校验）端点。**client_secret 现在只存在于 GAC，不在游戏代码里。**

---

## 🎯 下一步（按优先级）

### P1 — 上线前必须清理的临时脚手架

| 步骤 | 位置 | 内容 |
|---|---|---|
| **P1-1** | `chaos_login_user_game_account_center.lua:94-97`<br>`chaos_login_manager.lua:302`（客户端） | 移除 ps5 强制指向 `http://10.10.1.218:8015` 的本地联调 hack（客户端 + 登录服各一处），改用正式 GAC 地址/配置 |
| **P1-2** | `connect_config.xml` | YMJ 本机联调地址（`10.10.1.218`）——已保持未提交，上线前勿混入 |
| **P1-3** | `chaos_platform_delegate.cpp` | 硬编码的 `client_id` / `np_title_id` / `product_id` 按环境配置化（sp-int/prod-qa/np） |
| **P1-4** | GAC（Go 仓库） | **轮换泄漏的 client secret `DtCLkkWViqmORho9`**（曾出现在聊天/代码，游戏侧已删，GAC 侧仍需换） |
| **P1-5** | GAC 服务端文件 | 清掉 `[requestAccountCenterAuth] content_str` 等临时 LOG（含 token 明文） |
| **P1-6** | `chaos_login_user_base.lua` | 孤立的 `LoginHttpRequestType.ps5_auth/ps5_userinfo` 枚举（随死文件删除后已无引用，可选清理，注意枚举值别乱序） |

### P2 — 完整体验

| 步骤 | 内容 |
|---|---|
| **P2-1** | 用户切换/退出：监听 `sceSystemServiceReceiveEvent` / `sceUserServiceEvent`，切用户后重走登录 |
| **P2-2** | 已登录用户免框：`signedUp==true` 时用 `sceNpGetState` 判断在线态，已在线则跳过 SigninDialog |
| **P2-3** | token 刷新：access_token 过期后的续期流程 |
| **P2-4** | 错误提示细化：区分 NpAuth 失败 / GAC 失败 / 网络异常 |

---

## 🔍 如何验证 GAC 功能

见本文件末尾「GAC 验证」小节 + [docs/game_account_center.md](docs/game_account_center.md)。核心两条链路：

1. **客户端 → GAC `/ps5/getUserInfo`**：拿 auth code 换 account_id + token。
2. **登录服 → GAC `/login/auth/token`**：用上一步的 token 校验换 account_id。

分层验证（先单独 curl 打端点，再看游戏日志链路），详见回复。

---

## 相关文档

- [IMPLEMENTATION.md](IMPLEMENTATION.md) — 实现细节、代码路径、数据流
- [docs/game_account_center.md](docs/game_account_center.md) — GAC Go 服务分析 + PS5 收口方案
- [docs/ps5_login_methods.md](docs/ps5_login_methods.md) — S2S vs ID Token 方案选型
- [docs/ps5_sdk_reference_links.md](docs/ps5_sdk_reference_links.md) — SDK / Auth Web API 文档索引


---

# PS5 存档/奖杯/支付 — 当前进度（2026-08-26）

> **Jira**：CB2N-29569
> **分支**：`feature/CB2N-29569-ps5-trophy-payment`（两仓库，已 rebase 最新 master）
> **前序**：登录（CB2N-27968 已合入）、存档（同分支早期 commit，已 DevKit 验证）

## ✅ 存档（SaveData）— 完成
- `PS5DataArchive`：mount/prepare/commit 封装，context 持有，分阶段初始化
- 设置文件按 渠道_MD5(account) 命名，跨服唯一
- TRC R5089：写事务走子线程（`runOnPS5Subthread`，引擎任务调度器）
- 存档切换由索引变化驱动（`setSaveAccountID(platform, account)` 唯一入口）

## ✅ 奖杯（Trophy）— 代码完成，DevKit 解锁验证通过
- `PS5TrophyContext`：NpTrophy2 context + UDS 事件解锁（_UnlockTrophy）
- **PS5 无直接 unlock API**：解锁 = post UDS 事件，系统比对条件异步解锁，回调经 sceNpCheckCallback 派发
- 已解锁的奖杯重复 post：系统静默忽略（无提示无错误）
- deferred init（首帧）—— RegisterContext 阻塞须子线程，启动期调度器未就绪会崩
- **待办**：设计表 PlatformAchievementInfo 加 ps5_trophy_id 字段（schema 回退了，等资产管线配合）+ 策划填表

## 🔧 支付（Payment）— 代码完成，等 Content Pipeline 商品就绪（2026-08-31）
- 详见 [docs/ps5_payment_plan.md](docs/ps5_payment_plan.md) 实施状态章节
- 客户端 CHECKOUT 弹窗 + 服务端 consumeEntitlement（S2S）+ Bearer token + RPC 全链路代码就绪
- 商品已配（CONQCOIN00000000，PSVC unified entitlement）
- **代码侧两处修复已提交源码、待重编 dll**：
  - `getCheckoutState()` 改为取后自动回 idle（原 const getter 导致 purchased/closed 永不复位 → 二次 openCheckout 被 `not ready state=3` 拒绝）
  - `sceNpCommerceDialogGetResult()` 返回值判断改 `ret < 0`（正常终止返回正值：OK=1/USER_CANCELED=2/PURCHASED；旧 `ret != SCE_OK` 把 OK 当错误打出误导性日志）
- **当前卡点全在 Content Pipeline 侧**（见下方"支付商品发布链"）

### 支付商品发布链（Content Pipeline，2026-08-31 现状）
```
Product: Submitted ✅（≠ 可售）
  └─ Entitlement: In Progress ⏳（SIE 异步开通，只能等）
       └─ PAR: 已填各区域 WSP + Availability，待提交/审核 → Valid
            └─ Valid + Availability 日期到 → Product Preview 发布（PSVC 选
               "Publish without Linking Entitlements"）→ 可购买
```
- **WSP** = Wholesale Selling Price，批发结算价 = 商店售价基数（美区等另加消费税）
- **Availability** = 上架日期（street date）。**新 PAR 只能填未来日期**（系统强制，最早约 +5 天），
  日期未到 checkout 就是"无法购买"——预期行为
- **Regional Termination Date** = 区域下架日期，测试阶段留空（=永不下架）
- **dev 环境同样走 PAR 全流程**（Commerce Programming Guide：dev 测试 = 购买"created in the development environment"的商品）；
  dev 唯一优惠：测试卡充值（VISA 4444 4444 4444 4448）+ Product Preview 直接发布不过认证
- 一档面额 = 一个 Product（PSVC 文档 BIGGAMEBUCKS_100 模式）；多档位 = 多 Product，
  服务端按 entitlement label 映射金币数
- "目前无法购买此产品" = PS5 系统文案（非游戏代码打印）：商品未发布 / PAR 无效 / Availability 未到 / 区域与账号不匹配，任一即触发
- **区域必须匹配测试账号注册国**（账号美区→配 US/USD），checkout 按账号所在区取价

## 关键认知沉淀
- **PS5 分阶段初始化**：启动期（initializePS5，主线程直调）vs 首帧（deferred，调度器就绪可子线程）
- **CMake GLOB 坑**：新增 cpp 必须重新 reconfigure，否则不进工程
- **Meta 生成后必须重编对应 dll**：meta 新 dll 旧 → Lua 调用抛错 → 连锁崩溃
- **CRLF 红线**：中文注释文件必须 CRLF，LF 会让 MSVC(GBK) 注释吃掉下一行代码（静默）
- **Content Pipeline**：Group 内 Product=区域变体；多档位=多 Group 共享 entitlement；不能删除只能 DO NOT USE
- **CommerceDialog 生命周期**：按 SDK sample 每次购买 init→open→poll→result→terminate；
  GetResult 正常终止返回正值，错误才返回负值（SCE_OK 语义不适用）
- **PS5 客户端日志只有 stdout**（spdlog 文件 sink 被 Prospero 条件编译排除），
  调试器 Console Output 看，格式 `[Level][file][line][module][msg]`
- **充值 UI 挂在 BigWorldUIModel**：登录 Level 激活的是 LoginUIModel，UIStateManager:open
  静默无效——登录页测支付直接调 `platform_delegate:openPS5Checkout(label)`，不走 UI

## 🏆 奖杯重复测试方法（解锁后重置，无需换账号）
DevKit 系统软件提供奖杯数据删除功能（Trophy System Overview – Features for Deleting Trophy Data）：

**推荐（删当前用户 console+server，最彻底）**：
```
系统软件 Trophies → 选中奖杯集 → Options → ★Delete This User's Trophies (Console and Server)
或命令行：prospero-ctrl application delete-data trophy all /user:<User>
```
**注意**：删奖杯数据**不会**同时删 UDS Stats（解锁条件的统计数据）——两者不一致会导致奖杯
状态错乱。删完奖杯后**还要删 UDS Stats**：
```
★Debug Settings > PlayStation Network > Universal Data System data > Delete data of this user (console and server)
或：prospero-ctrl application delete-data uds all /user:<User>
```
完整重置 = 删奖杯（trophy all）+ 删 UDS（uds all），然后重新进游戏触发解锁。
另有 `trophy console`（只删本机，Online 模式会从服务器同步回来）和
Offline 模式下的 ★Unlock/★Lock 单个奖杯开关（PS4 奖杯限定，PS5 不可用）。
