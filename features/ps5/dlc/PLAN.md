# PS5 DLC（追加内容）接入方案

> **状态**：调研完成，未开工。等确认走 PSAL 还是 PSAC。
> **Jira**：未分配
> **前置**：登录（CB2N-27968，已合）、支付（CB2N-30579，进行中）

---

## 0. 两条路，先选

PS5 的 DLC 有两种包类型，工作量差一个量级。来源
`PlayStation_Store_Content-Guidelines/additional-content-for-purchase.md:178-181`。

| | PSAL（不带数据） | PSAC（带数据） |
|---|---|---|
| 内容在哪 | 主包里已有 | 单独打包，玩家下载安装 |
| 要不要打包 | 不用 | 要，上传 GEMS |
| 游戏怎么用 | 查权利 → 放行 | 查权利 → AppContent 挂载 → 读资源 |
| 用到的库 | NpEntitlementAccess | NpEntitlementAccess + **AppContent** |
| 典型用途 | 解锁已有内容、时装、功能开关 | 新关卡、新角色、新场景 |
| 未安装的情况 | 不存在 | 要处理：权利有效但数据没下载 |

**PSAL 只需权利检查**，客户端加一个查询 + 一处放行判断即可。
**PSAC 还要处理包挂载、资源路径、重下载引导**，且依赖 AppContent 库（文档缺口，见第 6 节）。

另有两种也走 unified entitlement，但不属于本方案：
`PSCONS`（消耗品，如弹药）、`PSVC`（虚拟货币，已在支付功能实现）。

---

## 1. 权利判定 API

核心库 `NpEntitlementAccess`——支付功能已引入过（虚拟货币教程里用它查未转移权利）。

### 单个 DLC：直接查

来源 `NpEntitlementAccess-Overview/accessing-additional-content.md:50-61`。

```cpp
SceNpServiceLabel serviceLabel = 0;
SceNpUnifiedEntitlementLabel entitlementLabel;
memset(&entitlementLabel, 0, sizeof(entitlementLabel));
strncpy(entitlementLabel.data, "0000111122223333", SCE_NP_UNIFIED_ENTITLEMENT_LABEL_SIZE);
SceNpEntitlementAccessAddcontEntitlementInfo info;

ret = sceNpEntitlementAccessGetAddcontEntitlementInfo(serviceLabel, &entitlementLabel, &info);
if (ret != SCE_OK) {
    // SCE_NP_ENTITLEMENT_ACCESS_ERROR_NO_ENTITLEMENT = 没买/被撤销
}
```

### 多个 DLC：先取个数再取列表

```cpp
// 第一次传 NULL 只取个数
SceNpEntitlementAccessAddcontEntitlementInfo* list = NULL;
uint32_t listNum = 0;
uint32_t hitNum;
ret = sceNpEntitlementAccessGetAddcontEntitlementInfoList(serviceLabel, list, listNum, &hitNum);

// 按个数分配后再取
list = (SceNpEntitlementAccessAddcontEntitlementInfo*)malloc(sizeof(*list) * hitNum);
listNum = hitNum;
ret = sceNpEntitlementAccessGetAddcontEntitlementInfoList(serviceLabel, list, listNum, &hitNum);
```

**上限**：单个 service label 最多 2499 个；label 可用 0-7 共 8 个，
单应用理论上限 19992 个（`:41`）。

注意（`:42-43`）：
- 开发环境用非 0 的 service label 时，启动时必须已登录 PSN 且网络可用
- 存在非 0 label 的同名应用时，那个应用的 entitlement label 也会混进列表

---

## 2. 三条硬约束

### 2.1 禁止缓存权利状态（TRC R5116）

`accessing-additional-content.md:65` 原文：

> `sceNpEntitlementAccessGetAddcontEntitlementInfoList()` or
> `sceNpEntitlementAccessGetAddcontEntitlementInfo()` **must always be used** to check
> whether or not an additional content entitlement is valid.
> (Do not use information saved to non-volatile storage such as save data to check.)

PS5 的 DRM 允许权利**从有效变回无效**（退款、有效期结束）。TRC **R5116** 要求这种情况下
应用必须相应地限制访问。

> there is a possibility that this will be difficult depending on the specifications of
> the additional content; therefore, thorough consideration is recommended at early
> stages of game/specification design.

**和奖杯相反**：奖杯是一次性事件（解锁即结束），DLC 权利是**持续状态**，每次用前都要查。
不能存进存档、不能存进服务端数据库当权威依据。

### 2.2 运行时权利会变，要监听事件

`SCE_SYSTEM_SERVICE_EVENT_ENTITLEMENT_UPDATE`（SystemService 库）。触发场景（`:69-74`）：

- 用户登录 / 登出
- 从 PS Store 买了权利
- PSAL（不带数据的追加内容）安装完成
- 有效期结束

**前提**：AppContent 库必须初始化过才能收到这个事件（`:84`）。
`sceAppContentInitialize()` 被调用时本身也会发一次这个通知（`:80`）。

系统**不会**在权利被撤销时自动限制访问（`:78`），必须应用自己处理。

### 2.3 买了不等于装了（仅 PSAC）

`additional-content-for-purchase.md:226`：

> there may be cases where additional content with extra data has been purchased but the
> data does not exist. If additional content has not been installed, it is required to
> re-download the additional content.

数据状态包含在 `sceNpEntitlementAccessGetAddcontEntitlementInfo` 返回的 `info` 里。
缺数据要引导重新下载。

---

## 3. ⚠ 当前配置的隐患：service 选错 DLC 挂不上

`PSN_Commerce-Programming_Guide/product-configuration-and-handling.md:39-42` 原文：

> Additional Content should be linked using the **PlayStation®Store Delivered Content**
> service. Products linked by the **Commerce Catalog and Entitlements** services are
> **not accessible through AppContent or the NpEntitlementAccess library** and therefore
> will be unable to be mounted during gameplay.

DevNet 侧两个服务都配了，NP Service Label 都是 0：

```text
PlayStation™Store Delivered Content     NP Service Label: 0    HP3255-PPSA38951_00
Commerce Catalog and Entitlement        NP Service Label: 0    HP3255-PPSA38951_00
```

而支付代码里写死的是后者（`chaos_ps5_commerce_context.cpp:72`）：

```cpp
param.serviceName = SCE_NP_SERVICE_COMMERCE_CATALOG_AND_ENTITLEMENTS;
```

**虚拟货币用这个是对的，DLC 必须用 PSSDC。** 做 DLC 时第一件事就是把 `serviceName`
按商品类型分流，不能继续写死。

---

## 4. 标签在哪建 —— 和虚拟货币不是同一个工具

`Entitlements-Overview/entitlement-types.md:86-89`：

| 包类型 | Entitlement label 创建位置 |
|---|---|
| PSGD / **PSAC** / **PSAL** | **PS5 GEMS** |
| PSVC / PSCONS / PSSUBS | Content Pipeline |

虚拟货币的 `CONQCOIN00000000` 是在 Content Pipeline 建的。**DLC 要去 GEMS**，流程不同。

Label 都是 16 位。同一个 label 在不同 Service ID 的 title 间语义相同（`:93`），
所以跨区版本可以共用一套判定代码。

### 打包侧要点（PSAC）

`additional-content-for-purchase.md:270-284`：

```text
GP5 file:   volume_type = "prospero_ac"（PS5 Additional Content Package）
            并设置 "Entitlement Key"
Param file: Publishing Tools GUI → New Project → "Additional Content Package with Extra Data"
内容信息:    必须明确标示这是追加内容
```

PSAL 更简单（`:292-304`）：不需要数据，在 GEMS 里建 PSAL 权利并设 Entitlement Key，
上传一个 zip 即可。**上传完成后会自动在开发环境发布**（`:309`）——
不像 PSVC 要等 PAR / Availability。

### Entitlement Key 的用途

`NpEntitlementAccess-Overview/usage-of-an-entitlement-key.md:90-92`：
`sceNpEntitlementAccessGetEntitlementKey()` 只在用户拥有权利时才能取到，
所以可以当作「绑定在 DLC 上的受限数据」用。

---

## 5. 开发期测试手段（比支付友好得多）

不依赖 Availability 日期、不用等 PAR 审核。来源
`NpEntitlementAccess-Overview/development-support-features-for-additional-content.md:96-119`。

| 工具 | 路径 | 用途 |
|---|---|---|
| Package Installer | ★Debug Settings > Game | 本地安装 PSAC 包 |
| **Add Content Manager** | ★Debug Settings > Game | 列出已装 DLC；**逐个禁用/启用权利**；逐个删除 |
| Require purchased license | ★Debug Settings > PSN，设为 "Additional Contents" | 忽略 Add Content Manager，按开发环境购买历史判定 |
| DevAdmin Tool | 外部工具 | 清开发环境购买历史 |
| Restore Licenses | Settings > Users and Accounts > Other | **清完购买历史后必须执行**，否则权利不会回到未购买态 |

**Add Content Manager 能逐个禁用权利**，正好用来测 R5116 要求的
「权利被撤销后限制访问」——被禁用的 DLC 会从 `GetAddcontEntitlementInfoList` 消失，
`GetAddcontEntitlementInfo` 返回 `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NO_ENTITLEMENT`。

系统软件的「管理游戏内容」界面（图标上按 Options）也能删 DLC，但那是给玩家用的，
开发期测试用 Add Content Manager（`:110-112`）。

---

## 6. ⚠ 文档缺口：AppContent 库没抓

`docs/sdk_12_crawl_report.md:2137-2145` 标为 `⬜ Not crawled`：

```text
AppContent Library Overview   → output/psn_12/System/Application_Content/AppContent-Overview/
AppContent Library Reference  → output/psn_12/System/Application_Content/AppContent-Reference/
```

**这是 PSAC 挂载的核心库。** `sceAppContentInitialize` 在别的文档里被反复引用
（收权利更新事件的前提），但它自己的 Overview / Reference 没有，
缺的是：挂载点路径、mount 语义、下载状态查询、追加内容标识符的完整定义。

补爬（按 `document/README.md` 的注意事项，**必须传第二参数** `output/psn_12`）：

```bash
cd features/ps5/document
python scripts/crawl_subtree.py https://game.develop.playstation.net/resources/documents/SDK/12.000/AppContent-Overview/__toc.html output/psn_12
python scripts/crawl_subtree.py https://game.develop.playstation.net/resources/documents/SDK/12.000/AppContent-Reference/__toc.html output/psn_12
```

补爬后 `_index.json` 可能落在 `output/_index.json`（错位置），需手动并入
`output/psn_12/_index.json`。

**走 PSAL 的话这个缺口影响很小** —— AppContent 只需初始化（为了收事件），不需要挂载。

---

## 7. 实现草案（待选定类型后细化）

### 客户端 C++（Chaos）

照 `PS5TrophyContext` / `PS5CommerceContext` 的模式：
`platform/` 下独立文件 + `ClientGlobalContext` 持有 + 分阶段初始化。

```text
chaos_ps5_entitlement_context.{h,cpp}   新增
  initialize()          deferred 首帧：load PRX NP_ENTITLEMENT_ACCESS
                        + sceNpEntitlementAccessInitialize
                        + （PSAC 需要）sceAppContentInitialize
  shutdown()
  hasEntitlement(label)         查单个，返回 Bool
  refreshEntitlementList()      查列表，填 map
  tick()                        轮询 SystemService 事件，收到
                                ENTITLEMENT_UPDATE 就重查

chaos_platform_delegate.{h,cpp}
  Meta 暴露给 Lua：hasPS5Entitlement(label) / refreshPS5Entitlements()

client/CMakeLists.txt
  libSceNpEntitlementAccess_stub_weak.a
  （PSAC 追加）libSceAppContent_stub_weak.a
```

**线程约束待确认**：NpEntitlementAccess 的 Get* 系列是否阻塞、能否主线程调，
文档里没明说。参照虚拟货币教程的做法是放子线程 job。保守起见先按子线程设计
（复用 `runOnPS5Subthread`），实测后再定。

### Lua 侧

DLC 内容的门禁点在哪，取决于卖什么。原则是**每次进入前查，不缓存**：

```lua
-- 伪代码
if client_lua_accessor:isPS5Platform() then
    local platform_delegate = g_client_global_context:get_m_platform_delegate();
    if not platform_delegate:hasPS5Entitlement(dlc_label) then
        -- 提示未购买 + 可选：拉起 CHECKOUT 弹窗卖它
        return;
    end
end
-- 放行
```

注意 `g_client_global_context`（不是 `g_lua_client_global_context`）——
支付的充值 widget 曾因为这个写错导致 PS5 分支从未跑通。

### 服务端

**PSAL / PSAC 的权利判定不经服务端** —— 是客户端直接问 PSN。

但如果 DLC 影响服务端逻辑（比如解锁的关卡要服务端也认），那就需要客户端把
判定结果上报，服务端**不能盲信**（客户端可改）。那种情况要走 Entitlements WebAPI
在服务端复查（和支付的 consumeEntitlement 同一套 S2S 基建，但用
`getEntitlement` 而非 `consumeEntitlement`，不消耗）。

⚠ 这条路会撞上支付功能同一个未决问题：`consumeEntitlement` 文档标注
client credential 不可用，`getEntitlement` 的使用限制表需要单独查证。

---

## 8. 待决问题

1. **PSAL 还是 PSAC？** 决定整个方案形态和工作量
2. **DLC 影响服务端逻辑吗？** 决定要不要做服务端复查
3. AppContent 文档补爬（走 PSAC 必须）
4. NpEntitlementAccess Get* 的线程约束（文档没写，需实测）
5. `getEntitlement`（WebAPI）的 client credential 可用性 —— 同支付的未决项
6. serviceName 分流：PSVC 走 Commerce Catalog，DLC 走 PSSDC

---

## 相关文档

- [STATUS.md](STATUS.md) — 进度
- `features/ps5/payment/` — 支付功能，共用 NpEntitlementAccess 与 S2S 基建
- 本地 SDK 文档：
  - `document/output/psn_12/PlayStationNetwork/Entitlements/NpEntitlementAccess-Overview/`
  - `document/output/psn_12/PlayStationNetwork/PlayStationStore/PlayStation_Store_Content-Guidelines/additional-content-for-purchase.md`
  - `document/output/psn_12/PlayStationNetwork/Entitlements/Entitlements-Overview/entitlement-types.md`

