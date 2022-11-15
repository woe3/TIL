import sys
from collections import deque
sys.setrecursionlimit(10**4)

n, m = map(int, sys.stdin.readline().split())
path = []
zero = [0 for _ in range(m)]
path.append(zero)
for _ in range(n):
    a = sys.stdin.readline().strip()
    row = [0] + [int(i) for i in a] + [0]
    path.append(row)
path.append(zero)

row_visited = [False] * (m+1)
visited = [row_visited for _ in range(n+1)]


def bfs(graph, visited):
    queue = deque([[1, 1]])
    visited[1][1] = True
    answer = 1
    while queue:
        now = queue.popleft()
        four_ways = []
        # down
        four_ways += [now[0]+1, now[1]]
        # up
        four_ways += [now[0]-1, now[1]]
        # left
        four_ways += [now[0], now[1]-1]
        # right
        four_ways += [now[0], now[1]+1]
        print(four_ways)
        # for i in four_ways:
        #     if not graph[i[0]][i[1]] == 0:
        #         if not visited[i[0]][i[1]]:
        #             queue.append(i)
        #             visited[i[0]][i[1]] = True
        answer += 1
    print(answer)

bfs(path, visited)
