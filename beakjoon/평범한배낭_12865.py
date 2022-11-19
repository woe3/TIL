import sys
n, k = map(int, sys.stdin.readline().split())
item = []
for _ in range(n):
    item.append(list(map(int, sys.stdin.readline().split())))
dp = [0] * (k + 1)
item.sort(reverse=True)

for i in range(k, 0, -1):
    for w, v in item:
        
        if i >= w:
            if w == i - w:
                new_v = v
            else:
                new_v = v + dp[i - w]
            if new_v > dp[i]:
                dp[i] = new_v
            
    print(dp)
print(dp[-1])