import sys
input = sys.stdin.readline
 
V, E = map(int, input().split())
Vroot = [i for i in range(V+1)]
Elist = []
for _ in range(E):
    Elist.append(list(map(int, input().split())))
 
Elist.sort(key=lambda x: x[2])
print(Elist)
print(Vroot)
def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]
 
 
answer = 0
for s, e, w in Elist:
    print(Vroot)
    sRoot = find(s)
    eRoot = find(e)
    print(sRoot)
    print(eRoot)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w
 
print(answer)

