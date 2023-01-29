import sys

word_1 = sys.stdin.readline().strip()
word_2 = sys.stdin.readline().strip()


sequence_1 = [i for i in word_1]
sequence_2 = [i for i in word_2]
length_1 = len(sequence_1)
length_2 = len(sequence_2)


dp = [0] * length_1
for i in range(length_2):
    save = 0
    for j in range(length_1):
        if dp[j] > save:
            save = dp[j]
        elif sequence_1[j] == sequence_2[i]:
            dp[j] = save + 1
    print(dp)
        

    
print(max(dp))