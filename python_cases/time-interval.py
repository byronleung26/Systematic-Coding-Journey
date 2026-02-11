# 输入第1个时间点
time1 = input("请输入开始时间点:_年_月_日_时_分_秒(输入一项后用1个空格分割输入下一项)").split()
year1 = int(time1[0])
month1 = int(time1[1])
day1 = int(time1[2])
hour1 = int(time1[3])
minute1 = int(time1[4])
second1 = int(time1[5])

# 输入第2个时间点
time2 = input("请输入结束时间点:_年_月_日_时_分_秒(输入一项后用1个空格分割输入下一项)").split()
year2 = int(time2[0])
month2 = int(time2[1])
day2 = int(time2[2])
hour2 = int(time2[3])
minute2 = int(time2[4])
second2 = int(time2[5])

def days_in_month(year,month):
    """判断每月多少天"""
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            return 29
        else:
            return 28
    else:
        print("月份输入错误，请正确输入")

def to_second(year,month,day,hour,minute,second):
    """计算时间点距1年1月1日0时0分0秒的距离"""
    total_days = 0
    for y in range(1,year):  # 计算year-1年的天数
        if y % 400 == 0 or y %4 == 0 and y % 100 != 0:
            total_days += 366  # 闰年366天
        else:
            total_days += 365  # 平年365天
    for m in range(1,month):  # 再加上month-1月的天数
        total_days += days_in_month(year, m)  # 调用判断每月天数的函数
    total_days += (day-1)  # 再加上当月天数
    total_second = total_days * 24 * 60 * 60  # 整天数转化为秒
    total_second += (hour-1) * 60 * 60  # 再加上当天整小时转化为秒
    total_second += (minute-1) * 60  # 再加上该小时整分钟转化为秒
    total_second += second  # 再加上该时间点的秒
    return total_second

total_second1 = to_second(year1, month1, day1, hour1, minute1, second1)  # 时间1距纪年开始
total_second2 = to_second(year2, month2, day2, hour2, minute2, second2)  # 时间2距纪年开始

duration_sec = total_second2 - total_second1  # 计算间隔的秒
sec = duration_sec % 60  # 最终的秒
duration_minute = duration_sec // 60  # 计算间隔的分钟
min = duration_minute % 60  # 最终的分钟
duration_hour = duration_minute // 60  # 计算间隔的小时
hou = duration_hour % 24 # 最终的小时
duration_day = duration_hour // 24  # 计算间隔的天数
print(f"""
2个时间间距:
{duration_sec}秒,
{duration_minute}分钟{sec}秒,
{duration_hour}小时{min}{sec}
{duration_day}天{hou}小时{min}分钟{sec}秒
""")