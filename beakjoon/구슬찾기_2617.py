import sys
n, m = map(int, sys.stdin.readline().split())
light = [[] for i in range(n+1)]
heavy = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    heavy[a].append(b)
    light[b].append(a)
count = 0
for i in heavy:
    if len(i) > 1:
        count += 1

for i in light:
    if len(i) > 1:
        count += 1

print(count)