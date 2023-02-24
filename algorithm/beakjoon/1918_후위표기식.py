import sys
from collections import deque

formula = sys.stdin.readline().strip()

# 정답 출력 스택
answer = deque()

# 연산자 스택
stack = deque()

# 중위 표기식 스택
formula = deque(list(formula))

# 연산자 우선 순위
priority = {"(": 0, "*": 1, "/": 1, "+": 2, "-": 2, ")": 4}


while formula:
    # print(answer)
    # print(stack)
    # print()
    n = formula.popleft()

    # 피연산자라면 바로 정답 스택에 삽입
    if not n in priority:
        answer.append(n)
    # 괄호가 닫혔다면 마지막으로 열린 괄호까지 연산자를 정답 스택에 삽입
    # 정답 스택에 삽입 할 때 괄호는 빼고 삽입한다.
    elif priority[n] == 4:
        while priority[stack[-1]] != 0:
            answer.append(stack.pop())
        stack.pop()
    # 연산자 일 때
    else:
        # 연산자 스택에 원소가 추가되는 것이 종료 조건이다.
        while True:
            # 연산자 스택에 원소가 있을 때
            if stack:
                # 연산자 스택의 마지막 원소가 현재 연산자보다 우선 순위가 낮을 때,
                # 연산자 스택의 마지막 원소가 열린 괄호 일 때
                # 스택에 추가만 한다.
                if priority[stack[-1]] > priority[n] or priority[stack[-1]] == 0:
                    stack.append(n)
                    break
                # 나머지의 경우 연산자 스택의 원소를 정답 스택에 삽입.
                else:
                    answer.append(stack.pop())
            # 원소가 없다면 그냥 삽입.
            else:
                stack.append(n)
                break
# 연산자 스택에 남아 있는 원소들을 차례대로 정답 스택에 삽입.
while stack:
    answer.append(stack.pop())

# 정답 스택의 원소를 하나의 string으로 합쳐서 출력
print("".join(answer))
