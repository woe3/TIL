import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
infinite = 9999999999
cost = [infinite] * (n+1)
for _ in range(m):
    a, b, c= map(int, sys.stdin.readline().split())
    graph[a].append([c, b])

s, e = map(int, sys.stdin.readline().split())
que = [[0, s]]


def bfs(count = 0):
    cost[s] = 0
    now = heapq.heappop(que)
    for i in graph[now[1]]:
        if cost[i[1]] > i[0]:
            heapq.heappush(que, i)
            cost[i[1]] = i[0]
    while que:
        now = heapq.heappop(que)
        for i in graph[now[1]]:
            if cost[i[1]] > now[0] + i[0]:
                heapq.heappush(que, [now[0] + i[0], i[1]])
                cost[i[1]] = now[0] + i[0]
                if i[1] == e:
                    count +=1
        if count == 2:
            return
bfs()
print(cost[e])
