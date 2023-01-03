def solution(orders, course):
    answer = []
    alphabet = [0] * 26
    for i in orders:
        for j in i:
            alphabet[ord(j)-65] += 1
    print(alphabet)
    return answer