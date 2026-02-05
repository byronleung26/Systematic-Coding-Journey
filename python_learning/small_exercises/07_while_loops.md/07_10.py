# 编写一个程序，调查用户梦想中的度假胜地。使用类似于
# “If you could visit one place in the world, where would you go?”
# 的提示，并编写一个打印调查结果的代码块。
places = {}
active = True
while active:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    places[name] = place
    judgement = input("Dose anyone else to respond? (Yes or No) ")
    if judgement == "no":
        active = False
print("\n===Result===")
for name, place in places.items():
    print(f"{name} would like to gou {place}")