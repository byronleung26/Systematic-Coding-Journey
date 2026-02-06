# 创建一个名为sandwich_orders的列表，其中包含各种三明治的名字，
# 再创建一个名为finished_sandwiches的空列表。
# 遍历列表sandwich_orders，对于其中的每种三明治，都打印一条消息，
# 如“I made your tuna sandwich.”，
# 并将其移到列表finished_sandwiches中。
# 当所有三明治都制作好后，打印一条消息，将这些三明治列出来。
"""sandwich_orders = ["ham","pastrami","egg","pastrami","chicken""pastrami",]
finished_sandwiches = []
while sandwich_orders:
    made = sandwich_orders.pop()
    print(f"I made your {made} sandwich")
    finished_sandwiches.append(made)
print("\nAny sandwiches have finished:")
result = ', '.join([f"{sw} sandwich" for sw in finished_sandwiches])
print(result)"""
# 先打印一条消息，指出熟食店的五香烟熏牛肉（pastrami）卖完了；
# 再使用一个while循环将列表sandwich_orders中的'pastrami'都删除。
# 确认最终的列表finished_sandwiches中未包含'pastrami'
sandwich_orders = ["ham","pastrami","egg","pastrami","chicken","pastrami"]
finished_sandwiches = []
print("Our Store has run out of pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    made = sandwich_orders.pop()
    print(f"I made your {made} sandwich")
    finished_sandwiches.append(made)
print(finished_sandwiches)
