# PS5 登录功能（CB2N-27968）

**目标**：在 Chaos 引擎 + Proven Ground 游戏中接入 PS5（Prospero）平台登录，复用现有 Steam/PlatformDelegate 模式。

**当前形态**：已走通真实 authorization code 获取 + 登录服 S2S token 交换。客户端通过 `PlatformDelegate` 调用 PS5 SDK 拿 code，服务端用 Client ID + Client Secret 调 PSN Auth Web API 换 `account_id` 完成登录。

**注意**：当前 Client Secret 为硬编码（最快路径），生产前必须迁出代码/配置。

---

## 分支

| 仓库 | 分支 |
|---|---|
| Chaos 引擎 | `feature/CB2N-27968-ps5-login` |
| Proven Ground | `feature/CB2N-27968-ps5-login` |

---

## 相关文档

| 文档 | 用途 |
|---|---|
| [STATUS.md](STATUS.md) | 当前进度与下一步 |
| [IMPLEMENTATION.md](IMPLEMENTATION.md) | 实现细节、代码路径、数据流 |
| [docs/ps5_login_methods.md](docs/ps5_login_methods.md) | **S2S vs ID Token 登录方案对比与选型说明** |
| [docs/ps5_save_data.md](docs/ps5_save_data.md) | **PS5 本地存档/设置项持久化（CB2N-29569）：实现、已知缺陷（含 TRC R5089 主线程问题）、验证方法** |
| [docs/game_account_center.md](docs/game_account_center.md) | **统一登录 Go 服务分析（`E:\code\game_account_center`）+ PS5 收口方案 + go mod tidy 修复** |
| [docs/ps5_sdk_reference_links.md](docs/ps5_sdk_reference_links.md) | **PS5 SDK / Auth Web API 原始文档索引** |
| [docs/ps5_document_crawler.md](docs/ps5_document_crawler.md) | `features/ps5-document` 爬虫能力与文档索引 |
| `features/ps5-document/docs/ps5_client_id_application_guide.md` | 如何申请 Client ID / Client Secret |
| `features/ps5-document/docs/ps5_online_game_integration_guide.md` | PS5 联网游戏接入总览 |

---

## 关键代码位置

### Chaos 引擎（C++ 客户端）

```
_source/_engine/source/client/
  private/chaos/client/platform/chaos_platform_delegate.cpp   # PS5 SDK 调用
  private/chaos/client/root/chaos_client_root.cpp             # 静态字段初始化
  private/chaos/client/script/lua/chaos_client_lua_accessor.cpp # Lua 绑定
  public/chaos/client/platform/chaos_platform_delegate.h
  public/chaos/client/root/chaos_client_root.h                # PS5 字段 + getter/setter
  public/chaos/client/script/lua/chaos_client_lua_accessor.h
  CMakeLists.txt                                              # Prospero 链接 libSceNpAuth_stub_weak.a + libSceSigninDialog_stub_weak.a
```

### Proven Ground（Lua 登录服 + 客户端）

```
_source/_scripts/
  client/game_level/chaos_client_login_level.lua              # 客户端 PS5 分支透传
  client/ui/ui_models/chaos_html_login_ui_model.lua           # 登录页自动登录触发（PS5 分支）
  server/login_server/login_user/chaos_login_user_ps5.lua     # PS5 S2S 登录实现（临时，目标收口到 game_account_center）
  server/login_server/login_user/chaos_login_user_base.lua    # HTTP 请求类型枚举 + 登录状态机
  server/login_server/login_user/chaos_login_user_manager.lua # 派发 PS5 登录用户
  common/chaos_lua_common_structures.lua                      # 账号类型等常量
```

### game_account_center（统一登录 Go 服务，独立仓库）

```
E:\code\game_account_center/          # Beego, Go 1.24；codebase-memory 项目名 E-code-game_account_center
  routers/router.go                   # 路由表（steam=/steam/getUserInfo，PS5 待加）
  controllers/LoginContrlloer.go      # 登录主逻辑
  oauth2/steam.go 等                  # 每平台一个文件；PS5 = 新增 oauth2/ps5.go
```


---

## 核心数据流

```
[PS5 DevKit]
  ├─ sceSigninDialogOpen(userId)              ← 未登录弹系统登录框；已登录立即 FINISHED/OK
  ├─ 每帧 tick() 轮询 SigninDialog 状态
  ├─ sceNpAuthGetAuthorizationCodeV3()        → auth_code + issuer_id
      └─ ClientRoot::setPS5AuthToken() / setPS5IssuerID()
          └─ Lua: platform_delegate:getPS5AuthToken() / getPS5IssuerID()
              └─ chaos_client_login_level.lua
                  └─ RPC RequestLanding / CLT2LGNRequestLogin (password = "issuer_id|auth_code")
                      └─ LoginUserPS5
                          └─ POST /oauth/token (Basic ClientID:Secret)
                              └─ GET /userinfo (Bearer access_token)
                                  └─ account_id → 游戏账号登录
```

---

## 环境映射（PS5 S2S Auth Web API v3）

| 环境 | Issuer ID | Token Endpoint | UserInfo Endpoint |
|---|---|---|---|
| sp-int（研发） | 1 | `https://s2s.sp-int.playstation.net/api/authz/v3/oauth/token` | `https://s2s.sp-int.playstation.net/api/authz/v3/oauth/userinfo` |
| prod-qa（认证） | 8 | `https://s2s.prod-qa.playstation.net/api/authz/v3/oauth/token` | `https://s2s.prod-qa.playstation.net/api/authz/v3/oauth/userinfo` |
| np（生产） | 256 | `https://s2s.np.playstation.net/api/authz/v3/oauth/token` | `https://s2s.np.playstation.net/api/authz/v3/oauth/userinfo` |

> NpAuth 客户端请求 authorization code 时 scope 必须为 `"psn:s2s openid id_token:psn.basic_claims"`；只传 `"psn:s2s"` 会被授权服务器以 `0x82XXXXXX` server error 拒绝。

---

## 安全提示（必读）

- **Client Secret `DtCLkkWViqmORho9` 已泄漏**（曾出现在聊天记录与代码中），生产前必须轮换。
- Client Secret 只能存在于服务端，禁止写入客户端、禁止提交 git、禁止明文传播。
- PS5 SDK 文档受 NDA 保护，不要上传到在线服务、AI 云、公开仓库或外传截图。

---

## 常用操作

### 切换 feature 上下文

```bash
python scripts/switch_feature.py ps5-login
```

### 抓取/更新 PS5 文档

见 [docs/ps5_document_crawler.md](docs/ps5_document_crawler.md)。
