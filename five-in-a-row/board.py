def initialization():
    """初始化棋盘"""
    chessboard = []
    for i in range(15):
        chessboard.append([])
        for j in range(15):
            chessboard[i].append('+')
    return chessboard

def print_board(board):
    """打印棋盘"""
    print("\033[1;37;41m--------------简易五子棋（控制台版）---------------\033[0m")
    print("\033[1;34;47m    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15   \033[0m")
    for i in range(len(board)):
        print("\033[1;34;47m " + chr(i + ord('A')) + " \033[0m", end='')
        for j in range(len(board[i])):
            print("\033[1;30;47m " + board[i][j] + " \033[0m", end='')
        print("\033[1;34;47m " + chr(i + ord('A')) + " \033[0m")
    print("\033[1;34;47m    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15   \033[0m")