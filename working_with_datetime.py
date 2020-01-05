from datetime import datetime, timedelta
import time

print(datetime(2019, 12, 2))
print(datetime.now())
print(datetime.fromtimestamp(time.time()))
dt = datetime.now()
print(dt.strftime("%Y/%m/%d"))

dt1 = datetime(2011, 11, 11)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print(duration.days)
print(duration.seconds)

dt2 += timedelta(days=1, seconds=10000)
duration = dt2 - dt1
print(duration)
print(duration.days)
print(duration.seconds)
