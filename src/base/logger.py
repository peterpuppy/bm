"""通用日志工具

功能：
- 获取最新日志文件（含轮转 .txt.1 / .txt.2）
- 获取同一会话的全部日志分片
- 读取日志（尾部N行、搜索过滤）
- Lua ERROR 快速扫描
- 清除 / 列出日志文件
"""

import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime

_LOG_PATTERNS = ['*.log', '*.txt', '*.txt.*']


class LogReader:
	"""日志文件读取器（支持日志轮转）"""

	def __init__(self, log_dir: str):
		self.log_dir = Path(log_dir)

	# ------------------------------------------------------------------
	# 文件发现
	# ------------------------------------------------------------------

	def _all_log_files(self) -> List[Path]:
		if not self.log_dir.exists():
			return []
		files: List[Path] = []
		for pat in _LOG_PATTERNS:
			files.extend(self.log_dir.glob(pat))
		return files

	def get_latest_log_file(self) -> Optional[Path]:
		"""最近修改的日志文件（含轮转分片）"""
		files = self._all_log_files()
		return max(files, key=lambda p: p.stat().st_mtime) if files else None

	def get_session_log_files(self, stem: Optional[str] = None) -> List[Path]:
		"""获取同一会话的全部日志分片，按序排列。

		轮转规则：log_xxx.txt (当前) → log_xxx.txt.1 (旧) → log_xxx.txt.2 (更旧)
		返回按时间**正序** [.txt.2, .txt.1, .txt]，拼接后即为完整日志。

		Args:
			stem: 日志文件名前缀，None 则用最新文件推断。
		"""
		if stem is None:
			latest = self.get_latest_log_file()
			if latest is None:
				return []
			name = latest.name
			stem = re.sub(r'(\.\d+)$', '', name)  # strip .1 / .2

		result: List[Tuple[int, Path]] = []
		for f in self._all_log_files():
			if not f.name.startswith(stem.replace('.txt', '')):
				continue
			suffix_match = re.search(r'\.txt\.(\d+)$', f.name)
			order = int(suffix_match.group(1)) if suffix_match else 0
			result.append((order, f))

		result.sort(key=lambda x: x[0], reverse=True)
		return [f for _, f in result]

	# ------------------------------------------------------------------
	# 读取
	# ------------------------------------------------------------------

	def read_log(
		self,
		lines: int = 100,
		search: Optional[str] = None,
		log_file: Optional[Path] = None,
		case_sensitive: bool = False,
	) -> Dict[str, Any]:
		"""读取日志文件尾部"""
		if log_file is None:
			log_file = self.get_latest_log_file()
		if log_file is None:
			return {"success": False, "message": f"No log files found in {self.log_dir}"}
		if not log_file.exists():
			return {"success": False, "message": f"Log file not found: {log_file}"}

		try:
			with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
				all_lines = f.readlines()

			if search:
				key = search if case_sensitive else search.lower()
				filtered = [l for l in all_lines if key in (l if case_sensitive else l.lower())]
				content_lines = filtered[-lines:] if lines > 0 else filtered
				filtered_count = len(filtered)
			else:
				content_lines = all_lines[-lines:] if lines > 0 else all_lines
				filtered_count = len(all_lines)

			return {
				"success": True,
				"filename": log_file.name,
				"path": str(log_file),
				"size_kb": round(log_file.stat().st_size / 1024, 2),
				"modified": datetime.fromtimestamp(log_file.stat().st_mtime).isoformat(),
				"total_lines": len(all_lines),
				"filtered_lines": filtered_count,
				"returned_lines": len(content_lines),
				"content": "".join(content_lines),
				"search": search,
			}
		except Exception as e:
			return {"success": False, "message": f"Failed to read log: {e}"}

	def read_session_log(self, lines: int = 0) -> Dict[str, Any]:
		"""读取当前会话的完整日志（拼接所有轮转分片）。

		Args:
			lines: 返回尾部行数，0=全部
		"""
		files = self.get_session_log_files()
		if not files:
			return {"success": False, "message": f"No session log in {self.log_dir}"}

		all_lines: List[str] = []
		file_names: List[str] = []
		for f in files:
			try:
				with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
					all_lines.extend(fh.readlines())
				file_names.append(f.name)
			except Exception:
				pass

		content_lines = all_lines[-lines:] if lines > 0 else all_lines
		return {
			"success": True,
			"files": file_names,
			"total_lines": len(all_lines),
			"returned_lines": len(content_lines),
			"content": "".join(content_lines),
		}

	# ------------------------------------------------------------------
	# 快速错误扫描
	# ------------------------------------------------------------------

	_LUA_ERROR_RE = re.compile(r'\[LuaError\]|LuaError|error:.*\.lua:\d+', re.IGNORECASE)
	_CALLSTACK_RE = re.compile(r'^\[callstack\]:|^\[C\]=|^\[Lua\]=')

	def scan_lua_errors(self, max_errors: int = 20, context: int = 5) -> List[Dict[str, Any]]:
		"""扫描当前会话日志中的 Lua ERROR（含 callstack 合并）。

		Returns:
			[{"line": int, "message": str, "callstack": [str], "file": str}]
		"""
		files = self.get_session_log_files()
		if not files:
			return []

		all_lines: List[str] = []
		for f in files:
			try:
				with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
					all_lines.extend(fh.readlines())
			except Exception:
				pass

		errors: List[Dict[str, Any]] = []
		i = 0
		while i < len(all_lines) and len(errors) < max_errors:
			line = all_lines[i]
			if self._LUA_ERROR_RE.search(line):
				entry: Dict[str, Any] = {
					"line": i + 1,
					"message": line.rstrip(),
					"callstack": [],
				}
				j = i + 1
				while j < len(all_lines) and j < i + 30:
					next_line = all_lines[j]
					if self._CALLSTACK_RE.match(next_line):
						entry["callstack"].append(next_line.rstrip())
						j += 1
					else:
						break
				errors.append(entry)
				i = j
			else:
				i += 1
		return errors

	# ------------------------------------------------------------------
	# 管理
	# ------------------------------------------------------------------

	def clear_logs(self) -> Dict[str, Any]:
		"""清除所有日志文件"""
		files = self._all_log_files()
		deleted, errs = 0, []
		for f in files:
			try:
				f.unlink()
				deleted += 1
			except Exception as e:
				errs.append(f"{f.name}: {e}")
		result: Dict[str, Any] = {"success": True, "deleted_count": deleted, "total_files": len(files)}
		if errs:
			result["errors"] = errs
		return result

	def list_log_files(self) -> Dict[str, Any]:
		"""列出所有日志文件"""
		files = self._all_log_files()
		infos = []
		for f in sorted(files, key=lambda p: p.stat().st_mtime, reverse=True):
			infos.append({
				"name": f.name,
				"size_kb": round(f.stat().st_size / 1024, 2),
				"modified": datetime.fromtimestamp(f.stat().st_mtime).isoformat(),
			})
		return {"success": True, "count": len(infos), "files": infos}

