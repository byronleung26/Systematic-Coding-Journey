# 创建一个列表，其中包含一系列简短的文本消息。
# 将这个列表传递给一个名为 show_messages() 的函数，
# 这个函数会打印列表中的每条文本消息
messages = ["Hello","Good","Quickly"]
def show_messages(messages):
    """打印列表中的消息"""
    for msg in messages:
        print(msg)
show_messages(messages)