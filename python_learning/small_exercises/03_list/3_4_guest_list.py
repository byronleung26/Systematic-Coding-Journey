# 如果你可以邀请任何人一起共进晚餐，你会邀请哪些人？
# 请创建一个列表，其中包含至少三个你想邀请的人，
# 然后使用这个列表打印消息，邀请这些人都来与你共进晚餐。
guest_list = ["张","刘","杨"]
print(f"{guest_list[0]}，明晚有空吗？我邀请你、{guest_list[1]}、{guest_list[2]}和我共进晚餐")
print(f"{guest_list[1]}，明晚有空吗？我邀请你、{guest_list[0]}、{guest_list[2]}和我共进晚餐")
print(f"{guest_list[2]}，明晚有空吗？我邀请你、{guest_list[0]}、{guest_list[1]}和我共进晚餐")
# 刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾
# 程序末尾添加函数调用print()，指出哪位嘉宾无法赴约
# 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名
# 再次打印一系列消息，向名单中的每位嘉宾发出邀请
print(f"{guest_list[1]}无法赴约")
guest_list[1] = "李"
print(guest_list)
print(f"{guest_list[0]}，明晚有空吗？我邀请你、{guest_list[1]}、{guest_list[2]}和我共进晚餐")
print(f"{guest_list[1]}，明晚有空吗？我邀请你、{guest_list[0]}、{guest_list[2]}和我共进晚餐")
print(f"{guest_list[2]}，明晚有空吗？我邀请你、{guest_list[0]}、{guest_list[1]}和我共进晚餐")
# 你刚找到了一张更大的餐桌，可容纳更多的嘉宾就座。
# 请想想你还想邀请哪三位嘉宾。
# 在程序末尾添加函数调用print()，指出你找到了一张更大的餐桌。
# 使用 insert() 将一位新嘉宾添加到名单开头。
# 使用 insert() 将另一位新嘉宾添加到名单中间。
# 使用 append() 将最后一位新嘉宾添加到名单末尾。
# 打印一系列消息，向名单中的每位嘉宾发出邀请。
print("我找到了一张更大的餐桌")
guest_list.insert(0,"王")
guest_list.insert(2,"赵")
guest_list.append("董")
print(f"{guest_list[0]}，明晚有空吗？我邀请你和我共进晚餐")
print(f"{guest_list[1]}，明晚有空吗？我邀请你和我共进晚餐")
print(f"{guest_list[2]}，明晚有空吗？我邀请你和我共进晚餐")
print(f"{guest_list[3]}，明晚有空吗？我邀请你和我共进晚餐")
print(f"{guest_list[4]}，明晚有空吗？我邀请你和我共进晚餐")
print(f"{guest_list[5]}，明晚有空吗？我邀请你和我共进晚餐")