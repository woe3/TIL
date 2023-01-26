import sys
sys.setrecursionlimit(100000)
n, r, q = map(int, sys.stdin.readline().split())
# answer = [0] * (n + 1)
graph = [[False] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
querys2 = []
querys = {}
for _ in range(q):
    node = int(sys.stdin.readline())
    querys[node] = 0
    querys2.append(node)
    graph[node][0] = True

visited = [False] * (n + 1)

def dfs(v, query_list = []):    
    visited[v] = True
    query = 0
    if graph[v][0] == True:
        query = v
        querys[v] += 1
    for k in query_list:
        querys[k] += 1

    for i in range(1, len(graph[v])):
        if not visited[graph[v][i]]:
            if query:
                dfs(graph[v][i], query_list + [query])
            else:
                dfs(graph[v][i], query_list)
dfs(r)

for i in querys2:
    print(querys[i])
