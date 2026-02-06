"""1. 需求
接收用户从键盘输入的商品价格
根据价格输出小票
    ·······································
    单号：DH202311010001
    时间：2023-11-01 20：56：15
    ·······································
    名称 数量 单价 商品金额
    金士顿U盘8G 1 40.00 40.00
    胜创16GTF卡 1 50.00 50.00
    读卡器 1 8.00 8.00
    网线2米 1 5.00 5.00
    ·······································
    总数：4 总额：103.00
    折后总额：103.00
    实收：103.00 找零：0.00
    收银：管理员
    ·······································
2. 分析设计思路
商品单价从键盘输入，其他内容固定
每一行内容看作一个字符串，通过input()函数输出
3. 分步实现代码"""
# 1. 输入价格（转换为浮点数）
udisk_price = float(input("扫描U盘的价格："))
gtf_price = float(input("扫描GTF卡的价格："))
card_reader_price = float(input("扫描读卡器的价格："))
network_cable_price = float(input("扫描网线的价格："))
print("·" * 40)
print("单号：DH202311010001")
print("时间：2023-11-01 20:56:15")
print("·" * 40)
print("名称            数量 单价   金额")
print("-" * 40)
# 2. 计算总额
total = udisk_price + gtf_price + card_reader_price + network_cable_price
# 3. 使用f-string格式化输出（自动对齐）
print(f"金士顿U盘8G     1    {udisk_price:>6.2f} {udisk_price:>6.2f}")
print(f"胜创16GTF卡     1    {gtf_price:>6.2f} {gtf_price:>6.2f}")
print(f"读卡器          1    {card_reader_price:>6.2f} {card_reader_price:>6.2f}")
print(f"网线2米         1    {network_cable_price:>6.2f} {network_cable_price:>6.2f}")
print("·" * 40)
# 4. 使用实际计算的总额
print(f"总数：4 总额：{total:.2f}")
print(f"折后总额：{total:.2f}")
print(f"实收：{total:.2f} 找零：0.00")
print("收银：管理员")
print("·" * 40)