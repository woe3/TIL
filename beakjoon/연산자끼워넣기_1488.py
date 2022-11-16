import sys
n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))
answers = []
def dfs(operator, answer = number[0], index = 1):
    if index == n:
        return
    for i in range(4):
        if operator[i] > 0:
            print(i)
            operator[i] -= 1
            if i == 0:
                answer += number[index]
            elif i == 1:
                answer -= number[index]
            elif i == 2:
                answer *= number[index]
            elif i == 3:
                answer /= number[index]
            index += 1
            dfs(operator, answer, index)
                   
    answers.append(answer)

dfs(operator)
print(answers)