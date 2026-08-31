"""多客户端状态管理

跟踪 N 个客户端进程的生命周期：PID、hotupdate 端口、连接状态、游戏状态。
供 game_session_tools 的多客户端 pipeline 使用。
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from src.core.hotupdate.client import (
    HotUpdateConnectionManager,
    execute_lua_on,
    get_connection_manager,
)


@dataclass
class ClientSlot:
    index: int
    pid: Optional[int] = None
    hotupdate_port: int = 0
    endpoint_name: str = ""
    connected: bool = False
    game_status: Optional[str] = None
    level_id: Optional[int] = None

    def __post_init__(self):
        if not self.endpoint_name:
            self.endpoint_name = f"client_{self.index}"
        if not self.hotupdate_port:
            self.hotupdate_port = HotUpdateConnectionManager.client_port(self.index)


@dataclass
class LevelSlot:
    """跟踪 Level 状态"""
    level_id: int
    client_indices: List[int] = field(default_factory=list)
    is_active: bool = True


class MultiClientManager:
    """管理 N 个客户端 slot 的生命周期与状态聚合"""

    def __init__(self):
        self.slots: Dict[int, ClientSlot] = {}
        self.server_pid: Optional[int] = None
        self.levels: Dict[int, LevelSlot] = {}  # level_id -> LevelSlot

    def get_or_create_slot(self, index: int) -> ClientSlot:
        if index not in self.slots:
            self.slots[index] = ClientSlot(index=index)
        return self.slots[index]

    def start_client(self, index: int, client_wait: float = 15.0) -> Dict[str, Any]:
        from src.base.config import get_service_config
        from src.base.process import ProcessManager

        slot = self.get_or_create_slot(index)
        cfg = get_service_config("client")
        exe = cfg["executable"]
        cwd = cfg.get("working_dir", "")

        pm = _get_process_manager()
        proc_name = f"client_{index}"

        env = {
            "LRDB_DEBUGGER_VSCODE": "1",
            "LRDB_DEBUGGER_PORT": str(slot.hotupdate_port + 1)
        }

        kill_existing = (index == 0)
        res = pm.start_process(
            name=proc_name,
            executable=exe,
            working_dir=cwd,
            env=env,
            auto_kill_existing=kill_existing,
        )
        if res.get("success"):
            slot.pid = res["pid"]
            time.sleep(client_wait)
        return res

    def connect_hotupdate(self, index: int, host: str = "127.0.0.1",
                          retries: int = 6, wait: float = 5.0) -> Dict[str, Any]:
        slot = self.get_or_create_slot(index)
        mgr = get_connection_manager()
        client = mgr.get_or_create_client(
            slot.endpoint_name, host, slot.hotupdate_port
        )
        last_err = ""
        for attempt in range(retries):
            ok, msg = client.connect(timeout=5.0)
            if ok:
                slot.connected = True
                return {"success": True, "attempt": attempt + 1, "endpoint": slot.endpoint_name}
            last_err = msg
            time.sleep(wait)
        return {"success": False, "message": last_err, "endpoint": slot.endpoint_name}

    def execute_lua(self, index: int, script: str, timeout: float = 10.0) -> Dict[str, Any]:
        slot = self.get_or_create_slot(index)
        return execute_lua_on(slot.endpoint_name, script, timeout)

    def disconnect_client(self, index: int):
        slot = self.slots.get(index)
        if not slot:
            return
        mgr = get_connection_manager()
        mgr.disconnect(slot.endpoint_name)
        slot.connected = False

    def query_state(self, index: int) -> Dict[str, Any]:
        slot = self.get_or_create_slot(index)
        from src.core.session.tools import _tm_call
        res = self.execute_lua(index, _tm_call("queryState"))
        output = (res.get("print") or "").strip()
        slot.game_status = _extract_field(output, "game_status")
        level_str = _extract_field(output, "level_id")
        if level_str:
            try:
                level_id = int(level_str)
                if level_id != slot.level_id:
                    self.set_client_level(index, level_id)
            except ValueError:
                pass
        return {"index": index, "endpoint": slot.endpoint_name, "output": output}

    def query_all(self) -> Dict[str, Any]:
        results = {}
        for idx in sorted(self.slots):
            results[f"client_{idx}"] = self.query_state(idx)
        from src.core.session.tools import _stm_call
        srv = execute_lua_on("game_server", _stm_call("diagnoseLevels"))
        results["server"] = (srv.get("print") or "").strip()
        return results

    def summary(self) -> Dict[str, Any]:
        clients = []
        for idx in sorted(self.slots):
            s = self.slots[idx]
            clients.append({
                "index": s.index,
                "endpoint": s.endpoint_name,
                "pid": s.pid,
                "port": s.hotupdate_port,
                "connected": s.connected,
                "game_status": s.game_status,
                "level_id": s.level_id,
            })

        levels = []
        for level_id, level_slot in sorted(self.levels.items()):
            levels.append({
                "level_id": level_slot.level_id,
                "client_count": len(level_slot.client_indices),
                "client_indices": level_slot.client_indices,
                "is_active": level_slot.is_active,
            })

        return {
            "server_pid": self.server_pid,
            "client_count": len(clients),
            "level_count": len(levels),
            "clients": clients,
            "levels": levels,
        }

    def reset(self):
        self.slots.clear()
        self.server_pid = None
        self.levels.clear()

    def register_level(self, level_id: int, client_index: int):
        """注册 Level 并关联客户端"""
        if level_id not in self.levels:
            self.levels[level_id] = LevelSlot(level_id=level_id)
        level_slot = self.levels[level_id]
        if client_index not in level_slot.client_indices:
            level_slot.client_indices.append(client_index)

    def unregister_level(self, level_id: int):
        """注销 Level"""
        if level_id in self.levels:
            del self.levels[level_id]

    def get_client_level(self, client_index: int) -> Optional[int]:
        """获取客户端所在的 Level ID"""
        slot = self.slots.get(client_index)
        return slot.level_id if slot else None

    def set_client_level(self, client_index: int, level_id: int):
        """设置客户端的 Level ID"""
        slot = self.get_or_create_slot(client_index)
        slot.level_id = level_id
        self.register_level(level_id, client_index)

    def get_level_clients(self, level_id: int) -> List[int]:
        """获取指定 Level 中的所有客户端索引"""
        level_slot = self.levels.get(level_id)
        return level_slot.client_indices if level_slot else []

    def query_all_with_levels(self) -> Dict[str, Any]:
        """聚合查询所有客户端 + Level 状态"""
        clients = {}
        for idx in sorted(self.slots):
            s = self.slots[idx]
            clients[f"client_{idx}"] = {
                "index": s.index,
                "endpoint": s.endpoint_name,
                "pid": s.pid,
                "connected": s.connected,
                "game_status": s.game_status,
                "level_id": s.level_id,
            }

        levels = {}
        for level_id, level_slot in self.levels.items():
            levels[f"level_{level_id}"] = {
                "level_id": level_slot.level_id,
                "client_indices": level_slot.client_indices,
                "is_active": level_slot.is_active,
            }

        return {
            "server_pid": self.server_pid,
            "clients": clients,
            "levels": levels,
        }


def _extract_field(text: str, key: str) -> Optional[str]:
    for part in text.replace(",", " ").split():
        if part.startswith(f"{key}="):
            return part[len(key) + 1:]
    return None


_multi_client_manager: Optional[MultiClientManager] = None


def get_multi_client_manager() -> MultiClientManager:
    global _multi_client_manager
    if _multi_client_manager is None:
        _multi_client_manager = MultiClientManager()
    return _multi_client_manager


_process_manager = None


def _get_process_manager():
    global _process_manager
    if _process_manager is None:
        from src.base.process import ProcessManager
        _process_manager = ProcessManager()
    return _process_manager
