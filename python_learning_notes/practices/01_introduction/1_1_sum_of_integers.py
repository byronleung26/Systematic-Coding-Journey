#习题1.1：输入整数n。计算1~n之和
n = int(input("请输入一个整数："))
total = 0
for i in range(1,n+1):
    total += i
print(f"1~{n}的求和结果为{total}")