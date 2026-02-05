# 将一些朋友的姓名存储在一个列表中，并将其命名为 names。
# 依次访问该列表的每个元素，从而将每个朋友的姓名都打印出来。
names = ["夏","楼","刘","吴","张"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
# 不打印每个朋友的姓名，而是为每人打印一条消息。
# 每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
message = f"{names[0]}，最近过的还好吗"
print(message)
message = f"{names[1]}，最近过的还好吗"
print(message)
message = f"{names[2]}，最近过的还好吗"
print(message)
message = f"{names[3]}，最近过的还好吗"
print(message)
message = f"{names[4]}，最近过的还好吗"
print(message)
# 创建一个包含多种通勤方式的列表。
# 根据该列表打印一系列有关这些通勤方式的陈述
commuting_method = ["walking","bicycle","electric bake","bus"]
print(f"The commuting mode I choose most often is {commuting_method[2]}")
print(f"For short distances, I would choose {commuting_method[0]}")
print(f"我坐{commuting_method[3]}会晕车")
print(f"天气好的时候，骑{commuting_method[1]}出行很好")