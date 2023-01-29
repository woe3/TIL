import sys
sys.setrecursionlimit(10**6)
k = int(sys.stdin.readline())
count = ['YES'] * k
check = True

def dfs(v, group = -1):
    global check
    visited[v] = group
    for i in graph[v]:
        if not visited[i]:
            dfs(i, -group)
        elif visited[i] == visited[v]:
            check = False
    
for case_number in range(k):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    for i in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0] * (v+1)
    for i in range(1, v+1):
        if not visited[i]:
            dfs(i)
        if not check:
            check = True
            count[case_number] = "NO"
            break
    
for i in count:
    print(i)