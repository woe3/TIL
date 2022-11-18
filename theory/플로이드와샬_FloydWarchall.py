
# n: 노드의 수
def floyd_warchall(cost, n):

    # k: 거쳐가는 노드
    for k in range(n):
        # i: 출발 노드
        for i in range(n):
            # j: 도착 노드
            for j in range(n):
                # k를 거쳐가는 거리와 바로 가는 거리를 비교해서 적은 값으로 교체
                if cost[i][k] + cost[k][j] < cost[i][j]:
                    cost[i][j] = cost[i][k] + cost[k][j]
    
    #  출력
    for i in cost:
        for j in i:
            print(j, end = ' ')
        print()

n = 4
inf = 99999999
cost = [
    [0, 5, inf, 8],
    [7, 0, 9, inf],
    [2, inf, 0, 4],
    [inf, inf, 3, 0]
]

floyd_warchall(cost, n)

# 3중 for문이 들어가기 때문에
# 플로이드 와샬의 시간복잡도는 n^3 이다