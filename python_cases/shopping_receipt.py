pricedict = {  # 商品价格字典
    "apple": 6,
    "banana": 3.3,
    "chips": 10,
    "glove": 15.5,
}
subtotal = []  # 存放商品小计的列表
items = []  # 记录商品名
while True:
    merchandise = input("请输入商品名：")
    if not merchandise:  # 未输入则退出
        break
    quantity = input("请输入数量：")
    if not quantity:  # 未输入则退出系统
        break
    quan_float = float(quantity)  # 输入价格转换为浮点数
    price = pricedict[merchandise]  # 从字典提出单价
    item_total = quan_float*price  # 计算商品小计
    subtotal.append(item_total)  # 小计加入列表
    items.append((merchandise, price, quan_float, item_total))  # 用元组记录记录商品信息并加入列表
total = 0  # 总价
for i in subtotal:  # 遍历计算总价
    total += 1
print("""
——————————小票——————————
商品   单价   数量   小计      
""")
for item in items:
    print(f"{item[0]}  {item[1]}  {item[2]}  {item[2]}")
print(f"""
———————————————————————
总价：{total:.2f}元
———————————————————————
""")