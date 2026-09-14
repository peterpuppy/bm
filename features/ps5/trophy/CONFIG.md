# PS5 奖杯配置流程

> 触发事件变更时看这里。**改成就触发条件不需要动 PS5 侧**。

---

## 三层配置，各管一段

```
① 设计表（服务端）         决定成就「什么时候算完成」
   available_achievements       DID 白名单
   *_cumulate.design_sheet.gpa  relate_event / condition_num

② game_preload 资源（客户端） 决定成就「对应哪个平台奖杯」
   game_preload.game_preload.ast → platform_achievement_infos

③ PS5 后端（UDS / GEMS）    只认 trophy_id，不知道触发原因
   UDS Management Tool 配置奖杯条件
```

**关键**：②把游戏 DID 映射到平台 ID，③只收到一个数字。
所以**改①不影响③** —— UDS 不知道你是因为"创建角色"还是"首次登录"解锁的。

---

## 数据流

```
设计表 relate_event = "login"
  └─ initializeAchievementData          chaos_character_server_design_data_manager.lua:860-873
       构建 m_event_type_to_achievement_dids_map["login"] = {DID...}
  └─ addAchievementEvent(character_id, "login", nil)    chaos_character_data_manager.lua:4831
  └─ tick → checkAchievementPendingEvents → checkAchievement
  └─ RPC WRD2CLTNotifyAbtainedAchievement
  └─ 客户端 unlockAchievement(DID)
  └─ m_ps5_trophy_id_map[DID] → unlockTrophy(trophy_id)
  └─ UDS post "_UnlockTrophy" { "_trophy_id": N }
  └─ 系统比对条件 → 解锁 → unlock 回调
```

---

## 改触发事件：要动哪些配表

以「创建第一个角色 → 首次登录」为例。

### ① 设计表（必须改，两边都要）

```
_content/design/server/24_achievement/04_activityachievement_cumulate.design_sheet.gpa
_content/design/client/24_achievement/04_activityachievement_cumulate.design_sheet.gpa
```

**同一行、同一列**：DID `2404002001`（创建第一个角色）

| 列 | 改成 | 为什么 |
|---|---|---|
| `relate_event1` | `create_character` → `login` | 这就是触发点 |
| `relate_event_num` | `1` | 事件数，至少 1 |
| `condition_num` | `0` | **条件为空 → `checkAchievement` 直接返回 `k_true`**，纯事件触发 |
| `achievement_count_type` | **不能是** `condition_achievement` | 否则代码走 `:874-881` 短分支，**完全跳过 `relate_event`** |

⚠️ 客户端和**服务端**两份设计表都要改 —— 两边同名同内容，都含 `relate_event`。

### ② `available_achievements.sheet.gpa`

`_content/design/_config_tables/available_achievements.sheet.gpa`

**只是 DID 白名单**（喂给 `getAchievementCount` / `getAchievementDIDByIndex`），
不含任何事件列。**改触发事件不用动它**；只有换 DID 才要。

### ③ `game_preload` 资源（客户端）

`_content/preload/game_preload.game_preload.ast:605-612`

```xml
<platform_achievement_infos>
  <element sketum_id="D91HZW060K67HTRC">
    <did>2404002001</did>
    <api_name>22</api_name>
    <display_name>创建第一个角色</display_name>
    <ps5_trophy_id>0</ps5_trophy_id>
  </element>
</platform_achievement_infos>
```

**原地改触发事件不用动**。只有**换 DID** 才要改 `<did>` —— 否则
`unlockAchievement` 查不到映射，静默失败（只有 `LOG_WARNING`）。

### ④ PS5 后端

**零改动**。UDS 只认 `trophy_id`（`<ps5_trophy_id>`），不知道触发原因。

---

## 设计表格式（`.gpa`）

XML，根元素 `DesignSheetGPA`：

```xml
<design_ids>
  <element sketum_id="D92B6K1TCWVLH996">2404002001</element>
</design_ids>
<columns>
  <element type="StringIDSheetColumnData">
    <key>relate_event1</key>
    <elements>
      <element sketum_id="...">login</element>   <!-- 与 design_ids 行序位置对齐 -->
    </elements>
  </element>
</columns>
```

列元素与 `design_ids` 的**行序按位置对齐** —— 改值时认准第几行，别按名字猜。

---

## 坑

- **成就去重**：`chaos_character_achievement_manager.lua:376`
  `if character_data.m_current_achievement_map:getItem(achievement_did) == nil then`
  拿到过一次就永久跳过。改触发事件后重测，**要么换账号，要么清 DB**
- **`checkAchievement` 空条件返回 `k_true`**：`condition_num = 0` 是事件型成就的前提，
  不是可选项
- **重测前清奖杯 + UDS 数据**，否则系统认为已解锁不再触发：
  ```bash
  prospero-ctrl application delete-data trophy all /user:<User>
  prospero-ctrl application delete-data uds all /user:<User>
  ```
