import sys
answer = []
n, m = map(int, sys.stdin.readline().split())
file = {}
folder = {}
for _ in range(n+m):
    a, b, num = sys.stdin.readline().split()
    if int(num) > 0:
        if a in folder:
            folder[a].add(b)
        else: folder[a] = {b}
    else:
        if a in file:
            file[a].add(b)
        else: file[a] = {b}

move = []
k = int(sys.stdin.readline())
for _ in range(k):
    a, b = sys.stdin.readline().split()
    a = a.split('/')[-1]
    b = b.split('/')[-1]
    move.append([a, b])

query = []
q = int(sys.stdin.readline())
for _ in range(q):
    a = sys.stdin.readline().strip()
    a = a.split('/')[-1]
    query.append(a)

for a, z in move:
    if not a in folder:
        pass
    elif not z in folder:
        folder[z] = folder[a]
        del folder[a]
    else:
        folder[z].update(folder[a])
        del folder[a]
    if not a in file:
        pass
    elif not z in file:
        file[z] = file[a]
        del file[a]
    else:
        file[z].update(file[a])
        del file[a]


def collect (x):
    global collection
    global count
    if x in folder:
        for i in folder[x]:
            if i in file:
                collection.update(file[i])
                count += len(file[i])
            if i in folder:
                collect(i)

for a in query:
    if a in file:
        count = len(file[a])
        collection = {0}
        collection.update(file[a])
    else:
        count = 0
        collection = {0}
    collect(a)
    print(len(collection)-1, end = ' ')
    print(count)