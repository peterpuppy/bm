# PS5 SDK 文档索引（CB2N-27968）

> 本地已爬取的 PS5 开发文档索引，涉及 SigninDialog、NpAuth、S2S Auth Web API。
>
> 原始文档来自 PlayStation®5 Developer Network，受 NDA 保护，仅限内部使用。

---

## NpAuth Library（客户端拿 authorization code / id token）

| 文档 | 本地路径 | 用途 |
|---|---|---|
| NpAuth Library Overview | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/NpAuth-Overview/index.md` | 总览：authorization code / ID token 获取流程 |
| 同步获取 authorization code | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/NpAuth-Overview/procedure-for-obtaining-authorization-code-synchronous-proce.md` | `sceNpAuthGetAuthorizationCodeV3()` 同步用法 |
| 异步获取 authorization code | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/NpAuth-Overview/procedure-for-obtaining-authorization-code-asynchronous-proc.md` | `sceNpAuthCreateAsyncRequest()` + poll/wait |
| 嵌入程序 | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/NpAuth-Overview/embedding-into-a-program.md` | PRX 加载、链接库说明 |
| NP 环境切换 | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/NpAuth-Overview/support-for-np-environment-switching.md` | issuer_id 与环境映射（sp-int=1, prod-qa=8, np=256） |
| NpAuth Library Reference | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/NpAuth-Reference/index.md` | 所有 API 参考入口 |
| `sceNpAuthGetAuthorizationCodeV3` | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/NpAuth-Reference/sce-np-auth-get-authorization-codev3.md` | 授权码 API、参数、错误码 |
| `sceNpAuthGetIdTokenV3` | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/NpAuth-Reference/sce-np-auth-get-id-tokenv3.md` | ID Token API、参数 |
| `SceNpAuthCreateRequest` | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/NpAuth-Reference/sce-np-auth-create-request.md` | 同步请求创建 |
| `SceNpAuthCreateAsyncRequest` | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/NpAuth-Reference/sce-np-auth-create-async-request.md` | 异步请求创建 |
| `SceNpAuthPollAsync` / `SceNpAuthWaitAsync` | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/NpAuth-Reference/sce-np-auth-poll-async.md` / `sce-np-auth-wait-async.md` | 异步结果获取 |

---

## SigninDialog Library（系统登录对话框）

| 文档 | 本地路径 | 用途 |
|---|---|---|
| SigninDialog Library Overview | `features/ps5/document/output/psn_12/PlayStationNetwork/Signin/SigninDialog-Overview/index.md` | 系统登录对话框总览 |
| SigninDialog Library Reference | `features/ps5/document/output/psn_12/PlayStationNetwork/Signin/SigninDialog-Reference/index.md` | API 参考入口 |

---

## Auth Web API（登录服 S2S）

| 文档 | 本地路径 | 用途 |
|---|---|---|
| Auth Web API Overview | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/Auth_WebAPI-Overview/index.md` | OAuth 2.0 / S2S 总览 |
| HTTP Status and Error Codes | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/Auth_WebAPI-Overview/http-status-and-error-codes.md` | 错误码、scope、grant type |
| Error Handling | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/Auth_WebAPI-Overview/error-handling.md` | 重试与错误处理策略 |
| Get Access Token (Authorization Code) | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/Auth_WebAPI-Reference/0005.md` | `POST /v3/oauth/token` |
| Refresh Access Token | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/Auth_WebAPI-Reference/0004.md` | `POST /v3/oauth/token` with `refresh_token` |
| Revoke Token | `features/ps5/document/output/psn_12/PlayStationNetwork/Authentication_and_Authorization/Auth_WebAPI-Reference/0006.md` | `POST /v3/oauth/revoke` |
| PSN Web APIs Overview - Error Processing | `features/ps5/document/output/psn_12/PlayStationNetwork/Start_Here/PSN_WebAPI-Overview/error-processing.md` | `0x82XXXXXX` server error 说明 |

---

## 其他相关文档

| 文档 | 本地路径 | 用途 |
|---|---|---|
| PS5 联网游戏接入总览 | `features/ps5/document/docs/ps5_online_game_integration_guide.md` | 项目自整理的接入总览 |
| Client ID / Client Secret 申请指南 | `features/ps5/document/docs/ps5_client_id_application_guide.md` | DevNet 注册、redirect URL、scope 申请 |
| SDK 12 文档目录 | `features/ps5/document/docs/sdk_12_catalog.md` | 全部已爬取文档索引 |
| SDK 12 爬取报告 | `features/ps5/document/docs/sdk_12_crawl_report.md` | 哪些文档已爬取、哪些未爬取 |

---

## 外部原始链接（需 DevNet 登录）

- NpAuth Library Overview: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpAuth-Overview/__toc.html
- NpAuth Library Reference: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpAuth-Reference/__toc.html
- Auth Web API Overview: https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_WebAPI-Overview/__toc.html
- Auth Web API Reference: https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_WebAPI-Reference/__toc.html

---

## 备注

- 所有 `features/ps5/document/output/` 下的内容为本地爬取副本，仅用于内部开发参考。
- 不要把这些文档上传到公开仓库、网盘、AI 云服务或外传截图。
