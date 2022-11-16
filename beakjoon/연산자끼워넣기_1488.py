import sys
n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))
answers = []
def dfs(operator, answer = number[0], index = 1):
    
        dfs(operator, answer, index)
                   
    answers.append(answer)

dfs(operator)
print(answers)