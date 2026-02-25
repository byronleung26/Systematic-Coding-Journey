# 有一家自助式餐馆，只提供5种简单的食品。请想出5种简单的食品，并将其存储在一个元组中。
foods = ("Noodle","dumpling","hamburger","fish","ice cream")
# 使用一个 for 循环将该餐馆提供的 5 种食品都打印出来。
for food in foods:
    print(food)
# 尝试修改其中的一个元素，核实 Python 确实会拒绝你这样做。
'''foods[2] = chicken'''
# 餐馆调整菜单，替换了两种食品。请编写一行给元组变量赋值的代码，用一个 for 循环将新元组的每个元素都打印出来。
foods = ("Noodle","dumpling","hamburger","chicken","milk")
for food in foods:
    print(food)