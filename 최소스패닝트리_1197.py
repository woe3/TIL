import sys

v, e = map(int, sys.stdin.readline().split())

edges = []
for _ in range(e):
    edges.append(list(map(int, sys.stdin.readline().split())))

parent = [i for i in range(v+1)]

edges.sort(key = lambda x : x[2])

def find(x):
    if not x == parent[x]:
        return find(parent[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
for a, b, c in edges:
    if not find(a) == find(b):
        union(a, b)
        answer += c
        

print(answer)