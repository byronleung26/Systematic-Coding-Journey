# 序数表示顺序位置，如1st和2nd。序数大多以th结尾，只有1st、2nd、3rd例外。
# 在一个列表中存储数字1～9。
# 遍历这个列表。
# 在循环中使用一个if-elif-else结构，打印每个数字对应的序数。输出内容应为"1st 2nd 3rd 4th 5th 6th 7th 8th 9th"，每个序数都独占一行。
numbers = list(range(1,10))
for i in numbers:
    if i == 1:
        print("1st")
    elif i == 2:
        print("2nd")
    elif i == 3:
        print("3rd")
    else:
        print(f"{i}th")