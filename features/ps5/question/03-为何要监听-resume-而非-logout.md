# 为何要监听 resume 而非 logout

## 结论

**因为应用无法感知 suspend。挂起期间不跑 tick，那条 LOGOUT 事件很可能根本没机会被处理。**

**`ON_RESUME` 是唯一可靠的检查点。**

---

## 原因

### 1. 文档明确：应用检测不到挂起

> It is **not possible for applications to detect transitions to the suspended state**, but
> **resuming from the suspended state can be detected** by obtaining resume events using
> `sceSystemServiceReceiveEvent()`.

来源：<https://game.develop.playstation.net/resources/documents/SDK/12.000/Programming-Startup_Guide/application-states.html>

**这句话是整件事的核心。** 系统的设计意图是：**不要试图检测挂起，而是在恢复时重新确认状态。**

### 2. 换用户的完整过程

```
玩家按 PS 键 → 切换使用者
   │
   ├─ 应用被 suspend            ← ★ 应用感知不到，tick 停止
   │    （此期间 LOGOUT 事件已发出，但应用可能没机会处理）
   │
   ├─ 玩家在主界面选另一个用户 / 重新登录
   │
   └─ 应用 resume               ← ★ 唯一可靠的检查点
        SCE_SYSTEM_SERVICE_EVENT_ON_RESUME (0x10000000)
```

**如果在 suspend 前处理 LOGOUT，会遇到**：
- 事件发出时机与挂起时机不可控
- 挂起期间 tick 停摆，队列里的 LOGOUT 可能一直不被消费
- resume 回来时事件队列状态不确定

**在 resume 后处理，则是**：应用完整地活过来了，此时查当前用户是谁，判断是否变化 —— **时序可控。**

### 3. resume 事件的完整用法

```c
SceSystemServiceStatus status;
sceSystemServiceGetStatus(&status);
if (status.eventNum > 0)
{
    for (int i = 0; i < status.eventNum; i++)
    {
        SceSystemServiceEvent event;
        ret = sceSystemServiceReceiveEvent(&event);
        if (ret == SCE_OK) {
            switch(event.eventType) {
            case SCE_SYSTEM_SERVICE_EVENT_ON_RESUME:
                {
                    // Processing after resuming
                }
                break;
            }
        }
    }
}
```

来源：<https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-receive-event.html>

**事件类型表**（10 种，节选相关的）：

| 事件 | 值 | 用途 |
|---|---|---|
| **`ON_RESUME`** | `0x10000000` | **应用恢复** ← 本场景 |
| `UNIFIED_ENTITLEMENT_UPDATE` | `0x10000018` | 统一 entitlement 更新（支付相关） |
| `SERVICE_ENTITLEMENT_UPDATE` | `0x1000000e` | service entitlement 更新 |
| `ENTITLEMENT_UPDATE` | `0x10000003` | 附加内容权利更新 |

来源：<https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-event-type.html>

### 4. 那 LOGOUT 事件还要不要监听？

**要。两者覆盖不同场景：**

| 来源 | API | 事件 | 覆盖场景 |
|---|---|---|---|
| UserService | `sceUserServiceGetEvent()` | `LOGIN`(0) / `LOGOUT`(1) | 玩家主动登出、系统强制登出 |
| **SystemService** | `sceSystemServiceReceiveEvent()` | **`ON_RESUME`(0x10000000)** | **换用户（挂起恢复）** |

**用户事件**：

> **SceUserServiceEventType**
> | `SCE_USER_SERVICE_EVENT_TYPE_LOGIN` | 0 | Login event |
> | `SCE_USER_SERVICE_EVENT_TYPE_LOGOUT` | 1 | Logout event |

来源：<https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-event-type.html>

**且用户事件无法区分登出原因**：

> **Information that would distinguish between logouts, logins, and changes to device linkages
> caused by the "Switch User" feature and those caused by other operations is not provided to
> the application.**

来源：<https://game.develop.playstation.net/resources/documents/SDK/12.000/User_Management-Overview/user-management-on-the-ps5.html>

**所以两者都是「一律回登录页」，不需要区分。**

### 5. resume 后如何判断用户是否真的变了

```c
SceUserServiceLoginUserIdList userIdList;
sceUserServiceGetLoginUserIdList(&userIdList);
// userIdList.userId[] 是当前登录用户数组
// 与之前记录的 m_ps5_user_id 比对
```

来源：<https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-get-login-user-id-list.html>

**本项目当前实现**是"resume 就回登录页"，没有比对 —— 因为回登录页是幂等且安全的，
登录页自身会处理"同一个用户重新登录"的情况，不会造成额外负担。

---

## 本项目实现

### Chaos C++

```cpp
// tick() 里，与 pollPS5UserEvents() 并列
pollPS5UserEvents();      // UserService：LOGOUT / LOGIN
pollPS5SystemEvents();    // SystemService：ON_RESUME
```

```cpp
void PlatformDelegate::pollPS5SystemEvents()
{
    SceSystemServiceStatus status;
    if (sceSystemServiceGetStatus(&status) != SCE_OK || status.eventNum == 0) return;
    for (UInt i = 0; i < status.eventNum; ++i)
    {
        SceSystemServiceEvent event;
        if (sceSystemServiceReceiveEvent(&event) != SCE_OK) break;
        if (event.eventType == SCE_SYSTEM_SERVICE_EVENT_ON_RESUME)
        {
            m_ps5_resume_pending = k_true;
        }
    }
}
```

**新增 include**：`<system_service.h>`

### Proven Ground Lua

```lua
function LuaClientLoginLevel:tickPS5UserEvent()
    local logged_out = platform_delegate:consumePS5LogoutEvent() == 1;
    local resumed    = platform_delegate:consumePS5ResumeEvent() == 1;
    if logged_out ~= k_true and resumed ~= k_true then return end
    g_lua_client_global_context.m_level_manager:returnToLoginLevel();
end
```

**位置**：`ClientLevelManager:tick` 里 `self.m_login_level:tick()` 是**无条件调用**的，
所以**游戏内收到事件也能响应**，不只登录页。

---

## 相关文档 URL

```
★ 应用状态 —— 「无法感知挂起，能感知 resume」原文
https://game.develop.playstation.net/resources/documents/SDK/12.000/Programming-Startup_Guide/application-states.html

SystemService 事件类型（ON_RESUME 0x10000000）
https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-event-type.html

SystemService 接收事件（含代码示例）
https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-receive-event.html

UserService 事件类型（LOGIN / LOGOUT）
https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-event-type.html

UserService 获取事件
https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-get-event.html

登录用户列表
https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-get-login-user-id-list.html

换用户机制（四种情况不可区分）
https://game.develop.playstation.net/resources/documents/SDK/12.000/User_Management-Overview/user-management-on-the-ps5.html

SystemService 总览 - 获取应用外部事件
https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Overview/obtaining-the-notification-of-events-occurring-outside-the-a.html
```
