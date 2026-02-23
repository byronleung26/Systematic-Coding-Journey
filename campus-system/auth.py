# 用户认证模块
def register():
    """用户注册"""
    user_data = {}
    with open("user.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                username, password = line.split(":")
                user_data[username] = password
    while True:
        username = input("输入用户名：").strip()
        if username in user_data:
            print("用户名已被占用，请重新输入")
            continue
        elif not username:
            print("用户名不能为空，请重新输入")
            continue
        break
    while True:
        password = input("输入密码：").strip()
        if len(password) <= 6:
            print("密码应该为6位以上")
            continue
        else:
            print("注册成功")
            break
    with open("user.txt", "w") as f:
        f.write(f"{username}:{password}\n")

def login():
    """用户登录"""
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
        
login()
