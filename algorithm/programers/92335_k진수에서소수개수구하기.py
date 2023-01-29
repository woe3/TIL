#제곱근 판별함수
def check_prime_number(N):
    N = int(N)
    if N < 2:
        return False
    for i in range(2,int(N**(1/2))+1):
        if N%i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    number = ""
    
    #k진수로 변환하면 뒷자리부터 나머지로 나타낼수 있다.
    #따라서  0이 나오면 지금까지 변환된 숫자를 소수인지 판별하고 정답에 숫자를 더한다.
    while True:
        num = n%k
        if not num == 0:
            number = str(num) + number
        else:
            if number == "":
                pass
            elif check_prime_number(number):
                print(number)
                answer += 1
            number = ""
        if n == 0:
            break;
        n = n//k
        
    return answer