import time
import re
from typing import Any, Dict, List

from src.core.hotupdate.client import execute_lua_on, get_connection_manager
from src.base.pipeline import SessionPipeline
from src.base.config import get_service_config
from src.base.logger import LogReader
from src.core.process.tools import start_service

def _tm_call(method: str, *args: str) -> str:
    """Build a pcall wrapper that calls ClientTestManager method and prints the return value."""
    arg_str = ", ".join(args) if args else ""
    return (
        f"local ok, r = pcall(function() "
        f"return g_lua_client_global_context.m_test_manager:{method}({arg_str}) "
        f"end)\n"
        f'if ok then print(tostring(r or "")) else print("error:" .. tostring(r)) end'
    )

def _stm_call(method: str, *args: str) -> str:
    """Build a pcall wrapper that calls ServerTestManager method and prints the return value."""
    arg_str = ", ".join(args) if args else ""
    return (
        f"local ok, r = pcall(function() "
        f"return g_lua_game_server_global_context.m_test_manager:{method}({arg_str}) "
        f"end)\n"
        f'if ok then print(tostring(r or "")) else print("error:" .. tostring(r)) end'
    )

# ==========================================
# Refactored Pipeline Steps
# ==========================================

def _step_start_server(pipe):
    cfg = get_service_config("game_server")
    exe_path = cfg.get("executable", "unknown")
    print(f"  [Start Server] Starting game_server process... ({exe_path})")
    reader = LogReader(cfg.get("log_dir", ""))
    existing = [str(f) for f in reader._all_log_files()]
    pipe.state["_pre_start_logs"] = existing
    pipe.state["server_log_dir"] = str(cfg.get("log_dir", ""))
    res = start_service("game_server", auto_kill_existing=True)
    if not res.get("success"):
        return False, res.get("message", "unknown error")
    pipe.state["server_pid"] = res["pid"]
    print(f"  [Start Server] Process started with PID={res['pid']}")
    return True, f"PID={res['pid']}"

def _step_wait_server(pipe, timeout=150):
    print(f"  [Wait Server] Waiting up to {timeout}s for server to be ready (polling hotupdate)...")
    mgr = get_connection_manager()
    cfg = get_service_config("game_server")
    c = mgr.get_client("game_server")
    c.host, c.port = "127.0.0.1", cfg.get("hotupdate_port", 10000)
    
    t0 = time.time()
    while time.time() - t0 < timeout:
        ok, msg = c.connect(timeout=2.0)
        if ok:
            alive = execute_lua_on("game_server", 'print("alive")', timeout=2.0)
            if "alive" in (alive.get("print") or ""):
                pipe.state["server_ready"] = True
                print(f"  [Wait Server] Server is ready! (took {int(time.time()-t0)}s)")
                return True, f"ready in {int(time.time()-t0)}s"
        time.sleep(3)
        
    return False, f"timeout {timeout}s"

def _step_start_client(pipe, client_wait=0):
    cfg = get_service_config("client")
    exe_path = cfg.get("executable", "unknown")
    print(f"  [Start Client] Starting client process... ({exe_path})")
    res = start_service("client", auto_kill_existing=True)
    if not res.get("success"):
        return False, res.get("message", "unknown")
    pipe.state["client_pid"] = res["pid"]
    print(f"  [Start Client] Process started with PID={res['pid']}")
    if client_wait > 0:
        time.sleep(client_wait)
    return True, f"PID={res['pid']}"

def _step_hotupdate_server(pipe):
    print("  [Hotupdate Server] Connecting to server hotupdate port...")
    mgr = get_connection_manager()
    cfg = get_service_config("game_server")
    c = mgr.get_client("game_server")
    c.host, c.port = "127.0.0.1", cfg.get("hotupdate_port", 10000)
    ok, msg = c.connect(timeout=5.0)
    if not ok:
        return False, msg
    alive = execute_lua_on("game_server", 'print("alive")', timeout=5.0)
    if "alive" not in (alive.get("print") or ""):
        return False, "connected but alive check failed"
    pipe.state["server_hotupdate"] = True
    mgr.start_monitor()
    print("  [Hotupdate Server] Connected successfully.")
    return True, "connected + alive"

def _step_hotupdate_client(pipe):
    print("  [Hotupdate Client] Connecting to client hotupdate port...")
    mgr = get_connection_manager()
    cfg = get_service_config("client")
    c = mgr.get_client("client")
    c.host, c.port = "127.0.0.1", cfg.get("hotupdate_port", 30000)
    last_err = ""
    for attempt in range(6):
        ok, msg = c.connect(timeout=5.0)
        if ok:
            pipe.state["client_hotupdate"] = True
            print(f"  [Hotupdate Client] Connected successfully on attempt {attempt+1}.")
            return True, f"connected (attempt {attempt+1})"
        last_err = msg
        print(f"  [Hotupdate Client] Attempt {attempt+1} failed, retrying in 5s...")
        time.sleep(5)
    return False, f"failed after 6 attempts: {last_err}"

def _step_connect(pipe):
    print("  [Connect] Sending connect command to client...")
    script = _tm_call("connect", '"127.0.0.1:10000;TCP"')
    for attempt in range(30):
        res = execute_lua_on("client", script, timeout=10.0)
        out = (res.get("print") or "").strip()
        if "error:no_login_widget" in out:
            print(f"  [Connect] UI not ready, retrying in 3s... (attempt {attempt+1})")
            time.sleep(3)
            continue
        if "error:" in out:
            return False, out
        pipe.state["connect_output"] = out
        print(f"  [Connect] Connect initiated. out={out}")
        time.sleep(3)
        return True, out
    return False, "failed to connect after 30 attempts"

def _step_prewar_ready(pipe):
    print("  [Ready] Waiting for team_selecting state...")
    for _ in range(20):
        state_res = execute_lua_on("client", _tm_call("queryState"), timeout=5.0)
        if not state_res.get("success"):
            print(f"  [Ready] queryState failed: {state_res}")
        state_out = (state_res.get("print") or "")
        if "game_status=team_selecting" in state_out:
            break
        time.sleep(3)
    else:
        return False, f"timeout waiting for team_selecting"

    print("  [Ready] Sending getReady command...")
    script = _tm_call("getReady")
    res = execute_lua_on("client", script, timeout=10.0)
    out = (res.get("print") or "").strip()
    if "error:" in out:
        return False, out
    pipe.state["ready_output"] = out
    print("  [Ready] getReady sent successfully.")
    return True, out

def _step_prewar_deploy(pipe):
    """完成战前部署（两阶段部署避免竞态）"""
    print("  [Deploy] Waiting for combat_deploying state...")

    # 等待进入 combat_deploying 状态
    for _ in range(20):
        state_res = execute_lua_on("client", _tm_call("queryState"), timeout=5.0)
        state_out = (state_res.get("print") or "")
        if "game_status=combat_deploying" in state_out:
            break
        time.sleep(2)
    else:
        return False, "timeout waiting for combat_deploying"

    print("  [Deploy] Sending deploy command...")
    script = _tm_call("deploy")
    res = execute_lua_on("client", script, timeout=10.0)
    out = (res.get("print") or "").strip()
    if "error:" in out:
        return False, out

    print("  [Deploy] Waiting 1s for UI auto-RPC...")
    time.sleep(1)

    print("  [Deploy] Sending deploy_finish command...")
    script = _tm_call("deploy_finish")
    res = execute_lua_on("client", script, timeout=10.0)
    out = (res.get("print") or "").strip()
    if "error:" in out:
        return False, out

    pipe.state["deploy_output"] = out
    print("  [Deploy] Deploy completed successfully.")
    return True, out


def _step_combat_deploy_start(pipe):
    """在部署界面点击开始游戏按钮"""
    print("  [Deploy Start] Waiting for combat_deploying state...")

    # 确认在 combat_deploying 状态
    state_res = execute_lua_on("client", _tm_call("queryState"), timeout=5.0)
    state_out = (state_res.get("print") or "")
    if "game_status=combat_deploying" not in state_out:
        return False, f"not in combat_deploying state: {state_out}"

    print("  [Deploy Start] Clicking start button (onStartButtonClicks)...")
    # 调用 ClientTestManager:startCombatDeploy()
    script = _tm_call("startCombatDeploy")
    res = execute_lua_on("client", script, timeout=10.0)
    out = (res.get("print") or "").strip()
    if "error:" in out:
        return False, out

    pipe.state["combat_start_output"] = out
    print(f"  [Deploy Start] Start button clicked: {out}")
    return True, out


def _step_wait_game_start(pipe, max_attempts=150):
    print(f"  [Wait Start] Waiting for game to start (up to {max_attempts*5}s)...")
    for i in range(max_attempts):
        r = execute_lua_on("client", _tm_call("queryState"), timeout=5.0)
        state_out = (r.get("print") or "")
        if "game_status=start" in state_out:
            pipe.state["game_started"] = True
            print("  [Wait Start] Game started successfully!")
            return True, "game started"
        if i % 2 == 0:
            status_match = re.search(r'game_status=(\w+)', state_out)
            status = status_match.group(1) if status_match else "unknown"
            print(f"  [Wait Start] Current status: {status} ({i*5}s)")
        time.sleep(5)
    return False, f"timeout waiting for game_start"

def _step_transfer_auth(pipe):
    print("  [Combat Setup] Transferring soldier authority...")
    res = execute_lua_on("game_server", _stm_call("transferSoldierAuthority"), timeout=15.0)
    out = (res.get("print") or "").strip()
    if "error:" in out:
        return False, out
    return True, out

def _step_disable_anticheat(pipe):
    print("  [Combat Setup] Disabling anti-cheat...")
    res = execute_lua_on("game_server", _stm_call("disableAntiCheat"), timeout=10.0)
    out = (res.get("print") or "").strip()
    if "error:" in out:
        return False, out
    return True, out


def _step_create_new_level(pipe, level_index=0):
    """为新客户端创建独立 PVE Level"""
    print(f"  [Level Create] Creating new PVE level for client {level_index}...")

    # 调用 ServerTestManager 创建新 Level
    script = _stm_call("createNewLevel")
    res = execute_lua_on("game_server", script, timeout=15.0)
    out = (res.get("print") or "").strip()

    if "error:" in out:
        return False, out

    # 解析返回的 level_id
    level_id = None
    if out and out.isdigit():
        level_id = int(out)

    if level_id:
        pipe.state[f"level_{level_index}_id"] = level_id
        print(f"  [Level Create] Created level {level_id} for client {level_index}")
        return True, f"level_id={level_id}"
    else:
        return False, f"failed to parse level_id from: {out}"


def _step_wait_for_level_ready(pipe, level_index=0, max_attempts=30):
    """等待 Level 完全就绪（有可用 Level）"""
    print(f"  [Level Wait] Waiting for level {level_index} to be ready...")

    for i in range(max_attempts):
        # 查询服务端是否有可用 Level
        script = _stm_call("queryState")
        res = execute_lua_on("game_server", script, timeout=5.0)
        out = (res.get("print") or "").strip()

        # 检查是否有可用 Level
        if "level_count=" in out:
            match = re.search(r'level_count=(\d+)', out)
            if match:
                level_count = int(match.group(1))
                if level_count > 0:
                    print(f"  [Level Wait] Level ready (count={level_count})")
                    return True, f"level_count={level_count}"

        if i % 5 == 0:
            print(f"  [Level Wait] Still waiting... ({i}s)")
        time.sleep(1)

    return False, "timeout waiting for level ready"


def _step_prepare_level_for_client(pipe, client_index=0):
    """为指定客户端准备 Level（PVE 隔离模式）"""
    print(f"  [Level Prep] Preparing level for client {client_index}...")

    # 在 PVE 模式下，服务端会自动创建新 Level
    # 我们只需要确保有可用 Level 即可
    script = _stm_call("prepareLevelForClient")
    res = execute_lua_on("game_server", script, timeout=10.0)
    out = (res.get("print") or "").strip()

    if "error:" in out:
        return False, out

    print(f"  [Level Prep] Level prepared: {out}")
    return True, out


def _step_cleanup_level(pipe, level_id=None):
    """清理指定 Level（玩家断开时）"""
    if level_id is None:
        level_id = pipe.state.get("level_id")

    if not level_id:
        return True, "no level to cleanup"

    print(f"  [Level Cleanup] Cleaning up level {level_id}...")

    script = _stm_call("cleanupLevel", str(level_id))
    res = execute_lua_on("game_server", script, timeout=10.0)
    out = (res.get("print") or "").strip()

    if "error:" in out:
        return False, out

    print(f"  [Level Cleanup] Level {level_id} cleaned up")
    return True, out

