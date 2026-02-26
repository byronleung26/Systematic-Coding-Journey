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

def msg(board, flagNum):
    """输出最后胜利的局面"""
    print("\033[1;34;47m    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15   \033[0m")
    for i in range(len(board)):
        print("\033[1;34;47m " + chr(i + ord('A')) + " \033[0m", end='')
        for j in range(len(board[i])):
            print("\033[1;30;47m " + board[i][j] + " \033[0m", end='')
        print("\033[1;34;47m " + chr(i + ord('A')) + " \033[0m")
        print("\033[1;34;47m    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15   \033[0m")
    """输出赢家"""
    if flagNum == 1:
        print("●棋胜利！")
    else:
        print("o棋胜利！")