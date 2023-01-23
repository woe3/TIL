import sys
from collections import deque
# n, m = map(int, sys.stdin.readline().split())
# boss = [0] + list(map(int, sys.stdin.readline().split()))
# employee = [[] for _ in range(n+1)]
# compliment = [0] * (n+1)
# for i in range(1, n+1):
#     if boss[i] > 0:
#         employee[boss[i]].append(i)
    
# for _ in range(m):
#     i, w = map(int, sys.stdin.readline().split())
#     number = deque([i])
    
#     while number:
#         num = number.popleft()
#         compliment[num] += w
#         for k in employee[num]:
#             number.append(k)

# for i in range(1, n+1):
#     print(compliment[i], end = " ")
            
            


n, m = map(int, sys.stdin.readline().split())
boss = [0] + list(map(int, sys.stdin.readline().split()))

compliment = [0] * (n+1)
total_score = 0    
for _ in range(m):
    i, w = map(int, sys.stdin.readline().split())
    i = boss[i]
    while i > 0:
        compliment[i] -= w
        i = boss[i]

total_score = -compliment[1]
for i in range(1, n+1):
    compliment[i] += total_score
    

for i in range(1, n+1):
    print(compliment[i], end = " ")