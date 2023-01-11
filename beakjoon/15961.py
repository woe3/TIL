import sys
from collections import deque

n, d, k, c = map(int, sys.stdin.readline().split())

sushi = []
for _ in range(n):
    sushi.append(int(sys.stdin.readline()))

answer = 0
temp_answer = 0
cnt = deque()
coupon = 1
dishes = [0] * (d+1)
for i in range(n+k):
    if i >= n:
        i -= n
    dishes[sushi[i]] += 1
    cnt.append(sushi[i])
    if dishes[sushi[i]] == 1:
        temp_answer += 1
    if len(cnt) > k:
        out = cnt.popleft()
        dishes[out] -= 1
        if dishes[out] == 0:
            temp_answer -= 1
    if dishes[c] == 0:
        coupon = 1
    else:
        coupon = 0
    if temp_answer+coupon > answer:
        answer = temp_answer + coupon


print(answer)