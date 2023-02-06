def solution(n):
    answer = []
    numbers = [i for i in range(int((n + 1) * n / 2), 0, -1)]

    triangle = []
    for num in range(1, n + 1):
        temp = [0] * num
        triangle.append(temp)

    movement = [[1, 0], [0, 1], [-1, -1]]
    y = 0
    x = 0
    move = 0
    while numbers:
        triangle[y][x] = numbers.pop()
        if move == 0:
            if y + 1 > n - 1 or triangle[y + 1][x] > 0:
                move = 1
        elif move == 1:
            if x + 1 > len(triangle[y]) - 1 or triangle[y][x + 1] > 0:
                move = 2
        elif move == 2:
            if triangle[y - 1][x - 1] > 0:
                move = 0
        y += movement[move][0]
        x += movement[move][1]

    for i in triangle:
        answer += i

    return answer


solution(5)
