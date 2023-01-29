import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
parent = [0] * (n+1)
visited = [False] * (n+1)
def find_root(graph, root, visited, parent):
    queue = deque([root])
    for i in graph[root]:
        parent[i] = root
    visited[root] = True

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            for j in graph[i]:
                if not visited[j]:
                    parent[j] = i
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            
    
find_root(graph, 1, visited, parent)
for i in range(2, n+1):
    print(parent[i])