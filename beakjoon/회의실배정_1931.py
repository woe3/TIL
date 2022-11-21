import sys
n = int(sys.stdin.readline())
meeting = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    meeting.append([a, b])
meeting.sort(key = lambda x : (x[1], x[0]))
answer = 0
time = 0
for a, b in meeting:
    if a >= time:
        answer += 1
        time = b

print(answer)