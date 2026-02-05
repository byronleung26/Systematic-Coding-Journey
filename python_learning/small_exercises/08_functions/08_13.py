# def build_profile(first, last, **user_info): 
#     """创建一个字典，其中包含我们知道的有关用户的一切""" 
#     user_info['first_name'] = first 
#     user_info['last_name'] = last 
#     return user_info 
# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics') 
# print(user_profil
# 调用build_profile()来创建有关你的简介。
# 在调用这个函数时，指定你的名和姓，以及三个用来描述你的键值对
def build_profile(first, last, **user_info): 
    """创建一个字典，其中包含我们知道的有关用户的一切""" 
    user_info['first_name'] = first.title() 
    user_info['last_name'] = last.title() 
    return user_info 
my_profile = build_profile('byron', 'leung', location='China', age=28, height='172cm', weight='75kg')
print(my_profile)