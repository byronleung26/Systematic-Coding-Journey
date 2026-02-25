# 创建一个名为 cities 的字典，将三个城市名用作键。
# 对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
# 表示每座城市的字典都应包含country、population和fact等键。
# 将每座城市的名字以及相关信息都打印出来。
cities = {
    "Shanghai": {
        "country": "China", 
        "population": "2480.26w", 
        "fact": "地处长江入海口"}, 
    "Newyork": {
        "country": "Amecrian", 
        "population": "825.80w",
        "fact": "濒临大西洋"}, 
    "Paris": {
        "country": "France", 
        "population": "1242.00w", 
        "fact": "法国首都"}
    }
for city,info in cities.items():
    print(
        f"{city}, "
        f"belong to {info['country']}, "
        f"population is {info['population']}, "
        f"it is {info['fact']}."
        )