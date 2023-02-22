def solution(k, tangerine):
    answer = 0

    # 과일을 세는 딕셔너리 만들기
    count = {}

    # 딕셔너리에 삽입
    for t in tangerine:
        if t in count:
            count[t] += 1
        else:
            count[t] = 1
    # 과일 개수가 많은 순서로 딕셔너리를 튜플 형식으로 정렬
    # ex) [(1, 2), (3, 1)]  (과일 종류, 과일 개수)
    count_list = sorted(count.items(), key=lambda x:-x[1])

    # 앞부터 k를 개수 만큼 빼기, 뺄 때마다 answer에 종류 추가
    # k가 0 이하인 경우 모두 골랐으므로 끝내기
    for i in count_list:
        k -=i[1]
        answer += 1
        if k < 1:
            break
    return answer