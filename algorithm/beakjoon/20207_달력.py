import sys
sys.setrecursionlimit(10**8)


answer = 0
plan = []
max_y = 0
max_x = 0
n = int(sys.stdin.readline())
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    plan.append([s-1, e-1, e-s+1])
    if e > max_x:
        max_x = e

plan.sort(key=lambda x: (x[0], -x[2]))
print(plan)
cal = [[0] * max_x for _ in range(n)]
filled_day = [-1] * max_x
for days in plan:
    for i in range(n):
        put_determine = True
        for j in range(days[0], days[1]+1):
            if cal[i][j] != 0:
                put_determine = False
                break
        if put_determine:
            for j in range(days[0], days[1] + 1):
                cal[i][j] = 1
                filled_day[j] = i
            if i > max_y:
                max_y = i
            break
print(filled_day)
cnt = 0
find_max_y = -1
for i in filled_day:
    if i >= 0:
        cnt += 1
        if i > find_max_y:
            find_max_y = i
    else:
        answer += (find_max_y +1) * cnt
        cnt = 0
        find_max_y = -1
answer += (find_max_y +1) * cnt
print(answer)
