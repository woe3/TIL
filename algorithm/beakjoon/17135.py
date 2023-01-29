import sys
from itertools import combinations
from collections import deque
n, m, d = map(int, sys.stdin.readline().split())
castle = [i for i in range(m)]
enemy = []
for _ in range(n):
    enemy.append(list(map(int, sys.stdin.readline().split())))

location_of_archer = list(combinations(castle, 3))


answer = 0
killed = 0

def shoot(location, d):
    global killed
    global enemy
    que = deque([n-1, location])  
    que.append(1)
    visit = [[0]* m for _ in range(n)]
    
    while que:
        new = que.popleft()
        if len(new) == 1:
            if new == d:
                return
            else:
                que.append(new+1)
        if enemy[new[0]][new[1]] > 0:
            enemy[new[0]][new[1]] = 0
            killed += 1
            return
        else:
            visit[new[0]][new[1]]  = 1
            if not visit[new[0]][new[1]-1]:
                que.append([new[0], new[1]-1])
            if not visit[new[0]-1][new[1]]:
                que.append([new[0]-1, new[1]])
            if not visit[new[0]][new[1]+1]:
                que.append([new[0], new[1]+1])
            
for x, y, z in location_of_archer:
    for i in range(n):
               