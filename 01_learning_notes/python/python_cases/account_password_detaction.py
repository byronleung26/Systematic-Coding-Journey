# 编写程序,模拟登录系统的账号密码检测功能,并限制账号或密码的错误次数至多3次。
# 改进计划：减少重复、函数封装、安全增强、界面美化
user_data = {'leung':'123456789', 'liang':'987654321'}
times = 0
while times < 3:
    account = input("请输入账号").strip()
    password = input("请输入密码").strip()
    if account in user_data:
        if password == user_data[account]:
            print("登录成功")
            break
        else:
            times += 1
            if times == 3:
                print("错误次数过多，请稍后再试")
            else:
                print(f"账号或密码错误,您还有{3-times}次机会")
            
    else:
        times += 1
        if times == 3:
            print("错误次数过多，请稍后再试")
        else:
            print(f"该用户不存在,您还有{3-times}次机会")
        