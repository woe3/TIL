import sys

n, k = map(int, sys.stdin.readline().split())
electronic = list(map(int, sys.stdin.readline().split()))
multi_tap = [[0,102] for _ in range(n)]

answer = 0

for i in range(k):
    count = False
    for j in range(n):
        index = 101
        for l in range(i+1, k):
            if electronic[l] == electronic[i]:
                index = l
                break
        if multi_tap[j][0] == electronic[i]:
            count = True
            multi_tap[j][1] = index
    if not count:
        
        if not multi_tap[-1][0] == 0:
            answer += 1
        multi_tap[-1] = [electronic[i], index]
    multi_tap.sort(key = lambda x : x[1])



print(answer)
