from datetime import datetime, timedelta

t1 = input("开始时间 (YYYY-MM-DD HH:MM:SS): ")
t2 = input("结束时间 (YYYY-MM-DD HH:MM:SS): ")

d1 = datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
d2 = datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")

delta = d2 - d1

print(f"时间间隔{delta}")