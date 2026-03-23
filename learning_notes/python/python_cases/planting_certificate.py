import time

name = input("输入姓名：") or "爱心人士"
plant = input("输入植物种类：") or "希望之树"
date = input("输入时间(20xx-xx-xx)：") or time.strftime("%Y-%m-%d")
location = input("输入种植地点：") or "绿色家园"
print(f"""
           植树证书
-------------------------------
 {name} 谢谢你：

     你 {date} 在 {location} 种
 植了一颗 {plant} ，我们将悉心照
 料它成长，你可以经常来看它。

    感谢你为环境绿化做出的贡献！
-------------------------------
""")