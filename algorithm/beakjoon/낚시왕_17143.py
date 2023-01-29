import sys
row, colum, m = map(int, sys.stdin.readline().split())
sea = [[[] for _ in range(colum+1)] for _ in range(row+1)]
for _ in range(m):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    sea[r][c] = [s, d, z]

catch = 0
move = []
for i in range(1, colum+1):
    for j in range(1, row+1):
        if sea[j][i]:
            catch += sea[j][i][2]
            sea[j][i] = []
            break
    temp_sea = [[[] for _ in range(colum+1)] for _ in range(row+1)]
    for r in range(1, row+1):
        for c in range(1, colum+1):
            if sea[r][c]:
                new_r = r
                new_c = c
                for m in range(sea[r][c][0]):
                    if sea[r][c][1] == 1:
                        new_r -= 1
                        if new_r < 1:
                            new_r += 2
                            sea[r][c][1] = 2
                    elif sea[r][c][1] == 2:
                        new_r += 1
                        if new_r > row:
                            new_r -= 2
                            sea[r][c][1] = 1
                    elif sea[r][c][1] == 3:
                        new_c += 1
                        if new_c > colum:
                            new_c -= 2
                            sea[r][c][1] = 4
                    elif sea[r][c][1] == 4:
                        new_c -= 1
                        if new_c < 1:
                            new_c += 2
                            sea[r][c][1] = 3
                
                if temp_sea[new_r][new_c]:
                    if temp_sea[new_r][new_c][2] < sea[r][c][2]:
                        temp_sea[new_r][new_c] = sea[r][c]
                else: temp_sea[new_r][new_c] = sea[r][c]
    
    for r in range(1, row+1):
        for c in range(1, colum+1):
            sea[r][c] = temp_sea[r][c]

print(catch)