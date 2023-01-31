import sys
sys.setrecursionlimit(10**6)

nodes = []
while True:
    try:
        nodes.append(int(sys.stdin.readline()))
    except:
        break

graph = {}


def restoreTree(nodes_list):
    graph[nodes_list[0]] = [0, 0]
    seperation = len(nodes_list)
    if len(nodes_list) == 1:
        return
    for r in range(1, seperation):
        if nodes_list[r] > nodes_list[0]:
            graph[nodes_list[0]][1] = nodes_list[r]
            seperation = r
            break
    for l in range(1, seperation):
        if nodes_list[l] < nodes_list[0]:
            graph[nodes_list[0]][0] = nodes_list[l]
            break

    if nodes_list[1:seperation]:
        restoreTree(nodes_list[1:seperation])
    if nodes_list[seperation:]:
        restoreTree(nodes_list[seperation:])


def postorder(root):
    if root == 0:
        return
    postorder(graph[root][0])
    postorder(graph[root][1])
    print(root)


restoreTree(nodes)
postorder(nodes[0])
