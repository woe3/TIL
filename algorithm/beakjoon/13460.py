import sys
n, m = map(int, sys.stdin.readline().split())
map_o = []
red = 0
blue = 0

for i in range(n):
    temp = []
    temp_map = sys.stdin.readline().strip()
    for j in range(m):
        temp.append(temp_map[j])
        if temp[j] == "R":
            red = [i, j]
        elif temp[j] == "B":
            blue = [i, j]
        
    map_o.append(temp)

# 오른쪽, 왼쪽, 위, 아래
movement = [[0, 1], [0, -1], [-1, 0], [1, 0]]
min_count = 11

def move(map, Rlocation, Blocation, direction, count):
    global min_count

    if count > 9:
        return
    ry, rx = Rlocation
    map[ry][rx] = '.'
    m_y, m_x = direction
    
    by, bx = Blocation
    
    
    
    
    
    
    meet = 0
    while map[ry + m_y][rx + m_x] != '#':
        if map[ry + m_y][rx + m_x] == 'O':
            while map[by + m_y][bx + m_x] != '#':
                if map[by + m_y][bx + m_x] == 'O':
                    return
                by, bx = by + m_y, bx + m_x
            min_count = min(count + 1, min_count)
            return
        elif map[ry + m_y][rx + m_x] == 'B':
            meet += 1
        ry, rx = ry + m_y, rx + m_x
    if meet > 0:
        ry, rx = ry - m_y, rx - m_x
    
    map[ry][rx] = "R"


    
    
    meet = 0
    while map[by + m_y][bx + m_x] != '#':
        if map[by + m_y][bx + m_x] == 'O':
            return
        elif map[by + m_y][bx + m_x] == 'R':
            meet += 1
        by, bx = by + m_y, bx + m_x
    if meet:
        by, bx = by - m_y, bx -m_x
    map[by][bx] = "B"
    
    if [ry, rx] == Rlocation and [by, bx] == Blocation:
        return
    

    for i in movement:
        j = [-i[0], -i[1]]
        if j == direction:
            continue
        else:
            for k in map:
                print(k)
            print()
            move(map, [ry, rx], [by, bx], i, count + 1)

for i in movement:
        move(map_o, red, blue, i, 0)
if min_count == 11:
    print(-1)
else:
    print(min_count)