# 编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。
# 这个函数应接受歌手名和专辑名，并返回一个包含这两项信息的字典。
# 使用这个函数创建三个表示不同专辑的字典，
# 并打印每个返回的值，以核实字典正确地存储了专辑的信息
# 给make_album()函数添加一个默认值为 None 的可选形参，以便存储专辑包含的歌曲数。
# 如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。
# 调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
# def make_album(singer,album,number=None):
#     """返回包含歌手和专辑名的字典"""
#     singer_album = {'singers':singer,'albums':album}
#     if number is not None:
#         singer_album['number'] = number
#     return singer_album
# album1 = make_album('Michael Jackson','Thriller',9)
# print(album1)
# album2 = make_album('凤凰传奇','月亮之上')
# print(album2)
# album3 = make_album('周杰伦','惊叹号！')
# print(album3)
# 编写一个while循环，让用户输入歌手名和专辑名。
# 获取这些信息后，使用它们来调用 make_album() 函数并将创建的字典打印出来。
# 在这个 while 循环中，务必提供退出途径。
def make_album(singer,album,number=None):
    """返回包含歌手和专辑名的字典"""
    singer_album = {'singers':singer,'albums':album}
    if number is not None:
        singer_album['number'] = number
    return singer_album
active = True
while active:
    singer = input("请输入歌手名（输入quit退出）：")
    if singer.lower() == 'quit':
        active = False
        break
    album = input("请输入专辑名（输入quit退出）：")
    if album.lower() == 'quit':
        active = False
        break
    else:
        s_a = make_album(singer,album)
        print(s_a)
