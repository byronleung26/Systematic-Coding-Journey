# 编写一个循环，提示用户输入一系列比萨配料，并在用户输入 'quit' 时结束循环。
# 每当用户输入一种配料后，都打印一条消息，指出要在比萨中添加这种配料。
while True:
    toppings = input("请输入配料：")
    if toppings == "quit":
        break
    else:
        print(f"将要在匹萨中添加{toppings}")
