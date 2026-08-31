"""Hotupdate Tools — Lua 热更新连接与执行"""
from typing import Any, Dict, Optional

from src.core.hotupdate.client import (
    HotUpdateConnectionManager,
    get_connection_manager,
)
from src.base.config import load_config


def _get_service_hotupdate_port(service_name: str) -> int:
    """Get hotupdate port for a service, supporting client_N dynamic endpoints."""
    idx = HotUpdateConnectionManager.parse_client_index(
        HotUpdateConnectionManager.normalize_endpoint(service_name)
    )
    if idx is not None:
        return HotUpdateConnectionManager.client_port(idx)
    config = load_config()
    services = config.get("services", {})
    defaults = {"game_server": 10000, "client": 30000}
    if service_name in services:
        return services[service_name].get("hotupdate_port", defaults.get(service_name, 30000))
    return defaults.get(service_name, 30000)


def register_hotupdate_tools(app):
    """Register hot-update MCP tools"""
    
    @app.tool()
    def hotupdate_connect(
        endpoint: str = "client",
        host: str = "127.0.0.1",
        port: Optional[int] = None,
        timeout: float = 5.0,
        enable_autoreconnect: bool = True
    ) -> Dict[str, Any]:
        """连接到指定端点进行热更新
        
        支持 "client", "client_0", "client_1" 等动态客户端端点。
        client_N 端口自动推导为 30000 + N*1111。

        Args:
            endpoint: 端点名称 ("client", "client_0", "client_1", "game_server")
            host: 服务器地址（默认: 127.0.0.1）
            port: 服务器端口（如不指定，自动推导）
            timeout: 连接超时时间（秒，默认: 5.0）
            enable_autoreconnect: 是否启用自动重连（默认: True）
        
        Returns:
            连接结果
        """
        if port is None:
            port = _get_service_hotupdate_port(endpoint)
        
        manager = get_connection_manager()
        manager.disconnect(endpoint)
        client = manager.get_or_create_client(endpoint, host, port)

        if enable_autoreconnect:
            manager.start_monitor()
        
        success, message = client.connect(timeout)
        
        return {
            "result": {
                "success": success,
                "endpoint": HotUpdateConnectionManager.normalize_endpoint(endpoint),
                "host": host,
                "port": port,
                "message": message,
                "autoreconnect": enable_autoreconnect
            }
        }
    
    @app.tool()
    def hotupdate_configure_autoreconnect(enable: bool = True) -> Dict[str, Any]:
        """配置热更新自动重连功能
        
        Args:
            enable: 是否启用自动重连
        """
        manager = get_connection_manager()
        if enable:
            manager.start_monitor()
            msg = "Auto-reconnect enabled"
        else:
            manager.stop_monitor()
            msg = "Auto-reconnect disabled"
        return {"result": {"success": True, "message": msg}}

    @app.tool()
    def hotupdate_disconnect(endpoint: str = "client") -> Dict[str, Any]:
        """断开指定端点的热更新连接
        
        Args:
            endpoint: 端点名称 ("client", "game_server", "all")
        
        Returns:
            断开连接结果
        """
        manager = get_connection_manager()
        
        if endpoint == "all":
            manager.disconnect_all()
            return {
                "result": {
                    "success": True,
                    "message": "All endpoints disconnected"
                }
            }
        else:
            manager.disconnect(endpoint)
            return {
                "result": {
                    "success": True,
                    "endpoint": endpoint,
                    "message": f"Endpoint {endpoint} disconnected"
                }
            }
    
    @app.tool()
    def hotupdate_status() -> Dict[str, Any]:
        """获取所有端点的热更新连接状态
        
        Returns:
            连接状态信息
        """
        manager = get_connection_manager()
        status = manager.get_status()
        
        return {
            "result": {
                "endpoints": status,
                "message": "Connection status retrieved"
            }
        }
    
    @app.tool()
    def hotupdate_execute_lua(
        script: str,
        endpoint: str = "client",
        timeout: float = 10.0
    ) -> Dict[str, Any]:
        """在指定端点执行Lua脚本热更新
        
        Args:
            script: Lua脚本内容
            endpoint: 端点名称 ("client", "game_server")
            timeout: 执行超时时间（秒，默认: 10.0）
        
        Returns:
            执行结果，包含返回值、打印输出和错误信息
        
        Example:
            >>> hotupdate_execute_lua("return 1 + 1", "client")
            {
                "success": True,
                "endpoint": "client",
                "result": "2",
                "print": "",
                "error": "",
                "message": "Success"
            }
        """
        manager = get_connection_manager()
        client = manager.get_client(endpoint)
        result = client.execute_lua(script, timeout)
        result["endpoint"] = endpoint
        
        return {"result": result}
    
    @app.tool()
    def hotupdate_require_lua(
        module: str,
        endpoint: str = "client",
        reload: bool = True,
        timeout: float = 10.0
    ) -> Dict[str, Any]:
        """通过require执行远端Lua模块（支持自动reload）"""
        normalized = module.replace("\\", "/")
        if normalized.endswith(".lua"):
            normalized = normalized[:-4]
        normalized = normalized.replace("/", ".")
        if normalized.startswith("."):
            normalized = normalized[1:]
        
        reload_flag = "true" if reload else "false"
        script = f"""
local module_name = "{normalized}"
if {reload_flag} then
    package.loaded[module_name] = nil
end
local ok, result = pcall(require, module_name)
if not ok then
    error(string.format("require('%s') failed: %s", module_name, result))
end
return result
"""
        return hotupdate_execute_lua(script, endpoint, timeout)
