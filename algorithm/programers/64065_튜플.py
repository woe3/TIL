import heapq
import re


def solution(s):
    # s가 string이므로 숫자만 추출해서 int로 변경
    tuple_list = list(map(int, re.findall(r'\d+', s)))
    answer = []
    heap = []
    element = [0] * 100001
    
    # 해당되는 인덱스 위치에 숫자의 개수 카운트
    for i in tuple_list:
        element[i] += 1
    
    # 0이 아닌 값을 (카운드, 인덱스)를 묶어서 힙큐에 넣음
    # 최소 힙 이기 때문에 카운트에 (* -1)을 해줌
    for i in range(100001):
        if element[i]:
            heapq.heappush(heap, (-element[i], i))

    # 힙큐에서 순차적으로 추출하면서 정답에 추가
    for _ in range(len(heap)):
        answer.append(heapq.heappop(heap)[1])
    
    return answer