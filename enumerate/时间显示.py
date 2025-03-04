n = int(input())
n = n // 1000  # 关键修正1：毫秒转秒
n %= 86400     # 关键修正2：取余一天的秒数（24*3600）

hour = n // 3600
minute = (n % 3600) // 60
second = n % 60

print(f"{hour:02d}:{minute:02d}:{second:02d}")