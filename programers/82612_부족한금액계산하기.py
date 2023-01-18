def solution(price, money, count):
    payment = 0
    for i in range(1, count+1):
        payment += i * price
    answer = payment - money
    if answer <= 0: return 0
    return answer