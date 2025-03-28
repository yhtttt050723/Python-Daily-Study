import requests
import random

def generate_random_ip():
    """生成一个随机的IP地址"""
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def send_request(url, x_forwarded_for):
    """发送带有指定X-Forwarded-For头的HTTP GET请求"""
    headers = {'X-Forwarded-For': x_forwarded_for}
    response = requests.get(url, headers=headers)
    return response

url = "http://202.120.222.171:32277/invitation/03a0271aee705bcc4d1bd9e54c0b037c"  # 替换为你要请求的实际URL
for i in range(100):  # 循环100次
    x_forwarded_for = generate_random_ip()  # 随机生成X-Forwarded-For头部的值
    response = send_request(url, x_forwarded_for)  # 发送请求
    print(f"Request {i+1}: X-Forwarded-For={x_forwarded_for}, Status Code={response.status_code}, Response Body={response.text[:500]}")  # 打印响应状态码和响应体（前100个字符）