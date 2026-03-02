try:
    height = float(input("请输入身高(cm)：")) / 100
    weight = float(input("请输入体重(kg):"))
    if height <=0 or weight <= 0:
        print("❌身高体重必须大于0")
    else:
        bmi = weight / height / height
        if bmi < 18.5:
            status = "偏瘦"
        elif bmi < 24:
            status = "正常"
        elif bmi < 28:
            status = "超重"
        else:
            status = "肥胖"
        print(f"您的BMI指数：{bmi:.2f}")
        print(f"📌 健康状况：{status}")
except:
    print("❌ 请输入有效的数字")