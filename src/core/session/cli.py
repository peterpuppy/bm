import os
import sys
import cmd
import time

from src.base.pipeline import SessionPipeline
from src.core.session import steps
from src.core.hotupdate.client import execute_lua_on
from src.core.process.tools import _process_manager

def stop_all():
    for name in list(_process_manager.processes.keys()):
        _process_manager.stop_process(name)

class GameSessionCLI(cmd.Cmd):
    intro = '''
====================================================
  Chaos Game Session Interactive CLI
====================================================
Type 'help' or '?' to list commands.

Individual Steps:
  start_server       - Start GS process
  wait_server        - Wait for GS to be ready
  hotupdate_server   - Hotupdate GS
  start_client       - Start Client process
  hotupdate_client   - Hotupdate Client
  connect            - Connects client to server
  ready              - Clicks 'Ready' in Prewar
  wait_start         - Waits for game_status=start
  status             - Queries current state anytime
  levels             - Queries server for all active levels and their occupancy
  combat_state       - Queries combat state (legions, alive counts)
  spawn_enemy        - Spawns enemies on the server (Usage: spawn_enemy [count] [distance] [level_id])
  disconnect         - Disconnects a specific client (Usage: disconnect [N])

Flows (Combined Steps):
  flow_server_infra  - start_server -> wait_server -> hotupdate_server
  flow_client_infra  - start_client -> wait 10s -> hotupdate_client
  flow_full_start    - Runs the entire startup pipeline (Single Client)
====================================================
'''
    prompt = '(chaos-cli) '

    def __init__(self):
        super().__init__()
        self.pipe = SessionPipeline()
        self.pipe.name = "InteractiveSession"

    def _check_hotupdate(self, target: str) -> bool:
        """Check if hotupdate is connected for the target ('client' or 'game_server')."""
        if target == "client" and not self.pipe.state.get("client_hotupdate"):
            print("[WARNING] 客户端热更未连接，请先执行 hotupdate_client")
            return False
        if target == "game_server" and not self.pipe.state.get("server_hotupdate"):
            print("[WARNING] 服务端热更未连接，请先执行 hotupdate_server")
            return False
        return True

    def _run_step(self, name, func, *args, **kwargs):
        print(f"\n---> Running: {name} ...")
        try:
            res = func(self.pipe, *args, **kwargs)
            if isinstance(res, tuple) and len(res) == 2:
                success, msg = res
                if success:
                    print(f"[OK] {msg}")
                else:
                    print(f"[ERROR] {msg}")
            else:
                print(f"[OK] {res}")
        except Exception as e:
            print(f"[EXCEPTION] {e}")

    def do_start_server(self, arg):
        """Start the game server process."""
        self._run_step("Start Server", steps._step_start_server)

    def do_wait_server(self, arg):
        """Wait for the game server to be ready."""
        self._run_step("Wait Server Ready", steps._step_wait_server, timeout=150)

    def do_hotupdate_server(self, arg):
        """Connect hotupdate to the game server."""
        self._run_step("Hotupdate Server", steps._step_hotupdate_server)

    def do_start_client(self, arg):
        """Start the game client process."""
        self._run_step("Start Client", steps._step_start_client)

    def do_hotupdate_client(self, arg):
        """Connect hotupdate to the game client."""
        self._run_step("Hotupdate Client", steps._step_hotupdate_client)

    def do_connect(self, arg):
        """Connect the client to the server."""
        if not self._check_hotupdate("client"): return
        self._run_step("Connect to Server", steps._step_connect)

    def do_ready(self, arg):
        """Click the Ready button in Prewar."""
        if not self._check_hotupdate("client"): return
        self._run_step("Send getReady", steps._step_prewar_ready)

    def do_wait_start(self, arg):
        """Wait for the game to start (polls status)."""
        if not self._check_hotupdate("client"): return
        self._run_step("Wait Game Start", steps._step_wait_game_start, max_attempts=150)

    def do_status(self, arg):
        """Query current state. Usage: status [all|client_N|server]"""
        target = arg.strip() or "client"
        
        if target == "all":
            print("\n---> Querying All Clients State...")
            from src.core.session.state import get_multi_client_manager
            mcm = get_multi_client_manager()
            res = mcm.query_all()
            for k, v in res.items():
                print(f"[{k}] {v}")
            return

        if target == "server":
            if not self._check_hotupdate("game_server"): return
            print("\n---> Querying Server State...")
            r = execute_lua_on("game_server", steps._stm_call("queryState"), timeout=5.0)
        else:
            # Assume it's a client endpoint
            print(f"\n---> Querying {target} State...")
            r = execute_lua_on(target, steps._tm_call("queryState"), timeout=5.0)
            
        out = r.get("print") or r.get("error") or "No output"
        print(out.strip())

    def do_disconnect(self, arg):
        """Disconnect and kill a specific client. Usage: disconnect <client_index>"""
        if not arg.strip():
            print("[ERROR] Please provide a client index (e.g., 'disconnect 1')")
            return
            
        try:
            client_index = int(arg.strip())
        except ValueError:
            print("[ERROR] Client index must be an integer.")
            return
            
        print(f"\n---> Disconnecting client_{client_index} ...")
        from src.core.session.state import get_multi_client_manager
        mcm = get_multi_client_manager()
        slot = mcm.slots.get(client_index)
        if not slot:
            print(f"[ERROR] client_{client_index} not found in manager.")
            return
            
        mcm.disconnect_client(client_index)
        if slot.pid:
            try:
                import psutil
                proc = psutil.Process(slot.pid)
                proc.kill()
                print(f"[OK] Killed process {slot.pid}")
            except Exception as e:
                print(f"[WARNING] Failed to kill process {slot.pid}: {e}")
            slot.pid = None
        print(f"[OK] client_{client_index} disconnected.")

    def do_combat_setup(self, arg):
        """Setup combat (transfer authority, disable anti-cheat)."""
        if not self._check_hotupdate("game_server"): return
        self._run_step("Transfer Authority", steps._step_transfer_auth)
        self._run_step("Disable Anti-Cheat", steps._step_disable_anticheat)

    def do_combat_state(self, arg):
        """Query combat state (legions, alive counts). Usage: combat_state [server|client_N|all]"""
        target = arg.strip() or "all"
        
        def _query_server():
            if not self._check_hotupdate("game_server"): return
            print("\n---> [Server] Querying Combat State...")
            r = execute_lua_on("game_server", steps._stm_call("queryCombatState"), timeout=5.0)
            print(r.get("print") or r.get("error") or "No output")

        def _query_client(ep):
            if not self._check_hotupdate(ep): return
            print(f"\n---> [{ep}] Querying Combat State...")
            r = execute_lua_on(ep, steps._tm_call("queryCombatState"), timeout=5.0)
            print(r.get("print") or r.get("error") or "No output")

        if target == "all":
            _query_server()
            from src.core.session.state import get_multi_client_manager
            mcm = get_multi_client_manager()
            for idx in sorted(mcm.slots):
                _query_client(f"client_{idx}")
        elif target == "server":
            _query_server()
        else:
            _query_client(target)

    def do_levels(self, arg):
        """Query server for all active levels and their occupancy."""
        if not self._check_hotupdate("game_server"): return
        print("\n---> [Server] Querying Levels...")
        r = execute_lua_on("game_server", steps._stm_call("diagnoseLevels"), timeout=5.0)
        print(r.get("print") or r.get("error") or "No output")

    def do_spawn_enemy(self, arg):
        """Spawn enemies on the server. Usage: spawn_enemy [count] [distance] [level_id]"""
        if not self._check_hotupdate("game_server"): return
        
        args = arg.split()
        count = int(args[0]) if len(args) > 0 else 20
        distance = float(args[1]) if len(args) > 1 else 15.0
        level_id = int(args[2]) if len(args) > 2 else -1
        
        print(f"\n---> [Server] Spawning {count} enemies at distance {distance} in level {level_id}...")
        script = f"local r = ServerTestManager:spawnEnemyLegion(2101110125, {distance}, {count}, {level_id}); print(r)"
        r = execute_lua_on("game_server", script, timeout=10.0)
        print(r.get("print") or r.get("error") or "No output")

    def do_flow_server_infra(self, arg):
        """Flow: Start server, wait ready, and hotupdate."""
        self.do_start_server(arg)
        self.do_wait_server(arg)
        self.do_hotupdate_server(arg)

    def do_flow_client_infra(self, arg):
        """Flow: Start client, wait 10s, and hotupdate."""
        self.do_start_client(arg)
        print("---> Waiting 10s for client to initialize...")
        time.sleep(10)
        self.do_hotupdate_client(arg)

    def do_flow_full_start(self, arg):
        """Flow: Execute the entire startup pipeline using parallel execution (Single Client)."""
        print("\n---> Running: Full Start Flow (Parallel) ...")
        
        from src.core.session.tools import run_game_start_pve_session
        
        res = run_game_start_pve_session()
        if res.get("result", {}).get("success"):
            print("[OK] Full start flow completed successfully.")
            self.pipe.state.update(res.get("result", {}).get("state", {}))
        else:
            print("[FAIL] Full start flow failed.")
            for step in res.get("result", {}).get("steps", []):
                if step.get("status") == "fail":
                    print(f"  Failed at step: {step.get('name')} - {step.get('detail')}")

    def do_stop_all(self, arg):
        """Stop all running servers and clients."""
        print("\n---> Stopping all services...")
        stop_all()
        print("[OK] Stopped.")

    def do_quit(self, arg):
        """Exit the CLI."""
        print("Exiting...")
        return True

    def do_exit(self, arg):
        """Exit the CLI."""
        return self.do_quit(arg)
