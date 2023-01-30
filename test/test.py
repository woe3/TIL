import sys

n, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    a, b, d = map(int, sys.stdin.readline().split())
    graph[a].append([b, d])

print(graph)