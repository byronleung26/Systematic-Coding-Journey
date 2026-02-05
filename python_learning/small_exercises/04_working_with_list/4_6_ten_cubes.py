# 通过给range()函数指定第三个参数来创建一个列表，其中包含1～20的奇；再使用一个for循环将这些数打印出来
number_list = list(range(1,21,2))
for value in number_list:
    print(value)
# 创建一个列表，其中包含前10个整数（1～10）的立方，再使用一个for循环将这些立方数打印出来。
ten_lifang = []
for i in range(1,11):
    ten_lifang.append(i**3)
for value in ten_lifang:
    print(value)
# 使用列表推导式生成一个列表，其中包含前10个整数的立方
ten_cubes = [value**3 for value in range(1,11)]
print(ten_cubes)