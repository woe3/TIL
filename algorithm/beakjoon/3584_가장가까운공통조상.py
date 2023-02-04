import sys

t = int(sys.stdin.readline())
answer = []
for _ in range(t):
    n = int(sys.stdin.readline())
    parents = set()
    graph = [0] * (n+1)
    for _ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        graph[b] = a

    node_1, node_2 = map(int, sys.stdin.readline().split())

    print(graph)
    while node_1:
        parents.add(node_1)
        node_1 = graph[node_1]

    while node_2:
        if node_2 in parents:
            answer.append(node_2)
            break
        node_2 = graph[node_2]

for i in answer:
    print(i)
