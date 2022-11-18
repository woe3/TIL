import sys
n, m = map(int, sys.stdin.readline().split())
light = [[] for i in range(n+1)]
heavy = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    heavy[a].append(b)
    light[b].append(a)


def dfs(graph, v):
    global count
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(graph, i)

answer = 0

for i in range(1, n+1):
    count = 0
    visited = [False] * (n+1)
    dfs(light, i)
    if count > n//2:
        answer += 1


for i in range(1, n+1):
    count = 0
    visited = [False] * (n+1)
    dfs(heavy, i)
    if count > n//2:
        answer += 1

print(answer)