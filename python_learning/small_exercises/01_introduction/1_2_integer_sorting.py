#习题1.2：输入3个整数，把这3个整数由小到大输出
l=[]#l和1不要写混
for i in range(3):#冒号
    x=int(input('请输入整数：'))
    l.append(x)
l.sort()
print(l)#变量名一致