spending = float(input("请输入消费总额："))
points = float(input("请输入积分："))
if spending >= 1000 and points >= 1000:
    print("钻石会员")
elif 500 <= spending < 1000 and 5000 <= points < 10000:
    print("白金会员")
elif 200 <= spending < 500 and 2000 <= points < 5000:
    print("黄金会员")
elif 100 <= spending < 200 and 1000 <= points < 2000:
    print("白银会员")
elif 50 <= spending < 100 and 500 <= points < 1000:
    print("青铜会员")
elif spending < 50 and points < 500:
    print("普通会员")
else:
    print("不是会员")