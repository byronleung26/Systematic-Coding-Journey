size = int(input("请输入棋盘大小(如15): "))

# 第一行
print("┌", end="")
for i in range(size-2):
    print("─┬─", end="")
print("─┐")

# 中间行
for row in range(size-2):
    print("├", end="")
    for col in range(size-2):
        print("─┼─", end="")
    print("─┤")

# 最后一行
print("└", end="")
for i in range(size-2):
    print("─┴─", end="")
print("─┘")