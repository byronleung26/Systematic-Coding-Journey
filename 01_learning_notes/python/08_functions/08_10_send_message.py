# 编写一个名为send_messages() 的函数，
# 将每条消息都打印出来并移到一个名为sent_messages 的列表中。
# 调用 send_messages() 函数，
# 再将两个列表都打印出来，确认把消息移到了正确的列表中
# messages = ["Hello","Good","Quickly"]
# sent_messages = []
# def send_messages(message_list):
#     """打印每条消息并移到新列表"""
#     while messages:
#         msg = messages.pop()
#         print(msg)
#         sent_messages.append(msg)
# send_messages(messages)
# print(sent_messages)
# 修改程序，在调用函数send_messages()时，向它传递消息列表的副本。
# 调用send_messages()函数后，将两个列表都打印出来，确认原始列表保留了所有的消息。
messages = ["Hello","Good","Quickly"]
sent_messages = []
def send_messages(message_list):
    """打印每条消息并移到新列表"""
    while messages:
        msg = messages.pop()
        print(msg)
        sent_messages.append(msg)
send_messages(messages[:])
print(messages)
print(sent_messages)
