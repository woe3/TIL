def solution(places):
    answer = []

    for place in places:
        check = True
        # 리스트로 변경
        place_list = []
        for i in place:
            place_list.append(list(i))

        # 응시자의 좌표만 추출
        person = []
        for i in range(len(place_list)):
            for j in range(len(place_list[0])):
                if place_list[i][j] == "P":
                    person.append([i, j])

        # 거리로 확인
        wrong_distance = []
        for i in range(len(person)):
            for j in range(i + 1, len(person)):
                i_y, i_x = person[i]
                j_y, j_x = person[j]
                distance = abs(i_y - j_y) + abs(i_x - j_x)
                if distance == 1:
                    check = False
                if distance <= 2:
                    wrong_distance.append([person[i], person[j]])

        # 테이블 확인
        if check:
            for seats in wrong_distance:
                y1, x1 = seats[0]
                y2, x2 = seats[1]
                if y1 > y2:
                    y_min = y2
                    y_max = y1
                else:
                    y_min = y1
                    y_max = y2

                if x1 > x2:
                    x_min = x2
                    x_max = x1
                else:
                    x_min = x1
                    x_max = x2

                for i in range(y_min, y_max + 1):

                    for j in range(x_min, x_max + 1):
    
                        if place_list[i][j] == "O":
                            check = False
                            break
                    if not check:
                        break
                if not check:
                    break

        if check:
            answer.append(1)
        else:
            answer.append(0)
    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])