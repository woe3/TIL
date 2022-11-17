import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
virus = []
new = [[] for _ in range(k + 1)] # k개 종류의 바이러스 존재

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    line = list(map(int, input().split()))
    virus.append(line)
    for j in range(n): # 처음 바이러스 상태 저장
        if line[j]: new[line[j]].append((i, j))

s, x, y = map(int, input().split())

def bfs(k, new_virus):
    queue = deque()
    while new_virus:
        queue.append(new_virus.pop())
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:  # 좌표 범위 유효성 판단
                continue
            if virus[nx][ny] == 0:
                virus[nx][ny] = k
                new_virus.append((nx, ny))

for _ in range(s):
    for i in range(1, k + 1):
        bfs(i, new[i])

print(virus[x-1][y-1])