# 有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；
# 3（含）～12岁的观众收费10美元；年满12岁的观众收费 15 美元。
# 请编写一个循环，在其中询问用户的年龄，并指出其票价。
while True:
    age = int(input("请输入年龄："))
    if age > 0 and age < 3:
        print("票价：免费")
    elif age >= 3 and age < 12:
        print("票价：10美元")
    elif age >= 12 and age < 150:
        print("票价：15美元")
    else:
        print("请正确输入年龄")