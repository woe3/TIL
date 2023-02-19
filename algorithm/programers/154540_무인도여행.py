import sys

sys.setrecursionlimit(10 ** 5)


def solution(maps):
    len_x = len(maps[0])
    len_y = len(maps)
    for i in range(len_y):
        maps[i] = list(maps[i])

    answer = []

    def dfs(y, x):
        if maps[y][x] == "X":
            return 0
        result = int(maps[y][x])
        maps[y][x] = "X"
        if y < len_y - 1:
            result += dfs(y + 1, x)
        if y > 0:
            result += dfs(y - 1, x)
        if x < len_x - 1:
            result += dfs(y, x + 1)
        if x > 0:
            result += dfs(y, x - 1)
        return result

    for y in range(len_y):
        for x in range(len_x):
            temp_answer = dfs(y, x)
            if temp_answer > 0:
                answer.append(temp_answer)

    answer.sort()
    if not answer:
        answer.append(-1)
    print(answer)
    return answer


solution(["X591X", "X1X5X", "X231X", "1XXX1"])
