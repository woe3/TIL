import sys
n = int(sys.stdin.readline())
matrix = []
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    matrix.append(a)
a, b = map(int, sys.stdin.readline().split())
matrix.append(a)
matrix.append(b)

answer = 0

while len(matrix) > 2:
    max_value = 0
    max_index = -1
    for i in range(1, len(matrix)-1):
        if matrix[i] > max_value:
            max_value = matrix[i]
            max_index = i

    cal = matrix[max_index-1] * matrix[max_index] * matrix[max_index+1]
    answer += cal
    matrix = matrix[:max_index] + matrix[max_index+1:]

print(answer)
