def solution(board):
    # 보드를 세로로 만든다.
    board_turn = ['', '', '']
    for i in range(3):
        for j in range(3):
            board_turn[j] += board[i][j]
    # 승리 카운트
    o_win = []
    x_win = []
    for i in board:
        o_win.append(i.count('O'))
        x_win.append(i.count('X'))
    for i in board_turn:
        o_win.append(i.count('O'))
        x_win.append(i.count('X'))
    x_cross = 0
    o_cross = 0
    for i in range(3):
        if board[i][i] == 'O':
            o_cross += 1
        elif board[i][i] == 'X':
            x_cross += 1
    o_win.append(o_cross)
    x_win.append(x_cross)
    x_cross = 0
    o_cross = 0
    for i in range(3):
        if board[2-i][i] == 'O':
            o_cross += 1
        elif board[2-i][i] == 'X':
            x_cross += 1
    o_win.append(o_cross)
    x_win.append(x_cross)
    # 불가능한 경우의 수
    # X > O
    x_num = 0
    o_num = 0
    for i in board:
        x_num += i.count('X')
        o_num += i.count('O')

    if x_num + 1 == o_num:
        if o_win.count(3) > 0 and x_win.count(3) == 0:
            return 1
        elif o_win.count(3) == 0 and x_win.count(3) == 0:
            return 1
    elif x_num == o_num:
        if x_win.count(3) > 0 and o_win.count(3) == 0:
            return 1
        elif o_win.count(3) == 0 and x_win.count(3) == 0:
            return 1

    return 0