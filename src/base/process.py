"""通用进程管理工具

提供进程启动、停止、监控等功能，可以被多个 MCP 服务使用。
"""

import psutil
import time
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional


class ProcessManager:
	"""进程管理器 — 通过 Start-Process 启动完全独立的进程"""
	
	def __init__(self):
		self.processes: Dict[str, int] = {}  # name -> pid
	
	def start_process(
		self,
		name: str,
		executable: str,
		working_dir: str,
		args: Optional[List[str]] = None,
		env: Optional[Dict[str, str]] = None,
		auto_kill_existing: bool = True,
		no_window: bool = True
	) -> Dict[str, Any]:
		"""启动进程
		
		Args:
			name: 进程名称标识
			executable: 可执行文件路径
			working_dir: 工作目录
			args: 命令行参数
			env: 环境变量 (可选)
			auto_kill_existing: 是否自动清理同名进程
			no_window: 是否不创建新窗口（Windows）
		
		Returns:
			包含启动结果的字典
		"""
		exe_path = Path(executable)
		
		if not exe_path.exists():
			return {
				"success": False,
				"message": f"Executable not found: {executable}"
			}
		
		# 自动清理现有进程
		if auto_kill_existing:
			self.kill_processes_by_name(exe_path.name)
			# GameServer 占用 10000，需多等一会再启动新进程，避免 bind 失败
			if "xenon_game_server" in exe_path.name.lower():
				time.sleep(1.5)
			else:
				time.sleep(0.5)
		
		# 准备环境变量
		import os
		process_env = os.environ.copy()
		if env:
			process_env.update(env)
		
		try:
			cmd = [str(exe_path)]
			if args:
				cmd.extend(args)

			ps_cmd = (
				f'Start-Process -FilePath "{exe_path}" '
				f'-WorkingDirectory "{working_dir}" -PassThru'
			)
			if args:
				arg_str = " ".join(f'"{a}"' if " " in a else a for a in args)
				ps_cmd = (
					f'Start-Process -FilePath "{exe_path}" '
					f'-ArgumentList \'{arg_str}\' '
					f'-WorkingDirectory "{working_dir}" -PassThru'
				)

			result = subprocess.run(
				["powershell", "-Command", ps_cmd + " | Select-Object -ExpandProperty Id"],
				capture_output=True, text=True, timeout=10, env=process_env
			)
			pid_str = result.stdout.strip()
			if not pid_str.isdigit():
				return {
					"success": False,
					"message": f"Start-Process failed: {result.stderr.strip() or result.stdout.strip()}"
				}
			pid = int(pid_str)

			time.sleep(0.5)
			try:
				proc = psutil.Process(pid)
				if not proc.is_running():
					return {"success": False, "message": f"Process exited immediately: {name}"}
			except psutil.NoSuchProcess:
				return {"success": False, "message": f"Process exited immediately: {name}"}

			self.processes[name] = pid

			return {
				"success": True,
				"message": f"{name} started successfully",
				"pid": pid,
				"working_dir": working_dir
			}
		
		except Exception as e:
			return {
				"success": False,
				"message": f"Failed to start {name}: {str(e)}"
			}
	
	def stop_process(self, name: str, timeout: int = 5) -> Dict[str, Any]:
		"""停止进程"""
		if name not in self.processes:
			return {"success": False, "message": f"No process named '{name}' is running"}
		
		pid = self.processes[name]
		try:
			proc = psutil.Process(pid)
			proc.terminate()
			try:
				proc.wait(timeout=timeout)
			except psutil.TimeoutExpired:
				proc.kill()
				proc.wait(timeout=3)
			del self.processes[name]
			return {"success": True, "message": f"{name} stopped (PID: {pid})"}
		except psutil.NoSuchProcess:
			del self.processes[name]
			return {"success": True, "message": f"{name} already stopped (PID: {pid})"}
		except Exception as e:
			return {"success": False, "message": f"Failed to stop {name}: {str(e)}"}
	
	def stop_all(self) -> Dict[str, Any]:
		"""停止所有管理的进程
		
		Returns:
			包含停止结果的字典
		"""
		results = {}
		for name in list(self.processes.keys()):
			results[name] = self.stop_process(name)
		
		return {
			"success": True,
			"results": results,
			"stopped_count": len(results)
		}
	
	def is_running(self, name: str) -> bool:
		"""检查进程是否运行中"""
		if name not in self.processes:
			return False
		try:
			return psutil.Process(self.processes[name]).is_running()
		except psutil.NoSuchProcess:
			return False
	
	def get_status(self, name: str) -> Dict[str, Any]:
		"""获取进程状态"""
		if name not in self.processes:
			return {"running": False, "message": f"No process named '{name}'"}
		pid = self.processes[name]
		try:
			proc = psutil.Process(pid)
			return {"running": proc.is_running(), "pid": pid, "exit_code": None}
		except psutil.NoSuchProcess:
			return {"running": False, "pid": pid, "exit_code": -1}
	
	@staticmethod
	def kill_processes_by_name(process_name: str) -> Dict[str, Any]:
		"""根据进程名杀死所有匹配的进程
		
		Args:
			process_name: 进程名称（如 "app.exe"）
		
		Returns:
			包含杀死结果的字典
		"""
		killed_pids = []
		errors = []
		
		try:
			for proc in psutil.process_iter(['pid', 'name']):
				try:
					if proc.info['name'].lower() == process_name.lower():
						pid = proc.info['pid']
						proc.kill()
						killed_pids.append(pid)
				except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
					errors.append(f"PID {proc.info.get('pid')}: {str(e)}")
			
			return {
				"success": True,
				"killed_count": len(killed_pids),
				"killed_pids": killed_pids,
				"errors": errors if errors else None
			}
		
		except Exception as e:
			return {
				"success": False,
				"message": f"Failed to kill processes: {str(e)}",
				"killed_count": 0
			}

