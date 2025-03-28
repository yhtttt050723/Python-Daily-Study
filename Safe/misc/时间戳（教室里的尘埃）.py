from datetime import datetime

# 将指定时间转换为 Unix 时间戳
custom_time = datetime(2025, 2, 24, 7, 30,26)
custom_timestamp = int(custom_time.timestamp())
print("自定义时间的 Unix 时间戳:", custom_timestamp)

from datetime import datetime
import pytz

# 明确指定为 UTC 时区
custom_time = datetime(2025, 2, 24, 7, 30, 26, tzinfo=pytz.UTC)
timestamp = int(custom_time.timestamp())
print(timestamp)