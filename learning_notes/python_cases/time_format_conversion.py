while True:
    time_list = input("按“年-月-日-时-分-秒”输入时间").split('-')
    if len(time_list) != 6:
        print("时间格式输入错误，请按如“2025-11-16-14-24-32”的格式重新输入")
    else:
        year = time_list[0].strip()
        month = time_list[1].strip()
        day = time_list[2].strip()
        hour = time_list[3].strip()
        minute = time_list[4].strip()
        second = time_list[5].strip()
        break
while True:
    country = input("请输入选择国家（输入数字1-5选择）："
                        "1.中国；"
                        "2.美国；"
                        "3.英国、澳大利亚、法国；"
                        "4.德国、俄罗斯；"
                        "5.加拿大")
    if country not in ['1', '2', '3', '4', '5']:
        print("国家选择错误，请在1-5中重新选择一个数字输入")
    else:
        if country == '1':
            print(f"{year}年{month}月{day}日 {hour}:{minute}:{second}")
        elif country == '2':
            print(f"{month}/{day}/{year} {hour}:{minute}:{second}")
        elif country == '3':
            print(f"{day}/{month}/{year} {hour}:{minute}:{second}")
        elif country == '4':
            print(f"{day}.{month}.{year} {hour}:{minute}:{second}")
        elif country == '5':
            print(f"{year}-{month}-{day} {hour}:{minute}:{second}")
        break