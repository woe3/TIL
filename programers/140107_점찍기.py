def solution(k, d):
    answer = 0
    
    #최대 길이의 제곱을 계산해둠
    d_square = d**2
    max_val = d//k*k

    #제곱의 dp를 만듬(제곱계산 줄이기)
    sq = [0]*(d+1)
    for i in range(k, d+1, k):
        sq[i] = i**2
    #for문을 k만큼 더해가면서 돌면서 d의 제곱보다 작을때 정답에 더하기1
    #거리가 더 길어 지면 다음 다음 줄으로 넘어감
    #문제! 2중 포문에서 시간초과? 제곱에서 시간초과?
    for i in range(0, d+1, k):
        for j in range(0, d+1, k):
            if sq[max_val - j] + sq[i] <= d_square:
                answer = answer + ((max_val - j)//k) + 1
                break;
                
    return answer 