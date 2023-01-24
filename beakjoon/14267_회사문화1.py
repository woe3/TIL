# import sys
# import heapq

# n, m = map(int, sys.stdin.readline().split())
# boss = [0] + list(map(int, sys.stdin.readline().split()))
# employee = [[] for _ in range(n+1)] #직원이 가지는 직속부하 그래프
# score = [0] * (n+1) # 직원들의 칭찬 점수 기록
# compliment = [] # 누가 칭찬을 받았는지 i, w의 리스트

# for i in range(1, n+1):
#     if boss[i] > 0:
#         employee[boss[i]].append(i)

# for _ in range(m):
#     i, w = map(int, sys.stdin.readline().split())
#     heapq.heappush(compliment, (i, w))
    
# def dfs (num, point = 0):

#     if not employee[num]:
#         return
    
#     for i in employee[num]:
#         score[i] += point
#         if i == compliment[0][0]:
#             new_point = compliment[0][1]
#             score[i] += new_point
#             heapq.heappop(compliment)
#             dfs(i, point + new_point)
#         else:
#             dfs(i, point)
            
        

# dfs(1)

# for i in range(1, n+1):
#     print(score[i], end = " ")
            
            


import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
boss = [0] + list(map(int, sys.stdin.readline().split()))
employee = [[] for _ in range(n+1)] #직원이 가지는 직속부하 그래프
score = [0] * (n+1) # 직원들의 칭찬 점수 기록
compliment = [] # 누가 칭찬을 받았는지 i, w의 리스트

for i in range(1, n+1):
    if boss[i] > 0:
        employee[boss[i]].append(i)

for _ in range(m):
    i, w = map(int, sys.stdin.readline().split())
    heapq.heappush(compliment, (i, w))
    
def dfs (num, k, point = 0):
    
    if num == k[0]:
        point += k[1]
        score[num] += k[1]
        if compliment:
            k = heapq.heappop(compliment)
        else:
            k = [0, 0]
    
    for i in employee[num]:
        score[i] += point
        
        dfs(i, k, point)

dfs(1, heapq.heappop(compliment))

for i in range(1, n+1):
    print(score[i], end = " ")