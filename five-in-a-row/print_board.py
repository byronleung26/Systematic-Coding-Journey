def print_board():
    """打印棋盘"""
    print("\033[1;37;41m--------------简易五子棋（控制台版）---------------\033[0m")
    print("\033[1;34;47m    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15   \033[0m")
    for i in range(len(chessboard)):
        print("\033[1;34;47m " + chr(i + ord('A')) + " \033[0m", end='')
        for j in range(len(chessboard[i])):
            print("\033[1;30;47m " + chessboard[i][j] + " \033[0m", end='')
        print("\033[1;34;47m " + chr(i + ord('A')) + " \033[0m")
    print("\033[1;34;47m    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15   \033[0m")