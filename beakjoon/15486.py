import sys
n = int(sys.stdin.readline())

table = [[0,0]]
for _ in range(n):
    d, cost = map(int, sys.stdin.readline().split())
    table.append([d, cost])

days = [[0, 0] for _ in range(n+1)]

last_time = 0
last_pay = 0

for i in range(1, n+1):
    if days[i - 1][0] <= 0:
        days[i][0], days[i][1] = table[i][0], days[i][1] + table[i][1]
        last_time, last_pay = table[i]
    else:
        if last_pay + table[i][0]