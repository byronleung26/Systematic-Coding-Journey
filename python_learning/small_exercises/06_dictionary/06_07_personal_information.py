# 创建三个表示个人信息的字典,
# 然后将这三个字典都存储在一个名为 people 的列表中。
# 遍历这个列表，将其中每个人的所有信息都打印出来。
information_01 = {"first_name": "Baoyan", "last_name": "Liang", "age": 28, "city": "PingLiang"}
information_02 = {"first_name": "Ziqi", "last_name": "Xia", "age": 26, "city": "WuHan"}
information_03 = {"first_name": "Weizhu", "last_name": "Lou", "age": 27, "city": "HangZhou"}
people = [information_01, information_02, information_03]
for person in people:
    print("个人信息：")
    print(f"name:{person['last_name']}{person['first_name']}")
    print(f"age:{person['age']}")
    print(f"city:{person['city']}")
    print('=' * 20)