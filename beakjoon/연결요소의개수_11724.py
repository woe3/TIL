import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)
answer = 0
for node in range(1, n+1):
    if not visited[node]:
        answer +=1
        dfs(graph, node, visited)

print(answer)