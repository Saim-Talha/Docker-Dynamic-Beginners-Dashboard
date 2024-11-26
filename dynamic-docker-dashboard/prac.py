import psutil
import datetime

boot_time = psutil.boot_time()
uptime = datetime.datetime.fromtimestamp(boot_time)

print(boot_time)