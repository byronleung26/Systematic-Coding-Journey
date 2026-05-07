"""favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")"""
# 对程序执行以下操作。创建一个应该会接受调查的人的名单，其中有些人已在字典中，而其他人不在字典中。
# 遍历这个名单。对于已参与调查的人，打印一条消息表示感谢；对于还未参与调查的人，打印一条邀请参加调查的消息。
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
surveyed = ["Landon", "jen", "Ross", "edward"]
for person in surveyed:
    if person in favorite_languages:
        print(f"{person}，感谢你参与调查")
    else:
        print(f"{person}，邀请你参与最喜欢语言的调查") 