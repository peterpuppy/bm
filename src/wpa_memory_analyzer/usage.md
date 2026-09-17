# wpr_analyzer 使用说明

把 WPR 的 VirtualAlloc 内核 trace，在 WPA 里手动拷出的 CSV，解析成内存归因报告：**哪个 dll 分配 / 哪段业务函数触发 / 哪些是绕过内存池的直接 new/malloc**。

## 快速试跑
不想自己抓数据，先看工具长什么样：双击 `test.bat`（或终端跑），它会分析自带的样例数据 `testdata\sample.csv`（截自真实登录场景），打印总结并把报告写到 `testdata\report\`。

## 环境
- **WPA（Windows Performance Analyzer）**：Microsoft Store 搜 "Windows Performance Analyzer" 安装，或装 Windows ADK 时勾 "Windows Performance Toolkit"（含命令行 `wpr` 录制）。
- **Python 3.7+**：纯标准库，无需 `pip install`。

## 使用步骤

### 1. 录制（管理员命令行）
```
wpr -start config\mem_trace_kernel.wprp -filemode     ← 必须先于游戏启动
   … 进场景，玩到内存峰值 …
wpr -stop mem.etl
```
必须从启动录（否则漏掉录制前的大块内存），玩到峰值再 stop。

### 2. 用 WPA 打开并加载符号
- WPA 打开 `mem.etl`。
- 菜单 **Trace → Configure Symbol Paths**，自行添加你的 `.pdb` 目录 → **Load Symbols**。
- 不加载符号 → 调用栈没有函数名，视图 2/3 失效。

### 3. 在 WPA 里拷出 CSV
- 打开 **Virtual Memory → VirtualAlloc Commit LifeTimes** 表。
- **filter 到目标进程**，展开 **Commit Stack**。
- 确认列含 `Commit Stack` / `Impacting Size (MB)` / `Size (MB)` / `Decommit Time`，且 **Impacting 有值**（net-resident，不是累计 churn）。
- 全选数据行 → 右键 **Copy**（含列头）→ 粘贴存为 `data.txt`（UTF-8）。

### 4. 分析
```
python wpr.py data.txt --out <输出目录>
```
可选：`--top N`（每视图 module 数，默认 25）、`--func-top K`（每 module 函数数，默认 12）。

## 输出（4 个文件）
| 文件 | 用途 |
|---|---|
| `wpr_summary.txt` | **一屏总结**：总量 / heap-direct / 池-非池 / 各视图 top5 —— 先看这个 |
| `wpr_report.txt` | 多视图 top-N 人读报告 |
| `wpr_by_function.csv` | **完整数据**（不截断）：`view,module,function,MB`，Excel 透视 |
| `wpr_by_module.csv` | 简易：`module,MB` |

## 视图
| | 含义 | 归因 |
|---|---|---|
| **View 1 直接分配器 dll** | 字节物理上由哪个 dll 提交 | 栈最深的非系统帧 |
| **View 2 业务调用方 module→函数** | 哪段业务代码触发分配 | 跳过分配器/容器胶水后的业务帧 |
| **View 3 非池 heap module→函数** | 绕过内存池的直接 new/malloc/STL | 走 CRT 堆但栈中无 mempool 帧 |
| **View 4 DefaultPool module→函数** | 兜底池里都是谁的内存 | 栈中含 `Chaos::PoolDefault` 的分配，按业务调用方归因 |

> 三个务必：① 管理员录制 ② 加载符号 ③ 取 net-resident（Impacting，非 churn）。漏任一，报告会退化或标红。
