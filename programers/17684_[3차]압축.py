from collections import deque

def solution(msg):
    answer = []
    # 사전 생성
    dictionary = {}
    # 문자 쪼개서 deque에 넣기
    msg = deque(list(msg))

    
    while msg:
        # 한 글자 빼기
        letters = msg.popleft()
        while msg:
            # 한 글자씩 더하면서 사전에 있는지 확인
            # 사전에 없을 때까지 더해가기
            temp = msg.popleft()
            letters += temp
            # 없다면 마지막 글자를 빼고 압축
            if not letters in dictionary:
                dictionary[letters] = len(dictionary) + 27
                letters = letters[:len(letters)-1]
                msg.appendleft(temp)
                break
            
        
        # 글자 수가 1개면 아스키 코드로 숫자 만들기
        # 2개 이상이라면 사전에서 숫자 찾기
        if len(letters) == 1:
            answer.append(ord(letters)-64)
        else:
            answer.append(dictionary[letters])

    return answer

print(solution("KAKAO"))