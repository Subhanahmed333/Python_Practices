import time

t = time.localtime()
fmt_time = time.strftime("%Y-%m-%d %H:%M:%S", t) # format time
if fmt_time > "2025-03-21 05:00:00" and fmt_time < "2025-03-21 12:00:00":
    print("Good Morning")
elif fmt_time > "2025-03-21 13:00:00" and fmt_time < "2025-03-21 20:00:00":
    print("Good Afternoon")
else:
    print("Good Night")
print(fmt_time)
