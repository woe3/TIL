def solution(line):
    coordinate = []
    x_list = []
    y_list = []

    # 모든 교점을 확인해서 좌표 리스트 추가한다.
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            x_1, y_1, c_1 = line[i]
            x_2, y_2, c_2 = line[j]
            if (x_1*y_2 - x_2*y_1) == 0:
                continue
            x = (y_1*c_2 - y_2*c_1)/(x_1*y_2 - x_2*y_1)
            y = (c_1*x_2 - x_1*c_2)/(x_1*y_2 - x_2*y_1)
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                coordinate.append((x, y))
                
                
    # 좌표 리스트에서 중복되는 값을 제외 시키고 x와 y 리스트를 따로 만들어 준다.             
    coordinate =list(set(coordinate))
    for x, y in coordinate:
        x_list.append(x)
        y_list.append(y)
    # x와 y 리스트를 이용해서 최대 최소 좌표를 찾는다.
    max_x = max(x_list)
    min_x = min(x_list)
    max_y = max(y_list)
    min_y = min(y_list)
    
    # 별을 찍기위한 전체 가로세로 길이를 구한다.
    length_x = max_x - min_x + 1
    length_y = max_y - min_y + 1
    stars = [["."] * (length_x) for _ in range(length_y)]
    
    # 좌표 리스트를 참조해서 교점에 별을 찍는다.
    for i in coordinate:
        x, y = i
        # 실제 좌표 값과 star의 좌표에 대입하기 위해서 
        # 각 좌표의 최소 값을 빼주면서 초기화를 해준다.
        x = x - min_x
        y = y - min_y
        stars[y][x] = "*"
    
    # 2차원 배열을 1차원 바열로 합쳐준다.
    for i in range(len(stars)):
        stars[i] = "".join(stars[i])
    
    # 실제 좌표는 위로 갈 수록 증가한다.
    # 따라서 가장 아래 좌표는 가장 위로 가주어야 한다.
    answer = []    
    for i in range(len(stars)-1, -1, -1):
        answer.append(stars[i])
    return answer