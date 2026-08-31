"""Server Tools — 服务进程管理"""
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from src.base.process import ProcessManager
from src.base.config import load_config


# Global process manager
_process_manager = ProcessManager()

_CLIENT_N_RE = re.compile(r"^client_(\d+)$")


def _get_service_config(service_name: str) -> Dict[str, Any]:
    """Get service configuration by name, supporting client_N dynamic names."""
    config = load_config()
    services = config.get("services", {})
    if service_name in services:
        return services[service_name]
    m = _CLIENT_N_RE.match(service_name)
    if m and "client" in services:
        return services["client"]
    raise ValueError(f"Service '{service_name}' not found. Available: {list(services.keys())}")


def kill_game_server_processes(exe_name: str, wait_after_s: float = 1.0) -> Dict[str, Any]:
    """结束本机所有指定的 GameServer（释放 10000 等端口）。可在手动启动前调用。

    Args:
        exe_name: 进程名称，如 xenon_game_server_pve.exe
        wait_after_s: kill 后等待秒数，便于端口释放；start_service 内会先调用本函数再 start_process，
            start_process 内还会再 kill 一次并等待，若希望总等待更短可传 0。
    """
    r = _process_manager.kill_processes_by_name(exe_name)
    if wait_after_s > 0:
        time.sleep(wait_after_s)
    return r


def start_service(
    service_name: str,
    working_dir: Optional[str] = None,
    args: Optional[List[str]] = None,
    env: Optional[Dict[str, str]] = None,
    auto_kill_existing: bool = True
) -> Dict[str, Any]:
    """启动一个配置好的服务进程（公开 API，供 CLI / game_session_tools 调用）"""
    service = _get_service_config(service_name)

    m = _CLIENT_N_RE.match(service_name)
    kill = auto_kill_existing and (m is None or m.group(1) == "0")

    # Merge args and env from config
    final_args = args if args is not None else service.get("args", [])
    
    # Check if config has hotupdate_port and inject env vars if so
    final_env = env.copy() if env else {}
    if "hotupdate_port" in service:
        final_env["LRDB_DEBUGGER_VSCODE"] = "1"
        # 避免 Lua 调试器占用 GameServer 的主通信端口 (10000)
        debugger_port = service.get("lua_debugger_port")
        if not debugger_port:
            if service["hotupdate_port"] == 10000:
                debugger_port = 20000
            else:
                debugger_port = service["hotupdate_port"]
        final_env["LRDB_DEBUGGER_PORT"] = str(debugger_port)

    exe_path = Path(service.get("executable", ""))
    if kill and "xenon_game_server" in exe_path.name.lower():
        print(f"[start_service] 启动前结束已存在的 {exe_path.name}（避免端口占用）…")
        kr = kill_game_server_processes(exe_path.name, wait_after_s=1.0)
        if kr.get("killed_count"):
            print(f"[start_service] 已结束旧进程 PIDs: {kr.get('killed_pids')}")

    return _process_manager.start_process(
        name=service_name,
        executable=service.get("executable"),
        working_dir=working_dir or service.get("working_dir"),
        args=final_args,
        env=final_env,
        auto_kill_existing=kill,
    )


def restart_service_impl(
    service_name: str,
    args: Optional[List[str]] = None,
    auto_kill_existing: bool = True
) -> Dict[str, Any]:
    """重启一个配置好的服务进程（公开 API）"""
    _process_manager.stop_process(service_name)
    service = _get_service_config(service_name)
    
    return _process_manager.start_process(
        name=service_name,
        executable=service.get("executable"),
        working_dir=service.get("working_dir"),
        args=args,
        auto_kill_existing=auto_kill_existing
    )


def register_server_tools(app):
    """Register server management MCP tools"""
    
    @app.tool()
    def run_service(
        service: str,
        working_dir: Optional[str] = None,
        args: Optional[List[str]] = None,
        env: Optional[Dict[str, str]] = None,
        auto_kill_existing: bool = True
    ) -> Dict[str, Any]:
        """Start a configured service process in the background.
        
        Args:
            service: Service name in config.json services (e.g., "client", "game_server", "bot_server")
        """
        return {"result": start_service(service, working_dir, args, env, auto_kill_existing)}
    
    @app.tool()
    def stop_service(service: str) -> Dict[str, Any]:
        """Stop the running service process started by MCP."""
        return {"result": _process_manager.stop_process(service)}
    
    @app.tool()
    def restart_service(
        service: str,
        args: Optional[List[str]] = None,
        auto_kill_existing: bool = True
    ) -> Dict[str, Any]:
        """Restart a configured service process."""
        return {"result": restart_service_impl(service, args, auto_kill_existing)}
    
    @app.tool()
    def stop_all(services: Optional[List[str]] = None) -> Dict[str, Any]:
        """Stop multiple services.
        
        If services is None, stop all services defined in config.json.
        """
        try:
            if not services:
                config = load_config()
                services = list((config.get("services", {}) or {}).keys())
        except Exception:
            # fallback: stop whatever MCP knows about
            services = list(getattr(_process_manager, "processes", {}).keys())
        
        results: Dict[str, Any] = {}
        any_success = False
        for name in services or []:
            r = _process_manager.stop_process(name)
            results[name] = r
            any_success = any_success or bool(r.get("success"))
        
        return {"result": {"success": any_success, "results": results}}
    
    @app.tool()
    def kill_processes(process_name: str) -> Dict[str, Any]:
        """Kill all processes matching the given name.
        
        Args:
            process_name: Process name to kill (e.g., "proven_ground_bot_server.exe", "python.exe")
        
        Returns:
            Dictionary with killed process count and details
        """
        import psutil
        
        killed = []
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'] == process_name:
                    proc.kill()
                    killed.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        return {
            "result": {
                "success": len(killed) > 0,
                "killed_count": len(killed),
                "killed_processes": killed,
                "message": f"Killed {len(killed)} process(es)" if killed else "No matching processes found"
            }
        }
