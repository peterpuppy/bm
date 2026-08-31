"""通用步骤编排框架

提供 SessionStep + SessionPipeline，用于将多步骤流程组织为
顺序执行的 pipeline，并输出结构化报告。
"""
import time
from typing import Any, Callable, Dict, List
import concurrent.futures


class SessionStep:
    """Pipeline 中的一个步骤"""
    __slots__ = ("name", "action", "status", "detail", "elapsed_s")

    def __init__(self, name: str, action: Callable):
        self.name = name
        self.action = action
        self.status: str = "pending"      # pending / running / ok / warn / fail
        self.detail: str = ""
        self.elapsed_s: float = 0.0

    def run(self) -> bool:
        self.status = "running"
        t0 = time.time()
        try:
            ok, detail = self.action()
            self.elapsed_s = round(time.time() - t0, 1)
            self.status = "ok" if ok else "fail"
            self.detail = detail
            return ok
        except Exception as exc:
            self.elapsed_s = round(time.time() - t0, 1)
            self.status = "fail"
            self.detail = str(exc)
            return False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "status": self.status,
            "detail": self.detail,
            "elapsed_s": self.elapsed_s,
        }


class ParallelStep(SessionStep):
    """并行执行多个步骤"""
    def __init__(self, name: str, actions: Dict[str, Callable]):
        super().__init__(name, lambda: (True, "parallel container"))
        self.sub_steps = [SessionStep(k, v) for k, v in actions.items()]
        
    def run(self) -> bool:
        self.status = "running"
        t0 = time.time()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.sub_steps)) as executor:
            futures = {executor.submit(step.run): step for step in self.sub_steps}
            concurrent.futures.wait(futures.keys())
            
        self.elapsed_s = round(time.time() - t0, 1)
        
        all_ok = all(step.status == "ok" for step in self.sub_steps)
        self.status = "ok" if all_ok else "fail"
        
        failed_steps = [step.name for step in self.sub_steps if step.status != "ok"]
        if failed_steps:
            self.detail = f"Failed sub-steps: {', '.join(failed_steps)}"
        else:
            self.detail = "All parallel steps succeeded"
            
        return all_ok
        
    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d["sub_steps"] = [step.to_dict() for step in self.sub_steps]
        return d


class SessionPipeline:
    """按顺序执行 SessionStep，收集结构化报告"""

    def __init__(self):
        self.steps: List[SessionStep] = []
        self.state: Dict[str, Any] = {}

    def add(self, name: str, action: Callable) -> "SessionPipeline":
        self.steps.append(SessionStep(name, action))
        return self
        
    def add_parallel(self, name: str, actions: Dict[str, Callable]) -> "SessionPipeline":
        self.steps.append(ParallelStep(name, actions))
        return self

    def run(self, stop_on_fail: bool = True) -> Dict[str, Any]:
        t0 = time.time()
        for step in self.steps:
            ok = step.run()
            if not ok and stop_on_fail:
                break
        total = round(time.time() - t0, 1)
        all_ok = all(s.status == "ok" for s in self.steps if s.status != "pending")
        return {
            "success": all_ok,
            "total_elapsed_s": total,
            "steps": [s.to_dict() for s in self.steps],
            "state": self.state,
        }
