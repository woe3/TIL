from collections import deque

def solution(s):
    # 길이가 1인 경우 1 반환
    if len(s) == 1:
        return 1
    
    # 정답의 최대 크기 설정
    answer = 1000
    
    # 문자열을 하나씩 나누기
    s = list(s)
    
    # 문자열을 나눌 개수 설정
    for cut in range(1, len(s)//2+1):
        # cut의 숫자 대로 문자열 나누워서 2차원 배열로 만들기
        string = []
        if cut > 1:
            for start in range(0, len(s), cut):
                end = start + cut
                if end > len(s) :
                    end = len(s)
                string.append(s[start:end])
        else: string = s

        # 현재 리스트와 다음 리스트가 얼마나 같은지 계산
        temp_answer = 0
        string_index = 0
        while string_index < len(string):
            cnt = 1
            same = 1

            while string_index + cnt < len(string):
                if string[string_index] == string[string_index + cnt]:
                    same += 1
                    cnt += 1
                else:
                    break
            if same > 1:
                temp_answer += len(str(same))
            temp_answer += len(string[string_index])
            string_index += cnt
            
        if temp_answer < answer:
            answer = temp_answer
    return answer
