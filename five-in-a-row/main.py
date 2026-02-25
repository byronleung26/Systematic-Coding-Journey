# 初始化
finish = False
flagNum = 1
flagch = '●'
x= 0
y = 0

# 初始化棋盘
chessboard = []
for i in range(15):
    chessboard.append([])
    for j in range(15):
        chessboard[i].append('+')

# 打印标题
print("\033[1;37;41m--------------简易五子棋（控制台版）---------------\033[0m")

def check_win(board, x, y, piece):
    """胜负判断算法"""
    # 四个方向：水平、垂直、右下、右上
    directions = [(1,0), (0,1), (1,1), (1,-1)]
    for dx, dy in directions:
        count = 1 
        # 正方向
        for step in range(1, 5):
            nx, ny = x + dx*step, y + dy*step
            if 0 <= nx < 15 and 0 <= ny < 15 and board[nx][ny] == piece:
                count += 1
            else:
                break
        # 反方向
        for step in range(1, 5):
            nx, ny = x - dx*step, y - dy*step
            if 0 <= nx < 15 and 0 <= ny < 15 and board[nx][ny] == piece:
                count += 1
            else:
                break
        if count >= 5:
            return True
    return False

while True:
    """落子与判断"""
    # 打印棋盘
    print("\033[1;34;47m    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15   \033[0m")
    for i in range(len(chessboard)):
        print("\033[1;34;47m " + chr(i + ord('A')) + " \033[0m", end='')
        for j in range(len(chessboard[i])):
            print("\033[1;30;47m " + chessboard[i][j] + " \033[0m", end='')
        print("\033[1;34;47m " + chr(i + ord('A')) + " \033[0m")
    print("\033[1;34;47m    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15   \033[0m")
    # 判断当前下棋者
    if flagNum == 1:
        flagch = '●'
        print('\033[1;37;45m请●输入棋子坐标（例如A10）：\033[0m', end=' ')  # 白字粉底
    else:
        flagch = '○'
        print('\033[1;30;42m请o输入棋子坐标（例如J12）：\033[0m', end=' ')  # 黑字绿底
    # 记录棋子坐标
    str = input()
    ch = str[0]
    x= ord(ch) - 65
    y = int(str[1:]) - 1
    # 判断棋子坐标
    if x < 0 or x > 14 or y < 0 or y >14:
        print("\033[31m您输入的坐标有误，请重新输入！\033[0m")
        continue
    # 判断指定坐标位置是否有棋子
    if chessboard[x][y] == "+":
        if(flagNum == 1):
            chessboard[x][y] = "●"
        else:
            chessboard[x][y] = "○"
    else:
        print("\033[31m您输入的位置已经有其他棋子，请重新输入！\033[0m")
        continue

    def msg():
        """输出最后胜利的局面"""
        print("\033[1;34;47m    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15   \033[0m")
        for i in range(len(chessboard)):
            print("\033[1;34;47m " + chr(i + ord('A')) + " \033[0m", end='')
            for j in range(len(chessboard[i])):
                print("\033[1;30;47m " + chessboard[i][j] + " \033[0m", end='')
            print("\033[1;34;47m " + chr(i + ord('A')) + " \033[0m")
            print("\033[1;34;47m    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15   \033[0m")
        """输出赢家"""
        if flagNum == 1:
            print("●棋胜利！")
        else:
            print("o棋胜利！")

    # 胜负判断
    if check_win(chessboard, x, y, flagch):
            msg()
            finish = True
            break

    # 更换当前下棋者
    flagNum *= -1
