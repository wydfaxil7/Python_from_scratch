######## TIME MODULE ########

import time

print(time.time())

print("Start: ", time.time())
time.sleep(5)
print("End: ", time.time())


t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)
# Output: 2022-11-08 08:45:33