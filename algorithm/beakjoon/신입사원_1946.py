import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    applicant = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        applicant.append([a, b])
    applicant.sort()
    interview = applicant[0][1]
    answer = 1
    print(applicant)
    for p, i in applicant:
        if i < interview:
            interview = i
            answer += 1
            print([p, i])
    print(answer)