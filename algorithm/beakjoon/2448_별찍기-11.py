import sys
from collections import deque
n = int(sys.stdin.readline())

star_tree = [[" "]*n*2 for _ in range(n)]

que = deque([(6*n//3)//2-1])


def star(n, que, cnt = 0):


    while que:
        while que:
            start = que.popleft()
            star_tree[cnt][start] = "*"
            
            star_tree[cnt+1][start-1] = "*"
            star_tree[cnt+1][start+1] = "*"
            
            for i in range(start-2, start+3):
                star_tree[cnt+2][i] = "*"
        if cnt+3 == n:
            break
        cnt += 2
        for i in range(1, len(star_tree[cnt])-1):
            if star_tree[cnt][i] == " ":
                if star_tree[cnt][i-1] == " " and star_tree[cnt][i+1] == "*":
                    que.append(i)
                if star_tree[cnt][i-1] == "*" and star_tree[cnt][i+1] == " ":
                    que.append(i)
        cnt += 1

    
    
star(n, que)
for i in star_tree:
    print("".join(i))