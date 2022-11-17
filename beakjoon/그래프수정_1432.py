import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
sub_indegree = [0] *(n+1)
for i in range(1, n+1):
    a = sys.stdin.readline().strip()
    for j in range(1, n+1):
        if a[j-1] == "1":
            graph[i].append(j)
            indegree[j] += 1
            sub_indegree[j] += 1



def topology_sort():
    result = [[] for i in range(max(indegree)+1)]
    que = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            que.append(i)
    count = 1
    while que:
        
        now = que.popleft()
        result[sub_indegree[now]].append([now-1, count])
        count += 1
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                print(i)
                que.append(i)
    print(result)
    answer = [0] * n
    for i in result:
        i.sort(key = lambda x : x[1])
        for x, v in i:
            answer[x] = v
    print(answer)
topology_sort()