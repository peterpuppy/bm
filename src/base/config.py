"""Configuration management for MCP Game Dev"""
from typing import Any, Dict
from pathlib import Path
import json

def load_raw_config() -> Dict[str, Any]:
    """加载主配置文件 config.json"""
    config_file = Path(__file__).parent.parent.parent / "config.json"
    with open(config_file, encoding='utf-8') as f:
        return json.load(f)

def save_raw_config(config: Dict[str, Any]) -> None:
    """保存主配置文件 config.json"""
    config_file = Path(__file__).parent.parent.parent / "config.json"
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

def get_active_config() -> Dict[str, Any]:
    """获取当前配置（含变量替换）"""
    raw_config = load_raw_config()

    roots = raw_config.get("roots", {})
    paths = raw_config.get("paths", {})
    services = raw_config.get("services", {})
    targets = raw_config.get("targets", {})
    
    # 构建变量替换字典
    subs = {}
    subs.update({k: v for k, v in roots.items() if not k.startswith("_")})
    
    def substitute(obj):
        """递归替换 {变量名} 占位符"""
        if isinstance(obj, str):
            result = obj
            for _ in range(5):  # 多次迭代处理嵌套变量
                changed = False
                for key, value in subs.items():
                    placeholder = f"{{{key}}}"
                    if placeholder in result:
                        result = result.replace(placeholder, str(value))
                        changed = True
                if not changed:
                    break
            return result
        elif isinstance(obj, dict):
            return {k: substitute(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [substitute(item) for item in obj]
        return obj

    # 替换路径，并将解析后的路径加入 subs 供后续使用
    resolved_paths = substitute(paths)
    subs.update({k: v for k, v in resolved_paths.items() if not k.startswith("_")})
    
    # 替换服务、目标中的变量
    resolved_services = substitute(services)
    resolved_targets = substitute(targets)
    
    return {
        "roots": roots,
        "paths": resolved_paths,
        "services": resolved_services,
        "targets": resolved_targets
    }

def get_service_config(service_name: str) -> Dict[str, Any]:
    """获取指定服务的配置"""
    config = get_active_config()
    services = config.get("services", {})
    if service_name not in services:
        raise ValueError(f"Service '{service_name}' not found in config")
    return services[service_name]

def get_service_log_dir(service_name: str) -> str:
    """获取指定服务的日志目录"""
    config = get_service_config(service_name)
    log_dir = config.get("log_dir")
    if not log_dir:
        raise ValueError(f"Service '{service_name}' has no log_dir configured")
    return log_dir

def load_config() -> Dict[str, Any]:
    """向后兼容的别名"""
    return get_active_config()
