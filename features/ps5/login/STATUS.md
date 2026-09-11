# PS5 登录 — 进度

> **最后更新**：2026-09-07（从 `features/ps5-login/STATUS.md` 拆分而来）
> **Jira**：CB2N-27968
> **状态**：**已合入 master**。DevKit 实机走通完整登录链路。

---

## 已完成

### 客户端（Chaos C++ `PlatformDelegate`）

- `initializePS5()` 只做初始化：加载 SigninDialog / LoginDialog / NpAuth PRX
  + `sceUserServiceGetInitialUser()`，**不弹任何框**
- 登录入口原语化为 `startPS5Login()`：重置凭证 + `beginPS5AuthForUser()`
  （内部判 guest → 选用户框 / 真实用户 → 登录框）
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
| P2-1 | 用户切换/退出：监听 `sceSystemServiceReceiveEvent` / `sceUserServiceEvent`，切用户后重走登录 |
| P2-2 | 已登录用户免框：`signedUp==true` 时用 `sceNpGetState` 判断在线态，已在线则跳过 SigninDialog |
| P2-3 | token 刷新：access_token 过期后的续期流程 |
| P2-4 | 错误提示细化：区分 NpAuth 失败 / GAC 失败 / 网络异常 |

**P2-1 是存档 D3 缺陷（二次登录不重新绑定存档）的前置条件。**
**P2-3 是支付 token 架构的前置条件之一。**

---

## 如何验证 GAC

两条链路，分层验（先单独 curl 打端点，再看游戏日志链路）：

1. **客户端 → GAC `/ps5/getUserInfo`**：拿 auth code 换 account_id + token
2. **登录服 → GAC `/login/auth/token`**：用上一步的 token 校验换 account_id

详见 [docs/game_account_center.md](docs/game_account_center.md)。

---

## 相关文档

- [IMPLEMENTATION.md](IMPLEMENTATION.md) — 实现细节、代码路径、数据流
- [docs/game_account_center.md](docs/game_account_center.md) — GAC Go 服务分析 + PS5 收口方案
- [docs/ps5_login_methods.md](docs/ps5_login_methods.md) — S2S vs ID Token 方案选型
- [../shared/ps5_sdk_reference_links.md](../shared/ps5_sdk_reference_links.md) — SDK / Auth Web API 文档索引
