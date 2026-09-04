#!/usr/bin/env python3
"""PS5 S2S 登录独立测试：复刻 GAC 的 PS5 登录逻辑。

用途：脱离游戏登录服，验证 DevKit 拿到的 authorization code 能否换出 account_id。
PSN S2S 流程：POST /v3/oauth/token 换 token（响应含 id_token JWT）→ 解 id_token 的 sub claim = account_id。
（PSN S2S 没有 userinfo 端点；account_id 来自 id_token。）

用法：
    python ps5_s2s_test.py "1|<authorization_code>"        # issuer|code 拼接（与 Lua password 一致）
    python ps5_s2s_test.py <authorization_code> --issuer 1  # 或分开传
    PS5_CLIENT_ID=xxx PS5_CLIENT_SECRET=yyy python ps5_s2s_test.py "1|<code>"

注意：
  - authorization code 一次性、有效期短——每次测试都要在 DevKit 重新获取。
  - 运行机器的公网 IP 必须已加入 DevNet Application Server 的 S2S IP allowlist，否则 Akamai 403。
"""
import argparse
import base64
import json
import os
import sys

import requests

# 研发默认值（与 game_account_center 的 login.conf [ps5] 一致）。secret 已知泄漏，仅研发用，勿扩散。
CLIENT_ID = os.environ.get("PS5_CLIENT_ID", "62828b87-3b8b-4e9a-9756-1a913e7cf977")
CLIENT_SECRET = os.environ.get("PS5_CLIENT_SECRET", "DtCLkkWViqmORho9")
REDIRECT_URI = "orbis://games"
SCOPE = "psn:s2s openid id_token:psn.basic_claims"

BASE_URL_BY_ISSUER = {
    1: "https://s2s.sp-int.playstation.net/api/authz",
    8: "https://s2s.prod-qa.playstation.net/api/authz",
    256: "https://s2s.np.playstation.net/api/authz",
}


def decode_id_token(id_token):
    """解 JWT payload（base64url，无 padding），返回 claims dict。只解码不验签。"""
    parts = id_token.split(".")
    if len(parts) < 2:
        raise ValueError("invalid id_token format")
    payload = parts[1]
    payload += "=" * (-len(payload) % 4)  # 补 padding
    return json.loads(base64.urlsafe_b64decode(payload))


def main() -> int:
    ap = argparse.ArgumentParser(description="PS5 S2S 登录独立测试")
    ap.add_argument("code", help='authorization code，或 "issuer_id|code" 拼接形式')
    ap.add_argument("--issuer", type=int, default=None, help="issuer_id（若 code 里没拼则必填）")
    args = ap.parse_args()

    if "|" in args.code:
        issuer_str, _, auth_code = args.code.partition("|")
        issuer_id = int(issuer_str)
    else:
        auth_code = args.code
        if args.issuer is None:
            ap.error("code 里没有 issuer 前缀时，必须用 --issuer 指定")
        issuer_id = args.issuer

    base_url = BASE_URL_BY_ISSUER.get(issuer_id)
    if base_url is None:
        print(f"[ERR] 不支持的 issuer_id: {issuer_id}（应为 1/8/256）")
        return 2

    print(f"[*] issuer_id={issuer_id}  base_url={base_url}")
    print(f"[*] auth_code(len={len(auth_code)})={auth_code}")

    # POST /v3/oauth/token —— 换 access_token + id_token
    token_url = base_url + "/v3/oauth/token"
    basic = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    r = requests.post(
        token_url,
        headers={
            "Authorization": "Basic " + basic,
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "authorization_code",
            "code": auth_code,
            "redirect_uri": REDIRECT_URI,
            "scope": SCOPE,
        },
        timeout=15,
    )
    print(f"\n[token] POST {token_url}\n    status={r.status_code}\n    body={r.text}")
    if r.status_code != 200:
        print("[ERR] token 交换失败，停止。")
        return 1

    id_token = r.json().get("id_token")
    if not id_token:
        print("[ERR] 响应里没有 id_token，停止。")
        return 1

    claims = decode_id_token(id_token)
    account_id = claims.get("sub")
    online_id = claims.get("online_id")
    print(f"\n[id_token claims] {json.dumps(claims, ensure_ascii=False)}")
    print(f"\n[✓] 走通！account_id(sub)={account_id}  online_id={online_id}")
    print("    -> GAC 会用这个 account_id 作为 UserName，缓存 (account_id,'ps5')->token，供登录服验证。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
