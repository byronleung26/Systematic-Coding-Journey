type = input("输入贷款类型1.商业贷款2.公积金贷款")
amount = float(input("输入贷款金额"))
term = float(input("输入贷款年限"))

rate_mon_business = {"5年以内": 4.75/12/100, "5年以上": 4.90/12/100}
rate_mon_fund = {"5年以内": 2.6/12/100, "5年以上": 3.1/12/100}

if type == '1':
    if term <= 5:
        monthly_rate = rate_mon_business["5年以内"]
    else:
        monthly_rate = rate_mon_business["5年以上"]
elif type == '2':
    if term <= 5:
        monthly_rate = rate_mon_fund["5年以内"]
    else:
        monthly_rate = rate_mon_fund["5年以上"]
else:
    print("Warning: 输入错误")

monthly_repayment = (
    (amount * monthly_rate * (1 + monthly_rate) ** (term * 12)) /
    (((1 + monthly_rate) ** (term * 12)) - 1)
)
total_repayment = monthly_repayment * term *12
total_interest = total_repayment - amount

print(f"""
      等额本金的情况下：
      每月月供{monthly_repayment:.2f}, 
      还款总额{total_repayment:.2f}, 
      总利息{total_interest:.2f}。
      """)