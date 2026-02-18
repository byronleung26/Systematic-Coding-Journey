import datetime

t1 = input("开始时间 (YYYY-MM-DD HH:MM:SS): ")
t2 = input("结束时间 (YYYY-MM-DD HH:MM:SS): ")

d1 = datetime.datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
d2 = datetime.datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")

delta = d2 - d1

print(f"间隔: {delta.days}天 {delta.seconds//3600}小时 "
      f"{(delta.seconds%3600)//60}分钟 {delta.seconds%60}秒")