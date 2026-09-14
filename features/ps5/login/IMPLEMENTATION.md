# PS5 登录实现细节（CB2N-27968）

> 本文档记录 PS5 登录从客户端到登录服的完整实现。所有路径基于：
> - Chaos 引擎：`H:\cb2\dev\chaos\_source\_engine`
> - Proven Ground：`H:\cb2\dev\wolfgang\_games\proven_ground\_source`

---

## 1. 整体架构

复用现有 Steam/PlatformDelegate 模式：

1. **C++ 客户端**在 `PlatformDelegate::initialize()` 中识别到 PS5 平台时，加载 PS5 SDK 模块并请求 authorization code。
2. 拿到的 code 与 issuer_id 存入 `ClientRoot` 静态字段。
3. **Lua 客户端**通过 `platform_delegate:getPS5AuthToken()` / `getPS5IssuerID()` 读取，拼成 `"issuer_id|auth_code"` 放入登录 RPC 的 `password` 字段。
4. **登录服**收到后，由 `LoginUserPS5` 解析、按 issuer_id 选环境、用 Client ID + Client Secret 调 PSN Auth Web API 换 token，再用 token 取 `account_id`，最后用 `account_id` 走游戏账号登录。

> 没有修改生成的 RPC schema，复用现有 `CLT2LGNRequestLogin` 的 `password` 字段做透传。

---

## 2. Chaos 引擎 C++ 层

### 2.1 PlatformDelegate 异步获取 authorization code

文件：`source/client/private/chaos/client/platform/chaos_platform_delegate.cpp`

关键流程（仅 `CHAOS_PLATFORM_PROSPERO`）：

```cpp
// 加载模块
sceSysmoduleLoadModule(SCE_SYSMODULE_SIGNIN_DIALOG);
sceSysmoduleLoadModule(SCE_SYSMODULE_NP_AUTH);

// 取初始用户
SceUserServiceUserId user_id;
sceUserServiceGetInitialUser(&user_id);

// 初始化并打开系统登录对话框；已登录用户会立即 FINISHED/OK
SceSigninDialogParam param;
sceSigninDialogParamInitialize(&param);
param.userId = user_id;
sceSigninDialogOpen(&param);

// 每帧 tick() 中轮询
while (sceSigninDialogUpdateStatus() != SCE_SIGNIN_DIALOG_STATUS_FINISHED) {
    // wait
}
SceSigninDialogResult result;
sceSigninDialogGetResult(&result);
if (result.result == SCE_SIGNIN_DIALOG_RESULT_OK) {
    // 调 sceNpAuthGetAuthorizationCodeV3() 拿 code
}
```

`PlatformDelegate` 内部状态机（`PS5SigninDialogState`）：

- `none` → `waiting_dialog`：打开对话框后
- `waiting_dialog` → `dialog_finished`：`sceSigninDialogUpdateStatus()` 返回 FINISHED
- `dialog_finished` → `auth_fetching`：用户确认/已登录，准备调 NpAuth
- `auth_fetching` → `success`/`failed`：`sceNpAuthGetAuthorizationCodeV3()` 结果

对话框结果存入 `ClientRoot`：

```cpp
ClientRoot::setPS5AuthToken(String(auth_code.code));
ClientRoot::setPS5IssuerID(static_cast<Int>(issuer_id));
```

### 2.2 ClientRoot 字段

文件：`source/client/public/chaos/client/root/chaos_client_root.h`

新增静态字段：

```cpp
static String m_ps5_user_id;
static String m_ps5_auth_token;
static Int m_ps5_issuer_id;
static Bool m_is_ps5_platform;
```

新增 getter/setter（`CHAOS_STATIC_FUNCTION`）：

```cpp
CHAOS_STATIC_FUNCTION void setPS5UserID(const String &ps5_user_id);
CHAOS_STATIC_FUNCTION void setPS5AuthToken(const String &ps5_auth_token);
CHAOS_STATIC_FUNCTION void setPS5IssuerID(Int issuer_id);
CHAOS_STATIC_FUNCTION void setPS5Platform(Bool is_ps5_platform);
CHAOS_STATIC_FUNCTION String getPS5UserID();
CHAOS_STATIC_FUNCTION String getPS5AuthToken();
CHAOS_STATIC_FUNCTION Int getPS5IssuerID();
CHAOS_STATIC_FUNCTION Bool isPS5Platform();
```

### 2.3 Lua 绑定

文件：
- `source/client/public/chaos/client/script/lua/chaos_client_lua_accessor.h`
- `source/client/private/chaos/client/script/lua/chaos_client_lua_accessor.cpp`

在 `Meta(CLASS_FUNCTION_METADATA_REGISTER)` 块中新增：

```cpp
.addFunction("getPS5AuthToken", &PlatformDelegate::getPS5AuthToken)
.addFunction("getPS5IssuerID", &PlatformDelegate::getPS5IssuerID)
.addFunction("isPS5Platform", &PlatformDelegate::isPS5Platform)
```

`PlatformDelegate` 内部转发到 `ClientRoot`：

```cpp
String PlatformDelegate::getPS5AuthToken() const
{
    return ClientRoot::getPS5AuthToken();
}
```

### 2.4 CMake 链接

文件：`source/client/CMakeLists.txt`

在 Prospero 平台段追加：

```cmake
list(APPEND SYS_LINK_TARGETS libSceNpAuth_stub_weak.a libSceSigninDialog_stub_weak.a)
```

---

## 3. Proven Ground Lua 客户端

文件：`_scripts/client/game_level/chaos_client_login_level.lua`

在 `loginAndGetAccountAccessToken` 中新增 PS5 分支：

```lua
if platform_delegate:isPS5Platform() then
    local ps5_auth_code = platform_delegate:getPS5AuthToken();
    local ps5_issuer_id = platform_delegate:getPS5IssuerID();
    if ps5_auth_code == nil or ps5_auth_code == "" then
        LOG_ERROR("[PS5] auth code is empty, signin dialog may not be finished");
        return;
    end

    self.m_real_username = "ps5_" .. tostring(ps5_issuer_id);  -- 占位，最终用 account_id
    self.m_access_token = tostring(ps5_issuer_id) .. "|" .. ps5_auth_code;
    -- 继续走现有登录 RPC，access_token/password 会被带上
    return;
end
```

> 注意：当 authorization code 由 `sceNpAuthGetAuthorizationCodeV3()` 获取时，Auth Web API 文档要求 `redirect_uri` 固定为 `orbis://games`，不是普通 HTTPS URL。

---

## 4. Proven Ground 登录服

### 4.1 登录用户枚举

文件：`_scripts/server/login_server/login_user/chaos_login_user_base.lua`

新增：

```lua
LoginHttpRequestType.ps5_auth = 35;
LoginHttpRequestType.ps5_userinfo = 36;
```

### 4.2 LoginUserPS5

文件：~~`_scripts/server/login_server/login_user/chaos_login_user_ps5.lua`~~ **已删除**
（登录改走 GAC，见 [STATUS.md](STATUS.md) 与 [docs/game_account_center.md](docs/game_account_center.md)）

主要流程：

```lua
function LoginUserPS5:requestLogin()
    self.m_current_login_status = AccountLoginStatus.auth;

    -- password 格式：issuer_id|auth_code
    local sep_pos = string.find(self.m_password, "|");
    if not sep_pos then
        self:onLoginFailed(STRING_ID("login_failed_invalid_params"));
        return;
    end

    local issuer_id_str = string.sub(self.m_password, 1, sep_pos - 1);
    local auth_code = string.sub(self.m_password, sep_pos + 1);
    local issuer_id = tonumber(issuer_id_str);

    local endpoint = self:getEndpointByIssuerID(issuer_id);
    if endpoint == nil then
        self:onLoginFailed(STRING_ID("login_failed_invalid_params"));
        return;
    end

    -- 1. 换 token
    local token_url = endpoint .. "/v3/oauth/token";
    local basic_auth = self:base64Encode(k_ps5_client_id .. ":" .. k_ps5_client_secret);
    -- 注意：code 来自 sceNpAuthGetAuthorizationCodeV3() 时，redirect_uri 必须是 "orbis://games"
    local token_body = "grant_type=authorization_code&code=" .. self:urlEncode(auth_code) ..
                       "&redirect_uri=" .. self:urlEncode("orbis://games") ..
                       "&scope=psn:s2s openid id_token:psn.basic_claims";
    self:sendHttpRequest(LoginHttpRequestType.ps5_auth, token_url, "POST",
        { ["Authorization"] = "Basic " .. basic_auth,
          ["Content-Type"] = "application/x-www-form-urlencoded" },
        token_body);
end

function LoginUserPS5:processResponsedHttpRequest(http_request, response_code, response_context)
    if http_request.m_request_type == LoginHttpRequestType.ps5_auth then
        -- 解析 access_token，继续调 userinfo
    elseif http_request.m_request_type == LoginHttpRequestType.ps5_userinfo then
        -- 解析 account_id，设置 m_user_name，进入 requestAccountInfo
    end
end
```

### 4.3 环境 endpoint 映射（PS5 S2S Auth Web API v3）

```lua
local k_ps5_endpoints = {
    [1]   = "https://s2s.sp-int.playstation.net/api/authz",   -- 研发
    [8]   = "https://s2s.prod-qa.playstation.net/api/authz",  -- 认证
    [256] = "https://s2s.np.playstation.net/api/authz",       -- 生产
};
```

Token：`{endpoint}/v3/oauth/token`；UserInfo：`{endpoint}/v3/oauth/userinfo`。

---

## 5. 数据流时序

```
PS5 DevKit
  ├─ SigninDialog / NpAuth PRX 加载
  ├─ sceUserServiceGetInitialUser()
  ├─ sceSigninDialogInitialize()
  ├─ sceSigninDialogOpen(userId)        ← 未登录用户弹系统登录框；已登录立即 FINISHED/OK
  │
  ▼ 每帧 tick()
  ├─ sceSigninDialogUpdateStatus()      → FINISHED
  ├─ sceSigninDialogGetResult()         → SCE_SIGNIN_DIALOG_RESULT_OK
  ├─ sceNpAuthCreateRequest()
  ├─ sceNpAuthGetAuthorizationCodeV3(scope="psn:s2s openid id_token:psn.basic_claims")
  │     → auth_code, issuer_id
  │
  ▼
ClientRoot::setPS5AuthToken(code)
ClientRoot::setPS5IssuerID(id)
  │
  ▼
Lua: platform_delegate:getPS5AuthToken() / getPS5IssuerID()
  │
  ▼
chaos_client_login_level.lua
  password = issuer_id .. "|" .. auth_code
  → RPC RequestLanding / CLT2LGNRequestLogin
  │
  ▼
LoginUserPS5
  ├─ 解析 issuer_id|auth_code
  ├─ POST https://s2s.<env>.playstation.net/api/authz/v3/oauth/token
  │     Authorization: Basic base64(ClientID:Secret)
  │     → access_token
  │
  ▼
  ├─ GET https://s2s.<env>.playstation.net/api/authz/v3/oauth/userinfo
  │     Authorization: Bearer access_token
  │     → account_id, online_id
  │
  ▼
  m_user_name = account_id
  → 游戏账号查询 / 预着陆
```

---

## 6. 调试与验证

### 客户端日志

- 确认 `PlatformDelegate::initializePS5()` 执行。
- 确认 `sceSigninDialogOpen()` 成功打开对话框；已登录环境下应迅速 FINISHED/OK。
- 确认 `sceSigninDialogGetResult()` 返回 `SCE_SIGNIN_DIALOG_RESULT_OK`。
- 确认 `sceNpAuthGetAuthorizationCodeV3` 返回成功，`auth_code` 非空。
- 确认 Lua 读取到 `getPS5AuthToken()` 有值。

### 登录服日志

- 确认 `LoginUserPS5` 被创建。
- 确认 `/v3/oauth/token` 返回 200 且含 `access_token`。
- 确认 `/v3/oauth/userinfo` 返回 200 且含 `account_id`。
- 确认 `m_user_name` 被设为 `account_id` 后进入 `requestAccountInfo`。

---

## 7. 后续改造点

1. **配置化凭据**：把 Client ID / Secret 移到登录服配置表或 KMS。
2. **多环境配置**：issuer_id → endpoint 的映射也走配置。
3. **Refresh token**：在 `account_center_verify` 失败后尝试 refresh。
4. **用户事件**：监听 `sceUserServiceEvent` 处理切换用户、登出。
5. **Redirect URL**：与 DevNet 注册保持一致，或在 S2S 流程中明确不需要回调。
