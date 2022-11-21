import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    
    dp = [1] + [0] * (m)
    for coin in coins:
        for i in range(1, m+1):
            if i - coin >= 0:
                dp[i] += dp[i-coin]
        print(dp)
    print(dp[-1])

    # 가장 처음 동전으로 만들 수 있는 모든 금액에 해당되는 인덱스를 1로 갱신한다.
    # 두번째부터는 하나의 동전으로 갱신 하지 못 할 때 부족한 금액을 다른 동전으로 만들 수 있었는지 확인!
    # 만들었다면 해 당 되는 금액에 경우의 수 추가!
    