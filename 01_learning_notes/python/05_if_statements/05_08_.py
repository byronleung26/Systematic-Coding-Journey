# 创建一个至少包含 5 个用户名的列表，并且其中一个用户名为'admin'。
# 想象你要编写代码，在每个用户登录网站后都打印一条问候消息。
# 遍历用户名列表，向每个用户打印一条问候消息
# 如果用户名为 'admin'，就打印一条特殊的问候消息:Hello admin, would you like to see a status report?
# 否则，打印一条普通的问候消息:Hello Jaden, thank you for logging in again
username = ["admin","zhang","liang","zhao","dong"]
for user in username:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")