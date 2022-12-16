import sys
m, n = map(int, sys.stdin.readline().split())
mapping = []
for _ in range(m):
    mapping.append(list(map(int, sys.stdin.readline().split())))
blank_map = [[0] * n for _ in range(m)]
blank_map[0][0] = 1
movement = [[0, 1], [0, -1], [-1, 0], [1, 0]]
count = 0

def move(y, x):
    global blank_map
    global count
    if (y == m-1) and (x == n-1):
        count += 1
    for i in movement:
        my = y + i[0]
        mx = x + i[1]
        if my < 0 or my > m-1:
            continue
        if mx < 0 or mx > n-1:
            continue
        
        if mapping[y][x] > mapping[my][mx]:
            if blank_map[my][mx] > 0:
                count += 1
            else:
                blank_map[my][mx] += 1
                move(my,mx)
        
            
move(0,0)
# for i in blank_map:
#     print(i)
# print()
print(count)