# Crash Dialog Feature

| 字段 | 值 |
|------|---|
| **Jira** | CB2N-25069 |
| **分支**（两个仓库同名） | `feature/CB2N-25069-crash-dialog` |
| **Commit 前缀** | `CB2N-25069: <message>` |
| **起点** | master（chaos + proven_ground 均从 master 新建） |

**目标**：游戏进程崩溃时弹一个 Windows 原生提示框，告诉玩家"游戏已崩溃"，避免玩家看到纯粹的闪退没有反馈。

**范围收敛**：
- ✅ 只做弹框
- ✅ 只处理"程序崩溃"（未捕获 C++ 异常 / access violation / abort / 栈溢出等）
- ❌ **不做** minidump（已有）
- ❌ **不做** 上报 / 收集 / 远端
- ❌ **不做** Lua 层报错、业务层错误、资源加载失败等

---

## 技术选型（已定）

**方案**：现有 crash handler 末端调用 **`MessageBoxW`**（user32.dll 原生 API）。

**为什么不用游戏内 UI**：
- **Coherent** 基于 Chromium，crash 后主进程状态损坏、渲染线程可能已死 → 不可靠
- **imgui** 依赖游戏主循环和 GPU 渲染管线 → crash 后都停了 → 弹不出来

**为什么选 MessageBoxW**：
- Win32 原生 API，依赖 user32.dll（几乎不会 crash）
- 同步阻塞，简单
- 不需要游戏主循环、GPU、渲染栈
- 支持中文（Unicode W 版本）
- 参数 `MB_TOPMOST` 保证在残留游戏窗口之上弹出

**调用形态**（示意）：
```cpp
::MessageBoxW(
    nullptr,                      // 不依赖父窗口（游戏窗口此时可能已损坏）
    L"游戏意外崩溃。\n\n崩溃信息已保存至 %dump_path%",
    L"Proven Ground - 崩溃",
    MB_OK | MB_ICONERROR | MB_TOPMOST | MB_SYSTEMMODAL
);
```

---

## 关键调研点（Phase 1 要搞清楚）

接入之前必须摸清现有 crash handler 链路。关注点：

| # | 问题 | 为什么重要 |
|---|------|-----------|
| 1 | crash handler 在哪层注册？引擎（chaos）还是游戏（proven_ground）？ | 决定本 feature 改哪个仓库 |
| 2 | 现在 crash 时有没有弹框？如果有，弹的是什么（imgui / Coherent / 原生）？ | 若已有 UI 框，是替换还是新增一个并行通道 |
| 3 | minidump 生成的位置、时序（同步 / 异步）？ | 弹框应放在 dump 写完之后，避免阻塞 dump |
| 4 | handler 在主线程还是独立线程？ | 决定 `MessageBoxW` 的安全性（独立线程更稳）|
| 5 | 栈溢出（stack overflow）场景 handler 还能跑吗？ | 栈溢出下 `MessageBoxW` 可能也调不动 —— 这种极端情况本 MVP 不处理 |

---

## 接入位置（待 Phase 1 确认）

两个可能落点：

**A. 引擎层（Chaos `H:\cb2\dev\chaos`）**
- 推测位置：`SetUnhandledExceptionFilter` 注册处 / minidump 模块附近
- 优点：所有基于 Chaos 的项目（不止 proven_ground）自动受益
- 缺点：提示文案里"Proven Ground"之类游戏名就要参数化

**B. 游戏层（`H:\cb2\dev\wolfgang\_games\proven_ground\_source`）**
- 推测位置：游戏初始化时注册自己的 top-level filter
- 优点：文案/行为可定制，不影响其他引擎用户
- 缺点：如果引擎已经注册了同类 handler，要确认覆盖关系

→ Phase 1 调研后决定。STATUS.md 里跟踪。

---

## 验证计划（Phase 3）

植入故意 crash 触发点（debug 菜单 / 命令行开关），在以下 4 种 crash 场景下跑：

| 场景 | 触发方式 | 期望 |
|------|---------|------|
| 未捕获 C++ 异常 | `throw std::runtime_error("test")` | 弹框出现 → 点 OK → 进程退出 |
| Access violation | `*(int*)0 = 42` | 弹框出现 → 点 OK → 进程退出 |
| abort() | `std::abort()` | 弹框出现 → 点 OK → 进程退出 |
| 除零 | `int x = 1/0` | 弹框出现 → 点 OK → 进程退出 |

非目标（栈溢出场景下弹框失败是可接受的）：
- `void f() { f(); }` 递归导致栈溢出 —— MVP 不保证此场景弹出

---

## 不做的事情（范围限定）

- 不做独立 CrashReporter 进程（需求里已说够用 MessageBox）
- 不做 minidump（已有）
- 不做上传 / 发送 / Sentry 集成
- 不做 Lua 层报错的弹框（范围外）
- 不做对栈溢出等极端 crash 的特殊鲁棒性（MVP 接受概率性失败）
- 不做多语言（中文即可，如果未来需要再扩）

---

## 下一步

见 `STATUS.md`。当前阶段：**Phase 1 调研**。
