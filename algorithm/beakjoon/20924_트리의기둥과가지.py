import sys
sys.setrecursionlimit(2_000_000)

n, r = map(int, sys.stdin.readline().split())
graph_temp = [[] for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
branch = []
for _ in range(n - 1):
    a, b, d = map(int, sys.stdin.readline().split())
    graph_temp[a].append([b, d])
    graph_temp[b].append([a, d])


def makeTree(root):
    visited[root] = True
    for i in graph_temp[root]:
        if not visited[i[0]]:
            graph[root].append(i)
            makeTree(i[0])


def findGigaRoot(root):
    height = 0
    while len(graph[root]) == 1:
        height += graph[root][0][1]
        root = graph[root][0][0]
    return [height, root]


def findBranch(node, length=0):
    if not graph[node]:
        branch.append(length)
        return
    for i in graph[node]:
        findBranch(i[0], length + i[1])


makeTree(r)
h, r = findGigaRoot(r)
findBranch(r)
longest = max(branch)
print(h, longest)