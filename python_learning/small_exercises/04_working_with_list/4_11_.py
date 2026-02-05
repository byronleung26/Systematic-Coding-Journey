# 创建水果列表的副本，并将其赋给变量friend_fruits，再完成如下任务
like_fruits = ["grape","banana","orange","apple"]
friend_fruits = like_fruits[:]
# 在原来的比萨列表中添加一种水果
like_fruits.append("pear")
# 在列表 friend_fruits 中添加另一种水果
friend_fruits.append("lemon")
# 核实有两个不同的列表,打印消息“My/friend's favorite fruits are:”，再使用一个for循环来打印列表
print("My favorite fruits are:")
for fruit in like_fruits:
    print(fruit)
print("Friend's favorite fruits are:")
for fruit in friend_fruits:
    print(fruit)