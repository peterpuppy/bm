# PS5 奖杯 — 进度

> **Jira**：CB2N-30497
> **分支**：`feature/CB2N-30497-ps5-trophy`（Chaos + Proven Ground，base: master）
> **状态**：DevKit 实机验证通过，已推远端。
> **方案**：[PLAN.md](PLAN.md) ｜ **配置流程**：[CONFIG.md](CONFIG.md)

---

## 已完成

- **Chaos C++**：`chaos_ps5_trophy_context.{h,cpp}` —— NpTrophy2 context/handle 生命周期
  + UDS `_UnlockTrophy` 事件 post + `sceNpCheckCallback` 驱动解锁回调
- **`PlatformDelegate::unlockAchievement(DID)`** 加 PS5 分支：DID → `m_ps5_trophy_id_map`
  → `unlockTrophy(trophy_id)`
- **CMake**：Prospero 链接 NpTrophy2 / NpUniversalDataSystem / Np stub
- **用户切换**：`registerPS5TrophyForCurrentUser()` 每 tick 自守卫，换用户自动重注册
- **配置**：`nptitle.dat` 放 `_content/PS5/sce_sys/`；UDS 走 Local Mode

## 成就触发事件调整

`create_character` → 复用 `login`（首次登录即解锁「创建第一个角色」）。
**只改设计表，PS5 侧零改动** —— UDS 只认 `trophy_id`，不知道触发原因。
详见 [CONFIG.md](CONFIG.md)。

---

## 验证方式

```bash
# 重测解锁前先清奖杯 + UDS 数据（需先退出游戏）
prospero-ctrl application delete-data trophy all /user:<User>
prospero-ctrl application delete-data uds all /user:<User>
```

用户名到 PS5 用户简介处查看。
