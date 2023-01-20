import sys
n = int(sys.stdin.readline())
answer = 0
# five는 설탕배달의 최소 개수이다.
five = n//5

# 5짜리 봉지를 하나씩 줄이면서 3짜리 봉지를 추가 가능한지 확인한다.
for i in range(five+1):
    if (n - ((five-i) * 5)) % 3 == 0:
        answer = (five - i) + (n - ((five-i) * 5)) // 3
        break

# answer이 갱신 되었다면 정답을 출력,
# 아니라면 5,3봉지로 나눌 수 없기 때문에 -1 출력
if answer:
    print(answer)
else: print(-1)
