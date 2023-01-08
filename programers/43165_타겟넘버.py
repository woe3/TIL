answers = []

# 재귀로 돌면서 -1과 1 조합을 만듬.
# 만들어진 조합을 numbers에 곱하기해서 더한 값을 answers에 리스트로 추가
def plus_minus(n, numbers, answer):
    if n == 0:
        answers.append(answer)
        return answer
    
    num = [1, -1]
    for i in num:
        plus_minus(n-1, numbers, answer + numbers[n-1]*i)

def solution(numbers, target):
    
    plus_minus(len(numbers), numbers, 0)
    answer = 0
    
    # target과 answers의 원소 값이 같으면 정답 +1
    for i in answers:
        if i == target:
            answer += 1
            
    return answer