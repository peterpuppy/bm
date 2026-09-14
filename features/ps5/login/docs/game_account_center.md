# game_account_center（统一登录/账号中心 Go 服务）

> 位置：`E:\code\game_account_center` ｜ 框架：Beego（私有 fork）｜ Go 1.24
> codebase-memory 项目名：`E-code-game_account_center`

## 是什么

各类平台登录/账号的**统一 Go 服务**，游戏客户端和登录服通过 HTTP 调它完成第三方认证、账号查询、白名单、未成年保护、VIP 充值等。客户端 Lua 里的 `LoginManager.k_game_account_center_addr`（如 `https://accounts-cbx.boomingtech.com`）指向的就是它。

已接入平台：netease（账号/将军令/密保卡/短信/二维码）、booming（poros/local）、facebook、google、kakao、twitter、steam、mailru、wegame、mygames、顺网(sw)。

## 目录结构

| 目录 | 职责 |
|---|---|
| `main.go` | 入口：initLog / InitCache / InitMySql / scheduler / beego.Run |
| `routers/router.go` | 所有 HTTP 路由 → Controller 方法 |
| `controllers/` | `LoginContrlloer.go`(4550行,登录主逻辑) / VIP / Whitelist / Common |
| `oauth2/` | **每个平台一个文件**（steam.go/facebook.go/google.go...）做第三方 API 调用 |
| `services/` | api_service / dispatch_service / login_mutex_service / request_service |
| `models/` `db/mysql/` | 数据模型 + MySQL 访问 |
| `pkg/` | cache / config / etcd / feishu / jwttoken / md5sum 等内部库 |
| `scheduler/` `collector/` | 定时任务 / 采集 |
| `conf/` | 配置（含 k8s / etcd 动态配置） |

部署：Dockerfile + k8s.yaml + gitlab-ci，K8s 模式下配置从 etcd 拉。

## 与 PS5 登录的关系（关键）

- 客户端 Lua 里 steam 走的是 `k_game_account_center_addr + "/steam/getUserInfo"` → **就是这个服务**。
- **PS5 此前这里没有任何路由**——所以最初把 PS5 的 S2S 交换临时写在 Lua 登录服 `chaos_login_user_ps5.lua` 里（**该文件已删除**，现已收口到 GAC）。
- **目标架构**：把 PS5 S2S 收口到本服务，与 steam 对称：
  - 新增 `oauth2/ps5.go`：做 `POST /v3/oauth/token`（Basic ClientID:Secret）+ `GET /v3/oauth/userinfo` → 返回 `account_id`。
  - 新增路由 `/ps5/getUserInfo`（或 `/login/ps5/...`），Controller 里加对应 handler。
  - 收益：① Client Secret 收口到服务端（修掉硬编码泄漏）② 静态出口 IP 满足 PSN 白名单（只需给这个服务申一个 IP）③ 后续 PSN 支付/权益回调也落这里。

详见 [ps5_login_methods.md](ps5_login_methods.md) 的方案选型。

## go mod tidy 障碍与修复

依赖两个**私有 GitLab 模块**：`gitlab.booming-inc.com/.../pkg/beego`、`.../pkg/log`。tidy 卡住的根因是**本机没配 gitlab.booming-inc.com 凭证**（`git ls-remote` 报 `missing OAuth configuration`），且 GOPRIVATE 为空导致私有模块走了公共代理。

```bash
# 1. 私有域绕开公共代理 + 校验库
go env -w GOPRIVATE=gitlab.booming-inc.com

# 2. 用 PAT 访问私有 gitlab（<TOKEN> = 你的 read_repository PAT，需在公司内网/VPN）
git config --global url."https://oauth2:<TOKEN>@gitlab.booming-inc.com/".insteadOf "https://gitlab.booming-inc.com/"

# 3. 验证连通
git ls-remote https://gitlab.booming-inc.com/booming/dev/backend/go_projects/pkg/log.git

# 4. tidy
cd E:/code/game_account_center && go mod tidy
```

> go.sum 已含这两个私有模块的 hash，凭证配好后校验能过；其余均为公共库，可正常拉取。
