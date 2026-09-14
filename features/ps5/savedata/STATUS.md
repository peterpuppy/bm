# PS5 本地存档（设置项持久化）— CB2N-29569

> **最后更新**：2026-08-10
> **Jira**：CB2N-29569
> **分支**：`feature/CB2N-29569-ps5-save-data`（Chaos + Proven Ground）
> **状态**：DevKit 实机验证通过 —— 改设置 → 重启 → `load success, 8 settings`，设置存活。

---

## 做了什么

把玩家设置项（`chaos_user_settings_{account_id}.xml` / `chaos_global_user_settings.xml`）从非持久的 `debugDataFolder` 改存到 PS5 标准 SaveData 挂载点，走 **Mount3 → Prepare → 写 → Commit** 事务。

**方案取舍**：用标准 SaveData（`sceSaveDataMount3`）而非 SaveDataMemory（KV 字节流）。原因是设置项本身是 XML 文件，挂载后 `/savedata0` 对 stdio 表现为普通文件系统，`XMLSerializer`（libxml2 → fopen）可以零改动复用；SaveDataMemory 需要把整表序列化成字节流整存整取，改动更大。

### 代码位置

| 文件 | 作用 |
|---|---|
| `client/public/chaos/client/platform/chaos_ps5_data_archive.h`<br>`client/private/.../chaos_ps5_data_archive.cpp` | **新增**。PS5 数据操作封装（仅 PS5 编译）：mount/unmount、prepare/commit、状态查询、`getRootPath()` |
| `client/private/.../platform/chaos_platform_delegate.cpp` | `initializePS5`/`finalizePS5` 挂 SaveData 生命周期；6 个 Lua 转发入口 + `getPS5UserID()` |
| `client/private/.../user_settings/chaos_user_settings_manager.cpp` | PS5 分支：路径取挂载点、写入包事务 |
| `client/CMakeLists.txt` | Prospero 追加 `libSceSaveData_stub_weak.a` |
| `platform/private/.../path/prospero/path.cpp` | `createDirectory` 修复：`stat` 返回值未检查（读未初始化结构体 = UB）、拼路径产生 `//savedata0` |
| `platform/private/.../file/prospero/file.cpp` | `isFileExists` 加 fopen 兜底：APR 是应用沙箱文件系统，解析不了 `/savedata0` |
| PG `_scripts/client/game_level/chaos_client_login_level.lua` | PS5 signin 成功后挂载存档 + 透传控制台用户 id |

### 关键约束（踩过的坑）

- **SaveData 挂载点不支持 `mkdir`**：`mkdir("/savedata0/_user_settings")` 返回 `errno=22 (EINVAL)`。所以 PS5 上设置文件直接写挂载点根目录，不建子目录（Windows 仍用 `_user_settings/` 子目录，两边布局不同是刻意的）。
- **APR 解析不了挂载路径**：`sce::Ampr::Apr::resolveFilepathsToIds` 只认 `/app0` 等沙箱路径，`/savedata0` 下的文件必然解析失败，需 fopen 兜底判存在性。
- **挂载时机在引擎启动早期（`initializePS5` 内），早于 `user_settings_manager->initialize()`**：mount 需要的 `userId` 在 `initializePS5` 里就拿到了（`sceUserServiceGetInitialUser`），与 PSN signin 无关，所以 mount 提前到 SDK init 之后、紧跟 `PS5DataArchive::initialize()`。这样 `user_settings_manager->initialize()`（`chaos_client_global_context.cpp:803`）读全局设置时 `/savedata0` 已存在，**第一次读就对**，不需要"挂载后重读"补丁。mount 失败则降级走回退目录（打 WARNING），不阻断启动。
- **事务资源句柄恒 `>0`**：`SceSaveDataTransactionResourceId` 是 `int32_t`，成功返回正值、失败返回负值、**永不为 0**，所以用 `0` 当"未创建"哨兵是安全的。
- **mount 参数**：`mount_mode = 33` = `CREATE2(32) | RDONLY(1)`，`blocks = 48`（48 × 64KB = 3MB）。`mountStatus == 0x1` 表示本次新建存档。

---

## ⚠️ 已知缺陷 / 技术债

### D1 —— `sceSaveDataPrepare()` 在主线程调用，违反 TRC R5089（**送认证前必须修**）

SDK 文档 `SaveData-Overview/notes-regarding-the-calling-source-thread.md:201-212` 明确点名 `sceSaveDataPrepare()`：该函数若在应用挂起流程刚开始时被调用，会阻塞调用线程直到挂起完成；而挂起要等 `suspendPoint()` 才继续，**因此从主线程调用会死锁**，必须放子线程（TRC **R5089**）。

当前调用链是纯主线程：

```
ClientTickManager::tickPostloads()        ← 主线程单线程段
  └─ UserSettingsManager::tick()
      └─ dumpUserSettingToFile()
          └─ PS5DataArchive::prepare() → sceSaveDataPrepare()   ← 命中禁止项
```

- **触发条件**：玩家按 PS 键 / 进入休息模式的瞬间正好发生一次设置落盘。概率低，常规测试碰不到。
- **影响**：认证硬性条款不通过；真实死锁风险。
- **修法**：把 SaveData 操作挪到子线程。需要先确认引擎线程设施（`TaskScheduler` / `JobQueue` / `ThreadManager` 是否有可用的异步任务队列），这是原方案就悬而未决的调研项。
- 我们用到的其他 API（`Mount3` / `Commit` / `Umount2` / `Initialize3`）不在硬名单内，文档只是"强烈建议"也放子线程。**硬伤仅 `prepare()` 一处。**

### D2 —— commit 失败会卡死本次会话的后续写入

`commit()` 失败时状态停留在 `prepared`，而 `dumpUserSettingToFile` 里 `isMounted()` 对 `prepared` 也返回 true → 再次 `prepare()` 因状态不符被拒 → 此后所有写入都失败，直到 unmount（退出时）才复位。

`prepare()` 内部有 `LOG_ERROR`，日志可见。commit 失败属于磁盘满/存档损坏级异常，暂不加恢复逻辑。

### D3 —— 二次登录不重新绑定存档

`mount()` 在已挂载时返回 `k_false`（"already mounted"），Lua 侧 `if ok == k_true` 于是跳过 `setCurrentAccountID`。首次已绑定所以正常工作；只有"登出后切换控制台用户再登录"会绑到旧用户。

正确修法是控制台用户切换时先 unmount 再 mount，依赖用户切换事件监听（与登录 P2-1 同一基础设施）。

### D4 —— PS5 未挂载时的回退路径

`getRootPath()` 未挂载时回退 `debugDataFolder`，且不带 `_user_settings/` 子目录。该路径在 PS5 上非持久（很可能只读），写入失败的症状只有 libxml2 的 `I/O error`。mount 失败本身在 `mount()` 内有 `LOG_ERROR`，`load begin` 日志也带 `mount_state`，信息不缺。

---

## 已修复的问题（留档备查）

| 问题 | 现象 | 修法 |
|---|---|---|
| 全局设置写得进读不回 | 音乐/音量/守护模式每次启动都是默认值 | mount 提前到 `initializePS5()` 内，使 `user_settings_manager->initialize()` 第一次读就在挂载之后 |
| `account_id` 语义被复用 | Lua 曾把**控制台用户 id** 塞进 `setCurrentAccountID`，进游戏后又被游戏服账号覆盖，产生两份设置文件（前一份无用） | 删掉 Lua 里那段透传：PS5 分支不再碰 account_id，交回原有游戏服流程，行为与 Windows 完全一致 |
| 层越界 + 隐藏副作用 | `startPS5SaveDataMount` 曾在挂载后偷调 `user_settings_manager->initialize()` 重读全局设置 | mount 提前到 `initializePS5()` 后，第一次读就对，重读补丁整个消失 |

---

## 上线前收尾（非阻塞）

| 项 | 位置 |
|---|---|
| 常规流程日志降级到 INFO（现在都是 WARNING），`load FAILED` 措辞偏惊悚（首次启动无文件是正常情况） | `chaos_user_settings_manager.cpp`、`login_level.lua` 5 条 `[PS5SaveData]` |
| 去掉开发期防御检查 `type(platform_delegate.startPS5SaveDataMount) == "function"` | `login_level.lua:2870` |
| magic number `48, 33` 提取为常量 | `login_level.lua:2871` |

---

## 如何验证

按顺序搜日志关键字。注意**按账号的用户设置要等游戏服登录返回后**才加载（account_id 从 0 变成真实账号才触发），所以要进到游戏里再看：

| 阶段 | 关键字 | 预期 |
|---|---|---|
| 引擎启动（initializePS5） | `PS5 SaveData mounted` | `mountStatus=0x1`（新建）或其他值（复用） |
| 引擎启动（紧跟其后） | `load begin`（全局设置） | 路径为 `/savedata0/chaos_global_user_settings.xml` |
| 进游戏（游戏服登录返回） | `load begin` | `path=/savedata0/chaos_user_settings_<游戏服账号>.xml`, `mount_state=1` |
| 首次进游戏 | `load FAILED: file not found` | **预期**（存档里还没这个账号的文件） |
| 改一个设置 | `committed` | 出现即写成功，**中间无 `I/O error`** |
| 重启后再进游戏 | `load success, N settings` | **最终验收点** |

两类设置要分别验证：
- **按账号的用户设置**：骑乘模式 `ride_mode`（`chaos_client_player_description.lua:11003`）、相机模式 `camera.enable_stand_alone`
- **全局设置**：音量/背景音乐（`chaos_sound_manager.cpp:398-410`）、守护模式开关（`chaos_client_guardian_mode_manager.lua:363`）—— 这类走 `chaos_global_user_settings.xml`，是上面"挂载后重读"那一步的验收对象

---

## 相关文档

- SDK：`features/ps5/document/output/psn_12/System/Save_Data/`（`SaveData-Overview/basic-procedure.md`、`notes-regarding-the-calling-source-thread.md`、`SaveData-Reference/sce-save-data-*.md`）
- [../login/STATUS.md](../login/STATUS.md) — PS5 登录（CB2N-27968）进度，本功能复用其 `initializePS5`/`finalizePS5` 与用户 id
