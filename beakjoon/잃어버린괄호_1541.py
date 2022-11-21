import sys
calculation = sys.stdin.readline().strip()

calculation = calculation.split('-')
answer = 0
temp = list(map(int, calculation[0].split('+')))
temp_num = 0
for j in temp:
    temp_num += j
answer += temp_num
for i in range(1, len(calculation)):
    temp = list(map(int, calculation[i].split('+')))
    temp_num = 0
    for j in temp:
        temp_num += j
    answer -= temp_num
    
print(answer)