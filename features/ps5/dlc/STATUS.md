# PS5 DLC — 进度

> **最后更新**：2026-09-07
> **状态**：调研完成，未开工
> **Jira**：未分配

---

## 现在在哪

只做了文档调研，**一行代码没写**。方案见 [PLAN.md](PLAN.md)。

卡在一个需要你决定的岔路：

```text
PSAL（不带数据）   内容在主包里，只卖权利钥匙
                  客户端加一次权利查询 + 一处放行判断
                  不依赖 AppContent 库，文档缺口影响小
                  上传 GEMS 后自动在开发环境发布，不用等 PAR/Availability

PSAC（带数据）     单独打包上传 GEMS，玩家下载安装
                  要 AppContent 库挂载 + 资源路径 + 重下载引导
                  AppContent 文档没抓，必须补爬
```

选定之前没法细化实现。

---

## 已确认的事实

| 结论 | 来源 |
|---|---|
| 权利判定用 `NpEntitlementAccess`，两个 API（单查 / 列表） | `accessing-additional-content.md:47-61` |
| **禁止缓存权利状态**，每次用前必须查（TRC R5116） | 同上 `:65` |
| 权利运行时会变，监听 `SCE_SYSTEM_SERVICE_EVENT_ENTITLEMENT_UPDATE` | 同上 `:69-78` |
| 收事件的前提是 AppContent 库已初始化 | 同上 `:84` |
| PSAC 可能「权利有效但数据未安装」，要引导重下 | `additional-content-for-purchase.md:226` |
| DLC 必须挂 **PSSDC** 服务，挂 Commerce Catalog 会导致游戏内挂载不了 | `product-configuration-and-handling.md:39-42` |
| PSAC/PSAL 的 label 在 **GEMS** 建，PSVC 在 Content Pipeline 建 | `entitlement-types.md:86-89` |
| 开发期可用 Add Content Manager 逐个禁用权利测 R5116 | `development-support-features-for-additional-content.md:102-107` |
| 单 label 上限 2499 个 DLC，8 个 label 共 19992 | `accessing-additional-content.md:41` |

---

## 发现的隐患（做 DLC 前必须处理）

支付代码里 `serviceName` 写死成 `COMMERCE_CATALOG_AND_ENTITLEMENTS`
（`chaos_ps5_commerce_context.cpp:72`）。虚拟货币这样是对的，**DLC 必须用 PSSDC**。
需要按商品类型分流。

DevNet 侧两个服务的 NP Service Label 都是 0，共用同一个 title ID，
所以分流只能靠代码里选 `serviceName`，不能靠 label 区分。

---

## 下一步

1. **你定 PSAL 还是 PSAC**
2. 走 PSAC 的话补爬 AppContent 文档（命令见 PLAN.md 第 6 节）
3. 确认 DLC 是否影响服务端逻辑（决定要不要做服务端复查）
4. 申请 Jira 号 + 建分支（base 用 master 还是支付分支，看是否复用 S2S 基建）

---

## 未决问题

- NpEntitlementAccess 的 Get* 系列线程约束：文档没写，需实测。
  保守按子线程设计（复用 `runOnPS5Subthread`）
- `getEntitlement`（WebAPI）对 client credential 是否可用 ——
  和支付的 `consumeEntitlement` 是同一类问题，那边已确认标注 Not Usable
