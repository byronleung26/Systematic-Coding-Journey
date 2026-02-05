#习题1.1：输入整数，n计算1~n之和
n=int(input("请输入一个整数："))
sum=0
for i in range(1,n+1):#注意冒号
    sum+=i#缩进4个空格或1个Tab
print("1~%d的求和结果为%d"%(n,sum))