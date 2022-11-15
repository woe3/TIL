import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()
visited_bfs = [False] * (n+1)
visited_dfs = [False] * (n+1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        now = queue.popleft()
        print(now, end = " ")

        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)
