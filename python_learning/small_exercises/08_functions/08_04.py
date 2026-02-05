# 编写一个名为describe_city()的函数，
# 它接受一座城市的名字以及该城市所属的国家。
# 这个函数应该打印一个像下面这样简单的句子。
#    Reykjavik is in Iceland.
# 给用于存储国家的形参指定默认值。
# 为三座不同的城市调用这个函数，其中至少有一座城市不属于默认的国家。
def describe_city(city,country="China"):
    """一座城市及所属的国家"""
    print(f"{city} is in {country}")
describe_city("Beijing")
describe_city("New York","USA")
describe_city(country="Japan",city="Tokyo")