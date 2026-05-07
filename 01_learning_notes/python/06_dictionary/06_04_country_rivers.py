# 创建一个字典，在其中存储三条河流及其流经的国家。例如，一个键值对可能是 'nile': 'egypt'。
# 使用循环为每条河流打印一条消息，如下所示。The Nile runs through Egypt.
# 使用循环将该字典中每条河流的名字打印出来。
# 使用循环将该字典包含的每个国家的名字打印出来。
country_rivers = {"Yellow River": "China",
    "Nile": "Egypt",
    "Amazon River": "Brazil",
    }
for river, country in country_rivers.items():
    print(f"The {river} runs through {country}.")
for river in country_rivers.keys():
    print(river)
for country in country_rivers.values():
    print(country)