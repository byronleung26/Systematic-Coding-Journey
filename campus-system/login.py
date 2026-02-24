# 用户登录模块

def login():
    """用户登录"""
    import json
    user_data = {}
    with open("user.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                username, password = line.split(":")
                user_data[username] = password
    times = 0
    while True:
        username = input("输入用户名：")
        password = input("输入密码：")
        if username in user_data and password == user_data[username]:
            print("登录成功")
            break
        else:
            times += 1
            if times < 3:
                print(f"账号或密码错误,您还有{3-times}次机会")
            else:
                print("错误次数过多，请稍后再试")
                break
