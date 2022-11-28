import sys
y , x = map(int, sys.stdin.readline().split())

mapping = []
for _ in range(y):
    a = sys.stdin.readline().strip()
    mapping.append(list(a))


y_range = []
x_range = []
x_move = [0, 0, 1, -1]
y_move = [1, -1, 0, 0]
drowning_list = []
for i in range(y):
    for j in range(x):
        if mapping[i][j] == 'X':
            count = 0
            for k in range(4):
                new_y = i - y_move[k]
                new_x = j - x_move[k]
                if new_y > y-1 or new_y < 0 or new_x > x-1 or new_x < 0:
                    count += 1
                elif mapping[new_y][new_x] == '.':
                    count += 1
            if count > 2:
                drowning_list.append([i, j])
            else:
                y_range.append(i)
                x_range.append(j)
            
for i, j in drowning_list:
    mapping[i][j] = '.'
x_1 = min(x_range)
x_2 = max(x_range)
for i in range(y_range[0], y_range[-1] + 1):
    answer = mapping[i][x_1: x_2 + 1]
    for j in answer:
        print(j, end = '')
    print()