import requests
from base64 import b64encode


def get_flag():
    url = "http://202.120.222.171:30135/"
    auth = b64encode(b"time_traveler").decode()

    response = requests.request(
        method="MECHANISM",
        url=url,
        headers={
            "Authorization": f"Basic {auth}",
            "User-Agent": "LeMMIH/0.1 (Chronos Protocol)",
            "X-Protocol-Era": "HTTP/1.0"
        }
    )

    if response.status_code == 200:
        cipher = response.text.split(": ")[-1].strip()  # 示例：a2Bk3S__D3V1c3R
        return decode_flag(cipher)
    return "访问失败"


def decode_flag(cipher: str) -> str:
    # ROT13解码
    decoded = cipher.encode('rot13').decode()

    # 转换规则：数字转字母（3->C，1->A，2->B）
    mapping = {'3': 'C', '1': 'A', '2': 'B'}
    flag = ''.join(mapping.get(c, c) for c in decoded).lower()

    return f"slctf{{{flag}}}"


print(get_flag())