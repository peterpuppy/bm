"""Game Session Tools — 游戏会话控制与编排

通过 Lua hotupdate 实现：
- 客户端操作通过 ClientTestManager (g_lua_client_global_context.m_test_manager)
- 服务端操作通过 ServerTestManager (g_lua_game_server_global_context.m_test_manager)
"""
import time
from typing import Any, Dict, List, Optional

from src.core.hotupdate.client import execute_lua_on
from src.base.pipeline import SessionPipeline
from src.core.session.state import get_multi_client_manager
from src.base.config import get_service_config
from src.core.session import steps


def _standardize_result(
    success: bool,
    message: str,
    data: Dict[str, Any] = None,
    recommendations: List[str] = None
) -> Dict[str, Any]:
    """标准化返回格式"""
    return {
        "success": success,
        "message": message,
        "data": data or {},
        "recommendations": recommendations or [],
    }


def run_game_start_pve_session(
    server_timeout: int = 150,
    client_wait: int = 15,
) -> Dict[str, Any]:
    """最简流程：启动服务器和客户端，连接并进入游戏

    完整阶段:
    1. start_server — 启动 GameServer 进程
    2. wait_server_ready — 等待服务端就绪
    3. start_client — 启动客户端进程
    4. connect_hotupdates — 并行建立双端热更连接
    5. connect_to_server — 客户端直连服务器
    6. prewar_ready — 等待 team_selecting 并准备就绪 (getReady)
    7. prewar_deploy — 完成战前部署（选择兵团）
    8. combat_deploy_start — 点击开始游戏按钮 (onStartButtonClicks)
    9. wait_game_start — 等待 game_status=start
    """
    pipe = SessionPipeline()

    # 1. 启动服务端
    pipe.add("start_server", lambda: steps._step_start_server(pipe))

    # 2. 等待服务端就绪
    pipe.add("wait_server_ready", lambda: steps._step_wait_server(pipe, timeout=server_timeout))

    # 3. 启动客户端
    pipe.add("start_client", lambda: steps._step_start_client(pipe, client_wait=client_wait))

    # 4. 并行连接双端的热更端口
    pipe.add_parallel("connect_hotupdates", {
        "hotupdate_server": lambda: steps._step_hotupdate_server(pipe),
        "hotupdate_client": lambda: steps._step_hotupdate_client(pipe)
    })

    # 5. 客户端直连服务器
    pipe.add("connect_to_server", lambda: steps._step_connect(pipe))

    # 6. 准备并进入游戏（Prewar 流程）
    pipe.add("prewar_ready", lambda: steps._step_prewar_ready(pipe))

    # 7. 完成战前部署（选择兵团等）
    pipe.add("prewar_deploy", lambda: steps._step_prewar_deploy(pipe))

    # 8. 点击开始游戏按钮（从部署界面进入战斗）
    pipe.add("combat_deploy_start", lambda: steps._step_combat_deploy_start(pipe))

    # 9. 等待游戏开始
    pipe.add("wait_game_start", lambda: steps._step_wait_game_start(pipe, max_attempts=150))

    report = pipe.run(stop_on_fail=True)

    # 标准化返回格式
    success = report.get("success", False)
    failed_step = report.get("failed_step", "")

    if success:
        return _standardize_result(
            success=True,
            message=f"PVE session started successfully (completed {len(report.get('results', []))} steps)",
            data={
                "steps_completed": len(report.get('results', [])),
                "duration_seconds": report.get('duration_seconds', 0),
                "step_results": report.get('results', []),
            },
            recommendations=["Run verify_game_started() to confirm game state"]
        )
    else:
        recommendations = []
        if failed_step:
            recommendations.append(f"Failed at step: {failed_step}")
            if "wait_server" in failed_step:
                recommendations.append("Check GameServer logs for startup errors")
            elif "connect" in failed_step:
                recommendations.append("Verify network connectivity and ports")
            elif "prewar" in failed_step:
                recommendations.append("Check if game level is properly configured")

        return _standardize_result(
            success=False,
            message=f"PVE session failed at step: {failed_step}",
            data={
                "failed_step": failed_step,
                "step_results": report.get('results', []),
                "duration_seconds": report.get('duration_seconds', 0),
            },
            recommendations=recommendations
        )


def register_game_session_tools(app):

    @app.tool()
    def game_connect_to_server(
        address: str = "127.0.0.1:10000",
        protocol: str = "TCP",
    ) -> Dict[str, Any]:
        """通过 login_level:connectToServer 让客户端直连 gameserver"""
        addr = f"{address};{protocol}"
        script = steps._tm_call("connect", f'"{addr}"')
        res = execute_lua_on("client", script, timeout=10.0)
        output = (res.get("print") or "").strip()

        success = "connect_initiated" in output or "connected" in output.lower()

        if success:
            return _standardize_result(
                success=True,
                message=f"Client connecting to {addr}",
                data={"address": addr, "output_preview": output[:200]},
                recommendations=["Wait for game status to change to 'team_selecting'"]
            )
        else:
            return _standardize_result(
                success=False,
                message=f"Failed to initiate connection: {output[:100]}",
                data={"address": addr, "output": output},
                recommendations=[
                    "Check if GameServer is running",
                    "Verify address and port are correct",
                    "Check client hotupdate connection",
                ]
            )

    @app.tool()
    def game_login_status() -> Dict[str, Any]:
        """查询客户端 login_level 状态机"""
        script = steps._tm_call("queryState")
        res = execute_lua_on("client", script, timeout=10.0)

        if res.get("success"):
            output = res.get("print", "")
            # 解析状态
            import re
            status_match = re.search(r'game_status=(\w+)', output)
            status = status_match.group(1) if status_match else "unknown"

            return _standardize_result(
                success=True,
                message=f"Client status: {status}",
                data={
                    "status": status,
                    "raw_output": output[:500],
                },
                recommendations=[]
            )
        else:
            return _standardize_result(
                success=False,
                message="Failed to query login status",
                data={"error": res.get("error", "Unknown error")},
                recommendations=[
                    "Check if client hotupdate is connected",
                    "Verify client is running",
                ]
            )

    @app.tool()
    def game_query_server_state() -> Dict[str, Any]:
        """查询服务端状态：level 数量、玩家数、ruler 状态、anonymous mode 等"""
        script = steps._stm_call("queryState")
        res = execute_lua_on("game_server", script, timeout=10.0)

        if res.get("success"):
            output = res.get("print", "")
            return _standardize_result(
                success=True,
                message="Server state retrieved successfully",
                data={"raw_output": output[:800]},
                recommendations=[]
            )
        else:
            return _standardize_result(
                success=False,
                message="Failed to query server state",
                data={"error": res.get("error", "Unknown error")},
                recommendations=[
                    "Check if GameServer is running",
                    "Verify game_server hotupdate connection",
                ]
            )

    @app.tool()
    def game_query_client_state() -> Dict[str, Any]:
        """查询客户端状态：login_level 状态、game_level、ruler、hero 等"""
        script = steps._tm_call("queryState")
        res = execute_lua_on("client", script, timeout=10.0)

        if res.get("success"):
            output = res.get("print", "")
            return _standardize_result(
                success=True,
                message="Client state retrieved successfully",
                data={"raw_output": output[:800]},
                recommendations=[]
            )
        else:
            return _standardize_result(
                success=False,
                message="Failed to query client state",
                data={"error": res.get("error", "Unknown error")},
                recommendations=[
                    "Check if client is running",
                    "Verify client hotupdate connection",
                ]
            )

    @app.tool()
    def game_skip_prewar() -> Dict[str, Any]:
        """PVE 模式下在服务端跳过 prewar"""
        script = steps._stm_call("skipPrewar")
        res = execute_lua_on("game_server", script, timeout=10.0)
        output = (res.get("print") or "").strip()

        success = "prewar_skipped" in output or "skipped" in output.lower()

        if success:
            return _standardize_result(
                success=True,
                message="Prewar phase skipped successfully",
                data={"output_preview": output[:200]},
                recommendations=["Game should now proceed to 'team_selecting' state"]
            )
        else:
            return _standardize_result(
                success=False,
                message=f"Failed to skip prewar: {output[:100]}",
                data={"output": output},
                recommendations=[
                    "Check if game_server hotupdate is connected",
                    "Verify skipPrewar method exists in ServerTestManager",
                ]
            )

    @app.tool()
    def game_start_pve_session(
        server_timeout: int = 150,
        client_wait: int = 15,
    ) -> Dict[str, Any]:
        """最简流程：启动服务器和客户端，连接并进入游戏

        Args:
            server_timeout: 等待服务端就绪的超时时间（秒，默认 150）
            client_wait: 启动客户端后的等待时间（秒，默认 15）

        Returns:
            {
                "success": bool,
                "message": str,
                "data": {
                    "steps_completed": int,
                    "duration_seconds": float,
                    "step_results": List[Dict],
                },
                "recommendations": List[str],
            }
        """
        return run_game_start_pve_session(server_timeout, client_wait)

    @app.tool()
    def game_query_all_clients() -> Dict[str, Any]:
        """聚合查询所有已连接客户端 + 服务端状态"""
        try:
            mcm = get_multi_client_manager()
            result = mcm.query_all()

            return _standardize_result(
                success=True,
                message=f"Queried {len(result.get('clients', []))} clients",
                data=result,
                recommendations=[]
            )
        except Exception as e:
            return _standardize_result(
                success=False,
                message=f"Failed to query clients: {str(e)}",
                data={},
                recommendations=[
                    "Check if multi-client manager is initialized",
                    "Verify client connections",
                ]
            )

    @app.tool()
    def game_combat_deploy_start() -> Dict[str, Any]:
        """在兵团部署界面点击开始游戏按钮

        适用场景：
        - 用户已经在 combat_deploying 界面
        - 需要调用 onStartButtonClicks 进入游戏
        - 会等待状态从 combat_deploying -> loading -> start

        Returns:
            {
                "success": bool,
                "message": str,
                "data": {
                    "clicked": bool,
                    "final_status": str,
                    "duration_seconds": float,
                },
                "recommendations": List[str],
            }
        """
        import time

        start_time = time.time()

        # 1. 检查当前状态
        print("[Combat Deploy] Checking current game status...")
        state_res = execute_lua_on("client", steps._tm_call("queryState"), timeout=5.0)
        state_out = (state_res.get("print") or "")

        if "game_status=combat_deploying" not in state_out:
            status_match = re.search(r'game_status=(\w+)', state_out)
            current_status = status_match.group(1) if status_match else "unknown"
            return _standardize_result(
                success=False,
                message=f"Not in combat_deploying state (current: {current_status})",
                data={"current_status": current_status},
                recommendations=[
                    "Wait until game reaches 'combat_deploying' state",
                    "Check status with game_query_client_status()",
                ]
            )

        # 2. 点击开始游戏按钮
        print("[Combat Deploy] Clicking start button (onStartButtonClicks)...")
        script = steps._tm_call("startCombatDeploy")
        res = execute_lua_on("client", script, timeout=10.0)
        out = (res.get("print") or "").strip()

        if "error:" in out:
            return _standardize_result(
                success=False,
                message=f"Failed to click start button: {out}",
                data={"output": out},
                recommendations=[
                    "Ensure ClientTestManager:startCombatDeploy() exists",
                    "Check client logs for UI errors",
                ]
            )

        # 3. 等待进入游戏
        print("[Combat Deploy] Waiting for game to start...")
        max_attempts = 60  # 最多等待 60 秒
        for i in range(max_attempts):
            r = execute_lua_on("client", steps._tm_call("queryState"), timeout=5.0)
            state_out = (r.get("print") or "")

            if "game_status=start" in state_out:
                duration = time.time() - start_time
                return _standardize_result(
                    success=True,
                    message="Game started successfully from combat deploy screen",
                    data={
                        "clicked": True,
                        "final_status": "start",
                        "duration_seconds": round(duration, 2),
                    },
                    recommendations=[]
                )

            if i % 10 == 0:  # 每 10 秒输出一次状态
                status_match = re.search(r'game_status=(\w+)', state_out)
                status = status_match.group(1) if status_match else "unknown"
                print(f"[Combat Deploy] Current status: {status} ({i}s)")

            time.sleep(1)

        # 超时
        duration = time.time() - start_time
        return _standardize_result(
            success=False,
            message="Timeout waiting for game to start after clicking start button",
            data={
                "clicked": True,
                "final_status": state_out[:200],
                "duration_seconds": round(duration, 2),
            },
            recommendations=[
                "Check if deploy was completed (兵团是否已选择)",
                "Verify startCombatDeploy method works correctly",
                "Check client logs for errors",
            ]
        )


    @app.tool()
    def game_disconnect_client(client_index: int = 0) -> Dict[str, Any]:
        """断开指定客户端的 hotupdate 连接（模拟断线测试）"""
        try:
            mcm = get_multi_client_manager()
            slot = mcm.slots.get(client_index)
            if not slot:
                return _standardize_result(
                    success=False,
                    message=f"client_{client_index} not found",
                    data={"client_index": client_index},
                    recommendations=["Check if client was started", "Verify client_index is correct"]
                )

            endpoint_name = slot.endpoint_name
            mcm.disconnect_client(client_index)

            if slot.pid:
                try:
                    import psutil
                    proc = psutil.Process(slot.pid)
                    proc.kill()
                except Exception:
                    pass
                slot.pid = None

            return _standardize_result(
                success=True,
                message=f"client_{client_index} disconnected and process killed",
                data={"client_index": client_index, "endpoint": endpoint_name},
                recommendations=["Client can be reconnected with game_start_pve_session()"]
            )
        except Exception as e:
            return _standardize_result(
                success=False,
                message=f"Failed to disconnect client_{client_index}: {str(e)}",
                data={"client_index": client_index},
                recommendations=["Check if multi-client manager is initialized"]
            )

    @app.tool()
    def game_create_pve_level() -> Dict[str, Any]:
        """创建新的 PVE Level

        Returns:
            {
                "success": bool,
                "message": str,
                "data": {
                    "level_id": int,
                },
                "recommendations": List[str],
            }
        """
        try:
            # 调用 ServerTestManager 创建新 Level
            script = steps._stm_call("createNewLevel")
            res = execute_lua_on("game_server", script, timeout=15.0)
            out = (res.get("print") or "").strip()

            if "error:" in out:
                return _standardize_result(
                    success=False,
                    message=f"Failed to create PVE level: {out}",
                    data={},
                    recommendations=["Check if GameServer is running", "Verify ServerTestManager:createNewLevel() exists"]
                )

            # 解析 level_id
            level_id = None
            if out and out.isdigit():
                level_id = int(out)

            if level_id:
                return _standardize_result(
                    success=True,
                    message=f"PVE level {level_id} created successfully",
                    data={"level_id": level_id},
                    recommendations=["Assign client to this level with game_assign_client_to_level()"]
                )
            else:
                return _standardize_result(
                    success=False,
                    message=f"Failed to parse level_id from output: {out}",
                    data={"output": out},
                    recommendations=["Check ServerTestManager:createNewLevel() return value"]
                )
        except Exception as e:
            return _standardize_result(
                success=False,
                message=f"Failed to create PVE level: {str(e)}",
                data={},
                recommendations=["Check if GameServer is running", "Verify hotupdate connection"]
            )

    @app.tool()
    def game_query_multi_level_state() -> Dict[str, Any]:
        """查询多 Level PVE 状态

        Returns:
            {
                "success": bool,
                "message": str,
                "data": {
                    "level_count": int,
                    "levels": List[Dict],
                    "clients": List[Dict],
                },
                "recommendations": List[str],
            }
        """
        try:
            # 查询服务端 Level 状态
            script = steps._stm_call("diagnoseLevels")
            srv_res = execute_lua_on("game_server", script, timeout=10.0)
            srv_out = (srv_res.get("print") or "").strip()

            # 查询所有客户端状态
            mcm = get_multi_client_manager()
            client_results = {}
            for idx in sorted(mcm.slots):
                client_res = mcm.query_state(idx)
                client_results[f"client_{idx}"] = client_res

            # 解析 level_count
            level_count = 0
            level_match = re.search(r'level_count=(\d+)', srv_out)
            if level_match:
                level_count = int(level_match.group(1))

            return _standardize_result(
                success=True,
                message=f"Multi-level state: {level_count} levels, {len(mcm.slots)} clients",
                data={
                    "level_count": level_count,
                    "server_diagnosis": srv_out[:500],
                    "clients": client_results,
                },
                recommendations=[]
            )
        except Exception as e:
            return _standardize_result(
                success=False,
                message=f"Failed to query multi-level state: {str(e)}",
                data={},
                recommendations=["Check if GameServer is running", "Verify multi-client manager is initialized"]
            )

    @app.tool()
    def game_start_multi_pve_session(
        client_count: int = 2,
        server_timeout: int = 150,
        client_wait: int = 15,
    ) -> Dict[str, Any]:
        """启动多客户端 PVE 会话，每个客户端在独立 Level

        Args:
            client_count: 客户端数量（默认 2）
            server_timeout: 等待服务端就绪超时（秒）
            client_wait: 启动客户端后等待时间（秒）

        Returns:
            {
                "success": bool,
                "message": str,
                "data": {
                    "levels": List[{"level_id": int, "client_index": int}],
                    "duration_seconds": float,
                },
                "recommendations": List[str],
            }
        """
        import time

        if client_count < 1 or client_count > 4:
            return _standardize_result(
                success=False,
                message=f"client_count must be between 1 and 4, got {client_count}",
                data={},
                recommendations=["Use client_count=2 for dual-level testing"]
            )

        start_time = time.time()
        pipe = SessionPipeline()
        mcm = get_multi_client_manager()

        # 1. 启动服务端
        pipe.add("start_server", lambda: steps._step_start_server(pipe))

        # 2. 等待服务端就绪
        pipe.add("wait_server_ready", lambda: steps._step_wait_server(pipe, timeout=server_timeout))

        # 3. 启动所有客户端（串行，避免时序问题）
        for i in range(client_count):
            pipe.add(f"start_client_{i}", lambda idx=i: steps._step_start_client(pipe, client_wait=client_wait if idx == 0 else 5))

        # 4. 连接所有客户端的热更端口
        hotupdate_tasks = {f"hotupdate_client_{i}": lambda idx=i: steps._step_hotupdate_client(pipe) for i in range(client_count)}
        hotupdate_tasks["hotupdate_server"] = lambda: steps._step_hotupdate_server(pipe)
        pipe.add_parallel("connect_hotupdates", hotupdate_tasks)

        # 5. 每个客户端连接服务器（PVE 模式下会自动分配到独立 Level）
        for i in range(client_count):
            pipe.add(f"connect_client_{i}", lambda idx=i: steps._step_connect(pipe))

        # 6. 所有客户端准备就绪（Prewar 流程）
        for i in range(client_count):
            pipe.add(f"prewar_ready_{i}", lambda idx=i: steps._step_prewar_ready(pipe))

        # 7. 所有客户端完成部署
        for i in range(client_count):
            pipe.add(f"prewar_deploy_{i}", lambda idx=i: steps._step_prewar_deploy(pipe))

        # 8. 所有客户端点击开始游戏
        for i in range(client_count):
            pipe.add(f"combat_deploy_start_{i}", lambda idx=i: steps._step_combat_deploy_start(pipe))

        # 9. 等待所有客户端游戏开始
        for i in range(client_count):
            pipe.add(f"wait_game_start_{i}", lambda idx=i: steps._step_wait_game_start(pipe, max_attempts=60))

        report = pipe.run(stop_on_fail=True)

        duration = time.time() - start_time
        success = report.get("success", False)

        if success:
            # 查询最终状态
            query_res = game_query_multi_level_state()
            return _standardize_result(
                success=True,
                message=f"Multi-PVE session started with {client_count} clients",
                data={
                    "client_count": client_count,
                    "duration_seconds": round(duration, 2),
                    "step_results": report.get('results', []),
                    "final_state": query_res.get('data', {}),
                },
                recommendations=["Verify level isolation with game_query_multi_level_state()"]
            )
        else:
            failed_step = report.get("failed_step", "")
            return _standardize_result(
                success=False,
                message=f"Multi-PVE session failed at step: {failed_step}",
                data={
                    "failed_step": failed_step,
                    "duration_seconds": round(duration, 2),
                },
                recommendations=["Check GameServer logs", "Verify PVE isolation is enabled in Game Repo"]
            )

    @app.tool()
    def game_diagnose_level_isolation() -> Dict[str, Any]:
        """诊断Level隔离状态

        Returns:
            {
                "success": bool,
                "message": str,
                "data": {
                    "level_count": int,
                    "levels": [{"id": int, "players": int, "available": bool}],
                    "is_isolated": bool,
                }
            }
        """
        import re

        try:
            # 调用 ServerTestManager 诊断 Level 状态
            script = steps._stm_call("diagnoseLevels")
            res = execute_lua_on("game_server", script, timeout=10.0)

            if not res.get("success"):
                return _standardize_result(
                    success=False,
                    message="Failed to execute diagnoseLevels on game_server",
                    data={"error": res.get("error", "Unknown error")},
                    recommendations=["Check if GameServer is running", "Verify hotupdate connection"]
                )

            output = (res.get("print") or "").strip()

            # 解析 Level 数量
            level_count = 0
            count_match = re.search(r'total_levels=(\d+)', output)
            if count_match:
                level_count = int(count_match.group(1))

            # 解析每个 Level 的信息
            levels = []
            level_pattern = r'level\[(\d+)\].*?players=(\d+).*?available=(\w+)'
            for match in re.finditer(level_pattern, output):
                level_id = int(match.group(1))
                players = int(match.group(2))
                available = match.group(3).lower() == "true"
                levels.append({
                    "id": level_id,
                    "players": players,
                    "available": available
                })

            # 判断隔离状态：至少2个Level且每个Level只有1个玩家
            is_isolated = level_count >= 2 and all(l["players"] == 1 for l in levels)

            return _standardize_result(
                success=True,
                message=f"Level isolation: {'isolated' if is_isolated else 'not isolated'} ({level_count} levels)",
                data={
                    "level_count": level_count,
                    "levels": levels,
                    "is_isolated": is_isolated,
                    "raw_output": output,
                },
                recommendations=[] if is_isolated else ["Check if anonymous login mode is enabled", "Verify clients are connecting properly"]
            )
        except Exception as e:
            return _standardize_result(
                success=False,
                message=f"Failed to diagnose level isolation: {str(e)}",
                data={},
                recommendations=["Check if GameServer is running", "Verify ServerTestManager:diagnoseLevels() exists"]
            )

    @app.tool()
    def game_diagnose_multi_client_level_isolation(
        client_count: int = 2,
        server_timeout: int = 150,
        client_wait: int = 15,
    ) -> Dict[str, Any]:
        """启动多客户端并诊断Level隔离状态（仅连接，不进入游戏）

        流程：
        1. 启动 GameServer
        2. 启动指定数量客户端
        3. 仅连接服务器（不执行getReady等操作）
        4. 自动运行Level隔离诊断

        Args:
            client_count: 客户端数量（默认2）
            server_timeout: 等待服务端就绪超时（秒）
            client_wait: 启动客户端后等待时间（秒）

        Returns:
            {
                "success": bool,
                "message": str,
                "data": {
                    "level_count": int,
                    "levels": [{"id": int, "players": int, "available": bool}],
                    "is_isolated": bool,
                    "duration_seconds": float,
                }
            }
        """
        import time

        if client_count < 1 or client_count > 4:
            return _standardize_result(
                success=False,
                message=f"client_count must be between 1 and 4, got {client_count}",
                data={},
                recommendations=["Use client_count=2 for dual-level testing"]
            )

        start_time = time.time()
        pipe = SessionPipeline()

        # 1. 启动服务端
        pipe.add("start_server", lambda: steps._step_start_server(pipe))

        # 2. 等待服务端就绪
        pipe.add("wait_server_ready", lambda: steps._step_wait_server(pipe, timeout=server_timeout))

        # 3. 启动所有客户端
        for i in range(client_count):
            pipe.add(f"start_client_{i}", lambda idx=i: steps._step_start_client(pipe, client_wait=client_wait if idx == 0 else 5))

        # 4. 连接所有客户端的热更端口
        hotupdate_tasks = {f"hotupdate_client_{i}": lambda idx=i: steps._step_hotupdate_client(pipe) for i in range(client_count)}
        hotupdate_tasks["hotupdate_server"] = lambda: steps._step_hotupdate_server(pipe)
        pipe.add_parallel("connect_hotupdates", hotupdate_tasks)

        # 5. 每个客户端连接服务器（PVE模式下会自动分配到独立Level）
        for i in range(client_count):
            pipe.add(f"connect_client_{i}", lambda idx=i: steps._step_connect(pipe))

        # 6. 等待一段时间确保连接完成并Level分配完毕
        pipe.add("wait_for_level_assignment", lambda: (time.sleep(5), True)[1] or (True, "waited 5s for level assignment"))

        # 7. 运行Level隔离诊断
        def _run_diagnosis(pipe):
            print("  [Diagnosis] Running level isolation diagnosis...")
            script = steps._stm_call("diagnoseLevels")
            res = execute_lua_on("game_server", script, timeout=10.0)

            if not res.get("success"):
                return False, f"diagnoseLevels failed: {res.get('error', 'unknown error')}"

            output = (res.get("print") or "").strip()
            pipe.state["diagnosis_output"] = output
            print(f"  [Diagnosis] Output:\n{output[:500]}")
            return True, output

        pipe.add("diagnose_levels", lambda: _run_diagnosis(pipe))

        report = pipe.run(stop_on_fail=True)

        duration = time.time() - start_time
        success = report.get("success", False)

        if success:
            # 解析诊断结果
            import re
            output = pipe.state.get("diagnosis_output", "")

            level_count = 0
            count_match = re.search(r'total_levels=(\d+)', output)
            if count_match:
                level_count = int(count_match.group(1))

            levels = []
            level_pattern = r'level\[(\d+)\].*?players=(\d+).*?available=(\w+)'
            for match in re.finditer(level_pattern, output):
                level_id = int(match.group(1))
                players = int(match.group(2))
                available = match.group(3).lower() == "true"
                levels.append({
                    "id": level_id,
                    "players": players,
                    "available": available
                })

            # 检查每个Level的玩家详情
            player_details = []
            player_pattern = r'player\[(\d+)\].*?level=(\d+).*?name=([^\s]+)'
            for match in re.finditer(player_pattern, output):
                char_id = int(match.group(1))
                level_id = int(match.group(2))
                name = match.group(3)
                player_details.append({
                    "character_id": char_id,
                    "level_id": level_id,
                    "name": name
                })

            is_isolated = level_count >= client_count and all(l["players"] == 1 for l in levels)

            return _standardize_result(
                success=True,
                message=f"Diagnosis complete: {'Level ISOLATED' if is_isolated else 'Level NOT ISOLATED - PLAYERS IN SAME LEVEL!'} ({level_count} levels, {len(player_details)} players)",
                data={
                    "level_count": level_count,
                    "levels": levels,
                    "players": player_details,
                    "is_isolated": is_isolated,
                    "duration_seconds": round(duration, 2),
                    "raw_output": output,
                },
                recommendations=[] if is_isolated else [
                    "CRITICAL: Multiple clients are in the same Level!",
                    "Check if anonymous login mode is enabled",
                    "Verify session_manager.preTick() is only processing first available level",
                    "Verify character_manager assigns and marks level unavailable immediately",
                ]
            )
        else:
            failed_step = report.get("failed_step", "")
            return _standardize_result(
                success=False,
                message=f"Diagnosis pipeline failed at step: {failed_step}",
                data={
                    "failed_step": failed_step,
                    "duration_seconds": round(duration, 2),
                },
                recommendations=["Check GameServer logs", "Verify all components are properly configured"]
            )
