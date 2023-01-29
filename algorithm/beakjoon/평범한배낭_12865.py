import sys
n, k = map(int, sys.stdin.readline().split())
item = []
for _ in range(n):
    item.append(list(map(int, sys.stdin.readline().split())))
dp = [0 for _ in range(k+1)]
item.sort()

for i in range(n):
    w = item[i][0]
    v = item[i][1]
    for j in range(k, 0, -1):
        if j - w >= 0:
            if dp[j] < v+ dp[j - w]:
                dp[j] = v+ dp[j - w]
print(dp[-1])