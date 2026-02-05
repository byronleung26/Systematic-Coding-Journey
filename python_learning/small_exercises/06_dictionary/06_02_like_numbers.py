# 使用一个字典来存储一些人喜欢的数。请想出5个人的名字，并将这些名字用作字典中的键。
# 再想出每个人喜欢的一个数，并将这些数作为值存储在字典中。
# 打印每个人的名字和喜欢的数。为了让这个程序更有趣，通过询问朋友确保数据是真实的。
like_numbers = {"Xia": 666, "zhang": 123, "Liu": 233, "Yang": 555, "Zhao": 88}
for name, number in like_numbers.items():
    print(f"{name}喜欢的数是{number}")