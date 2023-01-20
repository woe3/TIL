from collections import deque
def solution(queue1, queue2):
    # deque로 만들기
    que1 = deque(queue1)
    que2 = deque(queue2)
    
    # 합을 미리 구한다.
    sum1 = sum(que1)
    sum2 = sum(que2)
    answer = -1
    repeatation = 0
    
    # 3배만큼 반복
    while repeatation < len(queue1) * 3:
        
        # 큰쪽에서 작은 쪽으로 원소를 이동 시킨다.
        # 이동되는 원소의 크기만큰 sum을 더하고 빼준다.
        if sum1 > sum2:
            popping = que1.popleft()
            que2.append(popping)
            sum2 += popping
            sum1 -= popping
        elif sum2 > sum1:
            popping = que2.popleft()
            que1.append(popping)
            sum1 += popping
            sum2 -= popping
        else:
            answer = repeatation
            break
        repeatation += 1
    return answer