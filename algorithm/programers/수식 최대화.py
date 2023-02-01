from itertools import permutations
def solution(expression):
    answer = 0
    expression = list(expression)
    new_ex = []
    temp_num = ""
    cases = list(permutations([0, 1, 2]))
    for i in expression:
        if i.isdigit():
            temp_num += i
        else:
            new_ex.append(temp_num)
            temp_num = ""
            new_ex.append(i)
    print(cases)
    return answer