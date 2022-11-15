import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
result = 0
def dfs(graph, start, visited):
    global result
    visited[start] = True
    result += 1
    for i in graph[start]:
        if not visited[i]:            
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(result-1)