# 编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。
# 这个函数应返回一个格式类似于下面的字符串：
# "Santiago, Chile"
# 至少使用三个城市至国家对调用这个函数，并打印它返回的值.
def city_country(city,country):
    """城市及其所属国家"""
    connection = city + ", " + country
    return connection
connection = city_country('Beijing','China')
print(connection)
connection = city_country('Paris','France')
print(connection)
connection = city_country('New York','USA')
print(connection)
