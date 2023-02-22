def solution(book_time):
    # 시간을 분으로 변경
    time_to_min = []
    for t in book_time:
        temp_min = []
        # 시작 시간
        s, e = map(int, t[0].split(":"))
        temp_min.append(s * 60 + e)
        # 끝나는 시간은 청소 시간 포함해서 10분 추가
        s, e = map(int, t[1].split(":"))
        temp_min.append(s * 60 + e + 10)
        # 리스트에 넣기
        time_to_min.append(temp_min)

    # (24시간) * (60분) + (10분의 청소시간) 개의 인덱스를 가진 리스트 생성
    time_check = [0] * (60 * 24 + 10)
    # 최대 필요 방개수 카운트 변수
    max_rooms = 0

    # 전체 시간 리스트를 순회하면서 time_check를 채운다.
    for time in time_to_min:
        s, e = time
        for i in range(s, e):
            time_check[i] += 1
            # 채우면서 최대 방 개수도 함께 확인
            if time_check[i] > max_rooms:
                max_rooms = time_check[i]

    # 최대 방 개수 리턴
    return max_rooms

solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]])
solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])