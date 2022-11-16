import sys
from collections import deque
sys.setrecursionlimit(10**6)
n, m, k, x =map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    
visited = [False] * (n + 1)
que = deque([x])
visited[x] = True



def bfs(length = 1, count = k):
    if count == 0:
        
        return
    for _ in range(length):
        now = que.popleft()
        for i in graph[now]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
    length = len(que)
    count -= 1
    bfs(length, count)
    
bfs()

if que:
    result = [i for i in que]
    result.sort()
    for i in result:
        print(i)
else: print(-1)