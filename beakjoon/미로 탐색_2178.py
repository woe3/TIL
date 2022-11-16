import sys
from collections import deque
sys.setrecursionlimit(10**4)

n, m = map(int, sys.stdin.readline().split())
path = []
zero = [0 for _ in range(m+2)]
path.append(zero)
for _ in range(n):
    a = sys.stdin.readline().strip()
    row = [0] + [int(i) for i in a] + [0]
    path.append(row)
path.append(zero)


queue = deque([[1, 1]])
answer = 1
reach = [n, m]
def bfs(path, repeat, reach):
    global answer
    for i in range(repeat):
        now = queue.popleft()
        
        four_ways = []
        # down
        four_ways.append([now[0]+1, now[1]])
        # up
        four_ways.append([now[0]-1, now[1]])
        # left
        four_ways.append([now[0], now[1]-1])
        # right
        four_ways.append([now[0], now[1]+1])

        for i in four_ways:
            if path[i[0]][i[1]] == 1:
                if i == reach:
                    return print(answer+1)
                queue.append(i)
                path[i[0]][i[1]] = 0
    answer += 1           
    bfs(path, len(queue), reach)

bfs(path, 1, reach)