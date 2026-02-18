pricedict = {
    "apple": 6,
    "banana": 3.3,
    "chips": 10,
    "glove": 15.5,
}
subtotal = []
items = []
while True:
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