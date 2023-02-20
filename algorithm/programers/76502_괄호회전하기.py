from collections import deque


def solution(s):
    # 정답은 0부터 시작
    answer = 0

    # 2중으로 괄호 리스트를 만듬
    duoble_s = list(s) * 2

    # 괄호 리스트의 원래 길이만큼 for 실행
    for i in range(len(s)):
        # 회전 하는 괄호 리스트
        temp_s = duoble_s[i:i + len(s)]

        # 회전시킨 괄호 리스트 판별
        determine = deque()
        bracket = [")", "]", "}"]
        for b in temp_s:
            # 스택 마지막 원소와 현재 원소를 비교 해서 매치 되면 제거
            if len(determine) > 0 and b in bracket:
                if determine[-1] == "(" and b == ")":
                    determine.pop()
                elif determine[-1] == "[" and b == "]":
                    determine.pop()
                elif determine[-1] == "{" and b == "}":
                    determine.pop()
            # 아니라면 현재 원소를 삽입
            else:
                determine.append(b)
            print(determine)
        # 스택이 비어 있으면 괄호가 모두 매치 된것이므로
        # 정답에 1 더하기
        if not determine:
            answer += 1

    return answer