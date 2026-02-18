height = float(input("请输入身高(cm)：")) / 100
weight = float(input("请输入体重(kg):"))
bmi = weight / height / height
print(f"您的健康指数：{bmi:.2f}")