def get_player_input(flagNum):
    """玩家落子"""
    # 判断当前下棋者
    if flagNum == 1:
        flagpiece = '●'
        print('\033[1;37;45m请●输入棋子坐标（例如A10）：\033[0m', end=' ')  # 白字粉底
    else:
        flagpiece = '○'
        print('\033[1;30;42m请o输入棋子坐标（例如J12）：\033[0m', end=' ')  # 黑字绿底
    
    # 记录棋子坐标
    str = input()
    print(f"原始输入: '{str}'")  # 看看是什么
    ch = str[0]
    print(f"第一个字符: '{ch}', ASCII: {ord(ch)}")
    x = ord(ch) - 65
    print(f"计算x: {ord(ch)} - 65 = {x}")
    num_part = str[1:]
    print(f"数字部分: '{num_part}'")
    y = int(str[1:]) - 1
    print(f"计算y: {int(num_part)} - 1 = {y}")

    return flagpiece, x, y
    
def validate_coordinate(x, y):
    """判断棋子坐标是否在范围"""
    if x < 0 or x > 14 or y < 0 or y >14:
        print("\033[31m您输入的坐标有误，请重新输入！\033[0m")
        return False
    return True
    
def check_position(flagNum, board, x, y):
    """判断是否空位并落子"""
    if board[x][y] == "+":
        if flagNum == 1:
            board[x][y] = "●"
        else:
            board[x][y] = "○"
        return True
    else:
        print("\033[31m您输入的位置已经有其他棋子，请重新输入！\033[0m")
        return False