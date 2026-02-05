'''like_fruits = ["grape","banana","orange","apple","peach"]
for fruit in like_fruits:
    print(fruit)
for fruit in like_fruits:
    print(f"I like {fruit}")
print("I really like fruits")
'''  # 末尾添加几行代码，以完成如下任务
# 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素
like_fruits = ["grape","banana","orange","apple","peach"]
print("The first three items in the list are:")
print(like_fruits[0:3])
# 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素
print("Three items from the middle of the list are:")
print(like_fruits[1:4])
# 打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素
print("The last three items in the list are:")
print(like_fruits[-3:])