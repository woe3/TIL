import sys
import heapq
# 재귀 깊이 최대로 만들기
sys.setrecursionlimit(1000000)

n, m = map(int, sys.stdin.readline().split())
boss = [0] + list(map(int, sys.stdin.readline().split()))
employee = [[0] for _ in range(n+1)] #직원이 가지는 직속부하 그래프
score = [0] * (n+1) # 직원들의 칭찬 점수 기록

# 직원의 직속 부하 그래프 만들기
for i in range(1, n+1):
    if boss[i] > 0:
        employee[boss[i]].append(i)

# 칭찬 받은 직원의 부하 그래프의 0번 인덱스에 칭찬 점수 기록
for _ in range(m):
    i, w = map(int, sys.stdin.readline().split())
    employee[i][0] += w
    
# dfs로 탐색하면서 칭찬 점수가 있는 직원이 있다면 포인트를 더하고 dfs 진행
def dfs (num = 1, point = 0):
    if len(employee[num]) == 1:
        return
    for i in range(1, len(employee[num])):
        new_num = employee[num][i]
        score[new_num] += (point + employee[new_num][0])
        dfs(new_num, point + employee[new_num][0])

dfs()

for i in range(1, n+1):
    print(score[i], end = " ")