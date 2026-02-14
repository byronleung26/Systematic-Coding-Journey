# 分华东1、华南2、华北3三个地区不同的首重价目(13,12,14)和续重价目(3,2,4)计算快递价格
total_weight = float(input("请输入快递重量："))
destination = input("请选择目标地区（输入数字序号）1.华东2.华南3.华北")
base_price = {'1':13, '2':12, '3':14}
extra_price = {'1':3, '2':2, '3':4}
if destination in base_price:
    if total_weight <= 1:
        price = base_price[destination]
    else:
        price = base_price[destination] + (total_weight - 1)*extra_price[destination]
    print(price)
else:
    print("地区编号输入错误")