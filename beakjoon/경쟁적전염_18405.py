import sys

n, k = map(int, sys.stdin.readline().split())
virus = []
for _ in range(n):
    virus.append(list(map(int, sys.stdin.readline().split())))
s, x, y = map(int, sys.stdin.readline().split())

move_1 = [0,0,-1,1]
move_2 = [-1,1,0,0]
multi = []
def evil_virus():
    for i in range(n):
        for j in range(n):
            if virus[i][j] == 0:
                priority = k+1
                for x, y in zip(move_1, move_2):
                    if i+x < n and j+y < n and virus[i+x][j+y] != 0:
                        if virus[i+x][j+y] < priority:
                            priority = virus[i+x][j+y]
                if priority < k+1:
                    multi.append([priority, i, j])
    for v, i, j in multi:
        virus[i][j] = v
    
    

for _ in range(s):
    evil_virus()
    multi = []
print(virus[x-1][y-1])