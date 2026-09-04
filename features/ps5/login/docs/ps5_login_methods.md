# PS5 登录方案对比（CB2N-27968）

> 本文档说明 PS5 平台两种可落地的登录验证方案，并给出本项目的选型建议。
>
> 相关实现：
> - 客户端：`H:\cb2\dev\chaos\_source\_engine\source\client\private\chaos\client\platform\chaos_platform_delegate.cpp`
> - 登录服：`H:\cb2\dev\wolfgang\_games\proven_ground\_source\_scripts\server\login_server\login_user\chaos_login_user_ps5.lua`

---

## 结论先行

**本项目（联机游戏，需要创建/绑定游戏账号并复用 PSN 服务）应使用 S2S Authorization Code 方案。**

ID Token 方案只适合做“身份校验”，无法直接拿到 access_token 调用 PSN Web API，也不方便后续 refresh token 续期。

---

## 方案一：S2S Authorization Code（当前使用）

### 适用场景

- 需要创建或绑定游戏内账号。
- 登录服需要拿到稳定的 `account_id`。
- 后续需要调 PSN Web API（好友、奖杯、排行榜、匹配等）。
- 需要 refresh_token 做长会话续期。

### 数据流

```text
[PS5 DevKit]
  ├─ 加载 SigninDialog + NpAuth PRX
  ├─ sceUserServiceGetInitialUser() → user_id
  ├─ sceSigninDialogOpen(user_id)        ← 未登录弹系统登录框；已登录立即 FINISHED/OK
  ├─ 每帧 sceSigninDialogUpdateStatus() 轮询
  ├─ sceSigninDialogGetResult() == SCE_SIGNIN_DIALOG_RESULT_OK
  │
  ├─ sceNpAuthCreateRequest()
  ├─ sceNpAuthGetAuthorizationCodeV3(
  │       scope = "psn:s2s openid id_token:psn.basic_claims"
  │   ) → auth_code + issuer_id
  │
  └─ 把 "issuer_id|auth_code" 放入 CLT2LGNRequestLogin.password 发给登录服

[登录服]
  ├─ 解析 issuer_id|auth_code
  ├─ POST https://s2s.<env>.playstation.net/api/authz/v3/oauth/token
  │     Authorization: Basic base64(ClientID:ClientSecret)
  │     grant_type=authorization_code&code=...&scope=psn:s2s openid id_token:psn.basic_claims
  │     → access_token (+ refresh_token + id_token)
  │
  ├─ GET https://s2s.<env>.playstation.net/api/authz/v3/oauth/userinfo
  │     Authorization: Bearer access_token
  │     → account_id, online_id, ...
  │
  └─ 用 account_id 创建/查询/绑定游戏账号
```

### 优点

- 登录服持有 access_token，可随时调用 PSN Web API。
- refresh_token 可续期，适合长在线联机游戏。
- `account_id` 由 PSN 返回，稳定唯一，适合作为游戏账号绑定键。

### 缺点

- 需要登录服能访问 PSN S2S endpoint。
- Client Secret 必须部署在服务端，需安全存储。
- 每次登录多两次 PSN 网络往返。

### 关键 SDK API

- `sceNpAuthCreateRequest()` / `sceNpAuthGetAuthorizationCodeV3()`
- `SceNpAuthGetAuthorizationCodeParameterV3`
- `SceNpAuthorizationCode`

---

## 方案二：ID Token（仅身份校验）

### 适用场景

- 只需要验证“这是哪个 PSN 用户”，不需要后续调 PSN Web API。
- 不想在登录服维护 Client Secret。
- 服务器只负责校验 JWT 签名，不依赖 PSN 实时网络。

### 数据流

```text
[PS5 DevKit]
  ├─ 加载 SigninDialog + NpAuth PRX
  ├─ 登录/校验完成后
  ├─ sceNpAuthGetIdTokenV3(
  │       clientId, clientSecret,
  │       scope = "openid id_token:psn.basic_claims"
  │   ) → id_token (JWT)
  │
  └─ 把 id_token 发给登录服

[登录服]
  ├─ 从 id_token 中解析 header 拿 kid
  ├─ 缓存/获取 PSN JWKs 公钥
  ├─ 验证 JWT 签名、exp、iss、aud
  └─ 从 payload.sub 取 account_id，创建/查询游戏账号
```

### 优点

- 登录服不需要 Client Secret。
- 登录服不一定需要实时访问 PSN（只要缓存了 JWKs）。
- 单次网络往返更少。

### 缺点

- **拿不到 access_token**，无法调用其他 PSN Web API。
- 需要自行实现 JWT/JWKs 验证。
- 不方便做 refresh token 续期；要重新拿 id_token。
- 若后续要调好友/奖杯等服务，仍需回到 S2S 方案或额外再拿 token。

### 关键 SDK API

- `sceNpAuthGetIdTokenV3()`
- `SceNpAuthGetIdTokenParameterV3`
- `SceNpIdToken`

---

## 为什么本项目选 S2S

| 需求 | S2S | ID Token |
|---|---|---|
| 创建/绑定游戏账号 | ✅ 登录服拿 account_id 直接写库 | ✅ 也能拿到 account_id |
| 后续调用 PSN Web API | ✅ 登录服持有 access_token | ❌ 没有 access_token |
| refresh token 续期 | ✅ 标准 OAuth refresh | ❌ 需重新调 SDK 拿 id_token |
| 联机会话长期保持 | ✅ 适合 | ⚠️ 不太自然 |
| 服务端安全 | ⚠️ 需保管 Client Secret | ✅ 不需要 Client Secret |

对于联机游戏，**S2S 是唯一能从登录服侧持续使用 PSN 服务的方案**，所以选它。

---

## 原始 PS5 文档参考

见 [ps5_sdk_reference_links.md](ps5_sdk_reference_links.md)。

---

## 安全提示

- Client Secret 只能存在于登录服，禁止写入客户端或提交 git。
- 当前 `chaos_login_user_ps5.lua` 中硬编码的 Client Secret 仅用于研发测试，生产前必须轮换并迁出代码。
- PS5 SDK 文档受 NDA 保护，不要上传到在线服务或公开仓库。
