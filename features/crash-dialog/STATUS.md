# Crash Dialog — STATUS

**Jira**: CB2N-25069
**分支**: `feature/CB2N-25069-crash-dialog`（chaos + proven_ground 同名）
**当前阶段**: Hook + Electron reporter 骨架**已落地**，待 `npm install` / 打包 / 测试

---

## Phase 1 调研结果（已完成）

### 关键发现

1. **crash 捕获全在引擎层，基于 Google Breakpad**
   - 初始化入口：`chaos_client_root.cpp:835` → `CrashHandler::initialize(dump_folder, version, CrashHandlerFilterCallback)`
   - Breakpad 对象：`crash_handler.cpp:37` `google_breakpad::ExceptionHandler*`
   - HANDLER_ALL 模式捕获所有异常类型

2. **游戏层（proven_ground）未注册任何 handler** — 全交引擎层。`client_module.cpp:43-62` 的 init 只做 Lua 绑定，不处理异常。

3. **已有可扩展 handler 链**：
   - `crash_handler.cpp:39` `static std::vector<CrashHandler::CrashHandlerFun> g_crash_handlers`
   - `MinidumpCallback`（crash_handler.cpp:45-72）在 dump 写完后**同步遍历**这个 vector
   - `ClientRoot::clientMiniDumpCallBack`（chaos_client_root.cpp:668）就是注册进这个链的其中一项

4. **现在 crash 时完全不弹框** —— 只做：
   - 写 minidump（Breakpad 内部）
   - 日志 force flush
   - 启动外部 `CrashDumpUploader.exe`（异步独立进程）
   - Sentry 异步上报

5. **引擎已有 `Process::showMessageBox`**（process.cpp:215-218）：
   ```cpp
   void Process::showMessageBox(const std::string& capital, const std::string& msg) {
       MessageBox(NULL, msg.c_str(), capital.c_str(), MB_OK);
   }
   ```
   问题：
   - 用的是 `MessageBox`（ANSI）→ 中文可能乱码
   - 无 `MB_ICONERROR` / `MB_TOPMOST` / `MB_SYSTEMMODAL`（crash 场景弹出性不足）

### 其他相关注册点（已知，不动）
- `Process::initialize` (process.cpp:70-71) — `_set_invalid_parameter_handler` / `_set_purecall_handler`，把错误转 NativeException
- `initHackDetectSystem` (chaos_client_hack_detect.cpp:274) — VEH 反作弊
- `appendExceptionHandler` 任务调度链（task_scheduler.cpp:22-25）

---

## Phase 2 实现方案（待开工）

### 接入点：`ClientRoot::clientMiniDumpCallBack`

文件：`H:\cb2\dev\chaos\_source\_engine\source\client\private\chaos\client\root\chaos_client_root.cpp`
函数：`ClientRoot::clientMiniDumpCallBack(const std::string& dump_path, const std::string& dump_id)` (行 668-730)

**为什么选这里**：
- ✅ 在 Breakpad 写完 dump **之后**跑（dump 安全落地后再阻塞用户）
- ✅ 位于 `ClientRoot::` 类下，**客户端进程专属**（服务端不走 ClientRoot 初始化）
- ✅ 已有 Config 开关的先例（`client/upload_crash_dump`），弹框也可以走同样机制
- ✅ 所有上传逻辑都在这里，是 crash 收尾的天然汇合点

### 具体插入位置

```cpp
// chaos_client_root.cpp:668
void ClientRoot::clientMiniDumpCallBack(const std::string& dump_path, const std::string& dump_id)
{
#if !defined (CHAOS_PLATFORM_ORBIS) && ... && !defined(CHAOS_PLATFORM_ANDROID)
    if (g_global_logger_system != nullptr) g_global_logger_system->forceFlush();

    // ... 已有的 is_upload_crash_dump 判断 + uploader 启动（行 677-705）...
    Process::createProcess(crash_dump_uploader_path, upload_parameter, crash_dump_uploader_pid);

    // ★ 新增：在 uploader 已启动（独立进程，不受游戏退出影响）后，弹框阻塞玩家
    bool show_crash_dialog = true;
    Config::get()["client/show_crash_dialog"].getValue(show_crash_dialog);
    if (show_crash_dialog) {
        Process::showCrashMessageBox(
            "Proven Ground - 游戏崩溃",
            "游戏意外崩溃。\n\n崩溃信息已保存，感谢您的反馈。\n点击确定退出。"
        );
    }

    return;
#endif
    // Android 分支保持不变
}
```

### 配套改动：新增 `Process::showCrashMessageBox`

不改现有 `showMessageBox`（避免影响其他调用点），在 `process.h` / `windows/process.cpp` 新增：

```cpp
// process.h
static void showCrashMessageBox(const std::string& title_utf8, const std::string& body_utf8);

// windows/process.cpp
void Process::showCrashMessageBox(const std::string& title_utf8, const std::string& body_utf8) {
    // UTF-8 → UTF-16
    auto to_wide = [](const std::string& s) -> std::wstring {
        int n = ::MultiByteToWideChar(CP_UTF8, 0, s.c_str(), -1, nullptr, 0);
        std::wstring w(n, 0);
        ::MultiByteToWideChar(CP_UTF8, 0, s.c_str(), -1, &w[0], n);
        return w;
    };
    ::MessageBoxW(
        nullptr,  // 不依赖父窗口
        to_wide(body_utf8).c_str(),
        to_wide(title_utf8).c_str(),
        MB_OK | MB_ICONERROR | MB_TOPMOST | MB_SYSTEMMODAL
    );
}
```

非 Windows 平台（Linux/macOS）给空实现或 stderr 输出，不影响编译。

### Config 开关

新增 `client/show_crash_dialog`，默认 true。关闭场景：
- 自动化测试 / CI 跑 crash 验证
- headless 运行

### Phase 2 工作清单

- [x] `process.h`：声明 `showCrashMessageBox(const std::wstring& title, const std::wstring& body)`
- [x] `windows/process.cpp`：Windows 实现 `MessageBoxW` + `MB_OK | MB_ICONERROR | MB_TOPMOST | MB_SYSTEMMODAL`
- [x] 其他 7 个平台（android/apple/durango/linux/orbis/prospero/scarlett）：空实现
- [x] `chaos_client_root.cpp` `clientMiniDumpCallBack` 开头（`forceFlush` 之后、早 return 之前）插入弹框调用 + `client/show_crash_dialog` config 读取
- [ ] `client.cfg` 默认配置加 `client/show_crash_dialog = true`（有默认模板时）
- [ ] commit：`CB2N-25069: add crash dialog via MessageBoxW in clientMiniDumpCallBack`（**未提交**，等 Phase 3 验证后）

### 设计决策记录

- **弹框位置放到函数开头，而非 uploader 启动后**：原代码 `is_upload_crash_dump == false` 会早 return，把弹框放后面会被跳过。弹框是"通知玩家"，与"上传 dump"独立——两个 config 开关互不干扰。
- **接口用 `std::wstring` 而非 `std::string`**：避免 UTF-8→UTF-16 运行时转换的编码坑，用 `L"中文"` wide 字面量由编译器处理。
- **不改现有 `showMessageBox`**：新增独立方法，避免影响其他调用点的行为。
- **源文件加 UTF-8 BOM** 而非用 `\uXXXX` 转义：`chaos_client_root.cpp` 原本是纯 ASCII 文件。加 UTF-8 BOM（`EF BB BF`）后 MSVC 见 BOM 会按 UTF-8 读这一个文件，其他 .cpp 不受影响。字面量可直接写 `L"游戏崩溃"`，可读性恢复。仅影响本文件一处，风险收敛。
- **植入 crash 测试开关**：`initializeEngine` 末尾放一段 `#if 0` 包裹的 null 指针写入（access violation）。本地把 `#if 0` 改成 `#if 1` 重新编译就会在引擎初始化完成后立即 crash，走完整 handler 链（Breakpad → `g_crash_handlers` 链 → `ClientRoot::clientMiniDumpCallBack` → 弹 `MessageBoxW`）。`#pragma message` 打出警告提醒"不要 merge"。
- **点击"确定"后 `TerminateProcess` 终止进程**（首次测试发现 WER 二次弹框后加入，随后因破坏 crash 链回退）：Breakpad handler 返回后，SEH 异常会冒到 Windows 默认处理器 → 弹系统 WER "xxx 已停止工作"框。**最初尝试** 在 `clientMiniDumpCallBack` 末尾 `::TerminateProcess(self, 1)` —— 立即修正：会打断 Sentry 异步上报、跳过 `g_crash_handlers` 链中后续 handler、跳过 Breakpad 自身收尾。**改为** 在 `Process::initialize` 调 `::SetErrorMode(SEM_NOGPFAULTERRORBOX \| SEM_FAILCRITICALERRORS)` 全局抑制 WER UI，crash 链完整跑，Windows 只是不弹那个系统框。
- **重排 `clientMiniDumpCallBack` 流程**：原来是"弹框→早 return→uploader"，`upload_crash_dump=false` 时 uploader 被跳过但弹框也丢（因为放在早 return 之前的早 return 路径）。新顺序：forceFlush → `if (upload)` Lua dump + uploader → `if (show_dialog)` 弹框 → return。两个开关独立。uploader 是独立进程，启动后不等它完成即可阻塞弹框。
- **弹框用自定义 Win32 对话框替换 `TaskDialogIndirect`**（用户要求在正文嵌图后再次修正）：`MessageBox` / `TaskDialog` 都不支持在正文嵌任意图片，只能用 icon。改用 `CreateWindowEx` 自造对话框：注册自定义 WindowClass (`ChaosCrashDialogClass_CB2N25069`) + 3 个子控件（`STATIC SS_BITMAP` 承载图片、`STATIC SS_LEFT` 承载多行文字、`BUTTON BS_DEFPUSHBUTTON` 承载"确定"）+ 自己跑 modal message loop。布局：左图（最大 192×192）+ 右文（340 宽）+ 底部右下确定按钮。图片通过 `LoadImageW(..., IMAGE_BITMAP, LR_LOADFROMFILE)` 从磁盘加载 `.bmp`（`LoadImageW` 不支持 PNG）。路径由 Config `client/crash_dialog_icon_path` 驱动，支持 `$(ExeDir)` 宏展开。**三层 fallback**：(1) 有图片 + 加载成功 + 窗口创建成功 → 自定义对话框；(2) 否则 → `TaskDialogIndirect` + `TD_ERROR_ICON`；(3) TaskDialog 也失败（manifest 缺 Common Controls 6.0）→ `MessageBoxW`。Esc/Enter/Close 都视为点确定。

### Phase 3 验证清单

植入 debug 触发点（暂用 `-crashtest` 命令行 arg 或 debug 菜单），或找已有的 crash 测试入口：

| 场景 | 触发方式 | 期望 |
|------|---------|------|
| 未捕获 C++ 异常 | `throw std::runtime_error("test")` | 写 dump → 启动 uploader → 弹框 → 点 OK → 退出 |
| Access violation | `*(volatile int*)0 = 42` | 同上 |
| abort() | `std::abort()` | 同上 |
| 除零 | `volatile int x = 1; volatile int y = 0; x/y;` | 同上 |

额外检查：
- [ ] 弹框标题和正文中文无乱码
- [ ] 游戏全屏模式下弹框可见（MB_TOPMOST 生效）
- [ ] 服务端进程（game_server.exe 等）走的是别的 Root，**不会**弹框
- [ ] `client/show_crash_dialog=false` 时不弹

---

## 开放问题（Phase 2 开工前再问）

1. 弹框文案终稿（可参考友商：《xxx 意外崩溃，错误信息已发送给开发团队》）？
2. 是否需要"重启游戏"按钮（`MB_YESNO` + 重启逻辑）还是仅"确定退出"（`MB_OK`）？MVP 建议后者。
3. `client/show_crash_dialog` 配置 key 是否放到已有的 config 层级下，还是独立节？

---

## Phase 4：Hook + Electron Reporter（已落地）

### 架构
引擎通用、游戏特化 UI。chaos 只提供一个 callback 注册点，不背 proven_ground 的业务；游戏侧注册 callback，callback 里启动独立 `CrashReporter.exe`（Electron）。

- callback 已注册 → 调用 callback + return，完全跳过引擎内 Win32 兜底
- callback 未注册 → 走 Phase 2 的 Win32 兜底，不退化

### chaos 侧改动
- `chaos_client_root.h`：`#include <functional>`、protected 加 `m_crash_dialog_callback`、public 加 `setCrashDialogCallback()` 静态接口
- `chaos_client_root.cpp`：静态成员定义、setter 实现、`clientMiniDumpCallBack` 里前置 `if (m_crash_dialog_callback) { ...; return; }`

### proven_ground 侧改动
- `client_module.cpp` `ClientModule::initialize()` 末尾注册 callback；callback 用 `ArchiveManager::formalizeFilePath("$(ExeDir)/CrashReporter.exe")` 定位 reporter，`Process::createProcess` 启动

### Electron reporter 骨架
位置：`E:/code/mutli_level/features/crash-dialog/crash-reporter/`（临时，待测试后迁）

```
crash-reporter/
├── package.json          electron 27 + electron-builder 配置
├── main.js               CLI 解析 / 无 frame 窗口 / IPC
├── preload.js            renderer ↔ main 桥
├── renderer/
│   ├── index.html        布局
│   ├── style.css         样式（无标题栏，自 drag bar）
│   └── app.js            填充文案 + 按钮逻辑
├── locales/              zh-CN / zh-TW / en-US / ja-JP / ko-KR（7 条字符串 ×5）
├── assets/
└── README.md
```

### CLI 协议（game → reporter）

| 参数 | 当前 | 说明 |
|------|------|------|
| `--image` | ✅ 传 `$(ExeDir)/crash_illust.png` | PNG 原生支持透明 |
| `--dump-dir` | ✅ callback 第 1 参 | Breakpad dump 目录 |
| `--dump-id` | ✅ callback 第 2 参 | Dump 文件名（不含 `.dmp`） |
| `--show-report` | ✅ `false` | 暂关上报按钮（待有 upload-url 再开） |
| `--lang` | ❌ 不传 | reporter 用 `app.getLocale()` 自动决定 |
| `--upload-url` | ❌ 不传 | 等上报端点就位后由 config 驱动 |

### 下一步（你来执行）

1. `cd E:/code/mutli_level/features/crash-dialog/crash-reporter/`
2. `npm install` —— 装 electron & electron-builder（~200 MB node_modules，`.gitignore` 已排除）
3. `npm run dev` —— 本地试跑，验证 UI 能起、文案按系统 locale 切换
4. `npm run build` —— 打包出 `dist/CrashReporter.exe`（portable 单 exe，~150 MB）
5. 把 `CrashReporter.exe` 和 `crash_illust.png` 复制到游戏 exe 同目录
6. 重编 chaos + proven_ground，`#if 1` 打开 crash test，触发验证
7. 验证通过后把 reporter 项目迁到 proven_ground 的 `_tools/` 或独立仓

### 未来扩展点（留口不做）

- **上报**：`--upload-url` + `--show-report=true` 打开。`main.js` 里 `action:report` handler 已实现 POST dump file，只要 game 侧传 URL 就起效
- **语言显式指定**：game 侧从 config 读 `client/crash_dialog_lang`，加 `--lang=zh-CN` 到 CLI
- **增语言**：新增 `locales/xx-XX.json` 即可，不用改代码；`main.js` 的 `normalizeLang()` 按需扩充 CJK 归并规则
- **UI 美化**：全在 `renderer/style.css` 里；圆角用 `border-radius`，阴影加 `box-shadow`，动画 `@keyframes`——纯前端工作量

### 为什么不退化（设计说明）

- Win32 兜底**保留**：即使 reporter 找不到 / 启动失败 / 没部署，也不会静默退出
- `SetErrorMode(SEM_NOGPFAULTERRORBOX)` 依然有效：Windows 默认 WER 弹窗仍被压住
- Breakpad / Sentry / CrashDumpUploader 链**零改动**
