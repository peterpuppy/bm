# PS5 奖杯接入方案（CB2N-待分配）

## 0. 前置结论（颠覆初版设想）

初版设想"调 `sceNpTrophy2UnlockTrophy` 直接解锁"——**该函数在 SDK12 不存在**。

`NpTrophy2-Reference` 全函数清单：create/destroy-context、register-context、create/destroy-handle、get-{game,group,trophy}-info、register/unregister-unlock-callback、show-trophy-list、progress 等。**没有任何 unlock 函数**。NpTrophy2 库是只读+回调。

PS5 SDK12 解锁走 **NpUniversalDataSystem (UDS) 事件**：

```
应用 post UDS 事件 "_UnlockTrophy" { "_trophy_id": N }
  → 系统更新 UDS Stat
  → 系统比对奖杯条件（UDS Management Tool / GEMS 配置）
  → 满足则系统自动解锁
  → sceNpCheckCallback() 周期调用时触发已注册的 unlock 回调
```

文档来源：`Trophy_System-Overview/implementation-of-trophy-unlocking.md`

---

## 1. 现状（已存在，不重复造）

```
服务端 CharacterAchievementManager (Lua) → DB character_achievements 表
客户端 ClientAchievementManager (Lua) → 条件评估 + UI toast
平台解锁入口：platform_delegate:unlockAchievement(achievement_did)   [Lua player_description.lua:15827/15840 已调]
  └─ PlatformDelegate::unlockAchievement(DID)  [C++ chaos_platform_delegate.cpp:244]
       └─ Win32: DID→Steam api_name 映射 → SteamUserStats()->SetAchievement
       └─ PS5:  空操作（当前 return k_false）
```

集成点已在。本方案 = 给 PS5 分支填实现。

---

## 2. 涉及的 PS5 SDK 库（3 个，都要链接 stub + load PRX）

| 库 | 用途 | stub |
|---|---|---|
| NpTrophy2 | context/handle 生命周期 + 解锁回调 + 读奖杯数据 | libSceNpTrophy2_stub_weak.a |
| NpUniversalDataSystem | post `_UnlockTrophy` 事件（**真正的解锁动作**） | libSceNpUniversalDataSystem_stub_weak.a |
| Np (base) | `sceNpCheckCallback`（驱动 unlock 回调）+ NP Title ID 设置 | libSceNp_stub_weak.a（确认是否已链接） |

现有 `initializePS5()` 已 load：SIGNIN_DIALOG / LOGIN_DIALOG / NP_AUTH。**未 load**：NP / NP_TROPHY2 / NP_UTILITY / NP_UNIVERSAL_DATA_SYSTEM。

---

## 3. 生命周期

挂到现有 `initializePS5()` / `finalizePS5()`（同 PS5 登录 + SaveData 的挂法）。

### initializePS5() 末尾追加
```
1. sceSysmoduleLoadModule(SCE_SYSMODULE_NP)              // base NP（若未 load）
2. sceSysmoduleLoadModule(SCE_SYSMODULE_NP_TROPHY2)
3. sceSysmoduleLoadModule(SCE_SYSMODULE_NP_UTILITY)      // sceNpCheckCallback
4. sceSysmoduleLoadModule(SCE_SYSMODULE_NP_UNIVERSAL_DATA_SYSTEM)
5. sceNpInitialize(...)  /  sceNpSetNpTitleId(NPWR62682_00, secret)   // 设置 NP Title ID（奖杯 context 依赖）
6. setupTrophyContext(user_id)   // 子线程：CreateContext + RegisterContext（阻塞，必须子线程）
7. setupUDSContext(user_id)      // UDS context/handle
8. sceNpTrophy2RegisterUnlockCallback(callback)  // 注册解锁回调
```

### finalizePS5() 开头追加（逆序）
```
sceNpTrophy2UnregisterUnlockCallback()
destroyUDSContext()
destroyTrophyContext()   // DestroyContext
sceSysmoduleUnloadModule × 4
```

**NpCommunicationId `NPWR62682_00`** 用在 step 5（NP Title ID 设置），不是直接传给 trophy context。trophy context 用 `SceNpServiceLabel`（int），service label 从 NP title 配置派生。

---

## 4. 解锁实现（核心）

`PlatformDelegate::unlockAchievement(DID)` 加 PS5 分支：

```cpp
#elif defined(CHAOS_PLATFORM_PROSPERO)
    Map<DID, Int>::const_iterator itr = m_ps5_trophy_id_map.find(achievement_did);
    if (itr != m_ps5_trophy_id_map.end())
    {
        return postUnlockTrophyEvent(itr->second);  // UDS 事件，fire-and-forget
    }
    return k_false;
```

`postUnlockTrophyEvent(Int trophy_id)`：
```cpp
SceNpUniversalDataSystemEvent* event = nullptr;
SceNpUniversalDataSystemEventPropertyObject* prop = nullptr;
sceNpUniversalDataSystemCreateEvent("_UnlockTrophy", nullptr, &event, &prop);
sceNpUniversalDataSystemEventPropertyObjectSetInt32(prop, "_trophy_id", trophy_id);
sceNpUniversalDataSystemPostEvent(m_uds_context, m_uds_handle, event, 0);
sceNpUniversalDataSystemDestroyEvent(event);
```

**注意**：这是 fire-and-forget。真正解锁由系统异步完成，通过 `sceNpCheckCallback()` 驱动回调通知。Lua 侧 `unlockAchievement` 本来就不看返回值，契合。

---

## 5. DID → trophy_id 映射

Steam 用 `m_platform_achievement_id_map`（`Map<DID,String>`，api_name）。PS5 要 `m_ps5_trophy_id_map`（`Map<DID,Int>`，trophy 数字 ID）。

**来源选择**：
- **(a) 复用 `PlatformAchievementInfo`**，加 PS5 trophy_id 字段。设计表一处维护，Steam/PS5 同源。但要改设计表 schema + GamePreloadRSA 结构。
- **(b) PS5 专用映射配置**，独立加载。

**倾向 (a)**，跟 Steam 同源。`PlatformAchievementInfo` 现有 `m_did` + `m_api_name`（Steam），加 `m_ps5_trophy_id`（Int）。`load()` 里 PS5 分支读这个字段填 `m_ps5_trophy_id_map`。

⚠️ trophy_id 必须与 UDS Management Tool / GEMS 配置的奖杯 ID 一致，否则事件 post 出去解锁不了。这是配置侧约束，不是代码约束。

---

## 6. 解锁回调 + sceNpCheckCallback 驱动

```cpp
void onTrophyUnlocked(SceNpTrophy2Context, SceNpTrophy2Id trophy_id, void*)
{
    LOG_INFO("PS5 trophy unlocked: id={0}", trophy_id);
    // 可选：通知 Lua 显示 UI toast（但游戏自己的成就 toast 已由 ClientAchievementManager 处理）
}
```

`sceNpCheckCallback()` 需周期调用 —— 挂到引擎主线程 tick（参照 SaveData tick 的挂法，`chaos_client_tick_manager.cpp`）。**这个 tick 是主线程**，但 `sceNpCheckCallback` 只是把已就绪的回调派发到当前线程，不是阻塞 IO，主线程安全（与 SaveData Prepare 的子线程要求不同）。

---

## 7. 线程约束（查文档确认）

| 函数 | 约束 | 来源 |
|---|---|---|
| `sceNpTrophy2RegisterContext` | **阻塞，必须子线程**，不能 time-critical 线程 | register-context.md Notes |
| `sceNpTrophy2GetTrophyInfo` | 耗时，建议子线程 | using-the-library.md |
| `sceNpTrophy2CreateContext` | 无明确子线程要求 | create-context.md |
| `sceNpUniversalDataSystemPostEvent` | 待确认（UDS 文档未读，假设可主线程，实测验证） | — |
| `sceNpCheckCallback` | 主线程（派发回调用） | Np 文档 |

`RegisterContext` 的子线程要求与 SaveData 的 `Prepare` 同构 —— 复用 `PS5DataArchive::runWriteTransaction` 那套 `g_common_system_task_scheduler->addTask` + `waitForSingleTaskCounter` 模式。考虑把那个子线程事务封装抽到更通用的工具里（SaveData 和 Trophy 共用）。

---

## 8. .trp / 奖杯配置文件（构建侧，非代码）

文档 `placement-of-the-trophy-configuration-and-uds-configuration.md`：

- 奖杯配置在 **UDS Management Tool** 完成（不是代码，不是 .trp 手写）
- 配置完从 **GEMS**（Package/Disc Management Tool）下载 `npconfig.zip`
- 解压到应用二进制的 **`sce_sys/`** 目录
- 包含 trophy 配置文件 + UDS 配置文件

**开发期**：DevKit 的 UDS Development Mode 设 Local Mode，系统读本地安装的配置文件。

**这块归构建管线**，不归本代码 feature。需要确认：
- sce_sys 目录现在有没有？放没放 npconfig？
- 谁负责从 GEMS 拉 npconfig.zip？

---

## 9. 改动文件清单

### Chaos 引擎（`H:\cb2\dev\chaos\_source\_engine`）
- `source/client/CMakeLists.txt` — PS5 链接 NpTrophy2 / NpUniversalDataSystem / Np stub
- `source/client/public/chaos/client/platform/chaos_platform_delegate.h` — PS5 trophy 字段（context/handle/uds_context/uds_handle/trophy_id_map）+ 方法声明
- `source/client/private/chaos/client/platform/chaos_platform_delegate.cpp` — initializePS5/finalizePS5 挂载 + unlockAchievement PS5 分支 + postUnlockTrophyEvent + onTrophyUnlocked 回调
- `source/client/private/chaos/client/tick/chaos_client_tick_manager.cpp` — tick 调 sceNpCheckCallback（PS5）
- 设计表/`PlatformAchievementInfo` — 加 m_ps5_trophy_id 字段（若走方案 a）

### Proven Ground
- 无 Lua 改动（`unlockAchievement(DID)` 调用点已存在，平台分支在 C++ 侧切换）

### 构建/配置（非代码）
- sce_sys/ 放置 npconfig（GEMS 下载）
- DevKit UDS Development Mode 设 Local Mode

---

## 10. 验证

1. **编译**：Chaos Prospero 构建，3 个 stub 链接通过
2. **DevKit 实测**：
   - 启动 → initializePS5 调 trophy context create+register（子线程，看日志）
   - 触发一个成就 → `unlockAchievement(DID)` → post `_UnlockTrophy` 事件
   - sceNpCheckCallback 触发 → `onTrophyUnlocked` 回调日志
   - 系统"奖杯"界面看到该奖杯解锁
3. **Local Mode**：DevKit UDS Local Mode 下，系统读本地配置，不连 PSN 也能验证解锁流程
4. **回归**：非 PS5 平台 unlockAchievement 走原 Steam 分支，不影响

---

## 11. 待确认/风险

1. **NP Title Secret**：`sceNpSetNpTitleId` 需要 NP Title ID + Secret。ID 是 `NPWR62682_00`，Secret 从哪来？（PS5 登录申请 Client ID 时一起拿到的？需确认）
2. **sce_sys/npconfig**：现在有没有？谁放？没这个文件 RegisterContext 会报 `SCE_NP_TROPHY2_ERROR_TITLE_CONF_NOT_INSTALLED` (0x8055391e)
3. **UDS PostEvent 线程约束**：未读 UDS 文档，假设可主线程，实测验证
4. **trophy_id 与设计表 DID 的对应**：UDS Management Tool 配置的 trophy_id 必须与 `PlatformAchievementInfo.m_ps5_trophy_id` 一致，配置侧约束
5. **NP base 模块是否已 load**：现 initializePS5 只 load NP_AUTH，未 load NP。需确认 `sceNpInitialize` 是否已在别处调（prospero_platform.cpp grep 命中但未确认）
6. **子线程事务封装复用**：SaveData 的 runWriteTransaction 模式可抽通用，Trophy 的 RegisterContext 共用
