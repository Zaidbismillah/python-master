from datetime import time
data_time = time(hour=13, minute=14, second=31)
print("time:", data_time)
print(" ➜ hour:", data_time.hour)
print(" ➜ minute:", data_time.minute)
print(" ➜ second:", data_time.second)
print(" ➜ timezone:", data_time.tzinfo)
# output ↓
#
# time: 13:14:31
# ➜ hour: 13
# ➜ minute: 14
# ➜ second: 31
# ➜ timezone: None
