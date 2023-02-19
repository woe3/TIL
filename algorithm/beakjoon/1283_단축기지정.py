import  sys
n = int(sys.stdin.readline())
words = []
for _ in range(n):
    w = sys.stdin.readline().strip()
    words.append(w.split(" "))

shortcut = set()

for w in range(len(words)):
    found = False
    for i in range(len(words[w])):
        if not words[w][i][0].upper() in shortcut:
            shortcut.add(words[w][i][0].upper())
            words[w][i] = "["+words[w][i][0]+"]"+words[w][i][1:len(words[w][i])]
            found = True
            break
    if found:
        continue
    for i in range(len(words[w])):
        for j in range(1, len(words[w][i])):
            if not words[w][i][j].upper() in shortcut:
                shortcut.add(words[w][i][j].upper())
                words[w][i] = words[w][i][0:j] + "["+words[w][i][j:j+1]+"]"+words[w][i][j+1:len(words[w][i])]
                found = True
                break
        if found:
            break


for i in words:
    print(" ".join(i))
