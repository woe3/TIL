import sys

n = int(sys.stdin.readline())
print(2**n-1)
def move (n, s=1, e=3):
    if n == 1:
        print(s,e)
        return
    else:
        move(n-1, s, 6-e-s)
        print(s,e)
        move(n-1, 6-e-s,e)
        
move(n)