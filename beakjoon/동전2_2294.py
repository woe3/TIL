import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]

que = deque([[0,0]])
#(cost, count)

def bfs():
    while que:
        now = que.popleft()
        if now[0] == k:
            print(now[1])
            return
        for i in coin:
            cost = now[0] + i
            if cost <= k:
                que.append([cost, now[1]+1])
              
    print(-1)
bfs()