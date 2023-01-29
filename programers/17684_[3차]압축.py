def solution(msg):
    answer = []
    # 사전 생성
    dictionary = {}
    # 문자 쪼개기
    msg = list(msg)
    i = 0
    while i < len(msg):
        letters = msg[i]
        for j in range(i+1, len(msg)):
            letters += msg[j]
            print(letters)
            i = j
            if not letters in dictionary:
                dictionary[letters] = len(dictionary) + 27
                if len(letters) > 1:
                    letters = letters[:len(letters)-1]
                break
            
        
        
        # print(letters)
        if len(letters) == 1:
            answer.append(ord(letters)-64)
        else:
            answer.append(dictionary[letters])

    return answer

print(solution("KAKAO"))