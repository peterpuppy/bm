# PS5 用户流程全景（匿名 / 真实 / 切换）

> **目的**：一张图看清所有用户路径，防止后续改动引入"不清楚的 BUG"。
> **对应代码**：`chaos_platform_delegate.{h,cpp}`
> **2026-09-14 重构**：登录入口统一为 `startPS5Login()` **从头判定** ——
> 每次调用向系统重新查询初始用户与 `sceNpHasSignedUp`，不信任任何缓存。
> 首次启动 / 取消后重试 / 换用户后重进，全部走同一条路。
> 原 `beginPS5AuthForUser()` 已删除（逻辑折入 startPS5Login 的判定段）。
>
> **2026-09-15 修正 ②（输入交还时序）**：原生框取消后**不立即**把失败报给 Lua ——
> 新增中间态 `failed_pending`，由 tick 中的 `updatePS5PendingFailure()` 等到
> `SceSystemServiceStatus::isSystemUiOverlaid` 落回 false 再升级为 `failed`
> （上限 300 帧兜底）。根因：原生框关闭动画期间系统 UI 仍在**截获手柄输入**
> （文档原文：*"isSystemUiOverlaid will be true when the controller input is being
> intercepted from system software UI"*），此时游戏弹出的 HTML 提示框被压在系统层下，
> 按任何键都不会到达它。实测日志 `systemUiOverlaid=1 (signin_state=2)` 即此刻。
> `getPS5SigninState()` 把 `failed_pending` 归为"进行中"(0)。
>
> **2026-09-15 修正 ①（dialog 生命周期）**：两个 dialog 改为**初始化一次、重复 Open** ——
> 用完**不 terminate**，状态留在 FINISHED，下次直接 `Open()`（文档明确的再显示路径：
> LoginDialog/SigninDialog basic-procedure step 3 note）。terminate 只发生在
> `finalizePS5()`（关机）和 Open 失败兜底。原因：实测"每次 terminate → 重新 initialize"
> 循环后，第二次弹出的框不响应任何输入（open 返回 SCE_OK 但框是死的），
> 而 terminate 的文档契约只覆盖"初始化过之后"的场景。
> **关联**：[STATUS.md](STATUS.md) P2-1 ｜ [../question/](../question/README.md)

---

# PS5 用户流程（修复后）

## 一、匿名（guest）用户流程

```
启动
  ↓
initializePS5()
  m_ps5_user_id = sceUserServiceGetInitialUser()    // = guest 的 user id
  ↓
首帧 tick → pollPS5UserEvents()
  收到补发的 LOGIN 事件（可能是真实用户，不是 guest）
  → 只记日志，不改 m_ps5_user_id ✅              // 关键：不破坏 guest id
  ↓
Lua: 检测到 PS5 → startPS5AutoLogin()
  ↓
C++: startPS5Login()
  清理旧 dialog（如果有）
  m_ps5_signin_state = none
  ↓
startPS5Login() 重判定
  sceUserServiceGetInitialUser() → guest id
  sceNpHasSignedUp(guest_id) → false               // guest 判定
  ↓
startPS5LoginDialog()                              // 弹「选用户」框
  列出全部用户，initialFocus = guest_id
  m_ps5_signin_state = waiting_login_dialog
  ↓
【分支 A：玩家选了真实用户】
  updatePS5LoginDialog()
    result.userId = 真实用户 id
    m_ps5_user_id = 真实用户 id                   // 这里才真正切换
    m_ps5_savedata_remount_requested = true
    ↓
  startPS5SigninDialog()                           // 切到真实用户的登录框
    （如果已登录 PSN → 秒过；未登录 → 弹 PSN 登录）
    ↓
  后续走真实用户路径...

【分支 B：玩家取消】
  updatePS5LoginDialog()
    result.result = USER_CANCELED
    m_ps5_signin_state = failed
    m_ps5_user_id 保持 = guest_id（不清空）       // 关键：下次重试还能用
  ↓
Lua: tickPS5Login() 读到 failed
  弹提示框"需要登录"，回调 = startPS5AutoLogin()
  ↓
【玩家按提示框上的 X】
  回调触发 → startPS5AutoLogin()
    ↓
  C++: startPS5Login()
    重置状态机；dialog 直接复用（Open from FINISHED）✅
    从头判定（同首次）
    ↓
  从头判定（同首次）
    sceNpHasSignedUp(初始用户) → false
    ↓
  startPS5LoginDialog()                            // 第二次弹选用户框
    新框能接受输入 ✅
```

---

## 二、真实用户流程（已登录 PSN）

```
启动
  ↓
initializePS5()
  m_ps5_user_id = sceUserServiceGetInitialUser()    // = 真实用户 id
  ↓
首帧 tick → pollPS5UserEvents()
  收到补发的 LOGIN 事件（该用户自己）
  → 只记日志，不改 m_ps5_user_id ✅
  ↓
Lua: startPS5AutoLogin()
  ↓
C++: startPS5Login()
  清理旧 dialog
  m_ps5_signin_state = none
  ↓
startPS5Login() 重判定
  sceUserServiceGetInitialUser() → 真实用户 id
  sceNpHasSignedUp(真实用户id) → true              // 真实用户判定
  m_ps5_user_id = initial_user
  ↓
startPS5SigninDialog()                             // 弹「PSN 登录」框
  该用户已登录 PSN → 秒过（框闪一下就消失）
  m_ps5_signin_state = waiting_dialog → dialog_finished → auth_fetching
  ↓
sceNpAuthGetAuthorizationCode() → 成功
  m_ps5_signin_state = success
  ↓
Lua: 拿到 auth code，走 GAC 验证 → 进游戏
```

---

## 三、真实用户流程（未登录 PSN）

```
启动 → ... → startPS5Login() 从头判定
  sceNpHasSignedUp(初始用户) → true
  ↓
startPS5SigninDialog()
  该用户未登录 PSN → 弹真的 PSN 登录框（输邮箱密码）
  m_ps5_signin_state = waiting_dialog
  ↓
【分支 A：登录成功】
  updatePS5SigninDialog()
    框关闭 → sceNpAuthGetAuthorizationCode() → 成功
    m_ps5_signin_state = success
    ↓
  后续同上

【分支 B：取消】
  updatePS5SigninDialog()
    result = USER_CANCELED
    m_ps5_signin_state = failed
  ↓
  弹提示 → 重试 → 回到 startPS5Login() → 同匿名重试路径
```

---

## 四、用户切换流程（运行中）

### 4.1 同一用户 suspend/resume（不切换）

```
游戏运行中，玩家按 PS 键 → Home（Instant App Suspending = On 时触发 suspend）
  ↓
suspend → tick 停止
  ↓
玩家选回游戏 → resume
  ↓
pollPS5SystemEvents()
  收到 ON_RESUME
  isPS5UserLoggedIn(m_ps5_user_id) → true ✅        // 用户还在
  → 不设 m_ps5_resume_pending
  ↓
游戏继续，不回登录页 ✅
```

### 4.2 切换到不同用户（attribute2=0 的当前实测）

```
游戏运行中，玩家按 PS 键 → 切换使用者
  ↓
suspend → tick 停止
  ↓
系统想发 LOGOUT 事件，但 tick 停了，事件可能未被处理
  ↓
玩家选了不同用户 → 系统想 restart
  ↓
VS 跑的裸 ELF 无法 restart → 进程被终止 ❌      // attribute2=0 的行为
  （这不是 bug，是当前配置的预期）
```

### 4.3 当前用户登出（非切换）

```
游戏运行中，玩家主动登出（或系统强制登出）
  ↓
pollPS5UserEvents()
  收到 LOGOUT 事件
  event.userId == m_ps5_user_id → true ✅          // 是当前用户
  m_ps5_logout_pending = true
  ↓
tickPS5UserEvent()
  consumePS5LogoutEvent() == 1
  → returnToLoginLevel() ✅
```

### 4.4 其他用户登入/登出（旁观者）

```
游戏运行中，另一个用户登录/登出（不是你玩的那个）
  ↓
pollPS5UserEvents()
  收到 LOGIN/LOGOUT 事件
  event.userId != m_ps5_user_id
  → 只记日志，不设任何标志 ✅                    // 不打断游戏
```

---

## 关键差异点对比

| 场景 | startPS5Login 重判定 | 判定结果 | 弹的框 | 结果 |
|---|---|---|---|---|
| 匿名启动 | 初始用户未注册 | false | **LoginDialog**（选用户） | 选真实用户 → 切到 SigninDialog |
| 真实用户（已登录 PSN） | 初始用户已注册 | true | **SigninDialog**（秒过） | 直接拿 auth code |
| 真实用户（未登录 PSN） | 初始用户已注册 | true | **SigninDialog**（输密码） | 登录后拿 auth code |
| 匿名取消后重试 | **同首次，从头重判** | false | **LoginDialog**（第二次） | 与第一次完全同路径 |
| LoginDialog 里选了 guest | — | — | **SigninDialog**（强制 PSN 注册） | 注册/登录后拿 auth code |

---

## 不会混淆的保证

### ① 两种 dialog 不会串

- **LoginDialog**：选用户（MODE_ALL_USERS），只在 guest 路径
- **SigninDialog**：PSN 登录（输密码或秒过），只在真实用户路径

`startPS5Login()` 内的重判定（`getInitialUser` + `sceNpHasSignedUp`）是**唯一硬性分叉点**，
两条路径从此分开。**每次调用都重判，没有缓存路径。**

### ② m_ps5_user_id 只在三个地方改写

| 代码位置 | 时机 | 含义 |
|---|---|---|
| `initializePS5()` | 启动时 | 从系统拿初始用户（guest 或真实） |
| `startPS5Login()` | 每次登录尝试的重判定 | 重判后赋值（不信任缓存） |
| `updatePS5LoginDialog()` | LoginDialog 选了用户 | **玩家显式选定的切换点** |

**LOGIN 事件不再改写它** ✅ ← 这是这次修复的核心。

### ③ 事件只响应当前用户

- **LOGOUT**：`event.userId == m_ps5_user_id` 才触发
- **LOGIN**：只记日志，不改任何状态
- **ON_RESUME**：查 `isPS5UserLoggedIn(m_ps5_user_id)`，用户还在才放行

**旁观者的事件被过滤** ✅

---

## 潜在风险点（已处理）

### ✅ 风险 1：补发的 LOGIN 事件覆盖 guest id

**已修复**：LOGIN 不改 `m_ps5_user_id`。

### ✅ 风险 2：第二次弹框时 dialog 残留冲突

**已修复**：`startPS5Login()` 开头强制清理。

### ✅ 风险 3：旁观者登出误踢玩家

**已修复**：LOGOUT 只响应 `event.userId == m_ps5_user_id`。

### ✅ 风险 4：同一用户 resume 误踢回登录页

**已修复**：resume 时查 `isPS5UserLoggedIn()`。

### ⚠️ 风险 5：换用户后被杀进程（attribute2=0）

**不是 bug**，是当前配置的行为。要解决需要：
- 改 `attribute2 = 1` **且**
- 打包安装（裸 ELF 不读 param.json）

---

## 测试建议

| # | 场景 | 预期 | 验证点 |
|---|---|---|---|
| 1 | 匿名启动 → 按 X | 弹选用户框 | `startPS5LoginDialog` 日志 |
| 2 | 选用户框 → 取消 → 提示框按 X | 第二次框能响应 O/X | 实测交互 |
| 3 | 选用户框 → 选真实用户 | 切到 SigninDialog，拿到 auth code | `updatePS5LoginDialog` → `startPS5SigninDialog` |
| 4 | 真实用户启动（已登录 PSN） | SigninDialog 秒过 | `dialog_finished` → `success` |
| 5 | 回 Home 再回来（同一用户） | 游戏继续，**不回登录页** | `isPS5UserLoggedIn` → true |
| 6 | 另一个用户登录/登出 | 游戏不受影响 | 日志有 LOGIN/LOGOUT 但无 `logout_pending` |
| 7 | 当前用户登出 | 回登录页 | `logout_pending` → `returnToLoginLevel` |

**重点是 2 和 5** —— 这两个是这次修复的直接目标。

