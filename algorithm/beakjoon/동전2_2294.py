import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]

que = deque([[0,0]])
#(cost, count)
combination = [0] * (k + 1)
def bfs():
    while que:
        now = que.popleft()
        for i in coin:
            cost = now[0] + i
            if cost < k and combination[cost] == 0:
                que.append([cost, now[1]+1])
                combination[cost] = 1
            elif cost == k:
                print(now[1]+1)
                return    
    print(-1)
bfs()