# PS5 联网游戏接入指南（内部交付版）

> 目标读者：后续接手 PS5 联网功能开发的团队 / context。
> 基于已抓取的 SDK 12.000 + WebAPI 1 官方文档整理。
> 本地文档根目录：`output/psn_12/`

---

## 1. 本项目要做的事情

开发一款 PlayStation®5 联网游戏，需要接入：

1. **玩家本地登录 PSN**（客户端）。
2. **游戏服务器安全访问 PSN 数据**（服务端 OAuth）。
3. **多人联机基础设施**（Session、Matchmaking、P2P / Relay / 专用服务器）。
4. **合规与测试环境**（沙箱 / Legacy 环境、开发账号、服务配置）。

---

## 2. 关键术语

### NP
**NP = Network Platform**，即 PlayStation 的网络平台。所有以 `Np` 开头的库、ID、环境都属于这一层：

- `NpAuth`：Network Platform Auth，负责授权码和 ID token。
- `NpTitleId`：Network Platform Title ID，游戏的唯一标识。
- `NP Environment`：网络环境，即 sp-int / prod-qa / np（Legacy）或 DEV / CERT / RETAIL（Sandbox）。

### Sandbox / Legacy
- **Legacy**：传统架构，三个物理隔离的环境：
  - `sp-int`：开发环境
  - `prod-qa`：认证环境
  - `np`：生产环境
- **Sandbox**：新架构，DEV 和 CERT 是位于 RETAIL 基础设施内的虚拟隔离环境。开发和认证使用同一套底层服务。

---

## 3. 是否必须在开始就处理沙箱？

**不需要。**

沙箱/环境选择是**环境层**的问题；登录是**功能层**的问题。两者有关系，但不是阻塞关系：

| 层级 | 负责内容 | 是否第一天就要处理 |
|---|---|---|
| 功能层：登录 | `SigninDialog` 本地登录、`NpAuth` 拿 authorization code | **是，先做** |
| 授权层：服务端换 token | `Auth Web API` 用 code 换 access token | **是，跟着做** |
| 环境层：Sandbox / Legacy | 游戏连到哪个 PSN 后端 | **否，先 Legacy sp-int 跑起来** |

### Sandbox 与 NpAuth 的关系

- `NpAuth` 获取 authorization code 时，会**自动携带当前环境信息**。
  - Legacy：通过返回的 **issuer ID** 区分环境。
  - Sandbox：环境上下文嵌入在 access token 里。
- 你的游戏服务器需要根据这个环境信息，调用对应环境的 Web API endpoint。
- **登录代码本身基本不用改**，主要改服务端的环境识别和路由逻辑。

### 推荐接入顺序

| 阶段 | 该做的事 |
|---|---|
| **第一阶段（现在）** | 在 Legacy `sp-int` 环境完成登录验证、创建开发账号、跑通基础联网。 |
| **第二阶段** | 接入 Session Manager / Matchmaking / P2P，继续在 `sp-int` 验证。 |
| **第三阶段（上线前）** | 与 SIE 确认 Sandbox 迁移计划，迁移后做环境切换测试。 |

> 一句话：**先登录，后沙箱。代码保持环境无关，以后切沙箱改动最小。**

---

## 4. 必须关注的核心文档（已抓取）

### 4.1 登录与授权

| 主题 | 本地路径 | 作用 |
|---|---|---|
| SigninDialog Library Overview | `SDK/12.000/SigninDialog-Overview/` | 客户端显示系统级 PSN 登录对话框。 |
| NpAuth Library Overview | `SDK/12.000/NpAuth-Overview/` | 获取 authorization code / ID token，供游戏服务器换 access token。 |
| Np Library Overview | `SDK/12.000/Np-Overview/` | PSN 基础概念、账号初始化、NP 环境切换。 |
| Auth Web API Overview | `WebAPI/1/Auth_WebAPI-Overview/` | 服务端用 code 换 access token / ID token / refresh token。 |
| Auth for Websites Overview | `WebAPI/1/Auth_for_Websites-Overview/` | 网页端授权流程（如需官网/伴侣应用）。 |
| PlayStation™Network Overview | `SDK/12.000/PSN-Overview/` | PSN 整体架构、账号与身份平台、各子平台概览。 |
| PlayStation™Network Service Setup Guide | `SDK/12.000/PSN_Service_Setup-Guide/` | DevNet 注册产品、申请服务、获取 Client ID / Secret / Redirect URL。 |

### 4.2 多人联机

| 主题 | 本地路径 | 作用 |
|---|---|---|
| PlayStation™Network Multiplayer Platform Concept Overview | `SDK/12.000/PSN_Multiplayer_Platform_Concept-Overview/` | 多人平台整体概念：Player Sessions、Game Sessions、Matches、Game Intent。 |
| PlayStation™Network Multiplayer Best Practices | `SDK/12.000/PSN_Multiplayer_Best_Practices/` | 如何正确使用 Session Manager、邀请、P2P、语音聊天最佳实践。 |
| Session Manager Service Overview | `SDK/12.000/Session_Manager_Service-Overview/` | 会话体系核心概念与使用指南。 |
| Session Manager Web API Overview | `WebAPI/1/Session_Manager_WebAPI-Overview/` | 服务端操作 Player / Game Sessions。 |
| Matchmaking Overview | `WebAPI/1/Matchmaking-Overview/` | 匹配服务、ruleset 配置、backfilling、teams。 |
| Matchmaking Tool User's Guide | `SDK/12.000/Matchmaking_Tool-Users_Guide/` | 匹配规则集测试与配置工具。 |
| NpSessionSignaling Library Overview / Reference | `SDK/12.000/NpSessionSignaling-Overview/` | P2P 连接、NAT 穿透、信令。 |
| PlayerInvitationDialog Library Overview / Reference | `SDK/12.000/PlayerInvitationDialog-Overview/` | 系统级邀请对话框。 |

### 4.3 周边服务（按需接入）

| 主题 | 本地路径 | 作用 |
|---|---|---|
| Universal Data System Guide | `SDK/12.000/Universal_Data_System-Guide/` | Activities、Trophies、Game Help、Challenges 等数据驱动体验。 |
| Creating Data-Driven Experiences with UDS | `SDK/12.000/Creating_Data_Driven_Experiences_with_UDS/` | UDS 实际工作流。 |
| Trophy System Overview / NpTrophy2 | `SDK/12.000/Trophy_System-Overview/` | 奖杯系统。 |
| Leaderboards Web API | `WebAPI/1/Leaderboards-Overview/` | 排行榜。 |
| VoiceChat / ProprietaryVoiceChatHelper | `SDK/12.000/VoiceChat-Overview/` | 平台语音聊天（尚未抓取）。 |
| NpCommerce / NpCommerceDialog | `SDK/12.000/NpCommerce-Overview/` | 游戏内 commerce / 商店对话框。 |

### 4.4 沙箱与账号管理

| 主题 | 本地路径 | 作用 |
|---|---|---|
| Sandbox Network Architecture Guide | `SDK/latest/Sandbox_Network_Architecture-Guide/` | 沙箱架构、DEV/CERT/RETAIL、账号、迁移、服务配置。 |
| Development Accounts User's Guide | `SDK/12.000/Development_Accounts-Users_Guide/` | 创建/管理开发测试账号、title privileges。 |
| DevAdmin Tool User's Guide | `SDK/12.000/DevAdmin_Tool-Users_Guide/` | 清 entitlement、aging、改 online ID 等调试操作。 |
| Sandbox Management WebAPI | `WebAPI/1/Sandbox_Management_WebAPI-Overview/` | 用 Web API 管理沙箱。 |

---

## 5. Sandbox vs Legacy 详解

### 结论

- **不是接入登录的必要条件。** 登录流程在 Legacy 和 Sandbox 下基本一致。
- **Sandbox 是 SIE 未来的标准环境**，新立项的 PS5 游戏应朝 Sandbox 规划；老项目需等 SIE 迁移。
- 文档明确说明：`Currently, the Network Architecture setting is not available`，即 DevKit 当前可能还无法直接切换 Sandbox。

### 关键区别

| 维度 | Legacy | Sandbox |
|---|---|---|
| 环境 | sp-int（开发）、prod-qa（认证）、np（生产） | DEV、CERT，均位于 RETAIL 基础设施内 |
| 物理隔离 | 三套独立物理环境 | 虚拟隔离，共享同一基础设施 |
| API domain | 不同环境不同域名 | 统一域名，环境上下文在 access token 中 |
| 开发账号 | 各环境独立账号 | 同一账号可跨 DEV/CERT，account_type = SANDBOX |
| DevKit 切换 | ★Debug Settings > NP Environment | ★Debug Settings > Network Architecture（暂不可用） |
| 迁移 | 无需迁移（老项目默认在此） | 必须由 SIE 迁移标题和账号 |
| 服务配置 | 通过 DevNet / 传统工具 | `np-service-config` CLI 或 web 工具，可版本控制 |

### 推荐策略

| 项目状态 | 建议 |
|---|---|
| 新 PS5 项目 | 按 Sandbox 规划，但先用 Legacy sp-int 完成开发与验证，待 Network Architecture 设置开放后迁移。 |
| 已上线 / Legacy 老项目 | 继续在 Legacy 完成登录与联机接入；Sandbox 迁移由 SIE 主导，不可自行切换。 |
| 只需验证登录 | 用 Development Accounts 在 sp-int 创建测试账号，直接验证，无需 Sandbox。 |

---

## 6. 沙箱 / Legacy 环境切换相关文档链接

### Sandbox 架构与配置

| 文档 | 本地路径 |
|---|---|
| Sandbox 网络架构总览 | `output/psn_12/SDK/latest/Sandbox_Network_Architecture-Guide/sandbox-network-architecture-overview.md` |
| Sandbox 基础设施设计 | `output/psn_12/SDK/latest/Sandbox_Network_Architecture-Guide/sandbox-infrastructure.md` |
| 开发用账号（Sandbox） | `output/psn_12/SDK/latest/Sandbox_Network_Architecture-Guide/accounts-for-development-for-sandbox.md` |
| 标题迁移到 Sandbox | `output/psn_12/SDK/latest/Sandbox_Network_Architecture-Guide/sandbox-title-migration.md` |
| DevKit/TestKit 上管理 Sandbox | `output/psn_12/SDK/latest/Sandbox_Network_Architecture-Guide/sandbox-management-on-devkit-testkit.md` |
| Sandbox 服务配置 | `output/psn_12/SDK/latest/Sandbox_Network_Architecture-Guide/service-configuration.md` |
| 开发与发布工作流 | `output/psn_12/SDK/latest/Sandbox_Network_Architecture-Guide/developing-and-publishing-workflow.md` |
| 游戏和服务器代码适配 | `output/psn_12/SDK/latest/Sandbox_Network_Architecture-Guide/game-and-server-code.md` |

### Legacy 环境切换

| 文档 | 本地路径 |
|---|---|
| NpAuth 中的 NP 环境切换 | `output/psn_12/PlayStationNetwork/Authentication_and_Authorization/NpAuth-Overview/support-for-np-environment-switching.md` |
| PlayStation™Network 概述 - NP 环境 | `output/psn_12/PlayStationNetwork/Start_Here/PSN-Overview/np-environments.md` |
| PSN Service Setup - 服务请求与生产启用 | `output/psn_12/PlayStationNetwork/Start_Here/PSN_Service_Setup-Guide/requesting-a-service-enabling-to-productio.md` |

### Matchmaking 在两种架构下的 ruleset 应用

| 文档 | 本地路径 |
|---|---|
| Legacy 下应用 Ruleset | `output/psn_12/PlayStationNetwork/Session_Manager_(Sessions_Invitations_Matches_Matchmaking)/Matchmaking-Overview/using-rulesets.md` |
| Sandbox 下应用 Ruleset | `output/psn_12/PlayStationNetwork/Session_Manager_(Sessions_Invitations_Matches_Matchmaking)/Matchmaking-Overview/using-rulesets-in-sandbox-mode.md` |

---

## 7. PS5 登录接入方法

### 7.1 客户端本地登录

使用 `SigninDialog` 库：

```cpp
sceSysmoduleLoadModule(SCE_SYSMODULE_SIGNIN_DIALOG);
// 初始化 -> 设置 user ID -> 显示对话框 -> 轮询关闭 -> 结束处理
```

- 系统提供本地化登录 UI，支持注册、找回密码。
- 登录成功后，应用在本机处于已登录 PSN 状态。
- 参考：`SDK/12.000/SigninDialog-Overview/`

### 7.2 游戏服务器访问 PSN 数据（OAuth 2.0）

如果游戏服务器需要查询用户数据（好友、奖杯、资料等），使用 `NpAuth` + `Auth Web API`：

```
PS5 客户端                          游戏服务器                      PSN 服务器
   |                                   |                              |
   |-- sceNpAuthGetAuthorizationCodeV3() 得到 authorization code       |
   |                                   |                              |
   |--------- 发送 authorization code + issuer ID ------------------->|
   |                                   |                              |
   |                                   |-- Auth Web API: code -> access_token + id_token
   |                                   |                              |
   |<----------- 返回 access_token 或业务数据 -----------------------|
```

调用 `NpAuth` 需要：

- User ID（目标用户）。
- Client ID（DevNet 颁发给游戏服务器）。
- Scope（要访问的 PSN 数据范围）。

游戏服务器换 token 需要：

- Client ID + Client Secret。
- Redirect URL。
- authorization code。

参考：

- `SDK/12.000/NpAuth-Overview/`
- `WebAPI/1/Auth_WebAPI-Overview/`

### 7.3 环境识别（Legacy）

在 Legacy 架构下，游戏服务器需根据 `sceNpAuthGetAuthorizationCodeV3()` 返回的 **issuer ID** 判断环境：

| NP Environment | Issuer ID |
|---|---|
| np（生产） | 256 (0x100) |
| prod-qa（认证） | 8 (0x8) |
| sp-int（开发） | 1 (0x1) |

建议为每个环境部署独立的游戏服务器实例，由服务端根据 issuer ID 做路由。

参考：`SDK/12.000/NpAuth-Overview/support-for-np-environment-switching.md`

---

## 8. 多人联机接入方法

### 8.1 整体架构选择

PlayStation 多人平台提供两层能力：

1. **Session Manager**：管理 Player Sessions、Game Sessions、Matches、Matchmaking、Voice Chat、Game Intent。
2. **网络传输**：
   - **P2P**：用 `NpSessionSignaling` 做 NAT 穿透和信令。
   - **专用服务器 / Relay**：游戏自行实现或使用自有服务器；PSN 主要提供会话和匹配服务。

### 8.2 典型流程

```
1. 玩家登录 PSN
2. 创建/更新 Player Session（展示给好友、支持邀请）
3. 通过 Matchmaking 寻找对手/队友
4. 创建 Game Session，分配玩家/观众
5. 通过 NpSessionSignaling 建立 P2P 连接，或连接专用服务器
6. 游戏中更新 Session 状态，结束时清理
```

### 8.3 关键 API 文档

| 能力 | 客户端库 | 服务端 Web API |
|---|---|---|
| Player / Game Sessions | `SDK/12.000/Session_Manager_Service-Overview/` | `WebAPI/1/Session_Manager_WebAPI-Overview/` |
| Matchmaking | `SDK/12.000/Matchmaking_Tool-Users_Guide/` | `WebAPI/1/Matchmaking-Overview/` |
| P2P 信令 / NAT 穿透 | `SDK/12.000/NpSessionSignaling-Overview/` | 无 |
| 邀请 | `SDK/12.000/PlayerInvitationDialog-Overview/` | Session Manager Web API |
| 语音聊天 | `SDK/12.000/VoiceChat-Overview/`（未抓取） | Session Manager Web API |

### 8.4 匹配 Ruleset

- 用 JSON 定义匹配规则（teams、attributes、rules、relaxed rules）。
- 在 Matchmaking Tool 中测试。
- 分别参考：
  - Legacy: `WebAPI/1/Matchmaking-Overview/using-rulesets.md`
  - Sandbox: `WebAPI/1/Matchmaking-Overview/using-rulesets-in-sandbox-mode.md`

---

## 9. 开发前准备清单

1. **DevNet 注册**
   - 创建产品、获取 NP Title ID、NP Service Label、NP Title Secret。
   - 为游戏服务器申请 Client ID、Client Secret、Redirect URL。
   - 申请需要的 PSN 服务（Session Manager、Matchmaking、Leaderboards 等）。
   - 参考：`SDK/12.000/PSN_Service_Setup-Guide/`

2. **测试账号**
   - 用 Development Accounts Tool 创建 sp-int / Sandbox 开发账号。
   - 为账号分配 title privileges。
   - 参考：`SDK/12.000/Development_Accounts-Users_Guide/`

3. **DevKit/TestKit 环境**
   - Legacy：★Debug Settings > NP Environment 切 sp-int。
   - Sandbox：★Debug Settings > Network Architecture 切 Sandbox + DEV/CERT（当前文档提示尚未可用）。

4. **服务端准备**
   - 部署可接收 authorization code 的 endpoint。
   - 根据 issuer ID 或 sandbox 上下文路由到对应环境。
   - 实现 access token 缓存、refresh token 管理、token 失效重试。

---

## 10. 尚未抓取的联网相关文档

以下文档与联网游戏相关，但**尚未抓取**，如需完整接入建议补抓：

| 主题 | 路径 |
|---|---|
| VoiceChat Library Overview / Reference | `SDK/12.000/VoiceChat-Overview/` |
| ProprietaryVoiceChatHelper Library Overview / Reference | `SDK/12.000/ProprietaryVoiceChatHelper-Overview/` |
| Voice / VoiceQoS Library Overview / Reference | `SDK/12.000/Voice-Overview/` |
| NpEntitlementAccess Library Overview / Reference | `SDK/12.000/NpEntitlementAccess-Overview/` |
| Matches Web API Overview / Reference | `WebAPI/1/Matches_WebAPI-Overview/` |
| In-Game Catalog Web API | `WebAPI/1/In_Game_Catalog-Overview/` |
| Communication Restriction Status Web API | `WebAPI/1/Communication_Restriction_Status_WebAPI-Overview/` |
| Profanity Filter Web API | `WebAPI/1/Profanity_Filter_WebAPI-Overview/` |

---

## 11. 文档索引速查

- 全目录清单：`docs/sdk_12_catalog.md`
- 爬取覆盖率报告：`docs/sdk_12_crawl_report.md`
- 沙箱分析：`docs/sdk_12_sandbox_analysis.md`
- 本地文档根目录：`output/psn_12/`
- 本地 master index：`output/psn_12/_index.json`

---

*整理时间：2026-07-03*
*数据来源：PS5 SDK 12.000 / WebAPI 1 官方文档本地镜像*
*更新说明：补充 NP 术语解释、Sandbox/Legacy 与登录的关系、环境切换文档链接、以及“先登录后沙箱”的接入顺序建议。*
