import sys
n = int(sys.stdin.readline())

# for문으로 만든 피보나치 수열
fn1 = 0
fn2 = 1

for i in range(n-1):
    temp = fn1
    fn1 = fn2
    fn2 = fn2 + temp
    
print(fn2)


# 함수로 만든 피보나치 수열
def fibo(n, fn1 = 0, fn2 = 1):
    if n == 1:
        return print(fn2)
    else:
        fibo(n-1, fn2, fn1 + fn2)
fibo(n)