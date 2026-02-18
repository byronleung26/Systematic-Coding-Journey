name = input("请输入姓名: ").strip()
company = input("请输入单位: ").strip()
position = input("请输入职位: ").strip()
phone = input("请输入手机号码: ").strip()
email = input("请输入电子邮箱: ").strip()
print('='*30)
print(f"""
{'姓名：' + name:^30}
{'职位：' + company + ' ' + position:^30}
{'电话号码：' + phone:^30}
{'电子邮箱：' + email:^30}
""")
print('='*30)