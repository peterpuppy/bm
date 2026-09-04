# PS5 文档抓取与整理（ps5-document）

本目录用于爬取、整理 PlayStation 5 / PSN 官方文档，为 `CB2N-27968` PS5 登录功能提供离线参考。

---

## 目录

```
.
├── docs/              # 人工整理/生成的 Markdown 文档
├── logs/              # 爬取与处理日志
├── output/            # 爬取下来的原始文档（被 .gitignore，不入库）
├── scripts/           # 爬虫与辅助脚本
├── spike_output/      # 探索阶段输出（链接列表、landing 页等）
└── chrome_profile/    # Chrome 登录会话 profile
```

---

## 核心能力

### 1. 登录态保持

- 通过 Chrome CDP + Playwright 连接已登录 DevNet 的浏览器。
- `scripts/save_storage.py` 保存 storage state，避免每次重登。
- `scripts/copy_locked_cookies.py` / `inspect_cookies.py` 处理/检查 cookies。

### 2. 文档爬取

| 脚本 | 用途 |
|---|---|
| `fetch_single.py` | 单页抓取 |
| `crawl_subtree.py` | 递归子树爬取 |
| `crawl_toc_list.py` | 按 TOC 列表批量爬取 |
| `run_all_batches.py` | 分批跑完整套 PSN 文档 |

### 3. 目录与链接提取

| 脚本 | 用途 |
|---|---|
| `extract_psn_links.py` | 从 PSN landing 页提取所有文档链接 |
| `extract_sdk_12_catalog.py` | 提取 SDK/12.000 完整目录 |
| `split_psn_batches.py` / `merge_psn_batches.py` | 批次拆分/合并 |

### 4. 报告生成

| 脚本 | 用途 |
|---|---|
| `generate_crawl_report.py` | 生成 `docs/sdk_12_crawl_report.md` |
| `report_crawl_status.py` | 输出爬取状态摘要 |
| `verify_crawled_content.py` | 检查本地文件完整性 |
| `generate_catalog_docs.py` | 生成分类目录文档 |

---

## 快速开始

```bash
cd features/ps5-document

# 1. 启动已登录的 Chrome（CDP 9222）
python scripts/start_chrome_debug.py

# 2. 保存登录态
python scripts/save_storage.py

# 3. 探测并提取 PSN 文档链接
python scripts/probe_psn_12.py
python scripts/extract_psn_links.py

# 4. 分批爬取
python scripts/run_all_batches.py 10

# 5. 生成覆盖率报告
python scripts/generate_crawl_report.py
```

---

## ⚠️ 补爬单文档必须指定 output_dir

`crawl_subtree.py` / `fetch_single.py` 默认 output_dir 是 `output`，会爬到**错位置**（正确根目录是 `output/psn_12`）。补爬单个文档时**务必传第二参数**，否则目录错乱、`_index.json` 也对不上：

```bash
# 正确：补爬某个库的子树（Overview/Reference 等）
python scripts/crawl_subtree.py <__document_toc.html URL> output/psn_12

# 正确：补爬单页
python scripts/fetch_single.py <url> output/psn_12
```

补爬后 `_index.json` 在 `output/psn_12/_index.json`，`crawl_subtree.py` 会把新爬的条目写进 `output/_index.json`（错位置）——需手动合并：把新条目并入 `output/psn_12/_index.json` 并统一 path 为正斜杠，再删 `output/_index.json`。

---

## 已整理文档

| 文档 | 说明 |
|---|---|
| `docs/ps5_client_id_application_guide.md` | Client ID / Client Secret 申请步骤 |
| `docs/ps5_online_game_integration_guide.md` | PS5 联网游戏接入总览 |
| `docs/sdk_12_catalog.md` | SDK 12.000 文档目录 |
| `docs/sdk_12_crawl_report.md` | 爬取覆盖率报告 |

---

## 保密声明

PS5 SDK 与 DevNet 文档受 NDA 保护：

- `output/` 已加入 `.gitignore`，禁止提交。
- 禁止通过公开渠道、AI 云服务、IM、邮件或截图外传文档内容。

---

## 相关 feature

- `features/ps5-login/` — PS5 登录功能实现。
