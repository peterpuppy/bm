# PS5 支付（PSVC 虚拟货币）— 进度

> **Jira**：CB2N-30579
> **分支**：`feature/CB2N-30579-ps5-payment`（Chaos + Proven Ground，base: `feature/CB2N-30497-ps5-trophy`）
> **状态**：代码就绪并已提交，**未全链路实测** —— 卡在 DevNet 商品侧。
> **方案**：[PLAN.md](PLAN.md)

---

### 代码（已提交）

**客户端（Chaos）**：
- `chaos_ps5_commerce_context.{h,cpp}`：CHECKOUT 弹窗 + 状态机（idle/running/purchased/closed）
- 生命周期按 SDK sample 模式：**每次购买 Initialize → Open2 → 轮询 → GetResult → Terminate**（非常驻 init）
- `sceCommonDialogInitialize` 前置（CommerceDialog 是 CommonDialog 系，与 SigninDialog 不同）
- Param2/Open2 新 API：serviceLabel=0 + serviceName=COMMERCE_CATALOG_AND_ENTITLEMENTS
- PRX 只有 `SCE_SYSMODULE_NP_COMMERCE`（无独立 COMMERCE_DIALOG 模块）
- Meta 暴露：`openPS5Checkout(label)` / `getPS5CheckoutState()`
- V1 跳过 NpCppWebApi/In-Game Catalog 自绘（商品 label 配置侧给，CHECKOUT 价格系统渲染）

**服务端（PG charge_server）**：
- `chaos_charge_server_charge_manager_ps5.lua`：mixin 进主 manager（DMM/Xsolla 同模式）
- Bearer token：client credentials 流（POST oauth/token，Basic auth），缓存+提前5分钟刷新
- consumeEntitlement：PUT /api/entitlement/v2/users/{account_id}/entitlements/{label}
  - PSVC 不传 useCount（一次全部消耗），transactionId 幂等（order_id 充当，格式 ps5_N）
  - 200→发货（CHARGE2CHARACTERFinalizeSteamOrder 复用）；5xx→重试队列；4xx→终态删单
- **字段声明在主 manager ctor**（Chaos 严格类型 + 防御：initialize 链抛错不影响 tick）
- RPC：CLT2CHARACTERFinalizePS5RechargeOrder → character 转发 → CHARGE.FinalizePS5RechargeOrder（nsd schema 已加，RPC 已生成）

**引擎配置（Chaos general_server）**：
- config_accessor 加 ps5_s2s_server_addr/client_id/client_secret 字段+getter+setter
- general_server_root 解析 server_address_info_config.xml 的 <ps5> 节点
- **坑：meta 生成后必须重编 chaos_general_server.dll**（曾因 dll 旧导致 getter 缺实现→Lua 抛错→字段未初始化→tick 崩）

**客户端 Lua（PG）**：
- 充值 UI ps5 分支：列表过滤 + 点击 openPS5Checkout + tickImpl 轮询 purchased→RPC
- TEST 写死：商品 label "CONQCOIN00000000"（Content Pipeline 的 16 位 entitlement label）、测试档借用 steam 行

### 配置侧（Content Pipeline，已完成）
- Product Group: Add-on - Unified Entitlement（PS5 只能用 unified，service 是 PS4 遗留）
- 虚拟货币 = PSVC 包类型；Consumable=Yes + Consumable Limit + Virtual Currency=Yes
- **Group 内的 Product = 区域变体**（不是档位！）；**多档位 = 多个 Group 共享 entitlement**（Use existing consumable Entitlement）
- Entitlement Label 16位：CONQCOIN00000000
- 商品需 Publish to Sp-int 才能在 DevKit 测试

### 待验证（全链路实测）
- [ ] charge_server 启动无报错（字段 ctor 声明修复后）
- [ ] 充值 UI 显示 "PS5 TEST" 档
- [ ] CHECKOUT 弹窗 → 测试钱包付款（VISA 4444 4444 4444 4448）
- [ ] 日志链：checkout opened → purchased → onFinalizeRechargeOrder → token succeed → onConsumeSuccess
- [ ] 金币到账

### 2026-08-31 排障记录（"目前无法购买此产品"）

**结论：不是代码问题，是 Content Pipeline 商品未就绪。** 该文案是 PS5 系统 UI 文字
（checkout 模式下指定了不可购商品时系统报错，CommerceDialog 文档原文）。

排查过程中修掉的两个真实代码 bug（源码已改，**需重编 dll**）：
1. `getCheckoutState()` 原 const → purchased/closed 永不复位 idle，第二次 openCheckout
   被 `not ready state=3` 静默拒绝。改为读取 purchased/closed 后自动回 idle（一次性语义）。
2. `sceNpCommerceDialogGetResult()` 返回值判断 `ret != SCE_OK` → 错。该函数正常终止
   返回正值（OK=1/USER_CANCELED=2/PURCHASED），错误才是负值。改为 `ret < 0`。

**商品侧依赖链（当前卡点）**：
```
Product: Submitted ✅（Submitted ≠ 可售）
  └─ Entitlement: In Progress ⏳（SIE 异步开通 PSVC，只能等）
       └─ PAR: 各区域 WSP 已填 + Availability 已填 → 提交 → SIE 审核 → Valid
            └─ Availability 日期到（新 PAR 强制未来日期，最早约+5天）
                 └─ Product Preview 发布（PSVC 选 Publish without Linking Entitlements）
                      └─ ★Store Preview 确认有价 → checkout 可购买
```

**字段语义**：
- **WSP**（Wholesale Selling Price）：批发结算价 = 商店售价基数。SIE 分成结算基准，
  玩家看到的价格即基于它（美区等消费税另加）。dev 环境真实扣测试钱包。
- **Availability**：上架日期（street date）。**新 PAR 只能填未来日期**（Content Pipeline
  硬规则，防绕过审核），日期未到 = 所有环境不可购买。测试填系统允许的最早日期。
- **Regional Termination Date**：区域下架日期（对应 catalog API SKU endDate）。
  测试留空 = 永不下架。
- **区域必须匹配测试账号注册国**：checkout 按账号所在区取价/判可售，账号美区就配 US/USD。

**dev 环境也要走 PAR 全流程**（Commerce Programming Guide – Before Starting Development：
dev 测试 = 购买 "products created in the development environment"）。dev 优惠仅两条：
测试卡充值 + Product Preview 直接发布（不过 SIE 认证）。PAR 审核/Availability 规则不分环境。

**一档面额一个 Product**（PSVC 文档 BIGGAMEBUCKS_100 模式）。100 金币 = CONQCOIN00000000；
后续 500/1000 档各建 Product（独立 entitlement label），服务端按 label 映射金币数。


### 2026-09-14 Content Pipeline 后台实查（证据链）

用已登录 Chrome (CDP 9222) 直接查了后台，**三层证据都指向：商品未在 PSN 侧就绪**。

#### 后台地址

| 工具 | 地址 | 说明 |
|---|---|---|
| **Content Pipeline** | `https://publish.playstation.net/concepts/10020266` | CONQ concept。**注意不在 DevNet 域下** |
| CONQ COIN Product Group | `https://publish.playstation.net/concepts/10020266/products/10090141` | Product Group ID `10090141` |
| In-Game Catalog | `https://publish.playstation.net/concepts/10020266/ingamestructures/10008112` | Catalog 结构 |
| DevNet 标题管理 | `https://game.develop.playstation.net/titles/151408/products` | title id `151408` |
| CONQ product 页 | `https://game.develop.playstation.net/products/218485` | Services / Credential 下载 |
| **Certification Center** | 从 Content Pipeline 商品页跳转 | GC-119326 所在的工具 |

⚠️ **Content Pipeline 的在线帮助**（`https://learn.playstation.net/bundle/content-pipeline`）
**不在 SDK 文档树里，爬虫取不到** —— PAR/entitlement 的填写步骤只能看界面提示或问 SIE。

#### 证据 ①：In-Game Catalog 未发到 CERT/RETAIL

`ingamestructures/10008112` 页面：

```
Last Published to Sp-int:            Draft-2026-09-10 by Yuan, Mengjie   INGESTED
Last Published to Prod-QA:           Draft-2026-08-31 by Ross, Phil      INGESTED
Last Published to RETAIL:            Not Submitted
Certification Center Test Status:    Pending Approval
```

**Catalog 里的 CONQ COIN 行**：

```
NAME        TYPE                          ENTITLEMENT ID                            VALID  STATUS  DEV/SP-INT PUBLISH DATE
CONQ COIN   Add-on - Unified Entitlement  HP3255-PPSA38951_00-0683974373790429      (空)   (空)    2026-08-31
CONQ        Full Game                     HP3255-PPSA38951_00-0364252386100017      (空)   (空)    2026-08-20
```

**`VALID` 与 `STATUS` 两列为空 = 商品在该环境不可售。**

#### 证据 ②：PAR 四个区的价格状态为空

`products/10090141` → Pricing & Availability：

```
Coin | Booming Games | Digital | Standard
REGION        STATUS   FUTURE PRICE VERSIONS
SIEA          -        1
SIEE          -        1
SIEJA-ASIA    -        1
SIEJA-JAPAN   -        1
```

**PAR 存在、四个区都列了，但 `STATUS` 全空 —— 邮件说的 "entitlements are incomplete" 就是指这个。**

**⚠️ 更正（09-14）**：列表页的 `STATUS: -` 是**摘要未刷新**，点进 `Manage`
（跳到 `publish.playstation.net/termsofsales/10983265`）后实际状态是**已填完**：

| SIE Region | 国家/地区 | STATUS | Availability | WSP | IRP |
|---|---|---|---|---|---|
| SIEA | 18/18 | **Submitted** | 2026-09-20 | USD 0.34 | 0.49 |
| SIEE | 43/43 | **Submitted** | 2026-09-20 | EUR 0.29 | 0.49 |
| SIEJA-Japan | 1/1 | **Submitted** | 2026-09-20 | JPY 35 | 55 |
| SIEJA-Asia | 7/7 | **Submitted** | 2026-09-20 | USD 3.49 | 4.99 |

**所以价格不是卡点。** 教训：Content Pipeline 列表页的状态列不可信，要看详情页。

#### 证据 ③：Entitlement 卡在 Certification Center

```
Entitlement Status:  In Progress
MAIN ENTITLEMENT:  HP3255-PPSA38951_00-CONQCOIN00000000
CERTIFICATION CENTER ID:      GC-119326
CERTIFICATION CENTER STATUS:  On Hold          ← 之前记录的卡点，仍在
Application Type / Entitlement Package Type: PSVC
```

#### 结论

**代码侧无需改动。** `openPS5Checkout()` 的参数格式是对的 ——
弹窗能起来（`sceNpCommerceDialogOpen2` 返回 `SCE_OK`），是 PSN 侧判定该 product 不可购买。

文档依据（`NpCommerceDialog-Overview/using-the-checkout-mode.md`）：
> **An error occurs if even one already-purchased product or product that cannot be purchased is specified.**

#### ⚠️ 待确认：`CONQCOIN00000000` 到底是不是 product label

| 名称 | 值 | 出处 |
|---|---|---|
| Pricing Label（PAR） | `Coin` | Pricing & Availability 页 |
| Entitlement ID | `HP3255-PPSA38951_00-0683974373790429` | In-Game Catalog 行 |
| Main Entitlement Package | `HP3255-PPSA38951_00-CONQCOIN00000000` | Entitlement Details |

代码传的是 `CONQCOIN00000000`。而 CHECKOUT 文档说 `targets` 要的是 **product label**
（在 Product Groups 层级）。**`Coin` 看起来像 PAR 的 label，不是 product label —— 需向 SIE 确认。**

#### 邮件里的 `{0}` 未替换

```
SIE Regions: {0}: SIEA, SIEE, SIEJA_ASIA, SIEJA_JAPAN
Platform:    {0}: PS5
```

**模板变量未渲染**，通常意味某项配置为空导致系统拼不出值。这是 SIE 邮件模板的内部变量，
文档无说明 —— **建议直接回复该邮件询问**。

#### 时间约束

邮件 PAR start date = **2026-09-19**。即使上述全部配好，**9-19 之前依然不可购买**
（Availability 日期未到 = 所有环境不可售）。


### 2026-09-14 Certification Center 审查（On Hold 根因）

#### 结论：代码和商品配置都没问题，卡在认证流程

进入 **Certification Center** 实查 GC-119326，On Hold 原因**明确列出两条**。

#### 认证中心地址

| 工具 | 地址 |
|---|---|
| Certification Center | `https://certify.playstation.net/fqaweb/index.cfm` |
| Submission Manager | `https://certify.playstation.net/fqaweb/index.cfm?event=submission_manager.main` |
| MDT 表单（本产品） | `...viewMdtReportMaster&v_mdt_id=129327&v_format=PS5&v_product_id=10522325&v_product_type=DLC&v_region=ASIA&v_version=01.00` |
| **Communication Tracker** | `.../SCECommunicator/ScreenLayout/glo_generic_communication_layout.cfm?glo_what_screen=VIEW_EDIT&...` |
| 认证文档（可访问） | `https://learn.playstation.net/category/certify` |
| Add-On MDT 指南 | `https://learn.playstation.net/bundle/certops-guide/page/mdt_add-on.html` |

#### On Hold 原文（两条）

**第一次（已解除）**：
```
29-AUG → 31-AUG  (2d 7h 3m)
Content ID not visible within Prod-QA. Please check your configuration and
contact CertOps via the Communication Tracker once this issue has been resolved.
```

**当前（仍挂着，31-AUG 至今）**：
```
1. Awaiting submission of base application.
   Please contact CertOps via the communications tracker when this has been submitted.

2. This DLC is not appearing on the Regional or title store preview.
   Please verify that the DLC is set up correctly and raise a Help Center ticket
   if assistance is needed.
```

#### 认知修正：`DLC` 提交类型是**正确的**，不是配置错误

一度怀疑「内购金币选了 DLC 是选错了」。查 Add-On MDT 指南后**推翻**：

> **The following information is required on a DLC MDT form.**
>
> **Service Entitlement (PlayStation®4 and PlayStation®5 only)**
> This subsection **only appears for DLC set up as a consumable in Content Pipeline**.

**SIE 认证体系里，PSVC/PSCONS 这类内购商品统一走 `DLC` 提交类型** ——
`DLC` 是认证术语，涵盖所有 Add-on，不是狭义的"资料片"。

本产品 MDT 表单实测：
```
Product Type:                DLC
Entitlement - Package Type:  PSVC
Content ID:                  HP3255-PPSA38951_00-CONQCOIN00000000
MDT Status:                  FINAL          ← 已提交，必填项齐全
Last Modified:               MENGJIE YUAN on 28-AUG-2026
```

#### MDT 表单本身没问题

`MDT Status: FINAL`，表单上**无橙色未填标记**。所以「哪里没填完善」的答案
**不在 MDT 表单** —— 卡点是 On Hold 那两条。

**表单上三个可疑但不确定的点**（需问 CertOps）：
| 字段 | 值 | 疑虑 |
|---|---|---|
| `TRC waivers on DevNet` | 空 | 是否必填？ |
| `H.264/MPEG4 AVC Included` | 空 | 是否必填？ |
| `Additional Submission Requirements` | **「无」（中文）** | 表单其余字段是英文，审核员可能读不懂；且 `Supporting Documentation` 要求「奖杯列表及解锁方式」文档 |

#### Communication Tracker：一条记录都没有

```
My Communications → [No Communications]
```

**从未联系过 CertOps。** 而 On Hold 两次原文都要求「解决后通过 Communication Tracker 联系 CertOps」
—— 说明这是**人工放行**流程，不联系就永远挂着。

#### 关键：DLC 认证依赖主程序

Submission Manager 里**只有 CONQ COIN 一条**，没有主程序 `CONQ (PPSA-38951)` 的记录。

**On Hold 第 1 条 `Awaiting submission of base application` 说的就是这个** ——
DLC 认证天然要求 base application 先进系统。

#### 现在要做的

| # | 事项 | 谁做 |
|---|---|---|
| 1 | 确认主程序 `PPSA-38951` 的认证提交状态 | 你 |
| 2 | DevKit 上用 **Title Store Preview** 确认 CONQ COIN 在商店可见 | 你 |
| 3 | **Communication Tracker 开一条沟通**，说明进度 + 问上面三个疑问 | 你 |
| 4 | 等 Availability 日期（**2026-09-20**） | — |


### DEV 测试最小路径（目标：只在开发环境跑通内购）

**前提认知**：本项目只需 **Sp-int/DEV** 验证，不发布 RETAIL。但 **PAR 与 Availability
规则不分环境** —— dev 商品同样要走完。

#### 已完成的（无需再做）

| 项 | 状态 | 证据 |
|---|---|---|
| 商品创建 | ✅ | Product ID `HP3255-PPSA38951_00-0683974373790429` |
| Entitlement | ✅ | `HP3255-PPSA38951_00-CONQCOIN00000000`（PSVC） |
| **四区价格 + Availability** | ✅ | 全部 `Submitted`，WSP/IRP 齐全，日期 2026-09-20 |
| Metadata / Age Rating / Compatibility | ✅ | 均 `Complete` |
| Product Preview | ✅ | `Published`（2026-08-31） |
| In-Game Catalog → Sp-int | ✅ | `Draft-2026-09-10 INGESTED` |
| MDT 表单 | ✅ | `MDT Status: FINAL` |
| 代码 | ✅ | 见本文档「代码」节 |

#### 仍需解决的（按依赖顺序）

| # | 事项 | 依赖 | 谁做 |
|---|---|---|---|
| **1** | **Communication Tracker 开沟通** | 无依赖，**先做这个** | 你 |
| 2 | 确认主程序 `PPSA-38951` 认证状态（或问能否豁免） | 待 1 的回复 | 你 |
| 3 | DevKit 验 Title Store Preview 可见性 | 无 | 你 |
| 4 | 等 Availability 2026-09-20 | 无 | — |

**第 1 步是打破僵局的关键** —— On Hold 是人工放行，`[No Communications]`
意味着这条线从未启动过。

#### DEV 与 RETAIL 的差别（省事的地方）

| | DEV / Sp-int 测试 | RETAIL 发布 |
|---|---|---|
| SIE 认证审核 | 不需要（用 Product Preview 直接发） | 需要 |
| 测试卡充值 | 可用 | — |
| **PAR + Availability** | **仍需要** | 需要 |
| **Certification Center On Hold** | **仍需解除** | 仍需 |

**结论：不能跳过认证中心的 On Hold 直接测 DEV。** 它卡住的是 entitlement 的可用性，
而 entitlement 不发，商品在任何环境都不可购买。

### 遗留
- 设计表 recharge_gold_table 加 ps5 行 + ps5_product_label 列（替换 TEST 写死）
- client_id 确认有 entitlements scope（token 400 时查）
- Client Secret 生产前必须轮换（已泄漏过）
- GuardianModeManager 的 URL 缺斜杠 bug（2023年老bug，与支付无关，未修）
- 客户端 dll 重编（含 getCheckoutState/GetResult 两修复）后才能全链路实测
