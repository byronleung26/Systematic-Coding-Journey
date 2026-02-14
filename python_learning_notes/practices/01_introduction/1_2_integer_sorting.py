#习题1.2：输入3个整数，把这3个整数由小到大输出
number = []
for i in range(3):
    number.append(int(input('请输入整数：')))
number.sort()
print(number)