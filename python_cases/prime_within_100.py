# 编写程序,实现输出100以内质数的功能。

for n in range(2,101):
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n,end=" ")