from board import initialization, print_board
from decision import check_win, msg
from move import get_player_input, validate_coordinate, check_position

finish = False
flagNum = 1
flagpiece = '●'
x = 0
y = 0

board = initialization()  # 初始化return chessboard

while True:
    
    print_board(board)  # 打印棋盘
    
    flagpiece, x, y = get_player_input(flagNum) # 玩家落子return flagpiece, x, y

    if not validate_coordinate(x, y):  # 判断棋子坐标是否在范围return True or False
        continue

    if not check_position(flagNum, board, x, y):  # 判断指定坐标位置是否有棋子return True or False
        continue

    # 判断胜负、打印胜利棋盘和赢家
    if check_win(board, x, y, flagpiece):
        msg(board, flagNum)
        finish = True
        break
    
    # 更换当前下棋者
    flagNum *= -1