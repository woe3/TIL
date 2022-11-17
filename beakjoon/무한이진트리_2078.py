import sys
a, b = map(int, sys.stdin.readline().split())

l = 0
r = 0

while a > 1 or b > 1:
    if b > a:
        r += 1
        b -= a
    else:
        l += 1
        a -= b

print(l, end = ' ')
print(r)