# PS5 文档爬虫能力说明

> 对应目录：`E:\code\mutli_level\features\ps5\document`> 用途：爬取 PlayStation Developer Network（DevNet）在线文档到本地 Markdown，供离线查阅与接入参考。

---

## 1. 目录结构

```
features/ps5/document/
├── docs/                       # 人工整理/生成的文档
│   ├── ps5_client_id_application_guide.md   # Client ID / Secret 申请手册
│   ├── ps5_online_game_integration_guide.md # 联网游戏接入总览
│   ├── sdk_12_catalog.md                    # SDK 12.000 文档目录
│   └── sdk_12_crawl_report.md               # 爬取覆盖率报告
├── logs/                       # 爬取日志
├── output/                     # 爬取下来的原始文档（被 .gitignore）
│   └── psn_12/                 # PSN SDK/12.000 文档镜像
├── scripts/                    # 爬虫与辅助脚本
├── spike_output/               # 一次性探测/探索阶段输出
└── chrome_profile/             # Chrome 登录会话 profile
```

---

## 2. 爬虫能力一览

### 2.1 单页/子树爬取

| 脚本 | 能力 | 典型用法 |
|---|---|---|
| `scripts/fetch_single.py` | 抓取单个 URL，保存原始 HTML | 快速验证某篇文档是否可达 |
| `scripts/crawl_subtree.py` | 从入口 URL 递归爬取同一目录下的所有 `.html` | 整本指南离线化 |
| `scripts/crawl_toc_list.py` | 按 JSON 列表批量爬取多个 TOC 入口 | 配合 `run_all_batches.py` |
| `scripts/run_all_batches.py` | 把 PSN  landing 页链接分批，顺序爬完整套文档 | 一键生成 `output/psn_12` |

### 2.2 目录/链接提取

| 脚本 | 能力 |
|---|---|
| `scripts/extract_psn_links.py` | 从 PSN landing 页侧边栏提取所有文档链接 → `spike_output/psn_12_links.json` |
| `scripts/extract_sdk_12_catalog.py` | 提取 SDK/12.000 完整目录树 → `spike_output/sdk_12_catalog.json` |
| `scripts/split_psn_batches.py` | 把链接列表拆成小批次 |
| `scripts/merge_psn_batches.py` | 合并多批次爬取结果 |

### 2.3 报告与验证

| 脚本 | 能力 |
|---|---|
| `scripts/generate_crawl_report.py` | 对比 catalog 与 output，生成 `docs/sdk_12_crawl_report.md` |
| `scripts/report_crawl_status.py` | 输出爬取状态摘要 |
| `scripts/verify_crawled_content.py` | 检查本地文件是否完整/为空 |
| `scripts/generate_catalog_docs.py` | 生成分类目录文档 |

### 2.4 认证与会话

| 脚本 | 能力 |
|---|---|
| `scripts/start_chrome_debug.py` | 启动带 CDP 端口的 Chrome |
| `scripts/copy_locked_cookies.py` | 复制 DevNet 登录态 cookies |
| `scripts/save_storage.py` | 保存 Playwright storage state |
| `scripts/inspect_cookies.py` | 检查当前 cookies 是否有效 |
| `scripts/spike_login.py` | 登录流程探测 |

---

## 3. 典型工作流

### 3.1 首次抓取 PSN 文档

```bash
cd features/ps5/document

# 1. 启动已登录 DevNet 的 Chrome（CDP 9222）
python scripts/start_chrome_debug.py

# 2. 保存登录态
python scripts/save_storage.py

# 3. 拉取 PSN landing 页并提取链接
python scripts/probe_psn_12.py
python scripts/extract_psn_links.py

# 4. 分批爬取（每批 10 条）
python scripts/run_all_batches.py 10

# 5. 生成覆盖率报告
python scripts/generate_crawl_report.py
```

### 3.2 只抓单本指南

```bash
python scripts/crawl_subtree.py \
  "https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Service_Setup-Guide/__document_toc.html" \
  output/psn_service_setup
```

### 3.3 查看当前覆盖率

```bash
python scripts/report_crawl_status.py
# 或阅读
cat docs/sdk_12_crawl_report.md
```

---

## 4. 当前已抓取内容

根据 `docs/sdk_12_crawl_report.md`，当前已覆盖 PSN SDK/12.000 文档树的部分章节，重点包括：

- **PSN Service Setup Guide** — Client ID / Secret 申请、服务配置
- **NpAuth Overview / Reference** — 客户端 authorization code 流程
- **Auth Web API** — `/oauth/token`、`/userinfo` 等 S2S 接口
- **Sandbox / Legacy 环境说明** — sp-int、prod-qa、np 切换

覆盖率与具体章节见 `docs/sdk_12_crawl_report.md`。

---

## 5. 可继续扩展的抓取目标

| 缺失内容 | 建议抓取目标 | 用途 |
|---|---|---|
| DevNet 门户 UI 截图 | `https://game.develop.playstation.net/` 实际页面 | 写操作手册时定位按钮 |
| "Request New Services" 弹窗 | DevNet 产品详情页 | Client ID 申请步骤配图 |
| Client ID 配置页 | DevNet Client ID 服务配置 | Redirect URL 填写位置 |
| "Download Client Secret" 页面 | DevNet 产品详情页 | 下载入口确认 |
| UserService / SigninDialog 详细指南 | SDK UserService 章节 | 用户切换、登出事件处理 |

---

## 6. 保密要求

- PS5 SDK 与 DevNet 文档受 NDA 保护。
- 爬取的 `output/` 目录已加入 `.gitignore`，**不要**将其提交到公开仓库。
- 不要通过 IM、邮件、AI 云服务或截图外传文档内容。

---

## 7. 相关文档

- `docs/ps5_client_id_application_guide.md` — Client ID / Secret 申请手册
- `docs/ps5_online_game_integration_guide.md` — PS5 联网游戏接入总览
- `docs/sdk_12_crawl_report.md` — 爬取覆盖率报告
- `docs/sdk_12_catalog.md` — SDK 12.000 完整目录
