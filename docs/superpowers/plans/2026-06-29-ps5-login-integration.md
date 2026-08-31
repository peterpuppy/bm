# PS5 登录接入实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 Chaos 引擎和 Proven Ground 游戏中接入 PS5（Prospero）平台登录能力，复用现有 Steam/PlatformDelegate 模式，当前阶段先用占位 SDK 流程搭通客户端到登录服的完整链路。

**Architecture:** 客户端通过 `PlatformDelegate` 在 `CHAOS_PLATFORM_PROSPERO` 宏下初始化 PS5 SDK、获取用户 ID 和 auth session，存入 `ClientRoot`；Lua 登录状态机通过 `platform_delegate:getAuthSessionResponse()` 无感知透传；登录服解析 PS5 配置并新增 `chaos_login_user_ps5.lua` 作为校验占位。宏隔离、生命周期管理、配置解析均对齐现有 Steam 实现。

**Tech Stack:** C++17, Chaos Engine, PlayStation 5 SDK (sceUserService, sceNp 系列), Lua, CMake

## Global Constraints

- 所有 C++ 平台相关代码必须用 `CHAOS_PLATFORM_PROSPERO` 宏包裹，禁止在非 PS5 平台引入 PS5 SDK 头文件。
- 非 Ship 构建才允许输出详细错误日志；Ship 构建只允许记录关键失败码。
- 客户端登录状态机 Lua 层改动必须保持向后兼容，不能破坏 PC/Steam/NetEase 现有流程。
- 登录服新增平台配置解析必须放在 `LoginServerRoot` 已有 `initialize*Config` 模式内。
- 每次任务完成后必须能在当前活跃平台（Win64）编译通过；PS5 编译验证在计划末期单独说明。
- Commit message 以 `CB2N-xxxxx: ` 开头，一两行，不加 body（按项目 CLAUDE.md 约定）。

---

## File Structure

| 文件 | 职责 |
|---|---|
| `source/client/public/chaos/client/root/chaos_client_root.h` | 新增 PS5 用户凭证静态字段与 getter/setter 声明 |
| `source/client/private/chaos/client/root/chaos_client_root.cpp` | 新增 PS5 用户凭证静态字段定义与 getter/setter 实现 |
| `source/client/public/chaos/client/platform/chaos_platform_delegate.h` | 新增 `PlatformDelegate` 私有 PS5 辅助方法声明 |
| `source/client/private/chaos/client/platform/chaos_platform_delegate.cpp` | 新增 PS5 SDK 初始化、tick、析构、token 获取的 `#ifdef CHAOS_PLATFORM_PROSPERO` 实现 |
| `source/server/login_server/private/chaos/server/login_server/root/chaos_login_server_root.cpp` | 新增 `initializePS5Config` 并在主配置解析中调用 |
| `_scripts/server/login_server/login_user/chaos_login_user_ps5.lua` | 新建 PS5 登录用户校验占位类 |
| `_scripts/server/login_server/login_user/chaos_login_user_manager.lua` | 注册 PS5 平台到用户工厂 |
| `_scripts/client/game_level/chaos_client_login_level.lua` | 无改动：确认 `getAuthSessionResponse()` 透传路径 |
| `docs/superpowers/plans/2026-06-29-ps5-login-integration.md` | 本计划 |

---

## Task 1: ClientRoot 新增 PS5 用户凭证存储

**Files:**
- Modify: `source/client/public/chaos/client/root/chaos_client_root.h`
- Modify: `source/client/private/chaos/client/root/chaos_client_root.cpp`

**Interfaces:**
- Produces:
  - `static String ClientRoot::getPS5UserID()`
  - `static String ClientRoot::getPS5OnlineID()`
  - `static String ClientRoot::getPS5AuthToken()`
  - `static String ClientRoot::getPS5UserLanguage()`
  - `static Bool ClientRoot::isPS5Platform()`
  - `static void ClientRoot::setPS5UserID(const String&)`
  - `static void ClientRoot::setPS5OnlineID(const String&)`
  - `static void ClientRoot::setPS5AuthToken(const String&)`
  - `static void ClientRoot::setPS5UserLanguage(const String&)`
  - `static void ClientRoot::setPS5Platform(Bool)`

- [ ] **Step 1: 在头文件中声明字段和函数**

在 `chaos_client_root.h` 的 `m_is_cloud_game_platform` 之后、getter/setter 声明区域追加：

```cpp
static String m_ps5_user_id;
static String m_ps5_online_id;
static String m_ps5_auth_token;
static String m_ps5_user_language;
static Bool m_is_ps5_platform;
```

在 getter/setter 区域追加：

```cpp
CHAOS_STATIC_FUNCTION void setPS5UserID(const String &ps5_user_id);
CHAOS_STATIC_FUNCTION void setPS5OnlineID(const String &ps5_online_id);
CHAOS_STATIC_FUNCTION void setPS5AuthToken(const String &ps5_auth_token);
CHAOS_STATIC_FUNCTION void setPS5UserLanguage(const String &ps5_user_language);
CHAOS_STATIC_FUNCTION void setPS5Platform(Bool is_ps5_platform);
CHAOS_STATIC_FUNCTION String getPS5UserID();
CHAOS_STATIC_FUNCTION String getPS5OnlineID();
CHAOS_STATIC_FUNCTION String getPS5AuthToken();
CHAOS_STATIC_FUNCTION String getPS5UserLanguage();
CHAOS_STATIC_FUNCTION Bool isPS5Platform();
```

- [ ] **Step 2: 在 cpp 中定义静态字段并初始化**

在 `chaos_client_root.cpp` 的现有静态字段定义区追加：

```cpp
String ClientRoot::m_ps5_user_id;
String ClientRoot::m_ps5_online_id;
String ClientRoot::m_ps5_auth_token;
String ClientRoot::m_ps5_user_language;
Bool ClientRoot::m_is_ps5_platform = k_false;
```

- [ ] **Step 3: 实现 getter/setter**

在 `chaos_client_root.cpp` 的现有 getter/setter 实现区追加：

```cpp
void ClientRoot::setPS5UserID(const String &ps5_user_id)
{
    m_ps5_user_id = ps5_user_id;
}

void ClientRoot::setPS5OnlineID(const String &ps5_online_id)
{
    m_ps5_online_id = ps5_online_id;
}

void ClientRoot::setPS5AuthToken(const String &ps5_auth_token)
{
    m_ps5_auth_token = ps5_auth_token;
}

void ClientRoot::setPS5UserLanguage(const String &ps5_user_language)
{
    m_ps5_user_language = ps5_user_language;
}

void ClientRoot::setPS5Platform(Bool is_ps5_platform)
{
    m_is_ps5_platform = is_ps5_platform;
}

String ClientRoot::getPS5UserID()
{
    return m_ps5_user_id;
}

String ClientRoot::getPS5OnlineID()
{
    return m_ps5_online_id;
}

String ClientRoot::getPS5AuthToken()
{
    return m_ps5_auth_token;
}

String ClientRoot::getPS5UserLanguage()
{
    return m_ps5_user_language;
}

Bool ClientRoot::isPS5Platform()
{
    return m_is_ps5_platform;
}
```

- [ ] **Step 4: Win64 编译验证**

Run: `cd /h/cb2/dev/chaos && build_scripts/build.bat --target Client_Profile`（或当前常用构建命令）
Expected: 编译通过，无新 warning。

- [ ] **Step 5: Commit**

```bash
cd /h/cb2/dev/chaos
git add source/client/public/chaos/client/root/chaos_client_root.h
 git add source/client/private/chaos/client/root/chaos_client_root.cpp
git commit -m "CB2N-xxxxx: ClientRoot 增加 PS5 用户凭证字段"
```

---

## Task 2: PlatformDelegate 接入 PS5 SDK 占位流程

**Files:**
- Modify: `source/client/public/chaos/client/platform/chaos_platform_delegate.h`
- Modify: `source/client/private/chaos/client/platform/chaos_platform_delegate.cpp`

**Interfaces:**
- Consumes:
  - `ClientRoot::setPS5Platform(Bool)`
  - `ClientRoot::setPS5UserID(const String&)`
  - `ClientRoot::setPS5OnlineID(const String&)`
  - `ClientRoot::setPS5AuthToken(const String&)`
  - `ClientRoot::setPS5UserLanguage(const String&)`
  - `ClientRoot::isPS5Platform()`
  - `ClientRoot::getPS5AuthToken()`
- Produces:
  - `Bool PlatformDelegate::initialize()` 在 PS5 下调用 SDK 初始化
  - `void PlatformDelegate::tick(Float)` 在 PS5 下调用 SDK tick
  - `void PlatformDelegate::clear()` 在 PS5 下调用 SDK 清理
  - `Int PlatformDelegate::getAuthSessionResponse()` 在 PS5 下返回 token 长度或状态码

- [ ] **Step 1: 头文件新增私有辅助方法**

在 `chaos_platform_delegate.h` 的 `private:` 区域追加：

```cpp
#if defined(CHAOS_PLATFORM_PROSPERO)
Bool initializePS5();
void finalizePS5();
void tickPS5(Float delta_time);
Bool refreshPS5AuthSession();
Bool m_ps5_initialized{k_false};
#endif
```

- [ ] **Step 2: cpp 顶部包含 PS5 SDK 头文件（仅 PROSPERO）**

在 `chaos_platform_delegate.cpp` 的 include 区域追加到最底部（现有 Steam include 之后）：

```cpp
#if defined(CHAOS_PLATFORM_PROSPERO)
#include <libsysmodule.h>
#include <user_service.h>
#include <np.h>
#include <np_auth.h>
#include <sdk_version.h>
#endif
```

- [ ] **Step 3: 实现 initialize() 中的 PS5 分支**

在 `PlatformDelegate::initialize()` 函数末尾、`return k_true;` 之前追加：

```cpp
#if defined(CHAOS_PLATFORM_PROSPERO)
if (initializePS5() == k_false)
{
    LOG_ERROR(__FUNCTION__, "initializePS5 failed!");
    return k_false;
}
#endif
```

- [ ] **Step 4: 实现 tick() 中的 PS5 分支**

在 `PlatformDelegate::tick(Float delta_time)` 的 `#ifdef CHAOS_PLATFORM_WIN32 SteamAPI_RunCallbacks(); #endif` 之后追加：

```cpp
#if defined(CHAOS_PLATFORM_PROSPERO)
tickPS5(delta_time);
#endif
```

- [ ] **Step 5: 实现 clear() 中的 PS5 分支**

在 `PlatformDelegate::clear()` 中追加：

```cpp
#if defined(CHAOS_PLATFORM_PROSPERO)
finalizePS5();
#endif
```

- [ ] **Step 6: 实现 PS5 私有辅助方法**

在 `chaos_platform_delegate.cpp` 文件底部追加：

```cpp
#if defined(CHAOS_PLATFORM_PROSPERO)
Bool PlatformDelegate::initializePS5()
{
    // 占位：初始化 UserService 和 Np
    int ret = sceUserServiceInitialize(nullptr);
    if (ret != SCE_OK)
    {
        LOG_ERROR(__FUNCTION__, "sceUserServiceInitialize failed: {0}", String::format("{0}", ret));
        return k_false;
    }

    ret = sceNpInitialize(SCE_SDK_VERSION_MAJOR);
    if (ret != SCE_OK)
    {
        LOG_ERROR(__FUNCTION__, "sceNpInitialize failed: {0}", String::format("{0}", ret));
        return k_false;
    }

    ClientRoot::setPS5Platform(k_true);

    // 占位：获取本地用户 ID 和在线 ID
    SceUserServiceUserId user_id = SCE_USER_SERVICE_USER_ID_INVALID;
    ret = sceUserServiceGetInitialUser(&user_id);
    if (ret == SCE_OK && user_id != SCE_USER_SERVICE_USER_ID_INVALID)
    {
        ClientRoot::setPS5UserID(String::format("{0}", static_cast<Int>(user_id)));
    }

    refreshPS5AuthSession();
    return k_true;
}

void PlatformDelegate::finalizePS5()
{
    if (!m_ps5_initialized)
    {
        return;
    }
    // 占位：关闭 Np 和 UserService
    sceNpTerminate();
    sceUserServiceTerminate();
    m_ps5_initialized = k_false;
    ClientRoot::setPS5Platform(k_false);
}

void PlatformDelegate::tickPS5(Float /*delta_time*/)
{
    if (!m_ps5_initialized)
    {
        return;
    }
    // 占位：轮询 Np 状态、刷新 token 过期
}

Bool PlatformDelegate::refreshPS5AuthSession()
{
    if (!ClientRoot::isPS5Platform())
    {
        return k_false;
    }

    // 占位：调用 sceNpAuth 系列接口获取 ID token
    // 当前先用 online_id 填充 auth_token，供 Lua 透传占位
    ClientRoot::setPS5AuthToken(ClientRoot::getPS5OnlineID());
    m_ps5_initialized = k_true;
    return k_true;
}
#endif
```

- [ ] **Step 7: 修改 getAuthSessionResponse() 支持 PS5**

把 `getAuthSessionResponse()` 的实现改成：

```cpp
Int PlatformDelegate::getAuthSessionResponse()
{
#if defined(CHAOS_PLATFORM_WIN32)
    if (ClientRoot::isSteamPlatform())
    {
        String token = ClientRoot::getSteamUserToken();
        return static_cast<Int>(token.getLength());
    }
#elif defined(CHAOS_PLATFORM_PROSPERO)
    if (ClientRoot::isPS5Platform())
    {
        String token = ClientRoot::getPS5AuthToken();
        return static_cast<Int>(token.getLength());
    }
#endif
    return 0;
}
```

- [ ] **Step 8: Win64 编译验证**

Run: `cd /h/cb2/dev/chaos && build_scripts/build.bat --target Client_Profile`
Expected: 编译通过。`CHAOS_PLATFORM_PROSPERO` 分支在 Win64 下被完全编译掉。

- [ ] **Step 9: Commit**

```bash
cd /h/cb2/dev/chaos
git add source/client/public/chaos/client/platform/chaos_platform_delegate.h
 git add source/client/private/chaos/client/platform/chaos_platform_delegate.cpp
git commit -m "CB2N-xxxxx: PlatformDelegate 接入 PS5 SDK 占位流程"
```

---

## Task 3: 登录服新增 PS5 配置解析

**Files:**
- Modify: `source/server/login_server/private/chaos/server/login_server/root/chaos_login_server_root.cpp`

**Interfaces:**
- Produces:
  - `void LoginServerRoot::initializePS5Config(XMLNode* ps5_node)`

- [ ] **Step 1: 在头文件声明新方法**

Modify `source/server/login_server/public/chaos/server/login_server/root/chaos_login_server_root.h`，在现有 `initializeSteamConfig` 等声明附近追加：

```cpp
void initializePS5Config(XMLNode* ps5_node);
```

- [ ] **Step 2: 在 cpp 实现配置解析**

在 `chaos_login_server_root.cpp` 的 `initializeSteamConfig` 实现之后追加：

```cpp
void LoginServerRoot::initializePS5Config(XMLNode* ps5_node)
{
    CHAOS_RETURN_IF_NULL(ps5_node);

    String server_addr = ps5_node->getStringAttribute("server_addr", "");
    Int server_port = ps5_node->getIntAttribute("server_port", 0);
    Bool enabled = ps5_node->getBoolAttribute("enabled", k_false);

    g_login_server_global_context.m_config_accessor->initializePS5(server_addr, server_port, enabled);

    LOG_INFO(__FUNCTION__, "PS5 config loaded: enabled={0}, addr={1}:{2}",
             String::format("{0}", enabled),
             server_addr,
             String::format("{0}", server_port));
}
```

- [ ] **Step 3: 在主配置解析中调用**

在 `chaos_login_server_root.cpp` 中搜索 `XMLNode* steam_node = ...` 或类似平台节点解析位置，在 Steam 节点解析之后追加：

```cpp
XMLNode* ps5_node = platform_node->getChildNode("ps5");
if (ps5_node != nullptr)
{
    initializePS5Config(ps5_node);
}
```

- [ ] **Step 4: 在 ConfigAccessor 声明中占位（如尚未存在）**

如果 `LoginServerConfigAccessor` 没有 `initializePS5`，在 `source/server/login_server/public/chaos/server/login_server/config/chaos_login_server_config_accessor.h` 中追加：

```cpp
void initializePS5(const String& server_addr, Int server_port, Bool enabled);
```

并在对应 cpp 中追加空实现：

```cpp
void LoginServerConfigAccessor::initializePS5(const String& server_addr, Int server_port, Bool enabled)
{
    m_ps5_server_addr = server_addr;
    m_ps5_server_port = server_port;
    m_ps5_enabled = enabled;
}
```

同时在头文件中追加成员：

```cpp
String m_ps5_server_addr;
Int m_ps5_server_port{0};
Bool m_ps5_enabled{k_false};
```

- [ ] **Step 5: Win64 编译验证**

Run: `cd /h/cb2/dev/chaos && build_scripts/build.bat --target LoginServer_Profile`
Expected: 编译通过。

- [ ] **Step 6: Commit**

```bash
cd /h/cb2/dev/chaos
git add source/server/login_server/public/chaos/server/login_server/root/chaos_login_server_root.h
git add source/server/login_server/private/chaos/server/login_server/root/chaos_login_server_root.cpp
git add source/server/login_server/public/chaos/server/login_server/config/chaos_login_server_config_accessor.h
git add source/server/login_server/private/chaos/server/login_server/config/chaos_login_server_config_accessor.cpp
git commit -m "CB2N-xxxxx: 登录服新增 PS5 配置解析"
```

---

## Task 4: 登录服新增 PS5 登录用户类

**Files:**
- Create: `_scripts/server/login_server/login_user/chaos_login_user_ps5.lua`
- Modify: `_scripts/server/login_server/login_user/chaos_login_user_manager.lua`

**Interfaces:**
- Consumes:
  - 基类 `LoginUserBase` 的生命周期和 stage machine
  - 登录服 config accessor 的 `m_ps5_enabled` / `m_ps5_server_addr` / `m_ps5_server_port`
- Produces:
  - `LoginUserPS5` 类，继承 `LoginUserBase`
  - 工厂中 `account_platform == "ps5"` 的分支

- [ ] **Step 1: 创建 PS5 登录用户类**

Create `_scripts/server/login_server/login_user/chaos_login_user_ps5.lua`：

```lua
require("server/login_server/login_user/chaos_login_user_base");

LoginUserPS5 = class(LoginUserBase);

function LoginUserPS5:__init__(rpc_identify_id, account_platform)
    self.super.__init__(self, rpc_identify_id, account_platform);
end

function LoginUserPS5:requestAccountInfo()
    -- 占位：PS5 平台校验流程
    -- 实际应把 auth_token 发到 PSN/Np 校验服务，确认用户合法后回写 account_id
    local config_accessor = g_lua_login_server_global_context.m_config_accessor;
    if config_accessor.m_ps5_enabled ~= k_true then
        self:notifyLoginFailed("ps5_platform_disabled", "");
        self:setLoginStage(LoginStageType.failed);
        return;
    end

    local params_table = ParseUrlParams(self.m_auth_token);
    local online_id = params_table["online_id"] or self.m_auth_token;

    -- 占位：用 online_id 直接作为 account_id
    self.m_user_name = online_id;
    self.m_password = self.m_auth_token;
    self.m_account_id = online_id;

    self:requestPreLanding();
end
```

- [ ] **Step 2: 在工厂中注册 PS5 分支**

Modify `_scripts/server/login_server/login_user/chaos_login_user_manager.lua`，在创建 `LoginUserSteam` / `LoginUserNetease` 等分支的 `if/elseif` 链中追加：

```lua
elseif account_platform == STRING_ID("ps5") then
    login_user = LoginUserPS5(rpc_identify_id, account_platform);
```

- [ ] **Step 3: Commit**

```bash
cd /h/cb2/dev/wolfgang/_games/proven_ground
git add _scripts/server/login_server/login_user/chaos_login_user_ps5.lua
git add _scripts/server/login_server/login_user/chaos_login_user_manager.lua
git commit -m "CB2N-xxxxx: 登录服新增 PS5 登录用户占位类"
```

---

## Task 5: Lua 客户端确认透传路径

**Files:**
- Read-only: `_scripts/client/game_level/chaos_client_login_level.lua`

**Interfaces:**
- 确认 `platform_delegate:getAuthSessionResponse()` 返回值在 PS5 分支被正确发送到登录服。

- [ ] **Step 1: 检查 gateway_connected 状态的 auth session 发送逻辑**

在 `_scripts/client/game_level/chaos_client_login_level.lua` 中定位 `ClientLoginLevelStatus.gateway_connected` 处理（约第 1024 行）。确认代码逻辑：

```lua
local platform_delegate = g_client_global_context:get_m_platform_delegate();
local auth_session_response = platform_delegate:getAuthSessionResponse();
```

并确认 `RequestLanding` RPC 调用时把 `auth_session_response` 作为参数发出。

- [ ] **Step 2: 如需在 Lua 层识别 PS5 平台，添加 accessor 方法**

如果 UI 需要在 PS5 下隐藏用户名/密码输入框，修改 `source/client/private/chaos/client/lua/chaos_client_lua_accessor.cpp`（对应头文件 `source/client/public/chaos/client/lua/chaos_client_lua_accessor.h`）新增：

```cpp
Bool ClientLuaAccessor::isPS5Platform()
{
#if defined(CHAOS_PLATFORM_PROSPERO)
    return ClientRoot::isPS5Platform();
#else
    return k_false;
#endif
}
```

并在 Lua 绑定中注册（按现有 `isSteamPlatform` 绑定方式）。

- [ ] **Step 3: Commit（如添加了 accessor）**

```bash
cd /h/cb2/dev/chaos
git add source/client/public/chaos/client/lua/chaos_client_lua_accessor.h
 git add source/client/private/chaos/client/lua/chaos_client_lua_accessor.cpp
git commit -m "CB2N-xxxxx: Lua accessor 增加 isPS5Platform"
```

---

## Task 6: 配置示例与文档

**Files:**
- Create: `docs/superpowers/plans/2026-06-29-ps5-login-integration-config-example.xml`

- [ ] **Step 1: 提供登录服配置示例**

Create `docs/superpowers/plans/2026-06-29-ps5-login-integration-config-example.xml`：

```xml
<platform>
    ...
    <ps5 enabled="true" server_addr="np.service.example.com" server_port="443"/>
</platform>
```

- [ ] **Step 2: 在计划文档末尾追加后续待填项**

在 `docs/superpowers/plans/2026-06-29-ps5-login-integration.md` 末尾追加：

```markdown
## 后续待填（SDK 确定后）

1. 替换 `PlatformDelegate::refreshPS5AuthSession()` 中的占位逻辑为真实 `sceNpAuth*` 调用。
2. 实现 `LoginUserPS5:requestAccountInfo()` 中的 PSN 校验 HTTP/RPC 请求。
3. 处理 PS5 用户切换、账号登出、token 过期刷新。
4. 联调 PS5 devkit 上的完整登录链路。
```

- [ ] **Step 3: Commit**

```bash
cd /h/cb2/dev/chaos
git add docs/superpowers/plans/2026-06-29-ps5-login-integration-config-example.xml
git add docs/superpowers/plans/2026-06-29-ps5-login-integration.md
git commit -m "CB2N-xxxxx: PS5 登录配置示例与计划文档"
```

---

## Verification

### Win64 编译验证

1. 每个 Task 完成后分别编译 Client 和 LoginServer（Profile）。
2. 全局 grep 检查：

```bash
cd /h/cb2/dev/chaos
grep -R "sceNp\|sceUserService\|libsysmodule" --include="*.cpp" --include="*.h" source/ | grep -v "CHAOS_PLATFORM_PROSPERO"
```

Expected: 没有任何结果；所有 PS5 SDK 头文件和 API 都必须在 `CHAOS_PLATFORM_PROSPERO` 宏内。

### 运行时验证（Win64 占位路径）

1. 启动 Win64 客户端，进入登录界面。
2. 调用 `g_client_global_context:get_m_platform_delegate():getAuthSessionResponse()`，确认在 Win64 返回 `0`。
3. 确认 Lua 登录状态机不受影响，Steam/NetEase 登录仍可用。

### PS5 验证（需要 devkit / Prospero 构建环境）

1. 切换 Chaos 到 Prospero Profile 构建。
2. 确认 `PlatformDelegate::initializePS5()` 被调用且 `m_ps5_initialized` 置 true。
3. 在 devkit 上运行，确认 `ClientRoot::isPS5Platform()` 返回 true。
4. 查看日志输出 `PS5 user_id = ...`，确认 `RequestLanding` 把 auth token 发到登录服。
5. 登录服确认收到 `account_platform == "ps5"`，并创建 `LoginUserPS5` 实例。

---

## Risks

1. **PS5 SDK API 未最终确定**：当前 `sceNpInitialize` / `sceNpAuth*` 等函数名为占位，需在 SDK 版本确认后替换。
2. **初始用户选择**：`sceUserServiceGetInitialUser` 只适用于单用户场景；多用户手柄切换需要额外处理。
3. **Token 生命周期**：当前 `refreshPS5AuthSession` 是一次性的，未处理过期刷新。
4. **Ship 构建日志**：Ship 构建下需移除或降级 LOG_ERROR 中的错误码输出。
5. **跨平台宏遗漏**：新增文件或 cpp 中若忘记 `#ifdef CHAOS_PLATFORM_PROSPERO` 会导致 Win64 编译失败。
