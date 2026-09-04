#!/usr/bin/env python3
"""PS5 S2S 边缘可达性稳定性探测。

token + userinfo 端点各跑 N 次，统计"穿过 Akamai 边缘(拿到 PSN 应答)"vs"被 403 挡"，
并记录每次的默认出口 IP，用来验证在负载均衡出口池下 S2S 白名单是否稳定生效。

用法: python ps5_edge_probe.py [N]     # N 默认 10
说明:
  PASS       = 请求穿过了 Akamai 边缘（拿到 PSN 的 JSON 应答，如 invalid_grant）→ 源 IP 被放行
  EDGE_BLOCK = 被 Akamai 返回 403 "Access Denied" → 源 IP 不在白名单
  用假 code / 假 token，只看边缘放不放行，不关心业务是否成功。
"""
import os
import sys
import base64

import requests

CLIENT_ID = os.environ.get("PS5_CLIENT_ID", "62828b87-3b8b-4e9a-9756-1a913e7cf977")
CLIENT_SECRET = os.environ.get("PS5_CLIENT_SECRET", "DtCLkkWViqmORho9")
BASE = "https://s2s.sp-int.playstation.net/api/authz"
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10


def egress_ip():
    try:
        return requests.get("https://api.ipify.org", timeout=8).text.strip()
    except Exception:
        return "?"


def classify(resp):
    if resp.status_code == 403 and "Access Denied" in resp.text:
        return "EDGE_BLOCK"
    return "PASS"


def probe_token():
    basic = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    return requests.post(
        BASE + "/v3/oauth/token",
        headers={
            "Authorization": "Basic " + basic,
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "authorization_code",
            "code": "X",
            "redirect_uri": "orbis://games",
            "scope": "psn:s2s openid id_token:psn.basic_claims",
        },
        timeout=20,
    )


def probe_userinfo():
    return requests.get(
        BASE + "/v3/oauth/userinfo",
        headers={"Authorization": "Bearer FAKE"},
        timeout=20,
    )


def run(name, fn):
    print(f"\n=== {name}  x{N} ===")
    stats = {"PASS": 0, "EDGE_BLOCK": 0, "ERR": 0}
    ips = {}
    for i in range(1, N + 1):
        ip = egress_ip()
        ips[ip] = ips.get(ip, 0) + 1
        try:
            r = fn()
            c = classify(r)
            stats[c] += 1
            print(f"  #{i:2d} egress={ip:16s} http={r.status_code} -> {c}")
        except Exception as e:
            stats["ERR"] += 1
            print(f"  #{i:2d} egress={ip:16s} ERROR: {e}")
    print(f"  汇总: PASS={stats['PASS']} EDGE_BLOCK={stats['EDGE_BLOCK']} ERR={stats['ERR']}")
    print(f"  出口IP分布: {ips}")
    return stats


if __name__ == "__main__":
    print(f"探测 {N} 次/接口。PASS=穿过边缘, EDGE_BLOCK=被Akamai 403挡")
    print("(注：出口IP列是 ipify 单独连接的出口，与 PSN 请求的实际出口不一定一致，仅供观察池是否在飘)")
    t = run("token", probe_token)
    u = run("userinfo", probe_userinfo)
    total = sum(t[k] + u[k] for k in ("PASS", "EDGE_BLOCK"))
    passed = t["PASS"] + u["PASS"]
    print("\n===== 总计 =====")
    print(f"穿过边缘: {passed}/{total} (token PASS {t['PASS']}/{N}, userinfo PASS {u['PASS']}/{N})")
    if t["EDGE_BLOCK"] or u["EDGE_BLOCK"]:
        print("⚠️  有请求被 403 挡 → 出口池未全部白名单，真跑登录会时通时断。")
    else:
        print("✅ 全部穿过边缘 → 白名单稳定生效，可以放心跑登录。")
