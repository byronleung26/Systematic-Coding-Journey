pricedict = {
    "苹果": 6,
    "香蕉": 3.3,
    "薯片": 10,
    "手套": 15.5,
}
subtotal = []
items = []
while True:
    print("商品价格表")
    for i in pricedict:
        print(f"{i}: {pricedict[i]}元")
    merchandise = input("请输入商品名(直接Enter退出)：")
    if not merchandise:
        break
    quantity = input("请输入数量(直接Enter退出)：")
    if not quantity:
        break
    quan_float = float(quantity)
    price = pricedict[merchandise]
    item_total = quan_float*price
    subtotal.append(item_total)
    items.append((merchandise, price, quan_float, item_total))
total = 0
for i in subtotal:
    total += i
print("""
——————————小票——————————
商品   单价   数量   小计      
""")
for item in items:
    print(f"{item[0]}  {item[1]}  {item[2]}  {item[3]}")
print(f"""
———————————————————————
总价：{total:.2f}元
———————————————————————
""")