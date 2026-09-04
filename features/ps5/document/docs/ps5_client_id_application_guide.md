# PS5 Client ID / Client Secret 申请操作手册

> 基于已抓取文档：`SDK/12.000/PSN_Service_Setup-Guide/`
> 适用：Proven Ground 项目 PS5 登录（CB2N-27968）
> 目标：拿到服务端换取 PSN access token 所需的 Client ID + Client Secret

---

## 一、先确认已有什么

| 字段 | 典型来源 | 当前状态 |
|---|---|---|
| NP Title ID | DevNet 创建 `App (PS5)` 产品时发放 | 已确认有 |
| Product ID | DevNet 产品页 | 已确认有 |
| NP Service Label | 申请 PSN 服务时配置 | 可能有 |
| NP Title Secret / nptitle.dat | `App (PS5)` 产品页下载 | 可能有 |
| **Client ID** | **需单独给 App Server 产品申请** | **缺** |
| **Client Secret** | **Client ID 配置完成后下载** | **缺** |
| **Redirect URL** | **DevNet Client ID 配置页填写** | **缺** |

**关键原则**：Client ID/Secret 不会自动随 NP Title ID 发放，必须给 `App Server` 类产品单独申请。

---

## 二、申请前选择正确的产品类型

不要选 `Authorized App Server`（那是给第三方授权、需要用户 Consent Screen 的）。

我们要的是 **Server-to-Server（S2S）** 换 token，所以选：

```
App Server
或
App Server (Client Credential)
```

参考文档：
- `output/psn_12/SDK/12.000/PSN_Service_Setup-Guide/requesting-to-add-a-new-service-for-a-new.md`
- `output/psn_12/SDK/12.000/PSN_Service_Setup-Guide/issuance-of-the-product-credential-files.md`

---

## 三、分步操作

### 步骤 1：创建 App Server 产品

1. 登录 PlayStation®5 Developer Network（DevNet）。
2. 进入你的 Title 管理页。
3. 在该 Title 下创建新产品，产品类型选择：
   ```
   App Server
   ```
   （或 `App Server (Client Credential)`，如果后续希望用 client credential grant）
4. 等待产品创建完成。

> 文档说明：App Server 产品类型**不创建新服务实例**，而是引用已有 `App (PS5)` 产品的服务实例。

---

### 步骤 2：申请 Client ID 服务

1. 打开刚创建的 **App Server 产品详情页**。
2. 找到服务列表区域，点击：
   ```
   Request New Services
   或
   Request Services
   ```
3. 在服务列表中找到并勾选：
   ```
   Client ID
   ```
4. 提交申请。
5. SIE 会创建一个 DevNet service thread 进行审批。
6. 审批完成后，产品页上该服务状态从 **Requested** 变为 **Development** 或 **Production**。

参考文档：
- `output/psn_12/SDK/12.000/PSN_Service_Setup-Guide/requesting-to-add-a-new-service-for-a-new.md` 第 106-131 行

---

### 步骤 3：配置 Redirect URL

Client ID 服务状态变为可用后：

1. 在产品页找到 **Client ID** 服务卡片/下拉菜单。
2. 点击配置入口（可能是 **Configure** 或 **Consent screen configuration**）。
3. 填写 **Redirect URL**：
   ```
   https://<你的登录服域名>/psn/callback
   ```
   例如：
   ```
   https://login.provenground.com/psn/callback
   ```

> 注意：虽然我们的 S2S 流程是客户端直接把 authorization code 发给 login server，不是走浏览器回调，但 DevNet OAuth App 注册通常仍要求填写 redirect URL。可先填登录服的一个占位 HTTPS endpoint。

---

### 步骤 4：下载 Client Secret

1. 在产品详情页找到下载区域。
2. 点击：
   ```
   Download Client Secret
   ```
3. 下载文件为明文（已不再需要 PGP 解密）。
4. 文件中包含：
   - **Client ID**（字符串，如 `9c441948-3221-46c5-a210-ffcb3760cf1a`）
   - **Client Secret**（字符串，需保密）

参考文档：
- `output/psn_12/SDK/12.000/PSN_Service_Setup-Guide/issuance-of-the-product-credential-files.md` 第 246-281 行

---

### 步骤 5：设置团队访问权限

1. 在产品详情页进入 **Access Privileges** 或 **Product Credential Files** 权限管理。
2. 给需要的团队成员（Owner/Editor/Viewer）授予 **Product Credential Files** 权限。
3. 注意：所有下载行为都会被记录到 access log。

参考文档：
- `output/psn_12/SDK/12.000/PSN_Service_Setup-Guide/issuance-of-the-product-credential-files.md` 第 248-262 行
- `output/psn_12/SDK/12.000/PSN_Service_Setup-Guide/managing-access-privileges.md`

---

## 四、拿到凭据后交给开发

把下面这些信息整理成一份安全的内部文档：

```
Client ID:        xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Client Secret:    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Redirect URL:     https://login.yourgame.com/psn/callback
Environment:      sp-int (开发) / prod-qa (认证) / np (生产)
Scope:            psn:s2s
Issuer ID 映射:    sp-int=1, prod-qa=8, np=256
```

**Client Secret 只能存在服务端**，绝对不能：
- 提交到 git
- 写进客户端代码
- 通过 IM/邮件明文传播

---

## 五、当前文档缺少的内容（可用爬虫补抓）

以下是在线 DevNet 门户的 UI 操作细节，当前本地镜像**没有截图或逐步 UI 指引**。建议继续抓取：

| 缺失内容 | 建议抓取目标 | 用途 |
|---|---|---|
| DevNet 产品创建页截图 | `https://game.develop.playstation.net/` 门户实际页面 | 确认按钮位置 |
| "Request New Services" 弹窗截图 | DevNet 产品详情页 | 确认 Client ID 服务入口 |
| Client ID 配置页截图 | DevNet Client ID 服务配置 | 确认 Redirect URL 填写位置 |
| "Download Client Secret" 按钮截图 | DevNet 产品详情页 | 确认下载入口 |

> 抓取方式：用现有爬虫扩展 `psn_12` 目录，或者手动把 DevNet 门户关键页面 HTML 保存到 `features/ps5-document/output/devnet_portal/`。

---

## 六、拿到凭据后的开发动作

1. **客户端（chaos）**：
   - 把真实 Client ID 填入 `PlatformDelegate` 的 `SceNpClientId`。
   - 调用 `sceNpAuthGetAuthorizationCodeV3()` 拿到真实 authorization code。
   - 把 `issuerId` 一起透传给 login server。

2. **服务端（proven_ground login server）**：
   - 按 `issuerId` 选对应环境 endpoint。
   - 用 Client ID + Client Secret 调 PSN Auth Web API `/oauth/token`。
   - 换取 `account_id` / `online_id`，完成游戏账号登录。

---

*整理时间：2026-07-03*
*来源：PS5 SDK 12.000 / PSN Service Setup Guide 本地镜像*
