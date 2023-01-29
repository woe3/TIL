import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
infinite = 9999999999
cost = [infinite] * (n+1)
for _ in range(m):
    a, b, c= map(int, sys.stdin.readline().split())
    graph[a].append((c, b))

s, e = map(int, sys.stdin.readline().split())
que = []
heapq.heappush(que, (0, s))
cost[s] = 0

def bfs():
    
    while que:
        now = heapq.heappop(que)
        if cost[now[1]] < now[0]:
            continue
        for i in graph[now[1]]:
            if cost[i[1]] > now[0] + i[0]:
                heapq.heappush(que, (now[0] + i[0], i[1]))
                cost[i[1]] = now[0] + i[0]
                
bfs()
print(cost[e])