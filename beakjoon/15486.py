import sys
n = int(sys.stdin.readline())

table = [[0,0]]
for _ in range(n):
    d, cost = map(int, sys.stdin.readline().split())
    table.append([d, cost])

days = [ 0 for _ in range(n+2)]

# 뒤에서부터 계산
for i in range(n, 0, -1):
    # 남은 시간이 상담시간과 같거나 더 많을 때
    if  table[i][0] <= n - i+1:
        # 현재의 상담시간만큼 뒤로 간 후 계산하려는 상담시간을 더하고
        # 하루 뒤 상담 페이를 확인한 후 둘을 비교해 더 큰 값을 넣는다.
        days[i] = max(days[i + table[i][0]] + table[i][1], days[i+1])
        
    # 남은 시간이 상담시간보다 짧으면 하루 뒤 상담 가격을 그대로 이어받는다.
    else:
        days[i] = days[i+1]

    


print(days[1])