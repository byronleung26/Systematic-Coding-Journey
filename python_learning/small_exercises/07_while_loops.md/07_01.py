# 编写一个程序，询问用户要租什么样的汽车，并打印一条消息，如下所示。
#Let me see if I can find you a Subaru.
car = input("What car would you like to rent? ")
print(f"let me see if I can find you a {car}")
# 编写一个程序，询问用户有多少人用餐。如果超过 8 个人，就打印一条消息，指出没有空桌；否则指出有空桌。
people = input("请问有多少人用餐：")
if int(people) > 8:
    print("抱歉，没有空桌")
else:
    print("现在有空桌，您可以用餐")
# 让用户输入一个数，并指出这个数是否是 10 的整数倍。
number = input("请输入一个数：")
if int(number) % 10 == 0:
    print("这个数是10的整数倍")
else:
    print("这个数不是10的整数倍")