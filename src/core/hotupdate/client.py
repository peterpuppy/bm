"""热更新客户端
用于连接游戏服务器并执行Lua脚本热更新
"""

import socket
import struct
import threading
import time
from typing import Optional, Tuple, Dict, Any
from queue import Queue, Empty


class HotUpdateClient:
    """热更新客户端，处理TCP连接和协议"""
    
    # 网络包通道类型
    NET_PACKAGE_CHANNEL_REMOTE_COMMAND = 2
    
    # 服务类型（从chaos_net_session.h）
    SERVICE_TYPE_GMT = 19  # GMT Tool (LuaDebugger)
    SERVICE_TYPE_CLIENT = 1  # Client
    SERVICE_TYPE_GAME_SERVER = 2  # GameServer (GAM)
    SERVICE_TYPE_BOT_SERVER = 64  # Bot Server
    
    def __init__(self, host: str = "127.0.0.1", port: int = 44444, remote_type: int = None):
        self.host = host
        self.port = port
        self.socket: Optional[socket.socket] = None
        self.connected = False
        self.session_established = False
        self.receive_thread: Optional[threading.Thread] = None
        self.running = False
        self.response_queue: Queue = Queue()
        self.request_id_counter = 1
        self.pending_requests: Dict[int, Dict[str, Any]] = {}
        self.lock = threading.Lock()
        
        # 自动推断remote_type（如果未指定）
        if remote_type is None:
            if port == 44444:
                self.remote_type = self.SERVICE_TYPE_BOT_SERVER
            elif port == 10000:
                self.remote_type = self.SERVICE_TYPE_GAME_SERVER
            elif port == 30000:
                self.remote_type = self.SERVICE_TYPE_CLIENT
            else:
                self.remote_type = self.SERVICE_TYPE_BOT_SERVER  # 默认
        else:
            self.remote_type = remote_type
        
    def connect(self, timeout: float = 5.0) -> Tuple[bool, str]:
        """连接到服务器（支持断线后重连）"""
        if self.connected:
            try:
                self.socket.getpeername()
                return True, "Already connected"
            except Exception:
                self.connected = False

        self._cleanup_old_connection()

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(timeout)
            self.socket.connect((self.host, self.port))
            self.socket.settimeout(None)
            
            self.connected = True
            
            success, msg = self._session_handshake(timeout=timeout)
            if not success:
                self.socket.close()
                self.connected = False
                return False, f"Handshake failed: {msg}"
            
            self.running = True
            self.receive_thread = threading.Thread(target=self._receive_loop, daemon=True)
            self.receive_thread.start()
            
            return True, f"Connected to {self.host}:{self.port}"
        except socket.timeout:
            self.connected = False
            return False, f"Connection timeout to {self.host}:{self.port}"
        except Exception as e:
            self.connected = False
            return False, f"Connection failed: {str(e)}"

    def _cleanup_old_connection(self):
        """Clean up stale socket and receive thread before reconnecting."""
        self.running = False
        if self.socket:
            try:
                self.socket.shutdown(socket.SHUT_RDWR)
            except Exception:
                pass
            try:
                self.socket.close()
            except Exception:
                pass
            self.socket = None
        if self.receive_thread and self.receive_thread.is_alive():
            self.receive_thread.join(timeout=1.0)
        self.receive_thread = None
        self.session_established = False
        while not self.response_queue.empty():
            try:
                self.response_queue.get_nowait()
            except Empty:
                break
    
    def disconnect(self) -> Tuple[bool, str]:
        """断开连接"""
        try:
            self._cleanup_old_connection()
            self.connected = False
            return True, "Disconnected"
        except Exception as e:
            self.connected = False
            return False, f"Disconnect error: {str(e)}"
    
    def is_connected(self) -> bool:
        """检查是否已连接"""
        return self.connected
    
    def _session_handshake(self, timeout: float = 5.0) -> Tuple[bool, str]:
        """执行session握手"""
        try:
            random_key_len = 16
            content_offset = 8
            random_key = bytes([i % 256 for i in range(random_key_len)])
            
            local_type = self.SERVICE_TYPE_GMT
            remote_type = self.remote_type
            is_reconnect = 0
            head_info = (local_type << 48) | (remote_type << 32) | is_reconnect
            
            first_packet_body = b""
            first_packet_body += struct.pack("<i", random_key_len)
            first_packet_body += struct.pack("<i", content_offset)
            first_packet_body += random_key[:content_offset]
            first_packet_body += struct.pack("<Q", head_info)
            first_packet_body += random_key[content_offset:]
            
            packet_length = len(first_packet_body)
            first_packet = struct.pack("<H", packet_length) + first_packet_body
            self.socket.sendall(first_packet)
            time.sleep(0.5)
            
            self.session_established = True
            return True, "Session established"
        except Exception as e:
            return False, f"Handshake error: {str(e)}"
    
    def execute_lua(self, script: str, timeout: float = 10.0) -> Dict[str, Any]:
        """执行Lua脚本"""
        if not self.connected or not self.session_established:
            return {
                "success": False,
                "result": "",
                "print": "",
                "error": "",
                "message": "Not connected to server or session not established"
            }
        
        try:
            with self.lock:
                request_id = self.request_id_counter
                self.request_id_counter += 1
                if self.request_id_counter > 0xFFFFFF:
                    self.request_id_counter = 1
            
            success, msg = self._send_lua_script(request_id, script)
            if not success:
                return {
                    "success": False,
                    "result": "",
                    "print": "",
                    "error": "",
                    "message": f"Send failed: {msg}"
                }
            
            start_time = time.time()
            while time.time() - start_time < timeout:
                try:
                    response = self.response_queue.get(timeout=0.1)
                    if response["request_id"] == request_id:
                        return response
                    self.response_queue.put(response)
                except Empty:
                    continue
            
            return {
                "success": False,
                "result": "",
                "print": "",
                "error": "",
                "message": f"Timeout after {timeout} seconds"
            }
        except Exception as e:
            return {
                "success": False,
                "result": "",
                "print": "",
                "error": "",
                "message": f"Execute error: {str(e)}"
            }
    
    def _send_lua_script(self, request_id: int, script: str) -> Tuple[bool, str]:
        """发送Lua脚本"""
        try:
            script_bytes = script.encode("utf-8")
            rpc_id = 0x20
            field2 = 0
            field3 = request_id
            packet_body = struct.pack("<III", rpc_id, field2, field3) + script_bytes
            packet_length = len(packet_body)
            packet = struct.pack("<H", packet_length) + packet_body
            self.socket.sendall(packet)
            return True, "Sent"
        except Exception as e:
            self.connected = False
            return False, f"Send error: {str(e)}"
    
    def _receive_loop(self):
        """接收线程循环"""
        buffer = b""
        while self.running:
            try:
                data = self.socket.recv(4096)
                if not data:
                    self.connected = False
                    break
                buffer += data
                while len(buffer) >= 2:
                    packet_length = struct.unpack("<H", buffer[:2])[0]
                    if len(buffer) < 2 + packet_length:
                        break
                    packet_data = buffer[2:2 + packet_length]
                    buffer = buffer[2 + packet_length:]
                    self._parse_response(packet_data)
            except socket.timeout:
                continue
            except Exception:
                self.connected = False
                break
    
    def _parse_response(self, packet_data: bytes):
        """解析响应包"""
        try:
            if len(packet_data) < 12:
                return
            _, _, service_request_id = struct.unpack("<III", packet_data[:12])
            content = packet_data[12:].decode("utf-8", errors="replace")
            
            response = {
                "success": True,
                "request_id": service_request_id,
                "result": self._extract_xml_content(content, "ret"),
                "print": self._extract_xml_content(content, "print"),
                "error": self._extract_xml_content(content, "err"),
                "message": "Success"
            }
            if response["error"]:
                response["success"] = False
                response["message"] = "Error"
            
            self.response_queue.put(response)
        except Exception:
            return
    
    def _extract_xml_content(self, xml_str: str, tag: str) -> str:
        """提取XML标签内容（简单CDATA处理）"""
        try:
            start_tag = f"<{tag}>"
            end_tag = f"</{tag}>"
            start_idx = xml_str.find(start_tag)
            if start_idx == -1:
                return ""
            end_idx = xml_str.find(end_tag, start_idx)
            if end_idx == -1:
                return ""
            content = xml_str[start_idx + len(start_tag):end_idx]
            cdata_start = content.find("<![CDATA[")
            if cdata_start != -1:
                cdata_end = content.find("]]>", cdata_start)
                if cdata_end != -1:
                    content = content[cdata_start + 9:cdata_end]
            return content.strip()
        except Exception:
            return ""


class HotUpdateConnectionManager:
    """管理多个热更新连接，支持动态端点（多客户端 client_0/client_1/...）"""

    CLIENT_BASE_PORT = 30000
    CLIENT_PORT_STEP = 1111
    SERVER_PORT = 10000

    def __init__(self):
        self.connections: Dict[str, Optional[HotUpdateClient]] = {}
        self.lock = threading.Lock()
        self.auto_reconnect = False
        self.monitor_thread = None
        self.monitor_running = False

    @classmethod
    def normalize_endpoint(cls, endpoint: str) -> str:
        if endpoint == "client":
            return "client_0"
        return endpoint

    @classmethod
    def client_port(cls, index: int) -> int:
        return cls.CLIENT_BASE_PORT + index * cls.CLIENT_PORT_STEP

    @classmethod
    def parse_client_index(cls, endpoint: str) -> Optional[int]:
        """Return the integer index if endpoint matches 'client_N', else None."""
        if endpoint.startswith("client_"):
            try:
                return int(endpoint[7:])
            except ValueError:
                pass
        return None

    @classmethod
    def _infer_remote_type(cls, endpoint: str, port: int) -> int:
        if endpoint == "game_server" or port == cls.SERVER_PORT:
            return HotUpdateClient.SERVICE_TYPE_GAME_SERVER
        if cls.parse_client_index(endpoint) is not None:
            return HotUpdateClient.SERVICE_TYPE_CLIENT
        if endpoint == "bot_server" or port == 44444:
            return HotUpdateClient.SERVICE_TYPE_BOT_SERVER
        return HotUpdateClient.SERVICE_TYPE_BOT_SERVER

    def get_client(self, endpoint: str = "bot_server") -> HotUpdateClient:
        endpoint = self.normalize_endpoint(endpoint)
        # Avoid deadlock by not using get_or_create_client while holding the lock
        # or just use get_or_create_client directly since it acquires the lock itself
        return self.get_or_create_client(endpoint)

    def get_or_create_client(self, endpoint: str, host: str = "127.0.0.1",
                             port: Optional[int] = None) -> HotUpdateClient:
        endpoint = self.normalize_endpoint(endpoint)
        if port is None:
            idx = self.parse_client_index(endpoint)
            if idx is not None:
                port = self.client_port(idx)
            elif endpoint == "game_server":
                port = self.SERVER_PORT
            else:
                port = 44444
        remote_type = self._infer_remote_type(endpoint, port)
        with self.lock:
            existing = self.connections.get(endpoint)
            if existing and existing.is_connected():
                return existing
            client = HotUpdateClient(host, port, remote_type=remote_type)
            self.connections[endpoint] = client
            return client

    def disconnect(self, endpoint: str):
        endpoint = self.normalize_endpoint(endpoint)
        with self.lock:
            if endpoint in self.connections and self.connections[endpoint]:
                self.connections[endpoint].disconnect()

    def disconnect_all(self):
        with self.lock:
            for client in self.connections.values():
                if client:
                    client.disconnect()

    def remove_endpoint(self, endpoint: str):
        endpoint = self.normalize_endpoint(endpoint)
        with self.lock:
            client = self.connections.pop(endpoint, None)
            if client:
                client.disconnect()

    def get_status(self):
        with self.lock:
            status = {}
            for endpoint, client in self.connections.items():
                if client:
                    status[endpoint] = {
                        "connected": client.connected,
                        "host": client.host,
                        "port": client.port,
                        "auto_reconnect": self.auto_reconnect
                    }
                else:
                    status[endpoint] = {
                        "connected": False,
                        "host": None,
                        "port": None,
                        "auto_reconnect": self.auto_reconnect
                    }
            return status

    def connected_client_endpoints(self) -> list:
        with self.lock:
            return [
                ep for ep, c in self.connections.items()
                if c and c.connected and self.parse_client_index(ep) is not None
            ]

    def start_monitor(self):
        with self.lock:
            if self.monitor_running:
                return
            self.monitor_running = True
            self.auto_reconnect = True
            self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
            self.monitor_thread.start()

    def stop_monitor(self):
        self.monitor_running = False
        self.auto_reconnect = False

    def _monitor_loop(self):
        _consecutive_fails: Dict[str, int] = {}
        while self.monitor_running:
            try:
                time.sleep(3)
                if not self.auto_reconnect:
                    continue
                with self.lock:
                    endpoints = list(self.connections.keys())
                for endpoint in endpoints:
                    client = self.connections.get(endpoint)
                    if client and not client.connected and client.host and client.port:
                        try:
                            ok, _ = client.connect(timeout=3.0)
                            if ok:
                                _consecutive_fails[endpoint] = 0
                            else:
                                _consecutive_fails[endpoint] = _consecutive_fails.get(endpoint, 0) + 1
                                if _consecutive_fails[endpoint] >= 3:
                                    new_client = HotUpdateClient(
                                        client.host, client.port,
                                        remote_type=client.remote_type)
                                    with self.lock:
                                        self.connections[endpoint] = new_client
                                    _consecutive_fails[endpoint] = 0
                        except Exception:
                            pass
            except Exception:
                time.sleep(1)


_connection_manager: Optional[HotUpdateConnectionManager] = None


def get_connection_manager() -> HotUpdateConnectionManager:
    """获取全局连接管理器"""
    global _connection_manager
    if _connection_manager is None:
        _connection_manager = HotUpdateConnectionManager()
    return _connection_manager


def reset_connection_manager():
    """重置全局连接管理器"""
    global _connection_manager
    if _connection_manager:
        _connection_manager.disconnect_all()
        _connection_manager.stop_monitor()
    _connection_manager = None


def execute_lua_on(endpoint: str, script: str, timeout: float = 10.0,
                    auto_reconnect: bool = True) -> Dict[str, Any]:
    """在指定端点执行 Lua 脚本（断线时自动尝试重连一次）"""
    manager = get_connection_manager()
    endpoint = HotUpdateConnectionManager.normalize_endpoint(endpoint)
    client = manager.get_client(endpoint)

    if not client.is_connected() and auto_reconnect and client.host and client.port:
        ok, msg = client.connect(timeout=min(timeout, 5.0))
        if not ok:
            return {"success": False, "error": f"{endpoint} reconnect failed: {msg}"}

    if not client.is_connected():
        return {"success": False, "error": f"{endpoint} hotupdate not connected"}

    result = client.execute_lua(script, timeout)

    if not result.get("success") and "Send failed" in result.get("message", ""):
        if auto_reconnect and client.host and client.port:
            ok, msg = client.connect(timeout=min(timeout, 5.0))
            if ok:
                return client.execute_lua(script, timeout)

    return result

