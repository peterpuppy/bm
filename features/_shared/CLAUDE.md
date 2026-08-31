# 游戏多功能验证工作台（mutli_level 为仓库历史名）

> 围绕 Chaos 引擎 + Proven Ground 游戏做各种验证/调试任务。每个功能独立分区。
> **根 `CLAUDE.md` 由 `scripts/switch_feature.py` 自动生成**，表示当前 active feature 的上下文。请勿手工编辑根 CLAUDE.md；改动请编辑 `features/_shared/CLAUDE.md` 或 `features/<feature>/CLAUDE.md` 后重跑脚本。

## 外部源码仓库

```
Engine Repo:  H:\cb2\dev\chaos
Game Repo:    H:\cb2\dev\wolfgang\_games\proven_ground
MCP Root:     E:\code\mutli_level
```

## 通用 MCP Tools（任何 feature 可用）

| Tool | 用途 |
|------|------|
| `run_service` | 启动服务进程 |
| `stop_service` | 停止服务进程 |
| `stop_all` | 停止所有服务 |
| `hotupdate_connect` | 连接热更新端口 |
| `hotupdate_execute_lua` | 执行 Lua 代码 |
| `hotupdate_status` | 查询连接状态 |

Feature 专属工具（如 PVE 的 `game_start_pve_session` 等）见下方 feature 分区。

## 共享 Skills（跨 feature 的引擎/游戏通用知识）

| 命令 | Skill | 用途 |
|------|-------|------|
| `/chaos-engine` | chaos-engine-architecture | Chaos 引擎 C++ 层架构 |
| `/proven-ground` | proven_ground-game-architecture | 游戏 Lua 层架构 |
| `/world-server-topology` | world-server-topology | WorldServer 分布式拓扑 |
| `/game-schema-rpc` | game-schema-rpc | RPC 协议与 schema |

Feature 专属 skill（如 `/pve-*` 系列）见下方 feature 分区。

## 代码组织

```
src/
├── base/       通用基础设施（config / logger / pipeline / process）
└── core/       业务逻辑
    ├── session/    （当前为 PVE Session 调度；新 feature 按需新增子包）
    ├── process/    GameServer / Client 启动
    └── hotupdate/  热更新 RPC 代理
```

## 切换 Feature

```bash
python scripts/switch_feature.py              # 列出所有 feature + 当前 active
python scripts/switch_feature.py <feature>    # 切换（覆盖根 CLAUDE.md）
```

新 feature 起始：
1. `mkdir features/<new-name>/`
2. 从 `features/pve-multi-level/CLAUDE.md` 拷贝做模板，改写为新 feature 内容
3. 建 `features/<new-name>/STATUS.md` 写目标 + TODO
4. `python scripts/switch_feature.py <new-name>` 激活

低频回切 PVE：`python scripts/switch_feature.py pve-multi-level`

## Feature 工作流约定（Jira 任务编号）

每个 feature 对应一个 Jira 任务，编号形如 `CB2N-xxxxx`。所有代码动作都围绕这个编号。

### 分支命名
- 两个游戏源码仓库（**chaos 引擎** + **proven_ground 游戏**）都用同一分支名：
  ```
  feature/CB2N-xxxxx-<short-desc>
  ```
  例：`feature/CB2N-25069-crash-dialog`、`feature/CB2N-19044-pve-0407`

### Commit message（规范）
- **一两行**，以 `CB2N-xxxxx: ` 开头。不写 body、bullet 列表、详细解释 —— 这些放 PR description，不放 commit。
- **不要** 加 `Co-Authored-By` 行（覆盖全局默认）。
- 例：
  ```
  CB2N-25069: 游戏崩溃时弹出带自定义图片的原生提示框
  CB2N-19044: 直连场景下修复多 Level 隔离
  ```

### 开工流程（每个新 feature 开始时）
在**两个源码仓库都**执行：
1. `git checkout master`
2. `git fetch --prune && git pull --ff-only`
3. 若远端已有 `feature/CB2N-xxxxx-*` 分支 → `git checkout <name>`；否则 → `git checkout -b feature/CB2N-xxxxx-<desc>`
4. 在 `features/<name>/CLAUDE.md` 顶部记录 `Jira: CB2N-xxxxx` 和分支名

本工作台仓库（`mutli_level`）的 commit 无需该前缀（它只是工具仓库，不关联 Jira）。

### 源码仓库绝对路径
- Chaos 引擎：`H:\cb2\dev\chaos`
- Proven Ground 游戏：`H:\cb2\dev\wolfgang\_games\proven_ground`
