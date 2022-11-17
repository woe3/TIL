import sys
n, m = map(int, sys.stdin.readline().split())
floor = []
for _ in range(n):
    part = sys.stdin.readline().strip()
    floor.append([i for i in part])
count = 0
for i in range(n):
    for j in range(m):
        if floor[i][j] == 0:
            continue
        if floor[i][j] == '-':
            count += 1
            right = 0
            while True:
                floor[i][j+right] = 0
                right += 1
                if j+right == m or floor[i][j+right] != '-':
                    break
        elif floor[i][j] == '|':
            count += 1
            down = 0
            while True:
                floor[i+down][j] = 0
                down += 1
                if i+down == n or floor[i+down][j] != '|':
                    break

print(count)