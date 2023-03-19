def o_1_algorithm(arr, index):
    return arr[index]


arr = [1, 2, 3, 4, 5, 6]

result = o_1_algorithm(arr, 3)

print(result)  # 4


def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
