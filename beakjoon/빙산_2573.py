import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
move_x = [0,0,-1,1]
move_y = [-1,1,0,0]
melting = []
visited = [[0]*m for _ in range(n)]
ice_count = 0
year = 0
last_ice = []
def year_passed():
    global ice_count
    global last_ice
    global melting
    for i in range(1,n-1):
        for j in range(1, m-1):
            if graph[i][j] > 0:
                visited[i][j] = 0
                ice_count += 1
                melt = 0
                
                for x, y in zip(move_x, move_y):
                    if graph[i+x][j+y] < 1:
                        melt += 1
                melting.append([i,j,melt])

    for i,j,x in melting:
        graph[i][j] -= x
        if graph[i][j] < 1:
            ice_count -= 1
    melting = []



def bfs(v):
    global ice_count
    que = deque([v])
    while que:
        a, b = que.popleft()
        
        for x, y in zip(move_x, move_y):
            if graph[a+x][b+y] > 0 and visited[a+x][b+y] == 0:
                que.append([a+x, b+y])
                visited[a+x][b+y] = 1
                ice_count -= 1

def check_ice():
    global year
    for i in range(1, n-1):
            for j in range(1, m-1):
                if graph[i][j] > 0:
                    bfs([i,j])
                    return
    year = 0

while ice_count == 0:
    year += 1
    year_passed()
    check_ice()

print(year)
# 통과못함(시간 초과)