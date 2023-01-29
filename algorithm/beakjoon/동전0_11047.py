import sys
n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    a = int(sys.stdin.readline())
    coin.append(a)

answer = 0
for i in range(n-1, -1, -1):
    while True:
        if k >= coin[i]:
            k -= coin[i]
            answer += 1
        else:
            break
    if k ==0:
        break
print(answer)
    