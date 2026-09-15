# PS5 登录 — 进度

> **最后更新**：2026-09-07（从 `features/ps5-login/STATUS.md` 拆分而来）
> **Jira**：CB2N-27968
> **状态**：**已合入 master**。DevKit 实机走通完整登录链路。

---

## 已完成

### 客户端（Chaos C++ `PlatformDelegate`）

- `initializePS5()` 只做初始化：加载 SigninDialog / LoginDialog / NpAuth PRX
  + `sceUserServiceGetInitialUser()`，**不弹任何框**
- 登录入口统一为 `startPS5Login()`：**每次从头判定**（无条件拆 dialog → 重查
  `getInitialUser` + `sceNpHasSignedUp` → 唯一分叉）。原 `beginPS5AuthForUser()`
  已删除（2026-09-14 重构，见 [USER_FLOWS.md](USER_FLOWS.md)）
- `tick()` 状态机轮询 `sceLoginDialogUpdateStatus()` / `sceSigninDialogUpdateStatus()`，
  OK 后 `sceNpAuthGetAuthorizationCodeV3()` 拿 auth code + issuer_id 存入 `ClientRoot`
- NpAuth scope 用文档要求的 `"psn:s2s openid id_token:psn.basic_claims"`；
  nptitle.dat + param.json titleId 对齐后 `sceNpHasSignedUp` 正常（guest 检测有效）
- Lua 绑定：`startPS5Login()` / `getPS5SigninState()`（反射）
  + `getPS5AuthToken()` / `getPS5IssuerID()` / `isPS5Platform()`（accessor）
- Prospero CMake 链接 `libSceNpAuth_stub_weak.a` + `libSceSigninDialog_stub_weak.a`

### 客户端（Proven Ground Lua）

- `login_ui_model` PS5 分支：显示服务器选择框 + 调 `startPS5AutoLogin()`
- `login_level`：**去掉轮询协程**，改由 `tick()` 每帧调 `tickPS5Login()` 读状态统一判断
  （成功 → `loginAndGetAccountAccessToken()`；失败 → 提示框 → 重试）
- `loginAndGetAccountAccessToken()` 走 GAC：
  `GET GAC/ps5/getUserInfo?issuer=&code=` 拿 account_id + token，再 RPC 登录服（platform=ps5）

### 登录服（Proven Ground Lua）

- **PS5 统一走 GAC**：`LoginUserManager` 对 `AccountPlatform.ps5` 派发
  `LoginUserGameAccountCenter`，经 `GET GAC/login/auth/token` 校验换 account_id
- **删除废弃的 `chaos_login_user_ps5.lua`**（直连 S2S + 硬编码 secret 的旧实现，
  改走 GAC 后成死代码）

### GAC（`E:\code\game_account_center`，独立 Go 仓库）

- 新增 `/ps5/getUserInfo`（拿 PSN token）+ `/login/auth/token`（校验）端点
- **client_secret 现在只存在于 GAC，不在游戏代码里**

---

## 上线前必须清理（P1）

| 步骤 | 位置 | 内容 |
|---|---|---|
| P1-1 | `chaos_login_user_game_account_center.lua:94-97`<br>`chaos_login_manager.lua:302`（客户端） | 移除 ps5 强制指向本机联调地址的 hack（客户端 + 登录服各一处），改用正式 GAC 地址/配置 |
| P1-2 | `连接配置 xml` | 本机联调地址 —— 已保持未提交，上线前勿混入 |
| P1-3 | `chaos_platform_delegate.cpp` | 硬编码的 `client_id` / `np_title_id` / `product_id` 按环境配置化（sp-int / prod-qa / np） |
| P1-4 | GAC（Go 仓库） | **轮换泄漏的 client secret**（游戏侧已删，GAC 侧仍需换） |
| P1-5 | GAC 服务端文件 | 清掉 `[requestAccountCenterAuth] content_str` 等临时 LOG（含 token 明文） |
| P1-6 | `chaos_login_user_base.lua` | 孤立的 `LoginHttpRequestType.ps5_auth/ps5_userinfo` 枚举（可选清理，注意枚举值别乱序） |

---

## 完整体验（P2，非阻塞）

| 步骤 | 内容 |
|---|---|
| P2-1 | 用户切换/退出 —— **已实现，待实测**。详见下方 [P2-1 详述](#p2-1-用户切换实现与待验证项) |
| P2-2 | 已登录用户免框：`signedUp==true` 时用 `sceNpGetState` 判断在线态，已在线则跳过 SigninDialog |
| P2-3 | token 刷新：access_token 过期后的续期流程 |
| P2-4 | 错误提示细化：区分 NpAuth 失败 / GAC 失败 / 网络异常 |

**P2-1 是存档 D3 缺陷（二次登录不重新绑定存档）的前置条件。**
**P2-3 是支付 token 架构的前置条件之一。**

---

## P2-1 用户切换：实现与待验证项

> **状态**：代码已就绪（Chaos + Proven Ground），`param.json` 已改，**未实测**。
> **文档日期**：2026-09-14

### 事件原理（两个触发源）

**PS5 换用户在应用看来是「登出 + 登录」事件流**，但**真正可靠的检查点是 resume**：

```
玩家按 PS 键 → 切换使用者
   │
   ├─ 应用被 suspend        ← ★ 文档：应用无法感知进入挂起
   │    （挂起期间不跑 tick，LOGOUT 事件可能根本没机会处理）
   │
   ├─ 玩家在主界面选另一个用户 / 重新登录
   │
   └─ 应用 resume           ← ★ 唯一的可靠检查点
        SystemService 的 SCE_SYSTEM_SERVICE_EVENT_ON_RESUME (0x10000000)
```

**所以两个事件源都要监听**：

| 来源 | API | 事件 | 覆盖场景 |
|---|---|---|---|
| UserService | `sceUserServiceGetEvent()` | `LOGIN`(0) / `LOGOUT`(1) | 主动登出、系统强制登出 |
| **SystemService** | `sceSystemServiceReceiveEvent()` | **`ON_RESUME`(0x10000000)** | **换用户（挂起恢复）** |

### 四种登出场景（无法区分，也无需区分）

| 场景 | 事件 |
|---|---|
| 切换用户，B 原本**未登录** | LOGOUT(A) + LOGIN(B) + 恢复时 ON_RESUME |
| 切换用户，B 原本**已登录** | **只有 LOGOUT(A)**（无 LOGIN）+ ON_RESUME |
| 玩家主动登出 | LOGOUT |
| 系统强制登出（网络异常等） | LOGOUT |
| 设备重新绑定 | 无事件 |

> 原文：*"Information that would distinguish between logouts, logins, and changes to device linkages caused by the 'Switch User' feature and those caused by other operations is **not provided to the application**."*

**四种情况一律回登录页** —— 匿名用户强制登录由登录页自身逻辑保证，不受影响。

### suspend 的触发条件（由 `attribute2` 决定）

`InitialUserAlwaysLoggedIn` 是 **`attribute2` 的第 0 位**：

| `attribute2` | 含义 | suspend 触发条件 | 谁能 resume |
|---|---|---|---|
| `0` | 不支持初始用户登录/登出 | **初始用户**登出 | **只有初始用户** |
| **`1`**（本项目已改） | **支持**，应用自行接管 | **所有用户**都登出 | **任何用户** |

> 原文（`application-states.md`）：*"An application with the InitialUserAlwaysLoggedIn parameter disabled in param.json: **When all users log out, the application will transition to the suspended state. Any user can resume application operation.**"*

**注意**：改成 `1` 后 suspend **依然会发生**（换用户时旧用户登出、新用户未登录 = 所有用户都登出）。
区别在于 **`1` 时任何用户都能 resume**，`0` 时只有原用户能 resume（换用户后回不来）。

**日志**：`param.json` 由 `.gitignore` 排除（`_content/`），**手动上传到 DevKit**，不在版本控制里。

### 已实现的代码

**Chaos C++**（`chaos_platform_delegate.{h,cpp}`，全部在 `#if defined(CHAOS_PLATFORM_PROSPERO)` 内）

| 位置 | 内容 |
|---|---|
| `tick()` | `pollPS5UserEvents()` + `pollPS5SystemEvents()` —— 放在最前，用户变了同帧其它系统才能跟着反应 |
| `pollPS5UserEvents()` | 排空 UserService 事件：LOGOUT 置 `m_ps5_logout_pending`；LOGIN 更新 `m_ps5_user_id` + 重挂存档 |
| **`pollPS5SystemEvents()`** | 排空 SystemService 事件：`ON_RESUME` 置 `m_ps5_resume_pending` |
| `consumePS5LogoutEvent()` | 一次性标志（Meta 暴露） |
| **`consumePS5ResumeEvent()`** | 一次性标志（Meta 暴露） |

新增 include：`<system_service.h>`（cpp 的 PS5 include 段）

**Proven Ground Lua**（`chaos_client_login_level.lua`）

```lua
LuaClientLoginLevel:tickPS5UserEvent()      -- 挂在 tick() 里 tickStorageGeneration() 之后
    local logged_out = platform_delegate:consumePS5LogoutEvent() == 1;
    local resumed    = platform_delegate:consumePS5ResumeEvent() == 1;
    if logged_out ~= k_true and resumed ~= k_true then return end
    g_lua_client_global_context.m_level_manager:returnToLoginLevel();
```

**位置正确性**：`ClientLevelManager:tick` 里 `self.m_login_level:tick()` 是**无条件调用**的，所以**游戏内收到事件也能响应**，不只登录页。

### 为什么是「回登录页」而不是「退出游戏」

**文档推荐**（`user-management-on-the-ps5.md`）：

> *"User B logging in should be treated as an ordinary login... **If logging out means not being able to continue playing, then handle the logout by returning to the title screen** or by doing whatever else would be suitable in that case."*

**不采用「退出游戏」的理由**：

1. **★ TRC R5093 明令禁止** —— 见下节，这是硬性规定
2. **无法区分登出原因** → 网络抖动导致的系统强制登出也会被当成换用户，**误伤玩家**
3. **回登录页已满足需求** —— `returnToLoginLevel()` 会清 login level + game level，
   不存在状态串号；匿名用户仍会被强制登录

### ★ TRC R5093：应用不得自行终止

**权威原文**（`TRC/latest/TRC/R5093.html`）：

> **Requirement: The application does not perform processing to terminate itself.**
>
> This requirement is in place in order to **make the system software the standard way of
> terminating the application**. For example **implementations that use a button to terminate
> the application are prohibited**.

**另一处表述**（`Kernel-Overview/process-termination.html`）：

> **Voluntary process termination by an application is prohibited by TRC [R5093].**
> In other words, applications **must not return from `main()` or call `exit()`/`_Exit()`**.

**测试用例 R5093A**：

> **Procedures:** 1. Select the Application  2. **Proceed to where users are prompted to
> exit the application**  3. The user performs the prompt action
>
> **Notes:** "Users are prompted to exit the application" in step (2) refers to content such
> as **"Press the circle button to exit the application"**. **If a core dump is executed when
> the circle button is pressed at this time, the application will have performed voluntary
> termination processing and will be in violation of this requirement.**

#### `sceSystemServiceReportAbnormalTermination()` 的合规边界

**只允许**在不可恢复的致命错误时调用：

> only if processing that should succeed fails, and **advancement is no longer possible as
> the application cannot be restored**. Examples: When a required file is missing / When
> calling a function for a library essential to advancement returns an internal error

**明确禁止**用于可恢复错误：

> For the handling of **recoverable errors such as a network disconnection**, calling
> `sceSystemServiceReportAbnormalTermination()` **is not permitted** and appropriate error
> handling must be carried out instead.

**且在 CertOps 中会按崩溃处理**：

> Calling `sceSystemServiceReportAbnormalTermination()` force terminates the application
> generating a core dump. The forced termination will be handled in CertOps as **equivalent
> to the application crashing**.

**允许的替代做法** —— 提示用户，由系统终止：

> it is permitted to **display a message asking the user to terminate the application
> (without explaining how to do so)**.

### ⚠️ 待修：现有「退出游戏」按钮违反 R5093

**三个调用点，都是玩家可见的退出入口**：

| 位置 | 场景 |
|---|---|
| PG `client/ui/widgets/chaos_html_ui_widget_login_base.lua:35` | 登录页「退出游戏」按钮（`onQuitButtonClick`） |
| PG `client/ui/widgets/chaos_html_ui_widget_scr_sys_login.lua:120` | 系统登录界面「退出游戏」按钮 + `quit` 热键 |
| PG `client/game_level/chaos_client_level_manager.lua:750` | `ClientLevelManager:onExit`（核心退出流程） |

**调用链**：

```
Lua: 点「退出游戏」→ 弹确认框 "do_you_really_want_to_exit_game"
   → 确认 → m_world_manager:notifyShutdown()
       → C++ ClientWorldManager::notifyShutdown()   [m_engine_should_shut_down = k_true]
       → tickLogic 计时器到点 → ClientRoot::shutdown()
           → m_is_start_shut_down = k_true
               → 主循环 break → runImp 返回 → 进程结束
```

**唯一调用点**：`chaos_client_world_manager.cpp:394`（`ClientRoot::shutdown`）

**这就是 R5093 禁止的「用按钮终止应用」，且 UI 文案 "do you really want to exit game"
精确命中 R5093A 的测试步骤。**

**合规改法**：按钮不再终止应用，改为**弹提示让用户用系统方式退出**（按 PS 键选关闭）。
文案不要解释具体怎么操作：

> display a message asking the user to terminate the application
> (**without explaining how to do so**)

**影响**：本项目正在走 GC-119326 认证，**这是会被抓的项**。与换用户逻辑无关，需单独修。



### 待验证项（实机）

1. **换用户后进程状态**：suspend → resume？（文档说需要玩家重新选回应用才 resume）
2. **日志确认两个事件都收到**：
   ```
   [PlatformDelegate::pollPS5SystemEvents] resumed from suspension, user_id=<id>
   [LuaClientLoginLevel] PS5 returning to login level (logout=..., resume=...)
   ```
3. **回登录页后能否重新登录**，且奖杯/存档/商店绑到新用户
4. **DevKit 检查** `★Debug Settings > Game > Instant App Suspending`
   —— 文档说设为 "On" 时「按 PS 键 → Home」会 suspend 而非 background。
   **若为 On，测的就不是真实场景**，需确认。

### 文档地址（原始 URL）

**换用户 / 挂起恢复**

```
★ 应用状态与挂起/恢复（权威）
https://game.develop.playstation.net/resources/documents/SDK/12.000/Programming-Startup_Guide/application-states.html

SystemService 事件（ON_RESUME 等 10 种）
https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-event-type.html
https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-receive-event.html

UserService 事件（LOGIN / LOGOUT）
https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-event-type.html
https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-get-event.html

换用户机制 / 四种情况不可区分
https://game.develop.playstation.net/resources/documents/SDK/12.000/User_Management-Overview/user-management-on-the-ps5.html

param.json attribute2（InitialUserAlwaysLoggedIn 位）
https://game.develop.playstation.net/resources/documents/SDK/12.000/Param_Json-Specification/parameter-definitions-for-applications.html

单机模式 / InitialUserAlwaysLoggedIn
https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Overview/processing-procedure-for-single-player-games.html

终止 API（不要用于正常退出）
https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/sce-system-service-report-abnormal-termination.html

DevKit 设置项索引
https://game.develop.playstation.net/resources/documents/SDK/12.000/System_Software-Users_Guide_for_Settings/game-instant-app-suspending.html
```

**本地路径**：`../document/output/psn_12/Getting_Started/Programming_Basics/Programming-Startup_Guide/`
与 `System/User_Management/`、`System/System_Service/`

---

## 如何验证 GAC

两条链路，分层验（先单独 curl 打端点，再看游戏日志链路）：

1. **客户端 → GAC `/ps5/getUserInfo`**：拿 auth code 换 account_id + token
2. **登录服 → GAC `/login/auth/token`**：用上一步的 token 校验换 account_id

详见 [docs/game_account_center.md](docs/game_account_center.md)。

---

## 相关文档

- [USER_FLOWS.md](USER_FLOWS.md) — **用户流程全景**（匿名/真实/切换，所有路径与分叉点）
- [IMPLEMENTATION.md](IMPLEMENTATION.md) — 实现细节、代码路径、数据流
- [docs/game_account_center.md](docs/game_account_center.md) — GAC Go 服务分析 + PS5 收口方案
- [docs/ps5_login_methods.md](docs/ps5_login_methods.md) — S2S vs ID Token 方案选型
- [../shared/ps5_sdk_reference_links.md](../shared/ps5_sdk_reference_links.md) — SDK / Auth Web API 文档索引

---

## 相关文档 URL 索引（便于回查）

### 换用户 / 用户管理

```
换用户机制 / 四种情况不可区分  ★「回标题页」建议出自此篇
https://game.develop.playstation.net/resources/documents/SDK/12.000/User_Management-Overview/user-management-on-the-ps5.html
User Management 总览
https://game.develop.playstation.net/resources/documents/SDK/12.000/User_Management-Overview/__toc.html
单机模式 / InitialUserAlwaysLoggedIn
https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Overview/processing-procedure-for-single-player-games.html
UserService 总览 / 参考
https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Overview/__toc.html
https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/__toc.html
```

### 事件 API

```
SystemService 事件类型（ON_RESUME 0x10000000 等）
https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-event-type.html
SystemService 接收事件
https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-receive-event.html
SystemService 总览 / 参考
https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Overview/__toc.html
https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/__toc.html
UserService 事件类型（LOGIN / LOGOUT）
https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-event-type.html
UserService 获取事件
https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-get-event.html
登录用户列表
https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-get-login-user-id-list.html
```

### param.json

```
应用参数定义（attribute2 表 = InitialUserAlwaysLoggedIn 位）
https://game.develop.playstation.net/resources/documents/SDK/12.000/Param_Json-Specification/parameter-definitions-for-applications.html
规范总览
https://game.develop.playstation.net/resources/documents/SDK/12.000/Param_Json-Specification/__toc.html
```

### 终止（说明为何不用）

```
报告异常并终止 —— 文档明确会「向用户报错」且判为崩溃
https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/sce-system-service-report-abnormal-termination.html
★ R5093 原文见上方「TRC / 内核」节
```

### TRC / 内核

```
★ TRC R5093 —— 应用不得自行终止（权威）
https://game.develop.playstation.net/resources/documents/TRC/latest/TRC/R5093.html
Kernel Overview —— 进程终止（R5093 的另一处表述）
https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Overview/process-termination.html
Kernel Overview 总览
https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Overview/__toc.html
Kernel Reference 总览
https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/__toc.html
```

### DevKit 调试

```
Instant App Suspending 设置项  ★测 resume 前必须确认
https://game.develop.playstation.net/resources/documents/SDK/12.000/System_Software-Users_Guide_for_Settings/game-instant-app-suspending.html
System Software 设置总览
https://game.develop.playstation.net/resources/documents/SDK/12.000/System_Software-Users_Guide_for_Settings/__toc.html
```

### 后台工具

```
Content Pipeline —— CONQ concept（注意不在 DevNet 域下）
https://publish.playstation.net/concepts/10020266
CONQ COIN Product Group
https://publish.playstation.net/concepts/10020266/products/10090141
In-Game Catalog
https://publish.playstation.net/concepts/10020266/ingamestructures/10008112
Certification Center
https://certify.playstation.net/fqaweb/index.cfm
```
