# 假设玩家在游戏中消灭了一个外星人，
# 请创建一个名为alien_color 的变量，并将其赋值为 'green'、'yellow' 或 'red'
alien_color = "green"
# 编写一条if语句，测试外星人是否是绿色的。如果是，就打印一条消息，指出玩家获得了5分
if alien_color == "green":
    print("The player has gained 5 points!")
#编写这个程序的两个版本，上述条件测试在其中的一个版本中通过，在另一个版本中未通过（未通过条件测试时没有输出）
if alien_color == "red":
    print("The player has gained 5 points!")
# 编写一个ifelse结构
# 如果外星人是绿色的，就打印一条消息，指出玩家因消灭该外星人获得了5分
if alien_color == "green":
    print("The player has gained 5 points for eliminating alien!")
# 如果外星人不是绿色的，就打印一条消息，指出玩家获得了10分
else:
    print("The player has gained 10 points!")
# 编写这个程序的两个版本，在一个版本中将执行if代码块，在另一个版本中将执行else代码块
if alien_color != "green":
    print("The player has gained 10 points!")
else:
    print("The player has gained 10 points for eliminating alien")
# 改为if-elif-else结构
# 如果外星人是绿色的，就打印一条消息，指出玩家获得了5分
# 如果外星人是黄色的，就打印一条消息，指出玩家获得了10分。
# 如果外星人是红色的，就打印一条消息，指出玩家获得了15分
# 编写这个程序的三个版本，分别在外星人为绿色、黄色和红色时打印一条消息
if alien_color == "green":
    print("The player has gained 5 points!")
elif alien_color == "yellow":
    print("The player has gained 10 points!")
elif alien_color == "red":
    print("The player has gained 15points!")
