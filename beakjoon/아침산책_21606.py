import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
in_and_out_door = sys.stdin.readline().strip()
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

door = [0] + [int(i) for i in in_and_out_door]
count = 0
def dfs(v, before = None):
    global count
    for i in graph[v]:
        if not before == i:
            if door[i] == 0:
                dfs(i, v)
            else:
                count += 1

for i in range(1, n+1):
    if door[i] == 1:
        dfs(i)
        
        
        
print(count)

