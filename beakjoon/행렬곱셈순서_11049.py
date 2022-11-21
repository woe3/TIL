import sys
n = int(sys.stdin.readline())
matrix = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    matrix.append([a, b])
dp = [[0] * n for _ in range(n)]
for row in range(1, n):
    for column in range(n):
        min_list = []
        # 계산 될 좌표
        y = column
        x = column+row
        # 좌표 두개
        print(y, x)
        for i in range(1, row + 1):
            # 더 해야할 두 개의 dp 죄표
            a, b = y, x - i
            c, d = y - i + row + 1, x
            print(a,b)
            print(c,d)
            #새로 계산되는 행렬
            new = matrix[a][0] * matrix[b][1] * matrix[d][1]
            print(matrix[a][0])
            print(matrix[b][1])
            print(matrix[d][1])
            print(new)
            new += dp[a][b]
            new += dp[c][d]
            min_list.append(new)
        print(min_list)
        dp[y][x] = min(min_list)
        print(dp)
        if x == n-1:
            break
print(dp[0][n-1])