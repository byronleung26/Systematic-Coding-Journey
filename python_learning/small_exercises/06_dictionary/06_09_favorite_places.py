# 创建一个名为favorite_places的字典。
# 在这个字典中，将三个人的名字用作键，并存储每个人喜欢的1～3个地方。
# 遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
favorite_places = {
    "Li": ["HongKong", "Shanghai"], 
    "Zhang": ["Beijing"], 
    "Dong": ["NewYork", "Singapore", "Lhasa"]
    }
for person, place in favorite_places.items():
    print(f"{person} like {','.join(place)}")