# PS5 支付接入方案（CB2N-待分配）

## 0. 核心认知：PS5 支付与 Steam 的根本差异

Steam 是"服务端主动"：服务端调 `init_txn` 创建订单 → 弹窗 → finalize 验证。
**PS5 是"客户端主动 + 服务端被动确认"**：客户端弹商店 UI 完成购买（系统直接扣款），
 entitlement 落在 PSN 服务器上，**游戏服务端按需拉取并消耗（consume）**。

没有"创建订单"这一步。PSN 不通知你买了什么 —— 是你去查"玩家名下有没有没消耗的 entitlement"。

```
Steam:   客户端 init → Steam弹窗扣款 → 回调OrderID → 服务端 finalize_txn → 发货
PS5:     客户端 checkout弹窗(系统扣款) → entitlement 记在 PSN
           → 客户端通知服务端"我买了" → 服务端调 Entitlements WebAPI
           → listEntitlements 查 → consumeEntitlement 消耗 → 发货记账
```

**红线（PSN 政策）**：虚拟货币（PSVC 类 entitlement）**必须**由游戏服务器消耗，
必须**一次性消耗全部可用数**（all-at-once），**必须先 consume 成功再发货**。
consume 是幂等的（同 transactionId 重试安全），5xx/超时要用同一 transactionId 重发。

## 1. 官方参考实现（本地文档已全）

`Virtual_Currency-Tutorial`（SDK 12.000）—— 官方端到端 demo（游戏 + 游戏服务端 + 钱包）。
本方案流程即出自它的 code-walkthrough：
- 商店：`NpCppWebApi` 查 In-Game Catalog（getContainer）→ 自绘商品 UI + 价格规则
- 购买：`NpCommerceDialog` CHECKOUT 模式（系统购买 UI，处理扣款/密码/收据）
- 钱包：`NpEntitlementAccess` 查未转移 entitlement → 通知游戏服务器 → 服务器 S2S 消耗

## 2. 分层架构（对照现有 Steam 实现）

### 客户端 C++（Chaos 引擎，PlatformDelegate 扩展）

参照 PS5TrophyContext 模式（platform/ 下独立文件 + global_context 持有 + 分阶段初始化）：

```
chaos_ps5_commerce_context.{h,cpp}   ← 新增
  initialize()（deferred 阶段，首帧）
    load PRX: NP_COMMERCE / NP_COMMERCE_DIALOG / NP_ENTITLEMENT_ACCESS / NP_CPP_WEB_API
    sceCommonDialogInitialize + sceNpCommerceDialogInitialize
    sceNpEntitlementAccessInitialize
  shutdown()
  openCheckoutDialog(product_label)        ← CHECKOUT 模式购买弹窗
    sceNpCommerceDialogParamInitialize + mode=CHECKOUT + targets=[label]
    sceNpCommerceDialogOpen
  tickUpdate()                              ← PlatformDelegate::tick 里轮询
    sceNpCommerceDialogUpdateStatus → FINISHED 时 GetResult
    result==PURCHASED → 通知 Lua（事件/回调）
  hasUnconsumedEntitlement(entitlement_label)  ← 客户端预查（可选）
    sceNpEntitlementAccessRequestUnifiedEntitlementInfo + Poll
```

**线程约束**：Commerce dialog 的 UpdateStatus/GetResult 是 common dialog 模式，
与现有 SigninDialog/LoginDialog 同构 —— 主线程 tick 轮询即可（登录功能已验证此模式）。
NpEntitlementAccess 的 Request/Poll 是异步请求模式（request id + poll），也可主线程。

**Meta 暴露给 Lua**（平台分支在 C++ 内切，PG Lua 只调统一接口）：
- `openPS5Checkout(product_label)` / `getPS5CommerceDialogState()`
- 现有 `unlockAchievement` 的模式照抄

### 客户端 Lua（Proven Ground）

```
chaos_html_ui_widget_recharge_steam.lua 加 PS5 分支：
  platform == "ps5" && isPS5Platform()
    → platform_delegate:openPS5Checkout(product_label)
    → 轮询 getPS5CommerceDialogState()（照抄 SigninDialog 的 tick 轮询模式）
    → PURCHASED 后调 RPC.CHARACTER.CLT2CHARACTERFinalizePS5RechargeOrder(entitlement_label)
```

设计表 `recharge_gold_table` 加 `platform="ps5"` 行 + PS5 商品 label 映射列。

### 服务端（charge_server，PS5 charge manager）

**新文件** `charge_manager/chaos_charge_server_charge_manager_ps5.lua`（与 dmm/xsolla 平级）：

```
onFinalizePS5RechargeOrder(character_id, entitlement_label):
  1. 生成 transactionId（幂等键，重试必须复用 —— 存 charge_order_info）
  2. S2S 调 Entitlements WebAPI（Bearer token，复用登录服的 PSN OAuth 基建）:
     PUT /api/entitlement/v2/users/{accountId}/entitlements/{label}
         body: { transactionId: "..." }        ← PSVC 不传 useCount（全部消耗）
  3. 200 → amountConsumed → 发货（CHARGE2CHARACTERChargeAddGold）
     → 记 charge_order_info（复用现有表：order_id/product/state）
  4. 5xx/超时 → 用同 transactionId 重试（tick 驱动，照抄 SteamOrderRetry 模式）
```

**服务端 S2S 认证**：登录服已有 PSN OAuth token 交换（`chaos_login_user_ps5.lua`
的 client credentials 流）。支付复用同一 client_id/secret 拿 Bearer，
或走 Auth Web API 的 S2S token —— 与登录基建共用。

**登录态关联**：服务端需要玩家的 PSN `account_id` 才能查 entitlement。
登录时已经拿到（S2S userinfo 换过 account_id）→ 存玩家档案，支付时取用。

## 3. 关键 API 备忘（文档已验证）

| API | 用途 | 约束 |
|---|---|---|
| `sceNpCommerceDialogOpen`(CHECKOUT) | 购买弹窗 | targets=商品label数组；已购/不可购商品会报错 |
| `sceNpCommerceDialogUpdateStatus/GetResult` | 轮询结果 | PURCHASED 结果后同步钱包 |
| `sceNpCommerceShowPsStoreIcon` | 商店图标 | **展示 PS Store 商品时必须显示**（合规） |
| `getContainer`（In-Game Catalog） | 查商品/价格 | 价格展示规则（划线价/PS+折扣）必须遵守 |
| `listEntitlements`（S2S） | 查所有权 | GET /v2/users/me/entitlements |
| `consumeEntitlement`（S2S） | 消耗 | PUT，幂等（transactionId），PSVC 不传 useCount |
| `sceSystemServiceReceiveEvent` | 店外购买事件 | UNIFIED_ENTITLEMENT_UPDATE → 触发钱包同步 |

## 4. 改动文件清单

**Chaos 引擎**（`H:\cb2\dev\chaos\_source\_engine`）：
- `client/{public,private}/chaos/client/platform/chaos_ps5_commerce_context.{h,cpp}` — 新增
- `chaos_platform_delegate.{h,cpp}` — deferred init 挂 commerce + tick 轮询 + Meta 暴露
- `chaos_client_global_context.{h,cpp}` — 持有 commerce context
- `client/CMakeLists.txt` — 链接 NpCommerce/NpCommerceDialog/NpEntitlementAccess/NpCppWebApi stub

**Proven Ground**：
- `_source/_scripts/client/ui/widgets/chaos_html_ui_widget_recharge_steam.lua` — PS5 分支
- `_source/_scripts/client/chaos_client_player_description.lua` — 对话框状态轮询（如需）
- `_source/_scripts/server/charge_server/charge_manager/chaos_charge_server_charge_manager_ps5.lua` — 新增
- `_source/_scripts/server/charge_server/rpc/chaos_charge_server_rpc_handler.lua` — 注册 PS5 RPC
- 设计表 `recharge_gold_table` — PS5 行 + 商品 label（策划/运营配）

## 5. 配置侧前置（非代码）

1. **PS Store 商品配置** — 虚拟货币商品在 DevNet 配置（SKU/label/价格/PSVC 类型）
2. **service label** — NP service label（Apply 时分配，与奖杯同一个）
3. **Client ID 权限** — 现有 client_id 需加 entitlements scope（DevNet 申请）
4. **沙盒测试账号** — DevKit 测试钱包（DevNet 有 test funding）

## 6. 验证路径

1. 编译 + DevKit 启动：commerce context 初始化日志
2. In-Game Catalog 查商品（getContainer 返回配置的商品）
3. CHECKOUT 弹窗 → 测试钱包购买 → PURCHASED 结果
4. 服务端 consume（S2S）→ amountConsumed → 金币到账 → charge_order_info 落库
5. 幂等：同 transactionId 重发 consume，确认不重复扣
6. 回归：非 PS5 平台充值不受影响

## 7. 风险/待确认

1. **NpCppWebApi 依赖链最重**（C++ 封装层，libSceNpCppWebApi + Http2 + Json2）——
   若只用 CHECKOUT 弹窗 + 服务端查 entitlement，客户端可跳过 Catalog 自绘，
   用游戏自己的商品列表（label 硬编码/配置），省掉 NpCppWebApi 整条依赖。
   建议 V1 先跳过，V2 再做合规自绘商店。
2. **价格展示合规** — 若 V1 不自绘商店则无此问题；CHECKOUT 弹窗价格由系统渲染，天然合规。
3. **服务端 Bearer 获取方式** — 复用登录服 client credentials，还是 Auth Web API？
   实现时看登录服现有 token 管理怎么扩展最省。
4. **店铺外购买**（网页/手机 PS Store 买币）— SystemService 事件监听是加分项，V1 可后置。


---

## 实施状态（2026-08-26 更新）

### 已完成（全部代码已提交，分支 feature/CB2N-29569-ps5-trophy-payment）

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

### 遗留
- 设计表 recharge_gold_table 加 ps5 行 + ps5_product_label 列（替换 TEST 写死）
- client_id 确认有 entitlements scope（token 400 时查）
- Client Secret 生产前必须轮换（已泄漏过）
- GuardianModeManager 的 URL 缺斜杠 bug（2023年老bug，与支付无关，未修）
- 客户端 dll 重编（含 getCheckoutState/GetResult 两修复）后才能全链路实测
