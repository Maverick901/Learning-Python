from datetime import datetime
import time

print(datetime(2019, 12, 2))
print(datetime.now())
print(datetime.fromtimestamp(time.time()))
dt = datetime.now()
print(dt.strftime("%Y/%m/%d"))
