import sys
n = int(sys.stdin.readline())

stars = [[" "] * n for _ in range(n)]

def recursion(y, x, n):
    if n == 3:
        for i in range(y-3, y):
            for j in range(x-3, x):
                stars[i][j] = "*"
        stars[y-2][x-2] = " "
    else:
        new_n = n//3
        for i in range(y-(new_n*2), y+1, new_n):
            for j in range(x-(new_n*2), x+1, new_n):
                if i == y-new_n and j == x-new_n:
                    continue
                recursion(i, j, new_n)

recursion(n, n, n)
for star in stars:
    print("".join(star))
    

