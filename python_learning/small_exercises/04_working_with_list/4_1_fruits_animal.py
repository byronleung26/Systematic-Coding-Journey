# 想出至少三种你喜欢的水果，将其名称存储在一个列表中，再使用for循环将每种的名称打印出来。
like_fruits = ["grape","banana","orange"]
for fruit in like_fruits:
    print(fruit)
# 修改这个 for 循环，使其打印包含水果名称的句子,对于每种水果都显示一行输出。
for fruit in like_fruits:
    print(f"I like {fruit}")
# 在程序末尾添加一行代码（不包含在 for 循环中）,一个总结性的句子。
print("I really like fruits")