"""多关卡 PVE MCP 服务端

专注于多Level并行运行的MCP服务器，提供Session管理和热更新功能。
"""

import sys
from pathlib import Path
from mcp.server.fastmcp import FastMCP

# 路径：MCP 仓库根目录 + src/ 目录
_mcp_root = Path(__file__).resolve().parent.parent
_game_dev_dir = Path(__file__).resolve().parent
for p in (_mcp_root, _game_dev_dir):
    s = str(p)
    if s not in sys.path:
        sys.path.insert(0, s)

# 导入工具注册函数（仅保留核心多关卡功能）
try:
    from src.core.process.tools import register_server_tools
    from src.core.hotupdate.tools import register_hotupdate_tools
    from src.core.session.tools import register_game_session_tools
except ImportError as e:
    print(f"Import error: {e}")
    raise

# 创建 MCP 应用
app = FastMCP("multi_level_pve_mcp")

# 注册核心工具
register_server_tools(app)      # 基础进程管理
register_hotupdate_tools(app)   # 热更新工具
register_game_session_tools(app)  # 游戏会话工具（多关卡核心）

# Echo工具（用于测试连接）
@app.tool()
def echo(message: str) -> dict:
    """Echo back the input message. Useful for testing MCP connectivity."""
    return {"result": message}

def run() -> None:
    """Run the MCP server"""
    app.run(transport="stdio")

if __name__ == "__main__":
    run()
