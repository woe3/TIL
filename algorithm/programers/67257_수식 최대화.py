from itertools import permutations
import copy


def calculator(num1, num2, s):
    if s == "+":
        return num1 + num2
    elif s == "-":
        return num1 - num2
    else:
        return num1 * num2


def solution(expression):
    answer = []

    expression = list(expression)
    new_ex = []

    temp_num = ""
    for j in expression:
        if j.isdigit():
            temp_num += j
        else:
            new_ex.append(int(temp_num))
            temp_num = ""
            new_ex.append(j)

    new_ex.append(int(temp_num))

    cases = list(permutations(["+", "-", "*"]))
    for case in cases:
        temp_ex = new_ex.copy()
        for op in case:
            i = 1

            while i <= (len(temp_ex) - 2):

                if temp_ex[i] == op:
                    temp = calculator(temp_ex[i - 1], temp_ex[i + 1], op)
                    temp_ex[i] = temp
                    temp_ex.pop(i + 1)
                    temp_ex.pop(i - 1)
                    i -= 1

                i += 1

        answer.append(abs(temp_ex[0]))

    return max(answer)


print(solution("100-200*300-500+20"))
