delete_block = []

def square(l, board):
    global delete_block
    block = board[l[0]][l[1]]
    if (board[l[0]+1][l[1]] == block and 
        board[l[0]][l[1]+1] == block and 
        board[l[0]+1][l[1]+1] == block):
        delete_block.append([l[0], l[1]])
        delete_block.append([l[0]+1, l[1]])
        delete_block.append([l[0], l[1]+1])
        delete_block.append([l[0]+1, l[1]+1])


    return


    
def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    global delete_block
    answer = 0
    temp_answer = -1
    
    # 정답의 변화가 없다면 4블록을 모두 찾은 것으로 간주하여 멈춤
    while answer != temp_answer:
        temp_answer = answer
        #블록 찾기
        delete_block = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]:
                    square([i,j], board)
                    
        #블록 지우기
        for y, x in delete_block:
            if board[y][x]:
                board[y][x] = 0
                answer +=1

        #블록 내리기
        for i in range(m-1,-1,-1):
            for j in range(n):
                if not board[i][j]:
                    for k in range(i-1, -1,-1):
                        if board[k][j]:
                            board[i][j] = board[k][j]
                            board[k][j] = 0
                            break

    return answer

solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])