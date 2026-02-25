def initialization():
    """初始化棋盘"""
    chessboard = []
    for i in range(15):
        chessboard.append([])
        for j in range(15):
            chessboard[i].append('+')