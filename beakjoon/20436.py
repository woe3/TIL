import sys
keyboard = [
    ['q','w','e','r','t','y','u','i','o','p'],
    ['a','s','d','f','g','h','j','k','l'],
    ['z','x','c','v','b','n','m']    
]
keyboard1 = [
    ['q','w','e','r','t',0,0,0,0,0],
    ['a','s','d','f','g',0,0,0,0],
    ['z','x','c','v',0,0,0]    
]

keyboard2 = [
    [0,0,0,0,0,'y','u','i','o','p'],
    [0,0,0,0,0,'h','j','k','l'],
    [0,0,0,0,'b','n','m']    
]

def find_key(a):
    for i in range(3):
        for j in range(len(keyboard[i])):
            if keyboard[i][j] == a:
                return [i, j]

def time_typing(a, b):
    x1, y1 = a
    x2, y2 = b
    time = abs(x1 - x2) + abs(y1 - y2)
    return time

right, left = sys.stdin.readline().split()
right = find_key(right)
left = find_key(left)
w = sys.stdin.readline().strip()
word = []
for i in w:
    word.append(i)

time = 0
for i in range(len(word)):
    key = find_key(word[i])
    if keyboard1[key[0]][key[1]] != 0:
        tr = time_typing(key, right)
        time += (tr + 1)
        right = key
    else:
        tl = time_typing(key, left)
        time += (tl + 1)
        left = key

    

print(time)